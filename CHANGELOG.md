# Changelog

## v1.0.27 - 2026-09-11

- Check explanatory text for missing prerequisites, unclear referents, empty
  instructions, and unsupported causal steps. Recheck each unanswered reader
  question after editing.
- Apply these checks across prose and interface help, regardless of personal
  voice. Keep the existing task routing and protected-source boundaries.

## v1.0.25 - 2026-09-09

- Describe byte-preserving source-exact file operations without requiring one
  host shell.

## v1.0.24 - 2026-09-08

- Leave native Plan, Work Item, and Decision wording with Scoville Plan unless
  the user explicitly requests Scribe.
- Apply the same boundary to follow-up edits and mixed tasks while keeping
  unrelated prose on its own route.
- Keep Scribe usable under the current record owner's format when Plan is
  absent, unavailable, or inactive.
- Preserve applicable Plan format and lifecycle checks during explicit Scribe
  work.

## v1.0.22 - 2026-09-05

- Keep sentence-first punctuation as the default for editable natural language,
  without em dashes, en dashes, or semicolons.
- Check for unearned contrasts, inflated significance, vague attribution,
  rhetorical scaffolding, and decorative formatting.
- Check interface text for vague actions, unsupported reassurance, mismatched
  celebration, redundant help, and errors that obscure recovery.
- Preserve canonical terms, exact sources, code, and text outside the requested
  edit scope.

## v1.0.21 - 2026-08-31

- Limit punctuation rules to new prose and the requested edit scope. Existing
  text outside that scope remains unchanged.

## v1.0.20 - 2026-08-31

- Prefer complete sentences and grammatical clauses built around periods and
  commas.
- Rewrite the sentence when removing an em dash, en dash, or semicolon instead
  of swapping one punctuation mark for another.
- Keep necessary compound-word hyphens, list markers, syntax, and protected
  source text intact.

## v1.0.19 - 2026-08-31

- Prohibit em dashes, en dashes, and semicolons in newly written or edited
  natural language, including interface text and non-English prose.
- Prefer sentence restructuring and use sentence-level ASCII hyphens only when
  they genuinely help.
- Exempt exact quotations, fixed insertions, technical syntax, canonical names,
  compound words, and list markers.

## v1.0.18 - 2026-08-24

- Activate Scribe for requested wording artifacts, transformations, wording
  audits, source-exact work, and independently constrained interface text.
- Do not activate it for ordinary conversation, explanations, status reports,
  domain-owner results, or final framing merely because they contain prose.
- Route mixed requests by segment and keep fixed insertion distinct from
  rewriting.

## v1.0.15 - 2026-08-11

- Require explanatory prose to cover every requested dimension and state exact
  material results that follow from supplied facts.
- Keep negative source constraints out of the visible artifact unless the user
  asks to discuss them.
- Preserve exact material relationships and values needed to understand a
  summary.

## v1.0.11 - 2026-08-11

- Made every Scoville Skill optional and independently usable. Discovering a
  sibling does not install or activate it.

## 2026-08-07: Progressive disclosure and fidelity routing

- Added focused handling for summaries, localization, source-exact text,
  regulated claims, author-owned prose, and controlled variants.
- Keep truth, procedure integrity, family boundaries, and route selection in
  the Core while loading detailed guidance only for the active text surface.
- Separate fixed insertion, structured records, continuous prose, interface
  procedures, and fidelity transformations.

## 2026-08-06: Record and interface boundaries

- Generalized structured-record language so Scribe works with any canonical
  project format.
- Keep Scribe active for labels, errors, recovery guidance, accessible wording,
  and substantive decision rationale while leaving short format-owned records
  with their record owner.
- Group related decision proposals into one compact set with ID, title,
  practical effect, and required user choices.
- Activate interface guidance only when wording, meaning, terminology, source
  fidelity, or runtime string contracts must be decided, changed, localized,
  audited, or reconciled.
- Do not activate Scribe merely because an interface renders an exact supplied
  label or accessible name.

## 2026-08-03: Joint prompt and Scribe calibration

- Apply Scribe together with host and project instructions during generation,
  not as a generic post-processing pass.
- Let argument structure determine paragraphs, examples, useful lead-ins, and
  closing syntheses without turning every short argument into a list.
- Keep hypothetical numerical examples visibly hypothetical and preserve
  meaningful totals, ratios, bounds, and limitations.
- Carry important examples through to an observable result and account for
  every named completion condition in status summaries.

## 2026-08-03: Rename to Scoville Scribe Anti-AI-Slop

- Renamed the Skill from `scoville-scribe` to
  `scoville-scribe-anti-ai-slop`.

### Migration

- Replace an installation under `scoville-scribe/` with
  `scoville-scribe-anti-ai-slop/` so the directory matches the Skill name.

## 2026-08-02: Explanatory depth and voice boundaries

- Treat causal mechanism, supported implications, useful examples, and material
  limits as part of the reader outcome for explanatory prose.
- Allow useful lead-ins, closing syntheses, and invited humour when they fit the
  artifact's own voice and purpose.
- Keep conversational humour out of prose and interface text unless the
  artifact itself calls for it.
- Do not expand a sufficient direct instruction into an unrequested workflow,
  checklist, validation plan, or defensive procedure.
- Check repeated sentence openings, lengths, clause shapes, contrast frames,
  list patterns, noun-heavy compression, and stacked modifiers.

## 2026-08-02: Initial release

- Added Draft, Edit, Audit, Adapt, Localize, and source-exact modes with
  different permissions for adding, removing, and rewriting content.
- Added separate authority for truth, terminology, form, accessibility,
  regulated claims, author-owned prose, and controlled variants.
- Added focused guidance for interface text and continuous prose.
- Keep detector evasion and authorship diagnosis outside the Skill. Judge the
  result by meaning, reader outcome, project consistency, and observed
  behavior.
