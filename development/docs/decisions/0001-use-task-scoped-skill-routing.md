---
format_version: 1
id: ADR-0001
status: accepted
created: 2026-08-24
accepted: 2026-08-24
scope: skills/routing
---

# Use task-scoped minimal Skill routing

## Decision

Load only the smallest set of Skills required by the current task. Ordinary agent-user conversation uses the compact system-prompt defaults and does not activate Scoville Scribe merely because the response contains prose. Activate Scribe when wording itself is a requested artifact or transformation target, including drafting, editing, localization, source-exact work, and reader-facing interface text. Apply Skills only to the segments they own in mixed tasks. Keep routine Skill selection and loading silent unless it changes scope, risk, external effects, or continuation.

## Problem

The current prompt names Scribe broadly as the owner of prose and fidelity, while the Skill routes continuous prose and substantive explanations through its Core and Prose reference. This can make ordinary answers load thousands of additional instruction tokens, add tool and model cycles, increase latency, and produce repetitive Skill announcements. The desired behavior is automatic specialist support for real writing, coding, UI, planning, research, and handoff tasks without treating every conversational response as a specialist artifact.

## Drivers

- Avoid unnecessary input tokens, repeated context, tool calls, and latency.
- Preserve automatic activation of the correct Skill for specialized work.
- Preserve Scribe's factual, terminology, interface, localization, and source-fidelity guarantees when text itself is the deliverable.
- Keep coding work under Code, interface work under UI, and mixed tasks segmented by owner.
- Retain compact conversational quality rules in the system prompt without a second chat-writing Skill.
- Require measured routing, quality, token, and latency evidence before adoption.

## Considered alternatives

- Keep the current broad Scribe activation: rejected because ordinary explanations can load the full Scribe Core and Prose reference without needing artifact-writing safeguards.
- Add a Scribe Lite route inside the existing Skill: rejected because selecting the Skill still requires reading its complete Core before the lighter route can be chosen.
- Create a separate chat-writing Skill: rejected because it duplicates the system prompt, adds another routing decision, and still consumes context.
- Require explicit Skill invocation for every specialist task: rejected because appropriate Skills should continue to activate automatically from task intent.

## Consequences

- The system prompt becomes the sole owner of ordinary conversational style and technical explanation defaults.
- Scribe's activation description, Core routing gate, Prose selector, tests, and public documentation must use an artifact-or-transformation boundary rather than a generic prose boundary.
- The system prompt must define minimal task-scoped Skill selection, Scribe's artifact boundary, segment-level composition, and silent routine routing.
- Existing conversational Scribe evaluations must move to the system-prompt suite or become negative Scribe-routing cases while artifact-fidelity evaluations remain in Scribe.
- Candidate adoption depends on representative routing, answer-quality, token, latency, and model-cycle evidence rather than shorter payload alone.

## Confirmation

Run frozen current-versus-candidate routing cases for ordinary conversation, text artifacts, code, UI, mixed UI copy, explicit invocation, planning, research, and handoff. Confirm exact Skill and reference reads, model cycles, provider-reported input and cached tokens, output and total tokens, latency, and hard-result quality. Adopt only if ordinary conversation has no unnecessary Scoville Skill reads and specialist tasks retain their required owners and acceptance results.

## Revisit when

Revisit if the host gains native partial-Skill loading that changes the Core-read cost, if representative evaluations show a material loss in conversational or artifact quality, or if a new Skill requires a different composition boundary.
