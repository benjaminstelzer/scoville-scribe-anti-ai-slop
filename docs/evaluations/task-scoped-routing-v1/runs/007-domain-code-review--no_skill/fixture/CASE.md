# Routing case: domain-code-review

## Scenario

The user asks to review a patch for correctness and return actionable findings without drafting a separate publication artifact.

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
