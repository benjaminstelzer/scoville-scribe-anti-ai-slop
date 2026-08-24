#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_ROOT))
import run_qualification as q  # noqa: E402


ROOT = SCRIPT_ROOT.parent
CORRECTION_ROOT = ROOT / "correction-runs"


def ordinary_case_text() -> str:
    return """# Ordinary technical answer case

The retry loop waits 120 milliseconds between attempts and permits 16 attempts.
Functional tests pass. CPU cost on very large pages has not been measured.

Answer the user's ordinary conversational question: what is the maximum retry
window, what remains unknown, and what is the cheapest check that would resolve
that unknown? This answer is not intended for copying or publication.

Return exactly this JSON shape with no additional text:

```json
{
  "maximum_window_seconds": 1.92,
  "cpu_cost_status": "unmeasured",
  "next_check": "measure CPU on representative large pages"
}
```
"""


def ordinary_prompt(catalog: list[dict[str, str]]) -> str:
    entries = "\n".join(f"- `{item['logical_id']}`: {item['description']}" for item in catalog)
    return f"""You are one isolated execution run.

Available Scoville Skills (metadata only):

{entries}

Read `CASE.md` with `scoville_eval.read_fixture`, then perform the requested
task. Activate only Skills that genuinely apply to the user's actual request.
Read each activated Core exactly once and only its directly required references.
Some ordinary requests require no Skill. Use only `scoville_eval` tools; do not
seek shell, memory, network, browser, host files, or external evidence. Do not
modify files. Return exactly the requested JSON object with no commentary.
"""


def prepare_ordinary(condition: str, ordinal: int, manifest: dict[str, Any]) -> Path:
    run_root = CORRECTION_ROOT / f"{ordinal:03d}-ordinary-real--{condition}"
    run_root.mkdir(parents=True)
    fixture_root = run_root / "fixture"
    model_root = run_root / "model"
    state_root = run_root / "state"
    fixture_root.mkdir()
    model_root.mkdir()
    state_root.mkdir()
    q.write_text(fixture_root / "CASE.md", ordinary_case_text())
    catalog, skill_files = q.snapshot_catalog(condition, model_root)
    q.write_json(run_root / "private-control.json", {"schema_version": 1, "skill_files": skill_files})
    q.write_text(run_root / "prompt.md", ordinary_prompt(catalog))
    instructions = q.prompt_body(q.CURRENT_PROMPT if condition == "current" else q.CANDIDATE_PROMPT)
    q.model_catalog(run_root / "model-catalog.json", instructions)
    answer_expected = {
        "maximum_window_seconds": 1.92,
        "cpu_cost_status": "unmeasured",
        "next_check": "measure CPU on representative large pages",
    }
    q.write_json(
        run_root / "run-manifest.json",
        {
            "schema_version": 1,
            "run_id": run_root.name,
            "ordinal": ordinal,
            "case_id": "ordinary-real",
            "condition": condition,
            "model": manifest["model"],
            "reasoning_effort": manifest["reasoning_effort"],
            "expected": {"skills": [], "scribe_references": []},
            "answer_expected": answer_expected,
            "catalog": [item["name"] for item in catalog],
            "prompt_sha256": q.sha256(run_root / "prompt.md"),
            "case_sha256": q.sha256(fixture_root / "CASE.md"),
            "model_catalog_sha256": q.sha256(run_root / "model-catalog.json"),
            "configured_skill_files": sorted(skill_files),
        },
    )
    return run_root


def prepare_ui(ordinal: int, manifest: dict[str, Any]) -> Path:
    cases = json.loads((ROOT / "cases.json").read_text(encoding="utf-8"))["cases"]
    case = next(item for item in cases if item["id"] == "ui-implementation-new-copy")
    corrected = json.loads(json.dumps(case))
    corrected["expected"]["candidate"]["skills"] = [
        "scoville-code-anti-ai-slop",
        "scoville-scribe-anti-ai-slop",
        "scoville-ui-anti-ai-slop",
    ]
    run_root = q.prepare_run(ordinal, corrected, "candidate", manifest)
    target = CORRECTION_ROOT / f"{ordinal:03d}-ui-order--candidate"
    run_root.rename(target)
    run_manifest_path = target / "run-manifest.json"
    run_manifest = json.loads(run_manifest_path.read_text(encoding="utf-8"))
    run_manifest["run_id"] = target.name
    run_manifest["case_id"] = "ui-order"
    q.write_json(run_manifest_path, run_manifest, exclusive=False)
    return target


def finalize_ordinary(run_root: Path, summary: dict[str, Any]) -> dict[str, Any]:
    expected = json.loads((run_root / "run-manifest.json").read_text(encoding="utf-8"))["answer_expected"]
    summary["quality_pass"] = summary["final_json"] == expected
    summary["routing_pass"] = not summary["core_reads"] and not summary["scribe_reference_reads"]
    summary["combined_pass"] = summary["quality_pass"] and summary["routing_pass"] and summary["delivery_pass"]
    q.write_json(run_root / "summary.json", summary, exclusive=False)
    return summary

def main() -> int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    correction = json.loads((ROOT / "correction-manifest.json").read_text(encoding="utf-8"))
    parent_hash = q.sha256(ROOT / "report.json")
    if correction["parent_report_sha256"] != parent_hash:
        raise RuntimeError(
            f"Parent report hash mismatch: expected={correction['parent_report_sha256']} actual={parent_hash}"
        )
    if CORRECTION_ROOT.exists() and any(CORRECTION_ROOT.iterdir()):
        raise RuntimeError("Correction runs already exist; preserve evidence")
    CORRECTION_ROOT.mkdir(exist_ok=True)
    timeout = int(manifest["timeout_seconds_per_run"])

    current_root = prepare_ordinary("current", 1, manifest)
    print(f"SCOVILLE_CORRECTION_PROGRESS 1/3 {current_root.name}", flush=True)
    current = finalize_ordinary(current_root, q.execute(current_root, timeout))

    candidate_root = prepare_ordinary("candidate", 2, manifest)
    print(f"SCOVILLE_CORRECTION_PROGRESS 2/3 {candidate_root.name}", flush=True)
    candidate = finalize_ordinary(candidate_root, q.execute(candidate_root, timeout))

    ui_root = prepare_ui(3, manifest)
    print(f"SCOVILLE_CORRECTION_PROGRESS 3/3 {ui_root.name}", flush=True)
    ui = q.execute(ui_root, timeout)

    gates = {
        "ordinary_candidate": candidate["combined_pass"],
        "ordinary_comparison": len(candidate["successful_skill_reads"]) < len(current["successful_skill_reads"]),
        "ui_candidate": ui["combined_pass"],
    }
    report = {
        "schema_version": 1,
        "suite": correction["suite"],
        "status": "adopt" if gates["ordinary_candidate"] and gates["ui_candidate"] else "reject",
        "comparative_resource_claim": "supported" if gates["ordinary_comparison"] else "unproven",
        "gates": gates,
        "runs": [
            {
                "run_id": row["run_id"],
                "combined_pass": row["combined_pass"],
                "reads": row["successful_skill_reads"],
                "usage": row["usage"],
                "elapsed_seconds": row["elapsed_seconds"],
                "summary_sha256": q.sha256(CORRECTION_ROOT / row["run_id"] / "summary.json"),
            }
            for row in (current, candidate, ui)
        ],
    }
    q.write_json(ROOT / "correction-report.json", report)
    print(json.dumps(report, indent=2), flush=True)
    return 0 if report["status"] == "adopt" else 2


if __name__ == "__main__":
    raise SystemExit(main())
