# Austin Kayak Tours — SEO + Tech-SEO Audit (2026-08-16)

**REPORT ONLY — OVERNIGHT UNATTENDED PASS. No changes were made to the live site, WordPress, GBP listing, or any ad account. Every item below is a staged recommendation pending David's review.**

This is the fourth audit in four sessions (2026-08-14, 2026-08-15 AM, 2026-08-15 Pass 2, this one). It does not re-litigate findings already logged as open — see the reconciliation table below for live-verified status on everything already flagged. New value this pass: a fourth-day PSI status check, a title/meta character-length pass that hadn't been done yet, exact-duplicate confirmation on the two URL pairs, a redirect-chain check on the brand-hijack domain, and a scan of what's moved in the vault's content pipeline since Pass 2.

## Data sources used this session

- **Live site crawl** — direct `curl` + Python parsing against `https://www.austinkayaktours.com` (homepage, FAQ, Halloween tour, All Day Skyline/Swimming Hole tour, both duplicate-URL pairs, `/covid-19-info/`, `/blog/skyline/`, all 3 sitemaps, homepage schema block) run today, 2026-08-16.
- **`lonestarkayaktours.com`, `austinpaddle.com`, `kayakaustintours.com`** — re-crawled directly (headers, redirect behavior, title).
- **PageSpeed Insights API** — direct call (Node/`psi-run.mjs` unavailable in this session's shell — no `node` binary on PATH — so hit the PSI v5 REST endpoint directly instead). Returned HTTP 429, "Quota exceeded for quota metric 'Queries' and limit 'Queries per day'." **Fourth consecutive audit blocked.**
- **WebSearch** — one query to spot-check TripAdvisor listing landscape for AKT/Lone Star Kayak Tours.
- **WebFetch** — attempted against TripAdvisor and Yelp business pages; both returned HTTP 403 (bot-blocked), so the real review counts still could not be pulled from either source this session. Noting the attempt rather than guessing a number.
- **GSC / GA4 / GBP MCP** — `ToolSearch` run against this vault's connected servers found no `gsc_*`, `ga4_*`, or `gbp_*` tools loaded this session. Same as the last three audits. The `.mcp.json` for this vault only declares `google-austin`, `gbp`, `meta-organic`, `playwright`, `opencx`, `clarity` — and per Pass 2's finding, the underlying `google-personal` MCP server code does define `gsc_*`/`ga4_*` tools and a token file exists locally, but the connection isn't live in any of the four sessions run this week. **This is now a 4-for-4 pattern, not a one-off** — worth a direct, non-automated check (restart the MCP server / re-auth) rather than continuing to note it every night.
- **Vault docs** — all three prior audits in full, `SEO Action Plan & Blog Pipeline.md`, `Ranking Baseline 2026-06-07.md`, `AI-SEO-Bat-Tours-Action-Plan.md`, and a fresh listing of `Blog Drafts - Staged/`, `SEO Content/Cluster A - Lady Bird Lake/`, and `SEO Content/Pillars/` to check what's moved since Pass 2.

---

## Executive Summary

Nothing structural shipped to the live site between Pass 2 (2026-08-15 evening) and this session — every Quick Win and every Strategic item from the prior three audits is still open, reconfirmed by direct crawl tonight: FAQ page still has zero `FAQPage` schema, homepage `LocalBusiness` schema still shows `reviewCount: "4"` with no `sameAs` array (even though the real Facebook/Instagram/TripAdvisor/Yelp URLs are sitting in the homepage footer, just not in the JSON-LD), both pillar pages still 404, both duplicate URL pairs still live and self-canonicalizing with **identical titles and identical content** (confirmed this session — these are exact duplicates, not near-duplicates), `lonestarkayaktours.com` still fully live and self-canonicalizing, `/kayak-paddleboard-rental/` still 404, and PSI is blocked for the fourth straight day.

The content pipeline, by contrast, kept moving overnight between sessions: three more staged drafts appeared in `Blog Drafts - Staged/` since Pass 2 — `2026-08-15 - congress-avenue-history-tour-austin.md`, `2026-08-15 - is-austin-kayak-tours-the-same-as-lone-star-kayak-tours.md`, and `2026-08-15 - rainey-street-walking-bar-tour-austin.md`. The second one is worth flagging specifically: it directly answers Pass 2's own "brand-disambiguation content" gap recommendation (the `lonestarkayaktours.com` / `kayakaustintours.com` / `austinpaddle.com` confusion problem). That's good — a draft exists — but it is still unpublished, so the underlying trust/confusion problem it addresses is still live on the internet tonight.

One genuinely new technical finding this pass: the meta description on `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` is 163 characters, over the ~155-160 character point where Google typically truncates in the SERP snippet. None of the three prior audits ran a character-length pass on titles/descriptions, so this is new, not previously caught — see On-Page Issues table below.

`kayakaustintours.com`, the brand-hijack doorway site flagged in Pass 2, is still live and still uses the exact string "Austin Kayak Tours" in its `<title>` tag; the only change is its bare-domain now issues a clean 301 to its `www` version (not a takedown, just normal domain hygiene on the hijacker's side).

**Top 3 priorities by impact, unchanged in substance from Pass 2, restated because nothing has closed them:** (1) the FAQ schema + homepage `sameAs`/review-count fix are both now pure copy-paste jobs with zero research left to do — combined, under 30 minutes of WordPress work, and still sitting open after 3 prior audits flagged them; (2) resolve the 3-domain duplicate-property problem (`lonestarkayaktours.com`, the two exact-duplicate URL pairs, and the still-unresolved `austinpaddle.com` ownership question); (3) publish the two ready pillar pages, which are still targeting 2,799 impressions of unclaimed demand per the (now 10-week-stale) GSC snapshot — this is the one item on the list that needs real GSC data to size accurately, and GSC still isn't connected after 4 audits.

---

## What's still open vs. all three prior audits (explicit reconciliation)

| Item | Status tonight (2026-08-16) |
|---|---|
| FAQPage schema on `/faq/` | **Still open.** Reconfirmed: `FAQPage` string count = 0 in page source; 1 JSON-LD block total (auto-generated, not FAQ). |
| Homepage `LocalBusiness` schema — `sameAs` + review count | **Still open.** `reviewCount: "4"`, `ratingValue: "5"` still live in the `Product`/`Review` JSON-LD block. Confirmed the real `sameAs` URLs are visibly linked in the homepage footer (Facebook, Instagram, TripAdvisor, Yelp — same 4 URLs Pass 2 captured) but still absent from the JSON-LD itself. Zero research left; this is copy-paste. |
| `/kayak-paddleboard-rental/` 404 | **Still open.** Reconfirmed 404 tonight. |
| Two pillar pages not published | **Still open.** Both `/best-places-to-kayak-in-austin/` and `/kayaking-lady-bird-lake/` 404 tonight; neither slug appears anywhere in `page-sitemap.xml` (still 9 URLs) or `post-sitemap.xml` (still 57 URLs). |
| Duplicate URL pairs (`paddleboard-tour`, `corporate-events`) | **Still open — and confirmed exact duplicates tonight, not just "same pattern."** Both pages in each pair return HTTP 200 with byte-identical `<title>` tags and independent self-referencing canonicals. This is as clean-cut a duplicate-content case as SEO audits get. |
| `lonestarkayaktours.com` duplicate domain | **Still open.** Reconfirmed HTTP 200, WP-VIP hosted, own title/meta, `x-cache: STALE` today (still being actively served/cached, not abandoned). |
| `austinpaddle.com` ownership question | **Still open — no new information.** This is a David/Connor question, not something crawlable data can resolve. Flagging again because it gates the single biggest strategic decision on this list (see Pass 2's Executive Summary for the full evidence chain: shared FareHarbor slug, shared WP-VIP host header, identical address, identical tour catalog/pricing). |
| Halloween / All Day Skyline-Swimming Hole — schema + linking gap | **Still open**, not re-crawled at the schema level tonight (confirmed twice already, no reason to expect it changed given nothing else shipped). Both remain unlinked from the homepage nav (confirmed tonight via full href extraction — neither URL appears anywhere in the homepage's 51 total href attributes). |
| `/austin-walking-tours/`, `/rainey-street-walking-bar-tour/` — `Product` schema gap | **Still open**, not re-crawled tonight, no reason to expect movement. |
| Two missing internal links to `/corporate-events/` | **Still open.** Reconfirmed tonight: `why-team-building-is-great-on-kayaks` and `austin-bachelorette-party-guide` both still have zero mentions of "corporate-events" in their page source. |
| `/covid-19-info/` stale content | **Still open.** Page still returns 200, still indexed. |
| Cluster A (5 posts) + all staged drafts not published | **Still open.** `post-sitemap.xml` reconfirmed at exactly 57 URLs tonight — identical count to all three prior sessions. Zero net publishing this week despite active draft production (see New Findings below). |
| PSI / Core Web Vitals baseline | **Still blocked — fourth consecutive day.** Same daily-quota 429 on the shared keyless project. |
| GSC/GA4/GBP MCP connection | **Still not usable — fourth consecutive session.** See Data Sources note above; this has now outlasted "maybe it's a one-off" and is a standing infrastructure gap. |
| `kayakaustintours.com` brand hijack | **Still live, still using "Austin Kayak Tours" verbatim in its title tag.** Only change: bare domain → `www` now issues a proper 301 (cosmetic, not a resolution). |

---

## New findings this session

1. **Meta description length overrun on `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/`.** 163 characters — Google typically truncates around 155-160 on desktop, meaning the last ~10-15 characters of the current snippet are likely getting cut in the live SERP. None of the prior three audits ran a character-length pass on titles/descriptions; every other page checked tonight (`austin-skyline-tour`, `rental`, `faq`, `halloween-tour`, `austin-walking-tours`, `rainey-street-walking-bar-tour`) came in under the limit (137-158 characters). This is a single-page, low-effort fix.

2. **The two duplicate URL pairs are confirmed exact duplicates, not just "similar."** Byte-identical `<title>` tags on both `/paddleboard-tour/` vs `/austin-kayak-tours/paddleboard-tour/` and `/corporate-events/` vs `/austin-kayak-tours/corporate-events/`. This sharpens prior audits' language from "duplicate URL pattern" to "these are the same page served at two URLs with no redirect" — removes any ambiguity about severity when this gets handed to a dev.

3. **Three more blog drafts staged since Pass 2**, all dated 2026-08-15: `congress-avenue-history-tour-austin.md`, `is-austin-kayak-tours-the-same-as-lone-star-kayak-tours.md`, and `rainey-street-walking-bar-tour-austin.md`. The second is a direct answer to Pass 2's "brand-disambiguation content" gap recommendation — good, but it's a draft, not a live fix, and the confusion it addresses (`lonestarkayaktours.com`, `kayakaustintours.com`, possibly `austinpaddle.com`) is still live tonight. Don't reassign this topic; it's claimed.

4. **`kayakaustintours.com` redirect hygiene changed slightly, substance did not.** The bare (non-www) domain now 301s cleanly to `https://www.kayakaustintours.com/` (1 hop). The site itself is unchanged: still uses "🛶 Austin Kayak Tours | Explore Lady Bird Lake..." verbatim as its `<title>`, still the same brand-hijack doorway site flagged in Pass 2. Not evidence of any enforcement action having landed — just normal domain configuration on the hijacker's end.

5. **TripAdvisor/Yelp review-count verification attempted, not resolved.** Tried to pull the real review count to replace the schema's misleading `reviewCount: "4"` with an actual number, so the eventual fix in WordPress could use a real figure instead of a placeholder. Both TripAdvisor and Yelp blocked the fetch (HTTP 403 — standard bot defense, not a site-specific problem). **Recommend David or Connor grab the real current TripAdvisor and Google review counts directly (logged into each platform) before pasting the schema fix** — don't publish a guessed number just to unblock the fix; an inaccurate `aggregateRating` is worse than a low-but-correct one.

6. **Image alt text: only decorative images are missing alt text, not content images.** Checked the homepage (15 `<img>` tags, 4 missing alt — all 4 are the same repeated "orange-line" decorative divider PNG, not content photos) and the bat tour page (3 `<img>` tags, all have alt text). This is a non-issue; not adding it to the fix list, noting it here so nobody re-checks it as "unverified" next time.

7. **Homepage confirmed to have zero nav links to `/austin-kayak-tours/halloween-tour/`, `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/`, or `/corporate-events/` (either URL variant)** — pulled all 51 raw `href` attributes on the homepage tonight (not just the visible tour grid) to be exhaustive. This confirms, with full link-inventory evidence rather than a spot-check, that these three money pages get zero homepage-level internal linking. Adds precision to a gap already flagged three times.

---

## On-page issues table (new/updated items only — see prior three audits for the full carried-forward list)

| Page | Issue | Severity | Recommended Fix |
|---|---|---|---|
| `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` | Meta description is 163 characters, over the ~155-160 truncation point | Low | Trim to under 155 characters, keep the price/highlight framing that's already there. New finding this session. |
| `/paddleboard-tour/` + `/austin-kayak-tours/paddleboard-tour/` | Confirmed exact duplicates tonight — byte-identical titles, independent canonicals | Critical (severity confirmed, not new) | 301 one to the other. |
| `/corporate-events/` + `/austin-kayak-tours/corporate-events/` | Confirmed exact duplicates tonight — byte-identical titles, independent canonicals | Critical (severity confirmed, not new) | Same fix. |

---

## Technical SEO checklist — delta from prior sessions

| Check | Status | Details |
|---|---|---|
| Core Web Vitals / PageSpeed | **Still blocked, 4th consecutive day** | Direct PSI v5 REST call (not just the local runner script) also returned 429 tonight — confirms this isn't a script/environment issue, it's the shared Google Cloud project's daily quota being exhausted before this audit runs each night. |
| GSC/GA4/GBP MCP | **Still not connected, 4th consecutive session** | See Data Sources note — now a standing pattern worth a direct fix rather than a nightly re-flag. |
| robots.txt / sitemap.xml | **PASS, unchanged** | 57 posts, 9 pages, 13 activities — identical counts to all three prior audits. No AI-crawler blocks. |
| Redirect chains | **PASS, unchanged, plus one new domain checked** | `kayakaustintours.com` bare→www now a clean single 301 (new observation, cosmetic only). AKT's own domain variants unchanged from Pass 2's findings. |
| Broken-link crawl (homepage, full href inventory) | **PASS** | All 51 raw hrefs on the homepage extracted and reviewed tonight (more exhaustive than the "12 same-domain links" spot-check in Pass 2). No new 404s found beyond the already-known `/kayak-paddleboard-rental/`. Confirms the homepage nav gap for Halloween/All-Day/Corporate Events pages (finding #7 above). |

---

## Prioritized Fix List

### Quick Wins (this week, low effort / high leverage)

1. **Paste FAQPage schema onto `/faq/`.** Exact page: `https://www.austinkayaktours.com/faq/`. JSON-LD is already fully drafted in `Marketing/SEO Content/02 - Schema Markup Library.md`. Flagged in all 4 audits, zero research left, still not done. Expected impact: this page's entire content is FAQ pairs with zero structured markup — the single highest schema-ROI item on the site.

2. **Paste the 4 confirmed `sameAs` URLs into the homepage `LocalBusiness` schema, and fix the `reviewCount: "4"` / `ratingValue: "5"` values.** Exact page: `https://www.austinkayaktours.com/`. Exact URLs (reconfirmed live in the homepage footer tonight): `https://www.facebook.com/austinkayaktours/`, `https://www.instagram.com/austinkayaktours`, `https://www.tripadvisor.com/Attraction_Review-g30196-d11876981-Reviews-Austin_Kayak_Tours-Austin_Texas.html`, `https://www.yelp.com/biz/austin-kayak-tours-austin`. For the review count/rating: **get the real current number from TripAdvisor/Google directly** (both platforms block automated scraping, confirmed again tonight) rather than guessing — a wrong number is worse than the current low-but-accurate one. Expected impact: proper entity linking for Knowledge Panel / AI-citation eligibility; stops "4 reviews" from being the trust signal any AI engine or rich-result parser sees today.

3. **Fix the `/austin-kayak-tours/all-day-skyline-and-swimming-hole-tour/` meta description length.** Exact page and exact issue: 163 characters, over the ~155-160 truncation point. New finding this session — trim while keeping the existing price/highlight framing. Expected impact: modest — prevents the snippet from being cut off mid-sentence in the SERP, a CTR nicety, not a ranking fix.

4. **Fix the `/kayak-paddleboard-rental/` 404.** Still open since May. 301 to `/rental/`.

5. **Publish the two ready-to-go pillar pages.** `/best-places-to-kayak-in-austin/` and `/kayaking-lady-bird-lake/` — fully drafted, zero content work left, still 404 after 4 audits.

6. **Add the 2 still-missing internal links to `/corporate-events/`** from `why-team-building-is-great-on-kayaks` and `austin-bachelorette-party-guide` — reconfirmed tonight as the only 2 of the original 7 planned links that never shipped.

### Strategic Work (this quarter, higher effort)

1. **Resolve the 3-domain duplicate-property problem: `lonestarkayaktours.com`, the two exact-duplicate URL pairs, and `austinpaddle.com`.** Exact next step that's genuinely blocking progress: **get a direct yes/no from Connor on whether `austinpaddle.com` is company-owned.** Everything else on this item (301 mapping, canonical consolidation) is a downstream decision that depends on that one answer. This has been flagged for 2 straight audits without that question being asked/answered yet — it's cheap to resolve and gates the highest-impact strategic item on the whole list.

2. **File a spam/trademark report on `kayakaustintours.com`.** Still live, still using the exact brand name in its title tag, confirmed again tonight. This is a business/legal action, not a content edit — the evidence (title tag text, affiliate links, doorway-site network) was fully gathered in Pass 2 and hasn't changed.

3. **Consolidate the duplicate URL pairs.** Now confirmed byte-identical, not just similar — an unambiguous 301 job whenever a dev is available.

4. **Publish Cluster A (5 posts) and the growing staged-drafts backlog.** Now 12 files in `Blog Drafts - Staged/` (9 confirmed in Pass 2, 3 more added since) plus all 5 Cluster A posts and both pillar pages — a meaningful amount of finished, unpublished content. Recommend picking a fixed weekly publishing cadence (even 1/week) rather than letting the draft pile keep growing while the live post-sitemap count sits frozen at 57.

5. **Get GSC/GA4/GBP MCP tools actually loading for this vault.** Four consecutive audits confirm the server code and auth token exist but the tools don't surface via ToolSearch. This is a connection/restart problem, not a from-scratch integration — worth a 10-minute manual check (restart the MCP server, verify the vault's `.mcp.json` entries are being picked up) rather than a fifth night of re-flagging it. Every keyword/impression number in all 4 audits, including the "2,799 impressions" figure justifying the pillar-page push, is still the same 10-week-stale snapshot from the wrong domain's GSC property.

6. **Get a free PSI API key set up (`PSI_KEY` in `~/.claude/.env`).** Four consecutive audits with zero Core Web Vitals data. Cheap, one-time fix that keeps costing a full night's technical-SEO blind spot every day it's skipped.

7. **Everything else carried forward unchanged from Pass 2** — Halloween/All-Day-Skyline schema + linking build-out, `/austin-walking-tours/` and `/rainey-street-walking-bar-tour/` Product schema, `/covid-19-info/` retirement, About/ownership page. Not re-litigated in full here; see Pass 2's Strategic Work section.

---

*Compiled 2026-08-16. REPORT ONLY — no live-site, WordPress, GBP, or ad changes were made in the course of producing this report. This is the fourth consecutive audit finding zero live-site changes shipped; the underlying issues are well-documented and low-effort (several are literal copy-paste jobs) — the gap at this point is execution bandwidth, not information.*
