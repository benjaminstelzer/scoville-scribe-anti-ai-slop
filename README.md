# Scoville Scribe Anti-AI-Slop

Keeps the meaning. Cuts the slop.

You ask an agent to improve a piece of writing. It returns something smoother
and less true:

- The project calls a setting `Padding`; the new help text calls it `Spacing`.
- A tool was removed before release; the UI now tells users it is unavailable.
- "I had enough information" becomes "I knew enough," changing evidence into
  an inferred mental state.
- A translated message loses its singular branch or a runtime value such as
  `{fileName}`.

That is prose slop: language work that looks finished but makes the text less
useful or less true. Scoville Scribe is an Agent Skill for drafting, editing,
auditing, adapting, localizing, and preserving source-exact text. It protects
facts, source meaning, author voice, product vocabulary, and runtime text
contracts. It does not diagnose AI authorship or promise detector evasion.

It may improve a sentence. It does not get to improve what happened.

## Why "Scoville Scribe"?

The Scoville family is named for heat you can still detect after dilution.
Scribe applies that idea to language: the useful signal should remain visible
after an edit instead of disappearing under polished filler. Its version of
seasoning is deliberately conservative. It may sharpen the sentence, but it
does not swap the ingredients or rewrite the recipe card.

`Scribe` describes the range. The skill can draft, edit, audit, adapt,
localize, or preserve exact source text; it is not limited to marketing copy or
long-form prose.

## Install

Works with any coding agent that supports the Agent Skills format: a `SKILL.md`
instruction file with its name and description at the top. Compatible agents
include Claude Code and Codex.

Usually, let your coding agent install the skill. Send it this prompt:

```text
Install this Agent Skill from GitHub and make it available for my writing work:
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
```

Add "for all my projects" or "only for this project" when the installation
scope matters. The agent should choose its supported skills directory, install
the skill directory under the unchanged name
`scoville-scribe-anti-ai-slop`, and refresh its skill list.

If your agent cannot install skills itself, copy the repository's
`scoville-scribe-anti-ai-slop/` directory so the final path is:

```text
<skills-dir>/scoville-scribe-anti-ai-slop/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` for all projects or
`.claude/skills/` inside a repository for that project only. For other agents,
consult their documentation; paths differ per agent.

**Verify it works.** Ask the agent: *"This project calls the layout concept
Padding. Rewrite the related UI label and help text, and mention that the
internal Spacing tool is unavailable."* The result should retain `Padding` and
omit the internal tool if users never knew it existed.

**What it costs.** `SKILL.md` currently contains 1,222 words of rules plus 131
words for its name and description. Interface-text tasks can load another 821
words; prose tasks or explicit anti-slop requests can load another 1,300. A
task involving both surfaces can load both guides.

## What it enforces

- **The facts survive the edit.** Numbers, quotations, conditions, attribution,
  events, and the difference between `can`, `should`, and `must` retain their
  meaning. Smoother wording does not strengthen the evidence.
- **The product keeps its vocabulary.** A setting named `Padding` does not
  become `Spacing` because the thesaurus was feeling helpful.
- **Interface text describes the product users have.** Labels, help, and errors
  explain available actions and current behavior. An unreleased tool does not
  need an obituary in the UI.
- **Working messages stay working.** String keys, placeholders, ICU branches,
  access keys, keyboard shortcuts, accessible names, and localization contracts
  survive the rewrite.
- **The author still means what they wrote.** Strong passages stay. Edits
  preserve what the author claimed, how certain they were, and whose experience
  or judgment it was.
- **Explanations explain.** When readers need the mechanism, Scribe supplies the
  causal link, a useful example or contrast, and the material boundary. It can
  use visibly hypothetical counterexamples, preserves meaningful numeric
  invariants, and accounts for every enumerated completion condition before
  compressing a status.
- **The requested job stays the job.** An audit reports defects without silently
  rewriting them. An edit changes the narrowest real problem. A summary may
  omit detail, but it may not distort the claims it retains.

The full rules live in
[SKILL.md](scoville-scribe-anti-ai-slop/SKILL.md).

## Use with the Scoville family

Scribe works independently. When companion Skills are installed, combine them
only for the concerns they own.

Use [Scoville Code Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop)
when text belongs to a codebase or engineering change. Code owns engineering
scope, canonical implementation, and behavior verification; Scribe owns the
reader-facing words.

Use [Scoville UI Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop)
when presentation or interaction also changes. UI owns framework alignment,
hierarchy, layout, responsiveness, and whether required labels or accessible
names exist and are associated. Scribe owns what those labels and names mean.

For an error message in `errors.ts`, Code proves that the correct error reaches
the user, UI verifies its placement and interaction context, and Scribe makes
the message factual, actionable, and consistent with the product vocabulary.

Installing Scribe makes it available to the host's skill system. A host that
does not automatically use it for ordinary conversation can receive a standing
project instruction to apply `$scoville-scribe-anti-ai-slop` to user-facing
communication. That instruction selects the installed skill; it is not a
second copy of the skill rules. Documents, emails, and interface text still
follow their own source, audience, genre, and technical constraints.

## Design

Scribe resolves three separate questions from the source that can answer each
one: Is the text true? Does it use the project's established terms? Does it fit
the requested form and voice? Running behavior can establish truth but cannot
choose an authorial voice. A glossary can settle `Padding` versus `Spacing` but
cannot make a false status message true.

The rules apply per segment rather than forcing a whole artifact into one
profile. A settings page can contain a heading, explanation, button, error,
runtime placeholder, and accessible name. Each segment keeps the rules it
needs.

The agent conditionally loads two focused guides:

- [references/interface-text.md](scoville-scribe-anti-ai-slop/references/interface-text.md)
  covers controls, CLI text, errors, notifications, accessible names, dynamic
  messages, and descriptive metadata.
- [references/prose-patterns.md](scoville-scribe-anti-ai-slop/references/prose-patterns.md)
  covers manuals, articles, email, documentation, explanatory analysis,
  author voice, and source-near editing.

## Sources and inspirations

- [W3C Understanding SC 2.5.3: Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name)
  for the relationship between visible control text and accessible names.
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
  for selector branches, runtime values, and localization contracts.
- [Microsoft Writing Style Guide: Use technical terms carefully](https://learn.microsoft.com/en-us/style-guide/word-choice/use-technical-terms-carefully)
  for consistent product terminology.
- [Reinhart et al., Do LLMs write like humans?](https://doi.org/10.1073/pnas.2422455122)
  and [Wang et al., Catch Me If You Can? Not Yet](https://aclanthology.org/2025.findings-emnlp.532/)
  for instruction-following and style-imitation limits.
- [Microsoft Writing Style Guide: Em dashes](https://learn.microsoft.com/en-us/style-guide/punctuation/dashes-hyphens/)
  for context-sensitive punctuation rather than blanket bans.
- [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop) for
  reader-first editing and skepticism toward authorship claims based on word
  lists.

## Repository contents

The installable `scoville-scribe-anti-ai-slop/` directory contains the core
instruction file, two focused guides, and display metadata. This README, the
changelog, and the MIT license remain at the repository root and are not loaded
as skill instructions. The repository contains no executable software, model
requests, AI detector, or generated files.

## Status

The installable directory passes the canonical Agent Skill validator. The
documented word costs match the current files. Scribe makes no claim that a
style detector can identify authorship or that one voice fits every surface.

## License

MIT - see [LICENSE](LICENSE).
