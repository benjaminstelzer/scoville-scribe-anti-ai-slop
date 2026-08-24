---
name: scoville-ui-anti-ai-slop
description: Framework-aware guardrail for UI design, implementation, and audit. Use for hierarchy, layout, states, responsiveness, accessibility, usability, or clarity. Preserve the product design system and platform language. Excludes backend-only work and prose. Compose with Code for engineering and Scribe for variable UI wording.
---

Improve existing UI usability, information design, adaptation, accessibility,
and clarity; never replace its design language.

## Gates and owners

**OPT-OUT:** If the user explicitly excludes this Skill, STOP before references,
Skill tools, changes, or Skill-derived completion claims. If higher-authority
host/project rules require it, report exact conflict.

Apply the highest owner per concern:

1. system, safety, legally binding accessibility;
2. explicit user request, including informed acceptance of a reported
   limitation against a non-binding target;
3. repository instructions;
4. canonical product requirements, design-system components, wrappers, themes,
   semantic tokens, approved assets;
5. owning framework/platform for unresolved concerns;
6. deliberate owner-aligned local patterns;
7. this Skill's principles for the remaining gap.

Lower sources never override higher owners; report material conflicts.

- **LOCAL:** A repeated pattern counts only if deliberate, current, and right for
  the same surface.
- **UNKNOWN EXCEPTION:** Ownership is unresolved. Inspect or ask; normalize only
  with evidence it is accidental or stale.
- **GREENFIELD:** No visual owner plus requested polish makes the surface owner
  of a deliberate local direction; framework defaults remain primitives.
- **ACCESSIBILITY:** No target: web uses WCAG 2.2 AA; elsewhere use current
  platform guidance; always use supported components and APIs.
- **OWNER LIMIT:** Report exact canonical owner and limit; no parallel language.
  Informed acceptance may waive the reported non-binding target, never higher
  system, safety, or legal rules.

## Skill family

Family standalone: discovery != installed|active|applicable|required;
absent|inactive => ignore/no require|install|simulate|reimplement;
active+applicable => owner concern only, self continues; opt-out local. Owners:
`scoville-brainstorm` divergence;
`scoville-code-anti-ai-slop` engineering/proof;
`scoville-scribe-anti-ai-slop` wording/fidelity; `scoville-plan`
records/lifecycle; `scoville-handoff` transfer.

UI owns presentation and required label/accessibility-name existence and
association. Fixed source-exact strings do not activate Scribe.
When active, Scribe owns what text says; UI owns its presentation. Do not copy
or reverify siblings.

## Workflow

1. Inspect as needed: surface, repository rules, framework version, canonical
   owners, nearest comparable surface.
2. Identify primary task, priority, affected states, content variation, inputs,
   responsive transformations.
3. Reuse canonical components, tokens, variants, layouts, breakpoints, and
   interactions. Add a primitive only for a demonstrated owner gap.
4. Make the smallest coherent change for the outcome and required states.
5. Verify only rendered conditions able to disprove. Report rendered, source,
   and unverified evidence separately. Mark unimplemented or source-only work
   unrendered and rendered behavior unverified; never load Validation merely to
   state this boundary.

## Reference router

- **Framework:** Load
  [framework-alignment.md](references/framework-alignment.md) before choosing an
  owner if stack unfamiliar, ownership ambiguous, UI layers interact, no
  canonical visual owner exists, or customization path is uncertain.
- **Quality:** Load [ui-quality.md](references/ui-quality.md) before judging task
  flow, hierarchy, layout, readability, states, accessibility structure, or
  responsive behavior.
- **Validation:** Load [validation.md](references/validation.md) after an
  interface change or before claims of rendered/responsive behavior, observed
  interaction, visual quality, or accessibility. Build/source cannot prove
  rendering.

**EVIDENCE-ONLY:** UI decision fixed; judge proof only. Load Validation alone
unless judging UI. Classifying the problem or owner, choosing layout, or
selecting remaining rendered checks requires Quality and Validation.

**SOURCE-ONLY AUDIT:** If structure-only, omit Validation; explicitly mark
rendered/interactive behavior unverified. For unimplemented direction, omit it
only to report the same unrendered boundary.

## Integrity floor

Never improve appearance through: parallel visual language; semantic-token
bypass; accessible-component rebuild; removed focus/input accommodation; hidden
required content; meaning carried solely by one visual cue; missing changed-state
recovery; local exception applied through a global theme override.

Never impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoints, pixel values, or fashionable bans. Quantitative rules come only
from the applicable accessibility standard, platform, or design system.

Audit/advice only: return prioritized findings tied to observed evidence; make
no edits.
