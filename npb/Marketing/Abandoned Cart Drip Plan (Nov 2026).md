---
created: 2026-10-31
owner: David (Claude)
status: PLAN, nothing new live
builds-on: "[[Abandoned Cart - GHL Sequence Plan]]" (Michael, 2026-09-22)
---

# Abandoned Cart Drip Plan (Nov 2026)

## Where it stands (verified live 2026-10-31)

| Piece | State |
|---|---|
| FareHarbor native abandoned cart email | **ON** (Settings > Advanced, "Enable abandoned cart emails" checked). One email, 2h after drop-off, only if they typed their email in checkout and the date is 8h+ away. Can't edit, can't add steps. Michael's 9/22 FH Support request is what got it turned on. |
| Size of the leak (GA4, last 30 days) | 1,728 people opened the booking form, 411 added to cart, 280 bought. Roughly **130 cart abandoners a month**, plus ~1,300 who opened the form and left earlier. |
| Can we get abandoners' emails out of FareHarbor? | **No.** No API, no report, no Mailchimp event (FH docs: "Event-based automation for abandoned bookings ... not currently available"). The checkout is FareHarbor's iframe, our site never sees what they type. |
| Lead capture on nolapartybarges.com | **None.** Lead engine script is not on the site; 1 NPB lead in the engine DB. |
| "Booked" signal (to stop a drip) | Exists: review-sms poller on mbp-2 stores every booking's email/phone (db updated today). The FH webhook beside it has logged nothing since 2026-10-21; the poller is covering. |
| Meta pixel on checkout | Purchase fires (402 in Oct). InitiateCheckout only 132, so it under-fires; use `fareharbor-click` + InitiateCheckout for audiences. |

## Why nothing more ships tomorrow

1. The people who abandon in FareHarbor's checkout can only be emailed by FareHarbor, and that email is already going.
2. A real drip needs their email **before** they open checkout. That capture doesn't exist on the site yet.
3. The engine that would send it (`~/Projects/fh-lead-engine*`) is one shared Lambda for six brands, with three diverging copies and uncommitted giveaway work on `capture-v2`. Deploying a rushed change from any copy can wipe another's. Not bombproof by Sunday.

## The plan, three layers

### Layer 1: FareHarbor's email (live)
- Weekly check: Dashboard report, add **Online Booking Reference** column, filter `abndcrt`. That count = bookings it recovered. If it's zero for 2 weeks, ask FH Support whether the online cart is actually on for NPB's flows.

> **CURRENT STATUS (verified 2026-11-03): Layer 2 PAUSED by David same day ($4 spent, 284 impressions).** Was: David OK'd 11/3. Campaign `NPB | Purchase | Cart Abandoners | Nov 2026` (52589049238900), $8/day, ad set 52589049256100, audience 52589048966100 = PageView on boat/booking pages (freaky-tiki, twerkin-tiki, cajun-queen, bentley-bayou-cruiser, pedal-bike-barge-cruise, boat-rental, our-boats) in 14d, minus Purchase 30d. Ads reuse 3 already-live creatives: Still Thinking (9.5x ROAS over 90d in old RT campaign), Weather Kill, Planner's Win. Review date: 2026-11-24; kill if under account ROAS.
> **Correction:** the pixel has NO InitiateCheckout or fareharbor-click on nolapartybarges.com (last 28d those fired only on admirenola.com). The Oct "132 InitiateCheckout" was Admire NOLA, not NPB. Fix = add the FH click/checkout event script to the NPB site, then switch the audience to true checkout starters.

### Layer 2: Retargeting ads, the "drip" for everyone who left (can start Nov 1 with David's OK on spend)
Reaches all abandoners, no email needed. One Meta ad set, one campaign, account act_87863118.
- **Audience:** website visitors with `fareharbor-click` or `InitiateCheckout` in last 30 days, **excluding** Purchase in last 30 days.
- **Budget:** $8/day to start. Small audience, so frequency cap matters more than spend.
- **Sequence by recency** (3 ads, Meta rotates them):
  - "Your date's still open" style, real weekend availability, private boats first.
  - Proof: a real review + crew photo from the new marina.
  - Group angle: "Book it, everybody Venmos you."
- **Google:** GA4 audience `add_to_cart` without `purchase` (14 days) into the existing PMax/Display as an audience signal. No new budget.
- Success line: abandoner-audience ROAS above the account average after 3 weeks, else kill it.

### Layer 3: Our own email drip (build week of Nov 3, launch target Nov 10)
Only possible for people whose email we have before checkout.
- **Capture points** (in order of value):
  1. **Private-boat quote requests** via Nolan/OpenCX. Highest ticket ($800 to $1,200). These are the real "dropped carts." Turn on Update Contact for Messenger/IG so the email is saved (open item on the board since 10/22).
  2. **"Hold my date" box** next to Book Now on private-boat pages: date, group size, email (phone optional, SMS later). Michael's option A.
  3. Lead engine popup on the WordPress site (already built, needs the header script).
- **Trigger:** captured with a date in mind, no booking in the review-sms booking db within 3 hours.
- **Sequence** (email only; SMS waits on the toll-free verification refile):

| # | When | Subject angle | Job |
|---|---|---|---|
| 1 | +3h (after FH's 2h email) | "Still eyeing [date]?" | Their boat + their date, live availability, one button to that item's calendar with `ref=cart-drip` |
| 2 | +24h | "Send this to the group chat" | Kills "I have to check with everyone": shareable link, price per person, BYOB answer |
| 3 | +72h | "[Date] is filling up" | Only if their date is real and still open; skip otherwise. Reply-to-hold offer |
| 4 | +7d | "Different weekend?" | Next 3 open weekends; then they roll into the regular newsletter |

- **Hard rules:** stop on booking (any brand booking under that email), stop on any reply (hand to a human), stop on unsubscribe (hosted link, one-click header, no mailto), never send for a date already past or under 24h away, max one marketing email per day per person across all NPB flows, 9am to 8pm Central only, 10% holdout so we can see if it actually lifts bookings.
- **No discount codes.** Website Standards say no codes yet. If David wants one later, it goes in email 3 only.
- **Sender:** info@nolapartybarges.com, signed "the NOLA Party Barge crew." SES us-west-2 (production). Michael's plan lists SES as pending; that's out of date, us-west-2 has production access.

## Decisions for David
1. **Pick the engine:** our SES lead engine (built, booking signal exists) or Michael's GHL route (needs GHL SMTP, webhook premium, Rawgrowth). Recommend the lead engine; one system, one unsubscribe list.
2. **Approve Layer 2 spend:** $8/day Meta retargeting starting Nov 1.
3. Who builds the "Hold my date" box on WordPress (Michael's wp-admin lane) vs waiting for the new site.

## Build checklist (Layer 3)
- [ ] Merge the three engine copies into one branch before touching the drip (coordinate with the giveaway work on capture-v2)
- [ ] Booking sync: nightly push of emails from mbp-2 `review-sms.db` to engine `/booked`
- [ ] Find out why the FH webhook went quiet after 2026-10-21
- [ ] Drip flow + 4 templates, tests for every stop rule
- [ ] Seed test with `success+x@simulator.amazonses.com`, then one real test to David
- [ ] Capture point 1 (Nolan save-lead) live, then 2, then 3
