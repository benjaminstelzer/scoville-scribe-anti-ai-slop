# Task-scoped routing qualification

This evaluation binds the task-scoped routing candidate to the frozen prompt,
Skill, sibling-package, case, and harness hashes in `manifest.json`.

## Result

The original 21-run comparison in `report.json` is retained with status
`reject`. It exposed two test-harness defects rather than two candidate routing
defects:

- the ordinary case tested a meta-routing question, so both current and
  candidate prompts correctly selected no Skill;
- the UI expectation contradicted the case's required catalog order.

`correction-manifest.json` freezes the only permitted corrections and binds
them to the original report hash. The three correction runs adopt the exact
candidate:

- ordinary communication returned the required result with zero Skill reads;
- the mixed UI implementation selected Code, Scribe, and UI in catalog order,
  with only Scribe's Interface reference;
- both candidate gates passed.

The direct resource comparison remains **unproven** because the current and
candidate prompts both used zero Skill reads in the corrected ordinary case.
One repetition per cell also makes latency observational only. No token or
latency reduction is claimed from this suite.

## Evidence

- `report.json`: immutable original result, SHA-256
  `0f02dd1fba9b1106ef5b2c295fefaf0dc54857d958889054989a0df21f87d521`
- `correction-report.json`: adopted correction result, SHA-256
  `db09fa7c5fd6ea3206edc2f96926bfd6c7c48fdfd160598b51bd936b5a2672a8`
- candidate prompt SHA-256
  `23d2fb6bc06cd1ad68af05e2a4cb8391971219dd936d3d1c5a7411acb2cad899`
- candidate Scribe Core SHA-256
  `bf725f1609a2b6b61742200f55ed82a3a231129b47ac2dfb61674cb94b692426`

Run summaries and JSONL traces retain the observed routing and usage records.
Disposable Codex state databases are intentionally excluded.
