# Scoville Scribe Anti-AI-Slop

A rewrite can sound better and say something different. "May reduce latency"
becomes "will improve performance", or a summary drops the condition that made
the result true. Those are changes to the claim, even if the prose reads smoothly.

Scoville Scribe is an Agent Skill for requested text artifacts and
transformations: drafting, editing, rewriting, summarizing supplied sources,
localizing, source-exact work, interface text, and wording audits. It preserves
meaning, evidence, attribution, canonical terms, schemas, and behavior while
removing filler or fixing the requested wording problem. Ordinary answers,
explanations, status updates, and domain results stay with the host or their
domain owner. Merely containing prose is not an activation signal.

If Scoville Plan is installed and owns native planning records, their writing,
rewriting, and wording audits stay with Plan unless you explicitly request
Scribe. Without Plan, Scribe remains usable under the existing record owner's
format and lifecycle rules. Neither Skill requires the other.
When you explicitly request Scribe alongside an applicable Plan, Scribe handles
wording while Plan still checks permitted edits, format, and lifecycle.

Explanatory text also needs to carry the reader through the reasoning. Scribe
checks whether concepts have been introduced, references are clear, and
instructions say what to do and what result to check. These checks apply to
blog posts, reports, help, and manuals, including text written in a personal
voice.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
In Scribe, that means preserving meaning through editing, shortening and translation.

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

## Compatibility

Any Agent Skills host that can read references/. No scripts, no network, no subagents. Whole-file Source-exact work needs a byte-preserving file read and write that keeps encoding, line endings and trailing whitespace (not a line-splitting shell reader). Developed for Codex and Claude Code; other hosts untested.

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
- **Canonical terms stay canonical.** A setting named `Padding` keeps that name
  so the reader can find it in the product.
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

## How it was developed

Scribe grew through writing tasks where an apparently better sentence changed
the meaning. I examine the source, the final text and the task history together
to find missing conditions, altered terms and explanations that still leave
the reader guessing. Those cases guide changes to the instructions.

I have also compared which references an agent loads and used
[paired optimization tests](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/blob/660ae1c863d4404c74a83af7aff56ea726fee4b2/CHANGELOG.md)
to examine a shorter Core. The [changelog](CHANGELOG.md) follows the resulting
work on activation, source-exact handling and explanatory text. The aim is to
spend context on the writing problem actually being solved.

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
