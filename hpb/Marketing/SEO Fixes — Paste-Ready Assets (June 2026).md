# SEO Fixes — Paste-Ready Assets (June 2026)

**For:** David / Connor
**Source plan:** `SEO Audit & Plan (June 2026).md`
**Brand direction:** Lead with "Houston Party Barge" + "party boat / BYOB booze cruise." No "pedal" in customer-facing copy. Domain stays houstonpedalbarge.com.

Everything below is ready to paste. The schema blocks go in the ACF **Schema Markup** field on each page (raw JSON, no `<script>` wrapper, no escaped `\"` quotes). After saving each one, fetch the live page and run the JSON-LD through a validator before calling it done. The CMS accepts broken JSON silently.

---

## 1. Title tags + meta descriptions

### Homepage (/)
- **Title:** `Houston Party Barge | Clear Lake Party Boat & Booze Cruise`
- **Meta:** `BYOB party boat and booze cruise on Clear Lake near the Kemah Boardwalk. Fully captained, public tickets from $55, private charters up to 26 guests. Book online.`
- **H1:** `Houston Party Barge` (remove the second H1 — keep only one. Drop the "Pedal Barge" H2 and any pedal references in body copy.)

### Tour page (/houston-party-barge-cruise/)
- **Title:** `Clear Lake Party Boat Cruise | BYOB, Captained, from $55`
- **Meta:** `Cruise Clear Lake on a 26-guest party barge. Fully captained, BYOB, ages 8+, 1 hr 45 min. Public tickets $55 or private charter $800. Book your Houston cruise.`

### Corporate (/corporate-group-event/)
- **Title:** `Houston Corporate & Group Boat Events on Clear Lake | Up to 26`
- **Meta:** `Team building, holiday parties, and client outings on a private Clear Lake party barge. BYOB, fully captained, up to 26 guests. Get a quote for your group.`

### About (/about/)
- **Title:** `About Houston Party Barge | Clear Lake's BYOB Party Boat`
- **Meta:** `The story behind Houston's BYOB party boat and booze cruise on Clear Lake in Seabrook. Fully captained cruises for up to 26 guests. Book your trip today.`

Also fix the typo in the current homepage meta: it says "Seakbrook" (should be Seabrook) and lowercase "Clear lake."

---

## 2. JSON-LD schema

### Homepage — LocalBusiness + AggregateRating

> Before pasting: confirm the two `sameAs` social URLs and add the exact Yelp + TripAdvisor URLs (I left placeholders flagged). Geo is approximate — fine for now, refine later if you want.

```json
{
  "@context": "https://schema.org",
  "@type": "TouristAttraction",
  "name": "Houston Party Barge",
  "alternateName": "Houston Pedal Barge",
  "description": "A BYOB party boat and booze cruise on Clear Lake in Seabrook, Texas, near the Kemah Boardwalk. Fully captained cruises for up to 26 guests. Public tickets from 55 dollars or private charters.",
  "url": "https://houstonpedalbarge.com/",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/houston-party-barge.jpg",
  "telephone": "+1-832-974-0365",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 E NASA Pkwy",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 29.5618,
    "longitude": -95.0203
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "400"
  },
  "sameAs": [
    "https://www.instagram.com/houstonpedalbarge",
    "https://www.facebook.com/houstonpedalbarge",
    "YELP_URL_HERE",
    "https://www.tripadvisor.com/TRIPADVISOR_URL_HERE"
  ]
}
```

### Tour page (/houston-party-barge-cruise/) — Product + Offer + AggregateRating

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Houston Party Barge Cruise",
  "description": "A BYOB party boat cruise on Clear Lake in Seabrook, Texas. Fully captained, 1 hour 45 minutes, ages 8 and up, seats up to 26 guests. Bring your own drinks and food.",
  "image": "https://houstonpedalbarge.com/wp-content/uploads/houston-party-barge-cruise.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Houston Party Barge"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "400"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Public ticket (per person)",
      "price": "55.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/houston-party-barge-cruise/"
    },
    {
      "@type": "Offer",
      "name": "Private charter (up to 26 guests)",
      "price": "800.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://houstonpedalbarge.com/houston-party-barge-cruise/"
    }
  ]
}
```

### Contact page (/contact/) — LocalBusiness NAP

```json
{
  "@context": "https://schema.org",
  "@type": "TouristAttraction",
  "name": "Houston Party Barge",
  "alternateName": "Houston Pedal Barge",
  "url": "https://houstonpedalbarge.com/contact/",
  "telephone": "+1-832-974-0365",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2515 E NASA Pkwy",
    "addressLocality": "Seabrook",
    "addressRegion": "TX",
    "postalCode": "77586",
    "addressCountry": "US"
  }
}
```

---

## 3. FAQ block for the tour page (/houston-party-barge-cruise/)

Add these six as a visible Q&A section on the page, then paste the FAQPage JSON-LD below into the Schema Markup field (you can combine it with the Product schema by pasting both as an array, or add it as a second block).

**Visible copy:**

**How much does a Houston Party Barge cruise cost?**
Public tickets are $55 per person for ages 8 and up. A private charter for your whole group up to 26 guests is $800, with a $150 deposit to reserve your date. Both options run 1 hour 45 minutes on Clear Lake in Seabrook.

**Do we have to do any work to move the boat?**
No. A licensed captain and a motor handle everything. You just board, relax, and enjoy the cruise. There is nothing for guests to operate. Sit back with your group and take in Clear Lake and the Kemah Boardwalk from the water.

**Can we bring our own drinks and food?**
Yes. The cruise is BYOB and you can bring your own food too. Cans are welcome, no glass please. Bring a cooler, ice, snacks, and whatever your group likes. There is no bar tab and no catering minimum, so you control the whole spread.

**Where do we meet for the cruise?**
You board at our dock at 2515 E NASA Pkwy in Seabrook, Texas, near the Kemah Boardwalk and about 30 minutes southeast of downtown Houston. There is parking on site. Arrive about 15 minutes before your scheduled departure.

**Are there age or group size limits?**
Guests must be at least 8 years old. The boat seats up to 26 people, which makes it a great fit for bachelorette parties, birthdays, and corporate groups. For groups larger than 26 we can talk through options, just give us a call.

**How long is the cruise?**
Every cruise runs 1 hour 45 minutes on Clear Lake. That is enough time to get out on the open water, pass the Kemah Boardwalk, catch the sunset on an evening slot, and enjoy your drinks and your group without feeling rushed.

**FAQPage JSON-LD:**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does a Houston Party Barge cruise cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Public tickets are 55 dollars per person for ages 8 and up. A private charter for your whole group up to 26 guests is 800 dollars, with a 150 dollar deposit to reserve your date. Both options run 1 hour 45 minutes on Clear Lake in Seabrook."
      }
    },
    {
      "@type": "Question",
      "name": "Do we have to do any work to move the boat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. A licensed captain and a motor handle everything. You just board, relax, and enjoy the cruise. There is nothing for guests to operate. Sit back with your group and take in Clear Lake and the Kemah Boardwalk from the water."
      }
    },
    {
      "@type": "Question",
      "name": "Can we bring our own drinks and food?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The cruise is BYOB and you can bring your own food too. Cans are welcome, no glass please. Bring a cooler, ice, snacks, and whatever your group likes. There is no bar tab and no catering minimum, so you control the whole spread."
      }
    },
    {
      "@type": "Question",
      "name": "Where do we meet for the cruise?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You board at our dock at 2515 E NASA Pkwy in Seabrook, Texas, near the Kemah Boardwalk and about 30 minutes southeast of downtown Houston. There is parking on site. Arrive about 15 minutes before your scheduled departure."
      }
    },
    {
      "@type": "Question",
      "name": "Are there age or group size limits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Guests must be at least 8 years old. The boat seats up to 26 people, which makes it a great fit for bachelorette parties, birthdays, and corporate groups. For groups larger than 26 we can talk through options, just give us a call."
      }
    },
    {
      "@type": "Question",
      "name": "How long is the cruise?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every cruise runs 1 hour 45 minutes on Clear Lake. That is enough time to get out on the open water, pass the Kemah Boardwalk, catch the sunset on an evening slot, and enjoy your drinks and your group without feeling rushed."
      }
    }
  ]
}
```

---

## Before you paste — two things to fill in
1. **Social URLs** in the homepage `sameAs` array: confirm the Facebook handle and add the exact Yelp and TripAdvisor listing URLs.
2. **Image URLs** in the Product and homepage schema: swap in real uploaded image URLs from the media library.

Everything else (phone, address, rating 4.9/400, pricing) is pulled from current vault data and ready as-is.

## Validate after each paste
For each page, fetch the live URL and confirm the JSON-LD parses. Quick check from terminal:
`curl -sL https://houstonpedalbarge.com/houston-party-barge-cruise/ | grep -o 'application/ld+json'` should now return matches where it returned zero today.
