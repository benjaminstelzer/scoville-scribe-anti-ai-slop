# Scoville Scribe Anti-AI-Slop

Keeps the meaning. Cuts the slop.

You ask an agent to improve a piece of writing. It returns something smoother
and less true:

- The project calls a setting `Padding`; the new help text calls it `Spacing`.
- A tool was removed before release; the UI now tells users it is unavailable.
- "I had enough information" becomes "I knew enough," changing evidence into
  an inferred mental state.
- A translated message loses its separate wording for one or many items, or a
  value such as `{fileName}` that the software inserts when it runs.

That is prose slop: language work that looks finished but makes the text less
useful or less true. Scoville Scribe Anti-AI-Slop is an Agent Skill—a reusable
instruction file for coding agents. Whether the agent drafts, edits, reviews,
adapts, or translates text, Scribe keeps it faithful to the source, the product,
the writer's voice, and the words the project already uses.

It may improve a sentence. It does not get to improve what happened.

It does not diagnose AI authorship or promise detector evasion. It fixes a
pattern only when that pattern harms the reader's task or conflicts with source
meaning, genre conventions, or interface constraints.

## Why "Scribe"?

Scoville Code's engineering guardrail keeps a coding task focused on the result
the user asked for. Scribe does the same for writing: it keeps the text focused
on what the reader needs to understand or do. The first stops plans and tests
from replacing the code change; the second stops polished wording from
replacing the truth.

The name also describes the range. Scribe can draft, edit, audit, adapt,
localize, or preserve exact source text. It is not limited to marketing copy or
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
the skill directory under the unchanged name `scoville-scribe-anti-ai-slop`,
and refresh its skill list.

If your agent cannot install skills itself, copy the repository's
`scoville-scribe-anti-ai-slop/` directory so the final path is:

```text
<skills-dir>/scoville-scribe-anti-ai-slop/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` for all projects or
`.claude/skills/` inside a repository for that project only. For other agents,
consult their documentation; paths differ per agent.

### Use Scribe for agent communication

Installing Scribe makes it available to the agent's skill system, but does not
automatically make every conversational reply use it. To apply Scribe to all
user-facing communication in a project, send your agent this prompt:

```text
Add the following as a standing project instruction, using the instruction file
supported by this agent:

## Conversational writing

Apply `$scoville-scribe-anti-ai-slop` to all user-facing communication,
including questions, progress updates, explanations, and final responses. Apply
it without announcing or describing its use unless the user explicitly asks.
Follow the skill's prose and interface routing rules when applicable.
```

The exact project instruction file depends on the agent. It may be called
`AGENTS.md`, `CLAUDE.md`, or something else. Adding the rule there makes it a
persistent instruction for that project, so Scribe governs ordinary replies as
well as writing tasks that mention it by name.

This does not force every piece of text into the agent's conversational voice.
If a reply contains a document, email, or interface label, that part still
follows its own source, audience, style, and technical requirements.

The host prompt, project instructions, request, and Scribe act together while
the agent writes. Scribe is not a second pass over an otherwise finished answer.
The surface boundary selects the applicable voice rules without making one
instruction layer solely responsible for the output.

**Verify it works.** If your agent loads skills on demand, test the trigger. Ask
your agent:
*"This project calls the layout concept Padding. Rewrite the related UI label
and help text, and mention that the internal Spacing tool is unavailable."* The
result should retain `Padding` and omit the internal tool if users never knew it
existed.

**What it costs.** `SKILL.md` currently contains 975 words of rules plus 86
words for its name and description. Tasks involving buttons, errors, or other
interface text load another 790 words. Tasks involving paragraphs or an
explicit anti-slop request load another 1,240. Tasks involving both load both
guides. The agent counts this text as part of the context it reads for the task.

## Use with Scoville Code and UI

Use [Scoville Code Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop)
when the text belongs to a codebase or engineering change. Code keeps the
code change in the right place, checks that it works, and prevents unrelated
work. Scribe keeps the reader-facing words factual, clear, and consistent with
the product's vocabulary.

Use [Scoville UI Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop)
when interface presentation or interaction is also changing. UI owns framework
alignment, hierarchy, layout, responsiveness, and the presence and association
of required labels or accessible names. Scribe owns their wording and meaning.

They work toward the same requested result but handle different parts of it.
For an error message in `errors.ts`, Code proves that the correct error reaches
the user, UI verifies its placement and interaction context, and Scribe makes
the message factual, actionable, and consistent with the rest of the product.

## What it enforces

- **The facts survive the edit.** Numbers, quotes, conditions, who said or did
  something, what did or did not happen, and the difference between `can`,
  `should`, and `must` keep their meaning. Smoother wording does not get to
  strengthen the evidence.
- **The product keeps its own vocabulary.** If the interface calls a setting
  `Padding`, Scribe does not rename it `Spacing` because the thesaurus was
  feeling helpful.
- **Interface text describes the product users actually have.** Labels, help,
  and errors explain available actions and current behavior. A tool removed
  before release does not need an obituary in the UI.
- **Working messages stay working.** Placeholders such as `{fileName}`, singular
  and plural variants, internal string identifiers, keyboard shortcuts, and
  accessible names and labels survive the rewrite.
- **The author still means what they wrote.** Strong passages stay. Edits
  preserve what the writer claimed, how certain they were, and whose experience
  or judgment it was.
- **Explanations explain.** When readers need the mechanism, Scribe includes the
  reason something happens and a useful example or contrast. A load-bearing
  example follows one concrete instance to its observable result instead of
  merely naming cases. An otherwise categorical explanation of practical
  usefulness, risk, or failure grounds itself in one representative case.
  Scribe visibly mirrors genuinely separate dimensions, can use a marked
  hypothetical counterexample, and demonstrates weak small-sample evidence
  with a visibly hypothetical rate. It lands on a transferable rule when that
  adds real compression and separates what the evidence shows from what the
  writer concludes without forcing every answer into the same template.
- **The requested job stays the job.** An audit reports problems without
  rewriting the text. An edit changes only what needs fixing. A draft stays
  inside the facts it is allowed to use.

## UI and prose use separate guidance

The core rules live in
[SKILL.md](scoville-scribe-anti-ai-slop/SKILL.md). Depending on the task, the
agent also reads one or both of these focused guides:

- [references/interface-text.md](scoville-scribe-anti-ai-slop/references/interface-text.md)
  covers buttons and other graphical controls, command-line text, errors,
  notifications, screen-reader labels, messages assembled by software, and
  descriptive fields such as titles or alternative text.
- [references/prose-patterns.md](scoville-scribe-anti-ai-slop/references/prose-patterns.md)
  covers manuals, articles, email, documentation, explanatory analyses, author
  voice, and source-near editing.

The agent reads only what the current task needs. Buttons, errors, and other
interface text use the interface guide. Paragraphs, articles, and other
continuous writing use the prose guide. A task containing both uses both.

## Design

Scribe answers three separate questions: Is the text true? Does it use the
product's established words? Does it fit the requested format and voice? The
running product can show what is true but cannot choose a writing style. A
glossary can settle whether the setting is called `Padding` or `Spacing` but
cannot make a false status message true. Different questions need different
sources.

The rules apply to each part of a text rather than blindly to the whole file. A
settings page can contain a heading, explanation, button, error message, and a
label used by screen readers. Each part keeps the rules it needs without being
forced into one writing style.

Some details are never traded away for smoother style: facts, the difference
between `can`, `should`, and `must`, placeholders such as `{fileName}`, and
claims about what the product does. A score from an AI-text detector cannot
overrule any of them.

## Research basis

The skill draws from these sources:

- [W3C Understanding SC 2.5.3: Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name): the name read by assistive software must include the words users can see on the control.
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/): translated messages may contain separate wording for one item, many items, or other cases; every variant and inserted value must keep working.
- [Microsoft Writing Style Guide: Use technical terms carefully](https://learn.microsoft.com/en-us/style-guide/word-choice/use-technical-terms-carefully): product terms should remain consistent rather than vary for rhythm.
- [Reinhart et al., Do LLMs write like humans?](https://doi.org/10.1073/pnas.2422455122): models trained to follow instructions can still produce dense, information-heavy prose that does not fit the requested type of writing.
- [Wang et al., Catch Me If You Can? Not Yet](https://aclanthology.org/2025.findings-emnlp.532/): a few samples can help a model imitate structured writing more reliably than subtle informal voice, so samples guide the result but cannot guarantee a perfect match.
- [Microsoft Writing Style Guide: Em dashes](https://learn.microsoft.com/en-us/style-guide/punctuation/dashes-hyphens/): em dashes are valid for a break or parenthetical remark, but repeated interruptions can make prose harder to read.
- [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop): reader-first editing, meaning preservation, and skepticism toward word lists that claim to identify AI writing by style alone.

## Repository contents

The installable `scoville-scribe-anti-ai-slop/` directory contains the core
instruction file, two focused guides, and a small file that helps agents display
the skill. This README, the changelog, and the MIT license remain at the
repository root and are not installed as skill instructions. The repository
contains no executable software, model requests, AI detector, or generated
files.

## License

MIT, see [LICENSE](LICENSE).
