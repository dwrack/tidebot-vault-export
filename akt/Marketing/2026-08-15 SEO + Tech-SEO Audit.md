# Austin Kayak Tours — SEO + Tech-SEO Audit (2026-08-15)

**This is a report only. No changes were made to the live site, WordPress, GBP, or ads. Everything below is a finding or a recommendation for David/Connor/dev to act on later.**

## Data sources used this session

- **Live site crawl** — direct `curl` + Python parsing against `https://www.austinkayaktours.com` (homepage, FAQ, Halloween tour, All Day Skyline/Swimming Hole tour, the two duplicate-URL pairs, robots.txt, all 3 sitemap files, the JSON-LD blocks actually present on the homepage and Halloween page) run today, 2026-08-15.
- **`lonestarkayaktours.com`** — re-crawled directly (headers + head `<title>`/meta/canonical) to confirm current status.
- **PageSpeed Insights API** — attempted via `~/Projects/tech-seo/psi-run.mjs`. Returned HTTP 429 (quota exceeded) again. Second consecutive day blocked.
- **WebSearch** — live SERP spot-check for "austin kayak tours" / "lonestarkayaktours" / bat tour queries today.
- **Vault docs** — yesterday's audit (`2026-08-14 SEO + Tech-SEO Audit.md`), `01-05` SEO Content library, both Pillar drafts, all 10 Cluster folders, `Blog Drafts - Staged/`, `Ranking Baseline 2026-06-07.md`, `SEO Action Plan & Blog Pipeline.md`, `AI-SEO-Bat-Tours-Action-Plan.md`.
- **GSC and GA4 were NOT available this session** — same as yesterday. This vault's `.mcp.json` still only has `google-austin`, `gbp`, `meta-organic`, `playwright`, `opencx`, `clarity`. A ToolSearch for "search console" / "analytics GA4" / "GSC" surfaced no matching connected tools. **This is the second consecutive audit blocked on this.** Every keyword position/impression number below is still the `Ranking Baseline 2026-06-07.md` snapshot — now **10 weeks stale** and sourced from the legacy `lonestarkayaktours.com` GSC property. Recommend David connect a GSC MCP before the next audit; two audits in a row have shipped an action plan built on 10-week-old data from the wrong domain's property.

---

## Executive Summary

Nothing structural changed since yesterday, and that's itself the headline finding: **every Quick Win from the 2026-08-14 audit is still open.** The FAQ page still has zero FAQPage schema, the two pillar pages are still not published (both still 404), the `lonestarkayaktours.com` duplicate domain is still live and self-canonicalizing, the duplicate URL pairs are still both indexable, and `/kayak-paddleboard-rental/` is still a dead 404. Nothing shipped in the last 24 hours. This is one day of runway, not a crisis, but it's worth naming plainly: the highest-leverage items on this list (FAQ schema, the pillar pages) are each under an hour of work and are still sitting undone two audits running.

One correction to yesterday's diagnosis: the homepage schema situation is more nuanced than "missing." FareHarbor's theme auto-generates `Organization`, `LocalBusiness`, `WebSite`, `WebPage`, and a `Product`-type review block on the homepage (5 JSON-LD blocks, confirmed live today). But the `LocalBusiness` block has an **empty `openingHoursSpecification`, no `sameAs` social links, and no `aggregateRating`** — and the review data that does exist lives on a separate `Product` block showing only **4 reviews**, nowhere close to the "500+ on TripAdvisor" the vault's schema draft assumes. So the fix isn't "paste schema that doesn't exist," it's "the auto-schema is thin and the review count looks worse than reality" — different exact action, same urgency.

New finding today: a live SERP check for "austin kayak tours" / bat tour queries surfaced **kayakaustintours.com** (word-order swap of the real domain) and **austinpaddle.com** as live competitors not flagged in any prior audit. `kayakaustintours.com` in particular is a brand-confusion risk on top of the existing `lonestarkayaktours.com` problem — worth a look to confirm whether it's a copycat, an affiliate scraper, or unrelated.

Top 3 priorities by impact, unchanged from yesterday because nothing on this list moved: (1) resolve the `lonestarkayaktours.com` duplicate-domain problem, (2) ship the FAQ schema and publish the two pillar pages — all three are under an hour combined and still not done, (3) fix the duplicate-URL/canonical issue on paddleboard-tour and corporate-events pages.

---

## What's still open vs. yesterday (explicit reconciliation)

### Quick Wins from 2026-08-14 — status today

| # | Item | Status today |
|---|---|---|
| 1 | Paste FAQPage schema onto `/faq/` | **Still open.** Confirmed via live crawl: zero occurrences of "FAQPage" in the page source. |
| 2 | Paste homepage LocalBusiness + Organization schema | **Partially superseded — see correction above.** The schema types exist (auto-generated), but are thin: no `sameAs`, no hours, no proper `aggregateRating` on the `LocalBusiness` block, and the review count feeding the site (4) is far below the real TripAdvisor number. Reframe this task as "fix/extend the existing auto-schema" rather than "add schema from scratch." |
| 3 | Fix `/kayak-paddleboard-rental/` 404 | **Still open.** Confirmed 404 today. |
| 4 | Publish the two pillar pages | **Still open.** `/best-places-to-kayak-in-austin/` and `/kayaking-lady-bird-lake/` both confirmed 404 today. Not in `page-sitemap.xml` (9 URLs, unchanged from yesterday). |
| 5 | Replace homepage "Learn More" CTAs | **Not re-verified this session** (not re-crawled at DOM-interaction depth); no evidence it was touched. Assume still open. |
| 6 | Add internal links from 4 confirmed-live blog posts | **Not re-verified this session** at the anchor-text level; assume still open, nothing in the vault suggests this shipped. |

### Strategic Work from 2026-08-14 — status today

| # | Item | Status today |
|---|---|---|
| 1 | Resolve `lonestarkayaktours.com` duplicate domain | **Still open.** Re-crawled today: HTTP 200, title "Lone Star Kayak Tours \| Kayak Tours in Austin, TX", self-referencing `rel="canonical"` to `lonestarkayaktours.com/`, `robots: index,follow`. Confirmed via WebSearch today it still surfaces in the same result set as `austinkayaktours.com` for near-branded queries. |
| 2 | Consolidate duplicate URL pairs | **Still open.** `/paddleboard-tour/` + `/austin-kayak-tours/paddleboard-tour/` both HTTP 200 today. `/corporate-events/` + `/austin-kayak-tours/corporate-events/` both HTTP 200 today. |
| 3 | Reconcile vault SEO docs against live site | **Still open.** `01 - Title & Meta Rewrites.md` and `04 - Internal Linking Map.md` still reference `/sunrise-tour/`, `/sunset-skyline-tour/`, `/paddle-board-lessons/`, `/about-us/`, `/4th-of-july-fireworks-tour/` — all re-confirmed 404 today except the correctly-slugged `/austin-kayak-tours/fourth-of-july-tour/`, which is live. |
| 4 | Decide on Sunrise Tour / About page | **Still open**, no new information this session. |
| 5 | Build SEO coverage for Halloween Tour + All Day Skyline/Swimming Hole Tour | **Still open, re-confirmed today.** Both pages live (HTTP 200). Both have exactly **1 JSON-LD block each — an auto-generated `BreadcrumbList`, nothing else.** No `Product` schema, no `FAQPage`, no custom title/meta work beyond FareHarbor defaults. Zero internal links from any blog post in either the live 57-post sitemap or the drafted clusters. |
| 6 | Publish Cluster A + staged blog drafts | **Still open.** `post-sitemap.xml` re-pulled today: still exactly **57 URLs**, same list as yesterday (verified by diffing slugs — no Cluster A titles, no pillar page, no staged-draft slugs present). |
| 7 | Set up real Core Web Vitals baseline | **Still open — still blocked.** `psi-run.mjs both` and the AKT-specific run both returned HTTP 429 today, same as yesterday, same shared-quota project, still no `PSI_KEY` in `~/.claude/.env`. Two audits in a row with zero CWV data. |
| 8 | Connect GSC/GA4 MCP | **Still open.** See Data Sources section above — second consecutive audit with no GSC/GA4 access. |

**Bottom line on reconciliation: 13 of 14 tracked items from yesterday are unchanged. Zero live-site changes appear to have shipped in the last 24 hours.** The one nuance is the homepage schema diagnosis, which is a correction, not progress.

---

## New findings this session (not in yesterday's audit)

1. **Two additional competitors surfaced in a live SERP check today:** `kayakaustintours.com` (word-order swap of `austinkayaktours.com` — worth confirming whether this is a copycat/affiliate site or unrelated, because the name collision risk compounds the existing `lonestarkayaktours.com` confusion) and `austinpaddle.com` ("Austin Paddle Shack" — SUP/kayak rentals and tours on Lady Bird Lake, not previously on the competitor list). Neither appeared in the 2026-06-09 AI-SEO doc's competitor set or yesterday's audit.
2. **Homepage schema is present but thin, not absent.** Corrected above — the `LocalBusiness` JSON-LD block has an empty `openingHoursSpecification: []`, no `sameAs` array (no links to Facebook/Instagram/TripAdvisor/Yelp despite those profiles existing), and the only review signal on the page is a `Product`-type block showing `reviewCount: 4`. That number is what any AI engine or rich-result parser would see today if it reads the homepage schema — worth fixing before chasing AI-citation moves elsewhere, since a visible "4 reviews" undercuts trust more than showing nothing.
3. **Halloween Tour and All Day Skyline/Swimming Hole Tour pages confirmed to have literally one schema block each (BreadcrumbList only)** — this sharpens yesterday's finding (which flagged them as "no schema, no linking") with the exact current state: FareHarbor's auto-schema doesn't extend `Product` type to these two pages the way it does for the flagship tours, so this isn't just an SEO-doc gap, it's a template-level gap on these two specific pages.
4. **The 6 staged blog drafts (3 from June 13, 3 from August 14) already cover some ground not in the original 50-post pipeline.** `how-much-does-a-kayak-tour-cost-in-austin.md` and `is-lady-bird-lake-safe-to-kayak.md` (both dated 2026-08-14) are cost- and safety-intent topics that don't map to any of the 50 titles in `SEO Action Plan & Blog Pipeline.md` — these look like direct-answer / AI-Overview bait, which is a smart addition, but they're still unpublished like everything else in that folder.

---

## Content gap recommendations (topics NOT covered anywhere — for the content handoff)

These are real gaps confirmed against: the live 57-post sitemap, all 10 Cluster folders, both Pillar drafts, and all 6 files in `Blog Drafts - Staged/`. None of the below duplicate any existing draft or live post.

1. **Halloween Tour supporting content.** Real, live, bookable page (`/austin-kayak-tours/halloween-tour/`) with zero blog support anywhere in the pipeline. A seasonal post ("Halloween Kayak Tour in Austin: What to Expect") would be new, not a duplicate of Cluster E's seasonal posts (which cover spring/summer/fall/winter/4th of July/NYE, not Halloween).
2. **All Day Skyline and Swimming Hole Tour supporting content.** Same situation — live page, zero content anywhere, and no cluster or draft references "swimming hole" at all.
3. **Clear/crystal kayak comparison post.** Flagged as a competitive gap in yesterday's audit (competitors now running "Clear Kayak Tours" on Lady Bird Lake) and still not written or drafted anywhere.
4. **Brand-disambiguation content.** With `kayakaustintours.com`, `lonestarkayaktours.com`, and now a new near-name competitor all live, a real About page (already flagged as missing) plus explicit "who we are" content becomes more urgent — not just an E-E-A-T nice-to-have but a defensive move against name confusion in search and in AI answers.
5. **"Austin Paddle Shack" / competitor-alternative style content.** Not urgent, but worth a future comparison post once the higher-priority gaps above are closed.

---

## Full target keyword set audited against this session

Same combined set as yesterday (GSC snapshot is unchanged — no new pull was possible), reconciled against everything drafted or live. Hand this to the content-writing task; **do not** assign any of these 50 pipeline titles, the 2 pillar topics, or the 6 staged-draft topics as "new" — pick from the gaps above instead, or from adjacent long-tail variants not already claimed below.

**Head/commercial terms (from `Ranking Baseline 2026-06-07.md`, GSC snapshot, stale):**
austin kayak tours, kayak tours austin, kayak austin, austin kayak, austin kayaking, lady bird lake kayak rental, best place to kayak in austin, austin bat tours, bat tours austin, austin bat kayak tour, bat kayak tour austin, austin kayak bat tour, congress bridge bats (informational)

**50-post pipeline target keywords (all already assigned — do not duplicate):**
kayaking lady bird lake; kayak launch lady bird lake; lady bird lake kayak rules; best time kayak lady bird lake; lady bird lake vs lake travis kayaking; parking lady bird lake kayak; when do bats come out congress bridge; best way to see austin bats; bat bridge kayak tour; sunset kayaking austin; austin bats facts; austin skyline from water; tallest buildings austin; austin architecture tour; most photographed buildings austin; austin skyline changes; beginner kayaking austin; what to wear kayaking austin; what to bring kayak tour; are kayak tours worth it; solo kayaking austin; kayaking austin spring; summer kayaking austin; fall kayaking austin; winter kayaking austin; 4th of july kayak austin; new years eve kayak austin; austin bachelorette kayak; austin corporate team building water; austin birthday kayak; date night austin kayak; family kayaking austin; group kayak austin; best places to kayak near austin; kayaking lake travis; kayaking barton creek; kayaking san marcos river; paddle board lady bird lake; kayak vs paddle board lady bird lake; paddle board lessons austin; paddle board bat tour; sunrise vs sunset kayak austin; kayak rental vs tour austin; best kayak tour austin tourist; skyline vs bat kayak tour; cheap things to do austin outdoors; downtown austin day; restaurants near lady bird lake; dog friendly austin kayak; austin one day itinerary

**Pillar keywords (drafted, not live):**
best place to kayak in austin (pillar 1); kayaking lady bird lake + variants (pillar 2)

**6 staged-draft topics (already claimed, do not reassign):**
austin bat kayak tour bridge vs water; kayaking in austin downtown / Lady Bird Lake guide; sunset kayaking in austin; bachelor party kayaking austin; how much does a kayak tour cost in austin; is Lady Bird Lake safe to kayak

**Open — genuinely available for new content (see Content Gap section above):** Halloween kayak tour; All Day Skyline and Swimming Hole Tour; clear/crystal kayak tour comparison; brand-disambiguation / About page content; Austin Paddle Shack competitor comparison.

---

## Technical SEO Checklist

| Check | Status | Details |
|---|---|---|
| Legacy domain redirect | **FAIL (unchanged)** | `lonestarkayaktours.com` still HTTP 200, self-canonicalizing, `index,follow`, own title/meta, showing in live SERP alongside the main domain today. |
| Duplicate URLs, same content | **FAIL (unchanged)** | `/paddleboard-tour/` + `/austin-kayak-tours/paddleboard-tour/` and `/corporate-events/` + `/austin-kayak-tours/corporate-events/` all still independently HTTP 200. |
| robots.txt | **PASS (unchanged)** | Valid, references sitemap, disallows only low-value bots and `/edit/`, `/fhbr-console/`, `/cdn-cgi/`. AI crawlers (GPTBot, ClaudeBot, PerplexityBot) still not blocked. |
| sitemap.xml | **PASS structurally (unchanged)** | Sitemap index → `page-sitemap.xml` (9 URLs), `activity-sitemap.xml`, `post-sitemap.xml` (57 URLs, re-confirmed identical slug list to yesterday). |
| Core Web Vitals / Lighthouse | **NOT AVAILABLE (2nd consecutive day)** | PSI API HTTP 429 again today via `psi-run.mjs`. No `PSI_KEY` configured. Recommend adding a free PSI key before the next run — this is now blocking two audits running. |
| GSC index status | **NOT AVAILABLE (2nd consecutive day)** | No GSC MCP connected. |
| Known 404s | **All unchanged, still broken** | `/kayak-paddleboard-rental/`, `/4th-of-july-fireworks-tour/` (correct live slug is `/austin-kayak-tours/fourth-of-july-tour/`), `/sunrise-tour/`, `/sunset-skyline-tour/`, `/paddle-board-lessons/`, `/about-us/` — all re-confirmed 404 today. |
| Money pages spot-checked healthy | **PASS** | `/rental/`, `/austin-kayak-tours/fourth-of-july-tour/`, `/new-years-eve-fireworks-tour/`, `/austin-walking-tours/`, `/rainey-street-walking-bar-tour/` all HTTP 200 today. |

---

## On-page issues table

| Page | Issue | Severity | Recommended Fix |
|---|---|---|---|
| `/faq/` | Zero FAQPage schema despite the entire page being FAQ content | Critical | Paste the JSON-LD already drafted in `02 - Schema Markup Library.md` into the ACF Schema Markup field. Still a copy-paste job, still not done. |
| `/` (homepage) | LocalBusiness schema block is live but has empty `openingHoursSpecification`, no `sameAs`, and the site's visible review count via schema is 4 (Product block), not a real TripAdvisor/Google number | High | Extend the existing auto-schema (don't just paste the vault's standalone draft over it — check for duplication) with real hours, `sameAs` links to Facebook/Instagram/TripAdvisor/Yelp, and either suppress the low review count or replace it with the real aggregate. |
| `/austin-kayak-tours/halloween-tour/` | Only a BreadcrumbList schema block; no Product schema, no dedicated title/meta beyond defaults, zero internal links in from any post | High | Add Product schema per the library pattern, write 2-3 internal links from seasonal content once written. |
| `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` | Same as Halloween — BreadcrumbList only, zero internal links | High | Same fix pattern. |
| `/paddleboard-tour/` + `/austin-kayak-tours/paddleboard-tour/` | Duplicate URL pair, both self-canonicalizing | Critical | 301 one to the other per the May 9 plan. |
| `/corporate-events/` + `/austin-kayak-tours/corporate-events/` | Duplicate URL pair, both self-canonicalizing | Critical | Same fix. |
| `lonestarkayaktours.com` (whole domain) | Live, indexed, self-canonicalizing duplicate of the business | Critical | Needs a dev/FareHarbor conversation — 301 map or explicit differentiation. |

---

## Internal linking — no change from yesterday's corrected table

`04 - Internal Linking Map.md`'s corrected recommendations from the 2026-08-14 audit are still accurate and still not executed. Not re-litigated here in full — see that file's "Internal linking — corrected recommendations" section. Nothing indicates any of those 8 link additions shipped.

---

## Competitor comparison summary

| Dimension | AKT | Live Love Paddle | Boats and Bats | Get Up and Go Kayaking | kayakaustintours.com (new) | austinpaddle.com (new) |
|---|---|---|---|---|---|---|
| Bat tour price shown | Yes ($50) | Not verified this session | Not verified this session | Yes (bat tour listed) | Not verified this session | Not verified this session |
| FAQ schema | No | Not verified | Not verified | Not verified | Not verified | Not verified |
| Clear/crystal kayak option | No | No | No | **Yes** | Not verified | Not verified |
| Brand confusion risk | — | Low | Low | Low | **High — near-identical name** | Low |

kayakaustintours.com and austinpaddle.com are new sightings this session, not fully profiled yet — flagging for a closer look next audit rather than treating this table as complete.

---

## Prioritized Fix List

### Quick Wins (this week, low effort / high leverage — carried forward, still undone)

1. **Paste FAQPage schema onto `/faq/`.** Unchanged from yesterday. Still the single highest-ROI item on this list and still not done. JSON-LD is already written in `02 - Schema Markup Library.md`.
2. **Fix the homepage LocalBusiness schema — extend, don't replace.** Corrected scope: add `sameAs` (Facebook, Instagram, TripAdvisor, Yelp — all exist per the vault's own schema draft), populate `openingHoursSpecification`, and resolve the `reviewCount: 4` problem (either pull the real TripAdvisor/Google number into a proper `aggregateRating` on the `LocalBusiness` type, or drop the misleadingly-low count entirely). Expected impact: prevents any AI engine or rich-result parser from surfacing "4 reviews" as the trust signal for a business that has far more.
3. **Fix the `/kayak-paddleboard-rental/` 404.** Unchanged, still live, still flagged since May 9.
4. **Publish the two ready-to-go pillar pages.** Unchanged, still 404, still fully drafted and sitting idle. "best place to kayak in austin" (2,799 impressions at position 13, zero clicks per the stale GSC snapshot) is still unclaimed.
5. **Add Product schema to the Halloween Tour and All Day Skyline/Swimming Hole Tour pages.** New concrete ask this session, since today's crawl confirmed both pages currently have exactly one schema block (auto BreadcrumbList) and nothing else. Use the Product schema pattern from `02 - Schema Markup Library.md`.
6. **Replace homepage "Learn More" CTAs / add the 4 confirmed blog-post internal links.** Carried forward from yesterday, not re-verified but presumed still open.

### Strategic Work (this quarter, higher effort — carried forward, still undone)

1. **Resolve the `lonestarkayaktours.com` duplicate-domain problem.** Unchanged, now confirmed live two audits running. This is plausibly the single biggest drag on the whole ranking table.
2. **Consolidate the duplicate URL pairs** (`paddleboard-tour`, `corporate-events`). Unchanged.
3. **Reconcile the vault's SEO Content docs against the live site.** Unchanged — the same broken slugs are still referenced in `01 - Title & Meta Rewrites.md` and `04 - Internal Linking Map.md`.
4. **Investigate `kayakaustintours.com` and `austinpaddle.com`.** New this session. Confirm whether `kayakaustintours.com` is a copycat/scraper site (the near-identical name is the concern) or a legitimate unrelated operator, and whether either is siphoning branded search traffic.
5. **Build SEO coverage for the two orphaned live products (Halloween, All Day Skyline/Swimming Hole).** Unchanged in scope, sharpened today with the exact schema gap.
6. **Publish Cluster A (5 posts) and the 3 older staged drafts.** Unchanged — post-sitemap still 57 URLs, no new content live.
7. **Get a PSI API key and set up a real Core Web Vitals baseline.** Now blocking two consecutive audits. `PSI_KEY` should go in `~/.claude/.env` before the next run — recommend prioritizing this purely because it's cheap (free tier) and keeps costing a full audit's worth of technical blindness every day it's skipped.
8. **Connect a GSC (and ideally GA4) MCP for this vault.** Same recommendation as yesterday, now with two consecutive audits as evidence of the cost — every keyword number in both reports is a 10-week-old snapshot from the wrong domain's property.

---

*Compiled 2026-08-15. No live-site, WordPress, GBP, or ad changes were made in the course of producing this report.*
