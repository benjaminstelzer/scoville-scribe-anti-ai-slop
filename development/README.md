# Development

The only installable package is [`scoville-scribe-anti-ai-slop/`](../scoville-scribe-anti-ai-slop/). Current routing and regression cases in this directory are not installed with the Skill.

## Validate

Run the task-scoped routing checks from the repository root:

```text
python -B development/tests/validate_task_scoped_routing.py
```

Deterministic routing cases do not establish perfect factual fidelity, style quality, or authorship detection.

## Retention

Keep current routing tests, regression inputs, and this maintenance summary. Create model outputs, comparison runs, correction reports, audits, and reviews in temporary storage. Retain evaluation evidence only as a concise repository-owned summary when a published release links it.
