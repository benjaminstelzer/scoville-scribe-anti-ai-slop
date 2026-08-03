---
name: scoville-scribe-anti-ai-slop
description: >-
  Goal-first prose and interface writing guardrail. Use when drafting, editing,
  auditing, adapting, summarizing, localizing, or fidelity-checking manuals,
  articles, emails, documentation, UI labels, errors, notifications, CLI help,
  accessible names, metadata, and reader-facing strings in code or resource
  files. Preserves source meaning, factual claims, author voice, canonical
  product terms, verified behavior, runtime schemas, and source-exact text while
  removing generic filler. Use alongside scoville-code-anti-ai-slop for
  engineering artifacts and scoville-ui-anti-ai-slop when interface wording
  and visual presentation both change. Not needed for code semantics or
  machine-only data.
---

# Scoville Scribe Anti-AI-Slop

Treat prose slop as writing that looks finished while weakening the reader
outcome: invented facts, shifted meaning, generic filler, inconsistent product
terms, or interface text detached from product behavior.

## Precedence

Resolve each concern from the source that can answer it:

- **Current truth:** verified current behavior and supplied factual sources.
- **Target truth:** the explicitly requested final state when text changes with
  behavior. Scoville Code must verify that state before completion or
  publication.
- **Terminology:** explicit user terms, project glossary, shared strings, and
  established usage for the same concept.
- **Form:** explicit output requirements, house style, genuine voice samples,
  and the conventions of the surface or genre.

If these sources conflict materially, report the conflict instead of choosing
convenient wording. Terminology never overrides behavior, and style precedent
never authorizes a new claim.

For engineering artifacts, apply `scoville-code-anti-ai-slop` too. Scoville
Code owns engineering scope, canonical ownership, behavior verification,
artifact changes, and validation. Scribe owns human-readable text and the
smallest targeted read-only inspection of relevant terms and text surfaces.
Reuse verified behavior; do not infer it from wording.

For interactive interfaces, apply `scoville-ui-anti-ai-slop` when presentation
or interaction is also in scope. UI owns framework alignment, hierarchy,
layout, responsive behavior, and whether required labels or accessible names
exist and are associated. Scribe owns their wording and meaning.

Apply compatible host-prompt, project, request, and Scribe constraints together
while generating the text. Scribe is not a post-processing pass over an answer
owned by another layer. Surface boundaries decide which voice rules apply to a
segment; they do not make one instruction source solely causal.

## Governing principle

After safety and explicit constraints, optimize for the intended reader
outcome. Facts, meaning, project language, and format constrain delivery; smooth
prose is not a substitute for any of them.

Change text only when the edit advances the reader outcome, fixes a concrete
defect, or satisfies a binding request or project convention.

Match the requested level of detail. Keep a direct operational instruction
direct; do not expand it into an unrequested workflow, checklist, validation
plan, or defensive procedure. For explanatory, analytical, or teaching prose,
the mechanism is part of the reader outcome: include the causal link, a useful
example or contrast when it makes the behavior predictable, and the material
boundary. Do not confuse concision with leaving the reader to infer the answer.

## Modes

- **Draft:** Write only from permitted facts and claims.
- **Edit:** Make the smallest change that solves the observed problem.
- **Audit:** Report location, problem, reader effect, and correction direction;
  do not rewrite unless asked.
- **Adapt**, including summarize: Remove only information the requested form can
  omit while preserving the conditions that keep each surviving claim true.
- **Localize:** Preserve meaning, terminology, format contract, and runtime
  schema while allowing natural target-language grammar.
- **Source-exact:** Extract or quote without stylistic change. Audit fidelity if
  correction was not requested.

## Frame the text

Determine only what changes the result:

- the reader and what they should know, decide, or do;
- the permitted facts and claims;
- the required voice, language, genre, and output form;
- the applicable integrity constraints.

Ask only when a missing answer would produce materially different text.

## Apply rules per segment

One artifact can mix continuous prose, interface strings, procedures, release
or migration notes, and exact or regulated text. Classify each segment only far
enough to apply the right rules. Do not force the whole artifact into one
profile.

Treat these as combinable constraints, not new profiles:

- **behavior-bound:** wording must match verified current or requested final
  behavior;
- **terminology-bound:** canonical project terms must stay consistent;
- **dynamic or localized:** runtime tokens and message structure must survive;
- **accessibility-bound:** preserve applicable accessible purpose,
  relationships, and visible-label wording;
- **source-exact:** supplied wording must remain verbatim;
- **regulated:** authoritative sources and qualified review limit claims;
- **author-owned:** rewrite only as requested, preserving attribution, speaking
  position, and the stated basis and strength of retained claims or decisions;
- **variant-controlled:** change only the variable the comparison intends to
  test.

Read [references/interface-text.md](references/interface-text.md) for any
user-facing interface segment, including GUI, CLI, errors, notifications,
transactional messages, accessibility text, and metadata.

Read [references/prose-patterns.md](references/prose-patterns.md) for continuous
prose or when the user asks for natural, human-sounding, or anti-slop writing.

## Integrity floor

Never invent or silently change:

- names, numbers, dates, units, links, citations, or attribution;
- quotations, technical terms, negation, modality, conditions, or exceptions;
- first-person experience, feelings, opinions, relationships, or identity;
- product capabilities, causes, guarantees, timelines, or available actions.

Keep hypotheses and examples visibly hypothetical. Preserve deliberate
ambiguity when the evidence does not resolve it.

For behavior-bound interface and procedure text, describe the supported current
state. In release, migration, historical, retrospective, or comparative prose,
include past states when the reader task requires them.

In procedures, preserve prerequisites, sequence, inputs, warnings, commands,
and expected results unless verified behavior or the request changes them.

High-risk legal, medical, financial, safety, or publication claims require the
appropriate source and review. Editing cannot substitute for that review.

## Edit for reader effect

Preserve strong passages and the writer's demonstrated register. Do not
diagnose AI authorship, promise detector evasion, or apply universal word and
punctuation bans. Fix patterns for their effect on this reader and genre, not
for their supposed origin. A canonical term remains canonical.

Apply routine Scribe guidance silently. Do not announce skill use or narrate
normal drafting, editing, or auditing steps. Follow the host's disclosure rules
for non-obvious actions, pauses, scope changes, external effects, and material
risks.

## Verify and complete

1. Confirm the reader can reach the intended outcome.
2. Recheck every integrity-floor item touched by the edit.
3. Confirm each segment follows its surface-specific constraints.
4. Confirm the requested language, format, length, and mode.
5. Remove process commentary unless the user requested an audit or explanation.

Report unresolved factual or project conflicts. Do not hide them inside smooth
copy.
