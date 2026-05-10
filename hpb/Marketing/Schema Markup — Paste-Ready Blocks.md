# Houston Pedal Barge — Schema Markup Blocks (Paste-Ready)

**Created:** 2026-05-10
**For:** Connor (or whoever has WordPress access)
**Phase:** Action Plan — Phase 1, items 5, 6, 7

---

## Critical rules (read first)

1. **Paste raw JSON only.** Do NOT wrap in `<script type="application/ld+json">`. The FareHarbor / WP-VIP theme adds the script wrapper automatically. Wrapping it yourself produces the validator error: "Please provide valid JSON. Error in object #1: Syntax error."
2. **Do not use escaped inner double quotes (`\"`) anywhere.** The CMS strips the backslash and breaks the JSON on the live page. Every block below has been written without any inner double-quoted phrases. Single quotes inside JSON string values are fine.
3. **Where to paste:** every page edit screen has an ACF field labeled **Schema Markup** (field key `field_seo__schema_markup`). Paste the JSON for that page into that field. Save. Then verify on the live page.
4. **Verification step (don't skip).** After saving each page, fetch the live URL and run the embedded JSON-LD through `JSON.parse` (in browser console or via a JSON-LD validator like search.google.com/test/rich-results). The CMS accepts invalid output silently.
5. **Update the placeholders before you paste.** Several blocks use approximate values (geo coords, opening hours). Fill in the real values from David before publishing.

---

## Placeholder values to fill in

These show up in multiple blocks. Confirm with David before pasting:

| Placeholder | Best guess (verify) |
|---|---|
| Geo latitude | 29.5612 |
| Geo longitude | -95.0212 |
| Address line 2 | Suite D (per vault memory: "2515 E NASA Pkwy # D") — confirm |
| Opening hours | Wed-Sun 12:00-21:00 (typical season). Confirm seasonal hours |
| Aggregate review rating | Pull from Google Business Profile (likely 4.7-4.9) |
| Aggregate review count | Pull from GBP + Yelp + Tripadvisor combined |
| Founder year | When did HPB start? |

---

## 1. /contact/ — LocalBusiness

This is the canonical LocalBusiness entity. Every other page can reference it via `@id` once this is live.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://houstonpedalbarge.com/#localbusiness",
  "name": "Houston Pedal Barge",
  "alternateName": "Houston Party Barge",
  "url": "https://houstonpedalbarge.com/",
  "logo": "https://houstonpedalbarge.com/wp-content/uploads/houston-pedal-barge-logo.png",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/houston-pedal-barge-hero.jpg",
  "description": "Houston Pedal Barge is the city's first pedal-powered party boat on Clear Lake in Seabrook, Texas. Public and private booze cruises for groups up to 26, BYOB, captain and crew included.",
  "telephone": "+1-832-974-0365",
  "email": "houstonpedalbarge@gmail.com",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 East NASA Parkway",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 29.5612,
    "longitude": -95.0212
  },
  "areaServed": [
    {"@type": "City", "name": "Houston"},
    {"@type": "City", "name": "Seabrook"},
    {"@type": "City", "name": "Kemah"},
    {"@type": "City", "name": "Clear Lake"},
    {"@type": "City", "name": "League City"},
    {"@type": "City", "name": "Pasadena"},
    {"@type": "City", "name": "Pearland"}
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      "opens": "12:00",
      "closes": "21:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/htxpedalbarge/",
    "https://www.instagram.com/houstonpedalbarge/",
    "https://www.tripadvisor.com/Attraction_Review-g56646-d23800580-Reviews-Houston_Pedal_Barge-Seabrook_Texas.html",
    "https://www.yelp.com/biz/houston-pedal-barge-seabrook",
    "https://www.youtube.com/@houstonpedalbarge"
  ]
}
```

---

## 2. / (Homepage) — TouristAttraction with AggregateRating

Targets the homepage knowledge panel and review stars in SERP.

```json
{
  "@context": "https://schema.org",
  "@type": "TouristAttraction",
  "@id": "https://houstonpedalbarge.com/#touristattraction",
  "name": "Houston Pedal Barge",
  "url": "https://houstonpedalbarge.com/",
  "description": "Houston's first pedal-powered party boat. Cruise Clear Lake in Seabrook with up to 26 guests, BYOB, with a licensed captain and crew. 1 hour 45 minute tours from $55 per person.",
  "image": [
    "https://houstonpedalbarge.com/wp-content/uploads/pedal-barge-clear-lake-1.jpg",
    "https://houstonpedalbarge.com/wp-content/uploads/pedal-barge-bachelorette.jpg",
    "https://houstonpedalbarge.com/wp-content/uploads/pedal-barge-corporate.jpg"
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 East NASA Parkway",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 29.5612,
    "longitude": -95.0212
  },
  "telephone": "+1-832-974-0365",
  "isAccessibleForFree": false,
  "publicAccess": true,
  "touristType": [
    "Bachelorette parties",
    "Bachelor parties",
    "Corporate groups",
    "Birthday parties",
    "Tourists",
    "Local groups"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "180",
    "bestRating": "5",
    "worstRating": "1"
  },
  "sameAs": [
    "https://www.facebook.com/htxpedalbarge/",
    "https://www.instagram.com/houstonpedalbarge/",
    "https://www.tripadvisor.com/Attraction_Review-g56646-d23800580-Reviews-Houston_Pedal_Barge-Seabrook_Texas.html"
  ]
}
```

**Note on AggregateRating:** Google requires that aggregate ratings reflect actual reviews collected first-party or directly verifiable. The 4.8 / 180 figures are placeholders. Pull real numbers from Google Business Profile + Yelp + Tripadvisor and use a defensible total. If we can embed individual reviews on /houston-pedal-barge-reviews/, even better.

---

## 3. /houston-party-barge-cruise/ — Product + FAQPage (combined)

The canonical money page. This block has two `@graph` entries: a Product (the cruise) and a FAQPage (the existing Quick Details / Notice copy reformatted).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "@id": "https://houstonpedalbarge.com/houston-party-barge-cruise/#product",
      "name": "Houston Party Barge Cruise",
      "description": "A 1 hour 45 minute pedal-powered booze cruise on Clear Lake in Seabrook, Texas. Up to 26 guests per boat, BYOB, with a licensed captain and crew. Book public per-person seats or a private charter.",
      "image": [
        "https://houstonpedalbarge.com/wp-content/uploads/houston-party-barge-cruise.jpg"
      ],
      "brand": {
        "@type": "Brand",
        "name": "Houston Pedal Barge"
      },
      "offers": [
        {
          "@type": "Offer",
          "name": "Public Cruise — Per Person",
          "price": "55.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://houstonpedalbarge.com/houston-party-barge-cruise/"
        },
        {
          "@type": "Offer",
          "name": "Private Charter — Up to 26 Guests",
          "price": "800.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://houstonpedalbarge.com/houston-party-barge-cruise/"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "180",
        "bestRating": "5",
        "worstRating": "1"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://houstonpedalbarge.com/houston-party-barge-cruise/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How long is the Houston Pedal Barge cruise?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Cruises are 1 hour and 45 minutes. We board 15 minutes before departure, so plan to arrive at the dock 30 minutes early to load coolers and find your seats."
          }
        },
        {
          "@type": "Question",
          "name": "How many people fit on the pedal barge?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The boat holds up to 26 guests. There are 12 pedal stations and 14 surrounding seats. You can book individual public seats or charter the whole boat for a private group."
          }
        },
        {
          "@type": "Question",
          "name": "Is the Houston Pedal Barge BYOB?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Bring your own drinks and snacks. Cans only — no glass containers. We do not allow cake or rice on the boat. There is a cooler on board with ice."
          }
        },
        {
          "@type": "Question",
          "name": "Do I have to pedal?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. The boat has a 90 horsepower motor and a licensed captain. Pedaling is part of the fun but it is optional. Some guests pedal the entire time, others pedal in spurts, and some never pedal at all."
          }
        },
        {
          "@type": "Question",
          "name": "How much does a Houston Pedal Barge cruise cost?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Public seats start at 55 dollars per person. Private charters for the full boat start at 800 dollars and accommodate up to 26 guests. Pricing varies by date, time, and theme."
          }
        },
        {
          "@type": "Question",
          "name": "Where does the pedal barge launch?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We launch from 2515 East NASA Parkway, Seabrook, TX 77586. The dock is on Clear Lake, 8 minutes from Space Center Houston and 5 minutes from the Kemah Boardwalk."
          }
        },
        {
          "@type": "Question",
          "name": "What happens if it rains?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Light rain does not stop us. We have a covered top and clear vinyl side panels. If conditions are unsafe, the captain reschedules and we work with you to find a new date or issue a credit."
          }
        }
      ]
    }
  ]
}
```

---

## 4. /pedal-bike-barge-cruise-delta-dream/ — Product

If you decide to keep this page (vs. 301'ing to the canonical), use this. If you redirect, skip.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-delta-dream/#product",
  "name": "Pedal Bike Barge Cruise — The Delta Dream",
  "description": "The Delta Dream is one of two pedal pontoons in the Houston Pedal Barge fleet. Up to 26 guests, 1 hour 45 minute cruises on Clear Lake, BYOB, captain included.",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/delta-dream.jpg",
  "brand": {"@type": "Brand", "name": "Houston Pedal Barge"},
  "offers": [
    {
      "@type": "Offer",
      "name": "Public Cruise — Per Person",
      "price": "59.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-delta-dream/"
    },
    {
      "@type": "Offer",
      "name": "Private Charter",
      "price": "850.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-delta-dream/"
    }
  ]
}
```

---

## 5. /pedal-bike-barge-cruise-mama-tried/ — Product

Same caveat as Delta Dream. If you redirect, skip.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-mama-tried/#product",
  "name": "Pedal Bike Barge Cruise — Mama Tried",
  "description": "The Mama Tried is the black-and-gold pedal pontoon in the Houston Pedal Barge fleet. Up to 26 guests, 1 hour 45 minute cruises on Clear Lake, BYOB, captain included.",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/mama-tried.jpg",
  "brand": {"@type": "Brand", "name": "Houston Pedal Barge"},
  "offers": [
    {
      "@type": "Offer",
      "name": "Public Cruise — Per Person",
      "price": "59.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-mama-tried/"
    },
    {
      "@type": "Offer",
      "name": "Private Charter — Weekday",
      "price": "675.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/pedal-bike-barge-cruise-mama-tried/"
    }
  ]
}
```

---

## 6. /corporate-group-event/ — Service

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://houstonpedalbarge.com/corporate-group-event/#service",
  "serviceType": "Corporate Team Building Cruise",
  "name": "Houston Pedal Barge Corporate and Group Events",
  "description": "Private pedal barge charters for corporate team building, client entertaining, holiday parties, and group events on Clear Lake in Seabrook, Texas. Up to 26 guests, BYOB, captain and crew included.",
  "provider": {
    "@type": "LocalBusiness",
    "@id": "https://houstonpedalbarge.com/#localbusiness"
  },
  "areaServed": [
    {"@type": "City", "name": "Houston"},
    {"@type": "City", "name": "Seabrook"},
    {"@type": "City", "name": "Kemah"},
    {"@type": "City", "name": "Clear Lake"}
  ],
  "audience": {
    "@type": "BusinessAudience",
    "audienceType": "Corporate teams, client groups, conference attendees"
  },
  "offers": {
    "@type": "Offer",
    "name": "Private Corporate Charter",
    "price": "800.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://houstonpedalbarge.com/corporate-group-event/"
  }
}
```

---

## 7. /firework-show-and-party-barge/ — Event

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://houstonpedalbarge.com/firework-show-and-party-barge/#event",
  "name": "Firework Show and Party Barge Cruise",
  "description": "A pedal barge cruise on Clear Lake timed to view fireworks from the Kemah Boardwalk. 1 hour 45 minutes, BYOB, up to 26 guests.",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/firework-cruise.jpg",
  "location": {
    "@type": "Place",
    "name": "Houston Pedal Barge Dock",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "2515 East NASA Parkway",
      "addressLocality": "Seabrook",
      "addressRegion": "TX",
      "postalCode": "77586",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://houstonpedalbarge.com/#localbusiness"
  },
  "offers": {
    "@type": "Offer",
    "name": "Per Person Ticket",
    "price": "69.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://houstonpedalbarge.com/firework-show-and-party-barge/",
    "validFrom": "2026-01-01"
  }
}
```

---

## 8. /4th-of-july-firework-spectacular/ — Event (seasonal)

Update `startDate` annually. For 2026: July 4, 2026.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://houstonpedalbarge.com/4th-of-july-firework-spectacular/#event",
  "name": "4th of July Firework Spectacular Pedal Barge Cruise",
  "description": "Watch the Kemah Boardwalk fireworks from the water on a Houston Pedal Barge cruise. 1 hour 45 minute pedal-powered booze cruise on Clear Lake. BYOB.",
  "startDate": "2026-07-04T20:30:00-05:00",
  "endDate": "2026-07-04T22:15:00-05:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/4th-of-july-cruise.jpg",
  "location": {
    "@type": "Place",
    "name": "Houston Pedal Barge Dock",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "2515 East NASA Parkway",
      "addressLocality": "Seabrook",
      "addressRegion": "TX",
      "postalCode": "77586",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://houstonpedalbarge.com/#localbusiness"
  },
  "offers": {
    "@type": "Offer",
    "name": "4th of July Ticket",
    "price": "79.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://houstonpedalbarge.com/4th-of-july-firework-spectacular/",
    "validFrom": "2026-04-01",
    "validThrough": "2026-07-04"
  }
}
```

---

## 9. /christmas-themed-booze-cruise/ — Event (seasonal)

Update `startDate` annually for the season. Use a date range if you run multiple Christmas cruises.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://houstonpedalbarge.com/christmas-themed-booze-cruise/#event",
  "name": "Christmas Themed Booze Cruise",
  "description": "A holiday-themed pedal barge cruise on Clear Lake in Seabrook. Decked out for Christmas with festive music, lights, and BYOB drinks. 1 hour 45 minutes, up to 26 guests.",
  "startDate": "2026-11-28T18:00:00-06:00",
  "endDate": "2026-12-23T21:00:00-06:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/christmas-cruise.jpg",
  "location": {
    "@type": "Place",
    "name": "Houston Pedal Barge Dock",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "2515 East NASA Parkway",
      "addressLocality": "Seabrook",
      "addressRegion": "TX",
      "postalCode": "77586",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://houstonpedalbarge.com/#localbusiness"
  },
  "offers": {
    "@type": "Offer",
    "name": "Christmas Cruise Ticket",
    "price": "59.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://houstonpedalbarge.com/christmas-themed-booze-cruise/",
    "validFrom": "2026-10-01",
    "validThrough": "2026-12-23"
  }
}
```

---

## 10. /spooky-singles-booze-cruise/ — Event (seasonal)

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://houstonpedalbarge.com/spooky-singles-booze-cruise/#event",
  "name": "Spooky Singles Booze Cruise",
  "description": "A Halloween-themed pedal barge cruise on Clear Lake for singles in Houston. Costume optional, BYOB, 1 hour 45 minutes. Up to 26 guests.",
  "startDate": "2026-10-24T19:00:00-05:00",
  "endDate": "2026-10-31T22:00:00-05:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/spooky-singles.jpg",
  "location": {
    "@type": "Place",
    "name": "Houston Pedal Barge Dock",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "2515 East NASA Parkway",
      "addressLocality": "Seabrook",
      "addressRegion": "TX",
      "postalCode": "77586",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@type": "LocalBusiness",
    "@id": "https://houstonpedalbarge.com/#localbusiness"
  },
  "offers": {
    "@type": "Offer",
    "name": "Spooky Singles Ticket",
    "price": "59.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://houstonpedalbarge.com/spooky-singles-booze-cruise/",
    "validFrom": "2026-08-01",
    "validThrough": "2026-10-31"
  }
}
```

---

## 11. /houston-pedal-barge-reviews/ — AggregateRating + Review

For this to be valid in Google's eyes, you need actual on-page reviews to back it. Pull 8-12 real reviews from Google + Yelp + Tripadvisor and embed them on the page. Then this block points at them. If the page is just a hub of links to other sites without on-page reviews, skip the AggregateRating and just point at the LocalBusiness entity.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://houstonpedalbarge.com/#localbusiness",
  "name": "Houston Pedal Barge",
  "url": "https://houstonpedalbarge.com/",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/houston-pedal-barge-hero.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 East NASA Parkway",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "180",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "author": {"@type": "Person", "name": "Sarah M."},
      "datePublished": "2025-09-14",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "reviewBody": "Best bachelorette activity we did in Houston. The captain was awesome and the boat was perfect for our 14 person group. We brought our own drinks and music. Will definitely book again."
    },
    {
      "@type": "Review",
      "author": {"@type": "Person", "name": "Mike R."},
      "datePublished": "2025-08-02",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "reviewBody": "Took our team out for a corporate event. 26 of us, 1 hour 45 minutes on Clear Lake, BYOB. Way better than another escape room. The crew handled everything."
    },
    {
      "@type": "Review",
      "author": {"@type": "Person", "name": "Jenny K."},
      "datePublished": "2025-07-19",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "reviewBody": "Did the firework cruise on the 4th of July. Watching the Kemah fireworks from the water with our friends and our own drinks was unbeatable. Worth every penny."
    }
  ]
}
```

**Replace the three sample reviews with real, copy-pasted ones from Google.** Match the author name, date, and exact text. Do not invent reviews. Google catches fabricated review schema and penalizes it.

---

## 12. /about/ — Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://houstonpedalbarge.com/#organization",
  "name": "Houston Pedal Barge",
  "alternateName": "Houston Party Barge",
  "url": "https://houstonpedalbarge.com/",
  "logo": "https://houstonpedalbarge.com/wp-content/uploads/houston-pedal-barge-logo.png",
  "description": "Houston's first pedal-powered party boat. We run public and private booze cruises on Clear Lake in Seabrook, Texas, for groups up to 26.",
  "foundingDate": "2021",
  "founder": {
    "@type": "Person",
    "name": "David Wrack"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 East NASA Parkway",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  },
  "telephone": "+1-832-974-0365",
  "email": "houstonpedalbarge@gmail.com",
  "sameAs": [
    "https://www.facebook.com/htxpedalbarge/",
    "https://www.instagram.com/houstonpedalbarge/",
    "https://www.tripadvisor.com/Attraction_Review-g56646-d23800580-Reviews-Houston_Pedal_Barge-Seabrook_Texas.html",
    "https://www.yelp.com/biz/houston-pedal-barge-seabrook"
  ]
}
```

**Confirm `foundingDate` and `founder.name` with David before publishing.** If David isn't the public-facing founder name, swap it.

---

## Verification checklist (after each paste)

For each page you update:

- [ ] Save the page in WordPress
- [ ] Visit the live URL in a browser
- [ ] View page source (right click → View Page Source)
- [ ] Find the `<script type="application/ld+json">` block
- [ ] Copy the JSON contents into an online validator: https://search.google.com/test/rich-results
- [ ] Confirm "Valid items detected" with no errors
- [ ] If errors: open the JSON in a JSON formatter, find the broken character (usually a stray `\"` the CMS introduced), rewrite that string, paste again

---

## Order of operations

Do this in this order. If you batch all 12 in a row without verifying, a CMS quirk will silently break half of them.

1. /contact/ — LocalBusiness (canonical entity, everything references it)
2. / (homepage) — TouristAttraction
3. /houston-party-barge-cruise/ — Product + FAQPage (highest-traffic money page)
4. /houston-pedal-barge-reviews/ — only AFTER you embed real reviews on the page
5. /corporate-group-event/ — Service
6. /about/ — Organization
7. /firework-show-and-party-barge/ — Event
8. /4th-of-july-firework-spectacular/ — Event (seasonal)
9. /christmas-themed-booze-cruise/ — Event (seasonal)
10. /spooky-singles-booze-cruise/ — Event (seasonal)
11. /pedal-bike-barge-cruise-delta-dream/ — Product (only if not 301'd)
12. /pedal-bike-barge-cruise-mama-tried/ — Product (only if not 301'd)

---

## What this gets you

Once these are live and validated, you should see within 2-6 weeks:

- Star ratings appearing in Google SERP for branded queries
- FAQ rich results expanding the SERP footprint for /houston-party-barge-cruise/
- Event rich results for the seasonal cruises (highly visible during Halloween, 4th of July, Christmas search peaks)
- LocalBusiness knowledge panel signal getting stronger (combined with the existing GBP)
- AI search engines (ChatGPT, Perplexity, Gemini) more likely to cite HPB when answering "best Houston bachelorette boat" or "Clear Lake party boats" queries

This is the foundation. Without it, the 50-post content calendar publishes into a structural void.
