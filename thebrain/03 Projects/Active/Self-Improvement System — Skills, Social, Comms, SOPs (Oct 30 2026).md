# Self-Improvement System: Skills, Social, Comms, SOPs

Created 2026-10-30 from David's question "how can we self learn and improve." Survey of the vaults the same day.

> **CURRENT STATUS (verified 2026-10-30):** Loop 1 (corrections log) is live on dckt-guide-mac: nightly 23:40, Sunday rule proposals, tick-to-approve. David chose tick-to-approve for every rule edit. Still to install on wavey and mbp-2: run `TheBrain/Scripts/install-corrections-log.sh` once on each. Loops 2-6 not started. **Part 2 build A (Work Queue + nightly runner) is live on dckt-guide-mac** (verified 2026-10-30, smoke test passed in 40s): launchd `com.djl.work-queue` 10pm nightly, reads the Apple Note "Claude Queue" and `00 Dashboard/Work Queue.md`. Headphones: David chose both paths; the iMessage plain-sentence switch waits on mbp-2 access (channel lives there), the Siri Shortcut is queued after standing authorizations.

## The diagnosis in one line

We collect a lot of learning and close almost none of it. 06 Learning has 25+ saved frameworks, 55 loops produce reports, 94 SOP files exist, but the skills folder holds one real skill (seo-blog-writer, copied into 9 vaults) and the April vision board's "build one custom skill" is still open. Nothing turns a result or a correction into a changed rule.

What exists today (verified 2026-10-30):
- Inputs: 06 Learning frameworks, Newsletter Digest, Reading Queue, Courses, Books.
- Reports: review-watch, ad-optimizer, seo-watch, content-decay, opencx-watch, memory-freshness, social analytics (CURRENT RULES block in the 532 note, verified 10-14).
- Missing: a place where corrections land, a cadence that edits CLAUDE.md / skills / SOPs from evidence, SOP review dates, and a weekly "what changed" line.
- Memory is split: this root project's MEMORY.md is empty while the freshness report counts ~290 files on mbp-2 and ~1058 on the laptop. One home, not three.

## Six loops, cheapest first

### 1. Corrections log (build first, half a day)
- Trigger: nightly on mbp-2. Reads that day's session transcripts under `~/.claude/projects/*/`.
- Finds user turns that correct Claude (stop, don't, wrong, not that, I said, too long, wrong machine) and the assistant turn before them.
- Writes one line per correction to `TheBrain/06 Learning/Corrections Log.md`: date, vault, what Claude did, what David wanted.
- Weekly (Sunday, after life-ops): groups repeats, proposes a one-line rule edit to the right CLAUDE.md or skill file, tick-to-approve in `00 Dashboard/Approval Backlog.md`. Two ticks of the same correction in a month means it ships as a rule.
- Why first: the "stop recapping" rule took a frustrated message to get into CLAUDE.md by hand. This makes that automatic and compounds every week.

### 2. Social scorecard to rule refresh (weekly, per brand)
- Pull last 7 days of posts per brand (Meta Graph for IG/FB, Apify per-brand key for TikTok).
- Score each vs that brand's 90-day median reach. Log hook type, format, person-in-frame, length, caption length.
- Output: top 3 / bottom 3 per brand with the one variable that explains it, appended to each vault's `Marketing/Social Scorecard.md`.
- Rule change only on evidence: a variable has to win 3 weeks running before the CURRENT RULES block in the 532 note and the caption skill get edited. Otherwise it stays a note.
- Monthly: re-run the Apify competitor pull (same set as the Oct 14 study) so the rules are market-checked, not just self-checked.

### 3. Comms quality loop (weekly)
- Sample 20 outbound replies per week across OpenCX (bot + managers) and the business Gmails.
- Score against the tone rules (opens like a human, contraction use, one ask, close short, no "Dear"). Flag replies that broke a rule and replies that got a second inbound question (the answer missed).
- The most-repeated unanswered question each week becomes one FAQ entry in the bot training doc and one line in that brand's Guest Communication Templates SOP.
- Builds on the Aug "Complaints as Research" note, which is a method with no cadence yet.

### 4. SOP drift and corrective action (monthly, plus on incident)
- Add `reviewed: YYYY-MM-DD` and `owner:` frontmatter to all 94 SOP files (one-time sweep, Haiku).
- Monthly: list SOPs older than 6 months, and SOPs contradicted by a newer note on the same topic (search the vault for the SOP's subject after its review date). Output to `00 Dashboard/SOP Review/`.
- On incident: any 1-2 star review, refund, injury, or no-show complaint gets a corrective-action line that has to land in an SOP within 7 days. NKST already has "Incident Investigation & Corrective Action"; make it the template for every vault.
- Managers (Jeff, JT, Connor, etc.) see the diff, not the whole SOP.

### 5. Skill factory (monthly)
- Count which 06 Learning frameworks got cited in sessions that month (grep transcripts for the note title).
- Any framework used 3+ times becomes a skill in `~/.claude/skills/<name>/SKILL.md` with: when to use, the steps, one worked example from our data, and a 5-line self-check the skill runs on its own output.
- Candidates right now: 532 content grid, Sendable Reels hook formula, Blog Distribution Checklist (8 channels), Starving Crowd ad opener, Premium Brand 5 levers.
- skill-doctor already exists on mbp-2 but last exited non-zero (freshness report 10-26). Fix it, then have it run each skill against one fixture monthly and report drift.

### 6. Weekly Review as the hinge
- Weekly Review has gaps (nothing June 10 to Sept 17). Extend the Sunday life-ops run so the weekly file always carries a fixed "What we learned" block:
  1. one correction adopted as a rule
  2. one social rule changed or confirmed
  3. one SOP touched
  4. one skill built or fixed
  5. one thing we stop doing
- If a line is empty two weeks running, that loop is broken and goes to Loop Health.

## Guard rails
- Loops propose, David approves, except for additive notes (scorecards, logs). Rule edits to CLAUDE.md, skills, and SOPs always go through tick-to-approve.
- Every rule written carries "verified <date>" so the freshness loop can age it out.
- All of it runs on davids-mbp-2, never on the laptop.

## Order
1. Corrections log (this week)
2. SOP frontmatter sweep + Weekly Review block (same week, mechanical)
3. Social scorecard (next week, needs the per-brand Apify keys that exist)
4. Comms quality loop
5. Skill factory + skill-doctor fix

---

# Part 2: Learning from David's actual work, and working while he is away (added 2026-10-30)

David: "how else can we learn from my actual work, and how can I get you working more when I'm away from the computer and in between sessions. I don't want to sit at the computer as much."

## Where the time actually goes

The Approval Backlog on 2026-10-30 shows 9 items waiting 12 to 19 days. Claude is not short on capacity, it is short on decisions. Every loop ends in "waiting on you," so the more loops we add, the more sitting-at-the-computer we create. The fix is to move decisions off the desk (phone taps, standing rules) and to give Claude a queue it can pull from without being asked.

## Four more learning signals (beyond corrections)

| Signal | What it teaches | How (all from data we already have) |
|---|---|---|
| **Edits after Claude wrote it** | What David rewrites by hand is the strongest "you got it wrong" signal there is, and he never has to say it | Nightly: from transcripts, list every file Claude wrote or edited. Diff it against the file today. Where David changed wording, log the before/after to the Corrections Log as a "corrected by edit" row. Same script, one more pass. |
| **Approval outcomes** | Which drafts he ticks, which he kills, which he ignores for 3 weeks | Track every tick-to-approve file: ticked / deleted / stale. Killed and stale items feed the Sunday rule proposal ("stop proposing X"). Stale after 21 days gets auto-archived so the queue stays honest. |
| **What he actually sends** | His real voice per brand, vs what Claude drafted | Weekly: pull David's sent Gmail and iMessages (author = David). Where a Claude draft exists, diff draft vs sent. Refresh each vault's tone notes from the sent corpus, not from guesses. |
| **Session time audit** | Which business and which task types eat his hours, and what recurs (automation candidates) | Transcripts carry cwd, timestamps, cost. Weekly roll-up: hours per vault, top 10 recurring request types. Anything asked 3+ weeks running becomes a loop or a skill. |

## Working while he is away: three builds

### A. Work Queue + nightly runner (biggest lever)
- One file: `TheBrain/00 Dashboard/Work Queue.md`. David drops tasks in from anywhere: dictate to the phone session, an Apple Note titled "Claude Queue" (the Dump pipeline already reads Notes), or a text to the iMessage channel. One line per task, brand named.
- Nightly 10pm on dckt-guide-mac (and mbp-2 once installed): the runner reads the queue, takes every item not marked blocked, opens `claude -p` in the right vault with that vault's CLAUDE.md, does the work, writes the result next to the task line, and marks it done / needs-David with a one-line question.
- Morning brief (already runs 7:20a) gets a "Done overnight" block and a "Needs your tap" block. He reads it on his phone.
- Rules: anything outbound, money, deletes, or live-site stays in needs-David. Drafts, research, files, internal docs, data pulls run without asking.
- Safety: `claude -p` runs with the vault's permission allowlist, never bypass mode. Log per task in `~/Library/Logs/claude/work-queue/`.

### B. Standing authorizations (tick once, runs forever)
- `TheBrain/00 Dashboard/Standing Authorizations.md`: a list of categories Claude may do without a per-item tick. David ticks a category once; Claude checks the file before acting.
- Starter list to tick or reject: reply to 4 and 5 star reviews from the brand voice; answer OpenCX tickets that match an existing FAQ; file Apple Notes into vaults; publish blog drafts to WordPress as unpublished drafts; pause an ad set whose CPA runs 2x target for 3 days; send review-request SMS 24h after a tour; post the approved weekly GBP update.
- Each line carries a cap (per day, per brand, dollar limit) and "verified <date>." The Sunday rule proposal can suggest new lines from the approval-outcome signal above ("you ticked all 14 review replies this month, make it standing?").

### C. Phone-first approvals
- Each morning 7:35a: one push to the Claude app with the top 3 pending approvals as tap options (AskUserQuestion in the phone session, 2 to 4 choices each, batched into one card). Dictated "yes" is not an approval; the tap is.
- Items not tapped in 21 days get archived, not nagged. A queue he has decided against is worse than an empty one.
- iMessage fallback: reply "yes 2" to approve item 2, for when the app is not handy.

## Suggested order
1. Work Queue + nightly runner (one evening to build, uses the `claude -p` rail the loops already use)
2. Standing authorizations file with the starter list for a one-time tick
3. Phone-first approval push
4. Edit-diff learning pass added to corrections-log.py
5. Sent-corpus voice refresh and session time audit

## Headphones: talking to Claude hands-free (asked 2026-10-30)

| Path | Build | How it works | Catch |
|---|---|---|---|
| **iMessage + AirPods Announce Notifications** (use today) | none, if the iMessage channel on mbp-2 is up (last seen loaded 10-26, unverified) | Text the Claude iMessage line, Siri reads the reply in your ears, you dictate the next one. Phone-mode replies are already 3 lines, which is what makes this work. | Siri reads markdown literally. Replies on that channel need to be plain sentences, no tables or bullets. |
| **Claude app Voice mode** | none | Talk and listen in the regular Claude app. Good for thinking out loud and questions. | It is a chat, not a Code session: no vault access, no loops. Use it for brainstorming, then paste the gist into the phone session. |
| **"Hey Siri, ask Claude" Shortcut** (the real one) | one evening | iOS Shortcut: Siri dictation -> POST to a small bridge on mbp-2 over the Tailscale funnel -> `claude -p` in the vault -> reply spoken back by the Shortcut. Fully hands-free, has vault context, can queue work. | Needs the bridge (reuse the DocuSeal funnel pattern) and a token in the Shortcut. Outbound actions still end in a "say yes to confirm" step, spoken, then logged. |
| **Mac + AirPods at the desk** | none | macOS dictation into the terminal and Speak Selection to read replies. | Still at the desk, so not the point. |

Recommendation: iMessage + Announce Notifications now, build the Siri Shortcut as item 3 in the order above (it also becomes the fastest way to drop tasks into the Work Queue).
