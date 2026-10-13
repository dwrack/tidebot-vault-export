# Revenue Ladder: thin departures, drips, win-back

*Written 2026-10-13 from the Tue ops sync follow-up. David: "It's an opportunity Jeff sees as a problem, but we can make more money off of it." One rule, three places to use it.*

## The rule

Ask for the most money first. Drop one rung only on a "no" or silence. Never open with the discount. Every rung keeps a no-cost exit (another day) so nobody feels cornered, and refund is never offered until the guest says the word.

Why it works: the Extended already runs with a guide and boats, so an upsell seat is near-pure margin. Charging $65 beats $30 beats $0, but all three beat running a second guide for one paddler.

## 1. Thin kayak departures (BUILT, live once David OKs wording)

Prices from real bookings 10/13: 2-hour Manchac $90/person, Extended $155/person, gap $65.

| If | Then (rung 1, 10am day before) | Rung 2 (3pm, on "no" or silence) | Rung 3 (7:30pm) | 9pm + day-of 7am |
|---|---|---|---|---|
| 1 guest on the 2-hr, Extended runs same morning | Extended at +$65/pp, or another day free | Extended at +$30/pp, or another day | Extended free ("under our 2-person minimum"), or name a day, or say refund | Still silent → Jeff calls or runs it |
| 2 guests on the 2-hr (meets minimum), Extended same morning | Extended at +$65/pp, keeping the 9am is fine | Extended at +$30/pp | Combine groups: Extended free, reply "keep" to stay | Still silent → Jeff's call |
| 1 guest, another healthy departure same day (not Extended) | Move to that time, or another day | Same time or another day, private offered, refund if asked | Penciled onto the alt time, reply to change | Jeff's call |
| 1 guest, nothing else that day | Another day (two real dates with groups going), or private at 9am | Another day or private; refund only if neither | none | Jeff's call |

Reply handling: yes → Slack with the dollar figure ("+$130, charge the difference"); another day / refund / private / keep → Slack for Jeff, ladder stops; "no" → next rung on the next tick; unclear → Slack, a human answers. One text per rung, never twice, nothing between 9:30pm and 8am. Before every text the ladder re-checks FareHarbor: if the departure filled on its own, it stops and the tour runs as booked (a yes to the Extended already given stands).

Timing (David 10/13): earlier in the day beats later, so the first ask goes at 10am and the day is the runway. No 2-day-out warning: our bookings are last-minute, so most 48-hour thin departures fill, and "minimum" that early reads as "your tour might be cancelled." If we ever touch guests 2 days out it's a pure upsell with no warning in it, and only after the 1-day ladder has shown its conversion rate.

**The reverse fold** (David's add): if the Extended only has 1-2 people and the 2-hr has more, ask the Extended guests to join the 2-hr with the $65 back as an $80 credit toward a future paddle (cash refund if they insist). The 7am post includes the paste-ready text when that's the shape of the day. Not automated: it's a Jeff decision.

**Private as a rung (David 10/13: "offer private for 1 or 2, keeps the guides guiding, but it needs to make financial sense").** Prices pulled from FareHarbor 10/13: private 2-hour $250 / $350 / $450 for 1 / 2 / 3 guests, then $120 pp; private Extended $400 / $700 / $900, then $240 pp. Guide cost: $100-125 a tour, $200 on an Extended. So the ask is list price first, then a softer private that still clears the guide with margin:

| Guests on the 2-hour | They paid | Private at list | Softer private (rung 2) | Guide cost |
|---|---|---|---|---|
| 1 | $65 | $250 (+$185) | $150 (+$85) | $100-125 |
| 2 | $130 | $350 (+$220) | $210 (+$80) | $100-125 |
| 3 | $195 | $450 (+$255) | $270 (+$75) | $100-125 |

Floors live in config (`private_floor_total`): $150 / $200 / $260. Below that we'd rather move them to another day. A 2-guest group that already meets the minimum with no Extended that day now gets a pure "have the swamp to yourselves" upsell ($350, then $210) since the tour runs either way.

Website note: the 2-hour page says "Private Tours available" with no price; the Extended page shows $400 + $300 per extra person, which matches FareHarbor for 2 guests but not 3 ($900 in FareHarbor). Worth one pass to align.

## 2. Kayak email drip (16 emails built, only em01 sending at 4,500/day)

Today the drip is one email, one CTA, one price. Ladder version, same list, same cadence:

| Rung | Email | Ask |
|---|---|---|
| 1 | em01 Beat the heat (sending now) | Book the Extended / half-day first. Lead with the 4-hour, not the 2-hour. |
| 2 | "Why repeat paddlers book the half-day" | Extended again, with the reason, plus the private option for groups |
| 3 | "Pick your day on the bayou" | Standard 2-hour at full price, specific dates with groups going (real urgency, not fake) |
| 4 | "Planning something with a crew?" | Private / group booking at full private rate |
| 5 | Last touch, 30+ days unopened | A perk, not a price cut: free photo pack, or a $20 credit that expires in 14 days |

Clicked but didn't book → skip ahead to the next rung in 3 days instead of waiting a week. Opened nothing in 5 sends → drop to one email a month.

## 3. Party boat win-back (SES, Tue sends, h02 10/27, h03 11/17)

David's standing call: experience-led, no discounts. The ladder respects that: the price never moves, the ask does.

| Rung | When | Ask |
|---|---|---|
| 1 | h02 Friendsgiving | Private boat for your group at full rate ($800 / $900 / $1,200). The whole-boat ask comes first because it's the biggest ticket. |
| 2 | h03 NYE + office parties | Private boat again (NYE sells itself), and public seats at $59 as the fallback inside the same email |
| 3 | January | Public seats, real dates, "these three Saturdays are the ones filling" |
| 4 | Feb, still no booking | A perk, not a discount: first round on us, or captain's photo pack, 14-day expiry |
| 5 | Never, per David | No percent-off. If we ever break this, it's a credit with an expiry, never a coupon code in the wild. |

Measure each rung by FareHarbor ref (npb-winback-hNN / wNN), same as today. The 0.37% click rate says the list is tired; a bigger first ask costs nothing extra to send.

## What happens next

| Step | Owner | By |
|---|---|---|
| OK the kayak wording, flip sends on | David | Wed 10/14 |
| Private price for the kayak rung | Jeff | Wed 10/14 |
| Drip + win-back rung copy drafted in the vault | Claude | Mon 10/19 |
| Rung order decided for h02 | Michael + David | Tue 10/20 sync |
