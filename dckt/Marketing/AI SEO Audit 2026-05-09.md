# AI SEO Audit — doorcountykayaktours.com

**Date:** 2026-05-09
**Scope:** ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot
**Pulled from:** Live site fetches, GSC (last 90 days), live AI search snippets

---

## TL;DR

DCKT is **partially visible** to AI search — getting cited in summaries for Cave Point, beginner kayaking, kayak-while-pregnant, and shipwreck queries. But the foundation is wobbly: most tour pages and the homepage have **zero JSON-LD schema**, no FAQ blocks, no last-updated dates, no author attribution. AI cites what's structured. Right now we're getting cited despite the site, not because of it.

The fastest moves are technical (add FAQ + Tour + LocalBusiness schema across all tour pages and the top 10 GSC blog posts) and structural (rewrite tour-page first paragraphs into 40-60 word definition blocks). Both are 1-week jobs that compound across every AI platform.

The bigger play is third-party presence. We're missing from Wikipedia, weak on Reddit, and our Tripadvisor presence is fragmented across three locations. Wikipedia and Reddit are 2 of the top 3 sources ChatGPT pulls from.

---

## Current AI Visibility — Where We Show Up vs Where We Don't

### Cited (Good)
| Query | Platform | What gets cited |
|-------|----------|----------------|
| "Cave Point kayak tour Door County" | Web/AI summaries | DCKT mentioned alongside competitors |
| "kayaking Door County for beginners" | AI summaries | **Eco Estuary Tour named specifically** |
| "Door County kayak shipwreck tour" | AI summaries | DCKT cited with Schooner Fleetwing + Death's Door |
| "kayaking while pregnant" | Direct organic | DCKT post is a top result on this query family |
| "kayaking merit badge" | Organic | DCKT page indexed at pos 6 |

### Invisible (Bad)
| Query | Who wins instead |
|-------|------------------|
| "best kayak tours Door County" | Lakeshore Adventures + Kayak Guide Justin lead |
| "Door County kayak vs Lakeshore Adventures" | Lakeshore dominates |
| "things to do Door County" | Tripadvisor + DDC, no DCKT mention |
| "Door County family vacation activities" | DDC, Travel Wisconsin, Tripadvisor — DCKT zero |
| "Door County spring 2026" | DDC, Tripadvisor, Ashbrooke Hotel — DCKT zero |

**Pattern:** We win when someone searches kayak-specific queries. We disappear from broader Door County queries where AI assembles "things to do" lists. Those are the highest-volume search families and the ones AI Overviews summarize most.

---

## Pillar 1: Structure (Make Content Extractable)

### What's broken

**Homepage** (`/`) — 17,515 impressions in last 90 days
- ❌ Zero JSON-LD schema
- ❌ No "last updated" date
- ❌ No author attribution
- ❌ No FAQ section
- ❌ No definition of what the company does in first 40-60 words extractable form
- ❌ H1 = "Door County Kayak Tours™" (brand only, not query-targeted)

**Cave Point tour page** (`/kayak-tours/cave-point-county-park/`) — 8,143 impressions, pos 14
- ❌ Zero JSON-LD schema (no Tour, Product, Offer, FAQ)
- ❌ No FAQ block
- ❌ No last-updated date
- ❌ No comparison table
- ❌ First paragraph is flowery prose, not extractable definition. Current opener: "Pictures can hardly do justice to the crystal waters..."
- ❌ No specific time, distance, price stated upfront in extractable form

**Door Bluff Shipwreck page** (`/kayak-tours/door-bluff-county-park-shipwreck/`) — 1,025 imp, pos 22.7
- ❌ Zero JSON-LD schema
- ✅ Schooner Fleetwing named in first 200 words (good — that specific name is what AI cites)

**Eco Estuary tour page**
- ✅ Some schema present
- ❌ No FAQ, no step-by-step itinerary, narrative format only

**Blog index** (`/blog/`)
- ❌ Zero publish dates visible
- ❌ Zero author names
- ❌ Zero excerpts — AI can't tell what each post is about from index

**Pregnancy blog post** (already #2 on its target query)
- ✅ Has `BlogPosting` schema with `datePublished` and `dateModified` (2026-05-04)
- ✅ Has visible "Last updated" footer
- ❌ No author with credentials (claims 20+ years company experience but no individual)
- ❌ No FAQ schema even though the article literally has a "Practical questions we get from pregnant paddlers" section
- ❌ No external statistics or citations (Princeton GEO study showed +37-40% citation boost from cited stats)

**Critical gap: Death's Door tour page returns 404.** Per memory we have Death's Door content drafted, but `/kayak-tours/deaths-door-shipwreck-bluff/` doesn't exist. AI is summarizing "Death's Door" as a DCKT offering based on body copy, but there's no destination page to cite.

### What needs fixing (in priority order)

1. **Add FAQ schema to top 10 trafficked pages.** They already contain the answers in body copy. Pull 4-6 FAQs from each, mark up as `FAQPage` JSON-LD. Targets: pregnancy post, Cave Point, Door Bluff, Eco Estuary, types of kayaks, fish creek pillar, baileys harbor pillar, ephraim pillar, merit badge, kayak rental.

2. **Add `TouristTrip` or `Product` schema to all tour pages** with `name`, `description`, `provider` (LocalBusiness), `offers` (price, availability), `duration`, `itinerary`. This is the single biggest missing schema.

3. **Add `LocalBusiness` schema to homepage and footer-injected globally.** Include `address`, `telephone`, `priceRange`, `aggregateRating` (we have 2,000+ 5-star reviews — surface this as `AggregateRating` schema). Currently zero local schema is one reason we get beat by Lakeshore on local queries.

4. **Rewrite the first paragraph of every tour page as a 40-60 word definition block.** Format:
   > "The [Tour Name] is a [duration] guided kayak tour from [launch point] in [town], Wisconsin. Paddlers visit [3 specific named landmarks]. The tour costs $[price], runs [season window], and is suitable for [skill level]. Sit-on-top tandems are provided."

   That paragraph is what AI extracts. The current prose ("Pictures can hardly do justice...") is unextractable.

5. **Add `BreadcrumbList` schema to every page.** Helps AI understand site hierarchy.

6. **Show publish + last-updated dates on every blog post** AND on the blog index. Hidden dates kill freshness signals. AI weights recency heavily.

7. **Create author bio pages** with named guides + credentials (years guiding, certifications — but only ones we actually hold, per memory rule about not claiming ACA cert). Add `Person` schema and reference via `author` on blog posts.

8. **Build out the Death's Door tour page** that AI is already summarizing. It's a free citation sitting on the table.

---

## Pillar 2: Authority (Make Content Citable)

### Princeton GEO findings applied

| Lever | Boost | DCKT status |
|-------|-------|-------------|
| Cite sources | +40% | Almost zero external citations on the site |
| Add statistics | +37% | Some on pregnancy post, mostly absent elsewhere |
| Expert quotations | +30% | Zero named experts quoted |
| Authoritative tone | +25% | Strong on pregnancy post, weak on tour pages |
| Avoid keyword stuffing | +10% (avoiding penalty) | Low risk, current copy is clean |

### What to add

- **Verified statistics with sources.** Customer count ("guided 50,000+ paddlers since 2002"), review count ("2,000+ 5-star reviews"), specific tour stats ("4 miles, 2 hours, 15+ caves visited"). Per memory, founded 2002 — we're sitting on 24 years of credibility we're not citing.
- **Named guide quotes** on tour pages. "According to [guide name], lead guide since [year]: '[specific operational insight]'" — that exact attribution pattern is what AI lifts.
- **External authoritative sources** on informational pages. Pregnancy post should cite ACOG (American College of Obstetricians and Gynecologists) — they have public guidance on exercise during pregnancy. That single citation could push the post to AI Overview default.
- **Real numbers on tour pages.** Specific water temperatures, specific cave counts, specific distances. AI cites pages with numbers over pages with adjectives.

### Freshness

- Homepage shows no date. Add visible "Updated for 2026 season" with `dateModified` schema.
- Blog index shows no dates. Surface them.
- All tour pages need `dateModified` schema and a "2026 pricing & schedule" line.

---

## Pillar 3: Presence (Be Where AI Looks)

This is where the biggest gap is.

### Wikipedia
- The Door County, Wisconsin article does not mention any kayak operator. Not us, not Lakeshore, not anyone.
- **Action:** A neutral edit to the Recreation/Tourism section listing major outfitters (factual, not promotional) is fair game. ChatGPT pulls 7.8% of all citations from Wikipedia — that one mention is high-leverage. Don't write the edit yourself, brief Bella or a contractor familiar with WP norms (advocacy edits get reverted; encyclopedic ones stick).

### Tripadvisor
- We have **three fragmented Tripadvisor listings** (Egg Harbor, Ellison Bay, Sturgeon Bay) plus a Jacksonport one elsewhere. Reviews are split.
- **Action:** Consolidate. The strongest listing should be the Jacksonport address (HQ + most reviews). Tripadvisor lets owners merge or claim duplicates. AI heavily cites Tripadvisor for tour queries.

### Reddit
- No meaningful Reddit presence for DCKT.
- ChatGPT pulls ~1.8% of all citations from Reddit, and r/wisconsin + r/DoorCounty have active threads about "best kayak tour" that we're not in.
- **Action:** Don't astroturf. Have one of the guides do an authentic AMA-style "I guide kayak tours in Door County, AMA" post in r/wisconsin during peak season. One genuine thread = months of AI citation surface.

### YouTube
- Per memory the YouTube channel is launching, with Cave Point as video #1.
- AI Overviews cite YouTube heavily for "how to" and "what to expect" queries.
- **Action:** When publishing, structure description as: 60-word summary → tour facts table → timestamps → FAQ. Same extractable block patterns AI loves on web.

### Travel Wisconsin / Destination Door County
- Already listed. ✅
- **Action:** Update the listing copy to include the same definition-block format and pull in 2026 pricing. These directories are AI source material and we can edit our own listings.

### Industry / Niche citations
- Wisconsin Shipwrecks (`wisconsinshipwrecks.org`) already lists DCKT for shipwreck tours. ✅
- Outdoor publications (Backpacker, Outside, Wisconsin DNR) — zero coverage.
- **Action:** Pitch one outdoor publication per quarter for a guide-perspective piece. One piece in Outside online = permanent AI citation source.

---

## Robots.txt — Status: OK

Verified. AI crawlers are NOT blocked:
- ✅ GPTBot, ChatGPT-User (OpenAI) — allowed
- ✅ PerplexityBot — allowed
- ✅ ClaudeBot, anthropic-ai — allowed
- ✅ Google-Extended (Gemini + AI Overviews) — allowed
- ✅ Bingbot (Copilot) — allowed
- ✅ CCBot — allowed (training crawler — could block if there's a business reason)

The robots.txt blocks a list of spam crawlers (Megaindex, Baiduspider, Yandex, etc.) which is fine. **No action needed here.**

One minor note: sitemap line points to `https://www.doorcountykayaktours.com/sitemap.xml` — verify it returns and is current.

---

## High-Leverage Quick Wins (under 1 week each)

Ranked by impact-to-effort:

| # | Action | Why now | Impact |
|---|--------|---------|--------|
| 1 | Add FAQ schema to top 10 GSC pages (pregnancy, types-of-kayaks, fish-creek, cave-point, baileys-harbor, ephraim, eco-estuary, door-bluff, merit-badge, half-day) | Content already exists; just needs JSON-LD wrapper. Per the WordPress Schema Markup field rules in memory: paste raw JSON, no escaped quotes. | High — direct AI Overview / Perplexity citation lift |
| 2 | Add `TouristTrip` + `Offer` schema to all 8 tour pages | None currently exist. Tour pages are highest-converting. | High — drives rich results in AI tool answers + Google |
| 3 | Add `LocalBusiness` + `AggregateRating` (2,000+ reviews) schema globally | Surfaces social proof in extractable form | High — competitive parity vs Lakeshore |
| 4 | Rewrite first paragraph of every tour page as 40-60 word definition block | Current prose isn't extractable | High — fastest win for AI snippet selection |
| 5 | Surface publish + last-updated dates on all blog posts and the blog index | Freshness signal | Medium — affects ranking weight |
| 6 | Build out Death's Door tour landing page (currently 404) | AI is already summarizing the offering. Page is missing. | Medium — captures already-existing demand |
| 7 | Add ACOG citation + explicit FAQ schema to pregnancy post | Already #2; this push can make it the AI Overview default | Medium — high traffic, easy lift |
| 8 | Add `BreadcrumbList` schema sitewide | Hierarchy signal | Low-medium — schema basics |

---

## Strategic Investments (weeks-to-months)

| # | Action | Why | Impact |
|---|--------|-----|--------|
| 1 | Wikipedia edit: add DCKT (and 2-3 competitors, neutrally) to the Door County, WI article's recreation section | ChatGPT pulls 7.8% of citations from Wikipedia. Currently zero kayak operator mentions. | Compounds for years |
| 2 | Consolidate fragmented Tripadvisor listings to one strong Jacksonport listing | Reviews are split across 3-4 listings; Tripadvisor is heavily cited by AI | High |
| 3 | One authentic Reddit thread per season (guide-led AMA in r/wisconsin and r/Wisconsin_tourism) | Reddit = #2 source for ChatGPT after Wikipedia | High over 12 months |
| 4 | Comparison content: "Door County Kayak Tours vs Lakeshore Adventures" page (fair, balanced, structured table) | Comparison content gets ~33% of AI citations across categories | High — captures branded competitor searches |
| 5 | Author/guide bio pages with `Person` schema and verified credentials only | Adds expert attribution that AI extracts | Medium |
| 6 | Pitch Outside, Backpacker, Wisconsin Public Radio for guide-perspective coverage | One feature = permanent AI citation source | High but slow |
| 7 | YouTube videos with extractable descriptions (definition + table + FAQ) on every upload | Per video #1 production package, per memory | Compounds |
| 8 | Town pillar pages (Fish Creek, Baileys Harbor, Ephraim) — already drafted per memory — push to publish + add FAQ schema | Page-2 town queries (pos 10-12) need a structural push | High — these are leaking ~7,000 impressions/mo |

---

## Specific Page-Level GSC Opportunities

These pages are sitting on impressions but not converting to clicks/citations:

| Page | Impressions | Position | What's missing for AI |
|------|------------|----------|----------------------|
| `/blog/embracing-kayaking-during-pregnancy/` | 13,339 | 2.6 | FAQ schema, ACOG citation, named author |
| `/blog/how-far-can-a-kayak-hang-out-of-a-truck/` | 14,910 | 2.9 | HowTo schema, jurisdiction-by-state table |
| `/blog/different-types-of-kayaks-pros-and-cons/` | 10,388 | 7.9 | ItemList + comparison table schema |
| `/blog/7-reasons-fish-creek-is-the-best-town/` | 26,783 | 8.4 | FAQ schema, LocalBusiness for Fish Creek references |
| `/blog/7-reasons-why-baileys-harbor/` | 9,543 | 10.9 | FAQ schema, freshness update |
| `/blog/7-reasons-why-ephraim/` | 8,219 | 10.5 | Same |
| `/kayak-tours/cave-point-county-park/` | 8,143 | 14.2 | TouristTrip + Offer + FAQ schema, definition rewrite |
| `/kayak-tours/door-bluff-county-park-shipwreck/` | 1,025 | 22.7 | Same + Schooner Fleetwing already named — preserve and structure |
| `/kayak-tours/cave-point-whitefish-dunes-half-day/` | 840 | 28.3 | Half-day positioning per memory rule + schema |
| `/blog/kayaking-merit-badge-requirements/` | (in top queries) | 6.1 | HowTo schema for the requirement steps |

The pregnancy post is the single best AI-citation opportunity on the entire site: 13K impressions, position 2.6, already getting cited in WebSearch summaries, no FAQ schema, no external citations. Adding both could move it to AI Overview default for the entire query family.

---

## What NOT to do

- **Don't keyword-stuff.** Princeton GEO study showed -10% AI visibility for keyword stuffing. Kills citations.
- **Don't gate any kayaking how-to or local guide content.** AI can't cite what it can't read.
- **Don't write generic "we are the best" copy.** AI cites pages with specific numbers, named landmarks, dated facts. Marketing fluff doesn't get cited.
- **Don't use escaped double quotes** in any FAQ schema (per WordPress Schema Markup field rule in CLAUDE.md). Single quotes inside JSON strings are fine.
- **Don't claim ACA cert** anywhere (per memory feedback).
- **Don't fabricate guide credentials.** Use only verified ones.

---

## Monitoring Plan

Set up monthly check, first Monday of each month:
1. Run 20 priority queries through ChatGPT, Perplexity, Google AI Overview (manual)
2. Log: are we cited, who else is, what page of ours got cited
3. Track in a sheet, watch month-over-month
4. After 3 months of data, evaluate paid tools (Otterly AI, Peec AI, ZipTie) — under $200/mo would be reasonable

**The 20 priority queries to track:**
- best kayak tours Door County
- Cave Point kayak tour
- Door County kayak tour for beginners
- Door County shipwreck kayak tour
- Death's Door kayak tour
- kayaking while pregnant
- kayaking merit badge requirements
- types of kayaks pros and cons
- things to do in Door County
- Door County family vacation
- Fish Creek Wisconsin things to do
- Baileys Harbor things to do
- Ephraim Wisconsin things to do
- Door County kayak rental
- Door County e-bike rental
- Door County sauna
- Door County in spring
- best Door County tour company
- kayak Cave Point safe for kids
- Door County bachelorette ideas

---

## Recommended Sequence

**Week 1 (technical foundation):**
- Schema rollout: FAQ + Tour + LocalBusiness + AggregateRating across the top 10 pages identified above. Use the WordPress Schema Markup field per CLAUDE.md rules.
- Surface publish + last-updated dates on blog index + posts.
- Build Death's Door tour page.

**Week 2 (content rewrites):**
- Rewrite first paragraph of all 8 tour pages as 40-60 word definition blocks.
- Add ACOG external citation to pregnancy post.
- Add named guide quote to Cave Point and Eco Estuary pages.

**Weeks 3-4 (presence):**
- Tripadvisor consolidation outreach.
- Wikipedia edit briefed and submitted.
- Plan first Reddit thread for early summer.
- Update Travel Wisconsin + Destination DC listing copy.

**Ongoing:**
- One YouTube upload with structured description per week (per video pipeline).
- One outdoor publication pitch per quarter.
- Monthly AI visibility tracking.

---

## Sources Pulled For This Audit

- Live page fetches: homepage, Cave Point, Door Bluff Shipwreck, Eco Estuary, pregnancy blog, blog index
- robots.txt
- GSC top queries + pages, Feb 9 – May 8, 2026 (90 days)
- Live AI search snippets across 8 priority queries
- Wikipedia (Door County, WI article — no DCKT mentions found)
- Tripadvisor, Travel Wisconsin, Destination Door County listings
- Memory: brand voice, pricing, sit-on-top decision, half-day upsell rule, schema field rules, town pillars status
