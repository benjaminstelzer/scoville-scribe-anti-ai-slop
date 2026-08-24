#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ROOT.parents[2]
WORKSPACE = Path("Z:/Projekts/AI")
CODEX = WORKSPACE / "codex-runtime/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe"
BASE_MODEL_CATALOG = WORKSPACE / "docs/evaluations/scoville-skills-full-suite-v1/control/model-catalog.json"
BROKER_RUNNER = WORKSPACE / "docs/evaluations/scoville-skills-full-suite-v1/scripts/broker_runner.py"
EVAL_BROKER = WORKSPACE / "docs/evaluations/scoville-skills-full-suite-v1/scripts/eval_broker.py"
CURRENT_PROMPT = Path("C:/Users/benja/.codex/model-instructions/gpt-5.6-sol-system-prompt-fable-like.md")
CANDIDATE_PROMPT = WORKSPACE / "codex-fable-like-system-prompt-for-gpt-5.6-sol/gpt-5.6-sol-system-prompt-fable-like.md"
CURRENT_SCRIBE = Path("C:/Users/benja/.codex/skills/scoville-scribe-anti-ai-slop")
CANDIDATE_SCRIBE = REPO_ROOT / "scoville-scribe-anti-ai-slop"
OTHER_SKILLS = {
    "scoville-brainstorm": Path("C:/Users/benja/.codex/skills/scoville-brainstorm"),
    "scoville-code-anti-ai-slop": Path("C:/Users/benja/.codex/skills/scoville-code-anti-ai-slop"),
    "scoville-handoff": Path("C:/Users/benja/.codex/skills/scoville-handoff"),
    "scoville-plan": Path("C:/Users/benja/.codex/skills/scoville-plan"),
    "scoville-research": Path("C:/Users/benja/.codex/skills/scoville-research"),
    "scoville-ui-anti-ai-slop": Path("C:/Users/benja/.codex/skills/scoville-ui-anti-ai-slop"),
}
CONDITIONS = ("no_skill", "current", "candidate")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()


def write_json(path: Path, value: Any, *, exclusive: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "x" if exclusive else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_text(path: Path, value: str, *, exclusive: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "x" if exclusive else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        handle.write(value)


def parse_description(skill_path: Path) -> str:
    for line in skill_path.read_text(encoding="utf-8").splitlines()[1:]:
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip()
        if line == "---":
            break
    raise ValueError(f"Missing Skill description: {skill_path}")


def prompt_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.find("You are Codex")
    if start < 0:
        raise ValueError(f"Prompt body marker missing: {path}")
    return text[start:]


def model_catalog(path: Path, instructions: str) -> None:
    catalog = json.loads(BASE_MODEL_CATALOG.read_text(encoding="utf-8"))
    target = next(model for model in catalog["models"] if model.get("slug") == "gpt-5.6-sol")
    target["base_instructions"] = instructions
    target["instructions_template"] = instructions
    if isinstance(target.get("model_messages"), dict):
        target["model_messages"]["instructions_template"] = instructions
    write_json(path, catalog)


def skill_sources(condition: str) -> dict[str, Path]:
    if condition == "no_skill":
        return {}
    sources = dict(OTHER_SKILLS)
    sources["scoville-scribe-anti-ai-slop"] = CURRENT_SCRIBE if condition == "current" else CANDIDATE_SCRIBE
    return dict(sorted(sources.items()))


def snapshot_catalog(condition: str, model_root: Path) -> tuple[list[dict[str, str]], dict[str, str]]:
    catalog: list[dict[str, str]] = []
    mapping: dict[str, str] = {}
    for name, source in skill_sources(condition).items():
        if not (source / "SKILL.md").is_file():
            raise FileNotFoundError(source / "SKILL.md")
        target = model_root / "catalog" / name
        shutil.copytree(source, target)
        core_id = f"{name}/SKILL.md"
        mapping[core_id] = f"catalog/{name}/SKILL.md"
        catalog.append(
            {
                "logical_id": core_id,
                "name": name,
                "description": parse_description(source / "SKILL.md"),
            }
        )
        reference_root = source / "references"
        if reference_root.is_dir():
            for reference in sorted(reference_root.glob("*.md")):
                logical_id = f"{name}/references/{reference.name}"
                mapping[logical_id] = f"catalog/{name}/references/{reference.name}"
    return catalog, mapping


def case_text(case: dict[str, Any]) -> str:
    return f"""# Routing case: {case['id']}

## Scenario

{case['scenario']}

## Question

Decide which available Scoville Skill Cores apply to this task and which Scribe
references apply if Scribe is selected. Do not perform the described task.

Return exactly one JSON object with these keys in order and no additional text:

```json
{{
  "skills": ["zero or more available Skill names in catalog order"],
  "scribe_references": ["zero or more Scribe reference paths in Core routing order"]
}}
```
"""


def run_prompt(catalog: list[dict[str, str]]) -> str:
    if catalog:
        entries = "\n".join(f"- `{item['logical_id']}`: {item['description']}" for item in catalog)
        routing = f"""Available Scoville Skills (metadata only):

{entries}

First read `CASE.md` with `scoville_eval.read_fixture`. Select only the Skills
that genuinely apply. Read each selected Core exactly once with
`scoville_eval.read_skill`, then read only its directly required references.
Some cases intentionally require no Skill; read nothing else for those cases."""
    else:
        routing = """No Scoville Skill is available in this condition. Read `CASE.md`
with `scoville_eval.read_fixture`, select no Skill, and return empty arrays."""
    return f"""You are one isolated routing-qualification run.

{routing}

Use only `scoville_eval` tools. Do not seek shell, memory, network, browser,
repository history, host files, other Skills, or external evidence. Do not
modify files. Your final response must be exactly one JSON object with no code
fence, preamble, explanation, or trailing text.
"""


def prepare_run(ordinal: int, case: dict[str, Any], condition: str, manifest: dict[str, Any]) -> Path:
    run_id = f"{ordinal:03d}-{case['id']}--{condition}"
    run_root = ROOT / "runs" / run_id
    run_root.mkdir(parents=True)
    fixture_root = run_root / "fixture"
    model_root = run_root / "model"
    state_root = run_root / "state"
    fixture_root.mkdir()
    model_root.mkdir()
    state_root.mkdir()
    write_text(fixture_root / "CASE.md", case_text(case))
    catalog, skill_files = snapshot_catalog(condition, model_root)
    write_json(run_root / "private-control.json", {"schema_version": 1, "skill_files": skill_files})
    write_text(run_root / "prompt.md", run_prompt(catalog))
    instructions = prompt_body(CANDIDATE_PROMPT if condition in {"candidate", "no_skill"} else CURRENT_PROMPT)
    model_catalog(run_root / "model-catalog.json", instructions)
    expected = case["expected"][condition]
    write_json(
        run_root / "run-manifest.json",
        {
            "schema_version": 1,
            "run_id": run_id,
            "ordinal": ordinal,
            "case_id": case["id"],
            "condition": condition,
            "model": manifest["model"],
            "reasoning_effort": manifest["reasoning_effort"],
            "expected": expected,
            "catalog": [item["name"] for item in catalog],
            "prompt_sha256": sha256(run_root / "prompt.md"),
            "case_sha256": sha256(fixture_root / "CASE.md"),
            "model_catalog_sha256": sha256(run_root / "model-catalog.json"),
            "configured_skill_files": sorted(skill_files),
        },
    )
    return run_root


def json_lines(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def summarize(run_root: Path, elapsed: float, exit_code: int) -> dict[str, Any]:
    run_manifest = json.loads((run_root / "run-manifest.json").read_text(encoding="utf-8"))
    events = json_lines(run_root / "rollout.jsonl")
    reads: list[str] = []
    attempted_reads: list[str | None] = []
    tool_failures: list[dict[str, Any]] = []
    usage: dict[str, int] = {}
    provider_calls = 0
    tool_turns = 0
    for event in events:
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            provider_calls += 1
            usage = {key: int(value) for key, value in event["usage"].items() if isinstance(value, int)}
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "mcp_tool_call":
            continue
        tool = str(item.get("tool", ""))
        arguments = item.get("arguments") if isinstance(item.get("arguments"), dict) else {}
        logical_id = arguments.get("logical_id") if isinstance(arguments.get("logical_id"), str) else None
        if event.get("type") == "item.started" and tool == "read_skill":
            attempted_reads.append(logical_id)
        if event.get("type") != "item.completed":
            continue
        tool_turns += 1
        if item.get("status") == "failed" or item.get("error"):
            tool_failures.append({"tool": tool, "logical_id": logical_id, "error": item.get("error") or item.get("result")})
        elif tool == "read_skill" and logical_id:
            reads.append(logical_id)

    final_path = run_root / "final.txt"
    final_text = final_path.read_text(encoding="utf-8").strip() if final_path.is_file() else ""
    try:
        final_json = json.loads(final_text)
    except json.JSONDecodeError:
        final_json = None
    expected = run_manifest["expected"]
    expected_cores = [f"{name}/SKILL.md" for name in expected["skills"]]
    expected_scribe_refs = [f"scoville-scribe-anti-ai-slop/{path}" for path in expected["scribe_references"]]
    actual_cores = [logical_id for logical_id in reads if logical_id.endswith("/SKILL.md")]
    actual_scribe_refs = [logical_id for logical_id in reads if logical_id.startswith("scoville-scribe-anti-ai-slop/references/")]
    quality_pass = final_json == expected
    routing_pass = (
        actual_cores == expected_cores
        and actual_scribe_refs == expected_scribe_refs
        and all(actual_cores.count(core) == 1 for core in expected_cores)
        and all(actual_scribe_refs.count(reference) == 1 for reference in expected_scribe_refs)
    )
    delivery_pass = exit_code == 0 and bool(usage) and not tool_failures and isinstance(final_json, dict)
    total_input = usage.get("input_tokens", 0)
    cached_input = usage.get("cached_input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)
    summary = {
        **run_manifest,
        "exit_code": exit_code,
        "elapsed_seconds": round(elapsed, 3),
        "attempted_skill_reads": attempted_reads,
        "successful_skill_reads": reads,
        "core_reads": actual_cores,
        "scribe_reference_reads": actual_scribe_refs,
        "tool_failures": tool_failures,
        "tool_turns": tool_turns,
        "provider_model_calls": provider_calls,
        "usage": {
            **usage,
            "uncached_input_tokens": total_input - cached_input,
            "provider_total_tokens": total_input + output_tokens,
        },
        "final_json": final_json,
        "quality_pass": quality_pass,
        "routing_pass": routing_pass,
        "delivery_pass": delivery_pass,
        "combined_pass": quality_pass and routing_pass and delivery_pass,
        "rollout_sha256": sha256(run_root / "rollout.jsonl"),
        "final_sha256": sha256(final_path) if final_path.is_file() else None,
    }
    write_json(run_root / "summary.json", summary)
    return summary


def execute(run_root: Path, timeout_seconds: int) -> dict[str, Any]:
    control = json.loads((run_root / "private-control.json").read_text(encoding="utf-8"))
    command = [
        sys.executable,
        str(BROKER_RUNNER),
        "--codex-cli", str(CODEX),
        "--broker", str(EVAL_BROKER),
        "--broker-control", str(run_root / "private-control.json"),
        "--model-catalog", str(run_root / "model-catalog.json"),
        "--model-root", str(run_root / "model"),
        "--fixture-root", str(run_root / "fixture"),
        "--state-root", str(run_root / "state"),
        "--prompt", str(run_root / "prompt.md"),
        "--jsonl", str(run_root / "rollout.jsonl"),
        "--stderr", str(run_root / "stderr.txt"),
        "--skill-inventory", str(run_root / "skill-inventory.json"),
        "--final-output", str(run_root / "final.txt"),
        "--model", "gpt-5.6-sol",
        "--reasoning-effort", "medium",
        "--timeout-seconds", str(timeout_seconds),
        "--allowed-broker-tool", "read_fixture",
        "--allowed-broker-tool", "list_fixture",
    ]
    if control["skill_files"]:
        command.extend(("--allowed-broker-tool", "read_skill"))
        for logical_id in sorted(control["skill_files"]):
            command.extend(("--allowed-skill-read", logical_id))
    started = time.monotonic()
    completed = subprocess.run(command, cwd=ROOT, check=False)
    return summarize(run_root, time.monotonic() - started, completed.returncode)


def verify_inputs(manifest: dict[str, Any]) -> None:
    checks = {
        CODEX: manifest["host"]["codex_cli_sha256"],
        BASE_MODEL_CATALOG: manifest["host"]["model_catalog_sha256"],
        BROKER_RUNNER: manifest["host"]["broker_runner_sha256"],
        EVAL_BROKER: manifest["host"]["eval_broker_sha256"],
        CURRENT_PROMPT: manifest["prompt_hashes"]["current"],
        CANDIDATE_PROMPT: manifest["prompt_hashes"]["candidate"],
    }
    for path, expected in checks.items():
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"Frozen input drift: {path} expected={expected} actual={actual}")


def aggregate(summaries: list[dict[str, Any]], manifest: dict[str, Any]) -> dict[str, Any]:
    conditions: dict[str, Any] = {}
    for condition in CONDITIONS:
        rows = [summary for summary in summaries if summary["condition"] == condition]
        conditions[condition] = {
            "calls": len(rows),
            "quality_passes": sum(bool(row["quality_pass"]) for row in rows),
            "routing_passes": sum(bool(row["routing_pass"]) for row in rows),
            "delivery_passes": sum(bool(row["delivery_pass"]) for row in rows),
            "combined_passes": sum(bool(row["combined_pass"]) for row in rows),
            "core_reads": sum(len(row["core_reads"]) for row in rows),
            "scribe_reference_reads": sum(len(row["scribe_reference_reads"]) for row in rows),
            "provider_total_tokens": sum(row["usage"].get("provider_total_tokens", 0) for row in rows),
            "uncached_input_tokens": sum(row["usage"].get("uncached_input_tokens", 0) for row in rows),
            "output_tokens": sum(row["usage"].get("output_tokens", 0) for row in rows),
            "elapsed_seconds_median": statistics.median(row["elapsed_seconds"] for row in rows),
        }
    candidate_rows = [summary for summary in summaries if summary["condition"] == "candidate"]
    ordinary_current = next(summary for summary in summaries if summary["condition"] == "current" and summary["case_id"] == "ordinary-technical-explanation")
    ordinary_candidate = next(summary for summary in candidate_rows if summary["case_id"] == "ordinary-technical-explanation")
    gates = {
        "candidate_all_combined": all(row["combined_pass"] for row in candidate_rows),
        "ordinary_candidate_zero_reads": not ordinary_candidate["successful_skill_reads"],
        "ordinary_reads_lower_than_current": len(ordinary_candidate["successful_skill_reads"]) < len(ordinary_current["successful_skill_reads"]),
    }
    report = {
        "schema_version": 1,
        "suite": manifest["suite"],
        "status": "adopt" if all(gates.values()) else "reject",
        "interpretation": manifest["interpretation"],
        "gates": gates,
        "conditions": conditions,
        "runs": [
            {
                "run_id": row["run_id"],
                "condition": row["condition"],
                "case_id": row["case_id"],
                "combined_pass": row["combined_pass"],
                "core_reads": row["core_reads"],
                "scribe_reference_reads": row["scribe_reference_reads"],
                "usage": row["usage"],
                "elapsed_seconds": row["elapsed_seconds"],
                "summary_sha256": sha256(ROOT / "runs" / row["run_id"] / "summary.json"),
            }
            for row in summaries
        ],
    }
    return report


def main() -> int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    cases = json.loads((ROOT / "cases.json").read_text(encoding="utf-8"))["cases"]
    if len(cases) != 7 or len({case["id"] for case in cases}) != 7:
        raise RuntimeError("Expected seven unique frozen cases")
    verify_inputs(manifest)
    runs_root = ROOT / "runs"
    if runs_root.exists() and any(runs_root.iterdir()):
        raise RuntimeError("Runs already exist; preserve evidence and use a new suite")
    runs_root.mkdir(exist_ok=True)
    summaries: list[dict[str, Any]] = []
    ordinal = 0
    for case in cases:
        for condition in CONDITIONS:
            ordinal += 1
            run_root = prepare_run(ordinal, case, condition, manifest)
            print(f"SCOVILLE_ROUTING_PROGRESS {ordinal}/21 {run_root.name}", flush=True)
            summary = execute(run_root, int(manifest["timeout_seconds_per_run"]))
            summaries.append(summary)
            print(
                json.dumps(
                    {
                        "run": summary["run_id"],
                        "combined_pass": summary["combined_pass"],
                        "reads": summary["successful_skill_reads"],
                        "elapsed_seconds": summary["elapsed_seconds"],
                    }
                ),
                flush=True,
            )
    report = aggregate(summaries, manifest)
    write_json(ROOT / "report.json", report)
    print(json.dumps(report, indent=2), flush=True)
    return 0 if report["status"] == "adopt" else 2


if __name__ == "__main__":
    raise SystemExit(main())
