# Scoville Scribe benchmark evidence

## Final reliability-first qualification

The promoted package is the candidate from
`scoville-scribe-final-v6-v9-activation-bound-open-ab`, qualified on
2026-08-10. Routing used `gpt-5.6-sol` at `xhigh`; execution used
`gpt-5.6-terra` at `medium`. Network access and prediction reuse were
disabled.

| Arm | Split | Cases passed |
| --- | --- | ---: |
| Reliability control | Train | 18/18 |
| Reliability control | Validation | 9/9 |
| Reliability control | sealed Test | 3/3 |
| Compressed package | Train | 18/18 |
| Compressed package | Validation | 9/9 |
| Compressed package | sealed Test | 3/3 |

The candidate passed the hard result, exact routing, execution-semantic,
process, and efficiency gates in all 30 cases. It completed with provider
usage, zero routing retries, zero shell calls, and exact-once routed reads.
The sealed Test ran once per arm through separate fresh agents after the open
gate passed.

Two reliability-control Validation results differed from the expected text by
one final line-feed byte. Their text and Boolean semantics were otherwise
identical, and routing, process, efficiency, provider, and read-ledger checks
passed. They are retained in the raw scorer evidence as formatting false
negatives and do not count as Skill failures.

## Token effect

Token counts use `o200k_base` over the exact UTF-8 Skill files loaded for each
execution.

| Split | Reliability control | Compressed package | Change |
| --- | ---: | ---: | ---: |
| Train | 34,542 | 32,217 | -2,325 (-6.73%) |
| Validation | 22,590 | 21,195 | -1,395 (-6.18%) |
| sealed Test | 10,799 | 10,334 | -465 (-4.31%) |
| Total | 67,931 | 63,746 | -4,185 (-6.16%) |

These are literal executor-loaded Skill instruction tokens. Provider totals
also include routing, generation, and cache behavior, so they are not used as
the deterministic compression measure.

For the public previous-release comparison, the always-loaded Core is measured
directly with the same tokenizer: `v1.0.6` used 1,784 tokens and `v1.0.7` uses
1,430, a reduction of 354 tokens (-19.84%). This comparison is separate from
the reliability-matched benchmark control above.

## Reproducibility bindings

- Promoted Core SHA-256:
  `4B19990AABD3872AEF9BF5617D2E4E1A1C1010B9AFE7C367BBD7BCF88A110F70`
- Qualified candidate package-tree SHA-256:
  `749410D5937A3852F3CE1CF2020991A7A5B52069E37E2F044F63E76D4B8B56EC`
- Reliability-control package-tree SHA-256:
  `DDCC9A97995566F8C8569C1134A54EFAE7A1E3B7E8604C496C61387E529C3913`
- Open qualification report SHA-256:
  `B4A52412BEC8A26916883F56820410DA3FFE6F1F79E91E321539571FE816B94C`
- Test gate SHA-256:
  `10F6480048C94085433C8B525CB70E70D4976C4ED120A473581B4FF3CF02A9EF`
- Frozen benchmark lock SHA-256:
  `C82BC1F520C61D1CC1DFD85107DB692CE55A8D95CB7D5E3EE25471827C1AA63B`
- SkillOpt revision: Microsoft
  `ba820b500f9da96685cf2780c7dc85ed4eb6563e`

The complete reports, per-case metrics, final answers, traces, provider usage,
and one-shot Test claims remain in the central optimization workspace under
`skillopt-studio/runs/scoville-scribe-final-v6-v9-activation-bound-open-ab/`.

## Overall optimization history

The final four-Skill inventory records 797 run artifacts, including 742
technically valid benchmark runs, 5,762 observed model calls, and 3,452 case
executions. Scribe accounts for 181 artifacts, 175 valid benchmark runs, 1,216
model calls, and 753 case executions. The central machine-readable snapshot has
SHA-256
`1270F95CF9777EBC8E97151E37DFA5525D3E2DB8A6F0163DFBD71C8DA395A781`.

## Interpretation limits

The result establishes non-regression and lower prompt payload on the frozen
cases. It does not prove universal correctness, deterministic behavior, or the
same result on a weaker executor.
