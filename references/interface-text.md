# Interface Text

Use this reference for reader-facing product text: GUI, CLI, installers, console
or API errors, notifications, email, accessibility text, and metadata values.

## Inspect the relevant project state

Use the smallest targeted inspection that can answer the text decision. Check,
as applicable:

- the requested final behavior and product requirements;
- the affected component, command, state transition, or returned error;
- the glossary, design system, string catalog, and localization rules;
- shared strings and established terms on the same or neighboring surface;
- documentation only where it agrees with product behavior;
- runtime formatting, accessibility, and rendered-space constraints.

Do not run a repository-wide terminology rewrite for one surface. If behavior,
terminology, and documentation disagree materially, report the exact conflict.
Do not make a prose choice stand in for a product decision.

## Keep concepts and terms aligned

Use one canonical term family for one concept. Inflection, grammatical case,
pluralization, and locale-specific forms may differ. Similar-looking concepts
may require different terms. Removing a membership, for example, is not the
same operation as deleting the person's account.

When sources agree on meaning, prefer an explicit product requirement, then a
maintained glossary, a shared string for the same component and state, relevant
neighboring usage, and finally documentation that matches behavior.

Do not vary a product term for rhythm. Search likely variants when auditing
consistency, then verify the concept behind each occurrence before changing it.

## Describe the user-relevant state

State what is true in the supported state represented by the artifact. Describe a
requested final state only when it ships with the behavior and Scoville verifies
it before completion or publication. Omit internal causes, discarded tools,
issue chronology, and unreleased alternatives.

Mention an older state only when users could have encountered it and need that
history to migrate, understand a deprecation, avoid harm, or recover from a
specific failure. Put ordinary release history in release or migration text,
not in routine labels, help, or empty states.

## Match wording to behavior

- Name an action by its actual result. `Save`, `Apply`, `Create`, `Add`,
  `Remove`, `Delete`, `Upload`, and `Transfer` are not interchangeable.
- Use the same concept term in an action, its status, and its confirmation.
- Name the affected object in destructive actions and confirmations.
- In an error, state the problem and an available next action. Do not imply a
  prior action unless verified, or offer retry unless it is available and safe.
- Promise success, duration, reversibility, privacy, or support only when
  verified product behavior supports it.
- Include only information that changes understanding, choice, or next action.

## Preserve runtime and localization contracts

During an edit, preserve string keys and placeholder names, types, and escaping.
Do not add, drop, or duplicate occurrences silently. Change an occurrence count
only when the wording requires it and the schema accepts it. Preserve ICU `plural`, `select`,
`selectordinal`, and required `other` branches; markup; interpolation boundaries;
access-key syntax; shortcuts; command literals; and accessibility relationships
unless the task changes that contract. Runtime and intentional template placeholders are not drafting markers.

During localization, preserve lookup keys, argument names and types, selector
meaning, escaping, schema, and required fallback behavior. Allow the locale to
add required plural or ordinal branches, reorder, repeat, or omit an argument
where the message remains true, choose a different unique access key, and change
sentence structure or wrapping. Translate complete messages and keep the locale's
canonical term family consistent.

## Cover non-visible interface text

Accessible names must describe purpose or action, not only icon shape or screen
position. When a control has a visible text label, its accessible name must
contain that text, preferably at the start. It may add necessary context but
must not replace the visible wording.

Describe only known content in alt text, previews, metadata, and structured
data. Preserve structured-data keys, types, and schema when editing its
human-language values. Do not infer visual details, authorship, product
features, or search claims from a filename or development note. Status messages
must expose meaningful state changes when the interface relies on them.

## Verify in context

Where the artifact permits it:

1. Re-run the relevant term search for same-concept consistency.
2. Compare runtime tokens and message branches with the original.
3. Exercise the action or state and compare wording with the result.
4. Inspect rendering, wrapping, keyboard use, and accessible name.
5. Check every materially different changed ICU or state branch and at least one
   representative variable expansion.

A spelling or word-list check does not verify interface text.
