---
name: scoville-scribe-anti-ai-slop
description: Guardrail for requested wording artifacts and transformations such as drafting, editing, source summaries, localization, source-exact work, wording audits, and reader-facing interface text. Use when wording itself is the deliverable or an independently constrained segment. Do not use for ordinary conversation, explanations, status, domain results, final framing, or uninvoked fixed insertion merely because they contain text. Preserve facts, meaning, terms, behavior, schemas, attribution, and exact text.
---

# Scoville Scribe Anti-AI-Slop

Write effective artifact text without changing truth, meaning, canonical terms,
or behavior, and without filler.

**Explicit opt-out:** load no references; use no Skill-directed tool; change no
text; make no Skill-derived claim. Report higher-authority requirements to use
Scribe.

## Activate only for text artifacts

Activate Scribe when wording itself is a requested deliverable or transformation
target: drafting, editing, rewriting, summarizing supplied source material,
localizing, source-exact work, wording or fidelity audit, named-audience or
named-genre copy, publication-ready or paste-ready text, explicit reuse, or
reader-facing interface text.

Do not activate Scribe for ordinary answers, analysis, explanations, status or
progress recaps, domain review findings, research answers, final framing, or a
domain owner's normal record merely because the result contains prose. Chat,
file, commit, or other delivery alone neither activates nor suppresses Scribe.
Incidental comments, docstrings, commit messages, and pull-request text remain
with Code; explicitly requested drafting or rewriting of those artifacts adds
Scribe, with Code retained when engineering truth must be derived or verified.

Classify mixed tasks per segment. A domain owner's normal result does not add
Scribe without an independent wording or fidelity trigger. A referential
follow-up transformation of an active artifact reactivates Scribe; a pivot to
ordinary explanation does not inherit it. Fully supplied fixed insertion with
no wording, fidelity, terminology, behavior, or interface judgment does not
activate Scribe unless the user explicitly invokes it.

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
`scoville-research` source-backed research and synthesis;
`scoville-code-anti-ai-slop` engineering/proof; `scoville-ui-anti-ai-slop`
interface/rendered proof; `scoville-plan` records/lifecycle;
`scoville-handoff` transfer. Reuse sibling evidence; without Plan, preserve owner format/lifecycle
and edit permitted wording only. Never infer behavior from copy. Fixed
source-exact rendering does not trigger UI.

After safety and explicit constraints, serve the artifact reader's required
knowledge, decision, or action. Change text only for a binding request or
convention, a concrete defect, or that outcome. Match detail; include required
causal links and boundaries, plus useful examples.

## Select mode and references per segment

Route by the requested transformation and target artifact surface. Neither the integrity
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
| [Prose](references/prose-patterns.md) | Continuous artifact prose; independently requested substantive rationale; requested natural, human-sounding, or anti-slop artifact writing. Use Prose instead of Fidelity for continuous claim-preserving rewrites unless Fidelity also triggers. Exclude domain-owned normal records, format-owned fixed short records, and behavior-bound interface procedures. A non-interface artifact procedure triggers Prose only when its explanatory wording is independently variable. Audit artifact prose claims with Prose unless Fidelity triggers. |

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
authorship, promise detector evasion, or vary canonical terms for style. Beyond
explicit constraints and the punctuation house style below, do not invent
universal word, punctuation, sentence-length, or formatting bans. Apply routine
guidance silently. Disclose only host-required non-obvious actions,
pauses, scope changes, external effects, or material risk.

## Punctuation house style

Build newly written or edited natural-language text, including interface copy,
around complete sentences and grammatical clauses, primarily using periods
and commas. Do not use em dashes (U+2014), en dashes (U+2013), or semicolons (`;`).

Rewrite affected sentences, not just their punctuation. Integrate asides into
the main clause, connect related ideas grammatically, or split a thought into
self-contained sentences while preserving its logical relationships. Do not
keep the old construction by swapping in other marks, including hyphens,
colons, parentheses, commas, or periods.

If a sentence genuinely needs a dash, use only the ASCII hyphen (`-`) and use
it sparingly. Keep necessary compound-word hyphens and required list markers.

Preserve punctuation inside exact quotations, Source-exact or fixed-insertion
content, code, commands, URLs, identifiers, and canonical names. These rules
govern newly written prose and prose within the requested edit scope, not
protected source text or syntax. Leave existing text outside that scope
unchanged. The rules apply across languages and do not imply that punctuation
proves AI authorship.

## Complete

Before return, verify reader outcome, touched integrity items, each segment's
surface/fidelity route, requested language/format/length/mode, sentence-first
punctuation house style within the requested writing or edit scope, and removal
of unrequested process commentary. Report unresolved factual/project conflicts.
Audit-only means no edit.
