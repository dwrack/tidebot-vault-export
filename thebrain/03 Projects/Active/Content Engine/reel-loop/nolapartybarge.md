# @nolapartybarge reel loop (New Orleans Party Barge)

Weekly Instagram reel learning loop, built from the trial-reel-loop skill. Written by `~/.claude/scripts/reel-loop/reel_loop.py` on davids-mbp-2 (Sundays 06:10 PT), read-only Graph API. One dated section per run, newest at the bottom. Each reel is compared only to this account's own median in the same window.

## Run 2026-10-31 (last 14 days: 10 reels, 6 with mature data)

Ranked by outlier multiple (plays / this account's median plays), then sends per reach. Skip 3s is the share of views that swiped away within the first 3 seconds (lower is better). Rows marked * are under 48h old: shown, but left out of the medians and the ranking.

| Date | Hook | Theme | Plays | Reach | Outlier x | Skip 3s | Avg watch s | Sends/reach | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-28](https://www.instagram.com/reel/DfDBqiAE0xU/) | Rules are rules. Tag the friend who's always late. | - | 5,175 | 3,776 | 2.7x | 31.6% | 8.0 | 0.05% | 0.16% |
| [2026-10-26](https://www.instagram.com/reel/De-DATdi-xm/) | BBL? yep.. Bayou Boat Life. 🍑🌴🍹 | - | 3,034 | 1,917 | 1.6x | 48.1% | 5.8 | 0.83% | 0.05% |
| [2026-10-29](https://www.instagram.com/reel/DfFmcxgjAq6/) | The Great Wall of Louisiana. Almost two miles of concrete... | - | 2,980 | 1,964 | 1.6x | 48.1% | 7.2 | 0.25% | 0.20% |
| [2026-10-24](https://www.instagram.com/reel/De5DbfjigGs/) | New Orleans official Halloween pre-game party is at Nola... | - | 820 | 681 | 0.4x | 58.2% | 5.8 | 0.29% | 0.29% |
| [2026-10-27](https://www.instagram.com/reel/DfAc3D8jYcQ/) | Halloween's on a Saturday this year. The bayou goes pirat... | - | 609 | 476 | 0.3x | 61.8% | 4.8 | 0.21% | 0.00% |
| [2026-10-21](https://www.instagram.com/reel/Dexnr28xoqP/) | Nola Party Barge is a must this spooky season. 🎃 | - | 602 | 497 | 0.3x | 71.0% | 4.1 | 0.20% | 0.20% |
| [2026-10-31*](https://www.instagram.com/reel/DfK5EqECAi3/) | Every day can be Halloween at Nola Party Barge. | - | 435 | 280 | - | 62.6% | 3.6 | 0.00% | 0.00% |
| [2026-10-31*](https://www.instagram.com/reel/DfKwDJEoAPH/) | Uncut footage of a shark in Bayou Bienvenue. Send this to... | - | 510 | 385 | - | 64.1% | 3.5 | 0.00% | 0.00% |
| [2026-10-30*](https://www.instagram.com/reel/DfILq3qRjBo/) | We've gone yo ho and a bottle of rum for the weekend! Com... | - | 378 | 281 | - | 71.4% | 5.7 | 0.00% | 0.71% |
| [2026-10-30*](https://www.instagram.com/reel/DfILWYcE0E2/) | He's seen things. Tag the designated adult in your group. | - | 669 | 396 | - | 47.2% | 10.0 | 0.00% | 0.00% |

Account medians (6 mature reels): plays 1,900, reach 1,299, 3s skip 53.2%, avg watch 5.8s, sends/reach 0.23%, saves/reach 0.18%. Length band is unknown for every reel (duration is not in the Graph API), so outlier x compares against one account-wide median.

### Diagnosis

- Worst avg watch #1: 2026-10-21 "Nola Party Barge is a must this spooky season. 🎃": 3s skip 71.0% vs account median 53.2%, avg watch 4.1s vs 5.8s; nothing lands, so change the angle entirely.
- Worst avg watch #2: 2026-10-27 "Halloween's on a Saturday this year. The bayou...": 3s skip 61.8% vs account median 53.2%, avg watch 4.8s vs 5.8s; nothing lands, so change the angle entirely.
- Worst avg watch #3: 2026-10-26 "BBL? yep.. Bayou Boat Life. 🍑🌴🍹": 3s skip 48.1% vs account median 53.2%, avg watch 5.8s vs 5.8s; hook and body both work, so repeat the structure with a new topic.
- Best by outlier: 2026-10-28 "Rules are rules. Tag the friend who's always late.": 2.7x the account median plays, 3s skip 31.6% vs account median 53.2%, avg watch 8.0s vs 5.8s, sends 0.05% of reach; hook and body both work, so repeat the structure with a new topic.

### What works here

- **Best reel** (as of 2026-10-31): 2026-10-28 "Rules are rules. Tag the friend who's alwa..." ran 2.7x the median plays (3s skip 31.6%, avg watch 8.0s, sends 0.05% of reach)
- **Lowest 3s skip** (as of 2026-10-31): 2026-10-28 "Rules are rules. Tag the friend who's alwa..." held best: skip 31.6% vs account median 53.2%, avg watch 8.0s
- **Most sent** (as of 2026-10-31): 2026-10-26 "BBL? yep.. Bayou Boat Life. 🍑🌴🍹" drew the most sends: 0.83% of reach vs account median 0.23%
- **Hooks that carry a tag/send ask** (as of 2026-10-31): 2.1x the median plays vs 0.4x without (2 vs 4 reels)

Directional only: 6 mature reels in the window. Patterns firm up around 20 reels.

### Next batch to test

1. **Subject** vs parent 2026-10-28 DfDBqiAE0xU: keep the structure (hook is a 50-character statement with a tag/send ask, same pacing and caption shape; it held 3s skip 31.6%, avg watch 8.0s) and swap in a new subject: next in your queue: "25 years married and she still fires first. Tag...". Only the subject changes.
2. **Hook** vs parent 2026-10-21 Dexnr28xoqP: same footage, a new angle in the first frame and first line built on the best reel's hook shape (50-character statement with a tag/send ask); if this fails too, retire the angle. Only the hook changes.
3. **Hook** vs parent 2026-10-27 DfAc3D8jYcQ: same footage, a new angle in the first frame and first line built on the best reel's hook shape (50-character statement with a tag/send ask); if this fails too, retire the angle. Only the hook changes.
4. **Caption** vs parent 2026-10-26 De-DATdi-xm: same video, caption line one carries a single plain ask (book, DM, or one comment keyword). Only the caption changes.

<!-- reel-loop-state {"date": "2026-10-31", "found": 10, "ideas": [{"parent": "2026-10-28 DfDBqiAE0xU", "variable": "subject"}, {"parent": "2026-10-21 Dexnr28xoqP", "variable": "hook"}, {"parent": "2026-10-27 DfAc3D8jYcQ", "variable": "hook"}, {"parent": "2026-10-26 De-DATdi-xm", "variable": "caption"}], "mature": 6, "median": {"avg_watch": 5.787, "plays": 1900.0, "skip": 53.150000000000006, "spr": 0.0023233325916924815}, "works": [{"asof": "2026-10-31", "label": "Best reel", "text": "2026-10-28 \"Rules are rules. Tag the friend who's alwa...\" ran 2.7x the median plays (3s skip 31.6%, avg watch 8.0s, sends 0.05% of reach)"}, {"asof": "2026-10-31", "label": "Lowest 3s skip", "text": "2026-10-28 \"Rules are rules. Tag the friend who's alwa...\" held best: skip 31.6% vs account median 53.2%, avg watch 8.0s"}, {"asof": "2026-10-31", "label": "Most sent", "text": "2026-10-26 \"BBL? yep.. Bayou Boat Life. \ud83c\udf51\ud83c\udf34\ud83c\udf79\" drew the most sends: 0.83% of reach vs account median 0.23%"}, {"asof": "2026-10-31", "label": "Hooks that carry a tag/send ask", "text": "2.1x the median plays vs 0.4x without (2 vs 4 reels)"}], "worst_themes": []} -->

## Run 2026-11-01 (last 14 days: 10 reels, 6 with mature data)

Ranked by outlier multiple (plays / this account's median plays), then sends per reach. Skip 3s is the share of views that swiped away within the first 3 seconds (lower is better). Rows marked * are under 48h old: shown, but left out of the medians and the ranking.

| Date | Hook | Theme | Plays | Reach | Outlier x | Skip 3s | Avg watch s | Sends/reach | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-28](https://www.instagram.com/reel/DfDBqiAE0xU/) | Rules are rules. Tag the friend who's always late. | - | 5,226 | 3,802 | 2.7x | 31.7% | 8.0 | 0.05% | 0.16% |
| [2026-10-26](https://www.instagram.com/reel/De-DATdi-xm/) | BBL? yep.. Bayou Boat Life. 🍑🌴🍹 | - | 3,100 | 1,951 | 1.6x | 48.2% | 5.8 | 0.82% | 0.05% |
| [2026-10-29](https://www.instagram.com/reel/DfFmcxgjAq6/) | The Great Wall of Louisiana. Almost two miles of concrete... | - | 3,058 | 2,038 | 1.6x | 48.5% | 7.1 | 0.25% | 0.20% |
| [2026-10-24](https://www.instagram.com/reel/De5DbfjigGs/) | New Orleans official Halloween pre-game party is at Nola... | - | 825 | 686 | 0.4x | 58.1% | 5.8 | 0.29% | 0.29% |
| [2026-10-27](https://www.instagram.com/reel/DfAc3D8jYcQ/) | Halloween's on a Saturday this year. The bayou goes pirat... | - | 637 | 495 | 0.3x | 61.9% | 4.8 | 0.20% | 0.00% |
| [2026-10-21](https://www.instagram.com/reel/Dexnr28xoqP/) | Nola Party Barge is a must this spooky season. 🎃 | - | 603 | 497 | 0.3x | 71.0% | 4.1 | 0.20% | 0.20% |
| [2026-10-31*](https://www.instagram.com/reel/DfK5EqECAi3/) | Every day can be Halloween at Nola Party Barge. | - | 859 | 581 | - | 66.1% | 3.9 | 0.00% | 0.00% |
| [2026-10-31*](https://www.instagram.com/reel/DfKwDJEoAPH/) | Uncut footage of a shark in Bayou Bienvenue. Send this to... | - | 627 | 509 | - | 70.0% | 3.5 | 2.75% | 0.00% |
| [2026-10-30*](https://www.instagram.com/reel/DfILq3qRjBo/) | We've gone yo ho and a bottle of rum for the weekend! Com... | - | 386 | 287 | - | 72.2% | 5.6 | 0.00% | 0.70% |
| [2026-10-30*](https://www.instagram.com/reel/DfILWYcE0E2/) | He's seen things. Tag the designated adult in your group. | - | 717 | 425 | - | 48.8% | 9.5 | 0.00% | 0.00% |

Account medians (6 mature reels): plays 1,942, reach 1,318, 3s skip 53.3%, avg watch 5.8s, sends/reach 0.22%, saves/reach 0.18%. Length band is unknown for every reel (duration is not in the Graph API), so outlier x compares against one account-wide median.

### Diagnosis

- Worst avg watch #1: 2026-10-21 "Nola Party Barge is a must this spooky season. 🎃": 3s skip 71.0% vs account median 53.3%, avg watch 4.1s vs 5.8s; nothing lands, so change the angle entirely.
- Worst avg watch #2: 2026-10-27 "Halloween's on a Saturday this year. The bayou...": 3s skip 61.9% vs account median 53.3%, avg watch 4.8s vs 5.8s; nothing lands, so change the angle entirely.
- Worst avg watch #3: 2026-10-26 "BBL? yep.. Bayou Boat Life. 🍑🌴🍹": 3s skip 48.2% vs account median 53.3%, avg watch 5.8s vs 5.8s; hook and body both work, so repeat the structure with a new topic.
- Best by outlier: 2026-10-28 "Rules are rules. Tag the friend who's always late.": 2.7x the account median plays, 3s skip 31.7% vs account median 53.3%, avg watch 8.0s vs 5.8s, sends 0.05% of reach; hook and body both work, so repeat the structure with a new topic.

### What works here

- **Best reel** (as of 2026-11-01): 2026-10-28 "Rules are rules. Tag the friend who's alwa..." ran 2.7x the median plays (3s skip 31.7%, avg watch 8.0s, sends 0.05% of reach)
- **Lowest 3s skip** (as of 2026-11-01): 2026-10-28 "Rules are rules. Tag the friend who's alwa..." held best: skip 31.7% vs account median 53.3%, avg watch 8.0s
- **Most sent** (as of 2026-11-01): 2026-10-26 "BBL? yep.. Bayou Boat Life. 🍑🌴🍹" drew the most sends: 0.82% of reach vs account median 0.22%
- **Hooks that carry a tag/send ask** (as of 2026-11-01): 2.1x the median plays vs 0.4x without (2 vs 4 reels)

Directional only: 6 mature reels in the window. Patterns firm up around 20 reels.

### Next batch to test

1. **Subject** vs parent 2026-10-28 DfDBqiAE0xU: keep the structure (hook is a 50-character statement with a tag/send ask, same pacing and caption shape; it held 3s skip 31.7%, avg watch 8.0s) and swap in a new subject: next in your queue: "25 years married and she still fires first. Tag...". Only the subject changes.
2. **Hook** vs parent 2026-10-21 Dexnr28xoqP: same footage, a new angle in the first frame and first line built on the best reel's hook shape (50-character statement with a tag/send ask); if this fails too, retire the angle. Only the hook changes.
3. **Hook** vs parent 2026-10-27 DfAc3D8jYcQ: same footage, a new angle in the first frame and first line built on the best reel's hook shape (50-character statement with a tag/send ask); if this fails too, retire the angle. Only the hook changes.
4. **Caption** vs parent 2026-10-26 De-DATdi-xm: same video, caption line one carries a single plain ask (book, DM, or one comment keyword). Only the caption changes.

<!-- reel-loop-state {"date": "2026-11-01", "found": 10, "ideas": [{"parent": "2026-10-28 DfDBqiAE0xU", "variable": "subject"}, {"parent": "2026-10-21 Dexnr28xoqP", "variable": "hook"}, {"parent": "2026-10-27 DfAc3D8jYcQ", "variable": "hook"}, {"parent": "2026-10-26 De-DATdi-xm", "variable": "caption"}], "mature": 6, "median": {"avg_watch": 5.788, "plays": 1941.5, "skip": 53.3, "spr": 0.0022367938462148473}, "works": [{"asof": "2026-11-01", "label": "Best reel", "text": "2026-10-28 \"Rules are rules. Tag the friend who's alwa...\" ran 2.7x the median plays (3s skip 31.7%, avg watch 8.0s, sends 0.05% of reach)"}, {"asof": "2026-11-01", "label": "Lowest 3s skip", "text": "2026-10-28 \"Rules are rules. Tag the friend who's alwa...\" held best: skip 31.7% vs account median 53.3%, avg watch 8.0s"}, {"asof": "2026-11-01", "label": "Most sent", "text": "2026-10-26 \"BBL? yep.. Bayou Boat Life. \ud83c\udf51\ud83c\udf34\ud83c\udf79\" drew the most sends: 0.82% of reach vs account median 0.22%"}, {"asof": "2026-11-01", "label": "Hooks that carry a tag/send ask", "text": "2.1x the median plays vs 0.4x without (2 vs 4 reels)"}], "worst_themes": []} -->
