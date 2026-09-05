# Scoville Scribe Anti-AI-Slop

Better wording is useful. Better wording that quietly changes the facts is not.

It usually looks harmless:

- "May reduce latency" becomes "will improve performance." Smoother, stronger,
  and no longer the same claim.
- A product setting named `Padding` becomes `Spacing` because repetition felt
  inelegant. The interface remains stubbornly literal.
- A summary keeps the result but drops "only when the cache is warm," which was
  the part keeping the result true.
- An error tells the user to retry even though the product offers no retry.
  Encouragement is not yet a control.

That is writing slop: the prose gets cleaner while meaning, terminology, or
behavior moves underneath it. The sentence is delighted. The product less so.

Scoville Scribe is an Agent Skill for requested text artifacts and
transformations: drafting, editing, rewriting, summarizing supplied sources,
localizing, source-exact work, interface text, and wording audits. It preserves
meaning, evidence, attribution, canonical terms, schemas, and behavior while
removing filler or fixing the requested wording problem. Ordinary answers,
explanations, status updates, and domain results stay with the host or their
domain owner. Merely containing prose is not an activation signal.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution. In writing, the
heat is the original meaning after smoothing, shortening, localization, and the
occasional thesaurus have all had access to the sentence.

## How to use

Name Scoville Scribe when wording must improve without changing its factual or
technical contract:

```text
Use Scoville Scribe to tighten this release note while preserving every claim, version number, condition, and uncertainty. Keep the existing product terminology.
```

```text
Use Scoville Scribe to localize these interface strings into German. Preserve placeholders, access keys, ICU branches, and the distinction between labels, help text, and errors.
```

```text
Use Scoville Scribe in Source-exact mode to extract the text between the named markers. Preserve the selected bytes and return nothing else.
```

Explicit `$scoville-scribe-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

```text
Install the complete Scoville Skill suite for all my projects. Fetch and install every exact package directory below:

https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
https://github.com/benjaminstelzer/scoville-research/tree/main/scoville-research
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/tree/main/scoville-design-anti-ai-slop
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
https://github.com/benjaminstelzer/scoville-plan/tree/main/scoville-plan
https://github.com/benjaminstelzer/scoville-handoff/tree/main/scoville-handoff

Preserve existing customizations and ask before overwriting conflicting files. Report every installed location and whether the host discovers each Skill.
```

## What it enforces

- **Facts survive the edit.** Numbers, quotations, conditions, attribution,
  modality, and uncertainty keep their meaning.
- **Canonical terms stay canonical.** A setting named `Padding` does not become
  `Spacing` because the thesaurus was feeling helpful.
- **Working strings keep working.** Placeholders, ICU branches, access keys,
  shortcuts, schemas, and accessible names retain their contracts.
- **Behavior-bound text stays true.** Interface labels, help, errors, and
  procedures describe supported behavior rather than desired fiction.
- **The author's position survives.** Voice may improve without inventing
  certainty, experience, identity, or conclusions.
- **Prose is built around sentences.** Rewrite sentences that rely on em
  dashes, en dashes, or semicolons instead of mechanically replacing the marks.
  Structure newly written or edited prose primarily with periods and commas,
  using `-` only sparingly when a dash is genuinely needed. Existing text outside
  the requested edit scope stays unchanged, as do exact quotations, protected
  source text, and technical syntax.
- **The requested operation stays narrow.** An audit reports. An edit changes
  the smallest real defect. Source-exact output remains exact.
- **Filler does not stand in for meaning.** Check unearned contrasts, vague
  authority, inflated significance, and decorative formatting. Interface copy
  names the actual action and state without unsupported reassurance or
  celebration. These are contextual editing checks, not authorship detection.

The complete contract is in
[SKILL.md](scoville-scribe-anti-ai-slop/SKILL.md).

## How it works

The Skill description first keeps ordinary conversation and domain-owned normal
results out of Scribe. Once an artifact or transformation activates the Core,
it resolves truth, terminology, audience, and requested transformation per
segment, then loads only the Interface, Prose, or Fidelity guide needed for
that segment. Chat delivery alone neither activates nor suppresses Scribe.

For repository structure and development tools, see
[maintenance notes](docs/maintenance.md).

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web,
  GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns
  visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  framework-aligned implementation, interface mechanics, accessibility, and
  rendered evidence, with a standalone design fallback.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

Earlier 30/30 qualification and token-reduction results belong to a historical
package. The changed activation contract has focused static and composed
routing evidence, not a measured token or latency advantage. See
[benchmark evidence](docs/benchmark-evidence.md) and
[task-scoped routing evidence](docs/evaluations/task-scoped-routing-v1/README.md).

A Terra Medium prose case on 2026-09-05 preserved a protected quotation and
removed unsupported emphasis, but weakened the attribution of an internal
trial. It is not proof of perfect fidelity or AI-authorship detection.

## Sources

- [W3C Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name)
  for visible control text and accessible names.
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
  for selector branches, runtime values, and localization contracts.
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/word-choice/use-technical-terms-carefully)
  for consistent product terminology.
- [Reinhart et al.](https://doi.org/10.1073/pnas.2422455122) and
  [Wang et al.](https://aclanthology.org/2025.findings-emnlp.532/) for limits of
  LLM style imitation and authorship inference.
- [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop) for
  reader-first editing and skepticism toward word-list detectors.

## License

MIT. See [LICENSE](LICENSE).
