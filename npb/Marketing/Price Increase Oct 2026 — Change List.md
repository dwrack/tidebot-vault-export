# Price Increase, Oct 2026: Change List

Decided by David on 2026-10-22: "push public seats up to $65 and privates $100 and then we can do discounts easily." The goal is a higher list price so codes and discounts (the $50 popup code, CREW50-<MON>) land as real savings.

**Status: amounts and start date approved by David 2026-10-22; start Mon 2026-11-02. Nothing has changed in FareHarbor yet.** The current prices below were read live from the FareHarbor API on 2026-10-22 (rides on Sun 10/25).

## 1. FareHarbor prices (David or Michael, in the FH dashboard; the API can't write prices)

| Item (pk) | Now | New | Change |
|---|---|---|---|
| Seat, all four boats (Freaky Tiki, Twerkin' Tiki, Bayou Boogie, Party Queen) | $59 | **$65** | +$6 (10%) |
| Twerkin' Tiki 6 PM seat | $63 (as of 2026-10-13, not re-checked today) | **$69** | +$6, confirmed by David 2026-10-22 |
| The Bayou Boogie private (116007) | $800 | **$900** | +$100 (12.5%) |
| The Party Queen private (289593) | $900 | **$1,000** | +$100 (11%) |
| The Freaky Tiki private (340933) | $1,200 | **$1,300** | +$100 (8%) |
| The Twerkin' Tiki private (488558) | $1,200 | **$1,300** | +$100 (8%) |
| Luxury Pontoon, up to 6 (294180) | $350 | **$450** | +$100 (29%), confirmed by David 2026-10-22 |
| Private Shuttle add-on | $400 | $400 | not a boat, unchanged unless David says |
| EcoTour, Seafood Boil, Jingle on the Bayou | unchanged | | not part of this decision |

Set the new prices on all future dates, and leave booked trips alone. Change the seats and privates on the same day so the per-person math stays consistent.

## 2. Discounts to set up in the same session (FH > Settings > Campaigns)

- `CREW50-NOV` (expires 11/30) and `CREW50-DEC` (expires 12/31): $50 off the total, private boats only. Test that it comes off the total, not the deposit.
- A seat discount, so "discounts easily" works on seats too. Suggestion: a $6-per-seat code that brings a seat back to $59 for leads and past guests. Name and dates are David's call.
- FTC rule (16 CFR 233): only advertise "save $X" from a price people actually pay. So the new list price has to be live and actually charged before any "was $65" or "save" copy runs. Don't run a permanent site-wide code.

## 3. What has to change the same day the prices change

| Where | What | Who |
|---|---|---|
| Nolan (OpenCX) pricing instruction | Already stale ("only $63", $900/$1,100/$1,250 as of 2026-10-13). Rewrite with the new prices | Claude drafts, David publishes |
| Meta ads that mention $59 | See `Meta Ads - Price Fix Sheet (Oct 2026).md` | David approves any edits that affect spend |
| `FB Daily Queue.csv` | 2 rows say $59. Edit them before they're scheduled | Claude |
| Staged blog post `2026-10-13 - what-to-wear-new-orleans-party-boat.md` | Mentions $59 | Claude |
| `NPB Unboxing — Post-Booking Sequence (Oct 2026).md`, `LinkedIn Corporate Outreach/Playbook.md`, Corporate Holiday Deck | Quote current prices | Claude |
| New site brief (`~/Projects/npb-site`) | The cost splitter, the hero "from $41 a person" and the Party Queen math get recalculated from FH at build | Already written into the brief |
| Funnel Lab + Lead Funnels docs (cost splitter table in 05) | Internal planning docs. Update when they're next used | Claude |
| Google Things to Do / Reserve with Google | Comes from FareHarbor, nothing to do | n/a |

Other files with $59 are dated reports and readouts (history). Leave them alone.

## 4. Still open

1. Seat discount code: amount and name (suggestion: $6 off a seat, back to $59, for leads and past guests).
2. Who sets the prices in FareHarbor, and when. Do it the weekend of 10/31 so Mon 11/2 is clean, and before CREW50-NOV goes out.
