# Framework Alignment

Use this reference to determine who owns a UI decision. Framework fidelity is
not passive obedience to every default; it is changing the interface through
the canonical layer that the product has chosen.

## Contents

- Find the owners
- Classify the stack
- Distinguish convention from accident
- Handle true greenfield work
- Resolve accessibility conflicts

## Find the owners

Inspect only sources relevant to the requested surface:

1. repository and product instructions;
2. installed dependencies and their versions;
3. product design-system documentation and shared UI packages;
4. provider setup, themes, semantic token definitions, component wrappers, and
   approved assets;
5. nearby, repeated rendered patterns and their source; and
6. official documentation for the installed version when supported behavior or
   customization remains uncertain.

Do not fetch mutable third-party skill files or generic design checklists at
runtime. Prefer installed source and version-matched official documentation.

## Classify the stack

### Styled design system

Examples include component systems that supply visual defaults, theme tokens,
variants, and layout conventions. Treat their supported components, semantic
tokens, theme extension points, and responsive APIs as the visual owner. Reuse
project wrappers before reaching for the underlying library directly.

Do not replace the system's spacing, typography, shape, elevation, color, or
breakpoint language with personal defaults. If a local need reveals a genuine
system gap, extend the canonical owner rather than building a parallel layer in
one feature.

### Headless component library

Treat the library as the owner of the behavior and semantics it implements:
state machines, focus movement, keyboard interaction, relationships, and
announcements. It does not supply a visual language unless the project has
added one around it. Derive appearance from project tokens, wrappers, and
neighboring surfaces while preserving the library's supported structure and
behavior.

### Utility or application framework

A rendering framework, CSS utility library, module system, or routing framework
does not by itself define the product's design language. Look for project
tokens, presets, component layers, and deliberate local patterns. When no such
owner exists, the framework's default value scale may supply coherent
implementation values, but it does not settle hierarchy, product meaning, or
visual direction.

### Platform UI stack

Native mobile, desktop, and terminal UIs inherit platform conventions for
navigation, input, focus, scaling, safe areas, window or viewport adaptation,
and accessibility. Use platform components and adaptation mechanisms unless the
canonical product system explicitly owns the concern. Do not translate web-only
measurements or interaction assumptions into another platform.

### Multiple layers

Assign each concern independently. A styled component system may own visuals,
a headless primitive may own a composite interaction, the platform may own text
scaling, and Scribe may own visible wording. Prefer the highest canonical layer
that intentionally abstracts the lower one. Do not mix APIs from several layers
merely because they are all installed.

## Distinguish convention from accident

A repeated local pattern can resolve an otherwise open decision when it is
clearly intentional, current, and appropriate to the same surface. Check its
source, frequency, and relationship to canonical wrappers or tokens. Do not
promote one copied exception, stale screen, or workaround into product policy.

If a deliberate local convention diverges from a lower-level framework default,
treat it as project-level evidence. If ownership remains material and unclear,
ask or report the conflict instead of normalizing the interface in either
direction.

Apply this invariant before normalizing a local exception:

- Evidence establishes deliberate, current intent: preserve the exception as
  project-level evidence when it is appropriate to the surface.
- Evidence establishes an accidental or stale exception: normalize through the
  canonical owner.
- Intent is unknown or conflicting: ownership remains unresolved. Inspect or
  ask for intent; never infer that the exception is accidental.

## Handle true greenfield work

When there is no design system, theme, token set, approved precedent, or visual
owner:

When polished presentation is requested, the requested surface owns a
deliberate local direction. Framework defaults may supply compatible primitives
and scales, but they never become the visual owner.

1. follow the user's brief and target platform conventions;
2. use framework defaults and scales where they provide compatible primitives;
3. when polished presentation is part of the outcome, name a deliberate visual
   direction grounded in the product domain and primary task, then carry it
   consistently through information hierarchy, density, typography, shape,
   imagery, and interaction treatment without defaulting to a prescribed
   palette or fashionable template;
4. choose only the minimum internally consistent, reversible values needed for
   the requested surface; and
5. keep those choices local unless the task explicitly creates or extends the
   canonical design system.

Do not pretend a single screen's choices are a mature project-wide system. Ask
only when materially different visual directions would change the product
outcome.

## Resolve accessibility conflicts

Use WCAG 2.2 Level AA as the web fallback when the project declares no target;
for native, desktop, and terminal UI, use the owning platform's current
accessibility guidance. Implement the requirement through supported framework
and project mechanisms.

If the canonical design system cannot meet the floor, identify the exact owner
and limitation. Do not work around it with an isolated parallel visual language.
An explicit, informed user decision may accept a reported limitation against a
non-binding target, but never overrides system, safety, or legally binding
requirements.
