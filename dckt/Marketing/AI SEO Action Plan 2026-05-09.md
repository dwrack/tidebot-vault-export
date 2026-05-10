# AI SEO Action Plan — DCKT

**Date:** 2026-05-09
**Companion to:** `AI SEO Audit 2026-05-09.md`
**Owner:** David (with Bella for execution where flagged)

---

## What changed from the first audit

When I pulled the raw HTML (not WebFetch summaries), the picture sharpened in three important ways:

1. **Homepage actually has 4 schema blocks already** — `Organization`, `LocalBusiness`, `WebSite`, `WebPage`. So we're not starting from zero. We're starting from "boilerplate and incomplete."
2. **Tour pages still only have `BreadcrumbList`.** Cave Point, Eco Estuary, and the others have no `Tour`, `Product`, `Offer`, or `FAQPage` schema. This is the real gap.
3. **Lakeshore Adventures has the same gap.** They have only `BreadcrumbList` on their kayak-tours hub and `Organization` + `WebSite` + `WebPage` on the Cave Point page. **Nobody in Door County has Tour schema with Offers + FAQ.** This isn't catch-up. It's a clean opening to lead.

Plus three smaller but real issues I missed first pass:

- **Pregnancy post schema is malformed.** Date strings are not ISO 8601 (`"December 18, 2023"` should be `"2023-12-18"`). Author is `Organization`, not `Person`. HTML entities aren't unescaped in the headline (`&#8217;`).
- **Homepage `LocalBusiness` schema is missing `aggregateRating`** — we have 2,000+ 5-star reviews per memory and we're not surfacing them in schema.
- **Schema address is "Sturgeon Bay 54235, 6329 Wisconsin 57"** — that's the Jacksonport tour location. Per memory the legal/business address is `8442 State Hwy 42, Fish Creek WI 54212`. Decide which is canonical and align Yelp, GBP, schema, and footer.

---

## The competitive insight worth its own line

Tour schema with `Offer`, `priceRange`, and `availability` paired with `FAQPage` schema creates eligibility for Google rich results that Lakeshore, CPPP, Kayak Guide Justin, and Door County Adventure Center are all leaving on the table. This is structural alpha, not just a hygiene fix.

---

## Sequence

### Week 1 — Foundation (technical)

These are no-content-debate fixes. Bella or a contractor can do them with the templates below.

#### 1.1 Fix homepage `LocalBusiness` schema (1 hour)
**What:** Add `aggregateRating`, `openingHours`, `sameAs` (social profiles), `image`, `description`, `areaServed`. Also reconcile the address vs. memory's verified legal address.

**Where:** Homepage Schema Markup field (per CLAUDE.md, no `<script>` wrapper, no escaped quotes).

**Paste-ready template** (replace bracketed values; if Jacksonport is the customer-facing storefront and Fish Creek 54212 is HQ, list both):

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.doorcountykayaktours.com/#localbusiness",
  "name": "Door County Kayak Tours",
  "url": "https://www.doorcountykayaktours.com",
  "telephone": "+1-920-868-1400",
  "priceRange": "$$",
  "image": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/[hero-image-path].jpg",
  "description": "Guided kayak, e-bike, and paddleboard tours across Door County, Wisconsin since 2002. Beginner-friendly tours of Cave Point, Death's Door shipwrecks, Cana Island, and Eco Estuary launch points.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "8442 State Hwy 42",
    "addressLocality": "Fish Creek",
    "addressRegion": "WI",
    "postalCode": "54212",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "45.1294",
    "longitude": "-87.2470"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      "opens": "08:00",
      "closes": "19:00",
      "validFrom": "2026-05-15",
      "validThrough": "2026-10-15"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "2000",
    "bestRating": "5"
  },
  "sameAs": [
    "https://www.instagram.com/doorcountykayaktours/",
    "https://www.facebook.com/DoorCountyKayakTours/",
    "https://www.tripadvisor.com/Attraction_Review-g59850-d1036732-Reviews-Door_County_Kayak_Tours-Egg_Harbor_Wisconsin.html"
  ],
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Door County, Wisconsin"
  },
  "founder": "David Rack",
  "foundingDate": "2002"
}
```

**Acceptance:** Schema validator passes (Google Rich Results Test). Live page renders schema. `reviewCount` reflects current truth (we said 2,000+, use the actual number).

#### 1.2 Fix pregnancy-post schema (15 min)
**What:** Change date format to ISO 8601, change author to `Person` (or `[Organization, Person]` array), add `mainEntityOfPage`, `publisher`, unescape entities, and add a paired `FAQPage` block.

**Replace the existing Article block with:**

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Kayaking While Pregnant: What's Actually Safe From Guides Who've Paddled With Hundreds of Expecting Moms",
  "datePublished": "2023-12-18",
  "dateModified": "2026-05-06",
  "author": {
    "@type": "Person",
    "name": "[Lead Guide Name]",
    "jobTitle": "Lead Guide, Door County Kayak Tours",
    "worksFor": {
      "@type": "Organization",
      "name": "Door County Kayak Tours"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Door County Kayak Tours",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.doorcountykayaktours.com/wp-content/uploads/[logo-path].png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.doorcountykayaktours.com/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/"
  },
  "image": {
    "@type": "ImageObject",
    "url": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/2023/12/pregnant-lady-kayaking-with-lighthouse-cartoon.jpg",
    "width": 1000,
    "height": 1000
  },
  "citation": [
    "https://www.acog.org/womens-health/faqs/exercise-during-pregnancy"
  ]
}
```

**Pair with a separate FAQPage block** — this is the AI Overview play. Pull 6-8 questions already in the post:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is kayaking safe during pregnancy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Calm-water kayaking is generally safe during early and middle trimesters of an uncomplicated pregnancy, with provider clearance. We've guided hundreds of pregnant paddlers in Door County over 20+ years on flat-water tours like our Eco Estuary route. Avoid whitewater, big lake exposure, and any tour that requires rolling or wet-exit drills. Always run kayak plans by your OB or midwife first."
      }
    },
    {
      "@type": "Question",
      "name": "Which Door County kayak tour is safest for pregnant paddlers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Eco Estuary Tour on Rieboldt Creek at the base of Moonlight Bay is the calmest, most beginner-friendly tour we run. It uses sit-on-top tandems on a quiet creek with no Lake Michigan exposure, which is the right tour for most pregnant guests."
      }
    },
    {
      "@type": "Question",
      "name": "Do life jackets fit comfortably during pregnancy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, with the right size. We carry larger PFDs that adjust to fit a growing belly without compressing the abdomen. A PFD that squeezes the midsection is wrong for pregnancy. Tell your guide ahead of time and we will bring sizing options."
      }
    },
    {
      "@type": "Question",
      "name": "How late in pregnancy can you kayak?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most guests we've guided through later trimesters do their last paddle around weeks 28-32 of an uncomplicated pregnancy. After that, comfort, balance, and bathroom access become the limiting factors. Always defer to your provider."
      }
    },
    {
      "@type": "Question",
      "name": "What should pregnant paddlers wear and bring?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wicking clothing or swim layers, water shoes, sunscreen, a hat, and twice the water you think you need. Skip cotton. Bring a snack. Tell your guide your due date and any concerns at check-in so we can adjust pace and rest stops."
      }
    },
    {
      "@type": "Question",
      "name": "Can you cancel a kayak tour if you're not feeling well?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Door County Kayak Tours offers free cancellation up to 24 hours before your tour. If you wake up feeling off, call or text us. Pregnancy plans change, and we'd rather rebook you than have you push through a tour that doesn't feel right."
      }
    }
  ]
}
```

**Acceptance:** Both blocks validate. The page becomes eligible for FAQ rich result and Article rich result. Verify on the live page (Google Rich Results Test) before claiming this done.

#### 1.3 Add `TouristTrip` + `Offer` + `FAQPage` schema to all 8 tour pages (4-6 hours)

This is the biggest single move on the entire plan.

**Tour pages to do:**
1. `/kayak-tours/cave-point-county-park/` (Cave Point 2-hour)
2. `/kayak-tours/cave-point-whitefish-dunes-half-day-kayak-tour/` (half-day Cave Point — push half-day per memory)
3. `/kayak-tours/door-bluff-county-park-shipwreck/`
4. `/kayak-tours/eco-estuary-tour/`
5. `/kayak-tours/cana-island-lighthouse-kayak-tour/` (1,378 imp pos 10.8 — sleeper)
6. (whatever other tour pages are live — check the kayak-tours hub)

**Plus:** Build the missing `/kayak-tours/deaths-door-shipwreck-bluff/` page (currently 404 — AI is summarizing this offering and we have nowhere to land the citation).

**Paste-ready Tour schema template** (Cave Point example — adapt for each tour using verified pricing per memory `reference_dckt_pricing.md`):

```json
{
  "@context": "https://schema.org",
  "@type": "TouristTrip",
  "name": "Cave Point County Park Kayak Tour",
  "description": "A 2-hour guided sit-on-top kayak tour of the limestone caves and 30-foot bluffs at Cave Point County Park along Lake Michigan in Jacksonport, Wisconsin. Beginner-friendly. Tour covers approximately 4 miles. Sit-on-top tandem kayaks, paddles, and PFDs included.",
  "image": "https://www.doorcountykayaktours.com/wp-content/uploads/sites/2281/2019/03/Cave-Point-County-Park-cover.jpg",
  "touristType": ["Beginner paddlers", "Families", "Couples", "First-time kayakers"],
  "itinerary": {
    "@type": "ItemList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Check-in and orientation at Schauer Park"},
      {"@type": "ListItem", "position": 2, "name": "Paddle technique lesson on calm water"},
      {"@type": "ListItem", "position": 3, "name": "Paddle along the Lake Michigan shoreline"},
      {"@type": "ListItem", "position": 4, "name": "Explore accessible caves at Cave Point (weather permitting)"},
      {"@type": "ListItem", "position": 5, "name": "Return paddle to launch point"}
    ]
  },
  "offers": {
    "@type": "Offer",
    "price": "[VERIFIED PRICE]",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-05-15",
    "validThrough": "2026-10-15",
    "url": "https://www.doorcountykayaktours.com/kayak-tours/cave-point-county-park/"
  },
  "provider": {
    "@type": "LocalBusiness",
    "@id": "https://www.doorcountykayaktours.com/#localbusiness"
  },
  "subjectOf": {
    "@type": "CreativeWork",
    "url": "https://www.doorcountykayaktours.com/kayak-tours/cave-point-county-park/"
  }
}
```

**Plus FAQPage block per tour** — 5-6 questions each (drawn from real common questions):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long is the Cave Point kayak tour?",
      "acceptedAnswer": {"@type": "Answer", "text": "The tour is 2 hours on the water, covering roughly 4 miles of Lake Michigan shoreline. Plan on 2.5 hours total including check-in and orientation."}
    },
    {
      "@type": "Question",
      "name": "Do I need kayaking experience?",
      "acceptedAnswer": {"@type": "Answer", "text": "No. The tour is built for first-time paddlers. We use sit-on-top tandems, which are stable and easy to learn. Your guide handles route choice and weather calls."}
    },
    {
      "@type": "Question",
      "name": "Is the Cave Point tour safe for kids?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes for kids 5 and up paired with an adult in a tandem. Children pair with a parent on the same kayak. Lake Michigan is cold even in July, and PFDs are required."}
    },
    {
      "@type": "Question",
      "name": "What's included with the tour?",
      "acceptedAnswer": {"@type": "Answer", "text": "Sit-on-top tandem kayak, paddle, and PFD are included. Dry bags and phone dry bags are sold separately at the shop. We do not provide spray skirts (sit-on-top tours don't use them)."}
    },
    {
      "@type": "Question",
      "name": "What if the weather is bad?",
      "acceptedAnswer": {"@type": "Answer", "text": "We monitor wind and wave forecasts daily. If conditions are unsafe, we'll move you to a calmer route, reschedule, or refund. Free cancellation up to 24 hours before your tour."}
    },
    {
      "@type": "Question",
      "name": "Where do we meet for the tour?",
      "acceptedAnswer": {"@type": "Answer", "text": "Schauer Park, just south of Cave Point County Park in Jacksonport, Wisconsin. Address and parking instructions are sent in your booking confirmation."}
    }
  ]
}
```

**Acceptance:** Each tour page has 3 schema blocks: existing `BreadcrumbList`, new `TouristTrip`, new `FAQPage`. Validates in Google Rich Results Test. Customer-facing FAQ section is also visible on the page (the schema and the visible content must match).

#### 1.4 Add `Article` + `FAQPage` to top 9 blog posts (3-4 hours)
Based on GSC click data, the priority order:

| Rank | URL | Imp/90d | Pos | Schema needed |
|------|-----|---------|-----|---------------|
| 1 | `/blog/embracing-kayaking-during-pregnancy/` | 13,339 | 2.6 | Fix existing + add FAQPage |
| 2 | `/blog/how-far-can-a-kayak-hang-out-of-a-truck/` | 14,910 | 2.9 | Article + HowTo + FAQPage |
| 3 | `/blog/different-types-of-kayaks-pros-and-cons/` | 10,388 | 7.9 | Article + ItemList comparison + FAQPage |
| 4 | `/blog/7-reasons-fish-creek-is-the-best-town-to-stay-at-in-door-county/` | 26,783 | 8.4 | Article + FAQPage about Fish Creek |
| 5 | `/blog/door-county-bike-routes/` | 3,126 | 7.2 | Article + ItemList of routes + FAQPage |
| 6 | `/blog/7-reasons-why-baileys-harbor/` | 9,543 | 10.9 | Article + FAQPage |
| 7 | `/blog/7-reasons-why-ephraim/` | 8,219 | 10.5 | Article + FAQPage |
| 8 | `/blog/boy-scout-girl-scout-kayaking-merit-badge-requirements/` | 235 | 6.1 | Article + HowTo (steps) |
| 9 | `/blog/how-to-kayak-and-prevent-blisters/` | 2,184 | 4.4 | Article + HowTo |

**Article schema template** (use the corrected pregnancy-post version above as the pattern). Author should be a real Person on staff with a verified bio page (per Authority section below).

#### 1.5 Verify sitemap (5 min)
Per robots.txt: `https://www.doorcountykayaktours.com/sitemap.xml`. Open it. Confirm all current tour pages and blog posts are listed. Confirm Death's Door page is added once it's built.

---

### Week 2 — Content (definition blocks + missing pages)

#### 2.1 Rewrite first paragraph of every tour page as a 40-60 word definition block

**Current Cave Point opener:**
> "Pictures can hardly do justice to the crystal waters and breathtaking natural beauty experienced while paddling along the rugged Wisconsin shoreline..."

**Replace with:**
> "The Cave Point Kayak Tour is a 2-hour guided sit-on-top kayak tour of the limestone caves and 30-foot bluffs at Cave Point County Park in Jacksonport, Wisconsin. Tours launch from Schauer Park, cover roughly 4 miles of Lake Michigan shoreline, and are suitable for first-time paddlers. Tandem kayaks, paddles, and life jackets included."

**Acceptance criteria for every tour-page opener:**
- 40-60 words.
- Names the tour, duration, launch point, town, state.
- Names 2-3 specific landmarks visited.
- States skill level explicitly.
- States what's included.
- No marketing adjectives ("breathtaking," "crystal," "stunning") in this paragraph — those are unextractable.
- Keep the marketing prose, but move it to paragraph 2+.

Apply across: Cave Point, half-day Cave Point, Door Bluff, Eco Estuary, Cana Island, Death's Door, plus any others on the kayak-tours hub.

#### 2.2 Add visible FAQ section to each tour page
The schema and the visible content must match. Use the same 5-6 questions from the FAQPage schema block above. Render as expandable `<details>` blocks or a clean Q&A list.

#### 2.3 Build Death's Door tour landing page
Currently 404. AI is already summarizing this as a DCKT offering. Build the page at `/kayak-tours/deaths-door-shipwreck-bluff/` with:
- 40-60 word definition block opener
- Tour details (duration, price, launch point)
- The verified Native American history per memory `reference_deaths_door_history.md` — Potawatomi + Ho-Chunk battle, mid-1600s, sourced
- TouristTrip + FAQPage schema
- Internal links to Cana Island and Door Bluff Shipwreck pages
- Half-day upsell module per memory rule

Also: Bill Quackenbush (Ho-Chunk THPO, per memory `reference_ho_chunk_nation_contact.md`) was contacted 2026-05-06. If he's responded, fold any cultural sensitivity feedback in before publishing.

#### 2.4 Add ACOG citation to pregnancy post
One sentence: "The American College of Obstetricians and Gynecologists' guidance on exercise during pregnancy is a useful baseline; the safe-paddling principles in this post align with their general framework. Always defer to your own provider."

Link target: `https://www.acog.org/womens-health/faqs/exercise-during-pregnancy`

That single citation is worth a meaningful AI-citation lift on a post already at position 2.6.

#### 2.5 Publish town pillar pages
Per memory `project_town_pillars_buildout.md`, three pillars (Baileys Harbor, Fish Creek, Ephraim) were drafted in `SEO Content/Towns/` and not yet published. GSC shows the existing 7-reasons posts still ranking pos 10-12 for those town queries — confirms they're not live.

Publishing them with FAQPage schema is the single biggest move for the ~7,000 monthly impressions currently leaking on town queries. Don't change slugs (per memory feedback).

---

### Weeks 3-4 — Authority and presence

These are slower but compound longer.

#### 3.1 Create author/guide bio pages with `Person` schema
Author attribution lifts AI citation +25-30% per Princeton GEO. Need 2-4 named guide bios with:
- Name, photo, years guiding, areas of expertise
- Only verified credentials (per memory: NOT ACA certified — do not claim)
- `Person` schema on each bio page
- Reference these `Person` URLs as `author` on Article schema

#### 3.2 Wikipedia edit
The Door County, Wisconsin Wikipedia article has zero kayak operator mentions. ChatGPT cites Wikipedia for ~7.8% of all responses. A neutral, encyclopedic edit listing 3-4 major outfitters (DCKT, Lakeshore, Kayak Guide Justin, CPPP) in the Recreation section is fair game.

**Approach:** Don't write or submit this from a DCKT account or IP. Brief Bella with the policy notes (advocacy edits get reverted; encyclopedic, sourced ones stick), or hire a contractor experienced with WP norms ($150-300 fixed-fee gig).

**Source to anchor the edit:** Travel Wisconsin and Destination Door County both list these operators publicly. Cite those.

#### 3.3 Tripadvisor consolidation
We have 3-4 fragmented listings:
- Egg Harbor (`d1036732`)
- Ellison Bay (`d12545584`)
- Sturgeon Bay (`d10319552`)
- Plus a Jacksonport listing referenced on Yelp

Reviews are split. AI cites Tripadvisor heavily for tour queries. Pick the strongest listing (most reviews) as canonical and submit merge requests for the others through Tripadvisor's "report duplicate" flow. This is a Bella ticket.

#### 3.4 Update Travel Wisconsin + Destination Door County listing copy
Both already list us. Refresh the listing descriptions to use the same 40-60 word definition format with named landmarks and 2026 pricing. These directories are AI training/citation source material and we own the listing copy.

#### 3.5 Plan one Reddit AMA
One genuine, guide-led "I guide kayak tours in Door County, AMA" post in r/wisconsin or r/Wisconsin_tourism during peak season (mid-June to early August). One real thread = months of AI citation surface. Don't astroturf. Don't mention DCKT first; let it surface in answers.

#### 3.6 GBP post FAQ-style content
GBP is already running 60 daily posts via launchd (per memory `project_gbp_daily_poster.md`). Add 6-8 FAQ-style posts to the calendar — Question headline, structured answer, internal link to the relevant tour page. GBP content shows up in AI Overviews for local queries.

---

### Months 1-3 — Compounding

#### 4.1 YouTube descriptions formatted for extraction
Per memory `project_youtube_launch.md`, the channel is launching, with Cave Point as video #1. Every upload description should be:
- 60-word summary (extractable)
- Tour facts table (duration, distance, price, launch)
- Timestamps
- 4-5 FAQ-style Q&A
- Links to the tour page and booking

AI Overviews cite YouTube heavily for "what to expect" and "how to" queries.

#### 4.2 Comparison page: DCKT vs Lakeshore Adventures
Comparison content gets ~33% of all AI citations across categories. Build a fair, structured comparison page with a real table covering: tour types offered, locations, kayak type (sit-on-top tandem vs. clear-bottom), group size, pricing, season window, what's included. Per memory `project_clear_bottom_positioning.md`, lead with the shipwreck story angle, not the kayak design.

URL: something like `/door-county-kayak-tours-vs-lakeshore-adventures/`

This captures branded competitor searches AND positions DCKT in AI answers when someone asks for the comparison.

#### 4.3 Outdoor publication pitches
One pitch per quarter:
- Q3 2026: Outside online — "What it's like to guide kayak tours in Door County"
- Q4 2026: Wisconsin Public Radio — local feature
- Q1 2027: Backpacker — paddling section
- Q2 2027: AAA Living or Midwest Living — regional feature

One feature in any of these = permanent AI citation source.

#### 4.4 Sleeper queries to push
GSC opportunities sitting on impressions but ranking page 2:

| Query | Imp/90d | Position | Move |
|-------|---------|----------|------|
| Cana Island | 1,378 | 10.8 | Refresh Cana Island lighthouse tour page; add definition block + FAQ schema |
| Whitefish Dunes State Park | 1,173 | 12.9 | Refresh the 7-reasons-Whitefish-Dunes post; add FAQ |
| Cave Point County Park | 1,503 | 16.5 | Schema + definition rewrite (covered in Week 1 + 2) |
| Door County wisconsin things to do | 128 | 13.3 | Build a true "Things to Do" hub page on DCKT — currently leaking to homepage |
| Things to do in Door County | 689 | 17.2 | Same hub |

Building one solid `/things-to-do-in-door-county/` hub page with sections (kayak, hike, eat, lodge, beach, lighthouse) and internal links = could capture hundreds of monthly impressions.

---

## Tracking

### Monthly check (first Monday of each month)

Run the 20 priority queries (listed in the audit doc) through ChatGPT, Perplexity, and Google AI Overview. Log in `Marketing/AI Visibility Tracker.md` as a sheet:

| Query | Month | ChatGPT cited? | Perplexity cited? | AIO present? | AIO cited DCKT? | Page cited |

After 3 months of manual data, evaluate paid tools:
- Otterly AI (~$60/mo)
- Peec AI (~$200/mo for multi-platform)
- ZipTie (~$100/mo)

Pick whichever has DCKT-relevant query coverage.

### Leading indicators (weekly)
- New schema blocks deployed
- New FAQ blocks added
- Pages with definition-block openers
- New third-party citations

### Lagging indicators (monthly)
- AI Overview presence rate on priority queries
- Brand citation rate vs. competitors
- Referral traffic from `chatgpt.com`, `perplexity.ai`, `google.com` AIO sources (GA4)
- GSC click-through rate on the modified pages

---

## Owner assignments (suggested)

| Track | Owner | Notes |
|-------|-------|-------|
| Schema rollout (Week 1) | Bella + contractor (or David) | Use the paste-ready templates above. Apply WP Schema Markup field rules per CLAUDE.md (no `<script>` wrap, no escaped quotes). |
| Content rewrites (Week 2) | David, with `/seo-blog-writer` + `/copy-mentors` skill stack | Per memory `feedback_skill_pipeline_seo_blog.md` — full draft then polish. Don't change slugs. |
| Death's Door page build | David (story input) → contractor (publish) | Wait for Bill Quackenbush response if pending; pull verified history from memory. |
| Town pillar publish | David (final review) → Bella (publish) | Drafts already exist per memory. |
| Wikipedia edit | Bella or contractor | Don't edit from DCKT IP. |
| Tripadvisor consolidation | Bella | Submit merge requests through Tripadvisor's flow. |
| Reddit AMA | One of the lead guides | Genuine, not promoted. |
| YouTube descriptions | Lea (per memory `project_lea_onboarding.md`) | Use the structured-description template. |
| Comparison page | David (positioning input) → contractor (build) | Apply clear-bottom positioning per memory. |
| Outdoor pitch | David | One per quarter. |
| Monthly tracking | Lea | Standardize the sheet format. |

---

## What I'd do this week if I had only 4 hours

1. **Fix homepage `LocalBusiness` schema** — add `aggregateRating` with 2,000+ reviews, fix address. (60 min)
2. **Add `TouristTrip` + `FAQPage` schema to Cave Point page** — the highest-traffic tour page. Use templates above. (90 min)
3. **Fix pregnancy-post schema** — date format + author + add FAQPage block. (45 min)
4. **Rewrite Cave Point tour page first paragraph** to the 40-60 word definition format. (30 min)

Even just those four moves shift the ceiling on the highest-traffic page on the site and make the LocalBusiness schema look credible to Google and AI tools. Everything else compounds from there.

---

## Open questions for David

1. Canonical address — Fish Creek 54212 (legal) or Jacksonport 6329 St Hwy 57 (physical tour ops)? Need to align homepage schema, GBP, Yelp, Tripadvisor, footer.
2. Specific lead-guide name to attribute as Person on Article schema and on bio pages.
3. Verified review count to use in `aggregateRating` (memory says 2,000+ but want exact).
4. Whether to consolidate Tripadvisor on Jacksonport or Egg Harbor (the strongest listing, whichever has the most/highest reviews).
5. Whether to publish town pillars this week or hold for editorial polish.
