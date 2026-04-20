# Meta Ads Strategy — All Businesses

**Created:** April 14, 2026
**Status:** Planning phase
**Budget:** $5k+/mo across all businesses
**Related:** [[NKST — Facebook Ads Strategy & Copy]] (detailed NKST plan with ad copy)

---

## The Big Picture

10 tour/experience businesses across 5 cities. FareHarbor customer data is the foundation of everything: ad targeting, customer profiling, cross-sell, and eventually brand/partnership deals.

**Business Managers:**
- **Gravity Trails** (BM 87863118): NKST, NOLA Party Barge, NOLA Bike Bar
- **LSKT** (BM 638850950128825): Austin Kayak Tours
- **Buffalo Bayou** (BM 1015419897308486): Buffalo Bayou Kayak, Houston Pedal Barge
- **DCKT** (BM 10153674414451399): Door County Kayak Tours
- **Missing BMs**: Ebb & Ember (Portland), Door County Ebike, Airstream Sauna

---

## Phase 1: Infrastructure (Week of April 14)

### Pixel & Conversion Tracking
For each business website:
- Meta Pixel installed and firing on all pages
- Standard events: `ViewContent` (tour page), `InitiateCheckout` (booking form start), `Purchase` (booking confirmation)
- Phone-only businesses: set up offline conversion tracking or CallRail with Meta's offline events API
- Verify via Meta Events Manager / Pixel Helper

**Known issue from NKST audit:** InitiateCheckout pixel is broken (3,338 landing page views but only 4 initiate_checkout events). Likely broken on other businesses too. Needs dev fix across all sites.

### FareHarbor Customer Data Export
For each business, export all historical booking data:
- Customer email, name, booking date, tour type, group size, dollar amount, zip code/city

**Segment into:**
- All customers (master list per business)
- High-value customers (booked 2+ times or spent above average)
- Recent customers (last 90 days)
- Customers by tour type
- Customers by origin city/zip

**Upload as Custom Audiences to Meta**, then build Lookalike Audiences (1%, 2%, 5%) from each segment. Set up monthly export cadence.

### Cross-Business Customer Matching
Combine FareHarbor exports across all businesses. Look for:
- **Overlap**: Do NOLA Party Barge customers also book NOLA Kayak?
- **Cross-city travelers**: Did someone who kayaked in Austin also show up in Houston?
- **Demographics**: Age ranges, group sizes, spending tiers, booking lead time
- **Geographic origin**: Where are customers traveling from?

Upload combined master list as "portfolio customer" audience. Build lookalikes from it.

### Custom Audiences Per Business
- FareHarbor customers (segmented as above)
- FareHarbor high-value lookalikes (1% and 3%)
- Cross-business portfolio lookalikes
- Website visitors (30/60/90 days)
- Booking page visitors who didn't convert
- Video viewers (25%, 50%, 75%)
- Page engagers

---

## Phase 2: Campaign Structure (Per Business)

### Tier 1: Awareness (20% of budget)
- **Objective**: Video Views or Reach
- **Audience**: Broad targeting in metro (or tourist source cities for Door County)
- **Creative**: 15-30 sec UGC/GoPro video. Real people having fun >> polished content.
- **Goal**: Fill retargeting pools cheaply

### Tier 2: Retargeting (30% of budget)
- **Objective**: Traffic or Engagement
- **Audience**: Website visitors, video viewers, page engagers
- **Creative**: Testimonials, review quotes, "what to expect" carousel, seasonal urgency
- **Goal**: Get warm prospects back to booking page

### Tier 3: Conversion (50% of budget)
- **Objective**: Conversions (Purchase/Lead)
- **Audience**: Booking page abandoners, past customer lookalikes, high-intent visitors
- **Creative**: Direct CTA, limited availability, pricing, social proof
- **Goal**: Drive bookings

**Note:** NKST already has a detailed campaign plan with ad copy ready. See [[NKST — Facebook Ads Strategy & Copy]]. That plan calls for a dedicated campaign separated from the party barge, plus tourist vs. local adset split.

---

## Phase 3: Budget Allocation (April 2026 Starting Point)

| Business | City | Season | Budget/mo | Notes |
|---|---|---|---|---|
| NOLA Party Barge | NOLA | Peak (Jazz Fest) | $700 | High ticket, peak season |
| NOLA Kayak Swamp Tours | NOLA | Peak | $500 | Best ROAS in account when given budget |
| NOLA Bike Bar | NOLA | Peak | $400 | Group bookings |
| Austin Kayak Tours | Austin | Peak (pre-heat) | $500 | Dial back June-Aug |
| Buffalo Bayou Kayak | Houston | Good | $400 | Scale back for summer heat |
| Houston Pedal Barge | Houston | Good | $500 | Group/party bookings |
| Door County Kayak Tours | Door County | Ramping | $600 | Pre-season awareness |
| Door County Ebike | Door County | Ramping | $300 | Build awareness |
| Airstream Sauna | Door County | Year-round | $200 | Test spend |
| Ebb & Ember | Portland | Ramping | $400 | Pre-summer push |

**Total: ~$5,000/mo.** Shift monthly based on performance and season.

---

## Phase 4: Creative Strategy

### What works for experience businesses:
1. **UGC video** (phone footage from real tours)
2. **Customer review overlays** on photos/video
3. **POV reels** (first-person perspective)
4. **Carousel ads** (arrival to highlight moment)
5. **Seasonal hooks** ("Jazz Fest week? Start with a morning swamp kayak")

### Minimum creative per business:
- 2-3 short videos (15-30 sec)
- 3-5 static images with review quotes
- 1 carousel ad
- Refresh monthly

### Ad copy rules:
- Lead with the experience, not the company name
- Specific details: "90 minutes through cypress-lined bayous"
- Social proof: star ratings, review count
- Clear CTA with price when possible

---

## Phase 5: Customer Profile Intelligence

### Build from FareHarbor data:

**Demographics:**
- Age distribution (Meta audience insights once custom audiences uploaded)
- Gender split per business
- Household income proxy (zip code mapping)
- Group composition: couples, families, bachelorette parties, corporate

**Behavioral patterns:**
- Booking lead time (same-day vs. 2 weeks out)
- Peak booking days/times
- Average group size and spend
- Repeat rate across businesses
- Seasonal curves per city

**Geographic origin:**
- Top 10 origin cities/states per business
- Local vs. tourist split
- Which origin markets overlap across businesses

### How to Use It:
1. **Targeting**: Build lookalikes and target actual origin zip codes
2. **Creative**: If 60% of party barge bookings are bachelorette groups, show bachelorette groups
3. **Timing**: If most bookings happen 10-14 days out, front-load conversion ads to that window
4. **Cross-sell**: Kayak booker sees party barge ad. They're already proven experience-bookers.

**From NKST data we already know:**
- Women 25-44 are the core buyer (81% of spend, 8.2x ROAS)
- 45-54 is underserved with 9.6x ROAS
- 55+ underperforms (1.0x ROAS)

---

## Phase 6: Brand & Partnership Strategy

Your FareHarbor data across 10 businesses and 5 cities is a unique asset. Thousands of verified outdoor experience buyers. That's valuable to partners.

### Partnership types (ordered by ease of execution):

**1. Complementary businesses** (start here)
- Restaurants, breweries, bars near tour launch points
- Audience-sharing, co-branded Meta ads splitting costs
- Example: NOLA Bike Bar + popular NOLA brewery. Door County Kayak + local winery.

**2. Hotels & Airbnb hosts**
- "X% of our customers come from out of town. Let's cross-promote."
- Hotels feature tours in welcome packets/emails. Referral code or affiliate cut.

**3. Tourism boards**
- "We operate 3 experiences in NOLA. Here's aggregate data on where visitors come from."
- Get in official visitor guides. Some boards offer co-op ad funding.

**4. Outdoor/lifestyle brands**
- Yeti coolers on the party barge, Patagonia on kayak tours
- Start with regional brand reps, not corporate
- Free tour for their team + social content in exchange for product/sponsorship

**5. Event & group sales**
- Wedding planners, event coordinators, corporate retreat organizers
- Data-backed pitch: "40% of party barge bookings are bachelorette parties"

### Building the pitch:
- 1-pager per city: total bookings, customer demographics, origin cities, average spend, review scores
- Lead with data: "We ran 2,000 tours last year in NOLA. 40% of our customers came from Texas."
- Update quarterly

---

## Phase 7: Audience Strategy

### Tourist vs. Local (per business)

**Tourists** (NOLA, Door County, Austin):
- "Traveling in [City]" or "Recently in [City]" Meta behaviors
- "Trip planning" interests + city interest overlap
- Run 2-4 weeks before peak tourist windows

**Locals** (Houston, Portland):
- Metro area, 25-54, outdoor activities / date night / group events
- "Things to do this weekend" angle

### Lookalikes:
- 100+ purchasers per business: build 1% lookalikes (best-performing)
- Under 100: broader interest targeting, let Meta optimize

---

## Phase 8: Seasonal Calendar

| Month | Ramp Up | Peak Spend | Scale Back |
|---|---|---|---|
| Apr-May | Door County, Portland | NOLA, Austin | - |
| Jun-Aug | - | Door County, Portland, Houston evenings | Austin, NOLA (heat) |
| Sep-Oct | NOLA (fall), Austin (fall) | Door County (fall colors) | Portland (rain) |
| Nov-Dec | - | NOLA (holidays) | Door County, Portland |
| Jan-Mar | NOLA (Mardi Gras), Austin (SXSW) | - | Door County (closed) |

**Monthly rhythm:**
- Start of month: Review performance, kill underperformers, scale winners
- Mid-month: Refresh creative on anything with frequency > 3
- End of month: Reallocate budget for next month's seasonal shift

---

## Phase 9: Measurement & Optimization

### Weekly KPIs:
- **Cost per booking**: target < $15-25 (kayak tours), < $30-50 (party barge/group)
- **ROAS**: aim for 5x+ on conversion campaigns
- **CTR**: below 1% = creative needs work
- **Frequency**: above 3 = audience fatigued
- **CPM**: monitor for seasonal spikes

### Rules:
- 7+ days, 0 conversions, $50+ spend: pause
- CTR > 2% with conversions: increase budget 20%
- Test 2-3 creatives per ad set, kill loser after 500+ impressions
- Duplicate winners into new audiences before scaling budget

---

## Execution Timeline

1. **Week 1 (April 14)**: Export FareHarbor data for all businesses. Audit pixels. Set up missing BMs.
2. **Week 2**: Clean/segment data. Upload to Meta. Build lookalikes. Gather creative.
3. **Week 3**: Cross-business customer analysis. Build customer profile doc. Launch campaigns for top 5 businesses.
4. **Week 4**: Launch remaining businesses. Start retargeting. Begin cross-sell campaigns.
5. **Month 2**: Refine profiles with Meta Audience Insights. Build per-city media kits for partnerships.
6. **Month 3**: Start partnership conversations with real data. Test co-branded campaigns.
7. **Ongoing**: Review, reallocate, refresh creative, update data exports, grow partnership pipeline.

---

## Still Needed

- [ ] Set up BMs for Ebb & Ember, DC Ebike, Airstream Sauna
- [ ] Export FareHarbor data for all businesses
- [ ] Fix InitiateCheckout pixel across all sites (confirmed broken on NKST)
- [ ] Gather/create UGC video for each business
- [ ] Build NKST dedicated campaign (per [[NKST — Facebook Ads Strategy & Copy]])
- [ ] Write ad copy for remaining 9 businesses
- [ ] Confirm ad account IDs for all BMs
- [ ] Build customer profile document from FareHarbor data
- [ ] Create per-city partnership 1-pagers
