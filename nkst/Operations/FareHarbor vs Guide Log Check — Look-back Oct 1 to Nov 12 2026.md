# FareHarbor vs Guide Log Check: Look-back Oct 1 to Nov 12, 2026

Verified 2026-11-12 (live pull from FareHarbor and the guide Slack channel, read-only). Started by Stephanie's note in the Jeanette Quirk review thread: unsigned waivers, guests not checked in, money owed.

Scope: 58 guided departures, 181 bookings, 399 guests. Rentals, gift cards and passes left out. "Guide" below means the guide assigned in FareHarbor for that departure.

## The review

Jeanette Quirk is our guest. She was the second person on Ray Valek's 2-guest booking (374432506), **Fri Nov 6, 2:00 PM Manchac, guide Abbie Marks**, 10 guests. Her name is only on the signed waiver, not on the booking, which is why searching the manifest by name found nothing. Review posted Nov 12, six days after the tour. It was Abbie's 3rd tour in this window.

Abbie's own log that day (posted 6:15 PM) backs the review up: 10/10, incidents "No", but under Other Notes: "Got stuck in the hyacinth mentioned above" and "Traffic sucked. anyone have tips on avoiding ??". Emily ran the 11:30 the same day and logged "Canal otw to buzzards is blocked by water hyacinth", but her log posted at 4:35 PM, after the 2 PM group was already on the water. So the route warning existed and reached the next guide too late. Nobody answered Abbie's traffic question in the log.

## What the numbers say

| Check | Result |
|---|---|
| Bookings checked in | 143 of 181 (79%) |
| Tours with zero check-ins | 12 of 58 |
| Guests with no FareHarbor waiver | 41, across 26 bookings |
| Tours where the log said "Waivers signed? Yes" but fewer waivers than guests who went | 7 (first pass said 20; see re-check below) |
| Tours where the guide counted fewer guests than FareHarbor and nobody fixed FareHarbor | 8 tours, 13 guests |
| Tours with no trip log | 11 (2 had no guide assigned) |
| Money open | $330 owed to us, $259 owed back (details below) |

Check-in note: guides tick one name per party, so this is counted per booking, not per guest. Every check-in that exists was done the same day as the tour.

## By guide

| Guide | Tours | Bookings checked in | Zero check-in tours | Guests missing waiver | Said "yes" but short | Headcount gap not fixed | No log |
|---|---|---|---|---|---|---|---|
| Stephanie Lazensky | 18 | 58 of 59 (98%) | 0 | 3 | 3 | 2 | 1 |
| Emily Clarke | 17 | 44 of 48 (92%) | 2 | 16 | 9 | 4 | 1 |
| Michelle Healey | 6 | 20 of 22 (91%) | 1 | 9 | 2 | 1 | 2 |
| River Bourne | 4 | 10 of 13 (77%) | 1 | 3 | 0 | 0 | 1 |
| Alexis Hingle | 3 | 7 of 9 (78%) | 1 | 0 | 0 | 0 | 1 |
| Abbie Marks | 4 | 2 of 19 (11%) | 2 | 2 | 2 | 1 | 0 |
| Chelsea Hines | 3 | 0 of 6 (0%) | 3 | 1 | 0 | 0 | 2 |
| MJ | 1 | 2 of 3 | 0 | 3 | 0 | 0 | 1 |
| No guide in FareHarbor | 2 | 0 of 2 | 2 | 4 | 0 | 0 | 2 |

How to read it:
- **Check-in is a two-person problem.** Abbie and Chelsea are not checking guests in at all. Looks like they were never shown how. Everyone with more than a few tours is at 77% or better.
- **Waivers are the bigger gap, and it is spread out.** Emily's tours carry the most (16 guests, 10 tours), then Michelle (9, though 6 of those are one tour, see below). The log line "Waivers signed? Yes" is being answered from memory, not from the manifest.
- **Headcount gaps are an office job, not a guide job.** The guide logs 8, FareHarbor still shows 11, and nobody marks the no-show or decides on a refund. That is where "money owed or needed refunds" comes from.
- "No log" here is stricter than the Slack reminder bot (it wants a written Pre/Post log matched to that departure), so treat it as a lead, not a verdict.

## Waiver re-check (2nd pass, verified 2026-11-12 late)

The first pass compared waivers to FareHarbor's headcount. That blamed guides for no-shows (no waiver needed if they never came) and for honest "yes, except..." answers. Re-checked live against guests who actually went (the guide's own count), including rebooked bookings and other waiver systems (none found).

Cleared: Stephanie Oct 5 and Oct 26 (missing guest was a no-show), Emily Oct 11, Oct 26, Oct 29, Nov 2, Nov 6, Abbie Nov 2 (missing guests didn't come). River Oct 16 ("5 out of 7") and Stephanie Oct 18 ("yes, except our GetYourGuide guest") told the truth in the log.

Real "said yes, short" (guests who went, minus waivers on file):

| Guide | Tour | Missing | Pattern |
|---|---|---|---|
| Michelle | Nov 12 9:00 | 5 of 5 (0 on file, both bookings) | none signed at all; ask about paper |
| Michelle | Oct 23 9:00 | 1 | Amanda Weber (Viator) booked 2, only she signed |
| Emily | Nov 3 9:00 | 3 of 4 | Hyun Kim booked 4, only Hyun signed |
| Emily | Oct 14 11:30 | 1 | Camille Deschamps booked 2, only she signed |
| Emily | Oct 25 9:00 | 1 | Rotramel family of 5, 4 signed |
| Emily | Nov 9 11:30 | 1 | Brittany Loomis booked 2, only she signed |
| Abbie | Oct 16 4:30 | 1 | Aaron Baker booked 2, only he signed |

Pattern: almost every miss is the booker signing for themselves and the rest of the party never signing. FareHarbor's "waivers additional participants" setting is OFF for NKST, so a booker can't add another adult to their waiver. Each adult has to sign separately, and a guide glancing at the booking sees a signature and answers yes. The clear misses are Michelle Nov 12 (none) and Emily Nov 3 (1 of 4).

No log at all, waivers missing (not a "said yes" problem): MJ Oct 21 (3), Emily Oct 9 1-guest, Chelsea Oct 10 1-guest, plus the two no-guide tours. Raw: `data/nkst-waiver-verify-2026-11-12.json` on mbp-2.

## Items to clear now

| Date | Tour | Guide | What |
|---|---|---|---|
| Nov 12 | 9:00 Manchac | Michelle | 6 guests in FareHarbor, 0 waivers on file, 0 checked in. Log says waivers yes and 5/5 with one sick cancel. Ask if they signed on paper, and the sick guest needs a no-show or refund decision |
| Oct 26 | 11:30 Manchac | Emily | Booking 385745456, 3 guests, $270 unpaid. Log says 8 guests, FareHarbor has 11. Almost certainly these 3 never came; cancel it or collect |
| Oct 23 | 9:00 Manchac | Michelle | Booking 387087979 overpaid $210. Refund or explain |
| Oct 10 | 11:30 Manchac | Emily | Booking 380460901 (7 guests) $90 short, booking 384761934 (1 guest) $49 over. Looks like a guest moved between bookings |
| Oct 25 | 2:00 Manchac | none | Booking 373102882 $10 short, no guide assigned, no log, no waivers. Did this tour run? |
| Oct 9 | 4:30 Manchac | none | 2 guests, no guide, no log, no waivers. Did this tour run? |
| Oct 23, Oct 29 | 9:00 Manchac | Michelle, Emily | Two Viator bookings each show $50 "due". Probably how Viator payouts post, not real money. Confirm once |

Headcount gaps (guide count lower than FareHarbor, FareHarbor never updated): Oct 5 (6 vs 5), Oct 11 9:00 (7 vs 5), Oct 26 9:00 (12 vs 11), Oct 26 11:30 (11 vs 8), Nov 2 9:00 (8 vs 6), Nov 2 11:30 (10 vs 8), Nov 6 11:30 (9 vs 8), Nov 12 9:00 (6 vs 5).

## How to make this run every day (proposed, not built)

FareHarbor gives us, per booking, through the same logged-in session the trip-log reminder already uses: check-in status per guest with a timestamp, waiver signatures (including minors and extra participants), amount due, amount overpaid, payments and add-on line items. So the check is a small add-on to the existing log watcher on the always-on Mac, not a new system.

1. **Before the tour (7:00 AM CT, to the guide, in the guide channel):** today's manifest in two lines: guest count, and the names with no waiver yet. The guide gets them signed at the van instead of answering "yes" from memory.
2. **After the log lands (same thread as the guide's log):** one reply only if something is off. Example: "FareHarbor has 11, you logged 8. Who didn't show? 3 parties aren't checked in and 2 waivers are missing (names)." The guide answers in the thread and fixes check-in on their phone. No message when the tour is clean.
3. **Office queue (Jeff, #helm-nkst):** what a guide can't fix: no-shows that need a refund or a no-show mark, bookings with money due or overpaid, departures with guests but no guide. Each one stays listed until FareHarbor shows it fixed, then drops off.
4. **Friday scorecard (David and Michael only, DM):** the by-guide table above for the week, plus what is still open. This is the "who" record, and it shows whether a training push worked.
5. **Close the loop:** an item only closes when the next FareHarbor pull shows it fixed. Nothing closes on someone saying "done".

Rules it follows: double-check on a second pass before any ping, skip rentals, group thread not a 1:1 DM, pay numbers never in a shared channel.

Upsells: add-on line items are readable per booking, but the trip log has no line for "sold an add-on on site", so there is nothing to compare against yet. If guides sell anything at the van, the template needs one line: "Anything sold or owed on site?"

Training fix that should happen regardless: a 5-minute "check in and check waivers from your phone" walkthrough for Abbie and Chelsea, and a one-line change to the pinned template from "Waivers signed? Yes" to "Waivers: __ of __ signed in FareHarbor".

## Found along the way

The trip-log reminder bot reads FareHarbor start times as if they were Pacific (the always-on Mac's clock), so it thinks every tour starts and ends 2 hours later than it does. Reminders go out about 2 hours later than intended. Not fixed here; it gets fixed in the same change as the check above.

## Data

Raw pull: `~/Projects/fareharbor-brief/data/nkst-recon-lookback-2026-10-01_2026-11-12.json` on davids-mbp-2. Script: `debug/recon-lookback.mjs` (read-only; re-run with any date range).
