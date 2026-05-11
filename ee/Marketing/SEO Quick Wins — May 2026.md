# SEO Quick Wins — May 2026

Source of truth for the high-leverage SEO fixes pulled out of the May 9 audit. Work through this top to bottom in Squarespace. Each section says exactly what to paste and where.

---

## 1. Update sitewide title and brand consistency

Brand standard per memory: **Ebb and Ember**. Always written out. Never "Ebb +", "Ebb &", or "&" in titles, descriptions, or schema.

Three places to fix the "+" / "&" inconsistency:

### A. Squarespace SEO settings (Pages → each page → SEO panel)

Use these exact title + meta description pairs. All written for SERP CTR with the keyword we already rank for.

**/ (Homepage)**
- **Title:** `Floating Sauna Portland | Ebb and Ember on the Columbia River`
- **Meta description:** `Portland's floating sauna on the Columbia River. Cedar heat, snowmelt cold plunge, year-round sessions in North Portland. Book a social or private session.`

**/wellness** (will become /experiences after step 8)
- **Title:** `Sauna Experiences Portland | Banya, Movement & Meditation on the River`
- **Meta description:** `Guided movement, meditation, and Banya sessions on the dock followed by a full sauna and cold plunge on the Columbia. Small groups, real instructors, Portland OR.`

**/memberships**
- **Title:** `Sauna Memberships Portland | Ebb and Ember Monthly Plans`
- **Meta description:** `Monthly sauna memberships starting at $99 with guest passes, member rates on private sessions, and priority booking. Floating sauna on the Columbia River.`

**/faq**
- **Title:** `Floating Sauna FAQ | Ebb and Ember Portland`
- **Meta description:** `Answers about sessions, cold plunge, river temperature, what to bring, and private bookings at Portland's floating sauna on the Columbia River.`

**/shop** (currently has empty meta description)
- **Title:** `Sauna Gift Cards Portland | Ebb and Ember Floating Saunas`
- **Meta description:** `Give the gift of warmth. Sauna and cold plunge gift cards for Portland's only floating sauna on the Columbia River. Social and private sessions available.`

**/joinus**
- **Title:** `Newsletter | Ebb and Ember Floating Saunas`
- **Meta description:** `Get session news, member-only events, and a monthly chance to win a free 120-minute floating sauna session in Portland.`

### B. Site Header → Site Title (Squarespace Settings)

If it reads "Ebb + Ember Floating Saunas" or "Ebb & Ember Floating Saunas" anywhere in **Settings → Site Availability / Branding**, change to **Ebb and Ember Floating Saunas**. This propagates to the auto-generated WebSite and Organization schema blocks.

### C. Google Business Profile

GBP currently lists "Ebb & Ember Floating Saunas". Update via the GBP MCP or directly at business.google.com to "Ebb and Ember Floating Saunas" to match brand standard. Same edit on Facebook page name.

---

## 2. Fix the broken auto-generated schema (critical)

Squarespace is silently injecting **three broken schema blocks** on every page right now. They tell Google:
- The legal name is "173 NE Bridgeton Rd" (it's the address, not a legal name)
- The LocalBusiness *name* is "173 NE Bridgeton Rd" (same bug)
- Hours close at 5pm (you close at 9pm per GBP)
- WebSite description is empty
- No category, no reviews, no geo, no price range

We override this by injecting a clean schema block via **Code Injection → Header** at site level. This adds correct schema on every page. Squarespace's broken auto-schema will still appear but Google reconciles them and the explicit one wins.

### Paste this into Squarespace → Settings → Advanced → Code Injection → Header

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
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Bill Ernst"
      },
      "datePublished": "2026-04-23",
      "reviewBody": "Fabulous water level Columbia river view as you lay back on beautifully crafted cedar benches and relax in the heat. Dunk in the river or shower off to cool down and repeat. This Sauna Rocks!"
    },
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "byronfears"
      },
      "datePublished": "2026-04-30",
      "reviewBody": "What a wonderful relaxing and cleansing experience! First class amenities, heated floors, beautiful sauna with fantastic view of the marina, cold plunge in the Columbia River."
    },
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "Leilah Be"
      },
      "datePublished": "2026-04-23",
      "reviewBody": "Amazing and so restorative. Looking out over the Columbia river while in the sauna was sublime. Three in our group went into the river. I will return and bring more friends along too."
    }
  ]
}
</script>
```

### Important Google policy note on Review schema

Google requires that any reviews shown in Review schema be **visible on the page** where the schema lives. To stay compliant and avoid manual penalty risk:

**Add a Testimonials section to the homepage** with these same three quotes shown to visitors, attributing each by name and date. It's also great social proof. Keep the quoted text in the schema identical to what visitors see.

If you'd rather not add a visible testimonials block right now, **remove the `review` array from the schema above** and just keep `aggregateRating`. AggregateRating is safer to include without a visible block, though Google still prefers it to map to something on-page.

### Verify after deploying

Paste your homepage URL into Google's Rich Results Test: <https://search.google.com/test/rich-results>. You want to see "HealthClub" detected with all fields green. Same for the FAQ page after the next step.

---

## 3. Add FAQ schema to /faq

This unlocks rich snippets in SERPs (expandable Q&A rows under your listing). With 23 well-written questions, this is one of the highest-ROI fixes on the site.

Two prep edits first:

### A. Fix the broken Q23

Current Q23 reads: *"I have a different amount of people coming to my private and want to make sure i'm getting the door code."* This looks like an internal note that leaked into production. Replace with:

> **Q: What if my private booking party size changes?**
> A: Reach out to us at sauna@ebbandember.com or (503) 308-1293 as soon as you know. We'll update the booking and make sure your door code and headcount are sorted before your session.

### B. Fix Q1's location answer to include "North Portland"

The "sauna near me" keyword ranks position 7.9 with 351 impressions. Adding "North Portland" and "Hayden Island" to Q1's answer helps capture neighborhood-level searches.

### Now add the FAQ schema

In Squarespace, go to **Pages → /faq → Page Settings (gear icon) → Advanced → Page Header Code Injection** and paste this. (Page-level, not site-level, so it only loads on /faq.)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is Ebb and Ember located?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We're at 173 NE Bridgeton Rd in North Portland, Oregon, on the Columbia River just south of Hayden Island. Free parking is available, and signage will guide you through the floating home village to the sauna boat."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get a refund?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We do not offer refunds. If you need to change your booking, you can reschedule through your Periode account up to 24 hours before your session."
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
      "name": "What are the sauna hours?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We run sessions seven days a week from 7am to 9pm. Sessions are 1 hour 45 minutes. Booking windows are managed through Periode."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to be on time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Sessions start on time and we cannot extend if you're late. Arrive 5 to 10 minutes early so you can change and settle in."
      }
    },
    {
      "@type": "Question",
      "name": "What does social sauna mean?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A social session is a shared session you book per seat, up to 8 strangers in one sauna. It's the most affordable way to experience the boat and a good way to meet other regulars."
      }
    },
    {
      "@type": "Question",
      "name": "What should I bring?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A swimsuit, a towel, and a water bottle. Everything else is provided. Robes, hooks, and a place to change are on the boat."
      }
    },
    {
      "@type": "Question",
      "name": "Can I come if it's raining?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The sauna runs in all weather. Rain on the deck and steam off the river is part of the experience."
      }
    },
    {
      "@type": "Question",
      "name": "Are kids allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Guests must be 16 or older. Anyone under 18 must be accompanied by a parent or guardian for the full session."
      }
    },
    {
      "@type": "Question",
      "name": "Is there anywhere to hang out outside?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The rooftop deck and lower outdoor platform are open during your session. Both are great spots to cool down between rounds in the sauna."
      }
    },
    {
      "@type": "Question",
      "name": "What if I am pregnant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Saunas are generally not recommended during pregnancy. Please check with your healthcare provider before booking, and let us know about any concerns."
      }
    },
    {
      "@type": "Question",
      "name": "Can I plunge into the river?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Columbia River is over 40 feet deep at our dock. Two ladders, two throw rings, and life jackets are on board. The cold plunge is always optional, and a cold shower is available if you prefer."
      }
    },
    {
      "@type": "Question",
      "name": "Are there showers or bathrooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Heated changing rooms with showers and bathrooms are on site. Both hot and cold showers are available."
      }
    },
    {
      "@type": "Question",
      "name": "Can we bring food or snacks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Water and light snacks are fine on the outdoor deck. No alcohol, no full meals inside the sauna. Hydration is the main thing."
      }
    },
    {
      "@type": "Question",
      "name": "Are animals allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Service animals only. Pets cannot come on the boat."
      }
    },
    {
      "@type": "Question",
      "name": "Are towels and robes provided?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Robes are provided on the boat. Bring your own towel for the sauna and after the cold plunge."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a place to change and store my belongings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Private changing rooms with hooks, storage cubbies, and heated floors are on site."
      }
    },
    {
      "@type": "Question",
      "name": "What kind of sauna is it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A traditional cedar wood-fired Nordic sauna on a floating boat. Inspired by Norwegian and Finnish sauna culture and built for hot-cold contrast cycling."
      }
    },
    {
      "@type": "Question",
      "name": "How hot does it get?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The sauna runs around 180 to 200 degrees Fahrenheit during a session."
      }
    },
    {
      "@type": "Question",
      "name": "How many people fit in the sauna at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Up to 8 guests in a social session. Up to 10 in a private session."
      }
    },
    {
      "@type": "Question",
      "name": "What is the cold plunge or river temperature like year round?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Columbia runs around 42 degrees Fahrenheit in winter, climbs into the 50s in spring, reaches the mid 60s in summer, and cools back down through fall. It's Cascade snowmelt, so the temperature shifts with the seasons."
      }
    },
    {
      "@type": "Question",
      "name": "Do you have a lost and found?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Email sauna@ebbandember.com if you left something behind and we'll check."
      }
    },
    {
      "@type": "Question",
      "name": "What if my private booking party size changes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reach out at sauna@ebbandember.com or (503) 308-1293 as soon as you know. We'll update the booking and make sure your door code and headcount are sorted before your session."
      }
    }
  ]
}
</script>
```

After publishing, validate at <https://search.google.com/test/rich-results> using the /faq URL. Rich results may take 1-2 weeks to appear in SERPs.

---

## 4. Fix the /shop gift card naming bug

Current state on /shop (per crawl):
- **"Social Sauna Gift Card — $539 per session"** (accommodates up to 10 guests, described as ideal for gatherings)
- **"Private Sauna Gift Card — $59 per session"** (includes one seat in a shared social session)

The names are inverted. $539 for up to 10 guests is the **private session**. $59 for one seat in a shared room is the **social session**. Both pricing and descriptions need to swap labels.

**Corrected labels:**
- **Private Sauna Gift Card — $539 per session** — accommodates up to 10 guests for a private booking
- **Social Sauna Gift Card — $59 per seat** — one seat in a shared social session for up to 8 strangers

Update product names and descriptions in Squarespace → Commerce → Products. While you're in there, also bump the product titles to include keywords:
- "Private Sauna Gift Card — Portland Floating Sauna for up to 10 Guests"
- "Social Sauna Gift Card — Portland Floating Sauna Drop-in"

---

## 5. Rename nav: Wellness → Experiences

Squarespace path: **Pages → /wellness → Page Settings → URL slug**

Change:
- Nav label: `Wellness` → `Experiences`
- URL slug: `/wellness` → `/experiences`

**Important:** When you change the URL slug, Squarespace usually auto-creates a 301 redirect from /wellness to /experiences. Verify this happens by visiting `https://www.ebbandember.com/wellness` after the change. It should redirect, not 404. If it 404s, add a manual redirect in **Settings → Advanced → URL Mappings**:

```
/wellness -> /experiences 301
```

Once renamed, also update:
- All title and meta description references (see section 1)
- Any internal links pointing to /wellness in body copy
- Resubmit sitemap.xml in GSC after Squarespace regenerates it

---

## 6. /home vs / canonical — **already fine**

Verified in raw HTML: both `/` and `/home` set `rel=canonical` to `https://www.ebbandember.com`. Google treats them as the same URL. No action needed. The audit was wrong about this being an issue.

---

## 7. After everything is deployed

1. **Resubmit sitemap in GSC.** Search Console → Sitemaps → enter `sitemap.xml` and submit again.
2. **Run URL Inspection** in GSC on /, /faq, /memberships, /shop, /experiences. Click "Request Indexing" on each.
3. **Validate schema** at <https://search.google.com/test/rich-results>.
4. **Check back in 2-3 weeks** on GSC for CTR lift on /memberships, /shop, /experiences. Those were the lowest CTR pages, so they're the cleanest signal for whether the title and meta rewrites worked.

---

## Saved for later

- **Internal linking edits** (~18 specific link additions): see `Marketing/SEO Internal Linking Edits (For Later).md`
- **Blog post (Cold Plunge Portland FAQ):** already saved in vault at `Marketing/Blog — Cold Plunge Portland FAQ.md`. Not publishing yet per direction.
- **Build /cold-plunge money page:** queued for next pass
- **Build /banya-mondays page:** queued for next pass
- **Build /our-story page from Brand Story doc:** queued for next pass
