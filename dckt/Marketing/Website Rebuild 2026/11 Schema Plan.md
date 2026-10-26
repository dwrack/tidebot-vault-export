# Schema plan (JSON-LD), new site

*2026-10-16. Implemented in `~/Projects/dckt-site/src/lib/schema.ts` and the page templates. Every page emits one `@graph` in the head: the site-wide nodes plus the page's own. Validated by parsing every built page's JSON-LD with Python `json.loads` on 2026-10-16 (0 errors).*

## Site-wide (every page)

| Node | @id | Key properties | Source of truth |
|:-|:-|:-|:-|
| `LocalBusiness` + `SportsActivityLocation` | `https://www.doorcountykayaktours.com/#organization` | name, legalName (Door County Kayak Tours LLC), url, telephone +1-920-868-1400, email info@, foundingDate 2002, priceRange "$65 - $145", address 6329 WI-57 Sturgeon Bay WI 54235 (the shop; David's 2026-05-10 call for web schema; Fish Creek stays the legal address only), geo, areaServed (Door County towns), aggregateRating 4.9 / 1011 (GBP, verified 2026-10-15), sameAs (IG, FB, YouTube, TikTok), knowsAbout | `src/data/site.ts` |
| `WebSite` | `/#website` | name, url, publisher -> organization | same |

Not emitted: `openingHoursSpecification` (seasonal hours unverified; add when David confirms), `WebPage` (adds nothing).

## Per template

| Template | Nodes | Notes |
|:-|:-|:-|
| Home | FAQPage (6 Q&A, matches the visible FAQ 1:1) | |
| Tour page (Cave Point built; others Sat) | BreadcrumbList, TouristTrip (name, description = the 40-60 word definition paragraph, image, touristType, provider, itinerary = meet + launch, offers), Product (same name/description/image/offers + aggregateRating), FAQPage (8 Q&A, HTML stripped), VideoObject on Cave Point only (the 319k-view YouTube video, from the live page) | One `Offer` object shared by TouristTrip and Product: price, USD, InStock, url, validFrom = season start, seller -> organization. Price comes from `src/data/tours.ts` so the visible price and the schema price cannot drift. |
| Blog post | BreadcrumbList, BlogPosting (headline, description, image, datePublished from the live post, dateModified = today, author and publisher -> organization), FAQPage when the post has FAQs | Author is the organization, not a named person ("Drifty" vs Ashley conflict in the audits; David never confirmed a byline). |
| Ported legacy page | BreadcrumbList only | The theme's own breadcrumb was the only schema these pages had; nothing lost. Tour pages get the full set as they are rebuilt. |
| Blog index, hubs | BreadcrumbList | ItemList for the tour hubs on Sat. |

## Rules carried from the schema-markup and ai-seo skills

- Visible text first: every FAQ in schema is on the page, word for word.
- No `Review` nodes with invented text. Quotes on the Reviews block are public Google reviews, not marked up as Review (Google wants first-party reviews collected on-site for that).
- Dates ISO 8601, URLs absolute, no escaped inner double quotes (the WP-VIP lesson from memory still applies to anything pasted by hand).
- Check after launch: Search Console > Enhancements for Product, FAQ, Breadcrumb, Video; Rich Results Test on the three finished pages.

## Open

- `openingHoursSpecification` once David gives season hours.
- `Event` for the guide training camp (May) if David wants it listed.
- `aggregateRating` on Product: Google may show stars on tour results; if it ever flags "self-serving" we drop it from Product and keep it on LocalBusiness.
