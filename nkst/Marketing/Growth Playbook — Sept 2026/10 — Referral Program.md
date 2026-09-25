# 10 — Referral Program

*Growth Playbook, September 2026. Facts come from [[00 — Fact Sheet & Open Questions]]. The shared SMS, email, sender and link rules are in [[04 — Abandoned Inquiry & Booking Follow-Up]] §0.*

**Status: DRAFT.** Nothing here is live. **Every dollar amount in this file needs David's sign-off** (Fact Sheet open question 3). Items marked **PROPOSED** are ideas, not decisions. **FLAG FOR DAVID** marks a decision only he can make.

**Builds on:** [[NKST — Customer Journey Map]] Stage 6 (Give $10 / Get $10), [[NKST — Affiliate & Partner Program]] (about 100 dormant GHL signups, the 5-day welcome cadence, the ghost-tour approach), [[Marketing/NKST — Lead Nurture Strategy]] (ghost tour → Insider Guide), [[NKST + NPB — Cross-Promo & Affiliate Campaign]] (operator-to-operator deals), [[Marketing/Chevy — Email Marketing & GHL Assessment]] (the planned Partner Flow and Welcome Back Flow), [[05 — Review Engine]] (F1 hand-off).

**Relationship to [[06 — Partner Kit (Commission-Ready)]]:** 06 is the trade term sheet (commission, tiers, net rates, payout terms, tracking rails, and the pitch per partner type). **Where this file and 06 disagree on partner terms, 06 wins.** This file adds what 06 doesn't cover: the guest track, the email sequences (past-guest launch and the partner welcome), fraud rules for both tracks, the individual partner card, and the combined dashboard.

**Two tracks, kept separate** (the Affiliate doc: "Both matter. Don't conflate them."):
- **Track 1 — Past guests.** They had a good day and tell a friend. The reward is tour credit.
- **Track 2 — Local partners.** Hotel staff, concierges, drivers, baristas, ghost-tour guides. The reward is cash commission.
- *Out of scope:* operator-to-operator reciprocal deals. They stay in the NKST + NPB Cross-Promo doc.

---

## 1. Program names (pick one per track)

| Track 1 — guests | Why | Track 2 — partners | Why |
|---|---|---|---|
| **Pass the Paddle** *(recommended)* | Active, local and easy to say out loud. "Pass" fits the idea of sharing. | **NKST Local Partners** *(recommended)* | Plain and professional, which concierges and hotel staff prefer. No gimmick to explain. |
| Bring a Paddler | Literal and clear | Swamp Scouts | Fun, good for drivers, baristas and guides. A bit informal for hotels. |
| Paddle It Forward | Warm, has a conservation feel | Front Desk Friends | Hotel-specific, so it leaves out drivers and guides |
| Swamp Friends | Friendly, a little generic | Bayou Insiders | **Avoid.** It collides with the "New Orleans Insider Guide" lead magnet. |

---

## 2. Track 1 — Past guests: mechanics

### The offer (FLAG FOR DAVID)
| Option | Friend gets | Referrer gets | Our cost per new booking | Note |
|---|---|---|---|---|
| A. Current spec (Journey Map) | $10 off | $10 credit | $20 | Simple, but $10 on a $130+ booking doesn't move many people |
| **B. PROPOSED (recommended)** | **$10 off** | **$15 credit** | **$25** | A slightly richer reward for the person doing the work. Still about 19% of a 2-guest $130 booking, and less for bigger parties. |
| C. PROPOSED alternative | **Free round-trip shuttle** (up to 2 guests, $50 value) | $15 credit | Up to $65 | Better for friends staying in the Quarter, because it removes the logistics objection. More expensive, so test it later rather than launching with it. |

**Recommendation: launch with B.** Test C against it in month 3 if the referral rate is under target (A/B idea in §12).

### Rules (these go in the terms, §2.4)
1. **Friend discount:** $10 off one booking of the Manchac, Extended, Honey Island or Combo tours. It doesn't apply to self-guided rentals or private tours. Private tours are an upsell, not a discount (Rate Card).
2. **The friend must be new:** no earlier NKST booking under that email or phone.
3. **Referrer credit:** $15 per referred **booking** (not per guest). It's issued **after the friend's tour is completed** (FH checked-in), not when they book. That protects against cancellations.
4. **Credit form:** a **single-use $15-off FareHarbor promo code**, not a FareHarbor gift card. Our gift cards are sold and marketed as "never expire" ([[11 — Gift Card Campaigns]]). Mixing free promotional credit into the same product would muddy that promise and the gift-card liability.
5. **Credit expiry:** 12 months from issue, stated on the credit. It's promotional credit, not a gift card that was paid for. **Confirm the Louisiana and federal rules on promotional credit expiry with the accountant or counsel.**
6. **Stacking:** a referrer can stack up to 3 credits on one booking. Referral codes and credits don't stack with any other promo, the 04 §2 offer, or a partner code.
7. **Cap:** 10 credits ($150) per referrer per calendar year. Past that, Ray sends a personal thank-you and David decides on anything extra.
8. **PROPOSED later option:** "Donate my $15 to cypress planting" once the Sankofa add-on exists (Fact Sheet open questions 4 and 7).

### How a guest gets a code
- **Preferred:** every past guest is **pre-assigned** a unique code at launch, and each new guest gets one at review-engine step F1 (Day 10). Format: `FIRSTNAME` + 3 digits, for example `MARIA482`. It's stored in GHL custom field `ref_code`.
- **Dependency:** ask Kevin Schmitt (FH) whether FareHarbor can **bulk-create** promo codes (from a CSV or through support). If it can't, fall back to a **pool of 300 pre-made codes** that Ray loads into a GHL-linked Google Sheet, with GHL assigning the next free one. If even that isn't possible, use a "Get my code" form and Ray creates codes by hand within 1 business day. That's fine at low volume.
- **Share link:** `{link:ref}/{{ref_code}}` (suggested path: `neworleanskayakswamptours.com/r/[code]`, which mirrors 06's `/p/[code]` partner redirects) goes to a simple landing page that shows the code and the booking button. **Ask Kevin** whether FH booking URLs can pre-fill a promo code. If they can, the link applies it automatically. If not, the page says "Enter {{ref_code}} at checkout."

### 2.4 Guest terms (short form, shown on the landing page)
> Pass the Paddle: your friend gets $10 off their first New Orleans Kayak Swamp Tours booking with your code. After they paddle, you get a $15 credit toward your next tour. It's for new guests only, on public tours, one discount per booking. Credits expire 12 months after they're issued. Limit 10 credits per year. We may cancel codes that are shared publicly or misused. Full terms: {link:ref_terms}

---

## 3. Track 2 — Local partners: mechanics

### Who
The about 100 dormant GHL affiliate signups (Uber drivers, hotel receptionists, baristas, lobby staff), plus new ones: hotel concierges and front desk, Airbnb superhosts, ride-share and pedicab drivers, and ghost-tour guides.

**David's rule (Affiliate doc):** build 5 real relationships before mass-mailing anyone. The welcome sequence (§8) is what keeps a relationship warm. It can't start one.

### Payout (FLAG FOR DAVID)
| Option | Per 2-guest $130 booking | Per 6-guest $390 booking | Pros | Cons |
|---|---|---|---|---|
| **A. 10% of the tour subtotal** *(recommended; also the Fact Sheet assumption)* | $13 | $39 | Grows with the booking. It's the industry-normal shape. | Partners have to trust our math. The monthly statement handles that. |
| B. Flat $5 per guest | $10 | $30 | Easiest to explain at a front desk | Doesn't reward Extended or Combo bookings |
| C. "$50–100 per day you send bookings" (the old Affiliate doc pitch) | $50–100 | $50–100 | Big headline | **Not recommended.** It pays 38–77% of a small booking, it's hard to track, and it invites gaming. Superseded. |

**What the subtotal means:** the tour price only. It excludes the shuttle add-on, taxes, FH booking fees and gratuities. It's paid only on **completed** tours, and a refund or chargeback reverses it.

**Tiers:** individuals (this file's audience) stay on flat 10%. The 10/12/15% volume ladder in 06 §2 is only for hotel desks and agents.

**Guest-side benefit on partner codes:** use 06 §2d. By default, partner codes carry $0 off and are for tracking only. If a partner asks, the code can be set to **5% off for the guest + 5% commission**, which costs NKST the same. (The hotel-code precedent is in the Cross-Promo doc.)

**Who gets paid:** if an employer bars personal referral fees, pay the property or the desk's staff fund instead (06 §2e).

**Activation bonus (PROPOSED):** $10 extra on a partner's **first** completed booking, paid within 7 days. The Affiliate doc says "word spreads in hospitality circles when you actually pay out." The fastest possible first payout is the best marketing this program has.

**Ghost-tour guides:** follow the Affiliate doc's approach. Lead with **reciprocity** ("we send people your way, you send people ours"). **No money needs to change hands.** The commission code is offered as an option, not the pitch.

**Hotel and venue staff:** the partner confirms that taking referral fees is allowed by their employer. This line is in the partner terms (§3.3). Some hotels ban it, and we don't want to cost anyone their job.

### 3.3 Partner terms (the plain-English summary on the signup form; the full term sheet is in 06)
- Commission: 10% of the tour subtotal on completed tours booked with your code or link. *(Amount to be confirmed by David.)*
- Paid monthly by the 15th for the prior month's completed tours (§6, which matches 06 §4). A W-9 is required before the first payout.
- Tell guests you're a partner. For example: "I get a small thank-you if you book." FTC endorsement rules require this disclosure.
- Describe the tour honestly: silent kayaks, not airboats; alligators common, not guaranteed; minimum age 8.
- No paid search ads on our brand name, no coupon or deal sites, no spam, no posting your code in public reviews.
- Don't review NKST on Google or TripAdvisor while you're a paid partner. It's a conflict of interest under those platforms' rules.
- You're responsible for following your employer's rules on referral fees.
- Either side can end the partnership at any time. Commission already earned on completed tours still gets paid.

---

## 4. Tracking

| What | Guest track | Partner track |
|---|---|---|
| **Attribution (the source of truth)** | FH promo code on the booking | Per 06 §3: the FH affiliate or agent stamp, the tracked FH link (`ref=` / `asn=`), or the partner promo code. **06 found that FareHarbor's affiliate rails are already running for NKST**, so use them. Code naming follows 06: `IND-DEREK`, `HTL-[PROPERTY]`, `CON-[NAME]`. |
| Secondary | GHL trigger-link click (branded link) | The UTM on the QR code through the `/p/[code]` vanity redirect (06) |
| Contact record | GHL tags `ref-guest`, field `ref_code`, `ref_credits_issued`, `ref_credits_redeemed` | GHL tag `partner`, `partner-type-{hotel/driver/barista/ghost/host}`, fields `partner_code`, `payout_method`, `w9_received`, `first_booking_date`, `partner_status` |
| Why not the GHL Affiliate Manager alone | GHL's Affiliate Manager tracks sales through GHL checkouts. Bookings happen in FareHarbor, so it can't see them. **Use GHL for contact records, email and the partner portal link. Use FareHarbor promo-code reports for the money.** | Same |
| Insider Guide signups from a partner link | — | **PROPOSED:** stamp the contact with `ref_partner_code` and add that code to every booking link in their Lead Nurture emails. If they book with the code within 120 days, the partner gets paid. |
| Monthly reconciliation | Ray exports the FH promo-code usage report → the ledger sheet (§11) | Same, plus a commission calculation and statement |

---

## 5. Fraud and abuse rules

| Rule | How it's enforced |
|---|---|
| No self-referral | Friend's name, email, phone, card last-4 or billing address matching the referrer's means no credit. Ray checks the FH booking before issuing. |
| New guests only | Friend's email or phone is already in FH booking history, or already in GHL as `booked`, means no discount (void at check-in or refund the difference) and no credit |
| Paid on completed tours only | Credit or commission is issued only after check-in. No-shows, cancellations, refunds and chargebacks reverse it. |
| Public code posting | A guest code found on coupon or deal sites or in public social posts is deactivated and a new one issued, with a polite note. Partner codes: a first warning, then removal. |
| Brand bidding | Partners may not bid on "New Orleans Kayak Swamp Tours" or close variants in paid search. Violation means removal and forfeiture of unpaid commission. |
| Stacking | One discount per booking. FH settings enforce it where possible, plus Ray's review. |
| Volume anomaly | More than 5 referred bookings from one guest code in 30 days, or a partner's bookings spiking more than 3× their average, goes to manual review before payout |
| Same-party split bookings | One group splitting into several bookings to trigger several credits counts as one referral |
| Staff and guides | NKST guides and staff aren't eligible for either track. There may be a separate internal incentive later. |
| Misrepresentation | A partner telling guests alligators are "guaranteed," or calling it an airboat, gets one warning, then removal |
| Reviews | Referral and partner rewards **never** depend on a review (see 05 §2). The printed cards don't mention reviews at all. |

---

## 6. Payout cadence

| | Guests | Partners |
|---|---|---|
| **When it's earned** | Friend's tour completed | Guest's tour completed |
| **Issued** | Weekly. Every Monday, Ray issues the credits for the prior week's completed referred tours. | Monthly, by the **15th**, for the prior month's completed tours (06 §4) |
| **First payout** | Same weekly batch | **Fast-tracked within 7 days** of the first completed booking (plus the PROPOSED $10 activation bonus). This is an exception to 06's monthly cycle, and David needs to approve it. |
| **Minimum** | None | $25, per 06. Smaller balances roll over, and they're paid out at least once a year or when the partner leaves. |
| **Method** | Single-use FH promo code by email (and SMS if consented) | ACH or PayPal preferred, or a check on request (06 §4) |
| **Paperwork** | None | A W-9 before the first payout. Ray tracks the annual total per partner. **The accountant confirms the 1099-NEC threshold for 2026 and files.** |
| **Statement** | "Your friend paddled. Here's your $15." email | A monthly statement email: bookings, guests, subtotal, commission, paid date |
| **Who approves** | Ray (automatic within the rules) | Ray prepares, **David approves** before payment |

---

## 7. Launch campaign — past guests

### Audience and consent
- **Email:** past guests in FareHarbor with an email, most recent first. Before sending, remove everyone on `suppressed_emails_ghl_dnd.csv` (vault root), anyone who's unsubscribed, and bounces. The Lead Nurture deliverability rules apply: separate marketing subdomain, DKIM and DMARC on, and warm up the list, **500 a day, newest guests first**. Guests from before 2024 go last, and only if bounces stay under 2%.
- **SMS:** only past guests who booked **after Section 12 (SMS consent) of the privacy policy went live**, and only those in the last 18 months who haven't opted out. **Open item:** confirm when Section 12 went live. A promotional text to someone who never consented is the fastest way to lose the 10DLC campaign.
- **Sequencing with Chevy's Welcome Back flow:** if that flow is live, the referral launch goes out **after** Welcome Back email 1, so a past guest's first email in a while isn't a pitch.
- Every past guest gets a pre-assigned `ref_code` before G1 sends (§2).

### G1 — email: launch (also used as Review Engine step F1)
**Subject:** Know someone who'd love the swamp?
**Preview:** Give them $10 off. You get $15 toward your next tour.

> Hi {{first_name}},
>
> Thanks again for paddling with us. The best way people find us has always been a guest telling a friend, so we've made it official. It's called **Pass the Paddle**.
>
> **Your code: {{ref_code}}**
>
> - **Your friend gets $10 off** their first tour with us.
> - **You get a $15 credit** toward your next one once they've paddled.
>
> Share this link and the code comes with it: **{link:ref}/{{ref_code}}**
>
> Who's it good for? The friend who's headed to New Orleans and asked what to do besides Bourbon Street. The family with kids 8 and up. The person who'd like to see an alligator from a kayak rather than from a loud boat. They're common at Manchac from spring through fall, not guaranteed.
>
> Thanks for spreading the word.
>
> Ray
> New Orleans Kayak Swamp Tours · (504) 571-9975
>
> *New guests only, public tours. Credits expire after 12 months. Terms: {link:ref_terms}*

### G-S1 — SMS: launch (SMS-consented only; sent 2 days after G1, to anyone who hasn't clicked)
```text
Hi {{first_name}}, Ray at New Orleans Kayak Swamp Tours. Give a friend $10 off with code {{ref_code}}, get $15 toward your next tour. Reply STOP to opt out.
```
*(~155 chars)*

### G2 — email: reminder (Day 7 after G1, non-clickers only)
**Subject:** Your code, in case you need it: {{ref_code}}
**Preview:** Fall is the best season in the swamp, if anyone you know is planning a trip.

> Hi {{first_name}},
>
> Quick one. If anyone you know is headed to New Orleans this fall, it's the best season in the swamp: mild weather, active wildlife, and fewer bugs. It does book up.
>
> Your code **{{ref_code}}** gives them $10 off, and you get $15 when they paddle.
>
> **{link:ref}/{{ref_code}}**
>
> Ray

*(Change the season line for other launch months: winter "migratory birds, quiet water"; spring "gators waking up, common, not guaranteed"; summer "book the 9 AM, it's cooler.")*

### G3 — transactional: credit earned (email, plus SMS if consented)
**Subject:** {{friend_first_name}} paddled. Here's your $15.
> Hi {{first_name}}, your friend {{friend_first_name}} came out with us. Thanks for sending them. Your $15 credit: **{{credit_code}}**, good through {{credit_expiry}}. Book your next tour: {link:book_manchac}. — Ray

```text
{{first_name}}, your friend paddled with us. Thanks. Your $15 credit: {{credit_code}}, good through {{credit_expiry}}. - Ray
```
*(~125 chars)*

*(Privacy: use the friend's first name only if they checked "let my friend know I booked" on the landing page. Otherwise say "someone you referred.")*

---

## 8. Partner welcome sequence (the Affiliate doc's 5-day cadence)

**Trigger:** a partner signup form is submitted and Ray approves it (tag `partner-approved`). The partner code is created in FH before Day 1 sends.
**Reactivation of the ~100 dormant signups:** first send them **P0** (below). Anyone who clicks "I'm in" goes to Day 1. Non-responders get one more P0 after 7 days, then stay dormant.
**Channel:** email. **Partners don't get marketing SMS.** The A2P campaign lists recipients as guests and prospects, with "Affiliate Marketing: No." Texts to partners stay 1:1 (Ray replying). Confirm with Mo at OpenCX before any partner SMS automation.
**After Day 5:** weekly keep-warm until the first booking, then **monthly** (Affiliate doc).

### P0 — reactivation (dormant signups only)
**Subject:** You signed up to send people our way. Here's the easy version.
**Preview:** Your own code, 10% on every booking, paid monthly.
> Hi {{first_name}},
>
> A while back you told us you'd like to send guests our way. Sorry it took us a while to get this properly set up. It's ready now:
>
> - **Your own code.** Guests enter it when they book.
> - **10% of the tour price** on every completed booking, paid monthly. *(Amount to be confirmed.)*
> - **Printed cards** with your code on them, if you'd like some.
>
> **Still in?** {link:partner_confirm}. It takes one minute (payout method and a W-9).
>
> Ray
> New Orleans Kayak Swamp Tours · (504) 571-9975

### Day 1 — Welcome: your code and what you get
**Subject:** Welcome to NKST Local Partners, {{first_name}}
**Preview:** Your code is {{partner_code}}. Here's how it works.
> Hi {{first_name}},
>
> Welcome aboard. Here's everything in one place:
>
> - **Your code:** {{partner_code}}
> - **Your link:** {link:partner}/{{partner_code}}. Guests who book through it get the code applied.
> - **You earn:** 10% of the tour price on every completed booking. *(Amount to be confirmed.)*
> - **You're paid:** monthly by the 15th. Your first one is fast-tracked within a week.
> - **Cards:** reply with a mailing address, or pick them up at 740 N Rampart St, and I'll get you a stack with your code printed on them.
>
> Tomorrow I'll send you a 20-second way to mention us that doesn't feel like a sales pitch.
>
> Ray

### Day 2 — What to say
**Subject:** What to say (20 seconds, no pitch)
**Preview:** The line our best partners use when a guest asks, "What should we do?"
> Hi {{first_name}},
>
> The best referrals happen when a guest asks you, "What should we do tomorrow?" Here's the line:
>
> > "If you want to get out of the city, there's a kayak swamp tour about 35 minutes out. Silent kayaks, not airboats, small groups, and a guide who knows the swamp. The van picks up on Rampart. Use my code and you'll save a little."
>
> **Adjust it for where you are:**
> - **Front desk / concierge:** "Most guests who do it say it was the best thing they did outside the Quarter."
> - **Barista / bartender:** keep it short. Hand them a card.
> - **Driver:** mention it if they ask for recommendations. Don't bring it up with every rider.
> - **Ghost-tour guide:** end-of-tour line: "If you're doing something on the water tomorrow, these are the people."
>
> And say you're a partner ("I get a small thank-you if you book"). It's required, and honestly it builds trust.
>
> Ray

### Day 3 — Social proof: what guests experience
**Subject:** What your guests are signing up for
**Preview:** 4.9 stars on Google, 12 guests max, and guides people mention by name.
> Hi {{first_name}},
>
> So you know what you're recommending:
>
> - **4.9 stars on Google** from {{review_count}} reviews. Guests mention their guides by name all the time.
> - A TripAdvisor **Travelers' Choice** award.
> - **12 guests max**, silent kayaks, and trained naturalist guides, since 2013.
> - The **Manchac swamp**, the second-largest bald cypress swamp in the U.S.
>
> Here are three guest photos you can share or show people: {link:partner_photos}
>
> Ray

### Day 4 — FAQ: what guests will ask you
**Subject:** The 6 questions guests will ask you
**Preview:** Price, age, gators, rain, getting there, experience. Short answers.
> Hi {{first_name}},
>
> Keep these handy:
>
> 1. **How much?** Manchac Swamp Tour from $65/person (2 hrs). Extended is $130 (4 hrs). Shuttle +$25/person.
> 2. **How do we get there?** A round-trip shuttle from 740 N Rampart St that leaves 1 hr 15 min before tour time, or drive about 35 minutes to the launch. **No Uber**, because there's no ride back.
> 3. **Kids?** Ages 8 and up. Under 16 paddles tandem with an adult.
> 4. **Will we see alligators?** Common at Manchac from spring through fall, not guaranteed. Please say it this way.
> 5. **What if it rains?** They paddle in light rain and only cancel for lightning or severe weather, with a full refund when they cancel.
> 6. **Never kayaked?** Most guests haven't. Flat water, no current.
>
> Times: 9:00 AM, 11:30 AM, 2:00 PM and 4:30 PM. Groups over 12: private tours. Have them call (504) 571-9975.
>
> Ray

### Day 5 — Reminder and motivation
**Subject:** One this week
**Preview:** One referral this week is all it takes to start.
> Hi {{first_name}},
>
> That's the whole setup. One referral this week is all it takes to get going, and your first payout comes within a week of their tour.
>
> Your code again: **{{partner_code}}** · {link:partner}/{{partner_code}}
>
> If there's anything that would make this easier for you (more cards, a table tent for the desk, a different way to get paid), reply and tell me.
>
> Ray

### Weekly keep-warm (until the first booking) — rotate these topics
- "This week on the water": one guest or guide photo and a sentence. (Pull from 05 §8 uploads, with the guest's release.)
- Availability heads-up: "Saturday mornings are full through October. Point guests to weekdays or the 2:00 PM."
- Seasonal: fall best, winter birds, spring gators, summer 9 AM.
- Partner spotlight (with permission): "Jamie at [hotel] sent 6 guests last month."

### Monthly (after the first booking)
The monthly statement (§6) plus one line of news. Nothing more.

---

## 9. Printable card and QR copy

**Specs:** business card, 3.5 × 2 in, matte, with a QR code of at least 0.8 in. **The QR encodes a branded URL** on an owned domain, with a UTM and the code. Guest cards use `/r/[code]` (for example `/r/MARIA482?utm_source=card&utm_medium=print&utm_campaign=pass-the-paddle`), and partner cards use 06's `/p/[code]` redirect. Test-scan every print proof. No public shorteners (04 §0.2).

### Guest card — "Pass the Paddle" (guides hand one to each party at drop-off; no review mention)
**Front**
> **Pass the Paddle**
> Know someone headed to New Orleans?
> **They get $10 off. You get $15.**
> [QR]

**Back**
> Your code: ______________ *(the guide writes it in, or a sticker with the code)*
> *(Phase 1 fallback: print the generic line "Get your code: scan the QR" and the landing page issues the code.)*
>
> New Orleans Kayak Swamp Tours · Silent kayaks, not airboats · Since 2013
> neworleanskayakswamptours.com · (504) 571-9975
> *New guests, public tours. Terms at the link.*

### Partner card (printed with the partner's code; handed to guests)
**Front**
> **Get out on the swamp.**
> Small-group kayak tours, 35 min from the French Quarter.
> Silent kayaks, not airboats. 12 guests max.
> [QR]

**Back**
> Recommended by **{{partner_first_name}}** · Code **{{partner_code}}**
> *(Only if the partner chose the 06 §2d split: "Save 5% with this code.")*
> *{{partner_first_name}} may earn a referral fee from this recommendation.*
> Shuttle from 740 N Rampart St, or meet us at the launch.
> Ages 8+ · No experience needed · Alligators common spring–fall, not guaranteed
> neworleanskayakswamptours.com · (504) 571-9975

### Front-desk table tent (concierge / hotel, 4 × 6 in)
> **Where locals send guests who want to see the swamp.**
> Small-group kayak tours in the Manchac swamp. Trained naturalist guides. 4.9 on Google.
> Scan to book · Ask the desk for a card
> [QR with the partner's code]

*(Keep "4.9 on Google" and leave the count off printed pieces, since the count changes weekly.)*

---

## 10. KPIs

| Metric | Target (first 6 months) |
|---|---|
| Guest codes issued (past guests + new) | 100% of eligible guests |
| Guest share rate (landing page visits ÷ codes issued) | 10% |
| Referred bookings per month (guest track) | 20 by month 3, 40 by month 6 |
| Active partners (≥ 1 completed booking in the last 90 days) | 10 by month 3, 25 by month 6 |
| Dormant signups reactivated (clicked "I'm in") | 25% of about 100 |
| Days from partner approval to first booking | median under 21 days |
| Partner payouts on time (by the 15th) | 100% |
| Cost per referred booking (credits + commission ÷ referred bookings) | under $30 |
| Referred share of all direct bookings | 5% by month 6 |
| Fraud flags / reversals | tracked and under 3% of referred bookings |

---

## 11. Dashboard spec

**Phase 1: a Google Sheet** ("NKST Referral Ledger"), updated weekly by Ray. **Phase 2:** Looker Studio on top of the same sheet once there's enough volume.

### Data sources
| Source | Pull | How often |
|---|---|---|
| FareHarbor promo-code usage / booking export | Booking ID, date booked, tour date, item, guests, subtotal, promo code, status (checked-in / cancelled / refunded) | Weekly (Monday) |
| GHL contacts | `ref_code`, `partner_code`, tags, `partner_status`, `w9_received`, `payout_method`, link clicks | Weekly |
| Payout log (manual) | Date paid, amount, method, reference | Every time a payout happens |

### Tabs and fields
1. **Bookings:** one row per FH booking that used a referral or partner code. Fields: booking_id, code, track (guest/partner), owner (referrer or partner), tour_date, guests, subtotal, status, credit_or_commission_due, eligible (Y/N after fraud checks), paid (Y/N), paid_date.
2. **Guests (referrers):** ref_code, name, codes_shared (clicks), referred_bookings, credits_issued, credits_redeemed, credits_expired.
3. **Partners:** partner_code, name, type, status (active/dormant/removed), approval_date, first_booking_date, bookings_30/90/365, guests, subtotal, commission_owed, commission_paid, w9, method.
4. **Payouts:** the ledger. Ties every payment to booking IDs.
5. **Summary:** the KPIs from §10, a monthly trend, the top 10 partners, the top 10 guest referrers, and cost per referred booking. Also a **dormant partners list** (no booking in 60 days), which is Ray's reach-out list.
6. **Flags:** rows that failed the §5 fraud rules, with the reason.

### Views people use
- **David (monthly):** the Summary tab, plus the payouts to approve.
- **Ray (weekly):** credits to issue, flags to review, dormant partners to contact.
- **Partners (monthly):** their own statement, generated from the Partners tab (a PDF or email body). They never see the sheet.

---

## 12. A/B ideas

1. Offer B ($10/$15) vs. offer C (free shuttle / $15) for new-guest F1 sends, starting month 3.
2. G1 subject: "Know someone who'd love the swamp?" vs. "Your $15 is waiting on a friend."
3. The guest card handed at drop-off vs. no card (measure code redemptions by tour date cohort).
4. Partner code with the 06 §2d split (5% off / 5% commission) vs. a tracking-only code, to measure the attribution rate. Only with partners who agree to it.
5. Partner Day 2 script: the generic version vs. the partner-type version.

---

## 13. Contradictions found and what this file supersedes

| # | Where | What it says | What this file does |
|---|---|---|---|
| 1 | Journey Map Stage 6 and Fact Sheet: "Give $10 / Get $10" | vs. this file's recommendation | **Proposes** $10 off / $15 credit (option B). $10/$10 stays the fallback. **FLAG FOR DAVID.** |
| 2 | Affiliate doc Priority 3 pitch: "$50-100 per day you send us bookings, **or** 10% per customer" | Per-day pay costs 38–77% of a small booking and is hard to track | **Supersedes** the per-day option. Recommends 10% of the tour subtotal on completed tours. **FLAG FOR DAVID.** Also: the old pitch says "per customer," so the wording is updated to "per booking" and "guests." |
| 3 | Affiliate doc Priority 1: ghost-tour guides, "No money needs to change hands" | vs. the brief listing ghost-tour guides as commission partners | **Reconciled.** Lead with reciprocity as the Affiliate doc says. Commission is available but not the pitch. |
| 4 | A2P campaign: "Affiliate Marketing: No"; recipients described as guests and prospects | Partner SMS automation would be a different audience | Partners get **email only**. SMS is limited to 1:1 replies. Confirm with Mo before automating any partner SMS. |
| 5 | Journey Map Stage 6: referral email at D+30 | vs. Review Engine timing | Moved to **D+10** (05 F1), while the tour is still fresh |
| 6 | Journey Map Stage 5 and Affiliate doc Priority 4: guide asks for a review and a referral in one breath ("tell one person… and leave us a Google review") | Mixing the referral reward with the review ask risks looking like a review incentive | The guide's verbal script (05 §4) has no reward in it. The referral card is handed out separately, and it never mentions reviews. |
| 7 | Chevy assessment: a "Partner Flow: partner subscriber → welcome sequence" is planned | May already be half-built in GHL | **Check with Chevy** before building §8, and reuse the workflow shell if it exists. |
| 8 | Journey Map implies referral credit, and 11 markets gift cards as "never expire" | Issuing 12-month promotional credit as a gift card would conflict with that | Referral credits are single-use promo codes, never FH gift cards. |
| 9 | Lead Nurture: ghost-tour referrals go to the Insider Guide form, with no attribution | The partner gets no credit if the guest books later | **PROPOSED** `ref_partner_code` carry-through (§4). |
| 10 | 06 cards and desk materials print "1,400+ reviews" | The count was 1,401 on Sep 2 and falling. One more removal makes "1,400+" false. | This file's printed pieces say "4.9 on Google" with no count. Recommend 06 does the same. |

---

## 14. Build checklist

- [ ] **David decides:** guest offer (A/B/C), partner payout (10% / flat), whether to offer the 06 §2d 5%/5% split, the activation bonus, program names
- [ ] Kevin Schmitt (FH): bulk promo-code creation? Promo-code pre-fill in URLs? ASN/affiliate tracking on our plan? Gift-card items?
- [ ] Chevy: is the Partner Flow or Welcome Back Flow already built in GHL?
- [ ] Mo (OpenCX): confirm partner comms stay off the NKST 10DLC campaign, or register them
- [ ] Accountant: 1099 threshold for 2026 and promotional-credit expiry rules
- [ ] Build the GHL fields and tags (§4), the landing pages (`ref`, `ref_terms`, `partner`, `partner_confirm`, `partner_photos`) and the signup form with terms acceptance, W-9 upload and payout method
- [ ] Pre-assign `ref_code` to past guests. Warm up the email list (§7).
- [ ] Build workflows: G1/G-S1/G2/G3 (guest), P0 + Day 1–5 + weekly + monthly (partner)
- [ ] Build the ledger sheet (§11)
- [ ] Print proofs: guest card, partner card, table tent. Test-scan every QR.
- [ ] Launch order: (1) 5 hand-picked partners (David's rule), (2) new-guest F1 via the Review Engine, (3) the past-guest email launch in warm-up batches, (4) the dormant-affiliate reactivation (P0)
