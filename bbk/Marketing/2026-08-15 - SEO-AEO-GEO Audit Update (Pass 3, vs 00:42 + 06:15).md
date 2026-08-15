# BBK SEO/AEO/GEO Audit — Pass 3, 2026-08-15 (~14:20 UTC / ~09:20 local, vs. 00:42 full audit + 06:15 delta check)

**REPORT ONLY. Nothing changed live on the site, WordPress, GBP, or any ad account. This is a research/verification document for David to review. No edits, no publishing, nothing outbound.**

This is the third SEO check run today on Buffalo Bayou Kayak. It is a fresh, live re-verification pass, not a restatement of the two prior docs — every claim below was re-checked directly against production (curl, live JSON-LD parse, WebFetch, WebSearch) rather than copied forward. Bottom line up front: **almost nothing changed on the live site since 06:15** (as expected, it's been a few hours with nobody touching WordPress) — but one real thing did change: **3 more blog drafts got staged**, bringing the total to 9, and two long-standing "needs a direct fetch" open items from the 00:42 audit are now resolved with real answers instead of inference.

---

## What Actually Changed Since 06:15

1. **3 new blog drafts staged** in `Marketing/Blog Drafts - Staged/`, timestamped 06:15:27–06:18:03 today (right around/just after the 06:15 delta check ran):
   - `2026-08-15 - buffalo-bayou-park-guide.md` (covers Brief 5 — previously undrafted)
   - `2026-08-15 - full-moon-kayak-dates-2026.md` (covers Brief 12 — previously undrafted)
   - `2026-08-15 - houston-date-ideas-on-the-water.md` (covers Brief 6 — previously undrafted)

   Combined with the 3 June drafts (briefs 1, 2, 7) and the 3 from earlier this morning (briefs 2/partial, 3, 8), that's **9 staged drafts total now**, covering 8 of the original 12 content briefs (1, 2, 3, 5, 6, 7, 8, 12 — briefs 4, 9, 10, 11 still have zero draft). **None are published** — reconfirmed via a fresh live fetch of `post-sitemap.xml`, which still shows only the same 11 posts dated Nov 2023. Per instructions, unpublished staged drafts are not counted as a live SEO win regardless of volume — the content pipeline is filling up, but zero of it has hit the site.

2. **Paddlingmag.com "Guide To Kayaking Houston" — resolved with a direct fetch**, not just a search snippet. Both the 00:42 and 06:15 docs flagged this as needing a real article fetch. Did it this pass: the live article at `paddlingmag.com/trips/destinations/kayaking-houston/` does **not** mention "Buffalo Bayou Kayak" anywhere. The only Buffalo Bayou rental/tour provider it names is **Bayou City Adventures** ("rent a kayak in the park near Sabine Street from Bayou City Adventures," $30 start). Confirmed absence, not inferred.

3. **Houstonia's "7 Best Spots to Paddle and Rent Kayaks in Houston" — mostly resolved.** Direct WebFetch of the article hit a 403 (bot-blocked), but a WebSearch return quoted the article's own text directly: for the Buffalo Bayou Paddling Trail entry, "Bayou City Adventures offers guided tours and kayak rentals for this route." BBK is not the name attached to that stretch of water in Houstonia's copy either. Treat this as high-confidence, not 100% (couldn't render the full page myself), but it's a real answer where both prior docs had none.

Everything else below is unchanged from 06:15 — re-verified live today, not assumed.

---

## Data Gaps — Re-Checked, Still Present

**GSC / GA4 MCP:** Still does not exist anywhere in this environment. Re-checked both places again this pass:
- Vault `.mcp.json` (Buffalo Bayou Kayak): only `gmail-bbk`, `gbp`, `meta-organic`, `playwright`, `opencx`, `clarity`. No Search Console or Analytics server.
- Global `~/.claude.json` `mcpServers`: `ghl`, `google`, `gmail`, `facebook`, `gbp`, `imessage-send`, `google-ads`, `gmail-apresassets`, `twilio`, `higgsfield`, several `youtube-*` servers (including `youtube-bbk`), `gmail-admirenola`, `google-personal`, `imessage` — no search-console or analytics-flavored entry across any of them, and no per-vault override adds one for this vault (BBK's only per-vault addition is `opencx`).
- Also ran a live ToolSearch for GSC/GA4/analytics tooling — nothing surfaced beyond generic WebSearch/WebFetch.

No GSC/GA4 numbers appear anywhere in this document. Everything keyword/content-related below is SERP research (WebSearch/WebFetch against live pages), same honest standard as the two prior docs.

**PageSpeed Insights:** Retried directly against the live homepage this pass. Still `RESOURCE_EXHAUSTED` / HTTP 429, `quota_limit_value: 0`, same daily cap as the 00:42 and 06:15 runs. No `PSI_KEY` in `~/.claude/.env`. No official Lighthouse/CWV scores available for BBK today, at any of the three passes.

**`google-site-verification` tag:** Still live on the homepage, same value (`ZTdimCkZr-kTmPpOzczYnKjJzsqLccPSKlkof0W0bU4`), still unresolved. Nobody has told this session which Google account owns it. Still David's 10-minute chase-down.

---

## Live Re-Verification: 5 June Quick Wins

| Quick Win | Status (re-checked live, this pass) |
|---|---|
| 1-2. Publish the staged blog drafts | **Still unpublished.** `post-sitemap.xml` fetched fresh — same 11 Nov-2023 posts, none of the now-9 staged drafts present. |
| 3. Bat tour page links to blog content | **Still zero.** Fetched `/kayak-tours/houston-bat-bridge-kayak-tour/` live; only "blog"-adjacent string in the HTML is a Jetpack tracking parameter (`"blog":"248199702"`), not a content link. |
| 4. `google-site-verification` tag resolved | **Still open**, same tag value confirmed live on homepage. |
| 5. robots.txt stray `Disallow:` lines | **Unchanged.** Fetched live: `/fhbr-console/` and `/cdn-cgi/` still sit after the last named user-agent block instead of under `User-agent: *`. |

**Bonus spot-check (not one of the 5, but worth confirming nothing regressed):** live-parsed the JSON-LD on the bat tour page — `Product` + `FAQPage` schema still present and valid JSON (2 script blocks: `[Product, FAQPage]` + `[BreadcrumbList]`). No regression on the schema work from June.

---

## Technical Findings, This Pass

- **Redirects:** clean, unchanged. `https://` bare domain 200/0 redirects; `www` and `http` variants each single 301 to `https://buffalobayoukayak.com/`.
- **robots.txt:** unchanged, junk bots still blocked, GPTBot/ClaudeBot/PerplexityBot still unblocked (correct for GEO), same two orphaned `Disallow:` lines.
- **Broken-link crawl:** ran a fresh homepage-link crawl (31 unique on-domain links pulled directly from the live homepage HTML, wider net than the 18 nav/footer links the two prior docs checked). All 200 except:
  - `/privacy-policy/` → clean single 301 to `/privacy-statement-us/` (healthy redirect, not a break).
  - `/cdn-cgi/l/email-protection#...` → 404 on a direct GET. This is Cloudflare's automatic email-address-obfuscation decode endpoint (injected by Cloudflare when a `mailto:` link is on the page), not a WordPress link. It typically resolves fine when a real browser clicks it (Cloudflare's edge handles the decode with proper request context) but 404s to a bare curl/crawler request lacking that context. Flagging once since it showed up in this wider crawl — low priority, likely a non-issue, but if David wants to eliminate the false-positive on future automated crawls the fix is disabling Cloudflare's Email Address Obfuscation for this zone (cosmetic/infra, not a WordPress task).
- **Page weight / TTFB (curl, no PSI):** Homepage 0.59s TTFB / 1.31s total / 185KB; bat tour page 0.55s TTFB / 0.89s total / 141KB; FAQ 0.56s TTFB / 0.92s total / 145KB. These read faster than the 00:42 pass's 0.75-0.96s TTFB range, but this is a single curl sample per page each time, not controlled — treat as normal variance, not a confirmed performance win. Real Lighthouse/CWV data still requires a PSI key.
- **Keyword/content picture:** No material change from 00:42 beyond the two paddlingmag/Houstonia items resolved above. Bayou City Adventures remains the name that shows up across both outlets for Buffalo Bayou paddling generally — BBK's job is still to out-content them via schema, the FAQ page, and (once published) the blog, not to out-rank them on terms they already own editorially.

---

## Prioritized Fix List

### Quick Wins (this week)

1. **Publish `Marketing/Blog Drafts - Staged/2026-06-13 - houston-bat-kayak-tour-waugh-bridge.md`.** Still the single highest-value item across all three passes today. Peak bat season is running right now and this page has sat finished since June. Expected impact: gives AI answer engines and Google a citable BBK page for "Waugh Bridge bats" queries, currently owned by buffalobayou.org / 365thingsinhouston / TPWD.
2. **Publish the other 8 staged drafts** (now 9 total, up from 3 in June) after David's review, prioritizing by seasonal relevance: `full-moon-kayak-dates-2026.md` next (direct booking intent, time-sensitive, needs to go live before dates go stale), then `is-buffalo-bayou-safe-to-kayak.md` and `kayaking-for-beginners-in-houston.md` (fill briefs 3 and 8, currently zero live coverage). Expected impact: turns a 33-month-dead blog into a live content asset and gives Google fresh crawl signal across 9 new URLs instead of 1.
3. **Add a "From the Blog" link block to `/kayak-tours/houston-bat-bridge-kayak-tour/`**, pointing to the bat colony guide once published, plus reciprocal links from each new post back to the relevant tour/rental page with descriptive anchors ("Houston bat bridge kayak tour," not "book now"). This is the exact June Step 4 spec, confirmed still undone (zero links either direction, re-verified live this pass). Expected impact: stops leaking equity between the money pages and the blog the moment posts start publishing — do this at the same time as item 2, not after.
4. **Chase down the `google-site-verification` meta tag** (`ZTdimCkZr-kTmPpOzczYnKjJzsqLccPSKlkof0W0bU4`) on the homepage — third time this exact item has been flagged today across three separate passes. Ask David directly which Google account this belongs to (his, Connor's, or whoever originally built the site). Expected impact: could resolve the entire GSC access gap that's blocking real keyword/CTR data in one login, instead of a fresh Search Console re-verification.
5. **Clean up the two orphaned `Disallow:` lines in `robots.txt`** (`/fhbr-console/`, `/cdn-cgi/`) — move them under `User-agent: *`. Flagged in June, at 00:42, at 06:15, and again now. One FareHarbor support ticket. Expected impact: cosmetic/low-risk, removes ambiguity for strict crawler parsers.
6. **New this pass — confirm the paddlingmag.com and Houstonia non-mentions with David** and green-light outreach. Both were "needs verification" items in the 00:42 audit; both are now confirmed absent via direct fetch/quoted text, not inference. Expected impact: turns "maybe worth pitching" into "confirmed gap, worth pitching now" — removes the last excuse to delay the outreach email.

### Strategic Work (this quarter)

1. **Draft and publish a combined "Is Buffalo Bayou Safe to Kayak?" pillar** on `/2023/11/02/are-alligators-safe-to-kayak-with/` — merge the newly-staged `is-buffalo-bayou-safe-to-kayak.md` draft into an upgrade of the existing 2023 post rather than publishing as a separate competing URL. The 2023 post already ranks #1 in a live spot-check for this query cluster (confirmed at 00:42, unchanged). Expected impact: one strong consolidated page with a real shot at a featured snippet / AI Overview citation, instead of two thin pages splitting authority.
2. **Send the paddlingmag.com and Houstonia outreach email now that both gaps are confirmed live**, not inferred. Pitch: live Product/FAQPage schema on all 8 tour/rental pages, the ~4,400-word FAQ page, and the bat colony guide (once published). Expected impact: both outlets are cited directly by AI answer engines for Houston-kayaking queries per the June GEO findings — inclusion is a GEO win ranking alone doesn't buy. Per CLAUDE.md, any outbound pitch email should be signed by Connor Champaign (Manager) or the business name, never David.
3. **Merge the 8 thin 2023 history posts into one "History of Buffalo Bayou" pillar with 301s**, per June's still-open recommendation. Confirmed via today's `post-sitemap.xml` fetch: all 8 are still live individually, unchanged since Nov 2023. Expected impact: converts 8 orphaned, dilutive pages into 1 page with real topical authority.
4. **Draft the remaining 4 briefs with zero coverage** — briefs 4 (fold into item 1 above rather than drafting separately), 9 (Best Time of Year to Kayak in Houston), 10 (Houston Skyline Photo Spots), 11 (Team Building in Houston). 8 of 12 original briefs now have drafts; these 4 are what's left.
5. **Get a `PSI_KEY` added to `~/.claude/.env`.** Flagged in all three passes today — the keyless daily quota has blocked real Lighthouse/CWV data on every single run. Infrastructure fix, not a site fix, but it's now blocked three audits in a row.
6. **Resolve GSC/GA4/GBP access.** Still the most-repeated line item across all three passes today. Every keyword/content finding in this document and its two predecessors is SERP inference because there's no first-party data connected anywhere in this environment. This is the single change that would make every future BBK SEO audit dramatically more accurate.

---

## Notes on Scope

This pass re-verified the specific claims flagged as open in the 06:15 doc, ran a wider (31-link vs. 18-link) homepage crawl, retried PSI and the GSC/GA4 MCP check, and resolved two "needs direct fetch" items from the 00:42 audit with real fetches instead of search snippets. It did not re-audit the full 15-page scope from the 00:42 pass in exhaustive detail (title tags, meta descriptions, alt text sitewide) — nothing suggests any of that changed in a few quiet hours with no WordPress activity, and re-doing it wholesale would just restate the 00:42 findings. Did not touch the Google Ads account, GBP listing, or the content of the 9 staged drafts (quality/brand-voice review of those is a separate task, not part of this technical/SEO delta check).
