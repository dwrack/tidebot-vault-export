# Tech SEO: Buffalo Bayou Kayak (2026-10-31)

Measured 2026-10-31. Report only, nothing changed. PageSpeed Insights v5 (with key), curl, DataForSEO. Also filed (copy) at `TheBrain/00 Dashboard/Tech SEO/2026-10-31 - BBK.md`.

**Verdict:** Crawlability and indexing hygiene are clean. Mobile lab speed is poor (Lighthouse 37 to 53) but real-user field data is good, so this is P2, not P1. Most of it is the shared FareHarbor theme.

## Core Web Vitals + Lighthouse
| Page | Device | Perf | LCP | CLS | TBT | FCP |
|---|---|---|---|---|---|---|
| Home | Mobile | 37 | 12.1 s | 0 | 3,270 ms | 2.0 s |
| Home | Desktop | 70 | 1.4 s | 0.01 | 670 ms | 0.6 s |
| Bat bridge tour | Mobile | 38 | 10.3 s | 0.002 | 3,680 ms | 1.9 s |
| Bat bridge tour | Desktop | 69 | 0.9 s | 0.005 | 850 ms | 0.5 s |
| Skyline tour | Mobile | 53 | 4.2 s | 0.009 | 2,740 ms | 1.9 s |
| Skyline tour | Desktop | 56 | 1.8 s | 0.03 | 2,760 ms | 0.6 s |

**Field data (CrUX, 75th percentile, origin):** LCP 1,157 ms (good, under 2.5 s), INP 103 ms (good, under 200), CLS 0 (good). Google ranks on field data, so the lab numbers overstate the problem. Mobile lab LCP is a throttled-4G simulation.

Server TTFB by curl: 0.08 s to 1.2 s depending on page and cache (home 0.28 s, rentals 1.22 s, bat tour 0.09 s). `cache-control: max-age=300` on HTML.

## What is slow on BBK specifically (mobile home)
- Total page weight 6.2 MB. Unused JavaScript about 1.7 MB.
- **OpenCX chat widget** loads from `https://unpkg.com/@opencx/widget@latest/dist-embed/script.js` (663 KB transfer, about 1.1 s of script time, 365 KB unused). `@latest` is unpinned: any upstream release changes the live site without a deploy. Pin the version (the page also loads `@5.7.0` once) and load it after first interaction or idle.
- Hero images: `AdobeStock_400447597-scaled.jpeg` 734 KB and `kayak2.png` 627 KB (a PNG photo), plus a 204 KB jpg. Convert the PNG to JPG/WebP and cap heroes near 400 to 700 KB.
- Three or four Google tag IDs on the homepage (G-2CHJ9R6QSF, G-9J1S6JCPVY, G-CGV97LY2NK, and G-6WXE90X597 seen in the PSI trace), each loading a gtag.js of 80 to 190 KB. Worth confirming which are intended.

## Redirects
| URL | Result |
|---|---|
| http://buffalobayoukayak.com | 1 hop to https non-www (clean) |
| https://www.buffalobayoukayak.com | 1 hop to non-www (clean) |
| http://www.buffalobayoukayak.com | 2 hops (http then www then non-www); minor, template/DNS level |
| /kayak-tours (no slash) | 1 hop to trailing slash (normal WordPress) |

## Broken links
50 unique URLs from home, tours hub, rentals and bat tour page checked. No 4xx on real pages. Two `wp-json/oembed/1.0/embed?...` links return 404 (oEmbed discovery tags in `<head>`) and one third-party 403 (cookiedatabase.org, bot block). Harmless, but the oEmbed 404 is theme-level.

## robots.txt and sitemaps
- robots.txt: `User-agent: *` now carries the Disallow lines properly (the stray-lines note from the Aug 15 audit is fixed). Scraper bots blocked. GPTBot, ClaudeBot, PerplexityBot are NOT blocked (good for AI search). Sitemap line present.
- `sitemap.xml` is an index of page (16 URLs), activity (19) and post (11) sitemaps. Latest lastmod 2026-06-13 on pages/activities; posts frozen at 2023-11-28.
- `/llms.txt` exists (text/plain, 200).

## Index status
Not available: BBK is not a Search Console property on any connected account (checked 2026-10-31). Cannot report indexed vs discovered counts. Fixing GSC access is the prerequisite for this section.

## On-page and schema, technical side
- All 18 pages checked: self-referencing canonical, `index,follow`, Open Graph present, no images missing alt.
- JSON-LD parses on all pages. Product + Offer + FAQPage on the 7 tour/rental pages, BreadcrumbList everywhere, LocalBusiness + Organization + AggregateRating on home.

## Prioritized fix list
| Pri | Fix | Who |
|---|---|---|
| P2 | Pin OpenCX widget version and defer load (BBK-specific, check HPB/AKT too) | Whoever manages the OpenCX embed in FH |
| P2 | Compress/convert the two heavy hero images | FareHarbor or site editor |
| P2 | Confirm intended GA4/gtag IDs, remove duplicates | David / FH |
| P3 | 2-hop http://www redirect | FareHarbor |
| P3 | oEmbed 404 in head | FareHarbor (theme) |
| P3 | HTML cache-control only 5 minutes | FareHarbor |

## Affects all FH sites (shared theme, flag once)
Cross-checked mobile Lighthouse on sibling homepages the same day: **HPB 32, AKT 40, BBK 37**. Same signature on all three.
- Lab mobile LCP 10 to 12 s and TBT 1 to 5 s on every FH site tested.
- Page weight 6 to 8.6 MB and 1.7 to 2.8 MB of unused JavaScript. Biggest bundles come from the theme's CloudFront `static/cache/js/output.*.js` files (about 380 KB, 190 KB and 100 KB unused on BBK alone) plus multiple gtag loads.
- Unused CSS flagged at about 108 KB.
- `wp-json/oembed` discovery links 404.
- Ticket path: FareHarbor (Kevin Schmitt / Jasantha Mari). Stage only, no live edits.
