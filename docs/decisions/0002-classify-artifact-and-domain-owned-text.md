---
format_version: 1
id: ADR-0002
status: accepted
created: 2026-08-24
accepted: 2026-08-24
scope: skills/routing-boundary
---

# Classify artifact-bound and domain-owned text

## Decision

Use observable task intent rather than output medium to classify Scribe activation. Treat wording as a Scribe artifact or transformation when the user requests drafting, editing, rewriting, summarizing supplied source material, localization, source-exact work, named-audience or named-genre copy, publication-ready or paste-ready text, or text explicitly intended for reuse. Do not activate Scribe for ordinary answers, analysis, explanations, status recaps, review findings, research answers, final framing, or a domain owner's normal record merely because they contain prose. Chat delivery alone neither activates nor suppresses Scribe. Apply Scribe only to independently triggered text segments in mixed tasks.

## Problem

The accepted task-scoped routing direction does not yet classify the ambiguous middle band. Summaries, reports, reviews, documentation, code comments, commit and PR text, Plan and Handoff records, and text returned in chat can each be either disposable communication or a retained artifact. Without a frozen rule, the Skill implementation and evaluator can make different reasonable choices, preserving over-routing or causing under-routing after results are visible.

## Drivers

- Make the activation rule observable before implementation and evaluation.
- Preserve Scribe for source transformation, publication, reuse, localization, exactness, and independently requested wording quality.
- Prevent normal results from Code, UI, Research, Plan, and Handoff from automatically adding Scribe.
- Preserve automatic specialist routing without requiring explicit Skill names.
- Keep the same classification across chat, file, and copy-paste delivery when user intent is unchanged.
- Handle referential follow-ups, pivots, opt-out, and missing Skills consistently.

## Considered alternatives

- Classify by output location: rejected because reusable artifacts may be returned in chat and disposable explanations may be written into logs or records.
- Classify every summary, report, review, comment, or record as Scribe work: rejected because domain-owner output would recreate broad automatic composition.
- Require explicit Scribe invocation for every ambiguous case: rejected because requested artifacts and transformations should route automatically from intent.
- Leave ambiguous cases to runtime judgment without frozen fixtures: rejected because implementation and evaluation could diverge or move expectations after results.

## Consequences

- Requested source summaries remain Scribe Fidelity work; routine progress or status recaps do not activate Scribe.
- Domain review findings use their domain owner; wording review, claim-preserving rewrite, or audience-ready review copy activates Scribe for that segment.
- Research answers use Research; separately requested audience-ready reports add Scribe for the report artifact.
- Plan, Decision, and Handoff structure uses its domain owner; Scribe is added only for independently requested substantive wording or fidelity work.
- Incidental comments, docstrings, commit messages, and PR text created as subordinate coding work stay Code-owned; explicit drafting or rewriting of those text artifacts adds Scribe, with Code retained when engineering truth must be derived or verified.
- Source-exact extraction and reproduction use Scribe Fidelity; fixed supplied insertion without wording judgment does not activate Scribe unless explicitly invoked.
- A follow-up transformation of the same artifact reactivates Scribe, while a pivot to ordinary explanation does not inherit it.
- Explicit opt-out prevents automatic Scribe activation for the current task; a missing or unreadable required Skill uses the compact fallback and is reported briefly.
- On hosts without the custom GPT-5.6 Sol prompt, Scribe still follows this artifact boundary while ordinary conversation follows that host's own defaults.

## Confirmation

Before implementation, freeze a route table whose rows cover ordinary explanation, status recap, requested source summary, routine recap, domain review, wording review, research answer, audience-ready report, documentation draft, incidental and requested comments or docstrings, incidental and requested commit or PR text, source-exact work, fixed insertion, Plan, Decision, Handoff, reusable text returned in chat, file delivery, explicit invocation, opt-out, missing Skills, artifact follow-up, conversational pivot, and mixed UI copy. Each row must name exact Skills, exact references, required and forbidden reads, hard output requirements, and whether delivery or reuse intent changes classification.

## Revisit when

Revisit if representative qualification shows a material quality or routing regression, if a domain Skill adds its own artifact-writing owner, or if the host gains a native typed artifact signal that is more reliable than intent classification.
