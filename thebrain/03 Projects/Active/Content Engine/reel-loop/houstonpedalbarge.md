# @houstonpedalbarge reel loop (Houston Pedal Barge)

Weekly Instagram reel learning loop, built from the trial-reel-loop skill. Written by `~/.claude/scripts/reel-loop/reel_loop.py` on davids-mbp-2 (Sundays 06:10 PT), read-only Graph API. One dated section per run, newest at the bottom. Each reel is compared only to this account's own median in the same window.

## Run 2026-10-31 (last 14 days: 9 reels, 8 with mature data)

Ranked by outlier multiple (plays / this account's median plays), then sends per reach. Skip 3s is the share of views that swiped away within the first 3 seconds (lower is better). Rows marked * are under 48h old: shown, but left out of the medians and the ranking.

| Date | Hook | Theme | Plays | Reach | Outlier x | Skip 3s | Avg watch s | Sends/reach | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-23](https://www.instagram.com/reel/De2cCLgpmfN/) | BYOB and come get LIT Houston!! #bacherloretteparty #part... | - | 2,170 | 1,943 | 9.6x | 38.6% | 9.5 | 2.37% | 0.72% |
| [2026-10-23](https://www.instagram.com/reel/De2XcHUDCSr/) | BYOB and come get LIT Houston, round 2 🍾👰‍♀️ Send this to... | - | 466 | 377 | 2.1x | 35.2% | 6.7 | 0.27% | 0.00% |
| [2026-10-24](https://www.instagram.com/reel/De5L8yJTyG7/) | Come see the dolphins with us! #thingstodohoustontx #htx... | - | 260 | 239 | 1.2x | 68.9% | 3.8 | 0.00% | 0.42% |
| [2026-10-27](https://www.instagram.com/reel/DfBTgU5N3Ue/) | It's still warm, Houston! We can't wait to see our in the... | - | 241 | 208 | 1.1x | 66.7% | 4.8 | 3.85% | 0.00% |
| [2026-10-22](https://www.instagram.com/reel/Dez73AyJ7Ou/) | It's still warm, Houston! We can't wait to see our in the... | - | 209 | 195 | 0.9x | 77.5% | 2.5 | 0.00% | 0.00% |
| [2026-10-27](https://www.instagram.com/reel/DfARe0SJLXR/) | The weather is perfect for a boat party! Call us and book... | - | 179 | 140 | 0.8x | 66.9% | 3.9 | 0.71% | 0.00% |
| [2026-10-19](https://www.instagram.com/reel/Derr--_TY5m/) | Book us for your birthday, bachelorette, or for some fun!... | - | 170 | 152 | 0.8x | 53.8% | 5.5 | 0.00% | 0.00% |
| [2026-10-28](https://www.instagram.com/reel/DfDPaBuC23b/) | "Get there early so you can be the DJ." Tatyana, Google r... | - | 24 | 19 | 0.1x | 59.1% | 3.5 | 0.00% | 0.00% |
| [2026-10-30*](https://www.instagram.com/reel/DfIY-sSvHNR/) | Halloween weekend on Clear Lake 🎃🚤 Costume optional. Cool... | - | 349 | 311 | - | 39.7% | 5.2 | 0.00% | 0.00% |

Account medians (8 mature reels): plays 225, reach 202, 3s skip 62.9%, avg watch 4.3s, sends/reach 0.13%, saves/reach 0.00%. Length band is unknown for every reel (duration is not in the Graph API), so outlier x compares against one account-wide median.

### Diagnosis

- Worst avg watch #1: 2026-10-22 "It's still warm, Houston! We can't wait to see...": 3s skip 77.5% vs account median 62.9%, avg watch 2.5s vs 4.3s; nothing lands, so change the angle entirely.
- Worst avg watch #2: 2026-10-28 "'Get there early so you can be the DJ.' Tatyana...": 3s skip 59.1% vs account median 62.9%, avg watch 3.5s vs 4.3s; hook works, middle sags, so cut the length and move the payoff earlier.
- Worst avg watch #3: 2026-10-24 "Come see the dolphins with us! #thingstodohoust...": 3s skip 68.9% vs account median 62.9%, avg watch 3.8s vs 4.3s; nothing lands, so change the angle entirely.
- Best by outlier: 2026-10-23 "BYOB and come get LIT Houston!! #bacherlorettep...": 9.6x the account median plays, 3s skip 38.6% vs account median 62.9%, avg watch 9.5s vs 4.3s, sends 2.37% of reach; hook and body both work, so repeat the structure with a new topic.

### What works here

- **Best reel** (as of 2026-10-31): 2026-10-23 "BYOB and come get LIT Houston!! #bacherlor..." ran 9.6x the median plays (3s skip 38.6%, avg watch 9.5s, sends 2.37% of reach)
- **Lowest 3s skip** (as of 2026-10-31): 2026-10-23 "BYOB and come get LIT Houston, round 2 🍾👰‍..." held best: skip 35.2% vs account median 62.9%, avg watch 6.7s
- **Most sent** (as of 2026-10-31): 2026-10-27 "It's still warm, Houston! We can't wait to..." drew the most sends: 3.85% of reach vs account median 0.13%
- **Short hooks (40 characters or fewer)** (as of 2026-10-31): 5.4x the median plays vs 0.9x without (2 vs 6 reels)

Directional only: 8 mature reels in the window. Patterns firm up around 20 reels.

### Next batch to test

1. **Subject** vs parent 2026-10-23 De2cCLgpmfN: keep the structure (hook is a 31-character statement, same pacing and caption shape; it held 3s skip 38.6%, avg watch 9.5s) and swap in a new subject: next in your queue: "Birthday math checks out 🎂 Send this to whoever...". Only the subject changes.
2. **Hook** vs parent 2026-10-22 Dez73AyJ7Ou: same footage, a new angle in the first frame and first line built on the best reel's hook shape (31-character statement); if this fails too, retire the angle. Only the hook changes.
3. **Length** vs parent 2026-10-28 DfDPaBuC23b: same hook and caption, recut shorter with the payoff inside the first 5 seconds. Only the length changes.
4. **Hook** vs parent 2026-10-24 De5L8yJTyG7: same footage, a new angle in the first frame and first line built on the best reel's hook shape (31-character statement); if this fails too, retire the angle. Only the hook changes.

<!-- reel-loop-state {"date": "2026-10-31", "found": 9, "ideas": [{"parent": "2026-10-23 De2cCLgpmfN", "variable": "subject"}, {"parent": "2026-10-22 Dez73AyJ7Ou", "variable": "hook"}, {"parent": "2026-10-28 DfDPaBuC23b", "variable": "length"}, {"parent": "2026-10-24 De5L8yJTyG7", "variable": "hook"}], "mature": 8, "median": {"avg_watch": 4.3425, "plays": 225.0, "skip": 62.900000000000006, "spr": 0.001326259946949602}, "works": [{"asof": "2026-10-31", "label": "Best reel", "text": "2026-10-23 \"BYOB and come get LIT Houston!! #bacherlor...\" ran 9.6x the median plays (3s skip 38.6%, avg watch 9.5s, sends 2.37% of reach)"}, {"asof": "2026-10-31", "label": "Lowest 3s skip", "text": "2026-10-23 \"BYOB and come get LIT Houston, round 2 \ud83c\udf7e\ud83d\udc70\u200d...\" held best: skip 35.2% vs account median 62.9%, avg watch 6.7s"}, {"asof": "2026-10-31", "label": "Most sent", "text": "2026-10-27 \"It's still warm, Houston! We can't wait to...\" drew the most sends: 3.85% of reach vs account median 0.13%"}, {"asof": "2026-10-31", "label": "Short hooks (40 characters or fewer)", "text": "5.4x the median plays vs 0.9x without (2 vs 6 reels)"}], "worst_themes": []} -->

## Run 2026-11-01 (last 14 days: 9 reels, 8 with mature data)

Ranked by outlier multiple (plays / this account's median plays), then sends per reach. Skip 3s is the share of views that swiped away within the first 3 seconds (lower is better). Rows marked * are under 48h old: shown, but left out of the medians and the ranking.

| Date | Hook | Theme | Plays | Reach | Outlier x | Skip 3s | Avg watch s | Sends/reach | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-23](https://www.instagram.com/reel/De2cCLgpmfN/) | BYOB and come get LIT Houston!! #bacherloretteparty #part... | - | 2,174 | 1,943 | 9.7x | 38.5% | 9.5 | 2.37% | 0.72% |
| [2026-10-23](https://www.instagram.com/reel/De2XcHUDCSr/) | BYOB and come get LIT Houston, round 2 🍾👰‍♀️ Send this to... | - | 466 | 377 | 2.1x | 35.2% | 6.7 | 0.27% | 0.00% |
| [2026-10-24](https://www.instagram.com/reel/De5L8yJTyG7/) | Come see the dolphins with us! #thingstodohoustontx #htx... | - | 260 | 239 | 1.2x | 68.9% | 3.8 | 0.00% | 0.42% |
| [2026-10-27](https://www.instagram.com/reel/DfBTgU5N3Ue/) | It's still warm, Houston! We can't wait to see our in the... | - | 241 | 209 | 1.1x | 66.7% | 4.8 | 3.83% | 0.00% |
| [2026-10-22](https://www.instagram.com/reel/Dez73AyJ7Ou/) | It's still warm, Houston! We can't wait to see our in the... | - | 209 | 195 | 0.9x | 77.5% | 2.5 | 0.00% | 0.00% |
| [2026-10-27](https://www.instagram.com/reel/DfARe0SJLXR/) | The weather is perfect for a boat party! Call us and book... | - | 179 | 140 | 0.8x | 66.9% | 3.9 | 0.71% | 0.00% |
| [2026-10-19](https://www.instagram.com/reel/Derr--_TY5m/) | Book us for your birthday, bachelorette, or for some fun!... | - | 170 | 152 | 0.8x | 53.8% | 5.5 | 0.00% | 0.00% |
| [2026-10-28](https://www.instagram.com/reel/DfDPaBuC23b/) | "Get there early so you can be the DJ." Tatyana, Google r... | - | 27 | 22 | 0.1x | 66.7% | 3.3 | 0.00% | 0.00% |
| [2026-10-30*](https://www.instagram.com/reel/DfIY-sSvHNR/) | Halloween weekend on Clear Lake 🎃🚤 Costume optional. Cool... | - | 361 | 320 | - | 40.5% | 5.2 | 0.00% | 0.00% |

Account medians (8 mature reels): plays 225, reach 202, 3s skip 66.7%, avg watch 4.3s, sends/reach 0.13%, saves/reach 0.00%. Length band is unknown for every reel (duration is not in the Graph API), so outlier x compares against one account-wide median.

### Diagnosis

- Worst avg watch #1: 2026-10-22 "It's still warm, Houston! We can't wait to see...": 3s skip 77.5% vs account median 66.7%, avg watch 2.5s vs 4.3s; nothing lands, so change the angle entirely.
- Worst avg watch #2: 2026-10-28 "'Get there early so you can be the DJ.' Tatyana...": 3s skip 66.7% vs account median 66.7%, avg watch 3.3s vs 4.3s; hook works, middle sags, so cut the length and move the payoff earlier.
- Worst avg watch #3: 2026-10-24 "Come see the dolphins with us! #thingstodohoust...": 3s skip 68.9% vs account median 66.7%, avg watch 3.8s vs 4.3s; nothing lands, so change the angle entirely.
- Best by outlier: 2026-10-23 "BYOB and come get LIT Houston!! #bacherlorettep...": 9.7x the account median plays, 3s skip 38.5% vs account median 66.7%, avg watch 9.5s vs 4.3s, sends 2.37% of reach; hook and body both work, so repeat the structure with a new topic.

### What works here

- **Best reel** (as of 2026-11-01): 2026-10-23 "BYOB and come get LIT Houston!! #bacherlor..." ran 9.7x the median plays (3s skip 38.5%, avg watch 9.5s, sends 2.37% of reach)
- **Lowest 3s skip** (as of 2026-11-01): 2026-10-23 "BYOB and come get LIT Houston, round 2 🍾👰‍..." held best: skip 35.2% vs account median 66.7%, avg watch 6.7s
- **Most sent** (as of 2026-11-01): 2026-10-27 "It's still warm, Houston! We can't wait to..." drew the most sends: 3.83% of reach vs account median 0.13%
- **Short hooks (40 characters or fewer)** (as of 2026-11-01): 5.4x the median plays vs 0.9x without (2 vs 6 reels)

Directional only: 8 mature reels in the window. Patterns firm up around 20 reels.

### Next batch to test

1. **Subject** vs parent 2026-10-23 De2cCLgpmfN: keep the structure (hook is a 31-character statement, same pacing and caption shape; it held 3s skip 38.5%, avg watch 9.5s) and swap in a new subject: next in your queue: "Birthday math checks out 🎂 Send this to whoever...". Only the subject changes.
2. **Hook** vs parent 2026-10-22 Dez73AyJ7Ou: same footage, a new angle in the first frame and first line built on the best reel's hook shape (31-character statement); if this fails too, retire the angle. Only the hook changes.
3. **Length** vs parent 2026-10-28 DfDPaBuC23b: same hook and caption, recut shorter with the payoff inside the first 5 seconds. Only the length changes.
4. **Hook** vs parent 2026-10-24 De5L8yJTyG7: same footage, a new angle in the first frame and first line built on the best reel's hook shape (31-character statement); if this fails too, retire the angle. Only the hook changes.

<!-- reel-loop-state {"date": "2026-11-01", "found": 9, "ideas": [{"parent": "2026-10-23 De2cCLgpmfN", "variable": "subject"}, {"parent": "2026-10-22 Dez73AyJ7Ou", "variable": "hook"}, {"parent": "2026-10-28 DfDPaBuC23b", "variable": "length"}, {"parent": "2026-10-24 De5L8yJTyG7", "variable": "hook"}], "mature": 8, "median": {"avg_watch": 4.3425, "plays": 225.0, "skip": 66.7, "spr": 0.001326259946949602}, "works": [{"asof": "2026-11-01", "label": "Best reel", "text": "2026-10-23 \"BYOB and come get LIT Houston!! #bacherlor...\" ran 9.7x the median plays (3s skip 38.5%, avg watch 9.5s, sends 2.37% of reach)"}, {"asof": "2026-11-01", "label": "Lowest 3s skip", "text": "2026-10-23 \"BYOB and come get LIT Houston, round 2 \ud83c\udf7e\ud83d\udc70\u200d...\" held best: skip 35.2% vs account median 66.7%, avg watch 6.7s"}, {"asof": "2026-11-01", "label": "Most sent", "text": "2026-10-27 \"It's still warm, Houston! We can't wait to...\" drew the most sends: 3.83% of reach vs account median 0.13%"}, {"asof": "2026-11-01", "label": "Short hooks (40 characters or fewer)", "text": "5.4x the median plays vs 0.9x without (2 vs 6 reels)"}], "worst_themes": []} -->

## Run 2026-11-08 (last 14 days: 5 reels, 4 with mature data)

Ranked by outlier multiple (plays / this account's median plays), then sends per reach. Skip 3s is the share of views that swiped away within the first 3 seconds (lower is better). Rows marked * are under 48h old: shown, but left out of the medians and the ranking.

| Date | Hook | Theme | Plays | Reach | Outlier x | Skip 3s | Avg watch s | Sends/reach | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-30](https://www.instagram.com/reel/DfIY-sSvHNR/) | Halloween weekend on Clear Lake 🎃🚤 Costume optional. Cool... | - | 382 | 342 | 1.8x | 42.4% | 5.1 | 0.00% | 0.00% |
| [2026-10-27](https://www.instagram.com/reel/DfBTgU5N3Ue/) | It's still warm, Houston! We can't wait to see our in the... | - | 248 | 215 | 1.2x | 67.1% | 4.7 | 3.72% | 0.00% |
| [2026-10-27](https://www.instagram.com/reel/DfARe0SJLXR/) | The weather is perfect for a boat party! Call us and book... | - | 182 | 143 | 0.8x | 66.9% | 3.9 | 0.70% | 0.00% |
| [2026-10-28](https://www.instagram.com/reel/DfDPaBuC23b/) | "Get there early so you can be the DJ." Tatyana, Google r... | - | 34 | 31 | 0.2x | 63.3% | 3.5 | 0.00% | 3.23% |
| [2026-11-06*](https://www.instagram.com/reel/DfahaTzuqZO/) | Birthday math checks out 🎂 Send this to whoever's plannin... | - | 141 | 125 | - | 56.0% | 3.9 | 0.00% | 0.00% |

Account medians (4 mature reels): plays 215, reach 179, 3s skip 65.1%, avg watch 4.3s, sends/reach 0.35%, saves/reach 0.00%. Length band is unknown for every reel (duration is not in the Graph API), so outlier x compares against one account-wide median.

### Diagnosis

Too few reels to see a pattern (4 mature reels in the window, need 6).

### What works here

Too few reels to see a pattern.

Carried forward from earlier runs, not re-checked this run:
- **Best reel** (as of 2026-11-01): 2026-10-23 "BYOB and come get LIT Houston!! #bacherlor..." ran 9.7x the median plays (3s skip 38.5%, avg watch 9.5s, sends 2.37% of reach)
- **Lowest 3s skip** (as of 2026-11-01): 2026-10-23 "BYOB and come get LIT Houston, round 2 🍾👰‍..." held best: skip 35.2% vs account median 66.7%, avg watch 6.7s
- **Most sent** (as of 2026-11-01): 2026-10-27 "It's still warm, Houston! We can't wait to..." drew the most sends: 3.83% of reach vs account median 0.13%
- **Short hooks (40 characters or fewer)** (as of 2026-11-01): 5.4x the median plays vs 0.9x without (2 vs 6 reels)

### Next batch to test

Too few reels to see a pattern, so no test ideas this week. Post at least 6 reels in a window, then rerun.

<!-- reel-loop-state {"date": "2026-11-08", "found": 5, "ideas": [], "mature": 4, "median": {"avg_watch": 4.284, "plays": 215.0, "skip": 65.1, "spr": 0.0034965034965034965}, "works": [{"asof": "2026-11-01", "label": "Best reel", "text": "2026-10-23 \"BYOB and come get LIT Houston!! #bacherlor...\" ran 9.7x the median plays (3s skip 38.5%, avg watch 9.5s, sends 2.37% of reach)"}, {"asof": "2026-11-01", "label": "Lowest 3s skip", "text": "2026-10-23 \"BYOB and come get LIT Houston, round 2 \ud83c\udf7e\ud83d\udc70\u200d...\" held best: skip 35.2% vs account median 66.7%, avg watch 6.7s"}, {"asof": "2026-11-01", "label": "Most sent", "text": "2026-10-27 \"It's still warm, Houston! We can't wait to...\" drew the most sends: 3.83% of reach vs account median 0.13%"}, {"asof": "2026-11-01", "label": "Short hooks (40 characters or fewer)", "text": "5.4x the median plays vs 0.9x without (2 vs 6 reels)"}], "worst_themes": []} -->
