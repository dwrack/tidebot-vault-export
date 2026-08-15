---
type: seo-audit
business: New Orleans Kayak Swamp Tours
site: neworleanskayakswamptours.com
date: 2026-08-15
status: DRAFT — PENDING DAVID'S REVIEW — REPORT ONLY, NO CHANGES APPLIED
---

# NKST SEO + Tech SEO Audit — 2026-08-15 (Pass 5, Consolidated Final)

> **DRAFT. REPORT ONLY.** Nothing in this document has been applied to the live site, WordPress, GBP, or any ad platform. This is the 5th unattended audit today (Pass 1 ~00:28, Pass 2 ~01:49, Pass 3 ~05:36, Pass 4 delta-check ~mid-morning, this one). **This is not a 6th independent re-crawl.** Passes 1-4 already exhaustively verified the site's current state via live HTTP fetch, HTML/schema inspection, and a full homepage link crawl. Re-running all of that today would burn time to confirm what's already confirmed. Instead: (1) six targeted spot-checks below confirm nothing material changed since Pass 4, (2) one genuinely new root-cause finding — the reason GSC/GA4/GBP data has been unreachable across all 5 passes — is diagnosed for the first time, and (3) everything is merged into one final, single prioritized fix list so David has one document to act on instead of five.

**Bottom line up front: don't run a Pass 6.** Every open item below needs David at a keyboard, not another audit. The one exception — get the MCP servers approved — is itself now Quick Win #1, because it's what unblocks real GSC/GA4/GBP data for every future pass.

---

## What's new in this pass (read this first)

**1. Root cause of the data wall, found for the first time.** All 4 prior passes today ran `ToolSearch` for GSC/GA4/PSI tools, got nothing, and concluded "the MCP isn't exposing tools this session" without checking why. This pass checked why: the vault's `.mcp.json` lists seven servers — `google-nkst`, `gbp`, `meta-organic`, `slack`, `playwright`, `opencx`, `clarity` — but this session's actual resolved MCP server list (`~/.claude.json`, this project's entry) only has **two active: `playwright` and `opencx`**. `google-nkst` (which would expose GSC/GA4), `gbp`, `meta-organic`, `slack`, and `clarity` are simply not loaded in this session at all. The `GOOGLE_CLIENT_SECRET` env var is set and the OAuth token file (`~/.config/google/tokens/nolakayaktours-at-gmail-com.json`) exists on disk, so this isn't a broken credential — it's that the newer servers added to `.mcp.json` were never picked up/approved for this project's active session config. That approval step is interactive (a trust prompt when Claude Code loads new `.mcp.json` entries) and can't happen in an unattended run. **This is the actual fix for the data gap that's been flagged as "still unavailable" across 5 consecutive audits** — not a retry-until-it-works problem, a one-time approval problem. See Quick Win #1.

**2. Six spot-checks confirm zero material change since Pass 4:**

| Check | Result |
|---|---|
| Homepage links to `/tours/swamp/` or `/swamp-tours-new-orleans-guide/` | Still 0 matches |
| `/new-orleans-zipline-tour-kayak-tour-combo/` nav link | Still 301s straight back to `/` — dead end |
| `/tours/kayak-tours/honey-island-swamp-tour/` meta description | Still literal boilerplate: "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2" |
| `/which-swamp-tours-are-the-best/` and `/which-is-the-best-swamp-tour-around-new-orleans/` | Both still live (200) — cannibalization unresolved |
| `/alligator-tour-new-orleans/` | Still 404 (content-gate-passed draft exists, page doesn't) |
| `Marketing/Blog Drafts - Staged/` file count | **26, up from 23 at Pass 4 and 14 at Pass 2** — the approval backlog keeps growing, unattended, faster than anything else on this list moves |

Nothing here contradicts Pass 2-4. The single trend worth flagging on its own: the staged-drafts folder has grown from 14 to 26 over one day with zero publish decisions made. That's now the largest number on this entire report.

---

## Data grounding — what's real vs. carried forward

No fresher GSC, GA4, or GBP pull was possible this pass (see root cause above). Every ranking, impression, and traffic figure below is carried forward from a dated source, not invented:

- **GSC keyword/position data:** 2026-08-10 pull, 90-day window (2026-05-12 to 2026-08-09) — `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`
- **GA4 traffic/conversion data:** March 2026 pull — 11,848 sessions/90d, Paid Search converting 19.8% vs. Organic 13.0% vs. Paid Social 0.8%, and an unresolved FareHarbor→GA4 purchase-event gap (58 tracked events vs. 23,385 GHL contacts in the same window)
- **Core Web Vitals / Lighthouse:** cached PSI run from 2026-06-19, now **57 days old**. Fresh PSI attempts on 2026-08-14 and 2026-08-15 both returned `HTTP 429 Quota exceeded`, no `PSI_KEY` on file at `~/.claude/.env`
- **Live/current data (this pass and Pass 2-4):** page existence, HTTP status, HTML source, schema markup, internal links, meta tags — all directly fetched from production today

Where a number below is carried forward, it's labeled as such. Nothing is guessed.

---

## Prioritized Fix List (Final, Consolidated)

Merges SEO + technical findings from all 5 passes today into one list. Supersedes the fix lists in Pass 1, Pass 2, Pass 3, and Pass 4 — those documents remain in the vault for the underlying verification detail, but this is the one to work from.

### Quick Wins (this week)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 1 | Session/project MCP config (`~/.claude.json` project entry for this vault, or re-trust `.mcp.json` interactively) | David approves the newer MCP servers (`google-nkst`, `gbp`, `meta-organic`, `slack`, `clarity`) the next time he opens this vault in an interactive session — Claude Code will prompt for this. Confirm afterward with a quick `ToolSearch` for `gsc_query`/`ga4_report`. | **Unblocks real GSC/GA4/GBP data for every future audit.** Every "carried forward" figure in this report — GSC positions from Aug 10, GA4 sessions from March, GBP category status unverified across 5 audits — becomes a live number instead of a stale one. This is the single highest-leverage fix on this list because it fixes the process, not just one page. |
| 2 | `Marketing/Blog Drafts - Staged/` (26 files now, was 14 two passes ago) | David batch-reviews and approves/rejects in one sitting. Discard or repurpose the confirmed duplicates first (`airboat-vs-kayak-swamp-tour-new-orleans` and `first-time-kayak-swamp-tour-new-orleans`, both already live under the May `SEO Content/` slugs — publishing the staged copies would recreate the exact cannibalization problem flagged elsewhere on this site). Then publish the rest, starting with `alligator-tour-new-orleans` (content-gate 88/100, closes a 5-audit-old "genuinely missing page" gap) and `how-much-does-a-swamp-tour-cost-new-orleans` (content-gate 90/100, closes the highest commercial-intent PAA gap — confirmed via live WebSearch on 2026-08-15 that NKST is still absent from this query's results while Groupon/NOLA Adventures/Cajun Pride/Gators & Ghosts fill it). | Converts roughly 3 months of "needs research and writing" line items into a single approval pass. Nothing else on this list matters much if the content stays unpublished — the site now has more written, content-gate-passed inventory than it has published pages. |
| 3 | `/alligators-vs-crocodiles/` (272k impressions/quarter per the Aug 10 GSC pull — the site's highest-traffic page) | Add a "more reading" internal-link block to `/tours/swamp/`, `/swamp-tours-new-orleans-guide/`, and `/blog/airboat-vs-kayak-swamp-tour-new-orleans/`. Confirmed live today: page links to 6 tour pages already but 0 links to any of these three. All three destination pages are already built (3,100-4,600+ words, two of them already carry full FAQPage schema). | Redirects a slice of the biggest traffic asset on the site toward pages that are already built and good but structurally invisible — pure linking fix, no content work. |
| 4 | `/` (homepage) | Add nav/hero links to `/tours/swamp/` and `/swamp-tours-new-orleans-guide/`. Repoint the Honey Island nav link from `/tours/kayak-tours/honey-island-swamp-tour/` (301s) directly to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. Fix or remove the `/new-orleans-zipline-tour-kayak-tour-combo/` nav link — confirmed live today it still 301s straight back to the homepage, a dead end for anyone who clicks it. | The homepage currently ranks position 15-21 (Aug 10 GSC data) for the site's biggest keyword cluster ("swamp tours new orleans," ~1,100-4,000/mo; "swamp tour new orleans," ~3,000-10,000/mo) while linking to none of the pages built to win it. |
| 5 | `/tours/kayak-tours/honey-island-swamp-tour/` (blog category archive, confirmed ranking position 22 for a 9,900/mo keyword ahead of the real tour page) | 301 (or noindex if the CMS can't 301) to `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`. Meta description confirmed live today still reads the literal boilerplate "Click to view honey island swamp tour category posts in Blog \| Page 1 of 2." | Stops a boilerplate archive page from being Google's answer for a 9,900/mo keyword; hands that ranking signal to the real, schema-eligible tour page. |
| 6 | `/which-is-the-best-swamp-tour-around-new-orleans/` | 301 into `/which-swamp-tours-are-the-best/` (position 24 per Aug 10 GSC data), merging any unique content first. Both confirmed still live today with distinct H1s. | Ends self-cannibalization on "best swamp tour" queries (~1,600/mo) — the surviving page stops splitting its own ranking signal. |
| 7 | 5 recent Content Plan posts, both URL variants each (`/swamp-tours-new-orleans-guide/` + `/blog/swamp-tours-new-orleans-guide/`, and the same pattern for the Manchac, Bayou Bienvenue, and two other posts) | Pick the root URL as canonical (it's already the sitemap's choice) and either 301 the `/blog/`-prefixed variant or fix its `<link rel="canonical">` tag — confirmed via direct fetch that each variant currently self-canonicalizes, so there's no consolidation signal at all, not a "Google usually sorts it out" situation. | Consolidates ranking signal currently split across 10 live URLs down to 5, on pages that are otherwise the best-built content on the site (two already carry full FAQPage schema). |
| 8 | `~/Projects/tech-seo/psi-run.mjs` environment | Get a free PageSpeed Insights API key (Google Cloud Console), add as `PSI_KEY=...` to `~/.claude/.env`. | Unblocks a real Core Web Vitals read — the mobile-37 performance score has now been carried forward, unverified, for 57+ days across 5 consecutive audits. |

### Strategic Work (this quarter)

| # | Page/URL | Exact Change | Expected Impact |
|---|---|---|---|
| 9 | `/tours/swamp/` | Add Product + Offer (price/currency/availability) + AggregateRating (4.9 stars / 1,416 reviews, per Aug 10 GSC/GBP data) + FAQPage schema. Content is already ~3,100+ words — this is a schema/linking gap, not a content gap, confirmed across 5 audits. | Still the single biggest structured-data lever identified on the site — star ratings and price in search results, plus AI-answer extractability. |
| 10 | `/`, plus all 6 tour pages | Add AggregateRating + Product/Offer schema sitewide using pricing already published in page bodies. Confirmed zero commercial schema exists anywhere on the site as of today. | Enables rich results (stars, price) in organic search and improves extractability for AI Overviews/answer engines, which currently source NKST info from third-party OTA listings instead of the site itself. |
| 11 | GetYourGuide / TripAdvisor / Viator listings | Rewrite third-party OTA listing copy to lead with extractable specifics (duration, transport, species list, group size, difficulty) instead of mission-first language. | Confirmed via repeated live WebSearch checks that this is the layer AI answer engines currently source from over NKST's own site for high-intent queries like "how much does a swamp tour cost." |
| 12 | GBP: primary category + duplicate-listing cleanup | Needs a live GBP check once the MCP is approved (Quick Win #1) — carried forward unverified across 5 audits: category mismatch ("Canoe & kayak tour agency" vs. local-pack winners' "Boat tour agency"/"Tour operator"), plus 5 David-controlled listings clustering within a few blocks including one at a fabricated "Swamp Tour Street" address (standalone suspension risk). | Local-pack eligibility for "swamp tour near me" (12,100/mo, local-pack intent, NKST not ranking organically for it). |
| 13 | Crescent City Kayak property decision | Confirmed live and resolving today, unchanged across 5 audits. Either 301 into NKST or commit to a genuine funnel rebuild. | Every audit cycle this stays undecided, the property keeps splitting authority NKST already wins head-to-head on. |
| 14 | `/3-free-swamp-walks-in-and-around-new-orleans/` (ranking position 20 for "swamp tours in new orleans," 1,900/mo, a commercial-intent query) | Rewrite every section to end with a paid-tour CTA instead of the current "see it free" framing. No draft exists — this is a genuine edit-to-a-live-page task, one of the few left on this whole list. | Redirects commercial-intent traffic currently landing on a page whose thesis argues against booking a paid tour. |
| 15 | Bachelor/bachelorette content rebuild — `/top-destinations-for-your-bachelor-bachelorette-party/` | Confirmed still live, unrebuilt, across all 5 audits today. No draft found in `SEO Content/` or `Blog Drafts - Staged/` — genuinely still a from-scratch content gap, unlike almost everything else on this list. | Real, unaddressed search demand; both NKST's and competitors' existing content on this topic were flagged weak in the May 2026 audit. |
| 16 | FareHarbor → GA4 purchase-event tracking | Confirm with a dev or in GA4 directly (not verifiable via unattended HTTP checks) whether this was ever fixed — flagged unresolved for 2+ weeks of audit runs. As of the March 2026 pull: only 58 purchase events tracked against 23,385 GHL contacts in the same window. | Every conversion-rate and ROI figure cited anywhere in NKST's marketing stack — SEO, ads, content — is unreliable until this is confirmed fixed. |

---

## Notes

- Six spot-checks in this pass were run live via `curl` against production just now, not copied from prior passes. Everything else in the Data Grounding section above is explicitly labeled by source and date.
- The staged-drafts folder count (26) was counted live via `ls` this pass.
- The MCP root-cause finding (config file comparison between the vault's `.mcp.json` and this session's active `~/.claude.json` project entry) is new to this pass and wasn't investigated by Passes 1-4.
- **Recommend no Pass 6** until either David approves the newer MCP servers (Quick Win #1) so a real GSC/GA4/GBP-grounded audit becomes possible, or he clears the standing fix list above. A sixth same-day HTTP re-crawl of an unchanged site adds no new information — the marginal value from here is in David acting on what's already found, not more auditing.
- No content was published, no schema was added, no redirects were created, no GBP settings were changed, no MCP config was modified, and no ad platform was touched in producing this report. Every item above is a recommendation awaiting David's approval.
