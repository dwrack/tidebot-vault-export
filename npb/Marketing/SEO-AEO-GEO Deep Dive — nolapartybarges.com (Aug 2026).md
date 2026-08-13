# NPB — SEO / AEO / GEO Deep Dive

**Date:** 2026-08-13
**Property:** `sc-domain:nolapartybarges.com`
**Method:** Full crawl of all 134 sitemap URLs (titles, metas, H-structure, word counts, internal link graph), GSC 90d at query/page/country/searchAppearance level, live SERP pulls, backlink and anchor profile, robots/llms.txt, clickstream-normalized volumes.
**Companion:** `SEO-AEO-GEO Audit — nolapartybarges.com (Aug 2026).md` — the first pass. This goes after what that one didn't cover.

---

## Executive Summary

The first audit said the problem was entity naming. That's still true and still the highest-leverage fix. But a full crawl surfaces something bigger sitting on top of it.

**183,000 impressions across 17 pages are converting at 0.47%.** Not 4.7% — 0.47%. At a merely ordinary 2.5% those pages would produce about **4,570 clicks a quarter instead of 854**. That single gap is roughly 3,700 clicks per quarter, and it dwarfs every ranking opportunity discussed so far. You do not have a rankings problem on this domain. You have a **rankings-that-don't-convert-to-clicks** problem.

Underneath that, three structural issues the first pass missed:

- **26 programmatic location pages** (Baton Rouge, Gretna, Metairie, Slidell, Mississippi) produced **23 clicks in 90 days**. Eighteen of them got zero. That's 19% of your URLs earning 0.29 clicks per page per month.
- **Your `/llms.txt` exists — and all 48 links in it are malformed.** It's the file AI engines read to understand you, it uses `[text] (url)` with a space so nothing parses as a link, two URLs 404, and it introduces itself as *"New Orleans Pedal Barge offers New Orleans pedal party boat booze cruises."*
- **The word "barge" is poisoning your impressions.** `/boat-rental/` ranks for *barge rental, barge hire, barge boat for rent, 50 person boat rental* at positions 40-98. It has 13,505 impressions and 56 clicks because it's matching industrial shipping-barge queries.

Good news the crawl confirmed: server speed is fine (127ms TTFB), AI crawlers are not blocked, 404s return real 404s, www→non-www 301 is correct, and no page is missing a meta description.

---

## 1. The CTR Catastrophe

Every page with 3,000+ impressions and CTR under 1.3%:

| Page | Clicks | Impressions | CTR | Pos |
|---|---|---|---|---|
| /how-much-do-you-need-to-budget-...-2024/ | 378 | 41,274 | 0.92% | 4.3 |
| /exploring-december-weather-...-what-to-wear/ | 154 | 40,346 | 0.38% | 5.5 |
| **/krewe-of-endymion/** | **1** | **14,440** | **0.01%** | 9.8 |
| /boat-rental/ | 56 | 13,505 | 0.41% | 15.1 |
| /our-boats/ | 11 | 8,990 | 0.12% | 7.5 |
| /contact-us/ | 5 | 8,510 | 0.06% | 7.1 |
| /new-orleans-booze-cruise-giveaway/ | 1 | 8,023 | 0.01% | 6.0 |
| /1253-2/ | 23 | 6,512 | 0.35% | 7.1 |
| **/service-areas/** | **0** | **6,173** | **0.00%** | 5.8 |
| /new-orleans-swamp-tours-with-fishing.../ | 44 | 5,582 | 0.79% | 24.9 |
| /beyond-the-tourist-hotspots.../ | 35 | 5,428 | 0.64% | 12.4 |
| /the-best-self-guided-walking-tour.../ | 13 | 5,372 | 0.24% | 21.7 |
| /a-guide-to-new-orleans-housing-styles/ | 21 | 4,583 | 0.46% | 10.4 |
| /new-orleans-booze-cruise/ | 16 | 4,212 | 0.38% | 7.0 |
| /swamp-tour-questions/ | 30 | 3,715 | 0.81% | 6.2 |
| /the-cajun-queen/ | 42 | 3,270 | 1.28% | 14.5 |
| /unveiling-the-charm-...-dress-code/ | 24 | 3,052 | 0.79% | 6.7 |
| **TOTAL** | **854** | **182,987** | **0.47%** | |

Three deserve individual comment.

**`/krewe-of-endymion/` — 14,298 impressions for "endymion parade route", exactly zero clicks.** Not one, in 90 days, at position 9.7. It's a Mardi Gras parade route page. People searching a parade route want a map, get it from the AI Overview or the top three results, and never scroll. The query has no commercial relationship to booking a boat. This page is 8% of your total impressions and contributes nothing.

**`/service-areas/` — 6,173 impressions, 0 clicks, position 5.8.** Ranking well, converting nobody.

**`/our-boats/` — ranks #3.2 for "party boat new orleans" (577 impressions, 1 click).** Your homepage also ranks for that term. Two of your pages are competing and Google picked the one that converts at 0.17%. That's straight internal cannibalization on your best commercial keyword.

### Why it's happening

Not one cause, three:

1. **Titles truncate.** 67 of 134 pages exceed 60 characters, so Google cuts them. Worst is 100 chars.
2. **Informational queries that AI now answers.** Weather, budgets, parade routes, dress codes. You rank, the AI Overview answers, nobody clicks. You're #1 in the AI Overview on 21 December-weather variants.
3. **Wrong-intent matching.** See §4.

---

## 2. Internal Link Architecture

Crawled all 134 pages with nav, header and footer stripped, so this is genuine in-content linking.

| Finding | Count |
|---|---|
| Pages with **zero** inbound content links (orphans) | **15** |
| Pages with only 1-2 inbound links | **78** |
| Pages with zero H2s | **58** |
| Pages with multiple H1s | 7 |
| Pages missing an H1 | 1 |

**93 of 134 pages (69%) have two or fewer in-content links pointing at them.** Link equity isn't flowing anywhere.

Where it does flow:

| Page | Inbound content links |
|---|---|
| **/blog/** | **91** |
| /the-freaky-tiki/ | 32 |
| /pedal-bike-barge-cruise/ | 27 |
| /the-cajun-queen/ | 20 |
| /the-twerkin-tiki/ | 19 |
| /pedal-bike-bar/ | 15 |
| /bentley-bayou-cruiser/ | 10 |
| **/** (homepage) | **8** |

The blog index absorbs 91 internal links — more than every boat page combined — and it earned 2 clicks in 90 days. Meanwhile the homepage, which carries essentially all your commercial rankings, gets 8.

**Orphaned commercial pages** (money pages nothing links to):

| Page | Words |
|---|---|
| /boat-rental/ | 434 |
| /our-boats/ | 774 |
| /the-cajun-tiki-holiday-express/ | 541 |
| /bow-fishing-and-sightseeing-charter-w-captain-glenn/ | 1,088 |
| /new-orleans-booze-cruise-giveaway/ | 546 |

---

## 3. Content Inventory Problems

### 3a. The programmatic location cluster is dead

26 pages targeting Baton Rouge, Gretna, Metairie, Slidell and Mississippi:

| Metric | Value |
|---|---|
| Pages | 26 (19% of the site) |
| Clicks, 90 days | **23** |
| Impressions | 3,147 |
| CTR | 0.73% |
| Pages with zero clicks | **18 of 26** |
| Clicks per page per month | **0.29** |

Baton Rouge is 80 miles from Bayou Bienvenue. These pages promise a local experience you don't deliver locally, and Google has responded accordingly — several sit at position 30-60. They dilute topical focus and add crawl overhead for a quarter-click a month each.

Recommendation: consolidate the whole cluster into **one** honest "driving to us from Baton Rouge" page and 301 the rest into it. Keep `/party-boats-near-metairie/` (position 2.6) and `/party-boats-near-gretna/` (position 10.2) — those are genuinely nearby.

### 3b. Duplicate and junk URLs indexed

| URL | Impressions | Problem |
|---|---|---|
| /beyond-the-tourist-hotspots-exploring-**unique**-neighborhoods-in-new-orleans/ | 5,428 | Two versions of the same post |
| /beyond-the-tourist-hotspots-exploring-neighborhoods-in-new-orleans/ | 1 | ↑ duplicate |
| /sunset-cocktail-cruise-seafood-boil/ | 1,138 | Two versions |
| /sunset-cocktail-cruise-seafood-boil-**new-orleans**/ | 27 | ↑ duplicate |
| /swamp-tours-in-new-orleans-the-ultimate-bayou-adventure-guide/ | 3 | Two versions |
| /swamp-tours-in-new-orleans/ | 1 | ↑ duplicate |
| /blog/unveiling-new-orleans-weather-in-december-a-style-guide | 1 | Old URL of the December post |
| **/pedal-bike-bar/1000/** | 3 | Junk pagination URL indexed |
| /1253-2/ | 6,512 | WordPress default slug |
| **/category/swamp-tour-comparison/** | **263 @ position 2.08** | Category archive outranking real pages |

### 3c. Duplicate meta descriptions

22 pages share just two meta description strings. Twelve of them use the site tagline — *"New Orleans Pedal Party Boat Booze Cruise & Tours"* — which is both duplicated and off-brand.

---

## 4. The "Barge" Problem

`/boat-rental/` has 13,505 impressions and 56 clicks. Here's what it's ranking for:

| Query | Impressions | Position |
|---|---|---|
| barge rental | 79 | 57.7 |
| 50 person party barges | 60 | 59.6 |
| 50 person boat rental | 24 | 67.2 |
| barge boat party | 9 | 65.1 |
| barge rent | 3 | 80.3 |
| barge parties | 2 | 98.0 |
| barge hire | 1 | 88.0 |
| barge boat for rent | 6 | 43.0 |

Those are **industrial and commercial shipping barge queries.** Somebody searching "barge hire" wants to move freight. You'll never convert them, they'll never click, and their impressions drag your sitewide CTR down — which is a quality signal Google reads.

This is a real, quantifiable cost of the "Party Barge" name that I haven't seen accounted for anywhere. It doesn't mean rename the business. It does mean:

- Don't chase "party barge" keywords in titles or copy — lean on "party boat," "tiki boat," and "swamp tour," which is where the actual buyers are.
- The Site Title decision matters here too. Every additional page carrying "Barge" in the title widens the wrong-intent surface.

---

## 5. AEO / GEO — The Deep Layer

### 5a. AI crawler access: clean ✅

Checked robots.txt against 17 AI agents — GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot, CCBot, Google-Extended, Applebot-Extended, Bytespider, Amazonbot, meta-externalagent, cohere-ai and others. **None are blocked.** The blocklist targets SEO scrapers (MegaIndex, BLEXBot, Barkrowler, Yandex, Baiduspider) which is fine and deliberate.

Two small robots.txt defects:
- `Disallow: /fhbr-console/` and `Disallow: /cdn-cgi/` appear *after* the `Sitemap:` line with no `User-agent:` above them. Orphaned directives — most parsers ignore them.
- No `Host` or explicit canonical hint. Minor.

### 5b. llms.txt exists — and is broken

`/llms.txt` returns 200, real `text/plain`, 10,040 bytes, eight sections. Someone put genuine work into it. Three problems:

**1. All 48 links are malformed.** The file uses `[Booking Portal] (https://...)` — with a space between the bracket and the paren. That is not a markdown link. Every single one fails to parse. The file is a list of plain text with URLs floating next to it.

**2. Two links 404:**
- `https://nolapartybarges.com/home/`
- `https://nolapartybarges.com/how-many-days-in-new-orleans-is-enough/` (the intended clean slug for `/1253-2/` — somebody wrote the link before creating the page)

**3. It introduces you as the wrong business.** The opening lines:

> `# New Orleans Pedal Barge`
> `> New Orleans Pedal Barge offers New Orleans pedal party boat booze cruises and tours...`

This is the single document written specifically for AI engines to understand what you are, and it says "Pedal Barge" twice in the first two lines and describes the product as "pedal party boat booze cruises." It also points at `fareharbor.com/embeds/book/neworleanspedalbarge/`.

Fixing this file is maybe 20 minutes and it's the highest-leverage GEO action available.

### 5c. AI Overview position — unchanged and lopsided

25 citations. **21 are "December weather in New Orleans"** variants, most at AI Overview rank 1. Zero on any commercial swamp or party boat query. Full detail in the first audit's §3.

### 5d. Review snippets are working

GSC `searchAppearance` returns exactly one row: `REVIEW_SNIPPET` — **134,218 impressions, 1,358 clicks, position 11.9.** Elfsight's injected Product schema is being honored at scale. Leave it alone; add `Offer` for price.

Side effect: because the same Product block is injected sitewide with an identical SKU, review stars appear on December-weather and French-Quarter-walking-tour posts. Cosmetically odd, and it's part of why those posts rank without converting.

### 5e. PAA coverage gap

The "swamp tours new orleans" SERP surfaces four AI-generated People Also Ask boxes:

| Question | Do you have a page? |
|---|---|
| What's the best swamp tour in New Orleans? | Partly — `/which-swamp-tour-company-is-the-best/` (24 impressions, position 9.9) |
| Is it worth doing a swamp tour in New Orleans? | No |
| **How much does it cost to go on a swamp tour in New Orleans?** | **No** — highest commercial intent on the SERP |
| What's the best time of year for swamp tours? | Yes — `/what-time-of-day-is-best.../` 4,547 impressions at position 6.2, but **0.20% CTR** |

---

## 6. Technical — What's Actually Fine

Worth stating plainly so nobody spends money here:

| Check | Status |
|---|---|
| Server response (TTFB) | ✅ 127ms homepage, 198ms tour page |
| Full page load (HTML) | ✅ 0.22s / 0.33s |
| www → non-www 301 | ✅ correct, canonicals consistent |
| 404 handling | ✅ real 404s, not soft-404s |
| Sitemap | ✅ valid index, 3 child maps, 134 URLs |
| HTTPS | ✅ |
| Meta descriptions present | ✅ 0 missing (22 duplicated) |
| AI crawler access | ✅ not blocked |
| Image alt text | ⚠️ only 3 `<img>` tags on the homepage, 1 missing alt — most imagery is CSS backgrounds |
| HTML weight | ⚠️ 168KB, 29 script tags, 9 external JS — heavy but not fatal given the TTFB |
| Lazy loading | ⚠️ zero `loading="lazy"` |

**Do not spend money on a speed audit.** The server is fast. The problem is upstream of technical.

---

## 7. Revised Priority Stack

Ordered by expected clicks per hour of work.

### Tier 1 — do this week

| # | Action | Expected gain |
|---|---|---|
| 1 | **Rewrite titles + metas on the 17 pages in §1.** Cut every title under 60 chars, write a reason to click. | ~3,700 clicks/quarter at 2.5% CTR |
| 2 | **Fix `/llms.txt`** — repair all 48 link syntaxes, remove the 2 dead URLs, rewrite the header and description to lead with swamp tours and drop "Pedal Barge" | Highest-leverage GEO move available |
| 3 | **Set the WordPress Site Title** (fixes 59 page titles + 4 schema blocks + og:site_name + logo alt in one field) | Entity relevance |
| 4 | **Hand-edit the 6 titles carrying "Pedal"** (list in the previous message) | Entity relevance |
| 5 | **Resolve `/our-boats/` vs `/` cannibalization** on "party boat new orleans" — either de-optimize `/our-boats/` or make it the intended target and link to it properly | Recovers your best commercial term |

### Tier 2 — this month

| # | Action | Detail |
|---|---|---|
| 6 | **Consolidate the 26 programmatic location pages** into 1-2 honest pages, 301 the rest. Keep Metairie and Gretna. | 23 clicks/90d says these are pure overhead |
| 7 | **Fix internal linking.** 93 pages have ≤2 inbound links; /blog/ hoards 91. Add contextual links from the high-impression posts into the boat pages and the homepage. | Also the fix for the 5 orphaned commercial pages |
| 8 | **Clean up the duplicate URLs** in §3b — 301 each duplicate into its winner, kill `/pedal-bike-bar/1000/`, noindex `/category/swamp-tour-comparison/` | |
| 9 | **De-optimize for "barge."** Remove barge-rental language from `/boat-rental/`; retarget it at "party boat rental new orleans" | Stops the wrong-intent impression bleed |
| 10 | **Add H2s to the 58 pages that have none** | |
| 11 | **Write the swamp tour cost page** — the one PAA question with real buying intent and no page | |

### Tier 3 — the judgment call on /krewe-of-endymion/

14,440 impressions, 1 click, zero commercial relevance. Three options:

- **Rewrite it** to convert — "watching Endymion? here's what to do the rest of the weekend" with a hard boat CTA. Mardi Gras traffic is seasonal and enormous.
- **Leave it.** It costs nothing but drags sitewide CTR.
- **Noindex it.** Cleanest signal-wise, throws away a page that ranks top-10 for a 1,900/mo term.

I'd rewrite it. It's the only page on the site with parade-scale traffic and it's currently a dead end.

---

## 8. What Changed From the First Audit

| First pass said | Deep dive found |
|---|---|
| Entity naming is the #1 problem | Still true, but the CTR gap is 4x larger in absolute clicks |
| Two blog monsters have a CTR problem | It's **17 pages and 183,000 impressions**, not two |
| Site has ~134 pages | 26 of them (19%) earn 0.29 clicks/month |
| No llms.txt mentioned | It exists, and every link in it is broken |
| Schema needs `Offer` | Confirmed, and REVIEW_SNIPPET data proves the rest is working |
| Homepage carries all commercial rankings | Confirmed — and `/our-boats/` is cannibalizing it |
| Technical unknown | Technical is genuinely fine. Don't spend here. |
