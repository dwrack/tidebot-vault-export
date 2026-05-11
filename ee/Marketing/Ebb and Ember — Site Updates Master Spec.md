# Ebb and Ember — Site Updates Master Spec

*Merged 2026-05-10 from `SEO Quick Wins — May 2026.md` (May 9 audit) + `Jess Astrella — Site Updates Spec.md` (May 9 AI SEO audit). This is the canonical implementation doc for Jess Astrella and the Ebb and Ember team. Paired with `AI SEO — 90-Day Master Tracker.md` (dated weekly plan) and `Content Plan — 20 Blog Posts (Silos).md` (editorial calendar).*

---

## ✅ FAQ answers locked 2026-05-10

Davey confirmed 2026-05-10 that all four FAQ conflicts resolve in favor of the live /faq version. The FAQ schema in Section 4 and the live /faq answers should both match the answers below.

| FAQ | Locked answer (2026-05-10) |
|---|---|
| Q5 Do I need to be on time? | Sauna stays docked at all times, arrive anywhere within session window |
| Q7 What should I bring? / Q16 Towels and robes? | Nothing provided — guests bring swimsuit, two towels, water bottle |
| Q9 Are kids allowed? | 13+ on private bookings only with parent/guardian + signed waiver. Social sessions are 18+ |
| Q18 + Q19 Sauna type and temperature | Propane-fired (wet or dry depending on water on stones). Heats to 190°F, cycles back on at 170°F |

Schema `legalName: Elevated Tides Experiences LLC` is correct per public LLC structure and stays.

---

## TL;DR for Jess

We're consolidating two parallel docs into one. The work has three phases:

1. **Phase 1 (Week 1-2, May 11-24):** Schema overhaul, title/meta rewrites for 6 pages, FAQ schema, /shop label fix, /wellness → /experiences rename, homepage definition sentence. ~6-8 hours of your time, mostly Squarespace clicks and paste-in.
2. **Phase 2 (Week 3-6, May 25-Jun 21):** Five new cornerstone pages. I write the copy, you build the pages.
3. **Phase 3 (Week 7+, Jun 22 onward):** Add /journal blog, publish 20 long-form posts at 1/week for 5 months.

The 90-day master tracker (`AI SEO — 90-Day Master Tracker.md`) has dated week-by-week tasks with owners. This doc has the implementation detail behind each task. The 20-post editorial calendar (`Content Plan — 20 Blog Posts (Silos).md`) drives Phase 3.

---

# PHASE 1 — Foundation Sprint (Week 1-2, May 11-24)

## 1. Brand naming consistency

Standard per memory: **Ebb and Ember**. Always written out. Never "Ebb +", "Ebb &", or "&" in titles, descriptions, or schema.

Three places to fix:

### A. Site Title (Squarespace)
**Path:** Settings > Site Availability / Branding
If it reads "Ebb + Ember Floating Saunas" or "Ebb & Ember Floating Saunas", change to **Ebb and Ember Floating Saunas**. This propagates to the auto-generated WebSite and Organization schema blocks before we override them.

### B. Google Business Profile
Currently lists "Ebb & Ember Floating Saunas". Update at business.google.com to "Ebb and Ember Floating Saunas". Same edit on Facebook page name.

### C. Footer contact widget
Squarespace pulls the auto-injected schema from the footer contact widget block. Make sure the business name in that widget reads "Ebb and Ember Floating Saunas" with no ampersand or plus sign.

---

## 2. Title and meta description rewrites (6 pages)

**Path:** Pages > [each page] > SEO panel

**/ (Homepage)**
- Title: `Floating Sauna Portland | Ebb and Ember on the Columbia River`
- Meta: `Portland's floating sauna on the Columbia River. Cedar heat, snowmelt cold plunge, year-round sessions in North Portland. Book a social or private session.`

**/wellness** (will become /experiences in step 6)
- Title: `Sauna Experiences Portland | Banya, Movement & Meditation on the River`
- Meta: `Guided movement, meditation, and Banya sessions on the dock followed by a full sauna and cold plunge on the Columbia. Small groups, real instructors, Portland OR.`

**/memberships**
- Title: `Sauna Memberships Portland | Ebb and Ember Monthly Plans`
- Meta: `Monthly sauna memberships starting at $99 with guest passes, member rates on private sessions, and priority booking. Floating sauna on the Columbia River.`

**/faq**
- Title: `Floating Sauna FAQ | Ebb and Ember Portland`
- Meta: `Answers about sessions, cold plunge, river temperature, what to bring, and private bookings at Portland's floating sauna on the Columbia River.`

**/shop** (currently empty meta)
- Title: `Sauna Gift Cards Portland | Ebb and Ember Floating Saunas`
- Meta: `Give the gift of warmth. Sauna and cold plunge gift cards for Portland's only floating sauna on the Columbia River. Social and private sessions available.`

**/joinus**
- Title: `Newsletter | Ebb and Ember Floating Saunas`
- Meta: `Get session news, member-only events, and a monthly chance to win a free 120-minute floating sauna session in Portland.`

---

## 3. Override site-wide schema (HealthClub block)

**Critical context:** Squarespace silently injects three malformed schema blocks on every page (Organization with address-as-legalName, LocalBusiness with address-as-name, WebSite with empty description, wrong hours of 7am-5pm). We override with an explicit, complete HealthClub block via Code Injection. Google reconciles toward the more complete record.

**Path:** Settings > Advanced > Code Injection > Header

Paste this:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HealthClub",
  "@id": "https://www.ebbandember.com/#business",
  "name": "Ebb and Ember Floating Saunas",
  "alternateName": "Ebb and Ember",
  "legalName": "Elevated Tides Experiences LLC",
  "description": "Portland's floating sauna on the Columbia River. Cedar heat, snowmelt cold plunge, social and private sessions, year-round.",
  "url": "https://www.ebbandember.com/",
  "telephone": "+1-503-308-1293",
  "email": "sauna@ebbandember.com",
  "image": "https://images.squarespace-cdn.com/content/v1/690782c7287cf4635330dd1c/73464669-95db-4225-9aeb-660e068a1e3e/1%27x48%27_E%26E_LogoSign.png",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "173 NE Bridgeton Rd",
    "addressLocality": "Portland",
    "addressRegion": "OR",
    "postalCode": "97211",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 45.6118,
    "longitude": -122.6892
  },
  "hasMap": "https://maps.google.com/maps?cid=8740511744790975860",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      "opens": "07:00",
      "closes": "21:00"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/ebbandember/",
    "https://www.facebook.com/profile.php?id=61575154636279",
    "https://maps.google.com/maps?cid=8740511744790975860"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "86",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "Bill Ernst"},
      "datePublished": "2026-04-23",
      "reviewBody": "Fabulous water level Columbia river view as you lay back on beautifully crafted cedar benches and relax in the heat. Dunk in the river or shower off to cool down and repeat."
    },
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "byronfears"},
      "datePublished": "2026-04-30",
      "reviewBody": "What a wonderful relaxing and cleansing experience. First class amenities, heated floors, beautiful sauna with fantastic view of the marina, cold plunge in the Columbia River."
    },
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "Leilah Be"},
      "datePublished": "2026-04-23",
      "reviewBody": "Amazing and so restorative. Looking out over the Columbia river while in the sauna was sublime. Three in our group went into the river. I will return and bring more friends along too."
    }
  ]
}
</script>
```

**Google policy note on Review schema:** Any reviews shown in Review schema must be **visible on the page** where the schema lives. Two paths:

- **Path A (recommended):** Add a Testimonials section to the homepage with these same three quotes shown to visitors, attributing each by name and date. Keep the schema text identical to the on-page text. Great social proof anyway.
- **Path B:** If a homepage testimonial block isn't going in right now, remove the `review` array from the schema above and keep only `aggregateRating`. AggregateRating is safer without a visible block but Google still prefers it to map to something on-page.

**Verify after deploying:** Paste homepage URL into <https://search.google.com/test/rich-results>. Want to see "HealthClub" detected, all fields green.

---

## 4. FAQ schema on /faq

**Critical:** Confirm the five FAQ conflicts at the top of this doc before pasting. The version below uses the live /faq site answers as of 2026-05-09. If any of those answers have changed (e.g. robes are now provided), update both the live FAQ page AND this schema to match.

**Two prep edits to the live FAQ first:**

### A. Fix the broken Q23
Current Q23 reads: *"I have a different amount of people coming to my private and want to make sure i'm getting the door code."* This looks like an internal note that leaked into production. Replace with:

> **Q: What if my private booking party size changes?**
> A: Reach out to us at sauna@ebbandember.com or (503) 308-1293 as soon as you know. We'll update the booking and make sure your door code and headcount are sorted before your session.

### B. Fix Q1's location answer to include "North Portland"
The "sauna near me" keyword ranks position 7.9 with 351 impressions per GSC. Adding "North Portland" and "Hayden Island" to Q1's answer helps capture neighborhood-level searches.

### Now paste the schema

**Path:** Pages > /faq > Page Settings (gear icon) > Advanced > Page Header Code Injection. Page-level, not site-level.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Ebb and Ember?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ebb and Ember is Portland's first floating sauna, a Norwegian-inspired sauna boat moored on the Columbia River at Elevated Tides Marina in North Portland. We offer social and private sessions daily, plus four monthly membership tiers."
      }
    },
    {
      "@type": "Question",
      "name": "Where is Ebb and Ember located?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We are at 173 NE Bridgeton Rd in North Portland, Oregon, on the Columbia River just south of Hayden Island at Elevated Tides Marina. Free parking is available and signage guides you through the floating home village to the sauna boat."
      }
    },
    {
      "@type": "Question",
      "name": "What are the sauna hours?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We are open daily from 7:00 AM to 9:00 PM. Sessions are 1 hour 45 minutes."
      }
    },
    {
      "@type": "Question",
      "name": "How hot does the sauna get?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our propane sauna heats up to 190°F and then turns off. At 170°F it kicks back on, so the temperature stays in a comfortable range throughout your session."
      }
    },
    {
      "@type": "Question",
      "name": "How many people fit in the sauna at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "8 guests for a social session, and up to 10 for a private session."
      }
    },
    {
      "@type": "Question",
      "name": "What kind of sauna is it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is a propane-fired sauna that can be wet or dry depending on whether you add water to the stones."
      }
    },
    {
      "@type": "Question",
      "name": "What does social sauna mean?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Social sauna means a shared, communal experience with other guests. Up to 8 people share the sauna at once. Conversation is welcome but quieter, mindful energy is encouraged."
      }
    },
    {
      "@type": "Question",
      "name": "What should I bring?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bring a swimsuit, two towels (one to sit on, one to dry off), and a non-metallic water bottle. Towels and robes are not currently provided."
      }
    },
    {
      "@type": "Question",
      "name": "Are towels and robes provided?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We do not currently provide towels or robes. Please bring your own."
      }
    },
    {
      "@type": "Question",
      "name": "Is there somewhere to change and store my belongings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We have lockers and two heated changing rooms with hooks, storage cubbies, and heated floors."
      }
    },
    {
      "@type": "Question",
      "name": "Are there showers and bathrooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Freshwater showers are available on the boat (no soap allowed). Full bathroom and heated-floor shower facilities are in the on-shore lounge."
      }
    },
    {
      "@type": "Question",
      "name": "Can I plunge into the river?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Columbia River is over 40 feet deep at our dock. Two ladders, two throw rings, and life jackets are on board. The cold plunge is always optional, and a cold shower is available if you prefer. Always plunge with a buddy, never alone."
      }
    },
    {
      "@type": "Question",
      "name": "Can I come if it is raining?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Rain and mist only enhance the experience. The sauna is fully enclosed and stays warm year-round."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to be on time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The sauna stays docked at all times, so you can arrive anywhere within your booked session window."
      }
    },
    {
      "@type": "Question",
      "name": "Are kids allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Children ages 13 and older are welcome on private bookings only, with a parent or legal guardian present and a signed waiver. Social sessions are for guests aged 18 and older."
      }
    },
    {
      "@type": "Question",
      "name": "What if I am pregnant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Please consult your physician before sauna use during pregnancy. You are welcome to enjoy the boat exterior, lounge, and rooftop without using the sauna interior."
      }
    },
    {
      "@type": "Question",
      "name": "Are pets allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pets are not allowed on the sauna boat. Internal sauna temperatures of 160-195°F are unsafe for animals. ADA-recognized service animals are permitted in the lobby and lounge areas only."
      }
    },
    {
      "@type": "Question",
      "name": "Can we bring food or snacks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Snacks are welcome on the rooftop and in the on-shore lounge. Inside the sauna, only water is permitted. No alcohol."
      }
    },
    {
      "@type": "Question",
      "name": "Is there outdoor space to hang out?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The boat has a rooftop deck and a covered lounge with a bathroom, shower, hangers, and shoe cubbies. Both are great spots to cool down between rounds in the sauna."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get a refund?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All sales are final. Cancellations result in a gift card for the value of the booking, which can be applied to a future session."
      }
    },
    {
      "@type": "Question",
      "name": "How do I change my booking time or day?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Log into your Periode account and reschedule directly. Changes must be made at least 24 hours before your session. For help, email sauna@ebbandember.com."
      }
    },
    {
      "@type": "Question",
      "name": "Do you have a lost and found?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Items left and not retrieved will be donated after 2 weeks. Email sauna@ebbandember.com if you left something behind and we will check."
      }
    },
    {
      "@type": "Question",
      "name": "What is the Columbia River temperature like year-round?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Columbia runs around 42°F in winter, climbs into the 50s in spring, reaches the mid 60s in summer, and cools back down through fall. It is Cascade snowmelt, so the temperature shifts with the seasons."
      }
    },
    {
      "@type": "Question",
      "name": "What if my private booking party size changes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reach out at sauna@ebbandember.com or (503) 308-1293 as soon as you know. We will update the booking and make sure your door code and headcount are sorted before your session."
      }
    }
  ]
}
</script>
```

Per Davey's note: do NOT escape inner quotes (`\"`) in any string. Squarespace strips the backslash silently and breaks the JSON. All inner quotes in this block have been reworded.

**Validate after publishing:** <https://search.google.com/test/rich-results> with `https://www.ebbandember.com/faq`. Want to see FAQPage detected with 23 items.

---

## 5. Fix /shop gift card label inversion (P0 commerce bug)

Current state on /shop:
- "Social Sauna Gift Card — $539 per session" (accommodates up to 10 guests)
- "Private Sauna Gift Card — $59 per session" (one seat in shared session)

**The names are inverted.** $539 for up to 10 guests is the **private session**. $59 for one seat is the **social session**.

**Corrected labels (Squarespace > Commerce > Products):**
- **Private Sauna Gift Card — Portland Floating Sauna for up to 10 Guests** — $539, accommodates up to 10
- **Social Sauna Gift Card — Portland Floating Sauna Drop-in** — $59 per seat

This is a paying-customer bug, not just SEO. Highest urgency on the list.

---

## 6. /wellness → /experiences URL rename

**Path:** Pages > /wellness > Page Settings > URL slug

- Nav label: `Wellness` → `Experiences`
- URL slug: `/wellness` → `/experiences`

When the URL slug changes, Squarespace usually auto-creates a 301 redirect. Verify by visiting `https://www.ebbandember.com/wellness` after the change — should redirect, not 404. If it 404s, add a manual redirect at Settings > Advanced > URL Mappings:

```
/wellness -> /experiences 301
```

Once renamed, also update:
- Title and meta description (Section 2 above)
- All internal links pointing to /wellness in body copy
- Resubmit sitemap.xml in GSC after Squarespace regenerates it

---

## 7. Homepage definition sentence

**Why:** AI extracts the first informative paragraph. Current H1 is "Relax & Recharge" with poetic hero copy that contains zero entity-defining specifics. AI doesn't know what to extract.

**Add this single sentence directly under the H1, before the existing hero copy:**

> Ebb and Ember is Portland's first floating sauna, a Norwegian-inspired sauna boat moored on the Columbia River at Elevated Tides Marina, offering 1 hour 45 minute social and private sessions daily.

Keep existing brand copy ("Slow down, breathe deeply...") below it. Substance first, voice second. This sentence gets extracted verbatim by ChatGPT, Perplexity, and Google AI Overviews when someone asks "What is Ebb and Ember?"

---

## 8. Verify ebbandember.com in Google Search Console

**Path:** https://search.google.com/search-console (Davey's Google account)

Add property as `sc-domain:ebbandember.com`. Verify via DNS TXT record at the registrar. 48 hours for data to populate.

---

## 9. Resubmit sitemap and request indexing

After all Phase 1 changes are live:

1. **Resubmit sitemap in GSC.** Search Console > Sitemaps > enter `sitemap.xml` and submit again.
2. **Run URL Inspection** in GSC on /, /faq, /memberships, /shop, /experiences. Click "Request Indexing" on each.
3. **Validate schema** at <https://search.google.com/test/rich-results> for home and /faq.
4. **Check back in 2-3 weeks** on GSC for CTR lift on /memberships, /shop, /experiences. Those were the lowest CTR pages, so they are the cleanest signal for whether the title and meta rewrites worked.

---

# PHASE 2 — Cornerstone Pages (Week 3-6, May 25-Jun 21)

Five pages. Davey writes copy with Claude Code assistance. Jess builds in Squarespace and wires SEO settings.

## P1. /about

**Why it matters:** AI cites pages with named authors, dates, origin stories. Currently /about returns 404 — biggest single content miss on the site.

**Decision locked 2026-05-09:** Attribute everything to "the team" rather than naming individual founders. Reason: Dustin Miller buyout is active adversarial negotiation. Reattribute after Dustin exit closes (see memory `project_about_page_attribution.md`).

**Structure:**
- H1: "About Ebb and Ember"
- Hero paragraph with definition (extractable for AI)
- "How It Started" section (Norway origin, 2026 launch)
- "How It Works" (Norwegian-inspired, propane-fired, capacity, location)
- "The Team" section (generic attribution, brief)
- Press wall (links to KGW, Time Out, Portland Monthly x2, Travel Oregon, Yahoo)
- "Visit Us" CTA

**SEO settings:**
- Title: `About Ebb and Ember | Portland's First Floating Sauna`
- Meta: `Ebb and Ember is Portland's first floating sauna, opened January 1, 2026 on the Columbia River. Norwegian-inspired design, propane-fired heat, year-round sessions.`
- URL: `/about`

## P2. /floating-sauna-portland

**Why it matters:** Owns the category. AI cites this for "Portland floating sauna" / "Columbia River sauna" / "boat sauna Portland" queries.

**Structure:**
- H1: "Portland's First Floating Sauna on the Columbia River"
- Definition paragraph (1-2 sentences, extractable)
- "What Is a Floating Sauna?" section
- "Why on the Columbia River?" section
- Specifications block (vessel, dock location, temperature, capacity, session length, pricing)
- "What to Expect" section
- FAQ block (5-6 questions, with FAQPage schema added separately via page-level Code Injection)
- Direct booking CTA

**SEO settings:**
- Title: `Floating Sauna in Portland | Ebb and Ember on the Columbia River`
- Meta: `Portland's first floating sauna, located on the Columbia River at Elevated Tides Marina. Norwegian-inspired design, social and private sessions, daily 7am-9pm.`
- URL: `/floating-sauna-portland`

## P3. /sauna-experiences-portland (comparison guide)

**Why it matters:** Comparison content gets ~33% of all AI citations. Fair, balanced comparison of Portland sauna options gets cited by AI even when we are one of the options. AI penalizes biased comparisons.

**Structure:**
- H1: "Portland Sauna Guide: A Local's Comparison of the Best Sauna Experiences"
- Intro defining what makes a great Portland sauna experience
- Comparison table (name, location, type, capacity, price range, booking model, distinctive feature)
- Short profile of each (3-4 sentences, fair, balanced) — include Knot Springs, Löyly, Common Ground, SaunaGlo, Cascada, Bear Banya, Koti, Guss, Pure Sweat, us
- "Best for ___" section (best for first-timers, groups, cold plunge enthusiasts, date night, etc.)
- Last updated date visible
- Author byline

**SEO settings:**
- Title: `Best Saunas in Portland: A Local's Honest Guide (2026)`
- Meta: `Comparing Portland's best sauna experiences in 2026: Ebb and Ember, Knot Springs, Löyly, Common Ground, SaunaGlo, and more. Type, price, capacity, vibe.`
- URL: `/sauna-experiences-portland`

> Note: this overlaps with the existing /wellness page, which is becoming /experiences. Decision: /experiences is the conversion page (Banya, movement, meditation, paid sessions). /sauna-experiences-portland is the editorial guide page (informational, AI citation magnet, links to /experiences for conversion).

## P4. /cold-plunge-portland

**Why it matters:** Cold plunge is the wellness trend of 2025-2026. You have a year-round natural cold plunge (Columbia River) which is unique among Portland competitors. Educational content with citable science gets +40% AI citation lift.

**Structure:**
- H1: "Cold Plunging in Portland: A Practical Guide"
- Intro definition
- "What Cold Plunging Does" (cite peer-reviewed research)
- "Columbia River Cold Plunge" (your differentiator)
- "River Temperature by Month" table (NOAA-sourced, member observations)
- "Safety Guide" (existing FAQ content expanded)
- "Where to Cold Plunge in Portland" (you + competitors honestly)
- Booking CTA

**SEO settings:**
- Title: `Cold Plunge Portland | Year-Round on the Columbia River`
- Meta: `Cold plunging in Portland. Columbia River temperatures month-by-month, safety guide, science-backed benefits. Cold plunge access at Ebb and Ember.`
- URL: `/cold-plunge-portland`

> Note: The blog post `Marketing/Blog — Cold Plunge Portland FAQ.md` already exists in the vault. Decide whether that becomes this cornerstone page (recommended) or a supporting blog post. They serve different functions — cornerstone is the definitive guide, blog post is the topical follow-up.

## P5. /private-sauna-rental-portland

**Why it matters:** Highest commercial intent of any page on the site. Bachelorette, birthday, team retreat queries lead here at full price.

**Structure:**
- H1: "Private Sauna Rental on the Columbia River"
- Intro: "Book the entire floating sauna for your group of up to 10."
- Use cases: birthdays, bachelorettes, team retreats, wedding parties, dates
- What's included (full boat, rooftop, sauna, lounge access, door code, 1h 45m)
- Pricing (off-peak $449, peak $539)
- Booking CTA + member benefits (guest pass discounts)
- Group FAQ block (private rental specifics, FAQ schema via Code Injection)

**SEO settings:**
- Title: `Private Sauna Rental in Portland | Up to 10 Guests`
- Meta: `Rent the entire floating sauna for your group of up to 10. Private sessions for birthdays, bachelorettes, team retreats. From $449 off-peak.`
- URL: `/private-sauna-rental-portland`

---

## Internal linking pass after Phase 2 pages exist

1. Homepage links down to: /about, /floating-sauna-portland, /sauna-experiences-portland, /cold-plunge-portland, /book, /memberships, /private-sauna-rental-portland
2. Every cornerstone page links to /book and to two sibling cornerstones
3. /faq links to /floating-sauna-portland for "what is" questions
4. Navigation menu restructure: Home | About | Experience [dropdown: Floating Sauna, Cold Plunge, Private Rental] | Sauna Guide | Memberships | FAQ | Book
5. Footer gets all cornerstone links

Separate doc with the full list of 18 specific link additions queued at `Marketing/SEO Internal Linking Edits (For Later).md`. Pull from that doc during the internal linking pass.

---

# PHASE 3 — Blog Engine + Distribution (Week 7+, Jun 22 onward)

## Blog setup (Week 7, June 22-28)

Site has no blog as of 2026-05-10. Add it before content publishing starts.

**Setup:**
- Pages > + Add Page > Blog
- Section name: "Notes" or "Journal" (avoid "Blog" — too generic). Davey to decide.
- URL slug: `/notes` or `/journal`
- Default author: Davey Rack (or rotating per post)
- Categories: Sauna Education, Cold Plunge, Portland Things to Do, Private Events, Wellness Lifestyle (matches the 5 silos from `Content Plan — 20 Blog Posts (Silos).md`)
- Comments: off
- RSS: on (for feed readers and AI ingestion)

**Per-post settings (template Davey + Jess work through together at kickoff):**
- SEO title (Page Settings > SEO)
- Meta description (155 chars max)
- Featured image with descriptive filename (e.g., `what-to-wear-to-a-sauna-portland.jpg` not `IMG_0042.JPG`)
- Alt text on all images
- Last updated date visible
- Internal links wired before publishing

## Editorial calendar

20 blog posts over 20 weeks. Full calendar with target queries, internal linking, AI extraction angle for each post: `Marketing/Content Plan — 20 Blog Posts (Silos).md`.

Five silos:
1. Sauna Education (5 posts) → pillar /floating-sauna-portland
2. Cold Plunge & Contrast Therapy (4 posts) → pillar /cold-plunge-portland
3. Portland Things to Do (5 posts) → pillar /things-to-do-portland (new pillar)
4. Group & Special Occasion (3 posts) → pillar /private-sauna-rental-portland
5. Portland Wellness Lifestyle (3 posts) → pillar /sauna-experiences-portland

Vault draft `Marketing/Blog — Cold Plunge Portland FAQ.md` is the first publishable post (Silo 2). Reuse or repurpose as needed.

---

# Google Business Profile audit

Pulled the GBP listing 2026-05-09. Full IDs and metrics in memory `reference_ebb_ember_gbp.md`.

### What's right
- Title: "Ebb & Ember Floating Saunas" (needs the brand update per Section 1.B)
- Hours: Daily 7am-9pm
- Address, phone, website all correct
- 86 reviews, 4.90 average, 98% reply rate
- Voice of merchant verified

### What's missing or wrong

| Issue | Action |
|---|---|
| Only one category set ("Sauna") | Add: Wellness center, ideally Spa or Tour operator |
| No serviceItems list | Add: Social Sauna Session ($49-$59), Private Sauna Rental ($449-$539), Memberships (Ember 1 / Ember 2), Banya Mondays |
| No special hours configured | Set holiday hours for Memorial Day, July 4, Thanksgiving, Christmas, NYE |
| Zero GBP posts published | Start 2x/week cadence. AI Overviews read GBP posts directly. |
| Q&A not seeded | Seed 8-10 questions answered by the business (manual in Google's interface — API deprecated) |
| Photos catalog unaudited | Audit count, freshness, alt context. Aim for 30+ photos. |
| One 3★ unanswered review (Aubrey, 2026-02-22) | **P0 — Davey or Hannah reply this week** with empathy + what's changed |

---

# Review intelligence (sampled 50 of 86 reviews on 2026-05-09)

## Top 5 themes (use as marketing copy)
1. Heated floors in changing/bathroom areas
2. Cold plunge directly into the Columbia River
3. Panoramic river views from inside the sauna
4. Easy parking, well signed, "wander through a quaint floating home village"
5. Intentional design, attention to detail

## Testimonial quotes ready to publish (use on /about, /floating-sauna-portland, home page)

> "I celebrated my anniversary here tonight. A sauna on the river! Epic views at sunset. The attention to detail on the wood work and lighting was impressive." — Mel, January 2026

> "Huge windows welcome panoramic views of the river. Keep your eyes peeled for wildlife. We saw bald eagles fishing in the water nearby — absolutely stunning sight." — j ai, February 2026

> "Fabulous water level Columbia river view as you lay back on beautifully crafted cedar benches and relax in the heat. Dunk in the river or shower off to cool down and repeat." — Bill Ernst, April 2026

> "To just watch the ripples on the water of the majestic Columbia River while I sweat out my tensions inside the well designed, clean sauna space, was such a perfect way to end my day. I'm ready for the membership now!" — Phyllis, January 2026

> "It was the perfect mix of peaceful and luxurious. I left feeling completely refreshed and grounded." — Madison K, January 2026

(Three of these — Bill, byronfears, Leilah Be — are already in the override HealthClub schema in Section 3.)

## Operational signals (turn into FAQ + page copy)

| Signal | Action |
|---|---|
| First-timer plunge supervision worries | Add to /cold-plunge-portland: explicit "buddy system" + life ring locations |
| Strong upstream current — one family had to be rescued | /cold-plunge-portland River Safety section |
| Loud-group social etiquette complaints | Add FAQ: "What is social sauna etiquette?" + push Silent Tuesday when launched |
| Single bathroom limitation | Mention in /private-sauna-rental: private books the entire boat |
| Lone-traveler safety concern (Aubrey review) | Reply to Aubrey + add "Is it safe to visit alone?" FAQ |
| Peak weekend availability tight | Reinforce member priority booking in /memberships and /sauna-experiences-portland |

---

# Implementation order (paired with `AI SEO — 90-Day Master Tracker.md`)

| Week | Phase | Owner | Tasks |
|---|---|---|---|
| W1 (May 11-17) | Phase 0 prep | Davey | Reply to Aubrey 3★ review; verify GSC; baseline AI visibility check; PageSpeed audit |
| W2 (May 18-24) | Phase 1 | Jess + Davey | Kickoff sit-down; Sections 1-9 of this doc all live |
| W3 (May 25-31) | Phase 2 | Davey + Jess | /about + /floating-sauna-portland (P1, P2) |
| W4 (June 1-7) | Phase 2 | Davey + Jess | /sauna-experiences-portland research + draft (P3) |
| W5 (June 8-14) | Phase 2 | Jess + Davey | /sauna-experiences-portland live; internal linking pass; /press page |
| W6 (June 15-21) | Phase 2 | Davey + Jess | /cold-plunge-portland + /private-sauna-rental-portland (P4, P5) |
| W7 (June 22-28) | Phase 3 setup | Jess + Davey | Blog section added; Post 1.5 First Time at a Sauna live; first repurpose pass |
| W8+ | Phase 3 weekly | Davey + Jess + Hannah | 1 blog post per week per editorial calendar; 2 GBP posts/wk |

Full week-by-week breakdown with owners and risk register in `AI SEO — 90-Day Master Tracker.md`.

---

# Open decisions for the kickoff sit-down with Jess

1. Confirm the 5 FAQ conflicts at the top of this doc (live answers vs Quick Wins draft answers)
2. Squarespace plan tier — does current plan support all Code Injection / SEO field features needed?
3. Dustin attribution timeline — when is "the team" revisited (after buyout closes)?
4. Photo library access — does Hannah/Jess have a centralized library with rights cleared?
5. Author bylines — Davey only, or rotating? Member-contributed posts? Affects BlogPosting schema.
6. Periode UTM convention (utm_source, utm_medium, utm_campaign naming standard)
7. Press page — separate page or section of /about?
8. Membership pages — single page or one per tier?
9. Banya Mondays page — its own page or section under /private-sauna-rental-portland?
10. Themed weekday sessions (Silent Tuesday, Women's Wednesday) — own pages or section under /experiences?
11. Blog section URL slug — /journal or /notes?
12. Testimonials on homepage — Path A (add visible block) or Path B (remove `review` array from schema)?

---

# Saved for later (Phase 4+)

- Build /banya-mondays page (queued)
- Build /our-story page from Brand Story doc (note: maybe redundant with /about)
- Build /cold-plunge money page (covered by P4 above)
- 18 specific internal link additions (held in `Marketing/SEO Internal Linking Edits (For Later).md`)
- Wikipedia page push (need Mack to find experienced editor)
- 3-5 min YouTube walkthrough video
- Programmatic comparison pages (you-vs-Knot-Springs as standalone)
- Paid media layer (Google Ads, Meta tied to high-converting cornerstones)
- Conde Nast Traveler / Travel + Leisure / Outside pitch (Mack-led)

---

# Reference data

## GBP IDs (memory: `reference_ebb_ember_gbp.md`)
- Account ID: `109075056374613070632`
- Location ID: `16140834048343808850`
- Place ID: `ChIJN9ib_RinlVQRdFVlZx-JTHk`
- Maps CID: 8740511744790975860
- New review URL: https://search.google.com/local/writereview?placeid=ChIJN9ib_RinlVQRdFVlZx-JTHk

## Site stack (memory: `reference_ebb_ember_site_stack.md`)
- Squarespace
- Schema auto-injected from footer contact widget (see `reference_squarespace_schema_bug.md`)
- robots.txt explicitly allows GPTBot, ClaudeBot, anthropic-ai, Google-Extended, CCBot
- Brand renders "Ebb & Ember" on live site; preferred spelling is "Ebb and Ember"

## Press citations (use for /about and /press)
- Portland Monthly (Feb 2026): https://www.pdxmonthly.com/health-and-wellness/2026/02/portland-oregon-river-floating-sauna
- Portland Monthly (Best Saunas): https://www.pdxmonthly.com/health-and-wellness/saunas-spas-portland
- Time Out USA: https://www.timeout.com/usa/news/portlands-new-floating-sauna-is-the-best-and-sweatiest-way-to-warm-up-and-socialize-this-winter-021326
- KGW: https://www.kgw.com/article/news/local/portland-floating-sauna-opens-columbia-river/283-926d85f7-8b06-41d9-85ff-438fa88f27de
- Travel Oregon: https://traveloregon.com/things-to-do/sauna-getaways-in-oregon/
- Yahoo Lifestyle: https://www.yahoo.com/lifestyle/articles/warm-maybe-jump-river-floating-140051010.html
- Tripadvisor: https://www.tripadvisor.com/ShowUserReviews-g52024-d34042545-r1047131914-Ebb_and_Ember_Floating_Saunas-Portland_Oregon.html

---

*Source docs merged here: `Marketing/SEO Quick Wins — May 2026.md` + `Marketing/Jess Astrella — Site Updates Spec.md`. Both originals have been banner-noted as superseded.*
*Last updated: 2026-05-10 by Davey + Claude*
