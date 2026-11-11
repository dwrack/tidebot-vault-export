---
date: 2026-11-10
engine: claude
model: sonnet
days: 7
sources:
  mbp-2: 1236 sessions, ok
  laptop: 171 sessions, ok
  bigly: 37 sessions, ok
---
Engine: claude sonnet | Sources: mbp-2 1236 (loops 1100 excluded), laptop 171 (loops 21 excluded), bigly 37 (loops 14 excluded) | Drafts only, nothing applied.

## Top 5 this week
1. Long sessions run past 200k tokens before anyone starts fresh. 12+ sessions ended with "I can /compact or write a brief" at 200-566k tokens. Fix: automation (auto-brief at ~150k).
2. Outbound email openers and ask timing keep needing correction. 2 corrections in 2 days (11/09). Fix: rule exists but still broken, plus a small memory.
3. Mentioning a person David asked not to name, and re-asking things already decided. 2 hits (11/06, 11/09). Fix: memory.
4. GBP refill loop errors on 25 of 27 runs, and Slack-question and morning-brief/chief-of-staff loops also error. Fix: automation (run /failure-modes).
5. Recurring one-off pastes of "automate this" ops chores (WMA quarterly report, sales and use tax, rent chasing). 3 in 6 days. Fix: skill.

## Repeat mistakes and corrections

**Opener and timing in outbound drafts (rule exists but still broken)**
- 11/09 E&E: "opening line reads horrible... makes you look weak." The CLAUDE.md rule already exists, and the draft still needed the correction.
- 11/09 E&E: "stop asking for quotes later in the week." Drafts kept setting a "by Friday" deadline.
- Frequency: 2 in one day, same contractor-quote email.
- Fix: before showing any draft, run a self-check against the opener ban list and ask for "earliest convenience" on quotes. See the CLAUDE.md line below.

**Naming a person David wants kept out of it**
- 11/06 E&E: "stop mentioning marios name... trying to compartamentalize things."
- Related: 11/06 "no pressure gauge needed," "we arn't doing a permit." Claude re-added items David had already ruled out.
- Frequency: 2 sessions.
- Fix: memory entry below.

**Sessions run far past a sane length**
- 11/09 E&E gas line session at 566k tokens. 11/05 and 11/06 sessions at 207k to 256k tokens. Several asked "/compact or fresh brief" only at the end.
- Frequency: 10+ sessions.
- Fix: automation. A /token-diet check or a hook that writes the 10-line brief at ~150k and tells David once.

**Dashboard scope creep and duplicate surfaces**
- 11/05: "should all just be inside of each dashboard." 11/06: "I thought we were going to make one here that had everything."
- Frequency: 2 sessions.
- Fix: memory. One Command Center, no parallel artifacts or tabs without a yes. The "ask before changing format" memory exists but this was not applied to dashboards.

**Silent failures David finds himself**
- 11/05 E&E: "you keep an eye on my gmail... right?" The watcher was dead and the failure alert DM was off.
- 11/10 HPB: "still getting these dumb sms emails... figure it out." The daily send job pointed at a missing folder.
- Frequency: 2 times.
- Fix: run /failure-modes on each loop, and keep alerts on by default.

## Skills that should exist

**ops-compliance-filing**
- Triggers: "usage report," "sales and use tax," "quarterly filing due," "automate this filing."
- What it does: for a recurring government or vendor filing, finds the last filing, computes what is owed from bookings data, drafts the form for David's tap, and files a dashboard item with the due date. It also saves the recipe so the next quarter is one run.
- Evidence: 11/06 NKST: "lets automate this process as much as possible. i can write the check." 11/05 NKST: "automate it as 0$."
- No existing skill covers it. /cpa is advice only.

**tenant-rent-chase**
- Skip. Single case (11/06 Cave Point, rent late, "automate venmo? or automate a ach pull?"). Not yet 2 hits.

## Chores worth automating

**Session handoff briefs**
- Est. 1 to 2 hrs/week of re-explaining and re-reading.
- Where: laptop hook (sessions run there), not mbp-2.
- Approach: a hook at ~150k tokens that writes a 10-line brief to the vault and prompts David once.

**Loop failure triage**
- Est. 1 hr/week.
- Where: mbp-2.
- Evidence: GBP refill 25 errors of 27 runs, Slack Q&A 15 of 10 runs, morning-brief 13 of 7, chief-of-staff 9 of 7, bigly Phase 1 28 of 4. Wait: some may be expected tool errors, so verify live before reporting as broken.
- Approach: a daily check that DMs David only when a loop's error rate stays above 50% for 3 runs.

**Recurring quarterly filings (WMA report, sales tax)**
- Est. 1 hr/quarter each, about 0.2 hrs/week.
- Where: mbp-2, a launchd reminder that drafts the filing and puts it on the dashboard.

## Proposals (DRAFT, not applied)

### CLAUDE.md lines
1. `Before showing any outbound draft, re-read the opener against the Writing Style ban list (flattery, "thanks for reaching out"). Ask contractors for a quote "at your earliest convenience," never "by Friday" unless David gives the date. (David, 2026-11-09, E&E contractor quote draft, corrected twice.)`
2. `At about 150k tokens in a session, write a 10-line brief to the vault and tell David once. Don't wait for 250k+. (11/05 to 11/09: 10+ sessions hit 200-566k.)`

### Memory entries
1. 
```markdown
---
name: feedback_dont_name_stepped_away_people
description: Do not mention people David says are stepping away, and don't re-add items he ruled out
metadata:
  type: feedback
---

David (2026-11-06, E&E water line): "stop mentioning marios name. he stepped away and trying to compartamentalize things." Also dropped: pressure gauge, permit.

**Why:** He is separating work streams, and the repeated mentions are noise.
**How to apply:** In E&E plans and drafts, assign work by role, not by Mario's name. Don't re-add dropped scope items.
```
2.
```markdown
---
name: feedback_one_command_center
description: One Command Center, no parallel artifacts or standalone tabs
metadata:
  type: feedback
---

David (2026-11-05): competitor info "should all just be inside of each dashboard," no separate artifact or desktop-bar entry. 11/06: "I thought we were going to make one here that had everything."

**Why:** Parallel surfaces drift, and he sees them as missing data.
**How to apply:** Put new data inside the existing brand dashboard and Command Center. Ask before creating a new tab or artifact. See [[feedback_ask_before_changing_format]].
```

### New skill stubs
```markdown
---
name: ops-compliance-filing
description: Handle recurring filings and vendor reports (WMA usage report, sales and use tax). Use when David says "automate this filing," "usage report due," or "sales tax."
---

1. Find the notice or last filing in the brand's Gmail and vault. Note due date and form.
2. Pull the numbers from FareHarbor or the books. Show the math.
3. Draft the form or reply in full for David's approval. Never submit unasked.
4. File a dashboard item with the due date and default per the dashboard rule.
5. Save a recipe note in the brand vault `Operations/Recurring Filings.md` so next quarter is one run.
6. If the amount is zero and the form is simple, write a copy-paste prompt for the manager's Claude.
```

## Quiet
Nothing quiet.
