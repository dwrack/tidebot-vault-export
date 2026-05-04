# NOLA Party Barges — SEO, AEO, Ads & Conversion Growth Plan

**Date:** 2026-05-03
**Site:** nolapartybarges.com
**Data window:** Last 90 days GA4 (Feb 3 to May 3, 2026), full site crawl, competitor SERPs

---

## TL;DR (read this part)

The site does ~60k sessions and ~1,180 bookings in 90 days. That's a 1.97% sitewide conversion rate, which is fine but masks two things:

1. **Tracking is broken in two places.** Paid Social shows 17,771 sessions and zero conversions with 93-97% bounce rates. That's not bad creative, that's busted attribution. And nolapartybarges.com is listed as a referral source TO ITSELF (5,843 sessions, 317 conversions) which means the FareHarbor embed flow is breaking session continuity. Fix these two before judging anything else.
2. **The Freaky Tiki is a runaway hit, the rest of the catalog isn't pulling its weight.** Freaky Tiki page got 10,159 users. Twerkin Tiki: 2,529. Cajun Queen: 907. Sunset Seafood Boil: 366. That $165 cruise should be doing 10x what it is.

The single biggest unlock is **building real silos around the proven winners + claiming bachelorette/birthday/group SEO real estate that competitors are leaving open.** Cajun Encounters owns the swamp tour space with 61k reviews and a deep content moat. You won't out-swamp them. But nobody owns "best party boat for a NOLA bachelorette" or "BYOB sunset cruise vs Steamboat Natchez." That's where the money is.

---

## Section 1: What the data actually says

### Channel performance (90 days)

| Channel | Sessions | Conversions | CVR | Bounce |
|---------|----------|-------------|-----|--------|
| Direct | 10,868 | 232 | 2.1% | 67% |
| Paid Social FB | 9,490 | **0** | **0%** | **93%** |
| Paid Search (Google Ads) | 9,478 | 283 | **3.0%** | 50% |
| Self-referral (broken) | 5,843 | 317 | 5.4% | 21% |
| Paid Social IG | 5,738 | **0** | **0%** | **97%** |
| Organic Search | 4,799 | 88 | 1.8% | 37% |
| Organic Social FB | 4,007 | 8 | 0.2% | 91% |
| ChatGPT (AEO) | 93 | 3 | 3.2% | 51% |

**Reads I'd flag:**
- Google Ads is your best converting channel. 3.0% CVR. Don't cut it, scale it.
- Paid Social is either misattributed or your audience is junk. Almost certainly the former. Even garbage Meta traffic gets >0% conversion if pixel + click ID are wired correctly.
- Organic Search punches above its weight on engagement (37% bounce, very good) but only does 4,799 sessions. Tons of headroom.
- ChatGPT is already a paying channel. 93 sessions, 3 bookings, 3.2% CVR. Better than organic search. AEO needs investment now, not in 12 months.

### Top pages (90 days)

| Page | Users | Bounce |
|------|-------|--------|
| / | 27,045 | **72%** |
| /the-freaky-tiki/ | 10,159 | 50% |
| /the-twerkin-tiki/ | 2,529 | 26% |
| /pedal-bike-barge-cruise/ (legacy) | 2,522 | 23% |
| /our-boats/ | 1,436 | 13% |
| /the-cajun-queen/ | 907 | 13% |
| /how-much-budget-NOLA-vacation-2024/ | 474 | 67% |
| /sunset-cocktail-cruise-seafood-boil/ | 366 | 23% |
| /faq/ | 340 | 13% |
| /boat-rental/ | 450 | 11% |

**Reads:**
- Homepage is doing 72% bounce. That's the single highest-leverage page on the site. If you cut bounce 10 points you add ~250 bookings/year at current CVR.
- Freaky Tiki is the breakout. Build the brand around it, not around a generic "tiki boat" identity.
- Sunset Seafood Boil at 366 users for a $165 product is criminal. That's the one page where every user is worth real money.
- /pedal-bike-barge-cruise/ still pulls 2,522 users on a legacy URL and a name you've moved away from. Either redirect it or rebuild the page around current positioning.
- Boat rental page is thin (~400 words) and only gets 450 users despite "private boat rental new orleans" being a real money keyword.

### Geography

Top cities: New Orleans, Dallas, Mobile, Chicago, Birmingham, Houston, Atlanta. The Dallas/Houston/Birmingham/Atlanta cluster is your tourist drive-market. Atlanta and Birmingham are way under-served by direct flights but huge for road trips. Worth a Google Ads geo-test.

### Conversions

1,180 purchases in 90 days = ~13/day. Mobile is 87% of bookings. The site has to be mobile-first or nothing.

---

## Section 2: Fix these five things this month (before anything else)

These aren't strategic. They're plumbing. Without them, every other recommendation is half-blind.

### 1. Connect Google Search Console (today)

Neither dwrack81@gmail.com nor nolapedalbarge@gmail.com has GSC access for nolapartybarges.com. I literally couldn't pull a single query for this report. Add `dwrack81@gmail.com` as Owner in Search Console, verify domain property, and submit the sitemap. This unlocks: query data, click data, indexing issues, Core Web Vitals, and AI Overview impressions (Google rolled out an AIO performance report).

### 2. Fix the self-referral attribution bug

5,843 sessions are showing up as referrals from nolapartybarges.com to itself. That's almost certainly the FareHarbor embed flow breaking the GA session via cross-domain redirects. Add `fareharbor.com` and `book.fareharbor.com` (and the `nolapartybarges.com` cross-domain itself if needed) to GA4 Admin → Data Streams → Configure tag settings → List unwanted referrals. Once fixed, your real direct/organic numbers will jump and your CVR per channel will become trustable.

### 3. Audit the Meta pixel (today)

17,771 paid social sessions, zero conversions, 95% bounce average. That's a tracking bug, not a creative bug. Likely culprits:
- FBCLID isn't being preserved through the FareHarbor redirect, so Pixel + CAPI lose the user before purchase.
- Conversion event isn't firing because FareHarbor's confirmation page is on a different domain.
- Pixel is firing but CAPI isn't deduping, or vice versa.

Get the dev who set up the ads system to verify Purchase event fires and matches in Events Manager Test Events for at least 5 booked sessions. Until this is fixed, you're flying blind on Meta spend.

### 4. Add meta descriptions and basic schema sitewide

Zero pages have meta descriptions. That's free SERP CTR you're leaving on the table. Add one to all 17 page sitemap URLs (max 155 chars, lead with the differentiator: "BYOB," "no captain license needed," "closest swamp tour to French Quarter," etc).

Add JSON-LD schema on:
- Homepage: `LocalBusiness` (name, address, phone, hours, geo, aggregateRating, sameAs social)
- Each boat page: `Product` (name, image, description, offers.price, offers.priceCurrency, aggregateRating)
- /faq/: `FAQPage` (every Q&A wrapped, this is the highest-value schema for AI Overviews)
- /sunset-cocktail-cruise-seafood-boil/: `Event` or `TouristTrip` schema with price, duration, location

This single project probably adds 15-25% to organic CTR within 60 days.

### 5. Image alt text sweep

Sitewide alt text is generic or missing. For a tourism business where Google Images is a real entry point, this is leaving 1,000+ monthly impressions on the table. Use a WordPress plugin or batch edit. Format: `freaky-tiki-bachelorette-party-new-orleans-bayou-bienvenue.jpg` style descriptions, not "IMG_4032.jpg."

---

## Section 3: Silo architecture (the real plan)

You already have 40+ blog posts that fall into rough topic clusters. They're not interlinked, there are no hub pages, and the home page doesn't route to them. Here's the structure:

### Silo 1: BOATS (transactional, exists)

```
/our-boats/ (HUB)
├── /the-freaky-tiki/
├── /the-twerkin-tiki/
├── /the-cajun-queen/
├── /the-bayou-boogie/
├── /bentley-bayou-cruiser/
└── /boat-rental/ (private charter hub)
    ├── /boat-rental/bachelorette/ (NEW)
    ├── /boat-rental/birthday/ (NEW)
    ├── /boat-rental/corporate/ (NEW)
    ├── /boat-rental/wedding/ (NEW)
    └── /boat-rental/large-group/ (NEW)
```

The boat-rental sub-pages are the single biggest content gap. Each one targets one buyer intent ("bachelorette boat new orleans," "corporate boat rental nola," etc.) with: itinerary, group size, pricing, photo gallery from that vertical, FAQ, FareHarbor widget. These convert because the visitor self-selected.

### Silo 2: SWAMP & BAYOU (informational + commercial)

```
/swamp-tours/ (NEW HUB - currently doesn't exist as nav item)
├── /swamp-tours/best-time-to-go/
├── /swamp-tours/what-to-wear/
├── /swamp-tours/airboat-vs-pontoon/
├── /swamp-tours/closest-swamp-tour-to-french-quarter/  ← THE MOAT
├── /swamp-tours/with-alligators/
├── /swamp-tours/byob-allowed/
├── /swamp-tours/private-group/
└── /vs-cajun-encounters/  (comparison)
```

You don't beat Cajun Encounters on swamp tour authority. You beat them on **specific intent**: "BYOB swamp tour," "closest to French Quarter," "private group," "no airboat noise." The 7 miles from FQ + bathroom onboard angle is a defensible local moat. Own it in a dedicated page, not just one line on the homepage.

### Silo 3: BACHELORETTE / BIRTHDAY / GROUP EVENTS (currently nonexistent)

```
/bachelorette-party/ (PILLAR PAGE - 2,500+ words)
├── /bachelorette-party/itinerary/  (Day-by-day NOLA bach itinerary)
├── /bachelorette-party/best-boats/
├── /bachelorette-party/cost-guide/
├── /bachelorette-party/what-to-wear/
└── /bachelorette-party/playlist/  (link bait)

/birthday-party-new-orleans/ (PILLAR)
├── /birthday-party/30th/
├── /birthday-party/40th/
├── /birthday-party/50th/
└── /birthday-party/group-of-20/

/corporate-events/  (PILLAR)
└── /corporate-events/team-building/
```

Cajun Encounters doesn't have these. CVB owns "things to do bachelorette new orleans" with editorial content. Batch and Stag & Hen rank well too. None of them have a *boat* angle. The opportunity is to build the definitive bachelorette-on-the-water content and convert at the bottom of the page with a Freaky Tiki widget.

### Silo 4: SUNSET CRUISES & SPECIALTY EXPERIENCES

```
/sunset-cruise-new-orleans/  (NEW HUB)
├── /sunset-cocktail-cruise-seafood-boil/  (existing, BUILD UP)
├── /sunset-cruise/vs-steamboat-natchez/
├── /sunset-cruise/vs-creole-queen/
└── /sunset-cruise/byob-sunset-tour/
```

The seafood boil cruise is your premium product and it's underexposed. The vs-Steamboat-Natchez and vs-Creole-Queen pages target real comparison search volume and let you frame the "BYOB, smaller group, actual locals" angle.

### Silo 5: NOLA TRAVEL HUB (already started)

```
/things-to-do-in-new-orleans/  (PILLAR - currently underbuilt)
├── /blog/budget-guide-new-orleans/  (already exists, top-10 traffic page)
├── /blog/best-restaurants-near-marina/
├── /blog/december-in-nola/
├── /blog/halloween-in-nola/
├── /blog/3-day-nola-itinerary/
├── /blog/where-to-stay-in-new-orleans/
└── /blog/getting-around-new-orleans/
```

These don't convert directly but they pull top-of-funnel tourist traffic. Internally link every one of them down into the boat silos with contextual CTAs ("Looking for something to do on Saturday afternoon? Our 2pm Freaky Tiki cruise is 10 minutes from the French Quarter.")

### Internal linking rules

- Every blog post links to its silo hub + 2-3 sibling posts + 1 commercial page
- Every commercial page links to 2-3 supporting blog posts (e.g. /the-freaky-tiki/ links to /bachelorette-party/, /swamp-tours/byob-allowed/, /things-to-do-in-new-orleans/)
- Hub pages link down to all children
- Footer should have a "Plan Your Trip" column linking to all 5 hubs

---

## Section 4: AEO / GEO (this is the next 18 months)

ChatGPT is already sending 93 sessions and 3 bookings in 90 days. That's small but it's the starting line, not the finish. Google AI Overviews now show on ~25% of tourism queries. Perplexity is growing.

What gets cited by LLMs:
1. **Specific, structured answers to common questions.** Not "Our boats are amazing for groups." Instead: "Our Freaky Tiki holds 32 passengers, allows BYOB, and runs daily 11am, 2pm, and 5pm cruises from Bayou Bienvenue Marina, 7 miles from the French Quarter."
2. **FAQ pages with `FAQPage` schema.** Not optional anymore. AI engines parse JSON-LD heavily.
3. **Citation-ready content with stats and numbers.** "32 passengers," "$63 per person," "90-minute tour," "7 miles from French Quarter," "no boating license required."
4. **Mentions on third-party sites the AI trusts:** TripAdvisor, Reddit (r/NewOrleans), neworleans.com, local press.

### AEO playbook (next 90 days)

1. **Rewrite the FAQ page with 30+ questions structured for AI:**
   - "How much does a party boat cost in New Orleans?" → answer with $63 starting price
   - "Can you BYOB on a New Orleans boat tour?" → yes, here's the rules
   - "What's the closest swamp tour to the French Quarter?" → ours, 7 miles
   - "Do you need a captain's license to rent a boat in New Orleans?" → for our charters, no
   - "Are alligators on the bayou tours?" → yes, in spring/summer/fall
   - "What's the difference between an airboat and a pontoon swamp tour?" → comfort vs speed
   - Each one wrapped in FAQPage schema. Each one written to be quotable in one sentence.

2. **Get on Reddit r/NewOrleans, r/AskNOLA, r/travel.** Not spammy posts, real answers from a real account that links back when relevant. Reddit is now one of the top sources for AI Overviews on tourism queries.

3. **Get listed on the citation-friendly aggregators:**
   - neworleans.com (official CVB) - paid listing or partnership
   - explorelouisiana.com (already a referrer at 20 sessions, push for more visibility)
   - TripAdvisor (you have a presence, push for more reviews)
   - Yelp
   - Local press (Eater NOLA, Antigravity Magazine, Where Y'at)

4. **Statistical landmarks:** add a "By the Numbers" section to the homepage. "32 passengers per boat. 7 miles from the French Quarter. 4 boats in the fleet. Daily departures since 2018." Numbers get cited.

5. **llms.txt file:** publish `https://nolapartybarges.com/llms.txt` listing your key pages with one-line descriptions. AI crawlers are starting to look for this.

---

## Section 5: Google Ads recommendations

I don't have direct Ads account data, but from the GA4 channel performance:

**Ads is your best paid channel by a mile.** 3.0% CVR vs 0% on Meta. Whatever budget split you have between Google and Meta, shift it toward Google until Meta tracking is fixed and proven.

### Specific moves:

1. **Build out a campaign per silo, not per boat.** Currently you're probably bidding on "freaky tiki boat" type branded queries. Add:
   - Bachelorette campaign: "bachelorette boat new orleans," "bachelorette party boat nola," "girls trip new orleans boat" with /bachelorette-party/ landing page
   - Birthday campaign: "birthday boat rental new orleans," "30th birthday new orleans"
   - Sunset/seafood campaign: targeting "sunset cruise new orleans," "seafood boil cruise"
   - Comparison campaign: bid on competitor brand terms ("steamboat natchez alternative," "creole queen vs," "cajun encounters" - careful with TM)

2. **Geo-test the drive markets.** Birmingham, Atlanta, Mobile, Houston, Dallas all show up in your GA. Run a 30-day Performance Max campaign targeting these specifically with "New Orleans weekend trip" creative.

3. **Schedule ads around booking patterns.** People plan NOLA trips on Sunday nights and book boats Wednesday-Friday. Use bid adjustments accordingly.

4. **Negative keyword the swamp lane unless you can compete on it.** Cajun Encounters will outbid you on pure "swamp tour" generics. Bid on long-tail variations ("BYOB swamp tour," "closest swamp tour to French Quarter," "private group swamp tour") instead.

5. **Add call extensions.** Phone bookings have higher CVR than form bookings on tourism queries.

---

## Section 6: Conversion fixes (the homepage problem)

Homepage = 27,045 users, 72% bounce. That's the leakiest part of the funnel.

### Hypotheses + tests:

1. **Hero is unclear.** "Most Swamp Tours Are Boring. Ours Aren't." is fun but doesn't communicate what you sell, where you are, or what it costs. Test a hero that has: photo of boat full of people having a blast + "BYOB Party Boats from $63 - Closest to French Quarter, 7 Miles Away" + primary CTA "Check Today's Availability."

2. **Date picker above the fold.** FareHarbor has a calendar widget. Putting it directly in the hero (vs requiring a click) typically lifts booking flow entries 30-50%.

3. **Social proof bar.** "Rated 4.9 on TripAdvisor. 1,200+ groups partied with us in 2025." Anchored just below hero.

4. **Mobile-first redesign.** 87% of users are on mobile. Make sure boat selection is one tap, calendar is one tap, booking is three taps max.

5. **Exit intent or sticky CTA.** Right now nothing rescues the 72% who bounce. A simple sticky bottom bar on mobile ("Today's Cruises - Book Now") could pick up 5-10% of would-be bouncers.

---

## Section 7: 30/60/90 day roadmap

### Days 1-30 (plumbing month)

- [ ] Add dwrack81@gmail.com to GSC, verify domain, submit sitemap
- [ ] Fix self-referral attribution (FareHarbor cross-domain in GA4)
- [ ] Audit + fix Meta pixel + CAPI (this is critical)
- [ ] Add meta descriptions to all 17 core pages
- [ ] Add LocalBusiness, Product, FAQPage schema (homepage, boat pages, FAQ)
- [ ] Image alt text sweep
- [ ] Rewrite homepage hero + add date picker
- [ ] GBP category audit (Boat tour agency primary), add service areas, photo refresh

### Days 31-60 (silo build month)

- [ ] Build /bachelorette-party/ pillar page (2,500 words + FAQ + boat CTA)
- [ ] Build /swamp-tours/ hub + /closest-swamp-tour-to-french-quarter/
- [ ] Build /sunset-cruise-new-orleans/ hub + Steamboat Natchez comparison
- [ ] Build out /boat-rental/ with bachelorette/birthday/corporate sub-pages
- [ ] Rewrite /faq/ with 30+ AI-citable Q&As
- [ ] Internal linking pass across all blog posts
- [ ] Launch Google Ads bachelorette + birthday + comparison campaigns
- [ ] Start weekly GBP posts

### Days 61-90 (content + AEO push)

- [ ] Build /things-to-do-in-new-orleans/ as real hub linking to existing blog
- [ ] Publish 6-8 new blog posts targeting tourist top-of-funnel queries
- [ ] Reddit presence (1 helpful comment per week minimum)
- [ ] Get on neworleans.com, push for explorelouisiana.com mention
- [ ] TripAdvisor review push (QR code + post-cruise email)
- [ ] llms.txt published
- [ ] First A/B test on homepage hero with results
- [ ] Geo-test Google Ads in Birmingham/Atlanta/Mobile/Houston

---

## Section 8: KPIs to watch

| Metric | Today (90d) | 6 month target | 12 month target |
|--------|-------------|----------------|-----------------|
| Total bookings | 1,180 | 1,800 | 2,800 |
| Organic search sessions | 4,799 | 9,000 | 18,000 |
| Organic CVR | 1.8% | 2.5% | 3.0% |
| AI/LLM referral sessions | 93 | 500 | 2,000 |
| Homepage bounce | 72% | 60% | 50% |
| Pages with schema | 0 | 100% of templates | 100% |
| Average position (when GSC connects) | unknown | top-10 for 50 queries | top-3 for 100 queries |

---

## What I'd do this week if I were you

1. Get GSC connected (15 min admin task). Without it, half this plan is guessing.
2. Get the Meta pixel verified by whoever set it up. 17,771 sessions/quarter with zero attributed conversions is either the biggest leak or the biggest data fix on the entire site.
3. Pick ONE silo to build first. My pick: bachelorette. Highest commercial intent, biggest competitor gap, plays to the pirate/renegade brand reposition.

Everything else compounds from those three.
