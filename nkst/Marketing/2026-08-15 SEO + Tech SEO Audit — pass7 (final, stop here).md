---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: DRAFT — PENDING DAVID'S REVIEW — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech SEO Audit — 2026-08-15 (Pass 7, Final — Recommend No Pass 8)

> **DRAFT. REPORT ONLY.** Nothing here has touched the live site, WordPress, GBP, or any ad platform.

**Before reading further: this is the 7th SEO/Tech-SEO audit run on this vault today** — `Marketing/SEO + Tech SEO Audit — 2026-08-15.md` (00:28), `pass2.md` (01:49), `pass3.md` (05:42), `pass4.md` (09:55), `pass5 (consolidated final).md` (12:47), `SEO Content/2026-08-15 SEO + Tech-SEO Audit — NKST.md` (14:33), and this one (18:34). Six prior passes today already exhaustively HTTP-crawled, schema-inspected, and link-mapped the production site. **This pass does not re-derive any of that from scratch** — doing so an 7th time would burn time confirming what six passes already confirmed, with no new information. Instead: (1) 11 targeted live spot-checks below confirm the site is unchanged since the 14:33 pass, (2) the one real conflict between passes is resolved, (3) one new trend is flagged, and (4) everything is merged into one final list. **Recommend this be the last unattended pass until David acts on Quick Win #2 (drafts backlog) or #1 (MCP/PSI access) below.** Running an 8th identical crawl against an unchanged site produces a document, not new value.

---

## What's new in this pass

**1. Data wall confirmed unchanged, independently re-checked.** `ToolSearch` for `gsc_*`, `ga4_*`, and `gbp_*` tools returned nothing this session (same as all 6 prior passes). `.mcp.json` in this vault lists `google-nkst` and `gbp` servers with token files present at `~/.config/google/tokens/`, but neither is registering tools in this session — matches the root cause first diagnosed in Pass 5 (session-level MCP approval gap, not a broken credential). `~/.claude/.env` has no `PSI_KEY` set — PageSpeed Insights is still unreachable (Pass 3 and the 14:33 pass both hit `HTTP 429 quota exceeded` on the keyless runner; not re-tested this pass since the quota is daily and nothing indicates it reset).

**2. The Pass 1-5 vs. 14:33-pass conflict, resolved.** Passes 1 through 5 all flagged "`/alligators-vs-crocodiles/` has 0 links to `/tours/swamp/`" as the top quick win. The 14:33 pass caught the error: `/tours/swamp/` is a soft-404 (200 status, but renders the theme's search template, not real content) — the actual live category page is `/tours/swamp-kayak-tours/`. Re-verified fresh via curl this pass: `/alligators-vs-crocodiles/` contains **9 links** to `/tours/swamp-kayak-tours/` paths already. **The "0 internal links to the money page" framing in Passes 1-5 does not hold.** What is still confirmed true: the page has zero FAQPage schema and zero links to blog/guide content (only to booking pages) — that's the real, still-open gap, reflected in Quick Win #3 below.

**3. New trend: staged drafts backlog keeps growing, now the largest number on this report.** `Marketing/Blog Drafts - Staged/` file count, counted live this pass: **34 files** — up from 26 at Pass 5 (12:47), and 14 at the start of the day. That's 8 more unreviewed drafts added in the ~6 hours since Pass 5, faster than any other item on this list is moving. This is now flagged as the single highest-leverage bottleneck (see Quick Win #2).

**11 live spot-checks run fresh this pass (curl against production, 18:34 PT):**

| Check | Result |
|---|---|
| `robots.txt` | 200, healthy |
| `/new-orleans-zipline-tour-kayak-tour-combo/` nav link | Still 301 → `/` — dead end, unchanged |
| `/tours/kayak-tours/honey-island-swamp-tour/` meta description | Still literal boilerplate: "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2" |
| `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (real tour page) | 200, healthy |
| `/tours/swamp-kayak-tours/` (real category page) | 200, healthy |
| `/tours/swamp/` | 200 but soft-404 (search template, not content) — confirms 14:33-pass finding |
| `/which-swamp-tours-are-the-best/` and `/which-is-the-best-swamp-tour-around-new-orleans/` | Both still 200 — cannibalization unresolved |
| `/alligator-tour-new-orleans/` | Still 404 |
| `/alligators-vs-crocodiles/` links to `/tours/swamp-kayak-tours/*` | 9 (confirms 14:33-pass correction, contradicts Passes 1-5) |
| `/alligators-vs-crocodiles/` FAQPage schema | Absent — confirmed again, still the real gap |
| `Marketing/Blog Drafts - Staged/` file count | 34 (up from 26 at 12:47, 14 this morning) |

---

## Data grounding — what's real vs. carried forward

No fresher GSC, GA4, or GBP pull was possible this pass (data wall above). Every ranking, impression, and traffic figure below is carried forward from a dated source, not invented:

- **GSC keyword/position data:** `SEO Content/Content Plan.md`, real GSC pull, last-90-days as of 2026-05-06 (~3.5 months old) — the most complete measured keyword/traffic dataset in the vault. A second, narrower pull exists at `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md` (2026-08-10, 90-day window).
- **GA4 traffic/conversion data:** March 2026 pull — 11,848 sessions/90d, Paid Search converting 19.8% vs. Organic 13.0% vs. Paid Social 0.8%; unresolved FareHarbor→GA4 purchase-event gap (58 tracked events vs. 23,385 GHL contacts in the same window).
- **Core Web Vitals / Lighthouse:** cached PSI run from 2026-06-19 — now 57+ days old. No fresh attempt this pass (see above); last two attempts (Pass 3, 14:33-pass) both hit daily quota.
- **Live/current data (this pass and all 6 priors):** page existence, HTTP status, HTML source, schema markup, internal links, meta tags, robots.txt/sitemap — directly fetched from production, timestamped per pass.

---

## Prioritized Fix List (Final, Consolidated)

Merges findings from all 7 passes today, corrects the Pass 1-5 `/tours/swamp/` error using the 14:33-pass finding, and adds the drafts-backlog trend. **This supersedes all 6 prior documents from today** — they remain in the vault for underlying verification detail, but this is the one to work from.

### Quick Wins (this week)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | Session/project MCP config (`~/.claude.json` project entry for this vault, or re-trust `.mcp.json` interactively) + `~/.claude/.env` | David approves the MCP servers (`google-nkst`, `gbp`, `meta-organic`, `slack`, `clarity`) next time he opens this vault interactively (Claude Code will prompt), and adds a free `PSI_KEY` (Google Cloud Console → enable PageSpeed Insights API). | Unblocks real GSC/GA4/GBP/PSI data for every future audit — every "carried forward" figure in this report (GSC from May/Aug, GA4 from March, PSI from June) becomes a live number. Highest-leverage single fix on this list; it fixes the process, not one page. |
| 2 | `Marketing/Blog Drafts - Staged/` (34 files, up from 14 this morning — growing ~8/6hrs) | David batch-reviews and approves/rejects in one sitting. First resolve two duplicate pairs to avoid recreating cannibalization: airboat-vs-kayak (`SEO Content/Post 2` vs. `2026-08-14 - airboat-vs-kayak-swamp-tour-new-orleans.md`) and first-time-kayak (`SEO Content/Post 5` vs. `2026-08-14 - first-time-kayak-swamp-tour-new-orleans.md`). Then publish, starting with `alligator-tour-new-orleans` (content-gate 88/100, closes the live 404 at #11 below) and `how-much-does-a-swamp-tour-cost-new-orleans` (content-gate 90/100, closes a commercial-intent PAA gap NKST is confirmed absent from). | Single highest-leverage item on the whole report — the backlog is now growing faster than anything else moves. Converts ~3 months of "needs research and writing" into one approval pass; nothing else here matters much if written content stays unpublished. |
| 3 | `/alligators-vs-crocodiles/` | Add FAQPage JSON-LD wrapping the existing Q&A content. Confirmed live this pass (fresh curl): still only Article + BreadcrumbList + ImageObject + Organization + ListItem — no FAQPage. | This is the single largest organic asset on the site (308,394 impressions / 583 clicks over 90 days at position 6.5 per `Content Plan.md` — ~53% of sitewide impressions). FAQ rich-result eligibility, zero content-rewrite cost. |
| 4 | `/alligators-vs-crocodiles/` | Once new posts are live, add a "more reading" block linking to `/blog/manchac-swamp-visitor-guide/`, `/blog/swamp-tours-new-orleans-guide/`, and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/` (HTML pre-written in `SEO Content/Internal Linking Audit.md`, lines 17-26). Note: this page already links to `/tours/swamp-kayak-tours/` 9x and to 4 booking pages — the real gap is 0 links to blog/guide content, not 0 links overall (corrects Passes 1-5). | Passes link equity from the 308k-impression page into new content targeting the ~4,700-impression "swamp tour new orleans" page-2 cluster. Blocked only on Quick Win #2. |
| 5 | `/` (homepage) main nav | Remove or rebuild the `/new-orleans-zipline-tour-kayak-tour-combo/` nav link — confirmed live this pass it still 301s straight back to `/`, a dead end in primary navigation on every page. | Fixes a visible broken nav item; stops wasting crawl budget on a self-referential redirect inherited sitewide. |
| 6 | `/tours/kayak-tours/honey-island-swamp-tour/` (blog category archive) | 301 to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/` (the real tour page). Confirmed live this pass: still serves boilerplate meta "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2," no product schema. | Removes a low-quality indexed URL actively hurting CTR on any impression it earns; consolidates signal onto the real booking page (2,274 impressions @ pos 12.9 per `Content Plan.md`). |
| 7 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/` (4,158 impressions / 49 clicks @ pos 11.0 per `Content Plan.md`), merging unique content first. Confirmed live this pass: both still 200 with distinct H1s. | Ends self-cannibalization on "best swamp tour" queries (~1,600-4,000/mo) — surviving page stops splitting its own ranking signal. |
| 8 | 5 Content Plan posts, both URL variants each (root vs. `/blog/`-prefixed, e.g. `/swamp-tours-new-orleans-guide/` + `/blog/swamp-tours-new-orleans-guide/`) | Pick the root URL as canonical (already the sitemap's choice); 301 the `/blog/`-prefixed variant or fix its `<link rel="canonical">` — each variant currently self-canonicalizes, no consolidation signal exists. | Consolidates ranking signal split across 10 live URLs down to 5, on otherwise well-built content (two already carry FAQPage schema). |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 9 | `/tours/swamp-kayak-tours/` (real category page — see correction above, not `/tours/swamp/`) | Expand using content already written in `SEO Content/Post 1 — Swamp Tours New Orleans Guide.md` (1,800-2,200 words, FAQ schema spec'd) — port directly in, or publish Post 1 at its own slug and cross-link both directions. | The cluster "swamp tours new orleans" / "swamp tour new orleans" / "new orleans swamp tours" totals ~4,700 monthly impressions stuck at position 11-15 (`Content Plan.md`), with no page currently built to own it. |
| 10 | `/`, plus all 6 tour pages | Add Product + Offer (price/currency/availability) + AggregateRating schema sitewide using pricing already published in page bodies (David needs to source real rating count/average from FareHarbor or GBP — don't fabricate). Confirmed zero commercial schema exists anywhere on the site as of this pass. | Enables rich results (stars, price) in organic search; improves extractability for AI Overviews/answer engines, which currently source NKST info from third-party OTA listings instead of the owned site. |
| 11 | `/alligator-tour-new-orleans/` (confirmed still live 404 this pass) | Build an actual booking-intent commercial page at this URL — the existing staged draft is informational, not a commercial landing page for this exact keyword. | Closes an indexed 404; captures direct commercial-intent volume for "alligator tour new orleans" that the educational `/alligators-vs-crocodiles/` page doesn't convert. |
| 12 | `/3-free-swamp-walks-in-and-around-new-orleans/` | Rewrite each of the 3 walk sections to end with a paid-tour CTA (Manchac Mystic booking page) instead of the current "see it free" framing. No draft exists — live-page copy edit. | Page already converts traffic well (13,392 impressions / 235 clicks, 1.75% CTR per `Content Plan.md`) but dead-ends without monetization — direct booking lift, zero new content needed. |
| 13 | GBP listing(s) — category + duplicate cleanup, and the Crescent City Kayak / Wild Louisiana Tours property question | Needs live GBP check once MCP is approved (Quick Win #1) — carried forward unverified across all 7 audits today: category mismatch ("Canoe & kayak tour agency" vs. local-pack winners' "Boat tour agency"/"Tour operator"), 5 David-controlled listings clustering within a few blocks (one at a fabricated "Swamp Tour Street" address — standalone suspension risk), and the unresolved Crescent City Kayak 301-vs-rebuild decision. | Local-pack eligibility for "swamp tour near me" (12,100/mo, local-pack intent, NKST not ranking organically). Largest unverified item across the entire day's audit work. |
| 14 | `/top-destinations-for-your-bachelor-bachelorette-party/` | Rebuild — confirmed still live and unrebuilt across all 7 audits today. No draft found in `SEO Content/` or `Blog Drafts - Staged/` — a genuine from-scratch content gap, unlike most of this list. | Real, unaddressed search demand; both NKST's and competitors' existing content were flagged weak in the May 2026 audit. |
| 15 | GetYourGuide / TripAdvisor / Viator listings | Rewrite titles/descriptions to lead with extractable specifics (duration, transport, species list, group size, difficulty) and match the on-site "honest comparison" positioning. Off-platform work, not blocked by anything else on this list. | Confirmed via repeated WebSearch checks this is the layer AI answer engines currently source from over NKST's own site for high-intent queries like "how much does a swamp tour cost." Also strengthens brand consistency for the "honest operator" positioning. |
| 16 | FareHarbor → GA4 purchase-event tracking | Confirm with a dev or directly in GA4 (not verifiable via unattended HTTP checks) whether this was ever fixed — flagged unresolved across multiple weeks of audits. As of the March 2026 pull: only 58 purchase events tracked against 23,385 GHL contacts in the same window. | Every conversion-rate/ROI figure cited anywhere in NKST's marketing stack (SEO, ads, content) is unreliable until confirmed fixed. |

---

## Notes

- 11 spot-checks in this pass were run live via `curl` against production just now (18:34 PT), not copied from prior passes.
- The staged-drafts folder count (34) was counted live via `ls` this pass.
- The `/tours/swamp/` vs. `/tours/swamp-kayak-tours/` conflict between Passes 1-5 and the 14:33 pass is resolved above in favor of the 14:33 pass's finding, independently re-verified this pass.
- **GSC, GA4, GBP, and PageSpeed Insights were not reachable this session** — same MCP/quota wall as all 6 prior passes today. All ranking/impression/traffic figures above are dated and carried forward from named source docs, not invented.
- **Recommend no Pass 8.** Every open item above needs David at a keyboard — approving MCP servers (Quick Win #1), clearing the drafts backlog (Quick Win #2), or making the GBP/Crescent City/OTA calls that can't be resolved by unattended HTTP checks. An 8th same-day re-crawl of an unchanged site adds no new information; if this skill is running on a recurring schedule, it should be paused or spaced out (e.g., weekly) rather than re-firing same-day.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, no MCP config was modified, and no ad platform was touched in producing this report. Every item above is a recommendation awaiting David's approval.
