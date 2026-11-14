# E&E Lane Bot Eval

Weekly precision/recall on `~/lanes/ee/golden.jsonl` (mbp-2). Promotion to live needs 90% precision for a week; demote under 80. Labels: 3 hand-labelled known misses + a provisional Sonnet pass (2026-11-13) corrected by Davey's feedback over time.

| date | golden | positives | T0 precision | T0 recall | T1 precision | T1 recall | T1 unsure | T0+T1 precision | T0+T1 recall | hand misses caught |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-13 | 1093 | 200 | 83.8 | 46.5 | 100.0 | 100.0 | 96.4 | 83.8 | 46.5 | 3/3 |
| 2026-11-13 | 1093 | 200 | 83.8 | 46.5 | 71.4 | 26.3 | 0.9 | 82.2 | 48.5 | 3/3 |
| 2026-11-13 | 1093 | 200 | 83.8 | 46.5 | 66.7 | 68.4 | 1.8 | 77.0 | 52.0 | 3/3 |
| 2026-11-13 | 1093 | 200 | 83.8 | 46.5 | 80.6 | 65.8 | 1.8 | 81.1 | 51.5 | 3/3 |

Row notes (all 2026-11-13 rows use the same 110-event Tier 1 sample; T0 columns use all 1093 golden events, so T0+T1 recall understates Tier 1):
1. Tier 1 v1: Qwen2.5-3B on mbp-2, yes/no/unsure, 5+5 few-shots. Almost always unsure.
2. Tier 1 v2: same 3B, yes/no only, thread context, 20+20 few-shots (Davey: tune only, no Gemini).
3. Tier 1 v3: moved to bigly qc30 (Qwen3-Coder 30B Q4_K_M, Ollama) with typography-tolerant grounding that swaps in the verbatim source quote.
4. Tier 1 v4: v3 plus the Tier 0 address gate before the model (greets someone else, tags others not Davey, sent from our own address, Davey only cc, bot relays). Current production config. Shadow until 90% precision for a week.
