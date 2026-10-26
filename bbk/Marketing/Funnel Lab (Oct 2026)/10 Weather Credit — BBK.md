*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for BBK.*

# Weather Credit: BBK (full file 10, written for NKST, BBK, LSKT/AKT, NPB, HPB)

Board card c04 (04 card 4): pick = park / note = (none)

# Play 1: Weather credit instead of refund (two versions + a test we can run now)

*Drafted 2026-10-14 overnight by David's Claude. DRAFT. Nothing sent, nothing changed in FareHarbor, OpenCX or any site.*

Rank 1 on the Growth Plays Rollout. DCKT already has the full analysis and a 2027 policy draft (`Door County Kayak Tours/DCKT — 2026 Cancellation Analysis.md`, sections 7 and 9). This file is for the brands still in season right now: **NKST, BBK, LSKT/AKT, NPB, HPB.**

## Why it matters (DCKT numbers, verified in that analysis 2026-10-10)

- 553 cancels in 2026, about 91% of the cancelled money refunded or never collected.
- Only 12 of 529 cancelled guests rebooked within 45 days (2%). Today the refund path loses the customer, not just the sale.
- Planning number for DCKT alone: about $19k a season kept at midpoint credit redemption.

NKST's live FAQ says the opposite of what we want: "If we cancel due to weather, you get a full refund, no questions asked." Every swamp/bayou brand weather-cancels, so the same leak runs there.

---

## The decision, built both ways

### Version A: Credit by default (the DCKT model)
Weather cancel turns the payment into a credit automatically. Refund only on request, routed to a manager, or if the credit expires unused.

- Keeps the most money. Needs a policy change on every FareHarbor item and the website FAQ.
- Needs a legal read (Louisiana and Texas consumer rules, card-network refund rules) before it goes live. The DCKT draft keeps a refund fallback for exactly this reason.
- Risk: a few angry reviews from guests who expected cash. The fallback limits that.

### Version B: Guest chooses, credit is worth more (no policy change needed)
Weather cancel message offers two buttons: **full refund** or **a credit worth 120% of what you paid**, good 12 months, shareable.

- The current "full refund" promise stays true, so this can start **this week** without legal or FAQ edits.
- The extra 20% only costs us if the credit gets used, and it lands on seats that were empty anyway.
- Keeps less than A, because some guests still take the cash.

**My pick: run B now as a live test, decide A for 2027 with the results in hand.** B is the honest, low-risk way to learn the real credit-take rate before changing policy anywhere.

---

## The live test (Version B vs today)

| | Control (today) | Variant (B) |
|:-|:-|:-|
| Weather-cancel message | "We have to cancel, you'll get a full refund" | "Pick one: full refund, or a $[120%] credit good 12 months" |
| Who gets it | Bookings with an EVEN FareHarbor booking number | Bookings with an ODD booking number |
| Why that split | Free, random enough, no tooling, staff can apply it from the cancel screen |

**Measure (per brand, from FareHarbor):** credit-take rate (credits issued / weather cancels), credit redemption at 30/90/180 days, rebook rate within 45 days, refund dollars, and any 1-2 star reviews mentioning refunds.

**Sample reality:** NKST and BBK weather-cancel maybe 10 to 40 bookings in a bad week. This test needs roughly 60+ cancels per arm to read a 15-point difference in take rate, so it is a **season-long test**, read monthly. Pool NKST + BBK + LSKT to get there faster (same message, same split).

**Stop rule:** if variant B gets 2+ angry reviews about the credit offer in a month, pause and look.

---

## Copy (Version B, plain ASCII, paste-ready)

Placeholders in [BRACKETS]. Sign as the business, never a person. SMS only to guests with SMS on the booking.

**Weather-cancel text (variant arm)**
> [BRAND]: We have to cancel your [TOUR] on [DATE] at [TIME] for weather. Sorry, we know you planned around it. Pick one:
> 1) Full refund to your card: reply REFUND
> 2) A $[CREDIT] credit (that's 20% extra) good for 12 months, use it any day or give it to a friend: reply CREDIT
> 3) Move to a new date now: [rebook link]
> Reply STOP to opt out.

**Weather-cancel text (control arm, today's behavior written cleanly)**
> [BRAND]: We have to cancel your [TOUR] on [DATE] at [TIME] for weather. Sorry about that. You'll get a full refund to your card, or move to a new date here: [rebook link]. Reply STOP to opt out.

**Credit confirmation email**
> Subject: Your $[CREDIT] [BRAND] credit is ready
>
> Hi [FIRST NAME],
>
> Weather won on [DATE], so here's your credit: $[CREDIT], good through [EXPIRATION]. Code: [CODE].
>
> Use it on any tour, share it, or reply and we'll book it for you. [SEASON NOTE, e.g. "November mornings in the swamp are cool and quiet, the gators are still out on warm days."]
>
> If your plans change and you can't use it, reply before it expires and we'll refund what you originally paid.
>
> [BRAND]
> [PHONE] | [EMAIL]

Note the refund fallback is the original amount, not the 120%. Say so plainly so nobody feels tricked.

**NKST FAQ line (only if David picks Version A later; leave the FAQ alone for Version B)**
> If we cancel for weather, you choose: a new date, or a credit good for 12 months that you can share. If you can't use the credit before it expires, we refund it.

---

## Set-up steps (for whoever does it, after David says go)

1. FareHarbor: confirm with the rep how to issue a gift card / stored value card from a cancelled booking, and whether the amount can be 120% of the booking. If FH can't do over-value cards, issue the 120% as a promo code tied to the guest's email.
2. OpenCX weather macro: two versions (even/odd). Same for the dock team's text template.
3. Cancel note on every cancel: WEATHER, GUEST, STAFFING, NO-SHOW. DCKT logged a reason on only 44 of 553 cancels in 2026; we can't measure anything without this.
4. Monthly read: Claude pulls the FH cancelled-bookings report and the gift card report on the 1st and adds a row to the Experiment Board.

## Open questions for David

1. Version B test now, yes or no?
2. 120% or 115%? (120% is the cleaner pitch. 115% costs less. I'd start at 120% and only go lower if take rate is already high.)
3. Which brands first? My order: NKST, BBK, LSKT (most weather cancels), then NPB/HPB (boats cancel less).
4. Who sends the cancel texts at each brand today? The split only works if that person uses the right template.
