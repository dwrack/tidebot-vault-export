# Schema Markup Library

Paste-ready JSON-LD for every page. Reminders for the FareHarbor / WP-VIP theme:

- **Paste raw JSON only.** No `<script type='application/ld+json'>` wrapper. The theme adds it.
- **No escaped inner double quotes (`\"`)** anywhere. The render layer strips backslashes and breaks the page schema. Rewrite to avoid inner double-quoted phrases.
- After saving, fetch the live page and confirm the JSON-LD parses with `JSON.parse`.

---

## Homepage — LocalBusiness + Organization

Paste into the Schema Markup field on `/`:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.austinkayaktours.com/#business",
  "name": "Austin Kayak Tours",
  "alternateName": "Lone Star Kayak Tours",
  "url": "https://www.austinkayaktours.com/",
  "telephone": "+1-512-766-5640",
  "email": "austinkayaktours@gmail.com",
  "priceRange": "$20-$50",
  "image": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/2020/04/austin-1402097_1920.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "200 E Riverside Dr",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78704",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 30.2580,
    "longitude": -97.7414
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      "opens": "09:00",
      "closes": "20:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/austinkayaktours/",
    "https://www.instagram.com/austinkayaktours",
    "https://www.tripadvisor.com/Attraction_Review-g30196-d11876981-Reviews-Austin_Kayak_Tours-Austin_Texas.html",
    "https://www.yelp.com/biz/austin-kayak-tours-austin"
  ],
  "areaServed": {
    "@type": "City",
    "name": "Austin"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "500"
  }
}
```

Replace `reviewCount` with the real number from TripAdvisor before going live. Same for the `priceRange`, `latitude`, `longitude` if more precise coordinates are available.

---

## Austin Skyline Tour — Product + TouristTrip

Paste into Schema Markup field on `/austin-skyline-tour/`:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Austin Skyline Kayak Tour",
  "description": "A 2-hour guided kayak tour of Lady Bird Lake with downtown Austin skyline views, history, and architecture commentary from a local guide.",
  "image": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/austin-skyline-kayak-tour.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Austin Kayak Tours"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.austinkayaktours.com/austin-skyline-tour/",
    "priceCurrency": "USD",
    "price": "50.00",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-01-01"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "200"
  }
}
```

---

## Sunset Bat Bridge Kayak Tour — Product

Paste into `/bat-bridge-kayak-tour/`:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Sunset Bat Bridge Kayak Tour",
  "description": "A 2-hour sunset kayak tour on Lady Bird Lake to watch 1.5 million Mexican free-tailed bats fly from the Congress Avenue Bridge. Seasonal, daily March through October.",
  "image": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/bat-bridge-kayak-tour.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Austin Kayak Tours"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.austinkayaktours.com/bat-bridge-kayak-tour/",
    "priceCurrency": "USD",
    "price": "50.00",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "200"
  }
}
```

---

## Paddle Board Bat Tour — Product

Paste into `/paddleboard-tour/` (or correct slug):

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Paddle Board Bat Tour",
  "description": "Stand-up paddle board tour at sunset to watch the Congress Avenue bat colony from Lady Bird Lake. Beginner-friendly, 2 hours.",
  "image": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/paddle-board-bat-tour.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Austin Kayak Tours"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.austinkayaktours.com/paddleboard-tour/",
    "priceCurrency": "USD",
    "price": "50.00",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## Kayak & Paddle Board Rental — Product

Paste into `/rental/`:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Kayak and Paddle Board Rental",
  "description": "Hourly kayak, paddle board, and canoe rentals on Lady Bird Lake in downtown Austin. Walk-up or reserve online. Beginners welcome.",
  "image": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/kayak-rental.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Austin Kayak Tours"
  },
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "USD",
    "lowPrice": "20.00",
    "highPrice": "50.00",
    "url": "https://www.austinkayaktours.com/rental/",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## FAQ Page — FAQPage

Paste into `/faq/`. Note: every question is rewritten to avoid inner double quotes per the theme's rendering bug.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need experience to join a kayak tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Most of our guests have never kayaked before. Lady Bird Lake is flat, calm water and our guides walk you through everything in the first 5 minutes. If you can walk, you can do this tour."
      }
    },
    {
      "@type": "Question",
      "name": "What should I wear on a kayak tour in Austin?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Clothes you do not mind getting splashed. Quick-dry shorts or athletic wear, a t-shirt, sunglasses with a strap, and a hat. We suggest water shoes or sandals with a back strap. Skip flip-flops, they fall off."
      }
    },
    {
      "@type": "Question",
      "name": "How old do you have to be to kayak with us?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Five years old and up for most tours. Younger kids can ride tandem in a kayak with a parent. Anyone under 18 needs a guardian on the booking."
      }
    },
    {
      "@type": "Question",
      "name": "Where do tours launch from?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We launch from 200 E Riverside Drive in Austin, TX 78704. Free parking is available on-site. We are right next to the South Congress Bridge."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if it rains?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Light rain is fine, we still paddle. If there is lightning or a storm in the forecast, we either move you to another tour time or refund you in full. Safety call is always with the guide on the day of."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bring my dog?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dogs are welcome on rentals if they are calm on the water and have a life jacket. Tours are guides-only so we ask that dogs sit those out."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a weight or age limit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Single kayaks are rated to about 250 pounds. Tandem kayaks handle a combined 400 pounds. If you are close to that, just call us and we will set you up on a tandem so it is comfortable."
      }
    },
    {
      "@type": "Question",
      "name": "How early should I arrive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Plan to arrive 15 minutes before your booked time. We do a quick safety brief, fit your life jacket, and put you on the water on time."
      }
    },
    {
      "@type": "Question",
      "name": "Are there bathrooms at the launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, public restrooms are within a 2-minute walk of the launch site at 200 E Riverside Drive."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bring my phone or camera on the water?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We recommend a waterproof phone case or a dry bag. Most guests bring their phone for photos. We do see a few drop in the lake every season, so do not skip the case."
      }
    }
  ]
}
```

---

## BreadcrumbList — for every interior page

Pattern. Adjust the last item per page.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.austinkayaktours.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Tours",
      "item": "https://www.austinkayaktours.com/tours/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Austin Skyline Kayak Tour",
      "item": "https://www.austinkayaktours.com/austin-skyline-tour/"
    }
  ]
}
```

---

## Article schema — for every blog post

Use this template at the bottom of each post's Schema Markup field. Replace placeholders.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "POST TITLE HERE",
  "description": "SHORT META DESCRIPTION HERE",
  "image": "FEATURED IMAGE URL HERE",
  "author": {
    "@type": "Organization",
    "name": "Austin Kayak Tours"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Austin Kayak Tours",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.austinkayaktours.com/wp-content/uploads/sites/4074/2020/04/kayak-1.png"
    }
  },
  "datePublished": "2026-MM-DD",
  "dateModified": "2026-MM-DD",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "POST URL HERE"
  }
}
```
