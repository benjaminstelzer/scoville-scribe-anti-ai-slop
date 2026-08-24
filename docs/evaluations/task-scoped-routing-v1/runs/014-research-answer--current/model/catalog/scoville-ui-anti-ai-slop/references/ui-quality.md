# UI Quality

Apply only the lenses that can change the requested outcome. These are outcome
tests, not a visual recipe.

## Contents

- Start with the user task
- Make relationships perceptible
- Preserve readable content
- Make interaction predictable
- Adapt instead of merely shrinking
- Design states as part of the same interface
- Keep accessibility structural

## Start with the user task

Make the primary task and its next meaningful action understandable from the
interface, not from implementation knowledge. Secondary actions and supporting
information should remain available without competing equally for attention.
Preserve domain terminology and product intent; do not simplify away necessary
distinctions.

For each visible region, ask:

- What decision or action does it support?
- What information must be understood before that action?
- What can remain secondary, progressive, or contextual?
- What must persist across state or viewport changes?

Remove or demote content only when doing so preserves the user's task and the
canonical content owner permits it.

## Make relationships perceptible

Use the owning system's hierarchy, grouping, alignment, sequence, and emphasis
mechanisms so related information reads together and distinct concerns remain
distinct. Visual difference must represent a real difference in meaning or
interaction. Avoid adding containers, decoration, or emphasis that creates no
new relationship.

Consistency means that the same meaning and behavior receive the same treatment
within the relevant product context. It does not mean making unlike tasks look
identical. Preserve a deliberate exception when it communicates a genuine
difference. Fix accidental drift at the canonical owner when the fix is in
scope; otherwise report it without expanding the task.

## Preserve readable content

Use the project or platform's typography and spacing language while protecting:

- a clear reading order and heading structure;
- legibility at supported text scaling and zoom;
- wrapping and available space for realistic and localized content;
- deliberate truncation with a way to access required information;
- labels and values that remain associated visually and programmatically; and
- foreground/background relationships that meet the applicable accessibility
  target across supported states and themes.

Do not shorten, rewrite, or invent interface copy to solve a layout problem.
When Scribe is available, route variable wording through it; otherwise preserve
existing copy or treat the wording as a separate verified text decision. Fix
the presentation constraint here.

## Make interaction predictable

Use existing components and platform conventions so affordance and behavior
agree. For the states introduced or changed by the task, preserve the cues and
recovery needed to answer:

- What can I act on?
- What has focus or selection?
- Did the action start, succeed, fail, or become unavailable?
- What changed, and can I recover or retry?
- What input method and interaction sequence does this control support?

Do not depend on hover for required information or operation. Keep focus order,
keyboard behavior, touch behavior, programmatic relationships, announcements,
and motion accommodations intact. A custom visual treatment must not weaken the
owning component's semantics or state model.

## Adapt instead of merely shrinking

Responsive behavior preserves the task as space, content, text size, input
method, orientation, or window mode changes. Determine transformations from the
content and the project's supported breakpoints rather than imposing a fixed
device matrix.

Depending on the task and owner, adaptation may change flow, grouping,
disclosure, navigation, ordering, density, or interaction form. Preserve
meaning, required controls, status, and recovery. Do not clip, hide, or collapse
required content simply to eliminate overflow. Avoid separate interaction logic
for each viewport when one semantic flow can adapt through canonical layout
mechanisms.

## Design states as part of the same interface

Review only states affected by the change, including relevant initial, empty,
loading, partial, success, error, unavailable, and permission-dependent states.
Keep structure stable enough for orientation while making the state change
perceptible through more than one fragile cue. Place feedback where the user can
associate it with the action, and preserve a clear next step or recovery path.

Do not manufacture a complete state matrix for an unaffected component. The
floor is completeness for the requested flow, not ceremonial coverage.

## Keep accessibility structural

Accessibility is not a final color pass. Confirm that required names, labels,
roles, values, relationships, reading order, focus behavior, input alternatives,
scaling, and status communication survive the chosen component and layout.
Scribe owns the wording; UI owns whether the interface exposes and presents it
correctly.

Use the applicable standard or platform rule for quantitative requirements.
Do not invent substitute measurements or treat an automated scan as proof that
the interaction is usable.
