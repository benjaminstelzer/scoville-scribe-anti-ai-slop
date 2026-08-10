# Changelog

## 2026-08-10: Scoville Handoff sibling

### Changed

- Added Scoville Handoff to the optional family composition guide and
  reconciled the public run total across all five Scoville Skills.

## 2026-08-10: Clearer usage trade-offs

### Changed

- Explain that activating the Skill adds prompt context and is best suited to
  work where factual and semantic fidelity, terminology, source-exact handling,
  and reader-facing consistency justify the additional token cost.
- Remove the inline verification example and clarify that the public token
  comparison uses the pre-optimization release.

## 2026-08-10: Reliability-qualified compression

### Changed

- Compressed the activated Core while preserving source fidelity, procedure
  integrity, truthfulness, interface-text behavior, and routed prose guidance.
- Sharpened procedure-specific routing so fixed insertion remains distinct from
  interface work and general stepwise instructions.

### Validation

- The frozen paired benchmark passed Train 18/18, Validation 9/9, and sealed
  Test 3/3 for both the reliability control and compressed package.
- The compressed package passed all 30 cases across hard result, exact routing,
  execution semantics, process, and efficiency, with provider usage, no route
  retry, no shell call, and exact-once routed reads.
- Executor-loaded Skill instructions fell from 67,931 to 63,746 tokens across
  the 30 cases, a 6.16% reduction against the reliability-matched control.
- The canonical Agent Skill validator passes. The benchmark used
  `gpt-5.6-terra` at medium reasoning and does not establish equivalent
  behavior on weaker executors or arbitrary tasks.

## 2026-08-08: Optional Scoville Plan ownership

### Changed

- Assigned durable planning-record structure, ordering, lifecycle, and edit
  permission to Scoville Plan when that sibling is independently applicable.
- Preserved standalone Scribe behavior by deferring to an existing structured
  record owner when Scoville Plan is absent or inapplicable.
- Synchronized the interface-text contents list with its actual routed sections.

### Validation

- The canonical Agent Skill validator and repository diff checks pass.
- Fable's complete standalone and family review found no P0 or P1 issue; its
  remaining P2 interface-text navigation finding was corrected.
- The tested repository copy and the locally installed Skill are byte-identical.

## 2026-08-07: Progressive disclosure and fidelity routing

### Changed

- Added `references/fidelity-modes.md` for summary, localization, source-exact,
  regulated, author-owned, and variant-controlled transformations.
- Kept the universal truth floor, procedure integrity, family boundaries, and
  route selectors in the core while moving conditional detail to its owner.
- Clarified the boundaries between fixed insertion, structured records,
  continuous prose, interface procedures, and fidelity transformations.
- Shortened the frontmatter description without making sibling installation an
  activation signal.
- Kept a stepwise non-interface procedure Core-only unless it also requires
  continuous explanation, interface behavior, or explicit prose-style work.

### Validation

- The canonical Agent Skill validator passes.
- Seven focused standalone routing cases passed with `gpt-5.6-sol` at medium
  reasoning, including Core-only procedure and fixed-insertion boundaries,
  interface text, continuous prose, localization, source-exact text, and mixed
  editorial/transactional segments.
- The full UI/Code/Scribe composition and the explicit Scribe opt-out case
  passed with only their required references.
- With `gpt-5.6-terra` at medium reasoning, all seven standalone cases selected
  the intended Core and references, and both composition cases preserved their
  Skill and opt-out boundaries. Six standalone outputs preserved every required
  content fact; the mixed editorial/transactional case omitted one supplied
  delivery fact despite selecting the intended routes.
- Direct-reference, diff, encoding, and host-neutrality checks pass.

## 2026-08-06: Standalone structured-record terminology

### Changed

- Generalized structured-record and proposal-routing language so the Skill
  applies to any canonical project format without implying a dependency on a
  particular planning product.

### Validation

- The canonical Skill validator and evaluation JSON parser pass; standalone
  fixtures cover operation without a record system or sibling Skills.

## 2026-08-06: Format-owned records and grouped proposal reporting

### Changed

- Kept Scribe active for labels, errors, recovery guidance, accessible wording,
  and substantive decision rationale while excluding short format-owned
  ReasonKeep records from the continuous-prose reference.
- Grouped coherent decision-proposal reporting into one compact set with ID,
  title, practical effect, and the required user choices.
- Extended silent routine use to reference selection and Skill routing.

### Validation

- Positive and negative routing fixtures cover interface errors, recovery text,
  substantive decision records, short format-owned records, and grouped proposals.

## 2026-08-06: Narrow interface-text activation

### Changed

- Limited interface activation to tasks that decide, change, localize, audit,
  or reconcile wording, meaning, terminology, source fidelity, or runtime
  string contracts.
- Excluded source-exact labels and already-fixed accessible names from
  activating Scribe merely because an interface renders them.
- Prevented the continuous-prose reference from loading for isolated interface
  strings and fixed task copy.

### Validation

- The installable directory passed the canonical Agent Skill validator.
- A focused routing review confirmed that unchanged, explicitly supplied
  labels now remain with Code or UI unless a text decision is present.

## 2026-08-03: Family documentation alignment

### Changed

- Aligned the README section order and installation guidance with Scoville Code
  and Scoville UI.
- Added the Scribe-specific explanation of the Scoville family name.
- Consolidated routing, family composition, repository contents, and status
  into the shared documentation structure.

### Validation

- `quick_validate.py` accepted the installable skill directory.
- README links and documented word costs matched the current files.
- `git diff --check` passed.

## 2026-08-03: Scoville family composition

### Changed

- Updated engineering references to the renamed
  `scoville-code-anti-ai-slop` skill.
- Added the boundary with `scoville-ui-anti-ai-slop`: UI owns framework
  alignment and interface presentation; Scribe owns visible and accessible
  wording and meaning.

## 2026-08-03: Joint prompt and Scribe calibration

### Changed

- Clarified that Scribe composes with the host prompt, project instructions,
  and request during generation instead of acting as a post-processing pass.
- Made explicitly multi-part requests trigger matching lead-ins while keeping
  short connected arguments in prose.
- Allowed visibly hypothetical numerical counterexamples without weakening the
  distinction between illustration and evidence.
- Let argument structure determine paragraph rhythm and made useful closing
  syntheses more salient without requiring a summary.
- Integrated explicitly invited humor into the explanation before a possible
  callback and preserved segment-specific humor restrictions.
- Bound required limitation sections to their affected claims or calculations.
- Made load-bearing examples carry one concrete instance through to its
  observable result instead of stopping at a named case.
- Made claims about weak small-sample evidence trigger a visibly hypothetical
  probability instead of remaining qualitative.
- Made questions about what makes a tool, model, or practice useful trigger one
  representative case through contribution and external verification.
- Preserved meaningful totals, ratios, and bounds in numerical change
  summaries.
- Required status summaries to account for every enumerated completion
  condition before compressing.

### Validation

- `quick_validate.py` accepted the installable skill directory.
- README word-cost figures matched the updated `SKILL.md` and prose reference.
- `git diff --check` passed, and focused contract checks found matching rules in
  Scribe and the companion system prompt.

## 2026-08-03: Installable skill subdirectory

### Changed

- Moved `SKILL.md`, `agents/`, and `references/` into the installable
  `scoville-scribe-anti-ai-slop/` directory.
- Kept the README, changelog, and license at the repository root so they are not
  loaded as part of the skill.
- Updated installation instructions and documentation links for the nested
  layout.

## 2026-08-03: Rename to Scoville Scribe Anti-AI-Slop

### Changed

- Renamed the published repository and installable skill from
  `scoville-scribe` to `scoville-scribe-anti-ai-slop` for consistency with
  `scoville-anti-ai-coding-slop`.
- Updated the skill name, display metadata, installation prompt, example
  project instruction, and documented installation paths.

### Migration

- Existing installations under `scoville-scribe/` must be replaced by a folder
  named `scoville-scribe-anti-ai-slop/` so the folder matches the skill name in
  `SKILL.md`.

## 2026-08-02: Explanatory depth and Fable-style calibration

### Changed

- Treated the causal mechanism, supported derived implications, useful
  examples, and material boundaries as part of the reader outcome for
  explanatory prose.
- Allowed short bold lead-ins and closing syntheses when they expose or compress
  real argument structure instead of decorating or repeating it.
- Calibrated punctuation and permitted humor toward a more essay-like,
  technically literate voice without weakening evidence, attribution, output
  constraints, or artifact-specific voice boundaries.
- Kept the explanatory guidance in the existing prose reference rather than
  adding a third overlapping voice owner.

### Validation

- `quick_validate.py` accepted the updated skill structure and metadata.
- A fresh explanatory forward test derived an unchanged polling window, the
  lower detection latency, and the higher polling load while separating facts,
  inferences, and unknowns.
- A fresh source-near edit preserved the supplied numbers and dry humor, removed
  repetition, and added no process commentary or unsupported claim.

## 2026-08-02: Conversation and artifact voice boundaries

### Changed

- Made routine Scribe guidance silent without hiding actions, pauses, external
  effects, scope changes, or material risks.
- Allowed humor when requested or supported by the artifact's source, voice, or
  genre without treating natural or human-sounding prose as a humor request.
- Kept conversational humor out of prose and interface text unless the
  artifact's own constraints call for it.

## 2026-08-02: Requested detail level

### Changed

- Prevented a sufficient direct instruction from expanding into an unrequested
  workflow, checklist, validation plan, or defensive procedure.
- Kept detail required by correctness, safety, or the explicit request.

## 2026-08-02: Natural prose pattern checks

### Changed

- Made sentence and paragraph rhythm checks concrete enough to catch repeated
  openings, lengths, clause shapes, contrast frames, and list patterns.
- Added a clarity check for noun-heavy compression and stacked modifiers.
- Added context-bound guidance for em dashes and parenthetical expressions
  without fixed counts, punctuation bans, or manufactured randomness.

## 2026-08-02: README claim precision

### Changed

- Aligned context-cost and routing descriptions with segment- and request-based
  loading.
- Clarified that a style change needs a reader task, source, genre, or interface
  reason.
- Described Scribe and Scoville as separate responsibilities under one
  goal-first contract rather than claiming that they never overlap.
- Limited the research section to current sources; forward-test history remains
  in the changelog.

## 2026-08-02: Initial release

### Added

- A goal-first writing contract for Draft, Edit, Audit, Adapt, Localize, and
  source-exact work. Each mode changes what the agent may add, remove, or
  rewrite instead of treating every request as a generic humanizer pass.
- Concern-specific authority for truth, terminology, and form. This keeps a
  glossary from preserving false behavior and keeps product implementation from
  inventing a house voice.
- Segment-level constraints for behavior, terminology, dynamic messages,
  localization, accessibility, source-exact text, regulated claims,
  author-owned prose, and controlled variants.
- A UI reference covering project terminology, current-state text, action and
  error semantics, placeholders, ICU branches, access keys, visible labels,
  accessible names, metadata, and contextual checks.
- A prose reference covering source-near editing, reader-visible defects,
  contextual style judgment, author-owned claims, modality, and the difference
  between explicit evidence and inferred mental state.
- Agent metadata for Codex and other hosts that read `agents/openai.yaml`.

### Validation

- Fresh forward tests covered project terminology, unreleased product history,
  UI strings embedded in code, Polish ICU plural branches, accessible names,
  procedural prerequisites, Audit without rewriting, historical prose, mixed
  UI and manual text, and author-owned shortening.
- The author-owned shortening case repeatedly changed "had enough information"
  into "knew enough" or removed modal force. Two short contrast examples were
  added only after the abstract integrity rules failed to stop the behavior;
  the final fresh case preserved both propositions.
- A separate summary case confirmed that protecting retained propositions does
  not require every source detail to survive an allowed summary.
- `quick_validate.py` accepted the final skill structure and metadata.

### Note

- Scribe complements `scoville-anti-ai-coding-slop`; it does not copy
  engineering scope, planning, implementation, or validation rules.
- UI and continuous-prose details remain separate references. The common core
  loads once, and each task loads only the text-surface rules it needs.
- Detector evasion and authorship diagnosis are outside the contract. Quality
  is judged through meaning, reader outcome, project consistency, and observed
  behavior.
