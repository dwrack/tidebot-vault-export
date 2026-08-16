---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-16
status: DRAFT — PENDING DAVID APPROVAL — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech-SEO Audit — 2026-08-16

> **DRAFT. REPORT ONLY.** Nothing in this document has touched the live site, WordPress, GBP, or any ad platform. Every recommendation below needs David's sign-off before anything is built or published.

## Before you read this: this is the 9th SEO/tech-SEO pass on this vault in two days

`Marketing/2026-08-15 SEO + Tech SEO Audit — pass7 (final, stop here).md` (yesterday, 18:34) explicitly recommended holding further passes until one of two things changed: MCP/PSI access got unblocked, or the staged-drafts backlog got reviewed. As of this morning, **neither has fully happened** — MCP tools still aren't registering this session and PSI is still unreachable (different technical reason this time, see below) — but the drafts backlog **did** partially move: two of the five Content Plan posts went live overnight/yesterday evening, which created a real, new, previously-only-predicted problem (see Quick Win #1). That's a genuine delta, not a re-derivation, so this pass exists to capture it and re-confirm the rest rather than re-crawl from zero. Everything not explicitly re-verified below is carried forward from pass 7 and dated accordingly.

**What's actually new since pass 7 (18:34 yesterday):**
1. `/airboat-vs-kayak-swamp-tour-new-orleans/` and `/first-time-kayak-swamp-tour-new-orleans/` are now **live** (both return 200 at both the root URL and the `/blog/`-prefixed URL, each self-canonicalizing) — Content Plan Posts 2 and 5 got published. This is progress, but it immediately triggered the exact duplicate-canonical problem pass 7 flagged as a risk in Quick Win #8, now real instead of hypothetical for these two.
2. `Marketing/Blog Drafts - Staged/` is at **43 files**, up from 34 at pass 7 and 14 at the start of yesterday. Growth continued after pass 7 ran (dated files go up to 2026-08-15, none dated 2026-08-16 yet).
3. Confirmed live today: `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` (a real booking page) carries **zero** Product/Offer/AggregateRating schema — only BreadcrumbList, ImageObject, ListItem, Organization, VideoObject. This directly confirms Strategic Item #2 below with a fresh, specific example rather than a general claim.
4. `/alligators-vs-crocodiles/` still has **zero** of the three "More reading" links spec'd back in the May content plan and re-flagged in every pass since (`/blog/manchac-swamp-visitor-guide/`, `/blog/swamp-tours-new-orleans-guide/`, `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` — checked live via curl just now, none present). It does link to `/tours/swamp-kayak-tours/*` 8 times (in the same range as pass 7's count of 9).
5. Homepage nav link to `/new-orleans-zipline-tour-kayak-tour-combo/` still 301s straight back to `/` — unchanged, dead end confirmed live.
6. `/tours/kayak-tours/honey-island-swamp-tour/` still serves the literal boilerplate meta description "Click to view honey island swamp tour category posts in Blog | Page 1 of 2" — unchanged.
7. `/which-swamp-tours-are-the-best/` and `/which-is-the-best-swamp-tour-around-new-orleans/` both still live at 200 — cannibalization unresolved.
8. `/alligator-tour-new-orleans/` and `/how-much-does-a-swamp-tour-cost-new-orleans/` (both checked at root and `/blog/`) are still 404 — the corresponding staged drafts have not been published.
9. `robots.txt` and `sitemap.xml` both healthy (200), unchanged from pass 7.

---

## Data availability — read this before trusting any number below

**GSC, GA4, and GBP MCP tools were not reachable this session.** `ToolSearch` for `gsc_*`, `ga4_*`, `gbp_*` returned nothing; `.mcp.json` lists `google-nkst` and `gbp` servers with token files present at `~/.config/google/tokens/nolakayaktours-at-gmail-com.json`, but neither registered tools this session — same session-level MCP-approval gap diagnosed in pass 5 yesterday, unresolved today. **PageSpeed Insights was also unreachable this session, for a new reason**: the keyless PSI runner at `~/Projects/tech-seo/psi-run.mjs` requires `node`, which is not on PATH in this sandboxed session (`command not found: node`) — a different failure mode than yesterday's HTTP 429 quota exhaustion, same practical result. No live Core Web Vitals could be pulled.

Every ranking, impression, traffic, or Core Web Vitals figure below is **carried forward from a dated source**, clearly labeled, not invented:

- **GSC keyword/position data (Content Plan cluster):** `SEO Content/Content Plan.md`, GSC 90-day pull as of 2026-05-06 (~3.3 months old).
- **GSC + DataForSEO rank data (money-keyword deep dive):** `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`, GSC window 2026-05-12 to 2026-08-09, DataForSEO rank pull Aug 2026 (~6 days old, the freshest dataset in the vault).
- **GA4 traffic/conversion data:** March 2026 pull — 11,848 sessions/90d, Paid Search converting 19.8% vs. Organic 13.0% vs. Paid Social 0.8%; FareHarbor→GA4 purchase-event gap unresolved (58 tracked events vs. 23,385 GHL contacts same window).
- **Core Web Vitals / Lighthouse:** cached PSI run `~/Projects/tech-seo/out/psi-20260619.json`, dated 2026-06-19 — now **58 days old**. Mobile perf score 37/100, mobile lab LCP 16.2s (poor), desktop perf 54/100, desktop lab LCP 2.5s. Field/CrUX data (real users, not lab) shows LCP/CLS/INP all "FAST" — the gap between a poor lab score and a fast field score usually means the lab test is hitting a slow first-load path (large hero image / render-blocking JS) that repeat visitors and CDN caching mask in the field.
- **Live/current data (this pass):** page existence, HTTP status, HTML source, schema markup, internal link presence, meta tags, robots.txt/sitemap — fetched directly from production via curl just now, timestamped to this pass.
- **AI Overview / competitor SERP checks:** `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`, 2026-08-10 — 6 days old, not re-tested live this pass.

---

## Keyword Opportunity Table

Carried forward, deduplicated across the two source docs. Position/volume figures are dated as marked; nothing here is a fresh GSC pull.

| Keyword | Position | Volume/Impressions | Tier | Source/Date | Recommended Action |
|---|---|---|---|---|---|
| swamp tours new orleans | 15 | ~1,100–4,000/mo (corrected from Google Ads' 14,800 mirage figure) | Page 2 Hostage | DataForSEO, 8/10 | Build real money page at `/tours/swamp/`, see Strategic #1 |
| swamp tour new orleans | 21 | ~3,000–10,000/mo | New Territory | DataForSEO, 8/10 | Same page, secondary target |
| new orleans swamp tour | 9 | ~3,000–5,000/mo | Striking Distance | DataForSEO, 8/10 | On-page depth + schema on `/tours/swamp/` |
| new orleans swamp tours | 7 | 5,400/mo (Google Ads, directionally trustworthy here) | CTR Fix | DataForSEO, 8/10 | Only confirmed page-1 commercial win — protect it, add schema for rich results |
| honey island swamp tour | 22 (on a blog archive page, not a tour page) | 9,900/mo | Page 2 Hostage | DataForSEO, 8/10 | 301 the archive into the real tour page, see Quick Win below |
| alligator tour new orleans | 51 (not ranking) | 2,900/mo | New Territory | DataForSEO, 8/10 | No page exists — staged draft not yet published (still 404 today) |
| louisiana swamp tour | not in top 100 | 51–337/mo (corrected — the 4,400 Google Ads figure is a mirage) | Withdrawn | DataForSEO, 8/10 | Do not build a page for this — confirmed low-value |
| swamp tour near me | not in top 100 | Unreliable series (Google Ads carries a spike artifact) | Local pack only | DataForSEO, 8/10 | GBP category fix, not a content play — blocked on MCP access |
| kayak swamp tour | 1 | 880/mo | Owned | DataForSEO, 8/10 | No action — already #1, low volume |
| "swamp tours new orleans" cluster (5 close variants) | 11–15 | ~4,700/mo combined | Page 2 Hostage | Content Plan, GSC 5/6 | Same as `/tours/swamp/` money-page fix above |
| airboat tours new orleans | 11.1 | 828 imp/90d | Striking Distance | Content Plan, GSC 5/6 | Feeds now-live `/airboat-vs-kayak-swamp-tour-new-orleans/` — see canonical fix, Quick Win #1 |
| how much does a swamp tour cost | not ranking, PAA gap confirmed absent | — | New Territory | SEO-AEO-GEO 8/10 | Staged draft exists, content-gate 90/100 per pass 7 — still unpublished |

---

## On-Page Issues Table

| Page | Issue | Severity | Recommended Fix | Verified |
|---|---|---|---|---|
| `/airboat-vs-kayak-swamp-tour-new-orleans/` + `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` | Both live, both self-canonicalize, no consolidation | High | Pick root URL as canonical (matches sitemap convention elsewhere), 301 the `/blog/` variant or fix its `<link rel="canonical">` | Live curl, today |
| `/first-time-kayak-swamp-tour-new-orleans/` + `/blog/first-time-kayak-swamp-tour-new-orleans/` | Same duplicate-canonical pattern | High | Same fix | Live curl, today |
| `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` | Zero Product/Offer/AggregateRating schema on a real booking page | High | Add Product + Offer (price/availability) + AggregateRating using FareHarbor pricing + real review count (source from FareHarbor/GBP, don't fabricate) | Live curl, today |
| `/alligators-vs-crocodiles/` | No FAQPage schema; no "More reading" links to blog content (0 of 3 spec'd links present) | Critical | Add FAQPage JSON-LD around existing Q&A; add the 3-link "More reading" block already written in `SEO Content/Internal Linking Audit.md` lines 17-26 | Live curl, today |
| `/tours/kayak-tours/honey-island-swamp-tour/` | Boilerplate archive meta description, zero schema, ranks #22 for 9,900/mo term | High | 301 into `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` | Live curl, today |
| `/` main nav | `/new-orleans-zipline-tour-kayak-tour-combo/` link 301s to `/` — dead end on every page | Medium | Remove or rebuild the destination page | Live curl, today |
| `/which-swamp-tours-are-the-best/` vs `/which-is-the-best-swamp-tour-around-new-orleans/` | Duplicate intent, both under-ranking (#24/#30 and #43/#51 per DataForSEO 8/10) | High | Merge unique content, 301 weaker page into stronger | Live curl, today |
| `/tours/swamp/` | Best title/H1 on the site but only BreadcrumbList schema, 1,176 words, not linked from `/alligators-vs-crocodiles/` | Critical | See Strategic #1 | SEO-AEO-GEO audit, 8/10 |
| `/alligator-tour-new-orleans/` | Confirmed 404 today, indexed intent with no page | Medium | Publish the staged draft (commercial-intent version, not the informational alligators-vs-crocodiles angle) | Live curl, today |

---

## Internal Linking Opportunities (top 3, from `SEO Content/Internal Linking Audit.md`, drafted 2026-05-07, still unimplemented)

| Target Keyword | Money Page | Source Page | Suggested Anchor | Priority |
|---|---|---|---|---|
| manchac swamp tour | `/blog/manchac-swamp-visitor-guide/` | `/alligators-vs-crocodiles/` (308,394 imp/90d) | "A complete guide to Manchac, the second largest cypress swamp in the US" | High — zero cost, HTML pre-written, still not added after 3 months |
| swamp tours new orleans | `/blog/swamp-tours-new-orleans-guide/` | `/alligators-vs-crocodiles/` | "How to pick a swamp tour near New Orleans" | High — same block, same page |
| airboat vs kayak | `/airboat-vs-kayak-swamp-tour-new-orleans/` (now live) | `/alligators-vs-crocodiles/` | "Airboat vs. kayak: an honest comparison" | High — target page is now live, this link was blocked on publication and no longer is |

---

## Technical SEO Checklist

| Check | Status | Details |
|---|---|---|
| robots.txt | Pass | 200, references sitemap correctly, no accidental site-wide disallow (blocks a long bot list + `/edit/`, `/fhbr-console/`, `/cdn-cgi/` — all intentional) |
| sitemap.xml | Pass | 200 |
| HTTPS | Pass | http:// requests resolve cleanly, no mixed-content flags found in spot checks |
| Homepage redirect chain | Pass | 0 redirects, single 200 |
| Core Web Vitals (mobile) | Fail (lab) / Pass (field) | Cached 6/19, 58 days old: lab perf 37/100, LCP 16.2s; field CrUX all "FAST". Needs a fresh PSI pull — blocked this session on missing `node` binary in PATH |
| Core Web Vitals (desktop) | Amber (lab) / Pass (field) | Cached 6/19: lab perf 54/100, LCP 2.5s; field CrUX "FAST" |
| Broken links (spot-checked) | 1 confirmed | `/new-orleans-zipline-tour-kayak-tour-combo/` nav link is a dead-end redirect loop back to `/` |
| Structured data (site-wide) | Fail | Zero Product/Offer/AggregateRating anywhere confirmed checked; FAQPage missing on the highest-traffic page |
| Duplicate/canonical URLs | Fail | At least 2 confirmed live pairs (airboat, first-time-kayak); pass 7 flagged 5 total Content Plan posts at risk of this once published |
| GSC index status | Not checked | MCP unavailable this session |

---

## Content Gap / Competitor Notes (carried forward, `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`, 2026-08-10)

- On AI search, NKST gets AI Overview citations on 25 queries — 20 are alligator-vs-crocodile trivia, zero are commercial swamp-tour queries. A live AI search test for "best swamp tour New Orleans kayak eco tour" named competitor **Wild Louisiana Tours' "Manchac Magic"** first; NKST placed third with generic copy. This is 6 days old, not re-tested live this pass.
- `/tours/swamp/` is thin (1,176 words) against named competitors Cajun Encounters and Tour Big Easy on the same keyword.
- CTR on `/alligators-vs-crocodiles/` is 0.32% at position 6 (should be 6-9% at that position per the source doc's benchmark) — estimated 15,000-20,000 clicks/quarter left on the table from title/meta work alone, separate from the internal-linking gap above.

---

## Prioritized Fix List

### Quick Wins (this week)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | `/airboat-vs-kayak-swamp-tour-new-orleans/` and `/first-time-kayak-swamp-tour-new-orleans/` (both now live, both duplicated at `/blog/`-prefixed URLs) | Pick the root URL as canonical for both (matches the sitemap's existing pattern), 301 the `/blog/` variant into it or fix its `<link rel="canonical">` to point at root | These two posts just went live and are already splitting ranking signal across two URLs each on day one. Fixing now costs one redirect each; waiting lets duplicate content accumulate its own backlinks/indexing and gets more expensive to unwind |
| 2 | `/alligators-vs-crocodiles/` | Add the 3-link "More reading" block (HTML pre-written in `SEO Content/Internal Linking Audit.md` lines 17-26) pointing to `/blog/manchac-swamp-visitor-guide/`, `/blog/swamp-tours-new-orleans-guide/`, and the now-live `/airboat-vs-kayak-swamp-tour-new-orleans/` | Passes link equity from the single largest organic asset on the site (308,394 impressions/90d, ~53% of sitewide impressions) into new content. Zero content cost — the HTML is already written and one of the three targets just came online |
| 3 | `/alligators-vs-crocodiles/` | Add FAQPage JSON-LD wrapping the existing Q&A content — confirmed absent again via live curl today | FAQ rich-result eligibility on the site's single biggest traffic page; zero content-rewrite cost |
| 4 | `Marketing/Blog Drafts - Staged/` (43 files, up from 34 yesterday 18:34, 14 the morning before) | David batch-reviews in one sitting. Two live posts (airboat, first-time-kayak) prove the pipeline works when drafts get approved — prioritize `alligator-tour-new-orleans` (closes a live 404) and `how-much-does-a-swamp-tour-cost-new-orleans` (content-gate 90/100 per pass 7, closes a confirmed PAA gap) next | Highest-leverage item on the whole report by volume — 43 pieces of finished content sitting at zero SEO value. The backlog is still growing faster than it's being cleared even after two posts published |
| 5 | Session/project MCP config (`~/.claude.json` project entry, or re-trust `.mcp.json` interactively) + install `node` on PATH for this session (or set `PSI_KEY` in `~/.claude/.env`) | David approves the MCP servers (`google-nkst`, `gbp`, `meta-organic`, `slack`, `clarity`) next time he opens this vault interactively, and either fixes the sandboxed session's PATH or adds a free `PSI_KEY` | Unblocks live GSC/GA4/GBP/PSI data for every future audit. Two different technical causes have now blocked PSI on two consecutive days (quota, then missing `node`) — worth a permanent fix rather than a retry each run |
| 6 | `/tours/kayak-tours/honey-island-swamp-tour/` | 301 to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (confirmed live boilerplate meta today: "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2") | Removes a low-quality indexed URL currently outranking the real tour page (#22 for a 9,900/mo term); consolidates signal onto the real booking page |
| 7 | `/` homepage main nav | Remove or rebuild the `/new-orleans-zipline-tour-kayak-tour-combo/` link — confirmed live today it still 301s straight back to `/` | Fixes a visible broken nav item on every page of the site; stops wasting crawl budget |
| 8 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/` after merging any unique content — both confirmed still live at 200 today | Ends self-cannibalization on "best swamp tour" queries; surviving page (4,158 imp/90d per Content Plan) stops splitting its own signal |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | `/tours/swamp/` | Build a real money page targeting "swamp tours new orleans" exact-match — expand past 1,176 words using content already drafted in `SEO Content/Post 1 — Swamp Tours New Orleans Guide.md`, add Product/Offer/FAQPage schema, link it from `/alligators-vs-crocodiles/` | This is the single biggest structural gap in the account: Google currently ranks the homepage instead of a dedicated page for the site's largest keyword cluster (~4,700-10,000/mo combined per two independent pulls), stuck at position 15-21. Fixing the money page is the fix, not more content volume |
| 2 | All 6 tour pages, starting with `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/` (confirmed zero commercial schema today) | Add Product + Offer (price/currency/availability, sourced from FareHarbor) + AggregateRating (source real count/average from FareHarbor or GBP, don't fabricate) sitewide | Enables star/price rich results in organic search and gives AI answer engines machine-readable data to cite. Confirmed zero commercial schema exists anywhere checked; NKST currently gets zero AI Overview citations on commercial swamp-tour queries despite 1,400+ reviews per the 8/10 audit |
| 3 | `/alligator-tour-new-orleans/` (confirmed still 404 today) | Publish a booking-intent commercial page distinct from the informational `/alligators-vs-crocodiles/` angle | Closes an indexed 404, captures direct commercial-intent volume (2,900/mo per DataForSEO) that the educational page doesn't convert |
| 4 | GBP listing(s) | Category fix (currently "Canoe & kayak tour agency" vs. local-pack winners' "Boat tour agency"/"Tour operator"), duplicate-listing cleanup, resolve the Crescent City Kayak decision | Blocked entirely on MCP access (Quick Win #5) — cannot verify live GBP state without it. Local-pack eligibility for "swamp tour near me" family of queries |
| 5 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite each of the 3 walk sections to end with a paid-tour CTA instead of "see it free" framing | Page already converts well (13,392 imp/235 clicks, 1.75% CTR per Content Plan) but dead-ends without monetization — pure copy edit, no new content needed |
| 6 | OTA listings (GetYourGuide, TripAdvisor, Viator) | Rewrite titles/descriptions to lead with extractable specifics (duration, transport, species, group size, difficulty) | Per the 8/10 audit, this is the layer AI answer engines currently cite over NKST's own site for high-intent queries. Off-platform, not blocked by anything else here |
| 7 | FareHarbor → GA4 purchase-event tracking | Confirm with a dev or directly in GA4 whether the gap (58 tracked events vs. 23,385 GHL contacts, March 2026) was ever fixed | Every conversion/ROI figure cited anywhere in NKST's marketing stack is unreliable until this is confirmed fixed |
| 8 | `/top-destinations-for-your-bachelor-bachelorette-party/` | Rebuild — no draft exists in `SEO Content/` or `Blog Drafts - Staged/`, a genuine from-scratch gap unlike most items on this list | Real unaddressed search demand flagged weak vs. competitors in the May 2026 audit |

---

## Notes

- All live/current findings above were fetched via curl against production just now (today, 2026-08-16), not copied from yesterday's passes without re-verification.
- The staged-drafts folder count (43) was counted live via `ls` this pass.
- **GSC, GA4, GBP, and PageSpeed Insights were not reachable this session** — MCP tools didn't register (same gap as all 7 prior passes), and PSI failed on a missing `node` binary (a new, different blocker than yesterday's quota exhaustion). All ranking/impression/traffic/Core-Web-Vitals figures above are dated and carried forward from named source docs, not invented.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, no MCP config was modified, and no ad platform was touched in producing this report.
- **Recommendation for the next pass:** hold again until either MCP access is unblocked (Quick Win #5) or more of the 43-file drafts backlog gets reviewed. Two posts published since yesterday is real progress and is why this pass found something worth writing down; an identical pass tomorrow against an unchanged site would not.
