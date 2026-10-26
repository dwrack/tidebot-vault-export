---
type: analysis
status: findings + proposed system; rollover rule decided 2026-10-19 (not yet in Periode), nothing built or sent
created: 2026-10-19
sources: Periode merchant API (subscriptions, pulled 2026-10-19) + Periode Payments exports in Operations/Sales Data (Nov 6 2025 to Oct 12 2026, deduped)
related: "[[Community Framework — Fire Ladder + Stoke (Oct 2026)]]", "[[Post-Visit Text]]"
---

# Membership Usage Study (Oct 2026)

**One line:** Ember 2 members use their sessions and stay. Ember 1 members use 2.7 of 4 and almost half the Ember 1 months are below drop-in break-even, so those members are quietly overpaying and the usage fade shows up one to two cycles before they cancel. We can see all of this per member from the Periode export, which means a weekly watchlist is buildable today.

Per-member sheet: `Operations/Sales Data/Member Watchlist 2026-10-19.csv` (68 rows, cycle-by-cycle usage, last visit, flags).

## Snapshot (verified 2026-10-19)

| | Ember 1 ($99, 4 off-peak) | Ember 2 ($149, 8 any time) | Total |
|---|---|---|---|
| Active records | 21 | 20 | 41 |
| Comped / crew (0 charges) | 0 | 6 | 6 |
| Paying members | 21 | 14 | 35 |
| Cancelled (real people, not test accounts) | 15 | 13 | 28 |
| MRR (next charge, active) | | | ~$4,940 |
| Lifetime dues collected | | | $19,735 |
| Lifetime member add-ons (extra sessions, paid guests, private) | | | ~$11,280 |

New memberships per month are climbing: Jun 6, Jul 7, Aug 10, Sep 11, Oct 8 so far. Member sessions per month went from 19 in January to 101 in September.

9 emails have cancelled and come back (one of them three times). "Cancelled" is often a pause with no pause button.

## How members actually use it

Complete paid billing cycles inside the export window:

| | Ember 1 | Ember 2 |
|---|---|---|
| Cycles measured | 85 | 45 |
| Avg sessions used | 2.7 of 4 (67%) | 6.0 of 8 (76%) |
| Cycles with 0 sessions | 12% | 4% |
| Cycles with 0 or 1 | 24% | 9% |
| Cycles hitting the full allowance or more | 36% | 40% |
| Cycles below cash break-even vs drop-in | 45% (under 2 sessions) | 16% (under ~3) |

Break-even: Ember 1 beats paying $49 off-peak only at 3+ visits. Ember 2 beats drop-in at 3 visits. The Ember 2 crowd is a different animal: they come, they pay for extras (35 of 45 cycles had paid add-ons), they bring people.

**When members come:** 7pm and 5pm are 41% of member visits. Monday and Thursday are the top member days (Monday Banya helps). Members are filling the weekday slots that otherwise sit at 13 to 22% fill, which is exactly where we want them. 47% book same day, 65% within a day. Reminders have to be "this week," not "this month."

**Path in:** 37 of 62 paying members visited as a drop-in first. Median 23 days from first visit to joining; 13 joined within a week. 25 joined cold off the site.

## What cancelling looks like before it happens

28 real cancels split cleanly:

**15 left after 0 or 1 paid cycle.**
- 5 were crew, Early Bird or comp accounts churning (Mack, Jordan, Hannah B, Erin) - not real churn.
- 4 barely used it (0 to 2 sessions): devindimeoediger, hightideenergy, abundanciacoffee, erin@.
- 5 were the Jan to Mar guest-pass runners: dnokovic (4 own + 9 paid extra + 14 guest seats in one month), elizemails (5 + 5 + 8), jankekolb, syoung. That is the abuse pattern the May 5 guest policy fixed. They bought a month to run friends through, then left.

**13 left after 2+ cycles.** Usage fell from an average of 3.9 per cycle to 2.6 in the final cycle. The fade is visible every time:

| Member | Sessions per cycle, first to last |
|---|---|
| jwoodpdx (E1) | 4, 4, 3, 1 |
| craigvern (E1) | 4, 1, 1 |
| yorefinnej (E1) | 4, 4, 2 |
| elizemails (E2) | 5, 1 |
| chrisjensen10 (E1) | 4, 2 |
| aestevens617 (E1) | 3, 3, 4, 4, 3, 1 (came back Oct 9) |
| edelgadore, dan_galucki (E1) | 2, 0 and 1, 0 |

Two cancelled at full usage: josiahdmarshall (8, 8, 8, last visit Aug 30, likely moved or seasonal, win-back candidate) and zjd5007 (4, 4, 5, actually an upgrade to Ember 2).

**The signal:** one cycle at 0 or 1 session after a healthy run means a cancel within one to two cycles. Two low cycles in a row and they are gone. Nobody cancels mid-fade with a warning; the cycle just ends.

## Two leaks worth fixing

**Guest passes vanished after May 5.** Jan to Apr: 155 guest seats (67 free, 88 paid at $25/$29). May onward: zero rows itemized as "Ember 1 Guest" / "Ember 2 Guest". Either the policy ended guest use completely or Periode stopped itemizing guests. Either way, the "$25 bring a friend" benefit is not showing up in the data, and the Stoke Passes idea in the Community Framework depends on it working. Check with Jonah / Periode.

**Members paying full price with sessions left.** 14 sessions ($742) across 8 members were bought at $49/$59 while they still had allowance. 8 of the 14 were off-peak, so they booked logged out. alishamcb did it 5 times, then went quiet in August. A member who pays $59 on top of $149 and then sees unused sessions expire has every reason to cancel.

## Watchlist right now (data through Oct 12)

| Member | Tier | History | What's happening | Move |
|---|---|---|---|---|
| alishamcb@yahoo.com | E2, 7 cycles, $966 paid | avg 3/cycle | 0 sessions last 2 cycles, last visit Aug 13 (60 days). Overpaid 5x earlier. | Personal text from Davey this week. Offer pause or rollover. |
| nastja.rebrin@gmail.com | E1, 9 cycles | avg 1.8/cycle | last visit Sep 13, 0 this cycle. Chronic low user who is loyal anyway. | Personal check-in; invite to a standing slot. |
| ldunn88@gmail.com | E1, 2 cycles | 2, then 0 | last visit Sep 11, day 15 of cycle with nothing booked | Nudge with this week's open evenings. |
| danandersonpt@gmail.com | E1, 8 cycles, $904 paid | 0 visits under this email ever; next charge now $0 | Probably books under another email, or a gifted/discounted account. | Verify in Periode admin before any outreach. |
| jchris036@gmail.com | E2, joined Sep 28 | 1 visit in 14 days | Slow start on the $149 tier | First-two-weeks nudge. |
| khriziakamille@gmail.com | E1, joined Oct 12 | brand new | | Welcome text with 3 slots to pick from. |
| hbronfman, jacquelinesoukup | comped E2 | last visits Aug 9 / Sep 25 | | Nothing, crew. |

**Upsell to Ember 2 (they are paying extras every month on Ember 1):** nastiakuznets (22 paid extras lifetime), aestevens617 (10), gregost777 (6, used 6 in one cycle), miriam4vidal (6), kennedyhutsell (6). A "you would have saved $X on Ember 2" note is honest and converts.

## The re-engagement system (proposed)

Run from a fresh Periode export every Monday (the documented Chrome-bridge CSV flow on mbp-2), compute flags, post the watchlist plus pre-drafted texts to Davey in Slack. He sends in a few minutes. Automate the SMS steps once Twilio A2P is verified (the post-visit text job already has the plumbing).

| # | Trigger | Action | Channel |
|---|---|---|---|
| T1 | New member, no booking 5 days after joining | "Pick your first slot" with 3 open evenings | SMS or email, automated |
| T2 | Day 12 of cycle, 0 sessions | This week's open slots | SMS, automated |
| T3 | Day 21, 0 or 1 used | "2 left, they reset on the 4th. Book this week and we roll one forward." | SMS, automated |
| T4 | 21+ days since last visit, any member | Personal text from Davey or Jonah. No offer, just a check-in. | Manual |
| T5 | Cycle ends at 0 or 1 after a healthy run (the fade) | Invite to a standing slot (Tue 6am crew, Sunday reset) or a free one-month pause | Manual, personal |
| T6 | Cancel | Day 3: "we kept your seat" + pause option. Day 30: win-back. Full-usage cancellers get a personal note, not a template. | Email + text |
| T7 | Full-price booking while allowance remains | Same-day: "you had sessions left, refunded the difference" | Manual via Periode admin |
| T8 | Non-member books a 2nd visit within 30 days | Membership offer (median join is 23 days after the first visit) | Email, automated |

### Product changes that matter more than messages
1. **Roll one unused Ember 1 session forward** (cap the bank at 2). 45% of Ember 1 months are below break-even. Those members will do the math eventually; rollover removes the "I wasted $99" feeling that precedes every fade.
2. **Pause instead of cancel.** Periode supports skipping a charge. Make "pause a month" the first thing a cancelling member sees. 9 of 28 cancels came back anyway; make the path shorter.
3. **Membership applies at checkout automatically.** Kills the full-price leak.
4. **Verify guest passes still work** and reframe them as Stoke Passes per the Community Framework.
5. **Visit milestones.** The export gives per-member visit counts, so the Fire Ladder is feasible from the weekly job with no Periode changes.

## Decision 1 (Davey, 2026-10-19): roll unused sessions forward, friend-usable

Rule as proposed (needs Jonah's OK and a Periode feasibility answer):
- At the end of a paid cycle, unused sessions carry into the next cycle. Bank cap: 2 carried sessions at a time (so an Ember 1 member can hold at most 6 in a month, Ember 2 at most 10). Carried sessions expire at the end of the cycle they land in; they do not stack forever.
- A carried session can be used as a friend seat instead of the member's own: the friend comes free, member present at the session (same rule as the May 5 guest policy). Call it a Stoke Pass when it is used that way, per the Community Framework.
- Ember 1 carried sessions stay off-peak. Comped accounts do not accrue carry.
- The friend gets the normal post-visit text; a second visit within 30 days triggers the membership offer (T8).

Why this works on the numbers: 24% of Ember 1 months end with 0 or 1 used, so most carry goes to people who were about to feel ripped off. Seats are near-zero marginal cost at 13 to 34% weekday fill. The only revenue at risk is the $29 extra-session and $25/$29 paid-guest line (about $10K lifetime), and a free friend seat is a better acquisition channel than a $29 one: 37 of 62 members came in as a drop-in first.

Periode feasibility: unverified. The merchant API has no write endpoints for punches or items. Ask Erik Kvanli whether Periode can (a) auto-carry unused subscription punches with a cap and expiry, or (b) let admin add punches to a member manually. Fallback if neither: the Monday watchlist job lists each member's carry count at cycle end and Jonah or the ops assistant applies it in admin, or we issue the friend seat as an admin-generated gift code.

## Open decisions
1. ~~Rollover for Ember 1~~ Decided above: yes, with friend use. Still open: cap of 2 and one-cycle expiry OK?
2. Pause-instead-of-cancel as the default cancel path?
3. Who sends the personal texts (T4, T5): Davey, Jonah, or Hannah/Jess from the business number?
4. Text alishamcb, nastja.rebrin and ldunn88 this week?
5. Verify danandersonpt (8 months paid, zero visits) and the guest-pass zero since May with Jonah / Periode.
6. Build the Monday watchlist job on mbp-2?

## Method notes
- Member visits = $0 "BOOKING ITEM" rows for a session product under the member's email, net of $0 refunds, bucketed by billing cycle (charge date to next charge date). Guest seats = Item name containing "Guest". Paid extras = paid session rows that are not guest seats.
- Comped accounts = ACTIVE with no charges: doleshko (2 records), jacquelinesoukup, mack@, hbronfman, grant@kerfbuilds. Test accounts excluded: erik@periode.no, erik+100@, jess@ours-here, eabinante+.
- Export ends Oct 12 2026, so "this cycle" numbers are partial for anyone whose cycle started after mid-September.
- Capacity assumption from the July analysis still unverified against Periode admin.
