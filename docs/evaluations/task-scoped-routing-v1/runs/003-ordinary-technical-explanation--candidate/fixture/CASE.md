# Routing case: ordinary-technical-explanation

## Scenario

The user asks for an ordinary technical explanation of why a retry loop behaves as observed and what would prove the diagnosis. The wording is not intended for reuse.

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
