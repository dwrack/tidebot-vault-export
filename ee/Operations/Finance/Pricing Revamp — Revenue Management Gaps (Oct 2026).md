# Pricing Revamp: Revenue Management Gaps (Oct 13, 2026)

Compares Jonah's 10/12 "Getting closer on pricing" post in #pricing-revamp against the 3-level revenue management framework (Modern Hospitality Accelerator email Davey forwarded).

## Where Jonah's plan sits

Jonah's plan is a very good **Level 1**: a researched fixed price grid (72-sauna comp check), clear weekday vs weekend tiers, an event-date premium (xmas parade = weekend price), and retention built in (First Plunge, day-10 text, pause).

What it doesn't have yet is **anything that moves prices after launch**. Prices are set once on 11/1 and stay put until someone remembers to revisit. That's the exact trap the framework describes: underpriced on the best dates, overpriced on the slow ones. Our own data already shows it: weekends 58% full vs weekdays 25%.

## Gaps and actions

| # | Gap in current plan | Action | Effort |
|---|---|---|---|
| 1 | No KPI to judge prices by | Track **revenue per available seat-hour** (our version of ADR x occupancy), weekly, split weekday/weekend/private. Realized, after discounts and comps | Low, Periode export + script |
| 2 | Prices never move after 11/1 | Monthly price review with written triggers, e.g. a weekend slot over 85% full 14 days out → +$5-10 next month; a weekday slot under 20% for 4 weeks → convert to 1-hr or cut it | Low |
| 3 | No booking-pace view | Extend the ad pacer from "next-7-day fill" to a per-slot booking curve vs the last 4 weeks. Alert-only first, same as today | Medium |
| 4 | Demand we create isn't priced | When content/press spikes bookings (NPR, 1859, a reel that hits), that's our signal to hold or raise weekend price, not discount. Define an "event date" price above $60 (e.g. $70) and keep a dated event list (Bridgeton calendar, parades, Sauna Festivaali) | Low |
| 5 | Floors aren't written down | Set a floor per product ($35 / $50 / $60 social; $500 / $600 boat; $200 / $250 small). No code, comp or ad-hoc deal goes below it without a founder OK | Low |
| 6 | Small private launch has no review trigger | Jonah's 9/30 post said re-run after 60 days; the 10/12 post dropped it. Put it back with a number: weekend small privates over 70% booked 14 days out → $275 | Low |
| 7 | Comp set check is one-time | Re-run the competitor price check quarterly (Apify, ee account). Löyly and SweatHouz both moved in the last month | Low |
| 8 | Discounts leak quietly | Use L's discount templates to report monthly: list price vs realized price per product, and discount $ by type (influencer, donation, SERVICE, lodging) | Low, data exists |
| 9 | No policy for discount asks | Written answer for "can we get a deal" requests (corporate, groups, double-books). Default no; offer a better-fit product instead (First Plunge, private) | Low |
| 10 | Last-minute empty weekday seats | Don't discount publicly. 24h before an under-filled weekday slot, push it to members, First Plunge holders and lapsed guests | Medium, needs AC/Twilio flow |

## What not to do

- Don't buy the accelerator. Everything above is doable with Periode data + the pacer + Apify.
- Don't plug in a dynamic pricing tool (PriceLabs-style). Periode doesn't support it and our volume is too small for it to learn anything useful.

## Last winter (Periode exports, pulled 2026-10-13)

Approx paid Social seat fill (Sat/Sun vs Mon-Fri, 7 sessions x 8 seats; ignores privates blocking sessions, so a rough floor):

| Month | Net revenue | Weekend fill | Weekday fill | Gift cards sold |
|---|---|---|---|---|
| Dec 2025 | $20,016 | ~39% | ~6% | $3,207 |
| Jan 2026 | $51,122 | ~72% | ~24% | $2,378 |
| Feb 2026 | $31,561 | ~91% | ~25% | $2,271 |
| Mar 2026 | $27,349 | ~50% | ~19% | $689 |
| Sep 2026 | $35,598 | ~53% | ~23% | $324 |

- Winter weekends nearly sell out. Weekdays stay at ~25% even in the best month.
- Periode can't auto-price by demand, but each session has a price % (checked admin 2026-10-13). So set a higher winter weekend % for Dec-Feb by hand once. No tool needed.
- Weekday is a demand problem, not a price problem: corporate, ads, ET brand content.
- Dec 2025 was opening month (opened 11/7), so this Dec should run well above last year's.

## Open

- Who owns the monthly price review (Jonah? L?)
- Approve the floors in #5 before 11/1 go-live
