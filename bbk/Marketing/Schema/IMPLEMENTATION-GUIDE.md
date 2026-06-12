# BBK Schema & Copy Fixes — Implementation Guide

All JSON files in this folder are ready to paste. **Do not add a script tag wrapper.** Paste raw JSON only into the Schema Markup ACF field. The theme adds the script tag automatically.

After each save, verify the schema is live: paste the page URL into Google's Rich Results Test (search.google.com/test/rich-results).

---

## Step 1 — Copy Fixes (do these first, fastest wins)

### Bat Tour H1
**Page:** /kayak-tours/houston-bat-bridge-kayak-tour/ > Edit in WP admin

**Current H1:** Sunset Skyline Bat Bridge Kayak Tour
**Replace with:** Houston Bat Bridge Kayak Tour

Also update the page title (SEO Title field) to: Houston Bat Bridge Kayak Tour | Buffalo Bayou Kayak

---

### About Page Meta Description
**Page:** /about/ > Edit in WP admin > SEO fields

The current meta is truncated because it has an apostrophe the theme strips. Replace with this (no apostrophes, 157 chars):

```
Buffalo Bayou Kayak offers guided kayak tours, paddleboard tours, and rentals on Buffalo Bayou in downtown Houston. Explore the bayou, see the skyline, and paddle to the Waugh Bridge bat colony.
```

---

### Houston Skyline Tour H1 / Title Mismatch
**Page:** /kayak-tours/houston-kayak-tour/

**Current page title:** "Kayaking in Houston City Tours"
**Current H1:** "Houston Skyline Tour"

These should match. Recommended:
- Page title: Kayaking in Houston | Houston Skyline Kayak Tour
- H1: Houston Skyline Kayak Tour

---

## Step 2 — Schema JSON-LD (paste into Schema Markup ACF field)

### Bat Tour
**Page:** /kayak-tours/houston-bat-bridge-kayak-tour/
**File:** bat-tour.json
- Product schema: $60/person, 2 hrs, ages 7+
- FAQPage: 5 questions (bat emergence times, colony size, experience required, price, seasonal availability)

---

### Houston Skyline Tour
**Page:** /kayak-tours/houston-kayak-tour/
**File:** skyline-tour.json
- Product schema: $55/person, 2 hrs, 10am/1pm
- FAQPage: 4 questions (what to see, duration, price, beginner safety)

---

### Sunrise Serenity Tour
**Page:** /kayak-tours/houston-serenity-tour/
**File:** serenity-tour.json
- Product schema: $55/person, 2 hrs, 7am
- FAQPage: 3 questions (wildlife, departure time, price)

---

### Full Moon Tour
**Page:** /kayak-tours/full-moon-tour/
**File:** full-moon-tour.json
- Product schema: $65 adult / $55 child, 2 hrs, 6pm
- FAQPage: 4 questions (frequency, safety at night, price, what to wear)

---

### Paddleboard Tour
**Page:** /kayak-tours/paddleboard-tour/
**File:** paddleboard-tour.json
- Product schema: $55/person, 2 hrs including 30-min lesson
- FAQPage: 4 questions (experience needed, difficulty, price, what to wear)

---

### Rentals
**Page:** /watersports-rental/
**File:** rentals.json
- Product schema: all 6 price tiers (1hr/2hr/full-day, single/tandem)
- FAQPage: 4 questions (pricing, pickup location, experience needed, ID required)

---

### FAQ Page
**Page:** /faq/
**File:** faq-page.json
- FAQPage schema only (21 questions)
- This schema alone covers all questions; no Product schema needed on this page
- The page content itself also needs to be expanded to match the schema. Add these questions to the visible page HTML (they do not show up in Google if they are only in schema but not on the page):
  - Are there alligators in Buffalo Bayou?
  - Is Buffalo Bayou safe to kayak?
  - What happens if it rains?
  - Can I bring food or drinks?
  - Where do I park?
  - Is tipping expected?
  - Can I bring my phone or camera?
  - What if I fall out of my kayak?
  - How physically fit do I need to be?
  - Can I book a private or group tour?
  - Are both single and tandem kayaks available?

---

## Step 3 — Alt Text Pass

Go to each tour page, open the featured/hero image in the WP media editor, and add the alt text below. These are currently blank.

| Page | Recommended Alt Text |
|------|----------------------|
| Bat Tour | kayakers paddling toward Waugh Drive Bridge at sunset with Houston skyline in background |
| Houston Skyline Tour | guided kayak tour on Buffalo Bayou with downtown Houston skyline at midday |
| Serenity Tour | early morning kayaking on Buffalo Bayou through downtown Houston at sunrise |
| Full Moon Tour | kayakers on Buffalo Bayou under a full moon with city lights reflecting on the water |
| Paddleboard Tour | beginner stand-up paddleboarding lesson on Buffalo Bayou with Houston skyline view |
| Rentals | single and tandem kayaks lined up at the Buffalo Bayou Kayak launch at 1019 Commerce Street |
| About | Buffalo Bayou Kayak guides with guests at the 1019 Commerce Street launch point in downtown Houston |
| FAQ | kayakers exploring Buffalo Bayou through Houston in sit-on-top kayaks |
| Homepage Hero | guided kayak tour on Buffalo Bayou with the Houston downtown skyline in the background |

---

## Step 4 — Internal Linking (after publishing new blog posts)

Every blog post must link to at least 2 tour pages with descriptive anchor text (not "click here"). Example anchors:
- "Houston bat bridge kayak tour" -> bat tour page
- "kayaking in Houston" -> skyline tour page
- "Buffalo Bayou kayak rental" -> rentals page

Every tour page should get a "From the Blog" widget linking to relevant posts. The bat tour page should link to the bat colony guide once published.

---

## Step 5 — GSC / GA4 / GBP (requires your action)

Cannot be done by Claude — requires you to grant access to the management Google account.

1. **Search Console:** Go to search.google.com/search-console > select the buffalobayoukayak.com property > Settings > Users and permissions > Add user > add the management account as Owner or Full User.

2. **GA4:** Go to analytics.google.com > Admin > Account Access Management > Add users > add the management account.

3. **GBP:** Confirm who owns the BBK GBP listing (the connected account is an unverified personal account). If it is your account, verify the listing and then grant access under Business Profile Manager. If you cannot find the listing, search for "Buffalo Bayou Kayak" in Google Maps and claim it.

---

## Google Ads — Already Done

Two BBK campaigns were reactivated on 2026-06-12:
- [FH] Search - Brand - Shname_buffalobayoukayak (brand protection, $15/day budget)
- [FH] Search - Generic - Shname_buffalobayoukayak - Local (generic Houston kayak queries, $15/day budget)

Both were previously paused. They are now ENABLED and spending.

---

## Google Ads — Houston Bat Campaign (build in Google Ads UI)

Create a new Search campaign named: [FH] Search - Generic - Shname_buffalobayoukayak - Bat - Local

**Settings:**
- Budget: $30/day
- Bidding: Maximize conversions (switch to Target CPA once 30+ conversions accumulated)
- Location: Houston, TX metro (use the Google Ads location targeting for Houston-The Woodlands-Sugar Land DMA or just Houston, TX)
- Network: Search only (uncheck Search partners if you want to start conservative)

**Ad Group: BBK - Bat**

Keywords (all Phrase match to start):
- "houston bat kayak tour"
- "waugh bridge bat tour"
- "bat bridge kayak tour houston"
- "kayak bat tour"
- "kayak bats houston"
- "houston bat bridge tour"
- "waugh drive bat colony tour"
- "see bats in houston"
- "bat tour houston"
- "houston bat tour kayak"
- "bat kayak tour houston"
- "kayak to see bats houston"

**Responsive Search Ad:**

Headlines (pin none - let Google test):
- See 250,000 Bats From a Kayak
- Houston Bat Bridge Kayak Tour
- Waugh Bridge Bat Colony Tour
- Sunset Bat Emergence on the Bayou
- Book the Houston Bat Kayak Tour
- Only Kayak Bat Tour in Houston
- $60 Per Person - Ages 7 and Up
- Evening Bat Emergence Tour
- Guided Bat Bridge Kayak Tour
- Watch 250K Bats Leave the Bridge

Descriptions:
- Paddle to Waugh Bridge and watch 250,000 bats emerge at dusk. $60/person, ages 7+. Book online.
- The only kayak-based bat experience in Houston. 2 hours, all skill levels welcome. Downtown launch.
- See the famous Waugh Drive bat colony from the water. Guided tour from 1019 Commerce St downtown.
- Watch 250,000 Mexican free-tailed bats emerge at sunset. Start at $60/person. Book your spot now.

**Final URL:** https://buffalobayoukayak.com/kayak-tours/houston-bat-bridge-kayak-tour/

Create the campaign in PAUSED status, review the ad copy and keywords, then enable when ready.
