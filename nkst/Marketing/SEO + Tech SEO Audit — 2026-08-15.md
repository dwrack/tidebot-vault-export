---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: REPORT ONLY — NO CHANGES APPLIED
---

# NKST SEO + Technical SEO Audit — 2026-08-15

> **REPORT ONLY. Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform.** Generated in an unattended run with no interactive approval step. Every recommendation needs David's sign-off before anything gets touched. See "Data Sources & Gaps" for what's live-verified today vs. carried forward.

---

## Data Sources & Gaps (read this first)

**GSC/GA4 MCP: tried again today, still not available.** Per David's instruction, before assuming anything was unavailable I ran `ToolSearch` with `"select:gsc_query,ga4_report"`, `"google search console"`, `"search console query performance"`, `"google-nkst"`, `"analytics report"`, `"nkst analytics report"`, and `"pagespeed insights lighthouse"`. None returned any `gsc_*`, `ga4_*`, or PSI-adjacent MCP tool — only the generic `WebSearch`/`WebFetch` tools loaded, same as everything else in this session. This matches exactly what happened on 2026-08-14: the `google-nkst` MCP is configured in this vault but isn't exposing tools this session. No GBP MCP tools were found either. **No numbers below are invented** — every GSC/GA4/GBP figure is carried forward from the dated source noted, and every item marked "verified live today" was actually checked against production over HTTP just now.

**PageSpeed Insights: tried fresh, still blocked.** Ran `node ~/Projects/tech-seo/psi-run.mjs both` fresh (this run also swept all 8 FareHarbor-theme sites, not just NKST) — every site including NKST returned `HTTP 429 Quota exceeded for quota metric 'Queries' and limit 'Queries per day'`, same failure mode as yesterday. No `PSI_KEY` is on file (`~/.claude/.env` has no PSI entry). Falling back again to the same 2026-06-19 cached run (now 57 days old, not 56) — see §5.

**What today's report is built on:**

| Source | Date | What it gives us |
|---|---|---|
| `Marketing/SEO + Tech SEO Audit — 2026-08-14.md` | 2026-08-14 (yesterday) | Baseline to diff against — what was flagged, what's resolved |
| `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md` | 2026-08-10 | Full GSC query/position/impression data (90d window), DataForSEO volume cross-check, live AI Overview test, schema audit, GBP local-pack snapshot |
| `Marketing/SEO Audit 2026-05-04.md` | 2026-05-04 | Prior GSC pull, baseline internal-linking plan |
| `SEO Content/Content Plan.md` | Drafted 2026-05-06 | The 5-post Week 1 publish plan — used today to verify what actually shipped vs. what's still a plan on paper |
| `Analytics Report — March 2026.md` (referenced, not re-read in full today) | 2026-03-26 | Last real GA4 data — sessions, channel conversion, conversion-tracking gap |
| **Live checks run today, 2026-08-15** | Today | robots.txt, sitemap.xml (all 3 child sitemaps), HTTP status on 45+ URLs, HTML source inspection (title/meta/H1/JSON-LD schema/internal links/word counts) on 15 key pages, fresh PSI attempt (blocked), a live WebSearch pass on 2 money queries as a stand-in AI-answer check |
| `~/Projects/tech-seo/out/psi-20260619.json` | 2026-06-19 (57 days old) | Only available CWV/Lighthouse data point |

**Confirmed data gaps, same shape as yesterday:** no fresh GSC query data (relying on Aug 10 pull); no fresh GA4 session/conversion data (relying on March, now 5+ months old); no live GBP listing/category check (relying on Aug 10 findings, GBP MCP still unavailable); no fresh Core Web Vitals run (57-day-old cache). The WebSearch pass below is **not** a literal reproduction of Google's AI Overview — it's OpenAI-adjacent web search synthesis used as a rough proxy, flagged as such wherever cited.

**What's different about today's methodology vs. 2026-08-14:** rather than re-verifying the same 15 URLs and repeating the finding, I pulled the actual HTML source (not just status codes) on the alligator page, the money page, the homepage, the two duplicate "best swamp tour" posts, and — new this run — all five posts named in the May 6 `Content Plan.md`. That last check surfaced something the Aug 14 audit missed entirely: **three of the five Week 1 content-plan posts are live, indexed, and full-length that nobody had flagged as shipped.** See §Executive Summary and §4.

---

## Executive Summary

The core diagnosis from the last three audits is unchanged and still the right one: NKST has real authority (1,416 reviews at 4.9 stars, a 272k-impression alligator page, now a growing content library) but the money page for the biggest keyword cluster on the site still isn't linked to from anywhere with real traffic, and zero tour pages carry commercial schema. **What's new today:** digging into actual page source instead of just status codes shows the May 6 Content Plan shipped further than either the May or the two August audits gave it credit for. `/blog/manchac-swamp-visitor-guide/`, `/blog/bayou-bienvenue-vanishing-swamp/`, and `/blog/first-time-kayak-swamp-tour-new-orleans/` are all live, full-length (1,800-2,500+ words), and indexed in the sitemap — none of the prior three audits checked these URLs directly, so they've been invisibly "done" for over three months while `/kayak-vs-airboat-swamp-tour/` (which the Aug 14 report still lists as "not found" in its strategic work item #10) actually **does** exist, just at the URL the Content Plan actually specified (`/blog/airboat-vs-kayak-swamp-tour-new-orleans/`, 4,499 words, full FAQPage schema) rather than the URL the audit guessed at. That's a real correction, not just a status update: item #10 from yesterday's list should come off the board as "already built," and the actual gap is that it's an orphan, just like everything else.

That reframes the whole diagnosis slightly: **this is no longer primarily a content-gap problem, it's now almost entirely an internal-linking and schema problem.** The content exists. The alligator page — the site's single highest-authority asset — still links to none of it. Neither does the homepage. Confirmed live today: `/alligators-vs-crocodiles/` links to 6 tour pages (Manchac, both Honey Island URLs, Shell Bank, the plantation tour, and a Manchac category page) but zero of the 6 new/rebuilt content pages (`/tours/swamp/`, the swamp-tours-new-orleans-guide, the airboat-vs-kayak post, the Manchac visitor guide, the Bayou Bienvenue post, the first-timer post). The homepage links to none of them either. Everything else flagged critical on 2026-08-14 — the missing schema on `/tours/swamp/`, the Honey Island archive/real-page collision, the duplicate "best swamp tour" posts, the missing PSI key — is confirmed still open, unchanged, verified again today.

**Top 3 priorities by impact:**
1. Link the alligator page (272k impressions/quarter) and homepage to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, and the newly-confirmed-live `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` — this is now the single highest-leverage fix on the site because the destination content is already built and already good (4,000+ words, FAQ schema) but structurally invisible to both users and Google.
2. Add Product + Offer + AggregateRating + FAQPage schema to the 6 tour pages and homepage — confirmed still zero commercial schema anywhere, unchanged across three audits now.
3. Kill the cannibalization: 301 `/which-is-the-best-swamp-tour-around-new-orleans/` into `/which-swamp-tours-are-the-best/`, and fix the Honey Island URL collision (blog category archive still outranking the real tour page, meta description is still the literal boilerplate string "Click to view honey island swamp tour category posts in Blog | Page 1 of 2," confirmed live today).

---

## 1. Keyword Opportunity Table

Source: GSC 90-day pull from the 2026-08-10 audit (window 2026-05-12 to 2026-08-09). No fresher GSC pull was reachable today (see Data Sources & Gaps). Page/link status re-verified live today.

| Keyword | Position | Volume/mo (corrected) | Tier | Recommended Action | Status Today |
|---|---|---|---|---|---|
| swamp tours new orleans | 15 (homepage ranks) | ~1,100–4,000 | Page 2 hostage — biggest opportunity | Link `/tours/swamp/` from the alligator page + homepage; both confirmed still not linking to it | Unresolved |
| swamp tour new orleans | 21 | ~3,000–10,000 | Page 3 | Same fix, same money page | Unresolved |
| new orleans swamp tours | 7 | ~3,000–5,000 | Striking distance — only page-1 commercial win | Reinforce, don't disturb | Unchanged (good) |
| honey island swamp tour | 22, wrong URL (blog archive) | 9,900 | Page 2 hostage + URL collision | Noindex/301 the archive URL | **Confirmed still unresolved today** — meta still reads the literal boilerplate string |
| airboat tours new orleans | ~11 (May pull; not re-pulled Aug) | ~800-900 | Page 2 hostage / nemesis keyword | **Content now exists** (`/blog/airboat-vs-kayak-swamp-tour-new-orleans/`, confirmed live, 4,499 words, FAQPage schema) — the fix is now purely internal linking, not content creation | **Downgraded from "build the page" to "link the page"** |
| alligator tour new orleans | 51 (not ranking) | 2,900 | New territory | Build `/alligator-tour-new-orleans/` — confirmed still 404 today, no page exists | Unresolved |
| which is more dangerous alligator or crocodile | 6.4 | 10,210 impr/90d (info) | CTR fix — already actioned | Title/meta already rewritten; monitor CTR on next real GSC pull | Can't confirm movement without GSC |
| swamp tours in new orleans | 20, on `/3-free-swamp-walks-.../` | 1,900 | Commercial query landing on a "don't pay us" page | Rewrite to CTA every section to a paid tour | Confirmed page still live unchanged, still 5 links to Manchac tour (unchanged from prior), thesis still "free" |
| best new orleans swamp tours | 24 (`/which-swamp-tours-are-the-best/`); duplicate ~43-51 | 1,600 | Cannibalization | Merge duplicate pages | **Confirmed both still live today**, different H1s, unresolved |
| how much does a swamp tour cost | not ranking for NKST (confirmed via live WebSearch today — NKST absent from the result set entirely) | High commercial PAA intent | Content gap — **partially closed** | Guide page (`/swamp-tours-new-orleans-guide/`) now has a "Cost: what a swamp tour actually costs in 2026" section with real pricing, confirmed live today — but it's not in FAQ schema and the page isn't linked from anywhere with authority, so it isn't surfacing for the query yet | Partially addressed, not yet working |
| swamp tour near me | not in top 100 organically | 12,100 (local-pack query) | Local pack, not organic | GBP category fix, not a content play | No new data (GBP MCP unavailable) |
| kayak swamp tour | 1 | 880 | Owned | No action | Unchanged |

---

## 2. On-Page SEO Issues — Verified Live Today (2026-08-15)

| Page | Issue | Severity | Status vs. 2026-08-14 |
|---|---|---|---|
| `/tours/swamp/` | Confirmed today: `BreadcrumbList`/`ListItem` schema only. Word count ~3,100 (this is higher than the 1,176 cited in the Aug 10 audit — the page has been expanded since, just not schema'd or linked). No Product, Offer, AggregateRating, or FAQPage. | Critical | **Content grew, schema gap unchanged** |
| `/` (homepage) | Confirmed today: Organization, LocalBusiness, WebSite, VideoObject, PostalAddress, ContactPoint, GeoCoordinates, SearchAction, ImageObject, WebPage present. No AggregateRating, no FAQPage. Title/meta unchanged from prior audits ("New Orleans Kayak Swamp Tours | Save Our Wetlands"). No links to `/tours/swamp/` or any of the 6 target content pages found in homepage nav/body links crawled today. | High | Unchanged |
| `/alligators-vs-crocodiles/` | Confirmed today: title/meta rewrite from the Aug 14 window is still live ("Alligator vs Crocodile: Which Is More Dangerous?"). **Correction to the Aug 14 finding of "0 links found":** the page actually links to 6 tour pages (Manchac Mystic, both Honey Island URLs, Shell Bank, the plantation tour, a Manchac category page) — it is not a total orphan-maker. But it links to **zero** of the specific pages the plan calls for: not `/tours/swamp/`, not `/swamp-tours-new-orleans-guide/`, not the airboat-vs-kayak post. Still no FAQPage schema despite Q&A content. Word count ~3,200. | Critical (linking to money/pillar pages), Medium (schema) | **Refined finding** — partial linking exists, but not to the pages that matter most |
| `/tours/kayak-tours/honey-island-swamp-tour/` | Confirmed live today: meta description is still literally `"Click to view honey island swamp tour category posts in Blog | Page 1 of 2"`, zero schema of any kind. Real tour page (`/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`) confirmed live, 3,658 words, has VideoObject/Organization/BreadcrumbList/ImageObject — still no Product/Offer/AggregateRating either. | Critical | Unchanged |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Confirmed both live today. H1s: "New Orleans swamp tour reviews" vs "What is the best Swamp Tour near New Orleans?" (page 2's live H1 differs slightly from titles cited in prior audits — title tag itself now reads "What is the best eco-friendly Swamp Tour in New Orleans?", H1 hasn't been updated to match). Same query intent, two live pages. | High | Unchanged |
| `/3-free-swamp-walks-in-and-around-new-orleans/` | Confirmed live today, unchanged. Links to the Manchac tour page 5 times (up from the "2 links, none above the fold" cited on Aug 14 — worth a recheck of exactly where those links sit, but there are more of them now). Thesis is still "see it free." | High | Link count improved slightly; thesis rewrite still not done |
| `/swamp-tours-new-orleans-guide/` (Content Plan Post 1) | **New finding today.** Confirmed live, 4,644 words, FAQPage + BreadcrumbList schema present (4 questions: best swamp tour, Manchac vs Honey Island, alligators on tour, experience needed — cost question is answered in body but not in the FAQ schema block). Links out to the airboat-vs-kayak post, Honey Island pages, and the Manchac tour page. **Not linked in from the homepage or the alligator page** — an orphan pillar page despite being fully built. | High (linking) | Not assessed in any prior audit's page-by-page section — flagged here for the first time |
| `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` (Content Plan Post 2) | **New finding today — corrects the Aug 14 report.** Confirmed live, 4,499 words, FAQPage + BreadcrumbList schema. The Aug 14 audit's strategic item #10 ("New page: `/kayak-vs-airboat-swamp-tour/`... recommended in May, still missing") is **wrong** — the page exists, just at the slug the Content Plan actually specified. It is not linked from the alligator page, the homepage, or `/3-free-swamp-walks/`. | High (linking) | Corrects a false negative in the prior audit |
| `/blog/manchac-swamp-visitor-guide/` and `/manchac-swamp-visitor-guide/` (Content Plan Post 3) | **New finding today.** Both URL variants (with/without `/blog/` prefix) return 200 with identical content — confirm which is canonical before building more links to avoid a soft duplicate. Live, matches the Content Plan's title exactly. | Medium (canonicalization), Low otherwise | Not assessed in any prior audit |
| `/bayou-bienvenue-vanishing-swamp/` (Content Plan Post 4) | **New finding today.** Live, matches Content Plan title exactly. Same dual-URL pattern as Post 3. | Medium (canonicalization) | Not assessed in any prior audit |
| `/first-time-kayak-swamp-tour-new-orleans/` (Content Plan Post 5) | **New finding today.** Live, matches Content Plan title exactly. Same dual-URL pattern. | Medium (canonicalization) | Not assessed in any prior audit |
| `/tours/` | Meta description confirmed live today, same as Aug 14 finding — not truncated, low-priority polish only. | Low | Unchanged |

---

## 3. Internal Linking Opportunities (Updated Priority Order)

The picture changed today: this is no longer "some content doesn't exist yet," it's "the site's two highest-authority pages (alligator post, homepage) don't link to any of its 4-5 best commercial/pillar assets, all of which are already built."

| # | Source Page | Target | Suggested Anchor | Priority | Verified Status Today |
|---|---|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | `/tours/swamp/` | "swamp tours in New Orleans" | Critical | Confirmed missing |
| 2 | `/alligators-vs-crocodiles/` | `/swamp-tours-new-orleans-guide/` | "our full New Orleans swamp tour guide" | Critical | Confirmed missing |
| 3 | `/alligators-vs-crocodiles/` | `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` | "kayak vs. airboat, an honest comparison" | High | Confirmed missing — this content already exists and is good, this is a pure link-add |
| 4 | `/` (homepage) | `/tours/swamp/` | "swamp tours" (nav or hero CTA) | Critical | Confirmed missing |
| 5 | `/` (homepage) | `/swamp-tours-new-orleans-guide/` | "how to pick a swamp tour" | High | Confirmed missing |
| 6 | `/swamp-tours-new-orleans-guide/` (already a well-built pillar page) | `/tours/swamp/` | "book a swamp tour" | High | Confirmed missing — the guide currently links to 3 individual tour products but not the general money page |
| 7 | `/3-free-swamp-walks-in-and-around-new-orleans/` | `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` | "how a guided tour compares" | Medium | Not present |
| 8 | `/tours/kayak-tours/honey-island-swamp-tour/` (archive) | `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (real page) | "Honey Island kayak swamp tour" | Critical | Confirmed both still live and split today — really a redirect/consolidation, not a link add |
| 9 | `/manchac-swamp-visitor-guide/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "book the Manchac tour" | Medium | Not checked in detail today, worth a follow-up crawl once canonicalized (see §2) |
| 10 | `/julie-white/` | `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | "book a tour with one of our guides" | Medium | Page confirmed live (200), link not re-verified today |

**Orphan pages, updated:** `/swamp-tours-new-orleans-guide/` and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` should be added to the orphan list — both are substantial (4,000+ word), schema-complete pages with effectively zero authoritative inbound links. That's arguably a worse waste than a thin page being orphaned, because real writing effort already went in.

---

## 4. Content Gap Analysis — Revised

**The gap list from the 2026-08-14 and 2026-08-10 audits needs a correction, not just an update.**

| Item flagged as a gap (prior audits) | Status confirmed today |
|---|---|
| Kayak vs. airboat comparison — "recommended in both May and August audits" | **Not a gap. Built.** Live at `/blog/airboat-vs-kayak-swamp-tour-new-orleans/`, 4,499 words, FAQ schema. The real remaining task is linking it, not writing it. |
| "How much does a swamp tour cost?" page | **Partially closed.** A cost section exists inside `/swamp-tours-new-orleans-guide/` with real 2026 pricing language. Not yet in FAQ schema, not yet linked from anywhere with authority, and confirmed via live WebSearch today that NKST does not appear anywhere in the result set for "how much does a swamp tour cost New Orleans" — competitors (Cajun Pride, NOLA Adventures, Gators and Ghosts) currently own that query. Building a truly standalone page is now lower priority than fixing the linking/schema on the guide page that already answers it. |
| Manchac haunted-swamp cluster (Julia Brown legend, night tours) | **Still a real gap.** The new Manchac page (`/manchac-swamp-visitor-guide/`) covers "history, ecology, ghost stories" per its own Content Plan brief, so it may already touch some of this — worth a direct read-through before greenlighting new haunted-swamp content, to avoid duplicating what Post 3 already covers. Flagging as "verify before building," not "still fully open." |
| Practical-anxiety cluster (what to wear, kids, first-timer nerves) | **Mostly closed.** `/first-time-kayak-swamp-tour-new-orleans/` is live and matches this brief closely (Content Plan hook: "Most of our guests have never been in a kayak before"). Confirm its content actually covers wear/kids/bugs before assuming full coverage, but this is very likely done or close to done. |
| Bachelor/bachelorette content rebuild | Confirmed page still live at `/top-destinations-for-your-bachelor-bachelorette-party/`, not rebuilt. Still open, not reassessed in depth today. |
| Wild Louisiana Tours beating NKST in AI-style answers | **Directionally still true but the gap narrowed.** A live WebSearch today (not a literal Google AI Overview, flagged as a proxy) for "best swamp tour New Orleans kayak eco tour 2026" returned NKST in the second slot with genuinely specific copy — "beginner-friendly, guided kayak tours year-round with 2-3 hour tours daily... Locations include Manchac Swamp, the Pearl River, Honey Island Swamp and Cane Bayou" — which is a real improvement over the "eco-philosophy" framing quoted in the Aug 10 report. Worth treating as encouraging but unconfirmed without a true GSC/AI Overview re-test. |

**Genuinely still-open, not addressed by any of the above:**
- Canonicalization of the 3 new posts' dual URLs (`/blog/x/` vs `/x/`) — pick one, 301 the other, update the sitemap and all internal links to match. This wasn't on anyone's radar before today because nobody had checked these URLs.
- Crescent City Kayak's fate — still open across four audits now (May, Aug 10, Aug 14, today). Confirmed the property is still live and resolving today (`crescentcitykayak.com` → 200, no redirect).
- GBP category/duplicate-listing cleanup — no new data, GBP MCP still unreachable.

---

## 5. Technical SEO Checklist — Verified Live Today (2026-08-15)

| Check | Status | Details |
|---|---|---|
| Homepage redirect chain | Pass | 200, 0 redirects, 0.33s response — faster than the 0.87s cited yesterday, within normal variance |
| robots.txt | Pass | Identical to yesterday's findings — sitemap referenced correctly, admin/CDN paths blocked, scraper-bot blanket disallows intentional |
| sitemap.xml | Pass | Sitemap index → 3 child sitemaps (page, activity, post). Post-sitemap confirmed to contain all 5 Content Plan Week 1 slugs today (`swamp-tours-new-orleans-guide`, `airboat-vs-kayak-swamp-tour-new-orleans`, `manchac-swamp-visitor-guide`, `bayou-bienvenue-vanishing-swamp`, `first-time-kayak-swamp-tour-new-orleans` all present, 1 match each) |
| Broken-link crawl (45+ URLs checked today: all prior-audit URLs + all 5 Content Plan slugs + `/how-much-does-a-swamp-tour-cost/`) | Pass, 1 real 404 found | `/how-much-does-a-swamp-tour-cost/` and `/alligator-tour-new-orleans/` and `/kayak-vs-airboat-swamp-tour/` all 404 — but these are pages that were never built at those exact URLs (the airboat content exists at a different slug, see §2/§4), not broken outbound links from the live site. No actual broken internal links found. |
| Duplicate content / cannibalization | Fail | Two live pages still target "best swamp tour." Unchanged. |
| URL collision (archive vs. real page) | Fail | Honey Island archive still outranks the real tour page, boilerplate meta confirmed unchanged. |
| **New: dual-URL duplication on 3 recent posts** | **Fail (new finding)** | `/blog/manchac-swamp-visitor-guide/` and `/manchac-swamp-visitor-guide/` both return 200 with identical content; same for the Bayou Bienvenue and first-timer posts. Not flagged in any prior audit. Low urgency (Google usually picks one canonical) but worth a rel=canonical check or a 301 to consolidate signal. |
| Schema markup — homepage | Partial | Unchanged: Organization, LocalBusiness, WebSite, VideoObject present; AggregateRating, FAQPage missing |
| Schema markup — `/tours/swamp/` | Fail | BreadcrumbList only, unchanged |
| Schema markup — tour product pages | Fail | No Product/Offer/AggregateRating on any tour page checked (Manchac, both Honey Island URLs) |
| Schema markup — `/alligators-vs-crocodiles/` | Partial | Article, BreadcrumbList, Organization, ImageObject present; no FAQPage, unchanged |
| Schema markup — the 3 newly-confirmed content posts | **Good** | `/swamp-tours-new-orleans-guide/` and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` both carry full FAQPage + BreadcrumbList schema — these are the best-schema'd pages on the entire site, and they're the ones with the fewest inbound links. |
| HTTPS | Pass | Confirmed |
| Core Web Vitals / Lighthouse | **Still stale** | Fresh PSI attempt today returned `HTTP 429` quota exceeded, identical failure to yesterday. Last successful run: 2026-06-19, now 57 days old. No `PSI_KEY` on file. |
| GSC index status | Not available | GSC MCP not connected this session, confirmed via ToolSearch (see Data Sources & Gaps) |

### Core Web Vitals (still 2026-06-19, now 57 days old — unchanged data, treat as directional only)

| Strategy | Perf Score | LCP (lab) | CLS (lab) | TBT (lab) | Field data (CrUX: LCP/CLS/INP) |
|---|---|---|---|---|---|
| Mobile | 37 (red) | 16.2s (very poor) | 0.005 (good) | 1,600ms (poor) | FAST / FAST / FAST |
| Desktop | 54 (amber) | 2.5s (good) | 0.009 (good) | 620ms (needs improvement) | FAST / FAST / FAST |

Same caveat as yesterday: the field data (real users) disagrees sharply with the lab score. Don't act on the mobile-37 number until a fresh PSI run is possible — this is now two audits in a row citing the same stale data point. **Getting a `PSI_KEY` is now the single most overdue infrastructure fix in this whole audit chain** — two consecutive unattended runs have been blocked by the same quota wall with a trivial, well-understood fix (a free Google Cloud Console API key).

---

## 6. Local Search / GBP

No new data — GBP MCP unavailable again today, same as yesterday. Carried forward from the 2026-08-10 audit without re-verification: primary category mismatch ("Canoe & kayak tour agency" vs. pack winners' "Boat tour agency"/"Tour operator"), and 5 David-controlled listings clustering within a few blocks (including one at a fabricated "Swamp Tour Street" address — a standalone suspension risk). This needs a live GBP check before acting; it's now been carried forward, unverified, across three consecutive audits.

---

## 7. Competitor Comparison

| Dimension | NKST | Wild Louisiana Tours | Cajun Encounters / other airboat operators | Winner |
|---|---|---|---|---|
| GBP reviews / rating | 1,416 / 4.9 (Aug 10 data, not re-verified) | Not directly comparable | 12,000 / 4.9 | Cajun Encounters on volume |
| AI-answer-style commercial presence (live WebSearch today, "best swamp tour New Orleans kayak eco tour 2026") | Named #2 in the synthesized answer with specific copy — a real improvement over the Aug 10 test | Named #1 (Manchac Magic) | Not tested this pass | Wild Louisiana still first, gap narrowed |
| "How much does it cost" query ownership | **Absent entirely** from today's live WebSearch result set | Not tested directly | Cajun Pride, NOLA Adventures, Gators and Ghosts, airboatadventures.com all present | Airboat operators — NKST's own cost content isn't ranking/citing yet |
| Structured data (Product/Offer/Rating) on tour pages | Still none, confirmed today | GetYourGuide listing carries verified reviews | Not tested this pass | Wild Louisiana (via 3rd-party listing) |
| Content depth on comparison/first-timer topics | Now strong — 3 new 4,000+ word posts confirmed live today, just unlinked | Explicitly avoids folklore/haunted content per their own copy | Not tested this pass | NKST now has the content advantage, needs the linking to cash it in |

---

## 8. Traffic & Conversion Context (GA4, March 2026 — carried forward, 5+ months old)

No fresher GA4 pull was reachable today. Same figures as the 2026-08-14 report, restated for completeness, not re-verified:

- 11,848 sessions / 90d, +44% sessions and +59% conversions month-over-month at the time (spring seasonal ramp).
- Paid Search converted at 19.8% vs. 13.0% organic, 8.7% direct.
- Paid Social converted at 0.8% — flagged as essentially wasted spend at the time.
- Conversion tracking gap: only 58 `ads_conversion_Purchase_1` events tracked in 90 days against 23,385 GHL contacts — FareHarbor booking confirmations were not firing a GA4 purchase event as of March.

**Still open across two audits now: confirm whether the FareHarbor → GA4 purchase event was ever fixed.** This affects every conversion-rate figure in NKST's marketing stack, not just SEO, and it's now been flagged without resolution for over a week of unattended runs.

---

## 9. Prioritized Fix List

### Quick Wins (this week — all under a few hours each)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | `/alligators-vs-crocodiles/` | Add a "More reading" internal-link block linking to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/`. All three destination pages are confirmed live and substantial today — this is a pure linking fix, no content work required. | Redirects a slice of the 272k quarterly impressions toward 3 pages that are already built and already good but currently invisible from the site's highest-authority asset. |
| 2 | `/` (homepage) | Add hero/nav links to `/tours/swamp/` and `/swamp-tours-new-orleans-guide/`. Confirmed today: neither is linked from the homepage. | The homepage is what currently ranks (position 15-21) for the biggest keyword cluster on the site — pointing it at the real money page is the single fastest lever to test whether Google starts preferring `/tours/swamp/` instead. |
| 3 | `/swamp-tours-new-orleans-guide/` | Add a link to `/tours/swamp/` (the general booking money page) — currently the guide links to 3 individual tour products but not the money page itself. Also add the cost question ("How much does a swamp tour cost?") into the existing FAQPage schema block — the body copy already answers it, just not machine-readably. | Closes the gap on the highest commercial-intent PAA question identified in the Aug 10 audit, using content that already exists. |
| 4 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 (or noindex, if 301 isn't feasible via the CMS) to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. | Stops a boilerplate blog-archive page (meta description literally reads "Click to view honey island swamp tour category posts in Blog | Page 1 of 2," confirmed live today) from being Google's answer for a 9,900/mo keyword. |
| 5 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/`, merging any unique content first. | Ends self-cannibalization; the survivor page has a real shot once it's not splitting signal with itself. |
| 6 | `/manchac-swamp-visitor-guide/`, `/bayou-bienvenue-vanishing-swamp/`, `/first-time-kayak-swamp-tour-new-orleans/` (plus their `/blog/`-prefixed duplicates) | Pick one canonical URL per post (recommend dropping the `/blog/` prefix to match the other two Content Plan posts already live at root), add `rel="canonical"` or 301 the non-canonical version, update the sitemap. | New finding today — these 3 posts are splitting their own signal across two URLs each, undermining the SEO value of content that's otherwise well-built. |
| 7 | `~/Projects/tech-seo/psi-run.mjs` environment | Get a free PageSpeed Insights API key, add to `~/.claude/.env` as `PSI_KEY=...`. This has now failed identically two audits in a row. | Unblocks a real, current Core Web Vitals read — the mobile score 37 finding is now 57 days stale. |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 8 | `/tours/swamp/` | Add Product + Offer (price/currency/availability) + AggregateRating (4.9/1,416) + FAQPage schema. Content itself is already at ~3,100 words (grown since the 1,176 cited in May) — this is now a schema/linking task, not a rewrite task. | Single biggest lever identified across four audit passes now. The content gap on this page has mostly closed itself; the schema and linking gaps haven't. |
| 9 | `/`, all 6 tour pages | Add AggregateRating + Product/Offer schema sitewide, using pricing already published in page bodies. | Star ratings + price display in search results, AI-answer extractability. Confirmed still zero commercial schema anywhere on the site across four audits. |
| 10 | New page: `/alligator-tour-new-orleans/` | Still genuinely missing — confirmed 404 today, unlike the airboat-vs-kayak page which turned out to already exist. Build a dedicated commercial page targeting "alligator tour new orleans"/"gator tour new orleans" (2,900/mo combined). | Bridges NKST's AI-Overview alligator authority to an actual bookable page. |
| 11 | Manchac haunted-swamp content | **Before building new pages, read `/manchac-swamp-visitor-guide/` in full** — its own brief says it covers "history, ecology, ghost stories," which may already partially close this gap flagged as "highest-leverage" in the Aug 10/14 audits. Scope any new content to what's actually missing after that read. | Avoids duplicating effort on content that may already be 60-80% built. |
| 12 | Practical-anxiety cluster (what to wear, kids, mosquitoes) | **Before building new pages, read `/first-time-kayak-swamp-tour-new-orleans/` in full** — likely already covers most of this per its Content Plan brief. | Same reasoning as #11 — verify before commissioning duplicate work. |
| 13 | GetYourGuide / TripAdvisor / Viator listings | Rewrite third-party OTA listing copy to lead with extractable specifics (duration, transport, species list, group size, difficulty). | This is the layer AI answer engines source from; site-level fixes won't fully close the gap without this. |
| 14 | GBP: primary category + duplicate-listing cleanup | Needs a live GBP check (still not possible — MCP unreachable 3 audits running). Category mismatch and the "Swamp Tour Street" fabricated-address listing are both carried forward unverified. | Local pack eligibility for "swamp tour near me" (12,100/mo). |
| 15 | Crescent City Kayak property decision | Still open across four audits now. Confirmed live and resolving today, unchanged. Either 301 into NKST or commit to a genuine funnel rebuild. | Every quarter this stays undecided, CCK keeps splitting authority NKST already wins head-to-head. |
| 16 | Bachelor/bachelorette content rebuild | Confirmed still live, unrebuilt, at `/top-destinations-for-your-bachelor-bachelorette-party/`. | Real search demand, both NKST and competitor versions confirmed weak per the May audit. |

---

## Notes

- All URLs, HTTP status codes, schema types, word counts, and title/meta strings marked "confirmed live today" or "verified today" were checked directly against production source (not just status codes — actual HTML/JSON-LD inspection) on 2026-08-15.
- The single most important thing this run found that the last two audits missed: **three fully-built, schema-complete, 4,000+ word blog posts have been live and indexed since May with almost no inbound linking, and one of them was incorrectly listed as "not built" in yesterday's report.** This happened because prior audits checked whether pages existed at the URLs they assumed, not the URLs the Content Plan actually used. Worth a standing reminder for future runs: verify against the sitemap directly, not against assumed slugs.
- Numbers not re-pulled this session (GSC positions/impressions, GA4 sessions/conversions, GBP category/listing status, Core Web Vitals) are dated to their source above; none were guessed or extrapolated. The WebSearch-based "AI answer" checks in §4/§7 are explicitly flagged as a rough proxy for a true Google AI Overview test, not a literal reproduction.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, and no ad platform was touched in the production of this report. Every action item above is a recommendation awaiting approval.
