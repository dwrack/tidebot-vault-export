---
name: virality-predictor
description: Predict how a short-form video (IG Reel, TikTok, YouTube Short) will perform BEFORE it is posted. Scores the hook, retention, loop, send/save triggers, sound-off readability, caption SEO and account-safety against the brand's own Viral Playbook and analytics baseline, then predicts a view range vs the account median, lists the fixes that move the score most, and rewrites the hook and caption. Optionally adds Higgsfield's brain-activity Virality Predictor (hook strength, hold rate, attention curve) when its CLI is installed. Also logs every prediction and calibrates against real results later. Use when the user asks "will this go viral", "score this reel/script/caption", "predict views", "rate this TikTok", "is this ready to post", or logs actual results for a past prediction.
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

This skill lives in `thebrain/`. Brand folders are its siblings at the vault root (`../<brand>/` from `thebrain/`), so every `<brand>/...` path below is relative to the vault root, not to `thebrain/`. Also check `thebrain/03 Projects/Active/Content Engine/` for cross-brand content notes.

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
bash "<vault root>/thebrain/.claude/skills/virality-predictor/scripts/extract_frames.sh" "<video>" "<scratch dir>"
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

### Step 2b (optional): Higgsfield brain scan

Higgsfield's Virality Predictor (the "brain psychology" one, technical name
`brain_activity`) runs the video through a model of predicted viewer brain response and
returns a Virality Index, Hook Strength, Hold Rate, an attention curve, and a heatmap of
predicted visual-cortex and amygdala activation. It only sees the video: it knows nothing
about the caption, search terms, send/save triggers, the brand's rules, or the account's
baseline. That is what the rest of this skill adds.

Run it when a video file is available AND the Higgsfield CLI is installed and signed in:

```bash
command -v higgsfield && higgsfield --help   # find the brain_activity / virality command and its flags
```

- Cloud sessions: the API token is read from the `HIGGSFIELD_API_KEY` environment variable (set in the environment's settings, never pasted in chat). Install the CLI with `curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh`, then check `higgsfield --help` / `higgsfield auth --help` for how it takes a token (env var or a login flag) and use that. Never print the token.
- Not installed: skip this step and say so in one line. Setup (on the user's machine): `npx skills add higgsfield-ai/skills`, then `higgsfield auth login`. Do not run the login for the user.
- It takes clips up to 15 seconds. For a longer clip, score the opening, which is where the swipe decision happens: `ffmpeg -y -i in.mp4 -t 15 -c copy first15.mp4`. Note in the report that only the first 15s were scanned.
- Pass the video with `--video`, no prompt needed. Use the exact command and flags `--help` shows, do not guess them.

Use the results like this:
- Put Higgsfield's numbers in their own row block in the report, labeled as Higgsfield's model output, never mixed into the 100-point score as if they were ours.
- Cross-check: where Hook Strength or the attention curve disagrees with your Hook / Retention scores by a lot, look at the frames at that timestamp again and say which you believe and why. An attention dip at a timestamp is a specific fix to list.
- Treat the brain heatmap as a model prediction, not a measured brain. Do not tell the user a clip "lights up the amygdala" as fact.
- Log the Higgsfield Virality Index in the prediction log Higgsfield VI column, so calibration can tell over time whether it, our score, or both predict real views for this account.

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

Higgsfield brain scan (model prediction, first 15s): Virality Index .. | Hook Strength .. | Hold Rate ..
Attention dips: 4.5s, 9s -> <what is on screen there>   Agrees with our score? <yes / no, and why>
(omit this block if Higgsfield was not run)

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

| Date | Clip | Platform | Score | Tier | Higgsfield VI | Predicted 7d views | Actual 7d views | Sends | Saves | Hit? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
```

Leave the actual columns blank. Tell the user to come back with the 7-day numbers.

## Calibrate mode

When the user gives actual results ("that reel got 2.1k views, 40 sends"):

1. Find the row in the log, fill in actuals, mark Hit? as `hit` (inside range), `over` (beat the top), or `under`.
2. If the log has 5+ completed rows, report the hit rate and the bias (do we over- or under-predict?), and which factor best separated winners from losers. If Higgsfield VI was logged, compare how well it and our score each ranked the actual results.
3. Recommend a concrete adjustment (e.g. "shift the multiplier table down one band for this account" or "hook score is predicting well, save-value is not") and record it under a `## Calibration notes` section at the bottom of the log. Read those notes in Step 1 next time and apply them.

## Batch mode

Given several clips or ideas ("which of these 5 should I post first?"), score each, then
return a ranked table (rank, clip, score, tier, predicted range, the one fix that matters
most) and a posting order that respects the brand's cadence rules (for DCKT: max one per
day, no bursts). Log each one.
