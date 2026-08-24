# Rendered UI Validation

Choose the cheapest rendered evidence that could disprove the implementation.
Validation depth follows the changed behavior and risk, not a fixed screenshot
ritual.

## Contents

- Establish the claim
- Derive the test surface
- Inspect the rendered result
- Use automation as supporting evidence
- Handle reviews and missing renderers
- Report the result

## Establish the claim

State what the change is supposed to improve and which observable result would
show it. Separate claims about:

- source or build correctness;
- framework and token alignment;
- rendered layout and hierarchy;
- interaction and state behavior;
- responsive or adaptive behavior; and
- accessibility conformance.

Evidence for one category does not prove another. A passing build cannot prove
that text is visible; one screenshot cannot prove keyboard operation; an
automated audit cannot prove that a task is understandable.

## Derive the test surface

Use the project's supported environments and the conditions affected by the
change. Select only relevant combinations of:

- viewport, window mode, orientation, or safe-area constraints;
- mouse, keyboard, touch, switch, or platform navigation;
- default, focus, hover, pressed, selected, disabled, loading, success, error,
  empty, or permission states;
- supported themes and contrast modes;
- realistic short, long, dynamic, and localized content; and
- text scaling, browser zoom, reduced motion, and other supported user settings.

Do not impose a universal breakpoint list or test every possible combination.
Include a condition when it could change the decision or expose a failure in the
requested flow.

When a flow supports multiple input methods and one method can leave focus,
selection, pointer capture, composition, or shared state that affects another,
exercise at least one relevant handoff in the same task, such as pointer to
keyboard. Separate clean-start passes for each method do not prove that the
transition works. Do not create a cross-input matrix when the methods are
behaviorally independent.

When polished presentation is an explicit outcome, rendered evidence must show
a representative populated state rather than only an empty, loading, or error
state. Use realistic information density, content lengths, hierarchy, and at
least one relevant interaction state. Capture each target viewport named by the
task as its own observation so a desktop result does not stand in for mobile or
vice versa. Keep recovery-state evidence separate: a convincing error state
does not prove the primary populated surface, and the reverse is equally true.

## Inspect the rendered result

When practical:

1. render the nearest before state or inspect the existing surface;
2. exercise the changed task through its relevant interaction path;
3. inspect affected states and transitions, not only the settled appearance;
4. vary the relevant space, content, and user settings;
5. confirm focus, reading order, programmatic names and relationships, feedback,
   and recovery where the task touches them; and
6. compare the result with the owning components, tokens, and neighboring
   surfaces.

Use screenshots for spatial evidence and interaction tooling or platform
inspection for behavior. Measure computed values or accessibility properties
when visual inspection cannot establish the claim.

## Use automation as supporting evidence

Run focused component, integration, visual-regression, and accessibility checks
already owned by the project when they cover the change. Add or change automated
coverage only when it protects a behavior that can regress and the repository
has a canonical test seam. Do not create screenshot churn or assertion-free
tests to simulate proof.

Treat scanner output as a lead and a bounded check. Confirm relevant findings in
the rendered interface and interaction path.

## Handle reviews and missing renderers

For an audit without an implementation request, inspect the available rendered
surface and return prioritized findings with the observed evidence, affected
task, owner, and consequence. Do not silently redesign or edit.

If no browser, simulator, device, terminal harness, or runnable application is
available, inspect source only far enough to identify likely risks. Report
rendered behavior, responsiveness, and visual quality as unverified. Do not turn
absence of evidence into a pass.

## Report the result

Report:

- the surfaces and conditions actually rendered;
- the task and states exercised;
- relevant automated checks and their result;
- framework or design-system alignment observed; and
- residual unverified conditions or owner conflicts.

When supplied evidence explicitly names unobserved conditions that bound the
requested claim, retain those conditions individually or in an equally precise
grouping. A broad caveat does not preserve a narrower evidence gap.

Avoid generic claims such as "responsive," "accessible," or "looks good" when
the evidence covers only a narrower condition.
