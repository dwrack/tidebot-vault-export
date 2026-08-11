# NPB — SEO / AEO / GEO Audit: nolapartybarges.com

**Date:** 2026-08-11
**Property:** `sc-domain:nolapartybarges.com`
**Window:** GSC 2026-05-13 → 2026-08-10 (90d). Rank data: DataForSEO US, Aug 2026. SERPs pulled from New Orleans, LA.
**Companion:** `New Orleans Kayak Swamp Tours/Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`

---

## Executive Summary

NPB is in a genuinely better organic position than NKST — and pointed at a much smaller prize. You rank #2-3 for "party boat new orleans," #3 for "boat rides in new orleans," #5 for "new orleans boat tours." The problem is the category: **"party boat new orleans" is 590 searches/month. "booze cruise new orleans" is 320. "tiki boat new orleans" is 210.** You have effectively won a market that barely gets searched.

Meanwhile your homepage ranks **#7.5 for "swamp tours new orleans" — a 14,800/mo keyword — and it is outranking NKST, which sits at #15 for the same term.** That single fact should reorder the whole plan. The biggest organic opportunity on this domain is not party boats. It's swamp tours, and you're already halfway up page 1 without trying.

Two things are actively bleeding value. First, Google labels this site **"New Orleans Pedal Barge"** in live search results — every page title except the homepage still carries the old brand, which splits the entity signal and violates the no-pedal rule at the SERP level. Second, on the "party boat new orleans" SERP a reseller (letsbatch.com, 7 reviews) gets a rich snippet with stars and a **"$63.00 to $1,200.00"** price range while your own Freaky Tiki page gets a plain blue link — because your Product schema carries a rating but **no price**.

**Top 3 by impact:**
1. Deepen the homepage on swamp intent. You're #7.5 on a 14,800/mo term off 869 words and one H2.
2. Change the WordPress Site Title. One field kills "Pedal Barge" across every page's title, og:site_name, and all four schema blocks.
3. Add a server-side `Offer` (price) to each boat page. Elfsight covers the rating; price is the missing half.

---

## 1. Where You Actually Rank

### Commercial keywords — you're winning a small pond

| Keyword | Vol/mo | Position | Ranking page |
|---|---|---|---|
| party boat new orleans | 590 | **2** | `/` |
| new orleans party boats | 590 | 2 | `/` |
| new orleans party boat | 590 | 3 | `/` |
| party boat in new orleans | 590 | 4 | `/` |
| boat party new orleans | 590 | 2 | `/` |
| boat rides in new orleans | 1,600 | **3** | `/` |
| nola boat tours | 1,900 | 3 | `/` |
| new orleans boat tours | 1,900 | 5 | `/` |
| boat trips new orleans | 1,900 | 5 | `/` |
| boat tours in new orleans | 1,600 | 6 | `/` |
| boat cruises in new orleans | 1,600 | 9 | `/` |
| party barges | 3,600 | 5 | `/` |
| boat rental new orleans | 320 | 17 | `/bentley-bayou-cruiser/` |
| party boat to rent | 4,400 | 39 | `/boat-rental/` |
| tiki pontoon boat | 320 | 38 | `/the-freaky-tiki/` |

**Note the pattern: fifteen of these rank on `/`.** The homepage is carrying the entire commercial side of the site. Your product pages — Freaky Tiki, Twerkin' Tiki, Cajun Queen, Bentley Bayou Cruiser, boat-rental — rank for almost nothing outside brand terms.

### The swamp tour cluster — the actual opportunity

| Keyword | Vol/mo | NPB position | NKST position |
|---|---|---|---|
| **swamp tours new orleans** | 14,800 | **7.5** (GSC) | 15 |
| swamp tour new orleans | 14,800 | 7.5 (GSC) | 21 |
| new orleans swamp tour | 5,400 | 7.5 (GSC) | 9 |
| swamp boat tours in new orleans | 1,900 | 11 | 55 |
| swamp boat rides in new orleans | 480 | 10 | — |
| new orleans swamp boat rides | 480 | 17 | — |
| best swamp boat tours in new orleans | 1,600 | 29 | 51 |
| swamp tour (generic) | 8,100 | 55 | 8,100/mo, not ranking |

NPB pulled **20 clicks / 738 impressions** on "swamp tours new orleans" and **12 clicks / 871 impressions** on "swamp tour new orleans" last 90 days at position ~7.5. That's from a homepage with one H2 and 869 words. It's ranking on domain strength and GBP prominence alone.

Your GBP is even named **"Nola Party Barge - Swamp Tour Party Boat."** The positioning already exists. There's just no page behind it.

### Brand terms — locked down

"nola party barge" #1.2, "nola pedal barge" #1.3, "new orleans party barge" #1.7, "twerkin tiki" #1.0, "freaky tiki new orleans" #2.2. No work needed here. But note: **"nola pedal barge" still pulls 125 clicks/month.** People are searching the retired brand.

---

## 2. Structural Problems

### 2a. Google calls your site "New Orleans Pedal Barge"

Pulled live from the "party boat new orleans" SERP, the result for nolapartybarges.com:

> **website_name: "New Orleans Pedal Barge"**

And Yelp's "TOP 10 BEST Party Boat in New Orleans" listicle — which ranks #10 on that same SERP — lists you as **"3. New Orleans Pedal Barge."**

Source of the problem, from the live pages:

| Page | Title tag |
|---|---|
| `/` | Swamp Tour Party Boat Cruise \| **New Orleans Party Barge** ✅ |
| `/the-freaky-tiki/` | The Freaky Tiki \| **New Orleans Pedal Barge** ❌ |
| `/the-twerkin-tiki/` | The Twerkin' Tiki \| **New Orleans Pedal Barge** ❌ |
| `/new-orleans-booze-cruise/` | New Orleans Booze Cruise \| **New Orleans Pedal Barge** ❌ |
| `/1253-2/` | How Many Days In New Orleans Is Enough? \| **New Orleans Pedal Barge** ❌ |

The homepage was updated. Nothing else was. Google resolves the site-wide entity name from the dominant pattern across pages, and the dominant pattern is still the old brand. This is a global find-and-replace across the title template, not a page-by-page fix.

### 2b. Homepage H1 has a typo

> "Most Swamp Tours in New **Orelans** Are Boring. Ours Aren't."

That's the H1 on the page ranking #7.5 for a 14,800/mo keyword. Great line, misspelled city.

### 2c. Product schema exists (via Elfsight) but has no price and a duplicate SKU

**Corrected 2026-08-11.** An earlier draft of this audit said there was no AggregateRating on the site. That was wrong — it was based on the raw HTML. The Elfsight reviews widget injects a `Product` block client-side, after render, so it doesn't appear in source. Verified in the rendered DOM on both `/` and `/the-freaky-tiki/`.

What Elfsight actually injects, identically on every page:

```json
{
  "@type": "Product",
  "name": "<the page's title tag>",
  "brand": { "name": "<the page's title tag>" },
  "sku": "1101111",
  "mpn": "110111",
  "aggregateRating": { "ratingValue": 4.9, "reviewCount": 3843 },
  "review": { ...one rotating recent review... }
}
```

Server-side schema, for reference:

| Page | Server-rendered | Elfsight adds |
|---|---|---|
| `/` | Organization, LocalBusiness, WebSite, WebPage | Product + AggregateRating |
| `/the-freaky-tiki/` | VideoObject, BreadcrumbList | Product + AggregateRating |
| `/the-twerkin-tiki/` | VideoObject, BreadcrumbList | Product + AggregateRating |
| `/boat-rental/` | BreadcrumbList | Product + AggregateRating |
| `/new-orleans-booze-cruise/` | Article, BreadcrumbList | Product + AggregateRating |

So the rating is covered. Four things still aren't:

1. **No `Offer`, so no price.** You have $49 / $63 / $69 / $165 / $350 / $600 in body copy and not one Offer object. This is the whole gap.
2. **Same `sku` and `mpn` on every page.** Every boat is product `1101111`. To a parser, the site sells one item.
3. **`name` is the page title tag,** not a product name — "The Freaky Tiki | New Orleans Pedal Barge" as a product name.
4. **Ratings are aggregated from Google, Facebook, Yelp and TripAdvisor.** Google's review-snippet policy says ratings must come from users directly on your site, not from another platform or aggregator. This markup may simply be discarded.

What it costs, straight off the live SERP for "party boat new orleans":

| Result | Rich snippet? |
|---|---|
| #9 **letsbatch.com** (reseller, selling your Freaky Tiki) | ⭐ 5.0 (7 reviews) + **"$63.00 to $1,200.00"** |
| #3 **nolapartybarges.com** (you, 3,549 reviews) | Plain blue link |

letsbatch wins that snippet on **price**, not stars. Adding a server-side `Offer` with the real price to each boat page is the fix, and it's independent of Elfsight.

### 2d. Everything rides on the homepage

Fifteen commercial keywords, one ranking URL. That's fragile and it caps you. `/boat-rental/` is **434 words**. `/new-orleans-booze-cruise/` is **485 words**. `/the-freaky-tiki/` has **zero H2s**. These pages cannot rank for anything competitive at that depth, so Google falls back to the homepage for every query — which means you can never occupy two slots on the same SERP, and you can never target a specific intent ("bachelorette party boat," "birthday boat rental") with a page built for it.

### 2e. A WordPress default slug with 6,439 impressions

`/1253-2/` — position 7.1, 6,439 impressions, 22 clicks. Actual title: "How Many Days In New Orleans Is Enough?" The URL is an unedited WordPress post ID.

### 2f. www / non-www transition still resolving

`https://www.nolapartybarges.com/` correctly 301s to non-www, and canonicals are consistent. But GSC still shows both versions accruing impressions in the window: www at 31,590 imp / 1,781 clicks / pos 5.5, non-www at 41,015 imp / 738 clicks / pos 9.8. Google is still holding both. Not a crisis, but confirm consolidation in a month — if www is still showing, something is re-surfacing it (likely internal links or sitemap entries pointing at www).

---

## 3. AEO / GEO — You Run a Weather Site

### AI Overview citations: 25 total

| Query theme | Citations | Commercial value |
|---|---|---|
| **December weather in New Orleans** | **21** | **None** |
| French Quarter walking tour | 1 | Low |
| "symbols of new orleans" | 1 | None |
| "trip to new orleans" / "trip new orleans" | 2 | Top-funnel |
| **Party boat / booze cruise / tiki / boat tour** | **0** | — |

Twenty-one of your twenty-five AI Overview citations are for "december weather in new orleans" and its variants — and you hold **rank 1 in the AI Overview** on most of them. A 6,600/mo weather query. You are, as far as Google's models are concerned, a New Orleans weather resource.

The page doing it, `/exploring-december-weather-in-new-orleans-what-to-wear/`, pulled **39,863 impressions and 151 clicks** — a **0.38% CTR**. You are the #1 cited source in the AI answer and almost nobody clicks, because the AI already answered them. That's the zero-click trap in its purest form: maximum authority, minimum value.

Same story on `/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/` — **41,686 impressions, 376 clicks, 0.90% CTR, position 4.3.** (It also still says "2024" in the URL and title, in August 2026. That's a freshness signal actively working against you.)

**Between those two posts: 81,549 impressions, 527 clicks, 0.65% CTR.** That's the single biggest pool of wasted authority on the domain.

### What AI actually says about your boats

I ran a live AI search for "best party boat New Orleans bachelorette BYOB tiki boat." Good news: **The Freaky Tiki and The Twerkin' Tiki are both named and described accurately**, credited to "New Orleans Party Barges."

Bad news: look at where the AI sourced it from, in order —

1. GetYourGuide
2. letsbatch.com
3. Viator
4. TripAdvisor
5. admirenola.com *(yours)*
6. nolaboozecruise.com/party-boats/ *(yours)*
7. nolaboozecruise.com *(yours)*
8. neworleanstikiboats.com *(yours)*
9. nolaboozecruise.com/the-freaky-tiki/ *(yours)*
10. **nolapartybarges.com** *(the mothership — dead last)*

Your product wins the answer. Your flagship domain is the tenth of ten sources feeding it. The OTAs and your own sister sites are doing the talking. That works right up until an AI has to pick one booking link.

### The three GEO gaps

**Gap 1 — No structured facts.** Covered in §2c. Duration, price, capacity, BYOB policy, minimum age, departure point are all prose-only. AI engines extract structured data first.

**Gap 2 — The aggregator layer outranks you as a source.** GetYourGuide, Viator, TripAdvisor, Tiqets, letsbatch and Expedia all carry your boats with better-structured product data than your own site. Every one of those listings is a citation you don't control.

**Gap 3 — No answer content on commercial questions.** Related searches on the "party boat new orleans" SERP: *party boat new orleans **prices**, **best** party boat new orleans, party boat new orleans **tickets**, party boat new orleans **tours**.* You have a page for none of these. "Prices" is the highest-intent query on the board and there's no page answering it.

---

## 4. The Self-Competition Question

Live local pack + organic for "party boat new orleans," New Orleans, LA:

| Slot | Result | Owner | Reviews |
|---|---|---|---|
| Local #1 | New Orleans Party Boats | **Yours** | 288 (5.0) |
| Local #2 | **Nola Party Barge - Swamp Tour Party Boat** | **Yours** | **3,549 (4.9)** |
| Local #3 | New Orleans Booze Cruise | **Yours** | 214 (4.8) |
| Organic #1 | nolaboozecruise.com | **Yours** | — |
| Organic #2 | instagram.com/boattoursatthewharf | Competitor | — |
| Organic #3 | **nolapartybarges.com** | **Yours** | — |
| Organic #4 | hiddenadventuretours.com | **Yours** | — |
| Organic #5 | letsbatch.com (reselling Freaky Tiki) | Reseller | — |
| Organic #7 | neworleanstikiboats.com | **Yours** | — |

**You own eight of the nine slots on page one.** That's not a problem — that's near-total SERP capture on a 590/mo keyword, and it's genuinely impressive.

Two things worth noticing anyway:

- **Your 288-review listing outranks your 3,549-review listing** in the local pack. Review volume isn't the deciding factor; New Orleans Party Boats has the exact-match business name. Something to weigh if you ever want NPB in the top slot.
- **nolaboozecruise.com beats nolapartybarges.com organically** (#1 vs #3). The flagship is losing to a satellite on its own category term.

Unlike NKST's 70116 cluster — where five near-identical kayak listings sit on two blocks and Google's diversity filter may be suppressing all of them — this one is working. Leave it alone. The lesson from NKST doesn't transfer here.

---

## 5. Action Plan

### Quick wins — this week

| # | Action | Why |
|---|---|---|
| 1 | **Global find-and-replace "New Orleans Pedal Barge" → "New Orleans Party Barge"** in the title template, meta descriptions, Organization schema, and OG tags across every page | Google currently labels the whole site with the retired brand. Also fixes the no-pedal rule at the SERP level. |
| 2 | Fix the homepage H1 typo: "New **Orelans**" → "New Orleans" | It's the H1 on your highest-value ranking page |
| 3 | **Add a server-side `Offer` (price, currency, availability) + a real `name`/`sku` per boat** on `/the-freaky-tiki/`, `/the-twerkin-tiki/`, `/the-cajun-queen/`, `/bentley-bayou-cruiser/`, `/boat-rental/`. Elfsight already supplies AggregateRating — don't duplicate it, just stop it being the only thing there. | letsbatch beats you on the price snippet, not the stars. Price is the gap. |
| 4 | Rewrite title + meta on `/exploring-december-weather-.../` and `/how-much-do-you-need-to-budget-.../` with a hook and a reason to click | 81,549 impressions at 0.65% CTR between them |
| 5 | Add a hard CTA block to both of those posts routing to the boats — "coming in December? here's the one thing that's still fun when it's 55°" (the boats are heated, per your own meta description, and nobody knows) | Turns weather authority into bookings |
| 6 | ~~Drop "2024" from the budget post's URL~~ **Leave the slug alone.** The on-page title already reads 2026; only the URL string is stale, and Google takes freshness from content, not slugs. Not worth risking a position-4.3 page with 41,686 impressions on a 301. Refresh the body figures instead. | Revised — the risk outweighs the gain |
| 7 | 301 `/1253-2/` → `/how-many-days-in-new-orleans/` | 6,439 impressions on a WordPress default slug |
| 8 | Add H2 structure to `/the-freaky-tiki/` (currently zero H2s) | Basic on-page, page has 12,503 impressions |

### Strategic — this quarter

| # | Action | Detail |
|---|---|---|
| 9 | **Deepen the homepage on swamp intent — do NOT build a competing page** | *Revised 2026-08-11 after a cannibalization challenge; the revision is correct.* The homepage is already the swamp page: title "Swamp Tour Party Boat Cruise", H1 "Most Swamp Tours in New Orleans Are Boring. Ours Aren't." That's why it ranks #7.5. A second generic `/new-orleans-swamp-tour/` would target the identical query with weaker authority and make Google choose — the classic way to lose a position-7 ranking. Instead take the homepage from 869 words / 1 H2 to ~1,800 with H2s for: what you see (alligators, Bayou Bienvenue), 30 min from downtown, onboard bathroom, heated in winter, BYOB, price, duration, kayak/airboat/party-boat comparison. Add FAQPage schema for the four PAA questions. Zero cannibalization risk, and it strengthens the exact URL already ranking. |
| 9b | **Build long-tail swamp pages the homepage does *not* rank for** | Safe expansion, no overlap: `/swamp-tour-prices-new-orleans/`, `/swamp-tour-with-bathroom/` (expand the existing post), `/airboat-vs-party-boat-swamp-tour/`, `/swamp-tour-byob/`. Each targets a distinct query and links up to the homepage — that's how you add swamp footprint without competing with yourself. |
| 10 | **Own "swamp tour with bathroom" outright** | `/swamp-tours-with-onboard-restrooms/` already ranks 5.5 with a 5.8% CTR — your best-converting content by CTR on the whole site. Nobody else can make this claim. Expand it, and put the bathroom fact in the swamp page H1 area, GBP description, and every OTA listing. |
| 11 | **Build `/party-boat-new-orleans-prices/`** | Highest-intent related search on the SERP, and a pure AEO play. Real numbers, per-boat, per-head vs private. AI engines quote price tables. |
| 12 | **Build a bachelorette page** | "bachelorette party new orleans" is 1,300/mo — bigger than your entire party-boat cluster. `/a-locals-itinerary-for-a-new-orleans-bachelorette-party/` sits at position 21.8 with 2,107 impressions. Rebuild it as a commercial page, not a blog post. |
| 13 | **Give the boats real pages** | Each vessel page needs 1,200+ words, H2s, capacity, price, what's included, FAQ, and schema. Right now the homepage ranks for everything because nothing else is substantial enough to. |
| 14 | **Fix the OTA layer** | GetYourGuide, Viator, TripAdvisor, Tiqets and letsbatch outrank you as AI sources on your own products. Rewrite every listing with the extractable specifics: exact duration, capacity, BYOB policy, bathroom, heated, departure address, age minimum. |
| 15 | **Decide the nolaboozecruise / neworleanstikiboats / partyboats relationship** | Satellites are winning slots the flagship should hold (booze cruise #1 vs NPB #3). The SERP capture is working, so don't consolidate — but do make sure every satellite links to nolapartybarges.com with descriptive anchors so the authority flows to the mothership. |
| 16 | **Reconsider the blog's whole premise** | Weather, budgets, neighborhoods, French Quarter walking tours, housing styles, filming locations, Endymion parade routes. Roughly 150k impressions/quarter at sub-1% CTR that AI Overviews now answer directly. This content built domain authority — it will not build bookings. New posts should be swamp/bayou/boat/party-adjacent where the click still has to happen. |

---

## 6. NPB vs NKST — Portfolio Note

Same owner, same city, same 14,800/mo keyword, and they are not aligned:

| | NPB | NKST |
|---|---|---|
| "swamp tours new orleans" | **#7.5** | #15 |
| Google reviews | 3,549 (4.9) | 1,416 (4.9) |
| Dedicated swamp money page | **None** | `/tours/swamp/` (thin, unlinked) |
| Commerce schema | None | None |
| AI Overview citations | 21/25 December weather | 20/25 alligator trivia |
| Positioning | Party boat that does swamp tours | Kayak eco-tour |

Both sites built enormous informational authority on topics that don't sell, both are missing commerce schema, and neither has a real swamp tour money page — while the keyword they'd both fight for is the single biggest tour term in New Orleans.

They aren't competing for the same customer (BYOB bachelorette party vs quiet eco-paddle), so both can rank. But right now the party boat is beating the kayak company at kayak-company SEO, and neither is beating Cajun Encounters. Worth building the two swamp pages deliberately different from each other rather than by accident.

---

## 7. The One-Sentence Version

You've won a 590-searches-a-month category outright and become Google's favorite source on December weather, while sitting at #7.5 on a 14,800/mo swamp tour keyword off a thin homepage — deepen that page (don't clone it), change one WordPress field to kill "Pedal Barge," and put a price in your schema.
