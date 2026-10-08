# nolapartybarges.com Site Audit (2026-09-24)

Crawled all 134 sitemap URLs (30 pages, 13 tours, 91 blog posts) from the live site on 2026-09-24. Checked titles, descriptions, H1s, canonicals, schema, image alt text, every link (299), Book Now buttons, and FareHarbor prices and availability. Public site only: wp-admin login is still broken (see `Site - Jetpack SSO Broken, How To Fix (Sept 2026).md`).

Not covered: Google Search Console / GA4 numbers (the google-nola MCP was down) and a mobile PageSpeed score (the free PageSpeed API was out of quota today). Rerun both when available.

## Top 6 fixes, in order

1. **Prices on the website don't match FareHarbor.** Verified live on Freaky Tiki: the site says $63/person and $1,250 private; FareHarbor checkout says **$59** and **$1,200**. The $63 "From" price also shows on the homepage, Our Boats, Bayou Boogie, Party Queen and Bentley cards. Board note (2026-09-23) also has Party Queen at $1,100 on site vs $900 in FH. Customers see a higher price, then a lower one. Fix in wp-admin (tour cards / price fields).
2. **"Pedal" is still on 51 of 134 pages.** 27 page titles (below), 12 pages using the default description "New Orleans Pedal Party Boat Booze Cruise & Tours", the Contact page ("Contact Us New Orleans Pedal Barge"), FAQ ("Nola Pedal Barge"), Gift Card ("Purchase New Orleans Pedal Barge gift cards"), Bentley and Seafood Boil body copy, and the footer Yelp/TripAdvisor listings (still named "New Orleans Pedal Barge" on those sites). The default description is likely the WordPress Tagline setting, one edit fixes 12 pages.
3. **Tours that aren't running are still sold on the site.**
   - `/pedal-bike-bar/` books the Irish Channel Pedal Pub-Crawl (FH 501258). No dates in September or October. A "Bike Bar City Tour, Available Daily, $49" card also shows as a Related Tour on Twerkin' Tiki, Eco Tour, E-Bike and Airboat pages.
   - `/airboat-tour/` (FH 455887) and `/bow-fishing-and-sightseeing-charter-w-captain-glenn/` (FH 532387): "no online availability" for September and October.
   - Decide per tour: hide the page, or add a "call to book" note. (Holiday Express page left alone per the Jingle rule; only flagging that it exists.)
4. **Bayou Boogie page still promises captains wait:** "Another reason to book a private tour, we will wait... but it eats into your time" and "Arrive 30 min- 1 hr early" (standard is now 30-45 min). Needs wp-admin.
5. **No Product/price schema on any tour page** (still open from the 8/15 audit). Tour pages only have VideoObject + Breadcrumb. Adding price and rating markup is what gets stars and prices in Google results. Likely a FareHarbor support request, since it is a theme feature.
6. **Other brands' tours on NPB pages.** Kayak Swamp Tours (Mystic Swamp $69, Whitney Plantation combo $195) and Royal Carriages cards show as "Related Tours" on Boogie, Party Queen, Twerkin', Seafood Boil, Eco Tour and E-Bike. If that cross-sell isn't on purpose, it sends NPB buyers to other companies.

## Fixed since the 8/15 audit (verified today)

- `og:site_name` now "New Orleans Party Barge" sitewide.
- www and http both 301 to `https://nolapartybarges.com/`.
- Budget blog post title now "New Orleans Vacation Budget 2026: Costs & Tips".

## Still open from 8/15

- Product schema (above).
- `/1253-2/` junk slug ("How Many Days In New Orleans Is Enough?").
- December weather post: title unchanged, description 200 chars.
- `/our-boats/` uses the default Pedal description (likely why its click rate was 0.12% in the 8/15 GSC pull).

## Page title and description cleanup

- **Brand suffix is inconsistent.** Titles end in 5 different names: "NOLA Party Barges" (44), "New Orleans Party Barge" (38), "New Orleans Pedal Barge" (21), "Nola Pedal Barge", "Nola Party Barges". Pick one.
- **27 titles with Pedal:** service-areas, all 5 party-boats-near/in pages, all 5 swamp-tours-near/in pages (except Mississippi), faq, jobs ("Nola Pedal Party Boat Jobs"), contact-us, blog, bentley-bayou-cruiser, the-twerkin-tiki, the-freaky-tiki, the-cajun-queen ("Pedal Bike Party Booze Cruise"), tiki-boat-bayou-wildlife-tour, e-bike-tours, pedal-bike-bar, gift-card, and 4 old posts (jean-lafitte vs nola-pedal-barge, cajun-encounters vs nola-pedal-barge, a-winter-wonderland-on-the-swamp, nola-party-planning-tip-1).
- **Too long:** 63 blog titles over 60 characters (Google cuts them off), 44 descriptions over 160.
- **Duplicate title:** `/boat-rental/` and `/things-to-do-in-new-orleans/` are both "New Orleans Party Boat Rental".
- **Eco Tour page** title is "Tiki Boat Bayou & Wildlife Alligator Tour" but the H1 is "Swamp Eco Tour: Gators and Bayou Birds". Match them.
- **H1 problems:** `/review-us-here/` has none; 6 old posts have 2 or 3.

## Links

- No broken links on NPB's own pages except one missing image on `/review-us-here/` (Frown.gif, 404).
- The footer "Privacy Policy" link goes through a redirect on every page (`/privacy-policy/` to `/privacy-statement-us/`), and both URLs are in the sitemap. Point the footer at the real URL and drop the old one from the sitemap.
- `/2023-halloween-things-to-do/` has 4 dead outbound links and is a 2023 event list. Update or unpublish.
- Most other "errors" were sites blocking the checker (Yelp, TripAdvisor, cookiedatabase), not real breaks.

## Speed and mobile

- Homepage on desktop: loads in about 1.1s, 59 requests, 20 outside services (Elfsight review widgets, Mixpanel, Reddit, Meta, GA, OpenCX chat, etc.). Fine on desktop; mobile score not measured today.
- Mobile layout at 375px: no sideways scroll, hero and Book buttons look right. The chat bubble covers part of the "All boats & swamp tours include" heading.
- Every image check found 1 image without alt text on nearly every page (the logo/template image). One fix in the theme.

## What needs wp-admin vs what doesn't

- **wp-admin (blocked until FareHarbor fixes login):** prices, page titles, tagline/default description, Bayou Boogie wait line, Related Tours cards, hiding tours, footer link, 1253-2 slug.
- **FareHarbor support ticket instead:** Product schema, the theme image alt text, and the login itself.
- **Outside the site:** rename Yelp and TripAdvisor listings from "New Orleans Pedal Barge".

## Progress

- 2026-09-30: Prices fixed in wp-admin (Activities > each boat > Pricing tab) and verified on the live site. Freaky + Twerkin' $59 / $1,200, Bayou Boogie $59 / $800, Party Queen $59 / $900 (private up to 26). Price Sync is switched off on every activity, which is why they drifted.
- 2026-09-30: SEO titles and meta descriptions set on 39 pages (each page's SEO tab: Title Tag + Meta Description), verified live. Recrawl of all 134 sitemap pages: 0 with Pedal in title or description. Old values are in `Site Titles and Descriptions Rewrite 2026-09-24.md` if anything needs rolling back.
- 2026-09-30: Settings > General Site Title and Tagline changes did not stick (reverted within minutes, likely FareHarbor sync). Not needed now that every page has its own title/description.
