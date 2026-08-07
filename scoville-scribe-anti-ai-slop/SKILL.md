---
name: scoville-scribe-anti-ai-slop
description: Guardrail for prose, fidelity, and reader-facing interface text. Use for drafting, editing, summarizing, localizing, source-exact work, or audits. Preserve facts, meaning, terms, behavior, schemas, attribution, and exact text. Excludes code semantics, machine data, and supplied-text insertion without a wording, fidelity, or interface judgment.
---

# Scoville Scribe Anti-AI-Slop

Treat prose slop as writing that looks finished while weakening the reader
outcome: invented facts, shifted meaning, generic filler, inconsistent product
terms, or interface text detached from product behavior.

On explicit opt-out, do not read references, use Skill-directed tools, change
text, or make Skill-derived claims. If higher authority requires Scribe, report
that exact conflict. A sibling opt-out excludes only that sibling.

## Resolve the governing sources

Resolve each concern from the source that can answer it:

- **Current truth:** verified current behavior and supplied factual sources.
- **Target truth:** the explicitly requested final state when text changes with
  behavior. Engineering evidence must verify that state before completion or
  publication.
- **Terminology:** explicit user terms, project glossary, shared strings, and
  established usage for the same concept.
- **Form:** explicit output requirements, house style, genuine voice samples,
  and the conventions of the surface or genre.

If these sources conflict materially, report the conflict instead of choosing
convenient wording. Terminology never overrides behavior, and style precedent
never authorizes a new claim.

This Skill works independently. For engineering artifacts,
`scoville-code-anti-ai-slop`, when applicable, owns scope, canonical code,
behavior verification, artifact changes, and validation. Scribe owns readable
text and the smallest targeted read-only inspection of relevant terms and text
surfaces. Reuse verified behavior; do not infer it from wording.

For interactive interfaces, `scoville-ui-anti-ai-slop`, when applicable, owns
framework alignment, hierarchy, layout, responsive behavior, and whether
required labels or accessible names exist and are associated. Scribe owns their
wording and meaning. Rendering fixed source-exact strings does not trigger it.

Apply compatible host, project, request, and Scribe constraints together while
generating text. Scribe is not a post-processing pass over another owner's
answer. Surface boundaries decide which rules apply to each segment.

## Optimize for the reader outcome

After safety and explicit constraints, optimize for what the reader must know,
decide, or do. Facts, meaning, project language, and format constrain delivery;
smooth prose substitutes for none of them.

Change text only when the edit advances that outcome, fixes a concrete defect,
or satisfies a binding request or project convention. Match the requested
detail. Keep a direct instruction direct. For explanation, analysis, or teaching,
include the causal link and the material boundary; use an example or contrast
only when it makes the behavior more predictable.

## Select the mode and route

- **Fixed insertion:** Insert fully supplied wording into a fixed structure
  core-only when no wording, fidelity, terminology, behavior, or interface
  judgment is requested. This overrides later surface triggers; extraction or
  reproduction from a source is Source-exact.
- **Structured grouping:** Grouping enumerated decisions, proposals, or work
  items while retaining every item and open lifecycle choice is core; load no
  reference.
- **Draft:** Write only from permitted facts and claims.
- **Edit:** Make the smallest change that solves the observed problem.
- **Audit:** Report location, problem, reader effect, and correction direction;
  do not rewrite unless asked. An audit still follows the route for the subject
  it evaluates.
- **Fidelity-controlled:** Read
  [fidelity-modes.md](references/fidelity-modes.md) before adapting, materially
  summarizing, localizing, extracting or reproducing Source-exact text, auditing
  any such result, creating a controlled variant, or drafting or editing
  regulated or author-owned content. Fixed insertion and Structured grouping
  remain core-only.
- **Claim-preserving rewrite:** Changing wording or flow without changing claims
  is an Edit. For continuous prose, read
  [prose-patterns.md](references/prose-patterns.md), not the fidelity reference,
  unless a Fidelity-controlled condition above applies.

Determine only the reader, permitted facts and claims, required voice, language,
genre, form, and integrity constraints that can change the result. Ask only when
a missing answer would produce materially different text.

One artifact can mix prose, interface strings, procedures, structured records,
release notes, and exact or regulated text. Classify each segment only far enough
to apply the correct route; do not force the whole artifact into one profile.

Except for Fixed insertion, read
[interface-text.md](references/interface-text.md) before writing, changing,
auditing, or comparing any user-facing GUI or CLI string, error, notification,
transactional message, accessible text, metadata, or behavior-bound procedure.

Product-generated email uses the interface route; editorial, personal, or
newsletter prose uses the prose route unless behavior-bound. Route mixed email
per segment.

Before localizing user-facing strings, read both
[fidelity-modes.md](references/fidelity-modes.md) and
[interface-text.md](references/interface-text.md).

Read [prose-patterns.md](references/prose-patterns.md) for continuous prose,
substantive rationale drafted inside a structured record, or requested natural,
human-sounding, or anti-slop writing. Do not load it for a fixed short record
whose format owns its wording or for a behavior-bound interface procedure owned
by `interface-text.md`. Do not load it merely because a stepwise non-interface
procedure contains prose; keep that route Core-only unless the task also requires
substantive continuous explanation or explicitly requests natural or anti-slop
writing.

## Protect the universal integrity floor

Never invent or silently change:

- names, numbers, dates, units, links, citations, or attribution;
- quotations, technical terms, negation, modality, conditions, or exceptions;
- first-person experience, feelings, opinions, relationships, or identity; or
- product capabilities, causes, guarantees, timelines, available actions, or
  verified runtime behavior.

Keep hypotheses and examples visibly hypothetical. Preserve deliberate
ambiguity when the evidence does not resolve it. For behavior-bound text,
describe the supported current state; describe the requested target only when
the artifact is explicitly about that target and engineering evidence can own
the claim.

In every procedure—manual, interface, or CLI—preserve prerequisites, sequence,
inputs, warnings, commands, placeholders, and expected results unless verified
behavior or the request changes them. A clearer sentence does not authorize a
different operation.

High-risk legal, medical, financial, safety, privacy, or publication claims
require the appropriate authoritative source and qualified review. Editing
cannot substitute for either.

## Edit without manufacturing voice

Preserve strong passages and the writer's demonstrated register. Do not
diagnose AI authorship, promise detector evasion, or apply universal word,
punctuation, sentence-length, or formatting bans. Fix a pattern because of its
effect on this reader and genre, not its supposed origin. A canonical term stays
canonical even when repetition is stylistically inconvenient.

Apply routine Scribe guidance silently. Do not announce Skill use or narrate
normal drafting, editing, or auditing. Follow the host's disclosure rules for
non-obvious actions, pauses, scope changes, external effects, and material risk.

## Verify and complete

Before handing text back:

1. confirm the reader can reach the intended outcome;
2. recheck every integrity-floor item touched by the edit;
3. confirm each segment follows its surface and fidelity route;
4. confirm the requested language, format, length, and mode; and
5. remove process commentary unless the user requested an audit or explanation.

Report unresolved factual or project conflicts. Do not hide them inside smooth
copy. When asked only to audit, do not edit.
