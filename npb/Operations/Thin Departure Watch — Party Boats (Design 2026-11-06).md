---
type: design
business: NOLA Party Barge
status: awaiting David's approval (nothing built, nothing scheduled)
created: 2026-11-06
data: FareHarbor bookings by tour date, Sep 11 to Nov 5 2026 vs Sep 12 to Nov 6 2025, pulled live 2026-11-06
decision-record: TheBrain/07 Reference/Decisions/2026-11-06 NPB thin-departure watch.md
---

# Thin Departure Watch: party boats (design for approval)

Goal from the Jeff call: nobody has to remember to check thin boats or double-booked guides. Version 1 only recommends. Jeff or David makes every move in FareHarbor, and nothing reaches a guest or a guide.

## What the data says (last 8 weeks, shared-seat departures only, privates excluded)

| | 2026 | Same weeks 2025 |
|---|---|---|
| Shared-seat departures that ran | 147 | 197 |
| 6 guests or fewer | 34 (23%) | 51 (26%) |
| ...of those, another shared boat within 2 hours had room | 22 (82 guests) | 27 |
| Thin ones by day | Sun 13, Fri 8, Sat 8, Wed 3 | Sun 12, Fri 10, Thu 10 |

Timing matters more than I expected:
- At **2 days out**, 16 of the 34 departures flagged as thin went on to fill past 6. Acting that early would move guests off boats that end up healthy.
- At **1 day out**, 21 of 34 final thin departures are visible; 13 of the flagged ones still fill.
- 13 thin departures had **zero** bookings the day before. Their first booking came the same day.

## The design

**Threshold:** thin = 1 to 6 guests on a shared-seat departure (Freaky Tiki, Twerkin Tiki, Bayou Boogie, Party Queen). Six seats is about $340 gross against the captain ($80 a run per the vault) plus deckhand, fuel and ice. Jeff can move the number in config.

**Timing:** one run a day, 10:00 CT, on davids-mbp-2. One message, three parts:
1. **Tomorrow (act):** each thin departure with the recommended move.
2. **Day after (watch only):** listed, no action. Half of these fill.
3. **Today (late changes):** only departures that turned thin or got a guide clash since yesterday's post.

**What it recommends, in order:**
1. **Fold** onto another shared boat the same day within 2 hours that has room (Tiki to Tiki first). The post includes a paste-ready text Jeff can send in his own name.
2. **Rebook** to the nearest day in the next 7 that already has 12+ guests on that boat, if nothing fits the same day.
3. **Private upsell** if the group is 5 or 6 and no fold fits: "have the boat to yourselves for the difference," Jeff's call on price.
4. **Run it** if none of the above fits, and say so, so Jeff knows it was checked.
5. **Close empty siblings** on slow days: if a Sunday or weekday has an empty shared slot next to a booked one, recommend closing the empty one so late buyers land on the boat that is already running.

**Guide clash check (same message):** reads the crew assigned to each departure in FareHarbor and lists any person on two departures whose times overlap, counting 30 minutes of turnaround.

**Where it posts:** #helm-npb, at most one bot message a day, and only when there is something thin or a clash (quiet days post nothing). For the first week it posts to David by DM only, so you can check the calls before Jeff and Michael see them.

**What it costs:** $0 a month. Plain Node script on the FareHarbor cookie already used by the kayak checker. No paid APIs, no Claude tokens. Build time is about 2 to 3 hours, reusing the kayak `thin-check` code.

**Value:** 22 foldable departures in 8 weeks is about 3 a week. At roughly $150 to $180 saved per departure not run (captain $80 plus an assumed deckhand and fuel), that is about $450 to $550 a week through the slow season. The deckhand and fuel figures are my assumptions; Jeff should give the real ones.

## Fewer departures on slow days (Sunday example)

Sundays have had 27 shared departures in 8 weeks with a median of 7 guests, and 13 of them were thin. Sunday 2pm ran once in 8 weeks (13 guests). Recommendation for Nov to Feb: on Sundays, sell shared seats at **1pm, 3pm and 5pm only, one boat per slot**. Keep the other times open for privates. Same idea for Friday 10am to noon, which ran 3 to 6 guests most weeks. This is a FareHarbor schedule change for Jeff or Michael to make, not something the watch does.

## Friday same-day bookings: nothing is broken

| Fridays, last 8 weeks | 2026 | 2025 |
|---|---|---|
| Same-day bookings | 62 (145 guests) | 102 (253 guests) |
| Share of Friday bookings made same day | 32% | 31% |
| Booked less than 2 hours before departure | 9 | 30 |
| Same-day bookings from resellers (all days) | 5 | 22 |

- The share of Friday business booked same day is unchanged. The count is down about 40%, the same as Friday overall (guests down about 35%) and the 45% weekend pace drop.
- Today (Fri 11/6) had 4 same-day bookings. They are still coming in.
- The last two Fridays were the weakest (3 and 4 bookings), but the same Halloween-week dip happened last year (5 and 7).
- Two real gaps: (1) last-minute Friday bookings fell from 30 to 9. In 2025 the late Friday boat left at 6pm and drew 34 same-day bookings; in 2026 most late Friday boats leave at 5pm. (2) Same-day reseller bookings (Viator and similar) fell from 22 to 5. Neither is a broken button. They are schedule and channel questions.
- Saturday under-2-hour bookings still happen (15 in 8 weeks), so there is no global booking cutoff blocking late buyers.

## Guide double-booking: what is actually happening

- No code anywhere assigns guides. Searched the always-on Mac, TideBot and both vaults on 2026-11-06. Jeff assigns crew by hand in FareHarbor. The June to-do had him batch-assign captains to every weekday tour with the Availability Updater, which puts the same captain on every departure that day. That is the likely source of "a guide gets the whole day."
- FareHarbor assigns crew per departure, so the fix is in how they get assigned:
  1. **Now:** the clash check above flags every overlap the morning before.
  2. **Process:** assign crew per departure instead of per day in the bulk updater. Assign the second boat at the same hour to a different captain.
  3. **Later, if wanted:** a helper that lists who is free for each departure, from the same crew data. Read-only; Jeff still clicks.
- To confirm with Jeff: is there an automatic assignment setting he turned on in FareHarbor, or is it the bulk updater? A screenshot of how he assigns a day settles it.

## Guest side: ask for flexibility first (added 2026-11-10, David)

NOLA trips are planned tight, so the rule is: we only move people who already told us they can move. Nobody gets a "too few people" message.

1. **Checkout (optional, one question):** a weather backup question in FareHarbor. Rain or wind does move boats here, so the ask is real and it doesn't sound cheap.
2. **Day-before text, thin boats only:** only to guests on a thin boat who skipped the checkout question. Everyone else hears nothing new.
3. **The move itself:** framed as combining two boats into one bigger party at a time they said works. On a party boat a fuller boat is the selling point. We never say weather when it isn't weather.
4. **"Keep my time" is respected:** that group runs as booked, or gets offered the boat to themselves. They never get asked to move.

Drafts are in the 2026-11-10 session. Questions for Jeff and Michael are in the appendix of `NPB Ops Sync — 2026-11-11 Agenda.md`.

## Approve to build

- [ ] Threshold 6 guests, one 10:00 CT post, fold > rebook > private > run
- [ ] First week: DM to David only, then #helm-npb
- [ ] Include the guide clash check
- [ ] Sunday shared seats at 1, 3, 5 only (Jeff or Michael changes FareHarbor)
