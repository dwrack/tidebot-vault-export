# NKST — SEO / AEO / GEO Audit: The 5 Swamp Tour Money Keywords

**Date:** 2026-08-10
**Site:** neworleanskayakswamptours.com
**Window:** GSC 2026-05-12 → 2026-08-09 (90d). Rank data: DataForSEO US, Aug 2026. SERPs pulled from New Orleans, LA.
**Prior audit:** `Marketing/SEO Audit 2026-05-04.md` — see "What moved since May" below.

---

## Executive Summary

You rank on page 1 for the *small* version of the keyword and page 2+ for the *big* one. "New orleans swamp tour**s**" (5,400/mo) sits at #7. Flip the word order to "swamp tours new orleans" (14,800/mo, same intent, 2.7x the volume) and you drop to #15. Google treats those as two different queries and you're winning the cheap one.

The cause is structural, not content quality. Your best-titled money page — `/tours/swamp/`, H1 "Swamp Tours in New Orleans, LA" — is essentially invisible: no schema beyond breadcrumbs, 1,176 words, and it is not linked from your highest-authority page. Instead Google is ranking your **homepage** for the money term, and for several variants it's ranking a blog post about **free** swamp walks. You are being represented in the SERP by a page that tells people how not to pay you.

On AI search you're in a worse spot. You get AI Overview citations on 25 queries — 20 of them are alligator-vs-crocodile trivia. Zero commercial swamp-tour citations. Meanwhile when I asked a live AI search for "best swamp tour New Orleans kayak eco tour," it named **Wild Louisiana Tours' "Manchac Magic"** first — same swamp, same boat type, direct competitor — and put you third with generic filler copy.

**Top 3 by impact:**
1. Build a real money page at `/tours/swamp/` targeting the exact string "swamp tours new orleans," and point the alligator monster at it. (Fixes the 14,800 keyword.)
2. Ship Product + Offer + AggregateRating + FAQPage schema on every tour page. You have 1,416 reviews at 4.9 and not one of them is machine-readable. This is the single biggest AEO lever you have.
3. Kill or noindex the blog category archives and consolidate the two duplicate "best swamp tour" posts.

---

## 1. Where You Actually Rank

| Target keyword | Volume/mo | Your position | Page Google picked | Verdict |
|---|---|---|---|---|
| **swamp tours new orleans** | 14,800 | **15** | `/` (homepage) | Page 2. Wrong page. |
| swamp tour new orleans | 14,800 | 21 | `/` (homepage) | Page 3. |
| **swamp tour from new orleans** | 14,800 (same cluster) | ~15 | `/` | Same bucket as above. |
| new orleans swamp tours | 5,400 | **7** | `/` | Page 1 — your only commercial win. |
| new orleans swamp tour | 5,400 | 9 | `/` | Page 1, bottom. |
| **alligator tour new orleans** | 2,900 | **51** | `/` | Not ranking. No page exists. |
| gator tour new orleans | 2,900 | 45 | `/` | Same. |
| **louisiana swamp tour** | 4,400 | **not in top 100** | — | Not ranking at all. |
| **swamp tour near me** | 12,100 | **not in top 100** | — | Local pack only. See §4. |
| honey island swamp tour | 9,900 | 22 | `/tours/kayak-tours/honey-island-swamp-tour/` | **This is a blog category archive, not a tour page.** |
| swamp tours in new orleans | 1,900 | 20 | `/3-free-swamp-walks-.../` | Google ranks your *free alternatives* post for a buying query. |
| best new orleans swamp tours | 1,600 | 24 | `/which-swamp-tours-are-the-best/` | Competing with a near-identical post. |
| kayak swamp tour | 880 | **1** | `/` | You own the niche term. Nobody searches it. |

**The pattern:** you dominate "kayak swamp tour" (880/mo). You're absent from "swamp tour" (14,800/mo). The word "kayak" is doing the work of a moat and a wall at the same time.

---

## 2. Why You're Stuck on Page 2 (Root Causes)

### 2a. No money page is actually competing

`/tours/swamp/` is your correct target page. Current state:

| Element | Current | Problem |
|---|---|---|
| Title | "Swamp Tours in New Orleans - Manchac / Honey Island / Jean Lafitte" | Actually good. Best title on the site. |
| H1 | "Swamp Tours in New Orleans, LA" | Good. |
| Word count | 1,176 | Thin vs Cajun Encounters / Tour Big Easy. |
| Schema | BreadcrumbList only | No Product, no Offer, no rating, no FAQ. |
| H2s | 3 | Missing price, duration, what-you-see, how-to-get-there, comparison. |
| Internal links in | Very few. Not linked from `/alligators-vs-crocodiles/`. | Orphan-adjacent on the highest-value keyword. |

Google is ranking the homepage instead, which means it doesn't believe `/tours/swamp/` is the answer. That's a linking and depth signal problem.

### 2b. A blog category archive is your Honey Island "money page"

`/tours/kayak-tours/honey-island-swamp-tour/` ranks #22 for a 9,900/mo keyword. Its meta description is:

> "Click to view honey island swamp tour category posts in Blog | Page 1 of 2"

That's the auto-generated archive boilerplate. Zero schema. This URL looks like a tour page and behaves like a blog index. Meanwhile you have a real tour page at `/tours/swamp-kayak-tours/honey-island-kayak.../`. Two URLs, split equity, and the wrong one is winning.

### 2c. Your free-content post is eating commercial queries

`/3-free-swamp-walks-in-and-around-new-orleans/` currently ranks 18-20 for:
- "swamp tour new orleans la" (1,900)
- "swamp tours in new orleans" (1,900)
- "swamp tours of new orleans" (1,900)
- "new orleans area swamp tours" (1,900)
- "swamp tours in new orleans louisiana" (1,900)

That's ~9,500/mo of commercial-intent traffic being routed to a page whose thesis is "here's how to see a swamp without paying anyone." It has 9,079 impressions and 92 clicks at position 13.9. Every one of those clicks is a lost booking.

### 2d. Duplicate "best swamp tour" posts

- `/which-swamp-tours-are-the-best/` — H1 "New Orleans swamp tour reviews", 1,599 words, ranks #24 and #30
- `/which-is-the-best-swamp-tour-around-new-orleans/` — H1 "What is the best Swamp Tour near New Orleans?", 860 words, ranks #43 and #51

Same query, two pages, both on page 3-5. Textbook cannibalization. Neither will ever rank while both exist.

### 2e. The alligator monster is sealed off

`/alligators-vs-crocodiles/` did **272,489 impressions / 866 clicks** in 90 days at position 6.25. It is the most valuable internal-link asset you own. The May audit specified a "More reading" block linking it to the money pages. **I checked the live page — the block was never added.** It links to Manchac Mystic in-body (good) but not to `/tours/swamp/`, not to the swamp-tours guide, not to the airboat-vs-kayak comparison.

CTR on that page is **0.32%** at position 6. A page ranking #6 should pull 6-9%. You're leaving roughly 15,000-20,000 clicks per quarter on the table from one URL.

---

## 3. AEO / GEO — AI Search Position

### What AI engines currently cite you for

You hold **25 AI Overview citations**. Here's the breakdown:

| Query theme | Citations | Commercial value |
|---|---|---|
| Alligator vs crocodile trivia | 14 | **None.** These people are not in New Orleans. |
| Louisiana wildlife / swamps (informational) | 6 | Low. Top-funnel at best. |
| Kayak gear ("sit on top kayak", 18,100/mo) | 1 | None. |
| "postal code new orleans" (via your zipline page) | 1 | None — and it signals topical confusion. |
| **Commercial swamp tour queries** | **1** (rank 13, "best swamp boat tours in new orleans") | The only one that matters. |

You've built AI authority on the wrong entity. Google's models see you as *an alligator facts publisher*, not *a New Orleans swamp tour operator*.

### What a live AI search returns today

Query: "best swamp tour New Orleans kayak eco tour 2026" →

1. **Wild Louisiana Tours — "Manchac Magic Kayak Swamp Tour"** (described in detail: 2 hours, transportation from the city, alligators/egrets/owls/eagles, all skill levels)
2. **Voodoo Swamp Tours** (1hr 15min guided kayak)
3. **New Orleans Kayak Swamp Tours** — quoted as *"an immersive way to experience bayous, wildlife, and wetlands up close... by using kayaks instead of motorized watercrafts or airboats, they minimize noise, pollution, and disruption"*

Read your entry next to theirs. Wild Louisiana gets specifics — duration, transport, species list, difficulty. You get eco-philosophy. **AI models quote what's extractable.** Your copy leads with mission; theirs leads with facts. That's why they're first.

### The three GEO gaps

**Gap 1 — No structured facts.** Schema audit across your key pages:

| Page | Schema present | Missing |
|---|---|---|
| `/` (homepage) | VideoObject, Organization, LocalBusiness, WebSite, WebPage | AggregateRating, FAQPage |
| `/tours/` | BreadcrumbList | Everything |
| `/tours/swamp/` | BreadcrumbList | Product, Offer, FAQPage, AggregateRating |
| `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | VideoObject ×2, BreadcrumbList | **Product, Offer, AggregateRating, FAQPage** |
| `/tours/kayak-tours/honey-island-swamp-tour/` | **none** | Everything |

You have $65/$79/$195 pricing in the body text of these pages and **not one Offer object**. You have 1,416 reviews at 4.9 stars and **no AggregateRating anywhere**. AI answer engines lean hard on structured data because it's unambiguous. You're handing them prose and hoping.

**Gap 2 — Not in the aggregator layer AI reads from.** Every AI answer about NOLA swamp tours pulls from Viator, GetYourGuide, TripAdvisor listicles, and neworleans.com. Wild Louisiana's Manchac Magic has a dedicated GetYourGuide page with verified reviews — that's the page the AI quoted. Your TripAdvisor presence exists ("Kayak Swamp Tours") but is not the citation source.

**Gap 3 — No answer-shaped content for the PAA questions.** The "swamp tours new orleans" SERP surfaces these People Also Ask boxes, all AI-generated:
- What's the best swamp tour in New Orleans?
- Is it worth doing a swamp tour in New Orleans?
- **How much does it cost to go on a swamp tour in New Orleans?**
- What's the best time of year for swamp tours?

You have a page for #4 (`/what-is-the-best-time-of-day.../`, position 4.9, 7,967 impressions). You have nothing clean for the cost question — which is the highest commercial-intent question on the entire SERP.

---

## 4. "Swamp Tour Near Me" — Different Game Entirely

12,100/mo, and it is **100% a local pack query**. Organic position is nearly irrelevant. Current pack in New Orleans:

| # | Business | Reviews | Rating |
|---|---|---|---|
| 1 | Bayou Swamp Tours New Orleans | 3,300 | 4.9 |
| 2 | Swamp Tours New Orleans (Tour Big Easy) | 729 | 4.8 |
| 3 | Cajun Encounters Tours | 12,000 | 4.9 |

**Your GBP:** New Orleans Kayak Swamp Tours, 740 N Rampart St, 70116. **4.9 stars, 1,416 reviews.**

You have nearly double Tour Big Easy's review count and a better rating, and you're not in the pack. Review volume is not the blocker. Two things are:

**a) Primary category mismatch.** Yours is "Canoe & kayak tour agency." The pack winners are "Boat tour agency" and "Tour operator." Google matches primary category to query intent, and "swamp tour" resolves to boat tours. Your business name also leads with "Kayak," which reinforces the narrower classification.

**b) You are competing against yourself in the 70116 proximity cluster.** Listings you control within a few blocks:

| Listing | Address | Primary category |
|---|---|---|
| New Orleans Kayak Swamp Tours | 740 N Rampart St, 70116 | Canoe & kayak tour agency |
| Crescent City Kayak - Swamp Tours | 437 Esplanade Ave, 70116 | Canoe & kayak tour agency |
| Hidden Adventure Swamp & Plantation Tours | 435 Esplanade Ave, 70116 | Canoe & kayak tour agency |
| Admire New Orleans - Kayak Tours... | (no address) | Tour operator |
| Plantation & Swamp Tours New Orleans | **"Swamp Tour Street," 70117** | Tour operator |

Google shows one result per business cluster. Five near-identical listings on the same two blocks trigger the diversity filter and it may well be picking none of you. Separately: **"Swamp Tour Street" is not a real street.** A fabricated address is a listing-suspension trigger. Fix or remove that one regardless of everything else here.

---

## 5. What Moved Since the May Audit

| Item | May 2026 | Aug 2026 | Status |
|---|---|---|---|
| swamp tours new orleans | pos 12.4 | pos 15 | **Worse** |
| Homepage avg position | 10.0 | 11.4 | **Worse** |
| Alligator page | 308k imp / 583 clicks | 272k imp / 866 clicks | CTR improved, still 0.32% |
| "More reading" internal-link block | Specified | **Not shipped** | Not done |
| Swamp Tours New Orleans Guide post | Drafted | Live at `/swamp-tours-new-orleans-guide/`, pos 12.6 | Shipped, no links pointing at it |
| Airboat vs kayak page | Recommended | Not found | Not done |
| CCK consolidation decision | Open | Still open, still duplicating | Not done |

The content shipped. The internal linking didn't. That's why nothing moved — a new post with no links pointing at it is a page nobody, including Google, can find.

⚠️ **One thing to fix in the old plan:** the May internal-linking doc specifies URLs like `/blog/swamp-tours-new-orleans-guide/`. The live URL has no `/blog/` prefix. If those links get pasted as written, they'll all 404.

---

## 6. Action Plan

### Quick wins — this week

| # | Action | Where | Why it matters |
|---|---|---|---|
| 1 | Add the "More reading" block to `/alligators-vs-crocodiles/` — link to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/`. **Use root-level URLs, no `/blog/` prefix.** | Alligator page | 272k impressions of authority currently going nowhere |
| 2 | Rewrite the alligator page title + meta with a hook. Position 6 at 0.32% CTR is the biggest single leak on the site. | Alligator page | ~15-20k clicks/quarter available |
| 3 | Add `AggregateRating` (4.9, 1416) + `Offer` (price, currency, availability) + `Product` schema to all 6 tour pages | All `/tours/*` | Star ratings in SERP + AI extractability. Highest-ROI hour of work on this list. |
| 4 | 301 `/which-is-the-best-swamp-tour-around-new-orleans/` → `/which-swamp-tours-are-the-best/`, merge the best content | Blog | Ends cannibalization on "best swamp tour" |
| 5 | Rewrite `/3-free-swamp-walks-.../` so every section ends pointing at a paid tour, and add a prominent comparison CTA | Blog | ~9,500/mo of commercial queries currently landing on a "don't pay" page |
| 6 | Fix the `/tours/` meta description — it's truncated mid-sentence ("If you are in Louisiana, you can") | `/tours/` | Free CTR |
| 7 | Change NKST GBP primary category to **Tour operator** or **Boat tour agency**; keep kayak as secondary | GBP | Local pack eligibility for "swamp tour near me" |
| 8 | Fix or delete the "Swamp Tour Street" GBP listing | GBP | Suspension risk across the account |

### Strategic — this quarter

| # | Action | Detail | Effort |
|---|---|---|---|
| 9 | **Rebuild `/tours/swamp/` as the money page for "swamp tours new orleans"** | Target 2,000+ words. Title: "Swamp Tours New Orleans \| Small-Group Kayak Eco Tours". H2s must cover: price, duration, departure + drive time from the Quarter, what wildlife you'll see, airboat vs kayak, best time of year, what to bring, booking. Add FAQPage schema for the 4 PAA questions. Link to it from homepage, alligator page, and all 5 blog posts. | High |
| 10 | **Fix the Honey Island URL collision** | Noindex the category archive at `/tours/kayak-tours/honey-island-swamp-tour/` or 301 it to the real tour page. 9,900/mo keyword currently pointed at boilerplate. | Medium |
| 11 | **Build `/alligator-tour-new-orleans/`** | 2,900/mo, you're at #51. Nobody owns "kayak-level alligator viewing." You already rank #4-8 in AI Overviews for alligator content — this bridges your existing AI authority to a commercial page. Highest-leverage new page on the list. | Medium |
| 12 | **Build the airboat vs kayak comparison page** | Recommended in May, still missing. It's the #1 objection, it's a PAA question, and comparison pages are disproportionately cited by AI engines. | Medium |
| 13 | **Build a "How much does a New Orleans swamp tour cost?" page** | Direct PAA answer, highest commercial intent question on the SERP, and a pure AEO play. Include a real price comparison table across operators — that's the format AI quotes. | Low |
| 14 | **Target "louisiana swamp tour" (4,400/mo)** | Zero presence today. `/louisiana_swamp_guide/` gets 11,709 impressions at position 10.8 but is informational. Add a commercial section + internal links, or build a state-level page. | Medium |
| 15 | **Fix the GetYourGuide / Viator / TripAdvisor layer** | Wild Louisiana beat you in the AI answer because their GetYourGuide page is richer. Rewrite your OTA listings with the specifics AI extracts: exact duration, transport options, species list, difficulty, group size. This is where AI answers actually source from. | Medium |
| 16 | **Resolve Crescent City Kayak** | Flagged in May, still unresolved. Either 301 it into NKST or make it a genuine funnel. Right now it splits authority on the same queries. | High |
| 17 | **Rewrite copy to lead with facts, not mission** | "Small groups. 2.5 hours. 45 minutes from the Quarter. Alligators, herons, 500-year-old cypress." Then the eco mission. AI engines quote the first extractable specifics they find. Your competitors' copy is more quotable than yours. | Medium |

---

## 7. The One-Sentence Version

You've built a large, genuinely authoritative content site about alligators and accidentally forgotten to build one about buying a swamp tour — fix the money page, ship the schema, and point the alligator traffic at something you can sell.
