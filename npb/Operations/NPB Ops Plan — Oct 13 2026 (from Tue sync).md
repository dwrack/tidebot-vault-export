---
type: plan
business: NOLA Party Barge (plus the kayak companies Jeff runs)
created: 2026-10-13
source: Tue Oct 13 ops sync, David + Jeff. JT and Michael absent.
status: v1, David to approve. Accountability loop goes live the moment he says go.
---

# Ops plan from the Oct 13 sync

Six problems came out of the call. Each one below has the fix, who owns it, the date, and how we'll know it happened. "Claude" items are already underway (see the bottom).

## 1. Jeff is the only adult in the room

**Problem.** Jeff carries kayak schedule, kayak phones, van, weekend boat phones, property, crew. JT does the baseline and no more. There's no one to send when a 4th boat books or a guide calls out.

**Fix.**
- Hire a captain-licensed utility first mate on a day rate. Flexible by design: boats, van, pickups, phones. Posting drafted, Max is the first name.
- Weekday first mate standard from now on: captain's license (or willing, we pay) plus checklist discipline. Current person trains for it or we hire for it.
- JT comes off ops and phones. Keeps murals and projects on a per-day basis. Jeff opens the conversation, David and Michael make it official Thursday. The fair test: offer JT the license. If he jumps, he keeps a seat.

| Step | Owner | By | Done when |
|---|---|---|---|
| Soft pitch to JT | Jeff | Wed 10/14 | Jeff posts "talked to JT" in #helm-npb |
| Official conversation with JT | David + Michael | Thu 10/15 | JT knows the new shape and has the license offer in writing |
| Sound out Max: license, day rate, availability | Jeff | Thu 10/15 | Three answers in Thursday's sync |
| Posting live to kayak guides, then Indeed + FB boating groups | Jeff | Fri 10/16 | Link in #helm-npb |
| First interviews | Jeff (David joins if asked) | Wed 10/21 | Names and dates on the board |
| Hire made | Jeff + David | Fri 10/30 | Signed ICA, first shift scheduled |

## 2. Thin kayak days eat Jeff's time and the margin

**Problem.** 1-2 guest departures the day before mean Jeff hand-texts people to move them, often to international numbers. He does this by hand every afternoon.

**Fix.** Claude's 24-hour under-minimum check, run as a revenue ladder (David, 10/13: "it's an opportunity Jeff sees as a problem"). Day before, each thin departure's guests get texted from the kayak Google Voice line in Jeff's name: ask for the Extended at the full +$65/person first, then half ($30), then free, with reschedule as the fallback at every rung and refund only if they ask. Replies are read and classified; a yes/reschedule/refund lands in the group DM for Jeff to action in FareHarbor. Ladder detail: `Operations/Revenue Ladder — Thin Departures, Drips, Win-Back (2026-10-13).md`. Spec is in the kayak vault.

| Step | Owner | By | Done when |
|---|---|---|---|
| OK or edit the ladder wording (templates.json, 3 rungs per case) | David | Wed 10/14 | Says "go" or sends edits; Claude flips config.send |
| DONE 10/13: private rung priced from FareHarbor (list $250/$350, softer $150/$210, floors clear the $100-125 guide) | Claude | Wed 10/14 | In config; David can change the floors |
| DONE 10/13: daily 9:45am + 3pm plan post to the group DM (what's thin, what we'll offer, to whom) | Claude | Wed 10/14 | First post seen 9:45am CT 10/14 |
| Google Voice sign-in on the always-on Mac (kayak account + Door County) | David | Wed 10/14 | ~/Projects/gv-bot/sign-in.command run once over Screen Sharing |
| Ladder texts via Google Voice (built 10/13, gated off until the sign-in + wording OK) | Claude | Thu 10/15 | First guest texted, reply classified and posted in the group DM |
| Ladder: rung 1 at 10am day-before, rung 2 at 3pm, rung 3 at 7:30pm, silent-guest handoff 9pm + 7am; re-checks FareHarbor before every text and stops if the departure filled; non-US numbers routed to Jeff for WhatsApp | Claude | Thu 10/15 | Reply post seen in the group DM |
| Apply the same ladder to the kayak email drip (em02+) and the party-boat win-back emails (h02, h03) | Claude drafts, Michael + David call it | Tue 10/20 | Rung order agreed in Tue sync, copy in the vault |

## 3. Septic is flooding the bathrooms again

**Problem.** Plumber says the well is cracked and bayou water gets in when the water's high. Toilets can't drain. Undoes the June restroom win.

**Fix.** Porta potty now. One diagnostic question to the plumber, then the right permanent fix. David's backflow valve only helps if water is backing up the line; if it's coming through the crack, the tank floods anyway. Pumping the tank out somewhere other than a truck is not an option.

| Step | Owner | By | Done when |
|---|---|---|---|
| Porta potty on site | Jeff | Fri 10/16 | Photo in #helm-npb |
| Plumber answers "crack leak or backflow?" plus a price to seal/line the crack | Jeff | Fri 10/16 | Answer in Thursday's sync or Slack |
| Two quotes for the permanent fix | Jeff | Tue 10/20 | Numbers on the board |
| Pick the fix | David + Michael | Thu 10/22 | Work scheduled |

## 4. Weather calls are judgment calls

**Problem.** Last week's thread went in circles on credits vs refunds. Saturday's "pedal wheelers too sketchy" was a feel, not a number.

**Fix.** One written policy on the site and in OpenCX. Wind and rain cutoffs per boat written down. Claude drafts the wording, Michael approves, Jeff sets the numbers.

| Step | Owner | By | Done when |
|---|---|---|---|
| DONE Policy wording drafted (we cancel = reschedule or refund; guest cancels inside 7 days on a forecast we're running in = credit; call 24h out, 2h day-of for wind) | Claude | Tue 10/13 | Draft in Operations/ |
| Approve wording | Michael | Thu 10/15 | ✅ in Slack |
| Wind + rain cutoffs per boat (tikis vs pedal wheelers) | Jeff | Thu 10/15 | Numbers in the policy doc |
| Live on site FAQ + OpenCX | Claude | Fri 10/16 | Link to the FAQ, OpenCX answers the question correctly |

## 5. Slack is noise

**Problem.** Michael: "limit it to one message a day." Jeff: the feedback load adds to the stress. Reddit focus mode has been stuck since Oct 6 waiting on people who don't want it.

**Fix.** One combined Claude + TideBot digest a day at 8am CT in #helm-npb. Reddit nudges paused. JT's daily update is 3 lines (plan, problem, photo), no reminders. Everything else waits for Tue/Thu.

| Step | Owner | By | Done when |
|---|---|---|---|
| Michael names what to kill outright | Michael | Thu 10/15 | List in Slack |
| DONE Reddit focus mode paused | Claude | Tue 10/13 | No more nudges |
| All bot posts consolidated into the 8am digest | Claude | Fri 10/16 | One bot post a day, verified for a week |
| JT 3-line daily update | JT | daily from Wed 10/14 | Streak visible in the digest |

## 6. Side money we keep leaving on the table

- **Marina event hosting.** The tent group from last year wants the lot again. Base fee plus a small cut, with a one-page package (deposit, COI naming us, permits, cleanup, no guests on docks after dark). Scott Kitner reads it first because of the live fatality claim. Draft is in Operations/. Jeff owes her name, date, headcount, ticket price, alcohol yes/no by Thu 10/15.
- **Liquor.** Jeff's read: an ABO permit for packaged beer and wine is the simplest path. Feeds the alcohol licensing project, not a this-week item.

## Loose ends from the call

Mark a row DONE by starting its first cell with `DONE`. The agenda builder skips those.

| Item | Owner | By |
|---|---|---|
| Michelle's Chase card: cancel or reassign | David | Tue 10/13 |
| Van: Stephanie takes it in, paid. Low tire = fixed same day, no pumping and driving | Jeff | Tue 10/13 |
| Permit portal "issued / closed": send Claude the permit number and which permit | Jeff | Wed 10/14 |
| Claude follows up with the permit office daily | Claude | from the day Jeff sends it |
| Carousels: Jeff reviews the party-boat and kayak boards | Jeff | Fri 10/16 |

## How accountability works from here

Three mechanics, nothing new to learn:

1. **Every item has one owner and one date.** They live in `Operations/NPB Action Item Tracker.md`. "We should" doesn't go on the board. "Jeff by Friday" does.
2. **Thursday's agenda builds itself from the board.** Claude generates `NPB Ops Sync — <date> Agenda.md` the night before: overdue items on top, each person's 1-2 items, then new business. The meeting opens by reading the overdue list out loud. Nobody chases anybody; the list does it.
3. **One digest a day, and it says who's due.** The 8am #helm-npb digest ends with "due today / overdue" by name. That's the only nag. If something's overdue twice, it comes up Thursday with the question "do we drop this or re-date it?"

Meeting discipline, since Tuesday ran 47 minutes for two people: when half the room is missing, cut the agenda to what the people present can decide. 30 minutes, hard stop. Items that need the absent person go to Slack with their name on them.

## What Claude is implementing right now

| Build | Status 2026-10-13 |
|---|---|
| Carousel review board for Jeff (party boats + kayak, verdict + note per carousel, saves live) | LIVE: https://claude.ai/artifact/5iPhZPVahfocPAauN2v1PT (David shares it with Jeff as Contributor) |
| Kayak 24h check + revenue ladder texter | BUILT 10/13 on the always-on Mac: 9:45am + 3pm plan post to the group DM (live), ladder texter 10am / 3pm / 7:30pm + handoffs 9pm, 7am, re-checks FareHarbor before each text (David 10/13: earlier in the day; no 2-day warning) (installed, sending gated off until David OKs wording + signs in Google Voice). Test: Thu 10/15 1-guest 9am → reschedule/private/refund ladder; Fri 10/16 2-guest 9am next to a 5-guest Extended → +$65 → $30 → free. Prices read from real bookings ($90 / $155) |
| Weather policy wording | Drafted, Operations/Weather & Cancellation Policy — DRAFT 2026-10-13.md |
| Utility first mate posting | Drafted, Operations/ |
| Marina event hosting one-pager | Drafted, Operations/ |
| Thursday agenda generator | Built (~/Projects/npb-ops-agenda/build_agenda.py); Thu 10/15 agenda already in Operations/ |
| Slack digest consolidation | Waiting on Michael's kill list; Reddit nudges paused now. Recap went as a group DM (David, Jeff, Michael) 10/13 |
