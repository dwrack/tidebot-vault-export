---
name: virality-predictor
description: Predict how a short-form video (IG Reel, TikTok, YouTube Short) will perform BEFORE it is posted. Scores the hook, retention, loop, send/save triggers, sound-off readability, caption SEO and account-safety against the brand's own Viral Playbook and analytics baseline, then predicts a view range vs the account median, lists the fixes that move the score most, and rewrites the hook and caption. Also logs every prediction and calibrates against real results later. Use when the user asks "will this go viral", "score this reel/script/caption", "predict views", "rate this TikTok", "is this ready to post", or logs actual results for a past prediction.
---

# Virality Predictor

Predict a short-form clip's performance before it ships, explain why, and fix it.
This is a heuristic model built on the platform signals in the brand's playbook plus the
account's real view history. It is not magic: be honest about confidence, and get better
over time by logging predictions and comparing them to actuals.

## Inputs (any one is enough, more is better)

- A video file (`.mp4`, `.mov`) - best. Run the frame extractor below.
- A script / shot list / storyboard.
- A caption draft, hook line, or idea description.
- Optional: brand (folder code like `dckt`, `akt`, `nbb`, `hpb`, `bbk`, `lskt`, `nkst`, `npb`, `ee`, `et`), platform (Reels / TikTok / Shorts), audio plan, posting time.

If the brand is not given and cannot be inferred from the file path or content, ask once. If the platform is not given, assume Instagram Reels.

## Step 1: Load the brand context

Search the brand folder before scoring, the brand's own data beats the generic rubric:

- `<brand>/Marketing/**/*Viral Playbook*` - the rules and house style (hook timing, length bands, caption formula, banned claims).
- `<brand>/Marketing/*Analytics Readout*` - account baseline: median and average views, best posts, what hooks won, traffic source (For You vs Search).
- `<brand>/Marketing/*Customer Avatar*` - who has to care.
- `<brand>/Marketing/*Catalog*`, `*Content Grid*` - past posts to compare against.
- `<brand>/Marketing/Virality Predictions.md` - prior predictions and actuals (calibration).

Use Glob/Grep, not guesses. If a brand has no playbook, borrow `dckt/Marketing/Content Universe/04 Viral Playbook.md` for platform mechanics only (not its brand-specific claims), and say so. If there is no analytics baseline, predict relative tiers only, not view numbers.

## Step 2: Break down the clip

For a video file run:

```bash
bash .claude/skills/virality-predictor/scripts/extract_frames.sh "<video>" "<scratch dir>"
```

It prints duration, resolution/aspect, fps, whether there is audio and its loudness, and writes:
`hook_0.0s.jpg ... hook_3.0s.jpg` (the first 3 seconds, densely), `t_XXs.jpg` (one frame
every ~2s), `last.jpg`, and `sheet.jpg` (contact sheet). Read the hook frames and the
contact sheet with the Read tool. Look hard at frame 1: what does someone see before they
decide to swipe? Read any burned-in text verbatim. Compare `last.jpg` to `hook_0.0s.jpg`
to judge the loop.

If the user has no file, build the same breakdown from the script: second-by-second beats,
the on-screen text, the spoken words, audio, and the ending.

Write down (internally) the timeline: 0-1s, 1-3s, 3s-mid, close, last frame.

## Step 3: Score it

Score each factor with the rubric in `references/rubric.md` (100 points total, 9 factors,
plus hard gates and penalties). Always justify each score in one line that points at a
specific moment ("0.0s: slow drone push-in, no text" not "hook is weak").

Then apply the brand's own evidence: if the analytics readout says claim/question hooks
on a signature location are the account's only winners, a clip that does that earns its
hook points, and a pretty captionless montage gets the bottom-of-catalog treatment it
already got in real data.

## Step 4: Predict the outcome

Map the final score to a tier and a view multiplier of the account's **median** views
(from the analytics readout, the catalog, or the prediction log), using the table in the
rubric. Then adjust for account state:

- Dormant or 0% For You account: cap the upside at the Solid tier until the log shows real FYP reach. Say why.
- Search-driven account: a strong search term in on-screen text + caption line 1 raises the floor (long-tail views), not the ceiling.
- Trending audio caught early (<48h, low use count) widens the upside, late trending audio does not.
- Posting burst (2+ posts the same day) or repost: cut the prediction, and flag it.

Give a range, not a point ("400-900 views in 7 days, about 1.2-2.7x the 336 median"),
plus a confidence (Low / Medium / High) based on how much real baseline data you had and
how complete the input was (script only = at most Medium).

## Step 5: Report

Use this format, keep it tight:

```
## Virality Prediction: <clip name>  (<brand>, <platform>)

**Score: 72/100 - Solid**   Predicted: 500-1,000 views / 7 days (1.5-3x median 336)   Confidence: Medium
One-line verdict: <why it will or won't travel>

| Factor | Score | Why (timestamped) |
|---|---|---|
| Hook (0-1s) | 18/25 | ... |
| ... | | |
| Gates / penalties | -5 | ... |

**Strongest signal it will farm:** sends | saves | completion | replay
**Biggest risk:** ...

### Fixes, ranked by points gained
1. (+8) ... exact change, with timestamp
2. (+5) ...
3. (+3) ...
Score if all fixes land: 88/100 - Breakout candidate

### Rewrites
Hook options (on-screen text, first 3 words a claim or a question):
- ...
- ...
- ...
Caption (brand caption formula, house style):
<caption>
```

Follow the brand's house style in every rewrite (for DCKT: plain ASCII, no em dashes, no
double dashes, 3-5 hashtags on their own line, no founding year / review count / ACA
claim). Never invent facts for proof lines: only use facts the vault marks as cleared.

## Step 6: Log it

Append a row to `<brand>/Marketing/Virality Predictions.md` (create it with this header if missing):

```
# Virality Predictions

Predictions made before posting, and what actually happened. Used to calibrate the virality-predictor skill.

| Date | Clip | Platform | Score | Tier | Predicted 7d views | Actual 7d views | Sends | Saves | Hit? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
```

Leave the actual columns blank. Tell the user to come back with the 7-day numbers.

## Calibrate mode

When the user gives actual results ("that reel got 2.1k views, 40 sends"):

1. Find the row in the log, fill in actuals, mark Hit? as `hit` (inside range), `over` (beat the top), or `under`.
2. If the log has 5+ completed rows, report the hit rate and the bias (do we over- or under-predict?), and which factor best separated winners from losers.
3. Recommend a concrete adjustment (e.g. "shift the multiplier table down one band for this account" or "hook score is predicting well, save-value is not") and record it under a `## Calibration notes` section at the bottom of the log. Read those notes in Step 1 next time and apply them.

## Batch mode

Given several clips or ideas ("which of these 5 should I post first?"), score each, then
return a ranked table (rank, clip, score, tier, predicted range, the one fix that matters
most) and a posting order that respects the brand's cadence rules (for DCKT: max one per
day, no bursts). Log each one.
