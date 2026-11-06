# Reel Trials: test, measure, learn

Set up 2026-10-30 from David's "can you do the trial reels to see what works and learn from it." This is loop 2 of the [[Self-Improvement System — Skills, Social, Comms, SOPs (Oct 30 2026)]] made concrete: every trial is a real experiment with one variable, a baseline, and a decision rule, and the results change the posting rules instead of sitting in a report.

Baselines come from [[Social Analytics + Market Study (Oct 2026)]] (pulled 10-14). Trend inputs from [[Trend Pulse What Works]].

## How a trial works

- **One variable per trial.** Same clip, same end card, same post time of day. Only the thing under test changes (hook text, person in first 2 seconds, caption length, framing, post time).
- **2 to 4 cuts**, staggered one every 2 to 3 days on the brand's IG Reels (TikTok mirror when the account exists). Never two cuts on the same day.
- **Read at day 7.** Earlier reads lie; a reel that gets picked up on day 4 flips the result.
- **Metrics, in order:** shares per reach (the signal that predicted every hit in the Oct 14 study), saves, 3-second hold and average watch time, then profile visits and link clicks. Raw views last.
- **Baseline:** the brand's median reel reach (E&E 2,667, NPB 1,584, DCKT 993, HPB 346, BBK 240).
- **Winner rule:** a cut wins when it beats its siblings by 30% or more on shares per reach AND clears the brand median on reach. Anything less is "no signal": keep the current rule, do not change anything, log it anyway.
- **Rule change:** the same variable has to win in the same direction in 3 trials (any brand, 2 if the same brand) before it edits the CURRENT RULES block in the study and the per-brand 532 grid. Rules carry "verified <date>."
- **Losers teach too.** A format that loses twice goes on the brand's do-not-post list.

## Ledger

`Reel Trials Ledger.csv` next to this file. One row per cut: brand, trial, variable, cut, hook, posted, reach, shares, saves, hold3s, avg_watch, clicks, baseline, result. The day-7 pull appends the numbers; the Sunday review writes the result column.

## Trial queue

| # | Brand | Variable | Cuts | Status |
|---|---|---|---|---|
| T1 | E&E | Hook wording on the Portland Downpour clip | F made-it-rain / G book-on-purpose / H one-sunny-day / B six-minutes | Cut and captioned since summer, staged for Kimberlynn, never posted as far as the vault shows. Ready to go. See [[Portland Downpour - Reel AB Test (for Kimberlynn)]]. |
| T2 | E&E | Social framing vs wellness framing, same clip | "plans with friends" caption vs "reset" caption | Needs a clip. The two 131k and 51k reels say social wins; this confirms it on purpose. |
| T3 | NPB | Person in the first 2 seconds | Captain on camera vs boat-first open | Needs two cuts of one dock clip. NPB queue ran dry in September, so this also refills it. |
| T4 | HPB | Caption length | 3 to 15 words vs 100+ words, same LIT-style reel | HPB's one hit was LIT; cheapest brand to test on because the baseline is 346. |
| T5 | DCKT | Hook type (off-season lab) | Guide deadpan vs scenic | Low stakes in November, 60 raw clips in Raw Footage. |
| T6 | All | Post time | 7am vs 7pm, same cut | Runs after T1-T5 so time is not confounded with hook. |

## Rails: what runs where (verified 2026-10-30)

| Step | Where | State |
|---|---|---|
| Cutting | wavey (footage is iCloud-evicted on dckt-guide-mac, 0 bytes local) or Higgsfield for AI b-roll | E&E Downpour cuts already exist in `Ebb and Ember/Assets/Video/Recuts/` |
| Posting | Kimberlynn (E&E), David's phone tap, or the mbp-2 Meta Graph API for IG business accounts (needs a public video URL) | No IG/Meta MCP on dckt-guide-mac. Posting phones have no brand accounts yet. |
| Measuring | mbp-2, same Instagram Graph API pull the Oct 14 study used, run day 7 per cut, append to the ledger | To build: `reel-trials-pull.py` on mbp-2, weekly Sunday 6pm |
| Learning | Sunday: ledger -> result column -> rule proposal in [[Corrections - Proposed Rules]] style, tick-to-approve | Folds into the Sunday corrections run |

## Open on David
1. Which brand goes first (E&E is ready today).
2. Who posts: Kimberlynn, David's tap, or standing authorization for approved test reels via the API.
3. OK to send the 4 Downpour cuts to Kimberlynn as T1 with the stagger schedule.
