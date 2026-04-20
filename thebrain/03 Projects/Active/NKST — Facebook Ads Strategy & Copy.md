# NKST — Facebook Ads Strategy & Copy

**Last updated:** April 6, 2026
**Account:** Gravity Trails / Admire NOLA (act_87863118)
**Status:** Planning phase — ready to build

---

## The Situation

NKST has no dedicated campaign. It's bundled into "Tour PPC - TOF - Purchase - Hidden Adventures" alongside the party barge, competing for budget — and losing. The algorithm routes spend toward party barge ads because they generate more volume. The best-performing swamp tour ad (12.88x ROAS) is getting $21/month in budget.

---

## Account Performance (Last 30 Days — March 6 to April 4, 2026)

| Metric | Value |
|---|---|
| Spend | $1,499 |
| Revenue | $11,148 |
| ROAS | 7.44x |
| Purchases | 66 |
| Cost per purchase | $22.71 |
| Reach | 104,591 |
| Frequency | 2.68 |
| CTR | 3.6% |
| CPC | $0.15 |

---

## Ad-Level Performance (Last 30 Days)

| Ad | Adset | Spend | Purchases | CPP | ROAS |
|---|---|---|---|---|---|
| **Swamp Tour V01C01** | Kayak Interests | $21 | 2 | $10.66 | **12.88x** |
| Carousel C01 | Kayak Interests | $168 | 8 | $20.95 | 8.62x |
| Carousel C01 | No Interests | $77 | 3 | $25.81 | 6.42x |
| Party Barge V01C01 | No Interests | $535 | 22 | $24.30 | 6.63x |
| Party Barge V01C01 | Party Barge Interests | $698 | 31 | $22.51 | 7.72x |

**Key insight:** The dedicated swamp tour ad has the best ROAS in the whole account and is starved of budget.

---

## Audience Breakdown (Last 30 Days)

### By Age
| Age | Spend | Purchases | CPP | ROAS |
|---|---|---|---|---|
| 25-34 | $581 | 31 | $18.74 | 8.4x |
| 35-44 | $582 | 23 | $25.32 | 5.5x |
| 45-54 | $250 | 9 | $27.79 | 9.6x |
| 55-64 | $65 | 1 | $65 | 1.0x |

### By Gender
| Gender | Spend | Purchases | CPP | ROAS |
|---|---|---|---|---|
| Female | $1,213 (81%) | 56 | $21.67 | 8.2x |
| Male | $271 (18%) | 9 | $30.15 | 4.1x |

Women 25-44 are the core buyer. 45-54 is underserved with high ROAS upside.

---

## Annual 2025 Adset Performance (Hidden Adventures Campaign)

| Adset | Spend | CPP | ROAS |
|---|---|---|---|
| Party Barge Interests | $3,969 | $43.14 | 4.46x |
| Kayak Interests | $610 | $87.27 | 1.58x |
| No Interests (Broad) | $1,477 | $39.93 | 3.64x |

The Kayak Interests adset bled money all of 2025 until new creative was refreshed in Feb 2026. Now it's performing.

---

## Current Active Adsets (Hidden Adventures Campaign)

1. **Algorithm+ No Interests** — broad/Advantage+, 25-65, New Orleans 50mi, home or recent
2. **Algorithm+ Kayak Interests** — adventure travel, outdoor rec, kayaking, kayak, canoeing
3. **Algorithm+ Party Barge Interests** — nightlife, parties, bars, nightclubs, upcoming birthday

---

## Problems to Fix

1. **No dedicated NKST campaign** — party barge eats the budget
2. **No retargeting** — Nola Pedal Barge retargeting expired June 2025, never replaced
3. **Checkout tracking is broken** — 3,338 landing page views → only 4 initiate_checkout events → 66 purchases. Booking platform not firing the InitiateCheckout pixel event. Needs dev fix.
4. **Frequency at 2.68** — same 104k people seeing it almost 3x. Needs fresh creative.
5. **No tourist vs. local targeting split** — both get the same ad, different intent

---

## The Plan

### Step 1: Create dedicated NKST campaign
**Campaign name:** NKST - TOF - Purchase - Swamp Tours
**Objective:** Sales (purchase)
**Daily budget:** $30-40/day to start

**Adset 1 — Broad/Advantage+**
- No interests, Advantage+ audience
- Location: New Orleans 50mi, home or recent
- Age: 25-54 (cut 55+ based on data)
- Let Meta find the buyers

**Adset 2 — Tourist Intent**
- Location: New Orleans 50mi, **recent only** (not home)
- Age: 25-54
- No interest targeting — tourists in decision mode don't need filtering
- Different creative than the locals adset

### Step 2: Build retargeting campaign
**Audience 1:** Website visitors to booking page, last 30 days, did not purchase
**Audience 2:** Video view 75%+ on swamp tour video, last 30 days
**Copy angle:** Urgency + scarcity. "Tours fill up fast on weekends. A few spots left for this Saturday."

### Step 3: Fix InitiateCheckout pixel
Have developer add the `InitiateCheckout` standard event to the booking flow before payment step. This unlocks mid-funnel optimization signal for Meta.

### Step 4: Scale 45-54 women
Create a dedicated adset targeting women 45-54 to test scale. Currently only $250/month but 9.6x ROAS.

---

## What We Know From Reviews

**Sources:** Trustpilot (4.9 stars, 98% 5-star, 81 reviews), TripAdvisor, GetYourGuide, Yelp (313 reviews)

**Recurring customer language:**
- "Best thing we did on our trip to New Orleans"
- "Hands-down the coolest experience of my trip"
- "Just what the soul ordered"
- "Seeing birds, turtles, and a gator were just a bonus to what was already a fantastic experience"
- "Essential part of being in New Orleans"
- "Most beautiful kayak tour I've taken in the world"
- "This will be a must do again on my next New Orleans trip"
- "Getting to immerse yourself in the swamp and be surrounded by nature is breathtaking"
- "No alligator baiting — an emphasis on appreciating the ecosystem"
- "Even the first-timers were able to easily navigate the water"
- "Water was calm, scenery was stunning, tranquil — just what the soul ordered"
- "Guide was funny, knowledgeable, and fantastic"

**Key themes to build ads around:**
1. "Best thing in New Orleans" — tops the food, tops the French Quarter
2. The gator proximity — visceral, specific, memorable
3. Guide relationship — named guides, personal, local knowledge
4. Peaceful/soul-restoring — not just adventure, emotional restoration
5. Eco-friendly — no baiting, respects wildlife (differentiates from boat tours)
6. Beginner-friendly — no experience needed, removes objection

---

## Ad Copy — Ready to Use

### Version 1: "Best Thing" Hook
**Headline:** The best thing you'll do in New Orleans

**Body:**
We hear this constantly from our guests. Not the food. Not the French Quarter. The swamp.

Two and a half hours paddling through real Louisiana bayou. Cypress trees draped in Spanish moss. Gators in the water next to your kayak. A small group. A guide who actually knows this place.

No experience needed. First-timers welcome.

Book before it sells out this weekend.

---

### Version 2: Visceral/Specific
**Headline:** Gators, cypress trees, and two hours of pure Louisiana

**Body:**
You're 20 minutes outside New Orleans, paddling through a swamp that most people never see.

Your guide points out a 6-foot alligator resting 10 feet away. You stop paddling. Everyone goes quiet.

That's a typical Tuesday for us.

Small groups. Knowledgeable local guides. No experience needed. This is the New Orleans your Instagram feed won't shut up about.

---

### Version 3: Tourist Decision Mode
**Headline:** You're doing the French Quarter. Do the swamp too.

**Body:**
Most visitors spend 3 days in New Orleans and go home without seeing the part that makes it unlike anywhere else on earth.

The bayou. Alligators. Moss-covered cypress trees. Wildlife you can't find anywhere else in America.

Our guided kayak tours run daily. Small groups, 2.5 hours, no experience required. Guests call it the best thing they did on their whole trip.

Spots fill fast on weekends.

---

### Version 4: Social Proof Quote Lead
**Headline:** "Just what the soul ordered."

**Body:**
That's what one of our guests wrote after kayaking through the Louisiana swamp with us. We get versions of that review constantly.

Paddle through Manchac Swamp. Spot alligators, herons, turtles, owls. Learn the bayou from a guide who grew up here.

4.9 stars. 300+ reviews. Daily tours from New Orleans.

No kayaking experience needed — your guide handles the rest.

---

### Version 5: Eco/Authentic (differentiates from boat tours)
**Headline:** See the swamp the right way

**Body:**
Motorboats scare the wildlife. Kayaks don't.

That's why you'll get within feet of alligators, turtles, and birds that most tour boats never see. Small groups, quiet water, a guide who respects the ecosystem as much as the experience.

Real Louisiana. No crowds. No bait.

Book a small-group kayak swamp tour from New Orleans.

---

## Still Needed

- [ ] Average ticket price per person (to validate CPP targets)
- [ ] Booking platform name (for pixel fix)
- [ ] Raw video footage / GoPro / customer UGC for creative
- [ ] Confirm ad account IDs for lskt, buffalo_bayou, dckt BMs
- [ ] Write carousel card copy (3-5 cards)
- [ ] Write retargeting ad copy
- [ ] Write birthday/bachelorette-specific ad for party barge adset

---

## Next Actions

1. Build NKST dedicated campaign with 2 adsets (broad + tourist intent)
2. Test Version 1 and Version 3 copy first
3. Get dev to add InitiateCheckout pixel event to booking flow
4. Set up retargeting campaign (website visitors + video viewers)
5. Scale to other BMs once NKST campaign is proven
