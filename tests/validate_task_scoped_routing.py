#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = ROOT / "scoville-scribe-anti-ai-slop"
ROUTE_CONTRACT = ROOT / "tests" / "task-scoped-routing.json"
EVALUATION_CASES = ROOT / "tests" / "evaluation-cases.json"

KNOWN_SKILLS = {
    "scoville-brainstorm",
    "scoville-code-anti-ai-slop",
    "scoville-handoff",
    "scoville-plan",
    "scoville-research",
    "scoville-scribe-anti-ai-slop",
    "scoville-ui-anti-ai-slop",
}
KNOWN_SCRIBE_REFERENCES = {
    "references/fidelity-modes.md",
    "references/interface-text.md",
    "references/prose-patterns.md",
}
REQUIRED_CASES = {
    "ordinary-technical-explanation",
    "routine-status-recap",
    "requested-source-summary",
    "routine-recap-of-prior-answer",
    "domain-code-review",
    "wording-review",
    "research-answer",
    "audience-ready-research-report",
    "documentation-draft",
    "incidental-code-comment",
    "requested-docstring-artifact",
    "incidental-commit-message",
    "requested-commit-copy",
    "source-exact-reproduction",
    "fixed-supplied-insertion",
    "plan-record",
    "plan-rationale-wording",
    "handoff-record",
    "reusable-chat-text",
    "explicit-scribe-invocation",
    "explicit-scribe-opt-out",
    "missing-required-scribe",
    "artifact-follow-up-transformation",
    "pivot-to-ordinary-explanation",
    "ui-implementation-existing-copy",
    "ui-implementation-new-copy",
    "copy-only-ui-wording",
    "brainstorm-directions",
}


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"Expected JSON object: {path}")
    return value


def assert_unique_ids(cases: list[dict[str, object]], source: str) -> set[str]:
    ids = [case.get("id") for case in cases]
    if any(not isinstance(case_id, str) or not case_id for case_id in ids):
        raise AssertionError(f"Missing case id in {source}")
    if len(ids) != len(set(ids)):
        raise AssertionError(f"Duplicate case id in {source}")
    return set(ids)


def main() -> int:
    contract = load_json(ROUTE_CONTRACT)
    if contract.get("schema_version") != 1:
        raise AssertionError("Unsupported route-contract schema")
    if contract.get("decision") != "ADR-0002":
        raise AssertionError("Route contract must bind ADR-0002")

    baseline = contract.get("baseline")
    if not isinstance(baseline, dict) or not baseline:
        raise AssertionError("Missing frozen baseline")
    for key, digest in baseline.items():
        if not isinstance(key, str) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise AssertionError(f"Invalid baseline hash: {key}")

    cases = contract.get("cases")
    if not isinstance(cases, list) or not all(isinstance(case, dict) for case in cases):
        raise AssertionError("Route cases must be objects")
    case_ids = assert_unique_ids(cases, "task-scoped-routing.json")
    if case_ids != REQUIRED_CASES:
        missing = sorted(REQUIRED_CASES - case_ids)
        extra = sorted(case_ids - REQUIRED_CASES)
        raise AssertionError(f"Route-case inventory drift: missing={missing} extra={extra}")

    for case in cases:
        case_id = str(case["id"])
        skills = case.get("target_skills")
        references = case.get("target_scribe_references")
        forbidden = case.get("forbidden_scoville_skills")
        hard_checks = case.get("hard_checks")
        if not isinstance(skills, list) or any(skill not in KNOWN_SKILLS for skill in skills):
            raise AssertionError(f"Unknown target Skill in {case_id}")
        if len(skills) != len(set(skills)):
            raise AssertionError(f"Duplicate target Skill in {case_id}")
        if not isinstance(references, list) or any(reference not in KNOWN_SCRIBE_REFERENCES for reference in references):
            raise AssertionError(f"Unknown Scribe reference in {case_id}")
        if references and "scoville-scribe-anti-ai-slop" not in skills:
            raise AssertionError(f"Scribe reference without Scribe Core in {case_id}")
        if not isinstance(forbidden, list) or any(skill not in KNOWN_SKILLS for skill in forbidden):
            raise AssertionError(f"Unknown forbidden Skill in {case_id}")
        if set(skills) & set(forbidden):
            raise AssertionError(f"Skill both required and forbidden in {case_id}")
        if not isinstance(hard_checks, list) or not hard_checks:
            raise AssertionError(f"Missing hard checks in {case_id}")
        if case.get("delivery") not in {"chat", "file", "commit"}:
            raise AssertionError(f"Unsupported delivery surface in {case_id}")
        if not isinstance(case.get("reuse_intent"), bool):
            raise AssertionError(f"Missing reuse intent in {case_id}")

    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    required_skill_fragments = (
        "## Activate only for text artifacts",
        "Do not activate Scribe for ordinary answers",
        "Chat,\nfile, commit, or other delivery alone neither activates nor suppresses Scribe.",
        "A domain owner's normal result does not add\nScribe",
        "referential\nfollow-up transformation",
        "pivot to\nordinary explanation does not inherit it",
        "uninvoked fixed insertion",
        "`scoville-research` source-backed research and synthesis",
    )
    for fragment in required_skill_fragments:
        if fragment not in skill_text:
            raise AssertionError(f"Missing Skill routing fragment: {fragment}")

    description = next(
        line.split(":", 1)[1].strip()
        for line in skill_text.splitlines()
        if line.startswith("description:")
    )
    for fragment in ("wording itself is the deliverable", "ordinary conversation", "uninvoked fixed insertion"):
        if fragment not in description:
            raise AssertionError(f"Description misses activation boundary: {fragment}")

    evaluation = load_json(EVALUATION_CASES)
    evaluation_cases = evaluation.get("cases")
    if not isinstance(evaluation_cases, list) or not all(isinstance(case, dict) for case in evaluation_cases):
        raise AssertionError("Evaluation cases must be objects")
    evaluation_ids = assert_unique_ids(evaluation_cases, "evaluation-cases.json")
    if "technical-collaboration-capabilities-and-limits" not in evaluation_ids:
        raise AssertionError("Missing conversational negative fixture")
    technical = next(case for case in evaluation_cases if case["id"] == "technical-collaboration-capabilities-and-limits")
    if "Do not activate Scribe" not in " ".join(technical.get("expect", [])):
        raise AssertionError("Technical collaboration remains a positive Scribe fixture")

    print(
        json.dumps(
            {
                "status": "passed",
                "route_cases": len(cases),
                "evaluation_cases": len(evaluation_cases),
                "skill_sha256": hashlib.sha256((SKILL_ROOT / "SKILL.md").read_bytes()).hexdigest(),
                "route_contract_sha256": hashlib.sha256(ROUTE_CONTRACT.read_bytes()).hexdigest(),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
