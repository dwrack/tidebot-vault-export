# Trial Reels Log, @kayaknola

Trial reels go to non-followers only. Each batch changes one thing so the result can be read. Compare trials only to other trials, and only to this account's own median.

Baseline (reel loop run 2026-11-01, 3 review-quote reels): 3-second skip 64 to 78 percent, average watch 2.9 to 4.9 s, sends per reach 0 to 0.6 percent.

## Batch 1 (built 2026-11-06, NOT posted, waiting on David)

Variable tested: the hook format. Everything else is held the same: 7 seconds, one shot, same text style, music bed, top-third text.

Files: `Marketing/Content Plan Nov 2026/_render/out_trials/` (rebuild with `python3 trials.py` in `_render`). Covers: `Marketing/Content Plan Nov 2026/05 Trial Batch 1 Covers (2026-11-06).jpg`.

| File | On-screen hook | v2 format | Footage |
|---|---|---|---|
| t1-this-close.mp4 | you live this close to this / and you've never been | 1 Nature is closer | Drone DJI_0139 |
| t2-scared-of-gators.mp4 | me, scared of gators, / booking a kayak tour anyway | 2 Fear flip | Gator on bank, Nov 2 (IMG_5903) |
| t3-rooftop-bars.mp4 | some want rooftop bars. / we want this. | 3 Some want X | Kayak POV, Aug 28 (IMG_4107) |
| t4-send-this.mp4 | send this to the friend who'd / scream at the first gator | 5 Send this to | Gator, Oct 16 (IMG_8825) |
| t5-circle-back.mp4 | nobody out here has asked me / to circle back | 11 Deadpan | Drone DJI_0136 |

Open items before posting:
- No CreatorOS key exists. Plan is to post through the Graph API directly (`trial_params` on the REELS container) with a small script next to `post_reel.py` on davids-mbp-2. Not built or tested yet.
- Trial eligibility for @kayaknola is unverified until the first post is attempted.
- t4 uses the same gator clip as the queued Dec 11 reel (h-dec11-cold-gator).

Metrics get added here 72 hours after posting: skip rate, average watch, sends per reach, follows per reach.

## Text fix, 2026-11-06

The two-line captions were drawn as one white box per line, stacked edge to edge, which left notched, overlapping corners. `hooks.draw()` now draws one merged shape. All 29 queued text reels (w1-sat, w2 x4, h- x24) and the two text carousels (h-dec05, h-jan02) were re-rendered and replaced in `s3://nkst-reels-private`. Old versions are under `_bak-20261106-boxes/` in the same bucket; old code is `hooks.py.bak-20261106-boxes`.
