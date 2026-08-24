# Ordinary technical answer case

The retry loop waits 120 milliseconds between attempts and permits 16 attempts.
Functional tests pass. CPU cost on very large pages has not been measured.

Answer the user's ordinary conversational question: what is the maximum retry
window, what remains unknown, and what is the cheapest check that would resolve
that unknown? This answer is not intended for copying or publication.

Return exactly this JSON shape with no additional text:

```json
{
  "maximum_window_seconds": 1.92,
  "cpu_cost_status": "unmeasured",
  "next_check": "measure CPU on representative large pages"
}
```
