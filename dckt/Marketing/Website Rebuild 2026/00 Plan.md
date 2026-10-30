# Website Rebuild 2026: doorcountykayaktours.com on Astro

*Started 2026-10-16. Target swap: the week of Oct 19 to 25, 2026. Nothing is live, DNS is untouched, nothing sent or spent. Every step that spends money or changes a live surface waits for David's OK in that turn.*

**Status (2026-10-16, 1st session):** inventory done (121 URLs, 224 content images, every FareHarbor item id resolved), research pulled (GSC/GA4 12 months, existing audits), needs list below. Repo at `~/Projects/dckt-site` builds all 121 URLs (same paths as live, 0 missing, 0 extra). Home, Cave Point tour page and the pregnancy post are rebuilt; the other 118 are faithful ports. Preview runs locally at http://localhost:4321 (not on the internet yet).

**David's two calls today (2026-10-16, mid-build):** (1) the home hero flips to e-bikes on Oct 1 and back to kayaks on Apr 1, built in (`src/data/season.ts`); (2) no weather forecasting on the public site for now, it could scare bookings off. The conditions strip and 7-day row were removed from every page; the design stays parked in section 4 and in `src/data/conditions.ts` for whenever he wants it.

---

## 1. What I need from David (numbered, in order of urgency)

Items 1 to 4 gate the swap. 5 to 12 gate specific features and can trail by a day or two.

1. **GoDaddy login (registrar for doorcountykayaktours.com).** Registered 2004, renews 2028-07-24, nameservers are `cody/lucy.ns.cloudflare.com`. That Cloudflare zone is FareHarbor's (the vault's DMARC request went to support@fareharbor.com, which confirms FH controls DNS today). The swap means changing nameservers at GoDaddy to a Cloudflare account David owns. I can do it over the Chrome bridge once I have the login, or David does it in 3 clicks while I watch. **Nothing changes until David says go.**
2. **A Cloudflare account under David (free plan).** Hosting recommendation is Cloudflare Pages (section 3). If he already has one for another brand, which email? If not, create one at cloudflare.com with doorcountykayaking@gmail.com and I take it from there. The zone has to be added and the current DNS records copied (MX smtp.google.com, SPF with websitewelcome + amazonses, 3 SES DKIM CNAMEs, DMARC, Google site verification, the `dc-32bfd96faabf` MX) before nameservers move, so email never drops.
3. **FareHarbor: confirm the embed settings stay as-is.** Booking uses `fareharbor.com/embeds/api/v1/` lightframes and these items (all resolved from the live site, names from the public FH item API): Cave Point Kayak Tour 5669, Cave Point / Whitefish Dunes 1/2 Day 156126, Door Bluff Shipwreck 23855, Door Bluff 1/2 Day 156132, Eco-Estuary 6883, Cana Island 1/2 Day 149338, Fall Kayak 32973, Sunset Kayak Tour 5671 (not run; page stays but will not sell it), Kayak Rental 24268, Paddle Board Rental 5896, SUP Yoga 24492, Cave Point E-Bike Tour 208420, E-Bike Rental Cave Point 221394, Peninsula State Park E-Bike Tour 208419 (not offered), Sunset Glow Roll 216710 (paused), Fish Creek E-Bike Self-Rental 307122, Quad Bike 69326, Death's Door E-bike & Hike 379683, Cave Point Photography Hike 462554, Cheese Curd Walking Tour 221396, Cheese Cheers Trivia 515638, Wine Charcuterie Bingo 541967, Sauna Experience 584699, Sauna Tent 578353, Ice Shack 584407, House of Clouds 631526, Slime Time 647704, Guide Training Camp 44270, Gift Cards 5784. "Book Now" flow id 968496, second flow 291521. Questions: (a) which of these should the new site still sell (my default: kayak tours, kayak and SUP rentals, e-bike tour and rentals, gift cards; everything else stays reachable but un-promoted), (b) does the FareHarbor dashboard have the GA4 property `G-2CHJ9R6QSF` set under Integrations so lightframe bookings keep attributing (the live embed pageviews in GA4 say yes, just confirm), (c) OK to add `?ref=` placement tags to every book link so bookings can be matched to pages, quiz results and emails in the Advanced Bookings report.
4. **Go/no-go on the swap window itself.** Thursday Oct 22 evening is my proposed cutover (section 6). Say the word or move it.
5. **Google Tag Manager `GTM-PPSHWZB`: who has publish access?** Unverified since the Funnel Lab. The new site can run without GTM (GA4, Meta pixel and Clarity hard-coded in the layout, which is what the WP theme does today anyway). If nobody can publish to that container, I leave it out and we lose nothing. If David wants GTM for future tests, I need the Google account that owns it.
6. **GA4 property 320677015 / `G-2CHJ9R6QSF`:** I already read it through google-dckt. Nothing needed unless David wants a fresh property for the new site (I recommend keeping the same one so year-over-year holds).
7. **Microsoft Clarity:** project `xdp299xhtv` exists under dwrack81@gmail.com (never confirmed working on the WP site; the Clarity MCP returns an error for every project today, verified 2026-10-16). I will put the tag in the new site. David: log in once at clarity.microsoft.com and confirm the project still exists and the id matches, or tell me to create a new one.
8. **Meta pixel `421987437994175`:** keeps firing from the new site. Nothing needed from David unless he wants the Conversions API added later.
9. **WordPress export:** I am NOT using the wp-admin creds (2FA to his personal Gmail). The public crawl got everything: titles, metas, H1s, body text, images, JSON-LD, FareHarbor links. Only thing a WP export adds is draft posts and the media library's unused files. If David wants those, he exports Tools > Export > All content once and drops the XML in `Marketing/Website Rebuild 2026/`. Optional.
10. **Photo library (and one fall e-bike shot):** I have the Canva export (527 photos, 80 videos at 1080p) and the 224 images the live site uses (downloaded to `inventory/images/`). Missing: 4K/RAW originals of the drone and sea-cave shots, and any 2026 photos not uploaded to Canva. Where do the masters live (phone, Google Photos, a drive)? One folder of the 30 best originals makes the hero sections pop; I can work with what I have otherwise. Specific ask: one fat-tire e-bike photo in fall color on Lake Shore Road (none exists), for the Oct-Nov hero.
11. **Cave Point camera source (section 4): PARKED.** David said 2026-10-16 to steer clear of weather forecasting for now. Nothing needed. The two photo options stay written up in section 4 for later.
12. **Lead engine endpoints (section 5):** the engine API is `https://zrnrjszada.execute-api.us-west-2.amazonaws.com` (w.js widget, /lead, /quiz, /booked). DCKT is `enabled: false`, `quiz_enabled: false`, and `brands.json` has an empty address and phone for dckt (the engine refuses to send with an empty postal address). I need David's OK to (a) set dckt address `8442 State Highway 42, Fish Creek, WI 54212` and phone `920-868-1400` in brands.json, (b) flip dckt to enabled with the quiz popup only, (c) confirm the email sender stays `info@doorcountykayaktours.com` through SES us-west-2 (verified identity).
13. **Facts still open** (from the Funnel Lab; the site ships with these marked, not guessed): tandem weight 500 vs 550 lb; Door Bluff meeting point street number (live site 1310 Garrett Bay Rd, David remembers 1130, OSM says the ramp is nearest 1216); cancellation window 24h (brand-facts memory) vs 48h (FareHarbor default) vs "free reschedule"; credit policy decisions 5 to 7; whether the Cana Island 1/2 day and Fall Kayak items are real 2027 products.
14. **Copy sign-off:** home, Cave Point and one blog post are the finished examples this week. David reads them on the preview URL before the swap. The other 118 pages ship as faithful ports of the live copy (with fact corrections) and get rewritten one at a time after launch.

---

## 2. What the live site is (inventory, verified 2026-10-16)

- 121 URLs: 35 pages, 32 activities, 54 posts. Full export in `inventory/` (one JSON per URL plus `_index.md`, `_images.json`, `images/`).
- Platform: FareHarbor Sites theme "the-anchor" on WordPress VIP behind Cloudflare. Scripts loaded: jQuery 3.6, FareHarbor embeds API, Elfsight (review widget in the footer, app 69404596), OpenCX widget (Cedar), WP stats, Complianz cookie banner. Hard-coded tags: GTM-PPSHWZB, GA4 G-2CHJ9R6QSF, old UA-1996171-1, Meta pixel 421987437994175. No Clarity.
- Schema today: Organization + LocalBusiness (address 6329 Wisconsin 57, Sturgeon Bay, no hours) + WebSite on the home page; BreadcrumbList on every page; Article on most posts; one VideoObject on the Cave Point page (the 319k-view YouTube video). No Product/Offer, no FAQPage, no AggregateRating anywhere.
- Review count is not stated anywhere on the site. New site: "1,000+ Google reviews, 4.9 stars" (1,011 / 4.9 verified via GBP API 2026-10-15).
- Facts on the live site that are wrong and will not be carried over: Sunset Kayak Tour (does not run), Peninsula State Park e-bike tour (not offered), "All Ages" on Cave Point (kids 4+), photo package ($20, discontinued), ACA claims (none found on site, none added), $59 pricing (none found on site).

### Where the traffic is (GSC, 12 months to 2026-10-14)

| Page | Clicks | Impr. | Pos. | What it ranks for |
|:-|-:|-:|-:|:-|
| / | 4,318 | 88,714 | 16.1 | door county kayak tours (924 clicks, pos 1.1), door county kayaking, kayak door county, kayak rental door county |
| /e-bike-tours/ | 1,183 | 19,989 | 11.4 | door county bike rental(s), bike rental door county, ebike rental door county |
| /kayak-tours/cave-point-county-park/ | 855 | 47,506 | 10.9 | cave point kayak tour (pos 2.9), cave point kayak(ing), cave point county park (pos 14.8 on 14k impr.) |
| /blog/door-county-bike-routes/ | 813 | 22,730 | 6.6 | door county bike trails, biking in door county |
| /blog/embracing-kayaking-during-pregnancy... | 793 | 53,253 | 3.2 | can you kayak while pregnant (and 8 variants, all pos 2) |
| /blog/7-of-the-best-hiking-trails-in-door-county/ | 727 | 24,068 | 6.5 | best hikes in door county (pos 4.1) |
| /blog/7-reasons-fish-creek... | 712 | 148,087 | 8.7 | fish creek wi / fish creek wisconsin (pos 11, 0.4% CTR) |
| /sauna-experience/ | 325 | 3,802 | 6.3 | door county sauna, sauna door county |
| /kayak-tours/door-bluff-county-park-shipwreck/ | 255 | 9,087 | 12.0 | door bluff shipwreck tour (pos 1), shipwreck kayak tour door county |
| /blog/7-reasons-why-baileys-harbor... | 264 | 58,652 | 10.5 | baileys harbor (16k impr., pos 11.8) |

GA4 (property 320677015, 12 months): home 34.8k views, Cave Point tour page 10.4k, /kayak-tours/ 5.1k, Door Bluff 3.5k, e-bike tours 2.8k, half-day 2.2k. Peak months July and August 2026 (17.7k and 17.4k sessions, $20.7k and $16.4k GA4 deposit revenue). Blog traffic is big in impressions and converts at zero.

Full tables: `research/01` to `research/06`. Existing audits synthesized in `research/07`.

---

## 3. Architecture and hosting

**Stack:** Astro (static output), one layout, content in Markdown + a typed `site.ts` for facts (prices, ages, weight limits, phone, address) so a fact changes in one file. Images through Astro's image pipeline (sharp) to WebP/AVIF with the global size rules (hero 1920px ~400-700 KB, inline 1600px ~150-400 KB). No client framework; the only JS is the FareHarbor embeds API, the conditions strip, the quiz popup, the menu, and the tags.

**Host: Cloudflare Pages.** Why over Netlify:
- DNS is already on Cloudflare nameservers (FH's account). Moving the zone into David's own Cloudflare account puts DNS, CDN, SSL, redirects and hosting in one place, and the nameserver change at GoDaddy is the only registrar touch.
- Pages Functions + KV give the two tiny server bits we want (a cached Open-Meteo/NOAA conditions endpoint and the daily Cave Point photo) for $0 on the free tier.
- Git-push deploys with preview URLs per branch (David reviews `*.pages.dev` before DNS moves).
- The Elevated Tides rebuild already picked the same stack, so the two sites share patterns and the knowledge stays in one place.

Netlify would be fine too (free, forms built in) but splits DNS from hosting and its functions quota is smaller. If David already has a Netlify account he loves, say so; nothing in the build is host-specific.

**Repo:** `~/Projects/dckt-site`, GitHub https://github.com/dwrack/dckt-site (private, created 2026-10-16), branch `main` will auto-deploy to production once Cloudflare Pages is connected; every other branch gets a preview URL. **See it now on this laptop:** `cd ~/Projects/dckt-site && npm run build && npx astro preview --port 4321`, then http://localhost:4321/ (the home page, `/kayak-tours/cave-point-county-park/`, `/blog/embracing-kayaking-during-pregnancy-a-guide-to-safe-paddling/`).

**URL rule:** every one of the 121 live URLs renders at the same path with a trailing slash (Astro `trailingSlash: 'always'`, `build.format: 'directory'`). No redirects needed. Pagination and category archives (`/blog/page/N/`, `/blog/category/...`) are rebuilt by Astro from the same slugs.

### URL map (121, by what happens to each)

| Group | URLs | Treatment |
|:-|-:|:-|
| Home | 1 | New design, new copy (finished example this week) |
| Kayak tour pages | 9 (`/kayak-tours/` + 8 children) | Cave Point rewritten now; the rest ported with corrected facts (price, ages, weight, meeting point), Product/Offer + FAQ schema, same FH item. `/sunset-tour/` stays as a page that says we do not run it and points to Cave Point (no 404, no sale). `/guide-training-camp/` stays (it is the hiring/waiver item). |
| E-bike pages | 8 (`/e-bike-tours/`, `/activities/*` x3, `/peninsula-state-park-fat-tire-e-bike-tour/`, `/sunset-glow-roll-e-bike-tour/`, `/ice-castles-caves-e-bike-tour/`, `/sister-bay-e-bike-rental/`, `/deaths-door-ebike-hike/`) | Ported. Peninsula and Glow Roll pages say "not offered this season" above the fold and send to the Cave Point rental. |
| Rentals and SUP | 4 (`/kayak-rentals/`, `/sup/`, `/sup/paddle-board-rental/`, `/sup/sup-yoga/`) | Ported, Product schema |
| Sauna, food tours, odd activities | 9 (sauna x4, cheese curd, trivia, wine bingo, house of clouds, slime time, ice shack, photography hike) | Ported as-is, noindex only where David says the product is dead |
| Blog index + 54 posts | 55 | Ported from inventory body text; one post rewritten as the finished example (the pregnancy post, 793 clicks and position 2 on 9 queries, or the hiking post; pick in section 7). Article schema with real dates and author "Door County Kayak Tours". The 8 posts already POLISHED in `SEO Content/Blog Polished/` ship with the polished copy. Town pillars (Fish Creek, Baileys Harbor, Ephraim) ship with the pillar drafts from `SEO Content/Towns/`. |
| Utility | 20 (about, contact, gallery, gift cards x2, jobs x2, brochure, reviews x2, events, lodging, map, privacy x2, terms, data deletion, opt-out, unsubscribe, affiliates) | Ported. Forms (contact, brochure, job application, affiliates) go to a Cloudflare Pages Function that emails info@ via SES us-west-2. |
| Junk | 6 (`/claude-ads-mcp-2/`, `/contest-giveaway-entered/`, `/e-bike-contest-giveaway-entered/`, `/covid-19-...`, `/door-county-e-bike-tour-giveaway/`, `/door-county-gift-card-giveaway/`, `/new-door-county-activities-for-2025/`, `/download-your-kayak-photos/`, `/how-was-your-tour/`) | Render at the same URL with `noindex` so nothing 404s, content minimal. `/download-your-kayak-photos/` says the photo package ended. |

**Links and redirects (added 2026-10-16, from the keyword map's crawl findings):**
- The ported pages now carry their real HTML, not flattened text: 650 internal links on 78 pages survived the port (the first version had none). The WordPress theme's price tables, badges, buttons and the discontinued photo-package lines are stripped.
- About 50 links on the live site point at URLs that never existed (`/cave-point-half-day-kayak-tour/`, `/cave-point/`, `/deaths-door-shipwreck-kayak-tour/`, `/eco-estuary-kayak-tour/` and about 20 more, left over from drafts with idealized slugs). They are rewritten to the real pages inside the ported HTML, and `public/_redirects` 301s them too in case Google or a partner has them.
- Google still sends clicks to 8 deleted posts that 404 on the live site today (the "ten celebrities" post alone had 37 clicks). The new site 301s each to its nearest live page instead of 404ing. WordPress category, tag, page and year archives 301 to `/blog/`.
- `/7-of-the-best-hiking-trails-in-door-county/` (no `/blog/`) resolves on WordPress and gets 8 clicks; it 301s to the real post.
- Zero dead internal links in the built site (checked across all 121 pages, 4,900+ internal hrefs, 2026-10-16).

The tour and activity "hub" pages (`/kayak-tours/`, `/e-bike-tours/`, `/activities/`) get the family-first vs Cave Point-first test hooks the Funnel Lab asked for (card c14): two hero variants switched by a `?v=` param now, by the A/B script later.

---

## 4. Weather and Cave Point conditions (PARKED 2026-10-16 at David's request)

*David, 2026-10-16: "I'm hesitant to do too much weather forecasting, it might drive people away from booking, I'd rather steer clear of that for now." So: no forecast, no wind numbers, no GREEN/YELLOW/RED on the public site. The reassurance copy stays ("we watch the wind so you don't have to", free reschedule). The design below is kept so it can be switched on later; the code is in `~/Projects/dckt-site/src/data/conditions.ts` and `src/components/Conditions.astro`, not rendered on any page.*

*How Elevated Tides does it (read 2026-10-16 from `~/Projects/elevatedtides-site/src/data/conditions.ts` and `LivingSky.astro`):* Open-Meteo forecast + USGS river gauges, fetched at build time as a snapshot and refreshed in the browser; a canvas hero draws the real sun and moon position over a photo; the headline changes with the sky; a "next 24 hours" strip scores each bookable hour and names the best one. No key, no server.

**DCKT version, "Cave Point right now":**
- Point: 44.95N 87.04W (the 2026 cancellation analysis point, just off the Cave Point cliffs). Open-Meteo marine returns waves there (verified 2026-10-16: wave height, direction, period, wind-wave height, hourly, 7 days). Open-Meteo forecast returns wind speed, gusts, direction, sky, temp, sunrise/sunset. NDBC buoy 45002 (mid-lake) gives a real observed wind and seas as a cross-check. Water temperature: Open-Meteo has no lake temp and NOAA station 9087072 (Sturgeon Bay Canal) returned no water-temp product (checked 2026-10-16), so water temp comes from NOAA GLERL's Lake Michigan surface analysis [VERIFY endpoint] or the guides' morning reading; until then the strip shows air, wind, gusts and waves only.
- The strip (home hero and every Cave Point page): "Cave Point right now: wind 9 mph NW, waves 0.7 ft, 61F, sunny. Today's tours: GREEN." The GREEN/YELLOW/RED call uses the Cold Water and wind thresholds from the 11-beat playbook (`project_guide_log_audio_video`) and the cancellation analysis; the exact numbers are David's to confirm before the colors show [VERIFY thresholds: proposed GREEN under 12 mph and waves under 1.5 ft, YELLOW to 18 mph / 2.5 ft, RED above]. In the off-season the strip says "Tours return May 2027" and still shows the weather, which is the nicest thing a Door County site can show in January.
- Next 7 days: a row of day chips (wind, waves, sky) with the best paddling day highlighted, and a "book this morning" link into the FareHarbor calendar for that date.
- Built as a Pages Function `/api/conditions` that calls Open-Meteo + NDBC, caches 15 minutes in KV, so 10,000 visitors cost Open-Meteo nothing and the page never waits on a third party. Static fallback snapshot baked at build time.

**The photo: two options with costs**

| | Option A: a real camera | Option B: generated frames keyed to the forecast |
|:-|:-|:-|
| What the visitor sees | A photo of the actual water taken in the last 30 to 60 minutes, time-stamped | A photo-real rendering of Cave Point in today's conditions, labeled "rendered from today's forecast" |
| How | A1: solar + LTE camera (Reolink Go PT Ultra or Spypoint Flex, about $250 to $450 plus a $10 to $15/month LTE plan) on private property with a view of the Jacksonport / Cave Point shoreline, or on the shop building if the water is visible [VERIFY a mounting spot: county park land is off limits without a permit]. Uploads to Cloudflare R2 on a schedule; the site shows the latest. A2 (free): guides text a photo to the TideBot group DM or #dckt-tour-logs each morning; a script on mbp-2 pulls the newest to R2. Works only in season and only on tour days. | One-time set of about 16 frames made with Higgsfield image-to-image from 3 real DCKT photos of the same cliff: {calm, light chop, rough} x {sun, cloud, rain} x {morning, evening} plus winter ice. The conditions function picks the frame whose bucket matches now and each forecast day. |
| Cost | A1 hardware $250 to $450 once, LTE $120 to $180/yr, R2 $0. A2 $0. | About 16 to 24 generations (about 50 to 150 Higgsfield credits on the existing $39/mo plan), half a day of my time, $0 recurring. |
| Risk | Winter ice, battery, vandalism, and a permit question for anything on county land. A2 depends on staff. | It is not a photo and must say so. Honest label, no "live" wording. |
| Verdict | Best for "now," only in season | Needed anyway for the forecast days (nobody can photograph tomorrow). |

**Recommendation:** ship Option B for the 7-day forecast row at launch (it is the only way to render future days), and run A2 (guide photo) for the "right now" slot from May 2027 with A1 as an upgrade if David finds a mounting spot. Until a real photo exists, the "now" slot uses the matching B frame with the honest label. Needs David's OK on Higgsfield credits before I generate.

---

## 4b. Seasonal hero (David, 2026-10-16)

- **Oct 1 to Mar 31: e-bikes lead.** Hero photo is the e-bike shot (fall canopy road Oct-Nov, a winter e-bike shot Dec-Mar), subline sells fall color or winter rides, gold button books the $30/hr Cave Point e-bike rental (item 221394), ghost button goes to the kayak tours for next summer. The tour rows put the e-bike rental and e-bike tour first, kayak tours below with their dates.
- **Apr 1 to Sep 30: kayaks lead.** Cave Point aerial hero, "Paddle into the sea caves" subline, gold button books Cave Point (5669).
- Decided at build time in `src/data/season.ts`, so the site needs a **daily rebuild** for the flip to land on the day: a Cloudflare Pages deploy hook called at 5am CT from a launchd job on davids-mbp-2 (or a GitHub Actions cron). Zero cost. Goes on the Sat Oct 17 list.
- The H1 stays "Door County Kayak Tours" in both modes (it ranks #1 for the brand query).
- Photos: Oct-Nov uses the glow-roll group at sunset (the only strong fall-season e-bike still in the library; there is no true fall-color e-bike photo, so one shot on Lake Shore Road in late October would upgrade this hero). Dec-Mar uses the rider beside the Cave Point ice castles (Canva library).

## 4c. Launch rules added 2026-10-17

- **Shared tour page.** Every tour, rental and sauna page now renders through one component (`src/components/TourPage.astro`): hero, price, at-a-glance box, half-day upsell (above the fold, mid-page, sidebar), logistics, FAQ + schema, quiz card, related tours, sticky mobile book bar. Facts come from one catalog (`src/data/tours.ts`), so a price changes in one place.
- **Open facts cannot ship by accident.** Any page with an unanswered question shows a yellow "Preview only" note. `npm run build:prod` refuses to finish while any note remains, so the swap physically cannot happen with a guessed price or a dead product on sale. Today's notes are the questions in section 1 item 13 plus: Cana Island price and status, Fall Kayak price ($55 live vs $63 in FareHarbor), e-bike rider minimum age, Fish Creek self-rental and Death's Door e-bike and hike for 2027, surrey bikes after the fleet sale, SUP Yoga 2027, the three sauna products for winter 2026-27, and the Airstream price.
- **Launch gate.** `npm run preflight` checks every built page: all 121 live URLs exist, titles and metas present and unique, one H1, JSON-LD parses, no dead internal links, every FareHarbor link carries a `ref=site-...` tag. Must pass with `--prod` before DNS moves.
- **Titles: change money pages now, blogs later.** The rebuilt tour and hub pages get new titles at launch. The 54 blog posts keep their live titles through the swap, so any ranking wobble can be traced to the move and not to copy changes. The CTR title fixes in file 10 (pregnancy post, saunas, town pillars) go live two weeks after the swap, once Search Console shows the new site indexed and stable.
- **Daily rebuild.** `.github/workflows/daily-rebuild.yml` calls a Cloudflare Pages deploy hook every morning so the seasonal hero flips on the right date. It does nothing until the hook URL is saved as the repo secret `CF_PAGES_DEPLOY_HOOK` (comes with the Cloudflare account, needs item 2).

## 5. Lead capture, tags and tracking

- **Popup = quiz (card c21 = A), email unlocks the result (c19 = B), help-first nurture (c20 = A).** Quiz A ("Which Door County trip fits your crew?") and B ("What's your Door County summer?") live in `~/Projects/fh-lead-engine-quiz-dckt` (`engine/quiz/dckt.json`, previews `previews/quiz/dckt-A.html` and `-B.html`). The site loads the engine widget with one script tag in the layout: `<script async src="https://zrnrjszada.execute-api.us-west-2.amazonaws.com/w.js?b=dckt"></script>`. The widget already handles the 20-second / exit-intent trigger, the 3-day snooze, localStorage and the `/lead` POST. Quiz mode in the widget is a hub-side change (the NPB note says `widget.js` has no quiz mode yet); until it lands, the popup links to `/quiz/` on the engine, rendered in a lightbox.
- **Capture points on the site:** (1) the quiz popup, (2) a "Not sure which tour? 30-second quiz" card on every tour page and the hubs, (3) the footer "Conditions email: get the Cave Point forecast every Thursday in season" (new lead magnet, feeds the same engine with tag `magnet-conditions`), (4) the gift-card page ("send me the gift card guide"), (5) blog posts: an inline "Plan your paddle" box after paragraph 3 that opens the quiz (this is how blog traffic finally gets a path to booking).
- **Lead magnets:** the Thursday conditions email (zero production cost, it is the strip in email form), and "The first-timer's Cave Point checklist" (one page PDF built from the existing what-to-bring copy, delivered by the nurture's email 5).
- **`?ref=` tags:** every FareHarbor link carries `ref=<placement>` instead of today's `ref=https://www.doorcountykayaktours.com`. Scheme: `site-home-hero`, `site-home-grid`, `site-cavepoint-hero`, `site-cavepoint-sticky`, `site-halfday-upsell`, `site-blog-<slug>`, `site-conditions-<date>`, `quiz-<result>`, `email-<n>`. FareHarbor shows `ref` in the Advanced Bookings report, which is the one place attribution survives the lightframe (GA4 loses source through FareHarbor checkout, see memory `feedback_ga4_fareharbor_attribution`). The engine's `/booked` webhook matches a booking to a lead by email.
- **Tracking in the layout:** GA4 `G-2CHJ9R6QSF` (gtag, same property), Meta pixel `421987437994175`, Clarity `xdp299xhtv`, and GTM `GTM-PPSHWZB` only if David confirms publish access (otherwise omitted). Events: `fh_click` with placement, `quiz_start`, `quiz_result`, `lead_capture`, `conditions_view`, `call_click`. Cookie banner: keep a light consent bar (Complianz is gone with WordPress); the tags above fire on consent in the EU only, immediately in the US.

---

## 6. Day-by-day schedule (swap week)

| Day | What ships | Needs from David |
|:-|:-|:-|
| Fri Oct 16 (today) | Inventory, research, this plan, repo, home + Cave Point + one blog post on a local build | Read the needs list; answer 1, 2, 3 |
| Sat Oct 17 | All 9 kayak tour pages, hubs, rentals, e-bike pages rebuilt with corrected facts; TouristTrip/Product/FAQ schema on every tour page; daily rebuild hook for the seasonal hero | 7 (Clarity), 13 (facts) |
| Sun Oct 18 | All 54 posts ported (polished copies where they exist), utility pages, forms, 404, sitemap, robots, llms.txt. First preview URL on Cloudflare Pages | 2 (Cloudflare account) so the preview URL exists |
| Mon Oct 19 | Image pass (every image optimized and renamed), quiz popup wired, ref tags, tags verified in GA4 DebugView and Meta test events | 5 (GTM), 12 (engine) |
| Tue Oct 20 | Design pass (`/impeccable` critique), mobile QA on real phone sizes, Lighthouse on every template, crawl the preview with the same inventory script and diff titles/H1/metas/links against the live site | David reads home, Cave Point, blog post on the preview |
| Wed Oct 21 | Fixes from David's read; Cloudflare zone created with every DNS record copied; forms tested; redirects for the few WP paths outside the sitemaps (`/blog/category/*`, `/blog/page/*`, `/blog/2008/04/`) | 1 (GoDaddy) ready |
| Thu Oct 22, 7pm CT | **Cutover:** nameservers to David's Cloudflare, custom domain on Pages, SSL, www to apex rule. Old WP site stays up at FareHarbor's end untouched as the fallback (switching nameservers back reverts in minutes) | David's go in that turn |
| Fri Oct 23 | Post-swap checks: GSC URL inspection on 20 URLs, sitemap resubmitted, GA4 real-time, Meta pixel events, FareHarbor test booking, email still delivering | |
| Sat Oct 24 to Sun 25 | Watch GSC coverage and GA4 for drops; fix anything; write the memory and hand-over notes | |

Rollback at any point: set GoDaddy nameservers back to cody/lucy.ns.cloudflare.com. The WordPress site is never deleted during this project.

---

## 7. Decisions I made without asking (say so if wrong)

- Keep `www.` as canonical (that is what ranks today; apex redirects to www).
- Brand colors from the Canva kit (#1c3361 navy, #2373be blue, #4eb3df sky, #f5b752 yellow, #ea66a1 pink) with the pink held to accents under 10% of any screen; a toned off-white, never pure white. Type: an editorial serif for display, system sans for body, self-hosted (no Google Fonts call).
- The finished blog example is the pregnancy post (793 clicks, position 2 on nine queries, 53k impressions, the single best organic page outside the tours), rewritten from the POLISHED version in `SEO Content/Blog Polished/`.
- "1,000+ Google reviews, 4.9 stars" is the only review claim on the site. No "2,000+" anywhere.
- Kids 4+ on every kayak tour, bike trailers 2+, dogs on any tour when calm, tandem 500 lb and single 285 lb shown as the limits with the words "tell us at booking if anyone is close."
- Sunset kayak page kept at its URL but sells nothing.

## 8. Files in this folder

- `00 Plan.md` (this file)
- `inventory/` : one JSON per live URL, `_index.md`, `_images.json`, `images/` (originals)
- `research/01-06` : GSC and GA4 pulls (2026-10-16)
- `research/07 Existing SEO + AEO Findings (synthesis).md`
- `10 Keyword + Entity Map.md` : per-URL primary and secondary queries from GSC, proposed titles and H1s for all 121 URLs, site-wide entity list, opportunity tiers (page-2 town pages with 53k+ impressions, CTR fixes at position 1-4), 20 internal links to add, and the dead-link remap
- `11 Schema Plan.md` : JSON-LD per template, as implemented
- `12 Conditions Design.md` : the weather strip spec and the API shapes (parked, see section 4)

## 9. Session log

- 2026-10-26: David answered round 1 from the guide Mac (repo not reachable there, no code changed). 2027 lineup cut to the core plus paddle board rental; cancel 48 hrs; e-bike riders 12+; calm dogs on every tour. Logged at the top of `13 Questions for David.md`, about 50 of 109 cleared. Apply in the repo next session on the main laptop.

- 2026-10-19: all 27 tour, rental, sauna and hub pages rebuilt on the shared TourPage, each fact-checked and SEO-checked by separate reviewers, then a cross-page consistency pass (25 findings, all resolved or parked as questions). 16 internal links added to top blog posts; stale facts ($4 park fee, age 8, no-dogs, sunset tour) removed from 15 ported posts. Catalog photos all checked by eye; watermarked hero replaced. Winter e-bike tour and Cana Island shown as paused until confirmed. Preflight: 0 errors on 121 pages. 109 open questions consolidated in `13 Questions for David.md` (production build blocked until answered). Pushed to dwrack/dckt-site (d6057a7). Nothing live, DNS untouched.

- 2026-10-16: crawl, research, plan, repo scaffold, all 121 URLs building, home + Cave Point + pregnancy post designed, keyword map (file 10), schema plan (11), parked conditions design (12). David: seasonal hero (e-bikes Oct-Mar), no weather forecasting. Weather strip removed. Private GitHub repo dwrack/dckt-site pushed. Nothing live, DNS untouched.
