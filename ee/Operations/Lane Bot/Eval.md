# E&E Lane Bot Eval

Weekly precision/recall on `~/lanes/ee/golden.jsonl` (mbp-2). Promotion to live needs 90% precision for a week; demote under 80. Labels: 3 hand-labelled known misses + a provisional Sonnet pass (2026-11-13) corrected by Davey's feedback over time.

| date | golden | positives | T0 precision | T0 recall | T1 precision | T1 recall | T1 unsure | T0+T1 precision | T0+T1 recall | hand misses caught |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-13 | 1093 | 200 | 83.8 | 46.5 | 100.0 | 100.0 | 96.4 | 83.8 | 46.5 | 3/3 |
