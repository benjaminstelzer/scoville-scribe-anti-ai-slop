---
format_version: 1
id: PLAN-0001
status: completed
created: 2026-08-24
updated: 2026-08-24
---

# Task-scoped Scoville Skill routing

## Goal

Reduce avoidable token use and latency by loading only the smallest task-relevant Skill set while preserving automatic specialist support: ordinary conversation uses the compact system prompt, Scribe owns requested text artifacts and transformations, Code owns coding work, UI owns interface work, and mixed tasks compose only the owners required by each segment.

## Non-goals

- Do not remove automatic Skill activation, the available-Skill catalog, or any specialist's existing authority when it is applicable.
- Do not weaken Scribe's truth, terminology, localization, interface-text, source-exact, or artifact-fidelity guarantees.
- Do not change the model, reasoning effort, safety rules, tool permissions, or unrelated Codex behavior.
- Do not treat lower token counts or fewer calls as success when task quality or required evidence regresses.
- Creation of this Plan does not authorize implementation, installation, commits, pushes, releases, publication, or changes to unrelated repositories.

## Work items

### W-001 Narrow Scribe to requested text artifacts and transformations

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: The canonical Scribe package activates for wording artifacts, transformations, and explicitly requested Scribe work but stays inactive for ordinary conversation, explanations, status, analysis, and final framing.
Acceptance: Before edits, a frozen route table binds every case to task and segment classification, exact Skill set, exact Scribe reference set, hard output requirements, negative reads, delivery surface, and reuse intent; Scribe's frontmatter, Core activation gate, Prose selector, README, changelog, and routing fixtures implement the accepted table; normal-chat cases read no Scribe file; writing, localization, source-exact, and interface-copy cases load exactly the required routes; every existing case that moves or changes polarity is enumerated; historical benchmark claims remain bound to their original package; all retained artifact-fidelity cases pass; multi-turn pivot, opt-out, missing-Skill, and mixed-segment cases pass.
Steps:
1. Resolve ADR-0002 and freeze the route table for summaries, recaps, reports, reviews, documentation, comments, docstrings, commit and PR text, source-exact work, fixed insertion, domain-owned records, reusable chat-delivered text, explicit invocation, opt-out, missing Skills, and multi-turn pivots.
2. Inventory current positive, negative, mixed-task, and conversational routes and freeze the baseline package, case polarity, evaluator inputs, and historical evidence bindings.
3. Replace generic prose activation with the accepted artifact-or-transformation gate and define explicit invocation, domain-owner, cross-host, and mixed-segment behavior.
4. Move conversational explanation quality checks to the system-prompt suite while retaining artifact Prose, Fidelity, and Interface behavior.
5. Update public documentation, changelog, historical-evidence scope, and focused routing fixtures without weakening existing integrity constraints.
6. Run the canonical validator and focused Scribe routing and artifact-fidelity evaluations.
Evidence: [quick_validate.py passed on the candidate Scribe package, task-scoped routing validation passed 28 route cases and 12 evaluation cases, Fidelity and Interface references remain byte-identical to baseline, Scribe repository diff check passed]

### W-002 Align the global system prompt with minimal silent Skill routing

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: The GPT-5.6 Sol system prompt routes only the smallest applicable Skill set, delegates Scribe only for artifact-bound wording, composes mixed tasks per segment, and does not announce routine Skill selection or loading.
Acceptance: The Personality routing rule and complete owner maps match the qualified route table, including Research; one explicitly approved replacement suppresses routine selection, order, skipped-Skill, variant, action, and influence narration while preserving requested, unavailable, pause, blocker, scope, risk, and external-effect reporting; the candidate Using skills section matches its approved SHA-256; the original upstream snapshot and original Skills section remain pinned; every section marker is unique and ordered; all text outside Personality and the approved fixed Skills delta remains byte-identical to upstream; one-byte negative mutations in preserved mechanics, neighboring sections, and the preamble fail; prompt documentation names exactly two modified regions; optimizer scope remains Personality-only.
Steps:
1. Replace the broad prose-and-fidelity Scribe route with the qualified artifact-or-transformation boundary.
2. Align every Scoville owner map, including Research, and state that a domain owner's normal result does not activate Scribe without an independent wording or fidelity trigger.
3. Predeclare the exact upstream-to-candidate replacement for every affected Skill-disclosure clause and obtain prompt-owner acceptance of that exact text.
4. Update the boundary verifier to pin the complete approved candidate Skills section, preserve the original upstream hashes, assert unique ordered markers, and reject mutations outside the fixed delta.
5. Update prompt documentation, upstream-refresh instructions, SkillOpt boundary language, and changelog without claiming deterministic model behavior.
6. Run boundary, negative-mutation, diff, format, and prompt-routing checks.
Evidence: [candidate Skills section pinned at SHA-256 9fef18f7450eeec0e162d71c50a73b587d920e815a309a1d1ab9f0669d73a51b, upstream and protected boundary verifier passed, five one-mutation boundary cases were rejected, prompt repository diff check passed]

### W-003 Qualify routing quality, tokens, calls, and latency end to end

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: A frozen comparison establishes whether the candidate removes unnecessary Skill loads and improves resource use without losing conversational quality, artifact fidelity, engineering ownership, or mixed-task completeness.
Acceptance: Before any run, a qualification manifest pins current and candidate prompt and package hashes, sibling Skill descriptions and package hashes, case corpus, expected routes, hard checks, negative reads, evaluator and harness hashes, host version, models, efforts, provider settings, catalog exposure, read and call definitions, no-Skill semantics, cache strata, run order, repetitions, timeout handling, latency boundaries, non-inferiority thresholds, open development cases, and untouched adoption cases; separate no-Skill, current, and candidate arms follow that manifest; results record attempted, failed, successful, and duplicate Core and reference reads, retries, tool turns, provider model calls, input, cached, output, and total tokens, wall-clock latency, and hard-result judgments; ordinary conversation has zero unnecessary Scoville reads; specialist and mixed tasks route exactly their required owners; every predeclared quality and resource gate passes before adoption; raw traces and the final report are hash-bound.
Steps:
1. Freeze the complete route table and representative ordinary-chat, ambiguous-text, artifact, code, UI, mixed-copy, explicit-invocation, opt-out, missing-Skill, multi-turn, planning, research, and handoff cases with expected routes and hard results.
2. Pre-register the qualification manifest, non-inferiority gates, models, efforts, cache treatment, repetitions, interleaved run order, timeout handling, latency clocks, and sealed adoption split before observing candidate results.
3. Run isolated no-Skill, current, and candidate arms without inherited Skills, memories, or unrelated project instructions; run the composed custom prompt only in its supported GPT-5.6 Sol configuration.
4. Reconcile provider usage with literal loaded-Skill payload, catalog exposure, attempted and successful logical-path reads, retries, tool turns, and provider calls instead of attributing totals from answer shape alone.
5. Treat read and call counts as primary mechanism evidence and wall-clock latency as supporting evidence unless repetitions support a latency claim.
6. Review failures and disagreements without weakening gates or treating a small number of clean runs as causal proof.
7. Record an adopt, revise, or reject result bound to the exact candidate, corpus, harness, evaluator, sibling-package, trace, and report hashes.
Evidence: [the immutable 21-run report rejected two predeclared exact gates and is retained at SHA-256 0f02dd1fba9b1106ef5b2c295fefaf0dc54857d958889054989a0df21f87d521, the hash-bound three-run correction adopted both candidate gates at SHA-256 db09fa7c5fd6ea3206edc2f96926bfd6c7c48fdfd160598b51bd936b5a2672a8, ordinary candidate communication used zero Skill reads, all seven candidate routes passed semantically after correcting the contradictory UI order, one repetition makes latency observational only, the corrected current and candidate ordinary cases both used zero Skill reads so comparative token and latency improvement remains unproven]

### W-004 Document and synchronize an authorized qualified result

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: An explicitly authorized qualified candidate is documented and synchronized without mismatched prompt, Skill, installed package, tag, or release state.
Acceptance: Both repositories record the qualified behavior and evidence in their changelogs and relevant documentation while preserving prior benchmark claims as historical and package-bound; canonical package manifests and hashes match the intended commits; local Codex installations match the qualified artifacts and a fresh task passes normal-chat, artifact, code, UI-copy, opt-out, and pivot routing smoke tests; any commit, push, tag, GitHub Release, or cleanup occurs only after explicit authorization and is verified remotely.
Steps:
1. Prepare the final documentation and installation manifest from the adopted candidate evidence.
2. Request any missing authorization for repository, release, installation, or remote actions before performing them.
3. Apply only authorized synchronization and verify exact files, hashes, versions, tags, Releases, and installed paths.
4. Start a fresh Codex task and run the minimal normal-chat, writing, code, and mixed-UI routing smoke tests.
Evidence: [installed prompt SHA-256 23d2fb6bc06cd1ad68af05e2a4cb8391971219dd936d3d1c5a7411acb2cad899 matches the qualified candidate, installed Scribe Core SHA-256 bf725f1609a2b6b61742200f55ed82a3a231129b47ac2dfb61674cb94b692426 matches the qualified candidate and every package file matched, installed boundary and canonical Skill validation passed, a fresh local ordinary task returned 1.92 seconds with no Skill read or announcement, the first artifact smoke exposed an unrelated imitate-me false positive, its activation description was narrowed to explicit personal-voice requests at SHA-256 44c329d37bf99fff840f3a1f208613db5c2d7b7c539babc200e553829c04a828, the repeated artifact smoke loaded only Scribe and returned the requested two-sentence text, no commit push tag release or publication occurred]
