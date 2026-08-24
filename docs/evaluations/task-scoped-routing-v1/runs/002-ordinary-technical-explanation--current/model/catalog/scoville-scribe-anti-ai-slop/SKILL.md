---
name: scoville-scribe-anti-ai-slop
description: Guardrail for prose, fidelity, and reader-facing interface text. Use for drafting, editing, summarizing, localizing, source-exact work, or audits. Preserve facts, meaning, terms, behavior, schemas, attribution, and exact text. Excludes code semantics, machine data, and uninvoked supplied-text insertion without a wording, fidelity, or interface judgment; explicit invocation keeps such insertion Core-only.
---

# Scoville Scribe Anti-AI-Slop

Write effective text without changing truth, meaning, canonical terms, or
behavior, and without filler.

**Explicit opt-out:** load no references; use no Skill-directed tool; change no
text; make no Skill-derived claim. Report higher-authority requirements to use
Scribe.

For Source-exact extraction or reproduction, preserve the requested boundary
and that span's whitespace and newline state. When markers occupy their own
lines, the separator newline before the end marker is not part of the selected
span unless the boundary explicitly includes it. For whole-file Source-exact or
opt-out passthrough, use a byte-preserving API such as
`[System.IO.File]::ReadAllText`, never `Get-Content`; serialize directly. Fixed
insertion copies the supplied string exactly.

## Resolve authority and scope

Resolve compatible host, project, request, and Scribe constraints per segment
during writing:

| Concern | Ordered authority |
|---|---|
| Current truth | Verified behavior; supplied facts |
| Target truth | Engineering evidence before completion/publication |
| Terms | Explicit user terms; glossaries; shared strings; established same-concept usage |
| Form | Explicit requirements; house style; genuine voice samples; surface/genre conventions |

Report material conflicts. Behavior outranks terms; facts outrank style. Resolve
only output-affecting reader, allowed facts/claims, voice, language, genre, form,
and integrity. Ask only when an unknown changes output materially.

Scribe owns wording/meaning and minimal targeted read-only term/text inspection.
Family standalone: discovery != installed|active|applicable|required;
absent|inactive => ignore/no require|install|simulate|reimplement;
active+applicable => owner concern only, self continues; opt-out local. Owners:
`scoville-brainstorm` divergence;
`scoville-code-anti-ai-slop` engineering/proof; `scoville-ui-anti-ai-slop`
interface/rendered proof; `scoville-plan` records/lifecycle;
`scoville-handoff` transfer. Reuse sibling evidence; without Plan, preserve owner format/lifecycle
and edit permitted wording only. Never infer behavior from copy. Fixed
source-exact rendering does not trigger UI.

After safety and explicit constraints, serve the reader's required knowledge,
decision, or action. Change text only for a binding request/convention, concrete
defect, or that outcome. Match detail; include required causal links and
boundaries, plus useful examples.

## Select mode and references per segment

Route by the requested transformation and target surface. Neither the integrity
floor nor comparison against facts, requirements, behavior, or a glossary
selects Fidelity; add it only for an explicit Fidelity operation below. Combine
routes only when each route independently triggers for the same segment.

Selecting exact tokens from a structured requirements record is not
Source-exact extraction/reproduction. A stepwise non-interface procedure stays
Core-only unless a Fidelity-row trigger independently applies.

Report any requested route or profile from the selected references: none is
`CORE_ONLY`; otherwise report exactly the selected routes in controller order.

| Mode | Core rule |
|---|---|
| Fixed insertion | Fully supplied wording plus fixed structure, with no wording, fidelity, terminology, behavior, or interface judgment: insert and load no reference despite surface triggers. Extraction/reproduction is Source-exact. |
| Structured grouping | Retain every enumerated item and unresolved lifecycle choice; load no reference. |
| Draft | Use only permitted facts/claims. |
| Edit | Make the smallest sufficient change. Claim-preserving rewrite is Edit. |
| Audit | Report location, problem, reader effect, correction direction. Rewrite only if asked; follow the subject's route. |

Reference routes:

| Read | Before or for |
|---|---|
| [Fidelity](references/fidelity-modes.md) | Adaptation; material summary; localization; Source-exact extraction/reproduction; audits of those outputs; controlled variants; regulated or author-owned drafting/editing. |
| [Interface](references/interface-text.md) | Writing, changing, auditing, or comparing any non-Fixed-insertion user-facing GUI/CLI string, error, notification, transactional message, accessible text, metadata, or behavior-bound procedure. Product-generated email uses Interface. Editorial, personal, and newsletter prose follows prose routing unless behavior-bound. User-facing localization also needs Fidelity. |
| [Prose](references/prose-patterns.md) | Continuous prose; substantive record rationale; requested natural, human-sounding, or anti-slop writing. Use Prose instead of Fidelity for continuous claim-preserving rewrites unless Fidelity also triggers. Exclude format-owned fixed short records and behavior-bound interface procedures. A core-only stepwise non-interface procedure triggers Prose only for substantive continuous explanation or explicit natural/anti-slop requests. Audit prose claims with Prose unless Fidelity triggers. |

Classify mixed artifacts only far enough to route each segment correctly.

## Preserve integrity

Never invent or silently change: names; numbers, dates, units; links, citations;
attribution, quotations, exact-text boundaries; schemas, technical terms;
negation, modality, conditions, exceptions; first-person experience, identity,
relationships, opinions, feelings; product capabilities, causes, guarantees,
timelines, actions, or verified runtime behavior. Mark hypotheses/examples as
hypothetical. Preserve unresolved deliberate ambiguity.

Behavior-bound text states the supported current state. State a requested target
only in its artifact. Preserve
procedure prerequisites, order, inputs, warnings, commands, placeholders, and
expected results unless request or verified behavior changes them.

High-risk legal, medical, financial, safety, privacy, or publication claims need
appropriate authoritative sources and qualified review; editing is neither.

Preserve strong passages and demonstrated register. Never diagnose AI
authorship, promise detector evasion, impose universal word, punctuation,
sentence-length, or formatting bans, or vary canonical terms for style. Apply
routine guidance silently; disclose only host-required non-obvious actions,
pauses, scope changes, external effects, or material risk.

## Complete

Before return, verify reader outcome, touched integrity items, each segment's
surface/fidelity route, requested language/format/length/mode, and removal of
unrequested process commentary. Report unresolved factual/project conflicts.
Audit-only means no edit.
