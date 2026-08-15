# Buffalo Bayou Kayak — SEO / AEO / GEO Audit (August 2026)

**REPORT ONLY. No changes have been applied to the live site, WordPress, GBP, or any ad account. Generated 2026-08-15.** This document is research and recommendations for David to review and approve. Nothing in this file was published, edited, or pushed live.

**Data constraint, same as June:** buffalobayoukayak.com is still not confirmed connected to Google Search Console or GA4 under the management Google account. No GSC/GA4 MCP exists anywhere in this environment (checked `.mcp.json` for this vault — only `opencx`, `gmail-bbk`, `gbp`, `meta-organic`, `playwright`, `clarity` are configured — and checked `~/.claude.json` globally, no Google Search Console or Analytics MCP is registered for any vault). One new data point worth a look: the live homepage HTML now carries a `google-site-verification` meta tag (`ZTdimCkZr-kTmPpOzczYnKjJzsqLccPSKlkof0W0bU4`). That proves *some* Google account verified this domain in Search Console at some point — it does NOT prove the management account has access. David should check Search Console with whatever account he thinks might own that verification string before assuming access is still missing. Short of that, this audit is built the same way as June's: site crawl (live WebFetch/curl against production), SERP research (WebSearch), competitor analysis, and the vault's own keyword docs. No GSC/GA4 numbers are used or invented anywhere below.

**Second data gap this run:** PageSpeed Insights' keyless quota was exhausted for the day when this audit ran (`RESOURCE_EXHAUSTED`, daily limit already at 0 — likely used up by other business audits run earlier today across the 8-site FH portfolio). No `PSI_KEY` is configured in `~/.claude/.env`. So this report has **no official Lighthouse/Core Web Vitals scores** for BBK this run. What's below instead: real TTFB and page-weight numbers pulled directly via curl against the live production pages, which is a genuine but partial substitute. Recommend getting a free PSI API key added to `~/.claude/.env` (`PSI_KEY=...`) so the next tech-seo pass gets real CWV numbers.

---

## Executive Summary

The biggest story since June: **the June quick-win list actually got executed.** Every tour/rental page now carries live Product + FAQPage JSON-LD, the FAQ page grew from 783 words to roughly 4,400 words with all 21 planned questions visible in page copy (not just schema), the bat-tour H1/title fix, the skyline-tour title/H1 fix, the /about/ meta description fix, and the full alt-text pass all verified live on the production site. That is a genuinely rare thing to find on a re-audit — most quick-win lists rot in a doc. Good execution here.

What did NOT move: the three blog posts staged June 13 (bat colony guide, kayaking-downtown-Houston guide, same-day-things-to-do guide) are still sitting in `Marketing/Blog Drafts - Staged/` marked "do not publish until approved" — confirmed via the live `post-sitemap.xml`, which still shows only the same 11 dead-since-November-2023 posts. That means BBK has had a finished, GEO-flagship bat-colony guide sitting ready for two months, through the entire summer bat season, without shipping. That's the single costliest inaction in this audit. Internal linking is also still exactly where June left it: the blog is orphaned (verified — the bat tour page has zero links to any blog post), and there's no "from the blog" widget anywhere except the homepage's link to 3 of the 11 legacy posts.

Top 3 priorities: (1) get David's approval and publish the 3 staged blog posts — especially the bat guide, which is now shipping two months late relative to peak season; (2) close the loop with real internal linking between tour pages and blog content, since the on-page/schema work is done but isolated; (3) resolve the GSC/GA4/GBP access question definitively — that `google-site-verification` tag is a lead worth 10 minutes of David's time to chase down.

---

## What Changed Since June — Status of the June Action Plan

| June "This Week" Item | Status | How verified |
|---|---|---|
| Get GSC + GA4 + GBP access connected | **Still open** (unconfirmed) | No MCP access; found a `google-site-verification` meta tag live on the homepage — unknown which account it belongs to. Needs David to check. |
| Add Product + FAQPage JSON-LD to all 7 tour pages + rentals | **Done** | Live-fetched and JSON-parsed all 8 pages (bat, skyline, sunset-skyline, serenity, full-moon, paddleboard, rentals, FAQ). All 7 product pages carry `@graph` blocks with `Product` (correct price/offers) + `FAQPage`. |
| Add FAQPage schema + expand /faq/ to 20+ questions with visible text | **Done** | `/faq/` carries `FAQPage` JSON-LD; page body is ~4,400 words (up from June's 783) and contains all 11 questions listed in the implementation guide, confirmed as visible text, not just schema. |
| Fix /about/ meta description | **Done** | Live meta description is 163 chars, no apostrophe truncation: "Buffalo Bayou Kayak offers guided kayak tours, paddleboard tours, and rentals on Buffalo Bayou in downtown Houston. See the skyline and Waugh Bridge bats by water." |
| Fix bat-tour H1 to "Houston Bat Bridge Kayak Tour" | **Done** | Live H1 reads exactly "Houston Bat Bridge Kayak Tour"; title tag reads "Houston Bat Bridge Kayak Tour \| Buffalo Bayou Kayak Tours". |
| Align houston-kayak-tour title/H1 | **Done** | Live title: "Kayaking in Houston \| Houston Skyline Kayak Tour"; live H1: "Houston Skyline Kayak Tour" — matches the recommended fix exactly. |
| Reactivate [FH] Brand campaign + build Bat-Local campaign | **Partially done per the implementation guide's own log** | Brand + Generic Local campaigns were reactivated 2026-06-12 per the guide. The Bat-Local campaign build was left as a manual Google Ads UI task — this audit did not touch the ads account (out of scope, report-only) and can't confirm if it was built. |
| Alt text pass on tour page images | **Done** | Sampled hero + gallery images on all 7 tour/rental pages plus About and Home. All content images carry descriptive alt text matching (often verbatim) the implementation guide's Step 3 table. Only "missing alt" hit sitewide is a Facebook pixel tracking `<img>` (1x1, not user-facing — irrelevant to SEO). |
| **June "This Quarter" items** | | |
| Publish briefs 1-5 (bat guide first) | **Drafted, not published** | 3 of 5 briefs are fully drafted and staged (bat colony guide = brief 1; kayaking-downtown-Houston guide covers brief 2's ground; same-day-things-to-do covers brief 7's ground). All 3 dated 2026-06-13, still flagged "do not publish until approved," still absent from the live sitemap as of today. |
| Internal linking: blog block on tour pages, hub interlinks | **Still open** | Verified live: bat tour page has zero links to any blog content. Homepage links to only 3 of the 11 legacy posts via a widget. No change from June. |
| Earned-citation outreach (paddlingmag, 365thingsinhouston, Houstonia) | **Still open** | Re-checked paddlingmag's "Guide To Kayaking Houston" via search — it still surfaces Bayou City Adventures and Discovery Green, not BBK. Still an open outreach task. |
| Refresh/merge the 8 thin 2023 history posts | **Still open** | Confirmed via `post-sitemap.xml` — all 8 history posts are still live individually, unchanged since Nov 2023. |

---

## Live Technical Findings (this run)

### Redirects
- `https://buffalobayoukayak.com` → 200, 0 redirects (clean).
- `https://www.buffalobayoukayak.com` → 1 redirect → clean 301 to non-www HTTPS.
- `http://buffalobayoukayak.com` → 1 redirect → clean 301 to HTTPS non-www.
No chains, no loops, no mixed signals. Matches June's "fine" verdict.

### robots.txt
Still fine. Junk/scraper bots (MegaIndex, Barkrowler, BLEXBot, Baiduspider, etc.) blocked; no entry blocking GPTBot, ClaudeBot, or PerplexityBot — still correct for GEO. The June audit's cosmetic note is still true: the `Disallow: /fhbr-console/` and `Disallow: /cdn-cgi/` lines sit after the last named user-agent group (harmless, but worth a cleanup pass whenever someone's in the file for another reason).

### Sitemap
3-index structure unchanged (`page-sitemap.xml`, `activity-sitemap.xml`, `post-sitemap.xml`). `post-sitemap.xml` confirmed to contain only the same 11 posts from Nov 2023 — nothing published since. All sitemap URLs spot-checked return 200.

### Broken-link crawl
Crawled all 18 primary nav / footer links (tours, rentals, about, FAQ, contact, corporate events, membership, cleanup, walking tours, cross-sell pages). **Zero 4xx/5xx.** All 200.

### Page weight / TTFB (curl, not Lighthouse — see data-gap note above)
| Page | TTFB | Total load | HTML size |
|---|---|---|---|
| Homepage | 0.96s | 1.81s | 185 KB |
| /kayak-tours/houston-bat-bridge-kayak-tour/ | 0.75s | 1.42s | 141 KB |
| /kayak-tours/houston-kayak-tour/ | 0.94s | 1.27s | 142 KB |
| /watersports-rental/ | 0.95s | 1.18s | 150 KB |
| /faq/ | 0.59s | 1.05s | 145 KB |
| /about/ | 0.57s | 0.95s | 119 KB |

TTFB in the 0.6-1.0s range server-side is on the slow side for a first byte (good is generally sub-0.3-0.4s) and is a plausible drag on LCP, but without real Lighthouse/CrUX data this is a signal, not a diagnosis — get the PSI key added and re-run before spending dev time chasing it.

### Duplicate content flag (new finding, not in June audit)
There are two separate live "skyline" tour pages: `/kayak-tours/houston-kayak-tour/` (H1 "Houston Skyline Kayak Tour," daytime departures 10am/1pm) and `/kayak-tours/sunset-skyline-tour/` (H1 "Sunset Skyline Tour," title "Houston Sunset Kayaking"). These are legitimately different products (day tour vs. sunset tour) and each has its own Product+FAQPage schema and distinct canonical — not a duplicate-content bug. Flagging only because June's audit described "7 tour pages" without naming this one explicitly, and the nav shows it as a separate primary link. Worth confirming the July 23-dated `sunset-skyline-tour.json` schema file (one day after the other 7) means this page was a later addition to the schema rollout — it was, and it's live.

---

## Keyword / Content Findings (SERP research, no GSC)

### What's holding or improving since June
- **"is buffalo bayou safe to kayak" / alligator query cluster** — BBK's existing 2023 post (`/2023/11/02/are-alligators-safe-to-kayak-with/`) is now the *top* organic result in a live search check for "is Buffalo Bayou safe to kayak alligators," ahead of pinkyskayakrental.com and itsnothouitsme.com. June flagged this as "held by tiny niche blogs" — that's no longer accurate. The opportunity here has shifted from "win the ranking" to "the page already ranks, but it's thin and dated — expand it and it should hold or grow, not need to fight from behind." Brief 4 in the June content plan (upgrade the alligator post) is now lower-urgency than briefs 1-2.
- **"Waugh Bridge bats" queries** — BBK's bat tour page now surfaces directly in a live search for "Waugh Bridge bats Houston kayak tour," alongside 365thingsinhouston, TripAdvisor, downtownhouston.org, and TPWD. Encouraging, though this query already contains "kayak" so it doesn't yet prove BBK broke into the pure informational bat-search space the way brief 1 (the standalone bat guide) is designed to do.

### What's still open, confirmed via live search
- **paddlingmag.com's "Guide To Kayaking Houston"** — re-checked directly. Still surfaces Bayou City Adventures (Discovery Green rentals) and the North York Boat Launch as the go-to Buffalo Bayou access points. BBK is still not named. Outreach to paddlingmag remains an open, worthwhile ask — cite the live schema/FAQ work and the (once published) bat guide as reasons to include BBK.
- **Houstonia's "7 Best Spots to Paddle and Rent Kayaks in Houston"** — still the authoritative local listicle in this space; BBK's presence in it wasn't confirmed either way in this pass (would need a direct fetch of the article, not just search snippets — worth a follow-up).
- **Bayou City Adventures** — still open, active, still the name that shows up first in searches for Houston kayak rentals generally (1520 Silver St, Yelp reviews current through July 2026). Still the competitor whose legacy citations BBK needs to out-content, not out-rank on brand terms (BBK already wins those).

### Content plan status (against June's 12 briefs)
| # | Brief | Status |
|---|---|---|
| 1 | Waugh Bridge Bat Colony Guide | **Drafted, staged, unpublished** since 2026-06-13 |
| 2 | Where to Kayak in Houston (guide) | **Partially covered** by the staged "Kayaking Downtown Houston: A Local's Guide to Buffalo Bayou" draft — narrower scope than the original brief (doesn't cover competitor launches/rentals citywide the way brief 2 specified), also unpublished |
| 3 | Is Buffalo Bayou Safe to Kayak? | Not drafted. Lower urgency now — see above, the existing alligator post already ranks #1 in a spot-check |
| 4 | Are There Alligators in Buffalo Bayou? (upgrade) | Not drafted/upgraded |
| 5 | Buffalo Bayou Park Guide | Not drafted |
| 6 | Houston Date Ideas on the Water | Not drafted |
| 7 | Things to Do Outdoors Downtown Houston | **Loosely covered** by the staged "Same-Day Things to Do in Houston This Summer" draft — seasonal/urgency framing rather than evergreen discovery framing, unpublished |
| 8 | Kayaking for Beginners in Houston | Not drafted |
| 9 | Best Time of Year to Kayak in Houston | Not drafted |
| 10 | Houston Skyline Photo Spots | Not drafted |
| 11 | Team Building in Houston | Not drafted |
| 12 | Full Moon Kayak Dates 2026 | Not drafted |

3 of 12 briefs have drafts; 0 of 12 are published.

---

## Prioritized Fix List

### Quick Wins (this week — all are approve-and-publish or single-page edits)

1. **Publish `Marketing/Blog Drafts - Staged/2026-06-13 - houston-bat-kayak-tour-waugh-bridge.md`** to the live blog. It has sat finished for 2 months through peak bat season (Feb-Nov per June's own seasonality note). This is the single highest-value item in this report — it's already written, reviewed once, and the GEO flagship the June audit called for. Expected impact: gives AI answer engines and Google an actual page to cite for "Waugh Bridge bats" informational queries, currently owned by buffalobayou.org/365thingsinhouston/TPWD.
2. **Publish the other 2 staged drafts** (`2026-06-13 - kayaking-downtown-houston-buffalo-bayou.md`, `2026-06-13 - same-day-things-to-do-houston-summer.md`) after the same review. Expected impact: starts rebuilding the blog as a live content asset instead of a dead 2023 archive; gives Google fresh crawl signal on a site whose newest post is otherwise 33 months old.
3. **Add a "From the Blog" link block to the bat tour page** (`/kayak-tours/houston-bat-bridge-kayak-tour/`), linking to the bat colony guide once published, plus 1-2 links from the new blog posts back to the bat tour, skyline tour, and rentals pages with descriptive anchors (e.g., "Houston bat bridge kayak tour," not "book now"). This is the exact linking spec from the June implementation guide's Step 4, still undone. Expected impact: stops leaking equity from the money pages to an orphaned blog and back — currently zero internal links exist in either direction.
4. **Chase down the `google-site-verification` meta tag** (`ZTdimCkZr-kTmPpOzczYnKjJzsqLccPSKlkof0W0bU4`) live on the homepage. Someone verified this domain in Search Console at some point under some Google account. Ask David: does he recognize this, or should Connor/whoever built the site originally be asked? Expected impact: could resolve the entire GSC access gap in one login instead of a re-verification process.
5. **Clean up the two stray `Disallow:` lines in `robots.txt`** (`/fhbr-console/`, `/cdn-cgi/`) that sit orphaned after the last named user-agent block instead of under `User-agent: *`. Cosmetic and low-risk, but it's been flagged twice now (June and this pass) and takes one FareHarbor support ticket to fix. Expected impact: none functionally (crawlers likely still respect it), but removes ambiguity for any crawler that parses strictly.

### Strategic Work (this quarter)

1. **Draft and publish briefs 3-4 as a combined "Is Buffalo Bayou Safe to Kayak?" pillar** that folds in and upgrades the existing 2023 alligator post rather than treating them as two separate pieces — the alligator post is already the top live result in a spot-check for this query cluster, so this is "expand a winner," not "fight from behind." Expected impact: consolidates two competing thin pages into one strong page eligible for a featured snippet / AI Overview citation on "is buffalo bayou safe to kayak."
2. **Earned-citation outreach to paddlingmag.com and 365thingsinhouston**, now that BBK actually has something concrete to offer as a pitch: live Product/FAQ schema, an expanded FAQ page, and (once published) the bat colony guide. June's outreach recommendation stalled because there was nothing new to point to — that's no longer true. Expected impact: paddlingmag's "Guide To Kayaking Houston" and the 365thingsinhouston bat piece are both cited directly by AI answer engines per the June GEO findings; inclusion there is a GEO win that ranking alone can't buy.
3. **Merge the 8 thin 2023 history posts into one "History of Buffalo Bayou" pillar with 301s from the rest**, per June's recommendation — still fully open, still sitting as 8 separate 400-800 word essays dated Nov 2023 that dilute topical authority instead of consolidating it. Expected impact: turns 8 weak, orphaned pages into 1 strong page with a shot at ranking, and stops them looking like an abandoned blog to both users and AI crawlers.
4. **Draft briefs 5, 6, 8, 9, 10, 11, 12** — the 9 briefs from June's content plan that still have zero draft. Priority order given what's now known: brief 5 (Buffalo Bayou Park guide — utility page, wins "things to do" discovery queries) and brief 12 (Full Moon Kayak Dates 2026 — direct booking intent, needs annual refresh anyway) first; the rest can follow the original June order.
5. **Get a `PSI_KEY` added to `~/.claude/.env`** so future tech-seo passes for BBK (and the other 7 FH-portfolio sites) get real Lighthouse/CWV numbers instead of hitting the keyless daily quota. This is infrastructure, not a site fix, but it blocks getting real performance data on every future audit run until it's done. Expected impact: unblocks accurate LCP/CLS/INP measurement, which the elevated TTFB numbers in this report suggest may be worth investigating once real data exists.
6. **Resolve GSC/GA4/GBP access** — still the single most repeated line item across both audits. Everything in the Keyword / Content sections of both this report and June's is inference from SERP research because there's no first-party data. Expected impact: unlocks real striking-distance keyword data, real CTR problems, real conversion attribution — this is the item that makes every future SEO audit for BBK dramatically more accurate.

---

## Notes on Scope

This audit did not touch or verify: the Google Ads account (Bat-Local campaign build status — out of scope, ads account access wasn't part of this report-only run), GBP listing status, or a full crawl of every page on the site (this pass focused on the pages named in the June audit plus the primary nav, consistent with June's 15-page scope). The Houstonia listicle inclusion question is flagged as unresolved and worth a direct follow-up fetch rather than relying on search snippets.
