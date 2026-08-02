# Scoville Scribe

Keeps the meaning. Cuts the slop.

You ask an agent to improve a piece of writing. It returns something smoother
and less true:

- The project calls a setting `Padding`; the new help text calls it `Spacing`.
- A tool was removed before release; the UI now tells users it is unavailable.
- "I had enough information" becomes "I knew enough," changing evidence into
  an inferred mental state.
- A translated message loses an ICU branch or runtime placeholder.

That is prose slop: language work that weakens the reader outcome while looking
finished. Scoville Scribe is an Agent Skill that keeps drafting, editing,
auditing, adaptation, and localization tied to source meaning, verified product
behavior, author voice, project terminology, and the text's actual job.

It does not diagnose AI authorship or promise detector evasion. It fixes a
pattern only when that pattern harms this reader, source, genre, or interface.

## Why "Scribe"?

Scoville's engineering guardrail protects the requested observable outcome.
Scribe protects the intended reader outcome. The first stops code work from
drifting into ceremony; the second stops writing work from drifting into smooth
but unsupported copy.

The name also describes the range. Scribe can draft, edit, audit, adapt,
localize, or preserve exact source text. It is not limited to marketing copy or
long-form prose.

## Install

Works with any coding agent that supports the Agent Skills format (`SKILL.md`
with name/description frontmatter), including Claude Code and Codex.

Usually, let your coding agent install the skill. Send it this prompt:

```text
Install this Agent Skill from GitHub and make it available for my writing work:
https://github.com/benjaminstelzer/scoville-scribe
```

Add "for all my projects" or "only for this project" when the installation
scope matters. The agent should choose its supported skills directory, install
the repository under the unchanged name `scoville-scribe`, and refresh its skill
list.

If your agent cannot install skills itself, clone or copy the repository so the
final path is:

```text
<skills-dir>/scoville-scribe/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` for all projects or
`.claude/skills/` inside a repository for that project only. For other agents,
consult their documentation; paths differ per agent.

**Verify it works.** Skills load on demand, so test the trigger. Ask your agent:
*"This project calls the layout concept Padding. Rewrite the related UI label
and help text, and mention that the internal Spacing tool is unavailable."* The
result should retain `Padding` and omit the internal tool if users never knew it
existed.

**What it costs.** `SKILL.md` currently contains 784 words of rules plus 76
words of frontmatter. Interface tasks load another 745 words; continuous prose
tasks load another 447. Mixed artifacts load both references.

## Use with Scoville

Use [Scoville Anti-AI-Coding-Slop](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop)
when the text belongs to a codebase or engineering change. Scoville owns scope,
canonical implementation, behavior verification, and validation. Scribe owns
the reader-facing words and the smallest relevant terminology inspection.

They share a goal-first contract without duplicating each other. A change to an
error string in `errors.ts`, for example, uses Scoville to verify the error path
and Scribe to keep the message factual, actionable, and consistent with product
language.

## What it protects

- **Meaning and evidence.** Numbers, negation, modality, conditions, quoted
  text, attribution, and the stated basis of retained claims do not drift under
  a smoother paraphrase.
- **Project language.** One concept keeps one canonical term family. Similar
  concepts remain distinct, and stylistic synonym swapping never overrides the
  project's glossary or shared strings.
- **Current-state interface text.** Routine labels and help describe the
  supported state, not discarded tools, internal causes, or unreleased history.
- **Runtime structure.** Placeholders, ICU selectors, string keys, shortcuts,
  accessible relationships, and localization schemas survive ordinary edits.
- **Source and voice.** Good passages stay. Author-owned text keeps its speaking
  position, explicit propositions, uncertainty, and claim strength.
- **Mode boundaries.** Audit reports findings without silently rewriting; Edit
  makes the smallest useful change; Draft stays inside the allowed facts.

## UI and prose load separately

The core rules live in [SKILL.md](SKILL.md). It routes to two references:

- [references/interface-text.md](references/interface-text.md) covers GUI, CLI,
  errors, notifications, accessibility text, runtime messages, and metadata.
- [references/prose-patterns.md](references/prose-patterns.md) covers manuals,
  articles, email, documentation, author voice, and source-near editing.

An interface task does not pay for the prose reference. A manual edit does not
load ICU and accessibility rules unless the artifact also contains interface
text. Mixed artifacts load both because they need both.

## Design

Scribe resolves truth, terminology, and form separately. Product behavior can
answer what is true, but it cannot choose the house voice. A glossary can settle
the canonical term, but it cannot preserve a false status message. One source
ranking for every concern would make at least one of those decisions wrong.

Text profiles apply per segment rather than per file. A settings page can
contain a heading, explanatory paragraph, button, dynamic error, and accessible
name; each segment keeps the constraints that apply to it without forcing the
whole file through one writing style.

The integrity floor is hard. Style preferences do not compensate for lost
facts, altered modality, broken placeholders, or a product claim that was never
verified. Detector scores decide nothing.

## Research basis

The skill draws from these sources and the observed failure cases recorded
during its forward tests:

- [W3C Understanding SC 2.5.3: Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name): a visible control label must appear in its accessible name.
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/): localized messages need locale-specific plural and selector branches while preserving their runtime contract.
- [Microsoft Writing Style Guide: Use technical terms carefully](https://learn.microsoft.com/en-us/style-guide/word-choice/use-technical-terms-carefully): product terms should remain consistent rather than vary for rhythm.
- [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop): reader-first editing, meaning preservation, and skepticism toward surface-only AI tells.

## Repository contents

The repository is deliberately small: the core `SKILL.md`, two selectively
loaded references, agent metadata, this README, a changelog, and the MIT
license. It contains no runtime, model call, detector, or generated build output.

## License

MIT, see [LICENSE](LICENSE).
