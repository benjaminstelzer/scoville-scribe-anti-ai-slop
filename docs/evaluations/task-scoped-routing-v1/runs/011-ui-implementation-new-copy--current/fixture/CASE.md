# Routing case: ui-implementation-new-copy

## Scenario

The user asks to implement a responsive UI and formulate its labels, help text, and recovery error.

## Question

Decide which available Scoville Skill Cores apply to this task and which Scribe
references apply if Scribe is selected. Do not perform the described task.

Return exactly one JSON object with these keys in order and no additional text:

```json
{
  "skills": ["zero or more available Skill names in catalog order"],
  "scribe_references": ["zero or more Scribe reference paths in Core routing order"]
}
```
