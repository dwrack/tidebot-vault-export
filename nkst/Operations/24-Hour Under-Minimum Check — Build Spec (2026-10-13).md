---
type: build-spec
business: New Orleans Kayak Swamp Tours
status: SPEC, build this week. Jeff OKs first drafts in Slack before anything sends.
created: 2026-10-13
source: NPB Ops Sync 2026-10-13 (David + Jeff). Jeff named this as the one thing he wants off his plate by Friday.
---

# 24-hour under-minimum check

## What it does
Every afternoon, look at tomorrow's kayak departures. For any departure that is thin, draft the outreach Jeff would have written by hand, post it to Slack, and send once he OKs. After a week or two of clean runs, flip to auto-send with a daily digest.

## Rules (from the call, confirm with Jeff)
- **Minimum is 2 guests** (set in FareHarbor 2026-09-25; solo guests get moved to a private tour, new date, or refund). The confirmation email already tells guests this.
- **Thin = 1 guest** (under minimum) **or exactly 2 on the 2-hour Manchac**. 1 guest: reschedule, private, or refund. 2 guests: David wants them consolidated, not run at a loss.
- **Consolidate first.** Move the 2-guest group to a departure that already has people. If an Extended Manchac or Whitney combo runs that day, offer the upgrade at a discount so the Extended still goes and the 2-hour doesn't have to. Jeff: this also keeps the 9am slot open.
- **Extended + combo fold together.** Two people on an Extended and two on a combo become one departure.
- **Jeff's "no transportation available" trick** keeps the 9am bookable without a van. Keep it; don't let the check "fix" it.
- **Weather:** same pass flags guides in Slack when tomorrow's forecast is bad. (Numbers for wind/rain cutoffs still owed by Jeff.)
- **Airboat / Honey Island:** out of scope until Jeff says otherwise (Honey Island items are hidden right now anyway).

## Wording
Jeff's existing reschedule texts, verbatim, with the guest name and options filled in. He drops them in #helm-npb. Claude does not write its own version.

## Channels
- US numbers: Google Voice on the kayak line (same scrape approach as the JT daily loop, Chrome Profile 26). Known problem: GV logs out. A dead session must post "GV logged out, nothing sent" to Slack, never skip silently.
- International numbers (common on kayak bookings): WhatsApp via Twilio or OpenCX, else the booking email.
- Slack: #helm-npb, one post per thin departure with the draft and a ✅ to send.

## Data
- FareHarbor availability + headcount per departure: External API (keys at ~/.config/fareharbor/npb.env; check the kayak company shortname). Named bookings are not reachable by API, so guest names and phones come from the dashboard scrape (auth.json, same as the review texter).
- Runs on davids-mbp-2 as a launchd job, 3pm CT daily.

## Approval ladder
1. Week 1-2: every draft to Slack, Jeff ✅ before send. David: "let it mess up, we learn, but we watch it."
2. After that: auto-send, with a 3pm digest of what went out and a Slack ping on anything that needs a human.

## Open questions for Jeff
- Is exactly-2 on the 2-hour always a consolidate, or only when an Extended runs that day?
- Discount amount for the upgrade to Extended.
- Wind and rain cutoffs per tour.
- His reschedule texts.

## Update 2026-10-13 pm: it's a revenue ladder now

Built and installed on the always-on Mac (`~/Projects/fareharbor-brief/thin-check/`): `thin.mjs` finds thin departures at 3pm CT and posts the plan to the David+Jeff+Michael DM; `send.mjs` is the ladder (ticks 3:10pm, 5pm, 7:30pm, 9pm day-before, 7am day-of). Rungs: Extended at +$65/pp → +$30 → free, reschedule offered at every rung, refund only when the guest says it. Replies are read from the kayak Google Voice thread and classified (yes / another day / refund / private / keep / no / unclear) and posted to the DM. Wording lives in `templates.json` (Jeff's voice, edit freely). Sending is gated by `config.send` until David OKs the wording and the kayak Voice account is signed in. Full ladder incl. drips and win-back: NPB vault `Operations/Revenue Ladder — Thin Departures, Drips, Win-Back (2026-10-13).md`.
