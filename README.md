# Scoville Scribe Anti-AI-Slop

Better wording is useful. Better wording that quietly changes the facts is not.

Scoville Scribe is an Agent Skill for drafting, editing, summarizing,
localizing, source-exact work, interface text, and prose audits. It preserves
meaning, evidence, attribution, canonical terms, schemas, and behavior while
removing filler or fixing the requested wording problem. It does not own code
semantics, layout, or durable planning structure, no matter how persuasive the
new sentence sounds.

## Why "Scoville"?

The family is named for useful signal that survives dilution. In writing, the
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

Use an Agent Skills-compatible host and Terra 5.6 Medium or a comparably
capable executor such as Opus 4.8. Ask the agent to install:

```text
Install this Agent Skill and refresh the available Skill list:
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
Keep the installed directory name scoville-scribe-anti-ai-slop. Use Terra 5.6 Medium or a comparably capable executor such as Opus 4.8.
```

The final path must end in
`<skills-dir>/scoville-scribe-anti-ai-slop/SKILL.md`. For Claude Code, use
`~/.claude/skills/` globally or `.claude/skills/` inside one project. Other
hosts use their supported Skills directory.

**What it costs.** The 1,430-token Core is 19.84% smaller than `v1.0.6`;
interface, prose, and fidelity guidance loads only when needed. The added
context buys factual fidelity, terminology control, and source-exact handling.
Use it for consequential or behavior-bound text; skip it for a disposable
draft when token use matters more. See
[benchmark evidence](docs/benchmark-evidence.md).
The [family run ledger](docs/optimization-history.md) shows the complete count.

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
- **The requested operation stays narrow.** An audit reports; an edit changes
  the smallest real defect; Source-exact output remains exact.

The complete contract is in
[SKILL.md](scoville-scribe-anti-ai-slop/SKILL.md).

## How it works

The Core resolves truth, terminology, audience, and requested transformation
per segment. It then loads only the Interface, Prose, or Fidelity guide needed
for that segment. Runtime behavior can establish truth, a glossary can settle
terminology, and a voice sample can guide form; none is allowed to moonlight as
the other two.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  interface hierarchy, framework fit, accessibility, and rendered evidence.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

A reliability-first extension of
[Microsoft SkillOpt](https://github.com/microsoft/SkillOpt) tested the six
Scoville Skills across **1,201 optimization and evaluation runs**. Scoville
Scribe passed **30/30 final cases** and its always-loaded instructions use
**19.84% fewer tokens than v1.0.6**. See
[benchmark evidence](docs/benchmark-evidence.md).

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

MIT - see [LICENSE](LICENSE).
