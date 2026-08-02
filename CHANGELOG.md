# Changelog

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
