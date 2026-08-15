# Houston Pedal Barge — SEO & Tech-SEO Audit (2026-08-15)

**Status: DRAFT — pending David's approval. Report only. No changes have been applied to the live site, WordPress, GBP, or any ad account.**

**Date:** 2026-08-15
**Domain audited:** houstonpedalbarge.com (live crawl this date, via curl/Playwright-style checks + PageSpeed Insights API)
**Prior docs referenced:** `Houston Pedal Barge — AI SEO Audit & Action Plan (May 2026).md`, `Marketing/SEO Audit & Plan (June 2026).md`, `Marketing/SEO-AEO-GEO + Analytics Deep Dive (June 11 2026).md`

---

## Data availability — read this first

This vault's `.mcp.json` has no GSC or GA4 MCP server configured (only google-houston/Gmail, gbp, meta-organic, playwright, opencx, clarity). I confirmed no GSC/GA4 tools were reachable before concluding this. **No GSC query/impression/click data or GA4 traffic data could be pulled for this audit.** Every number below is either from the live site crawl, PageSpeed Insights, or explicitly carried over and labeled as "per the June 11 audit" (do not treat those as current — they are 65 days old).

PageSpeed Insights/Lighthouse also came back **HTTP 429 (daily quota exceeded)** on the keyless API and no `PSI_KEY` is configured in `~/.claude/.env`. Core Web Vitals below are a directional proxy from raw TTFB/page-weight, not real Lighthouse scores. Recommend re-running with a PSI API key.

This is an on-page, technical, schema, and competitive audit — genuinely useful, just not query-level.

---

## The headline: real progress since June 11, more than the prior audits show

This is the good news up front. Since the June 11 audit (which said schema was buggy, titles/metas unshipped, and the blog dead since Nov 2023), a lot actually shipped:

- **9 new blog posts published June 16 – Aug 11**, almost exactly matching the June 11 content plan: Boat Rides in Houston, Bachelorette Party Boat Guide, Things to Do in Kemah, Paddle Boat Houston, BYOB Boat Party, How Much Does It Cost, 4th of July Fireworks, Birthday Party on a Boat, Sunset Cruise Houston. Each one carries `Article` + `Organization` + `BreadcrumbList` schema, real word counts (~1,500+ words), and a working link back to the money page. This is the single biggest positive change and isn't mentioned in any prior audit.
- Homepage, money page, corporate, about, and contact **titles and meta descriptions are all live and match the June 12 rewrite** — the "Seakbrook" typo is gone, one clean H1 on every page checked.
- Homepage schema bugs are fixed: phone is `+1-832-974-0365` (no double-plus), `aggregateRating` (4.9/400) is present, `sameAs` links to FB/IG/Yelp/TripAdvisor are present, brand name/alternateName are correct.
- Money page (`/houston-party-barge-cruise/`) carries `Product` (2 offers) + `FAQPage` (6 Q&As) + `BreadcrumbList` — live and valid.
- Contact page carries `TouristAttraction` + `PostalAddress` (NAP schema).
- robots.txt allows all major AI crawlers and points to a valid sitemap index; sitemap URLs all return 200.

**Still open**, and this is where the fix list below focuses:
- **NAP address conflict is unresolved and now visibly worse.** The money page body text itself contains *both* addresses in different sentences (see Quick Win #1).
- About page: title/meta were rewritten, but the actual page body was never touched. It's still ~40 words, still says "Houston Pedal Barge" and "Cruise, pedal, and party," and has zero founding-year/guest-count/founder content — despite the meta description promising "the story behind..."
- Reviews page: still a bare "leave us a review" prompt, no testimonials, no `Review`/`AggregateRating` schema, title still says "Houston Pedal Barge Reviews."
- Corporate page: still no static pricing, group-size minimums, or testimonials in the actual page copy (the one `$55.00` on the page is a dynamic FareHarbor related-activity widget, not written content). Still only `BreadcrumbList` schema.
- llms.txt still opens with "pedal-powered party barge" and describes the money page as guests who "pedal along scenic waterways" — directly contradicts the June 7 brand decision to lead with Party Barge and stop foregrounding pedaling as a top objection-killer.
- 5 stale posts from 2022–2023 (including the untitled `/304/` orphan) are still live and still in the sitemap. None were 301'd or refreshed.
- `openingHoursSpecification` isn't in the homepage schema at all anymore (previously an empty array — now just absent). Still a gap either way.
- GA4 conversion wiring: can't verify from the client side whether it was completed (this requires GA4 admin access, not available here). No visible book-now conversion event fired in a page-source check, which suggests it may still be open, but this is not a definitive check — flag for a direct GA4 look next time that MCP exists.

---

## Quick Wins (do this week — all low effort, all still on the live site)

1. **Fix the NAP address conflict on the money page itself.** `/houston-party-barge-cruise/` currently states the dock address as **"2513 NASA Road 1, Seabrook, TX 77586"** twice in the body copy, and **"2515 E NASA Pkwy"** once, in the same page. Contact page and homepage schema both use 2515 E NASA Pkwy. This has been flagged since the June 11 audit and is now a live, on-page contradiction, not just a schema-vs-Yelp mismatch. Pick one (confirm with David/Connor which is correct — Yelp also says 2513 NASA Road 1) and make every mention on every page + all schema + GBP + Yelp match exactly. Impact: NAP inconsistency actively hurts local pack ranking and is a trivial fix once the correct address is confirmed.

2. **Rewrite the About page body copy** (`/about/`). Currently ~40 words of actual content: "Houston Pedal Barge offers private and public bike bar boat party tours and booze cruise boat rentals on Clear Lake... Cruise, pedal, and party on the water with 26 of your friends." The title/meta already promise "the story behind Houston's BYOB party boat" — the page needs to deliver that. Add founding year, guest-count-to-date, captain/crew credentials, and drop "Houston Pedal Barge" / "pedal" language per the June 7 brand decision. This page has real impression volume per the June 11 audit (9,173/90d) and is the biggest gap between what the snippet promises and what the page delivers.

3. **Fix the llms.txt framing.** It still opens "Houston Pedal Barge offers pedal-powered party barge and boat tour experiences" and describes the money page as guests who "pedal along scenic waterways." This is the exact framing the business decided to kill on June 7 because "do I have to pedal?" is a top objection. Rewrite the intro line and activity descriptions to lead with BYOB/party boat/captained, matching the on-site copy. Low effort, direct GEO impact since llms.txt is what AI crawlers read first.

4. **Build a real Reviews page.** `/houston-pedal-barge-reviews/` is still just a "review us on Google/TripAdvisor/Facebook/Yelp" prompt with no actual review content and no `Review`/`AggregateRating` schema — despite the homepage already having a legitimate 4.9/400 aggregate rating to draw from. Even 10-15 pulled testimonials with `Review` schema would give AI systems and Google something to cite. Also fix the page title, which still reads "Houston Pedal Barge Reviews" (old brand).

5. **301 or noindex the 5 stale blog posts still live and in the sitemap:** `/2022/02/17/why-pedal-barges-make-sense-for-partying/`, `/2023/11/28/304/` (untitled orphan), `/2023/11/29/unveiling-the-rich-tapestry-of-buffalo-bayou-a-journey-through-history/`, `/2023/11/29/unveiling-the-latest-party-boat-trends-making-waves-in-2024/`, `/2023/11/29/party-theme-ideas-for-your-houston-party-boat-extravaganza/`, `/2023/06/16/why-a-houston-pedal-barge-tour-on-fathers-day-is-a-great-gift/`. This was recommended in both June audits and nothing has changed. Redirect the thin/dated ones to the closest matching new post (e.g., the "2024 trends" post → the new Sunset Cruise or Boat Rides post) or to the money page; keep the Buffalo Bayou history piece only if it's rewritten to be evergreen and non-promotional-feeling.

---

## Strategic Work (this quarter)

1. **Rebuild the corporate/group page as an actual conversion page.** `/corporate-group-event/` still has no static pricing table, no written group-size minimums/maximums, and no testimonials in the body copy — the only dollar figure on the page is a dynamically-pulled FareHarbor widget price, not content. Add a real pricing table (per-person for 4-12, $920 private charter for 13-26 as noted in the May audit — confirm current price since the money page schema shows $800 for private now, so these two numbers disagree and need reconciling), what's-included checklist, and 3-5 named corporate testimonials. Add `Service` schema. This page has been flagged as the weakest-converting high-impression page in all three prior audits and nothing has shipped on it.

2. **Add `openingHoursSpecification` back into the homepage `LocalBusiness`/`TouristAttraction` schema** with real hours, and add `AggregateRating`/`Review` schema to the corporate and about pages once they're rebuilt. Also add `Service` schema to corporate and consider `FAQPage` on the new blog posts (they currently ship `Article` only — no FAQ blocks despite good length).

3. **Reconcile the private-charter price discrepancy.** Money-page schema shows a private offer at $800; the May audit's copy examples and the corporate page reference $920. Confirm the actual current price with FareHarbor and make sure schema, on-page copy, and the corporate page all agree — an AI citing the wrong price is worse than not citing a price at all.

4. **Verify GA4 conversion wiring directly** (needs GA4 access this vault's MCP set doesn't currently have). A client-side check found generic `gtag`/`dataLayer` calls but no distinguishable `book_now_click` or purchase-style event in the page source. Given the June 11 audit found **zero conversion events** in 21,000 sessions, this is very likely still open and remains the top blocker to knowing whether any of this SEO work is producing bookings.

5. **Comparison/pillar content is still the biggest content gap vs. competitors.** Gulf Coast Party Boats' homepage carries only generic `WebPage`/`WebSite` schema — HPB's schema stack (TouristAttraction + AggregateRating + Product + FAQPage on the money page) is now actually ahead of at least this one competitor. The gap that remains is content: no comparison page ("Houston Pedal Barge vs. Gulf Coast Party Boats," "vs. renting a yacht charter") and no Wikipedia/Reddit presence, both still untouched from the May plan. Worth reviving now that the blog cadence is proven to actually ship.

6. **Re-run PSI/Lighthouse and GSC once access allows.** Today's run hit a PSI quota wall (no API key configured) and this vault has no GSC MCP, so Core Web Vitals and query-level striking-distance data are both blind spots in this specific audit. Recommend: (a) add a `PSI_KEY` to `~/.claude/.env` so `~/Projects/tech-seo/psi-run.mjs` can run cleanly, and (b) decide whether to wire a GSC MCP into this vault the way other business vaults may have it, since three audits in a row have now had to lean on manually-pasted GSC tables from whoever ran them with browser access.

---

## Technical SEO checklist (verified live, 2026-08-15)

| Check | Status | Details |
|---|---|---|
| robots.txt | OK | Allows all major AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended not blocked); disallows a long list of low-value/aggressive scraper bots; points to valid sitemap |
| Sitemap | OK | Sitemap index → page/activity/post sitemaps, all return 200, all URLs in them return 200 (one 301 found: `/privacy-policy/` → `/privacy-statement-us/`, working as intended) |
| Redirect chains | OK | http→https and www→non-www each resolve in a single hop; no multi-hop chains found |
| Broken links | None found | Checked ~27 URLs pulled from homepage nav + all 3 sitemaps; all returned 200 except the one intentional redirect above |
| Canonical tags | OK | Correct non-www self-referencing canonical on homepage, money page, corporate, about, contact |
| H1 structure | OK | Exactly one H1 per page checked (the duplicate-H1 bug from June is fixed) |
| JSON-LD schema | Partial | Present and mostly valid on homepage, money page, contact; missing/thin on corporate, about, reviews (see fix list) |
| Core Web Vitals / Lighthouse | **Not measured** | PSI API returned 429 (quota exceeded), no API key configured. TTFB proxy only: homepage 0.57s, money page 1.34s (money page is the slowest of the four checked — worth a real Lighthouse pass) |
| GSC index status | **Not available** | No GSC MCP in this vault |
| Image alt text | OK | Only the 1x1 Facebook pixel tracking image lacks alt text (expected, non-issue) |
| Mixed content / HTTPS | OK | Site fully serves over HTTPS, no obvious mixed-content resources in the pages checked |

---

## Bottom line

The gap between "what the last audit recommended" and "what's actually live" closed significantly since June 11 — the blog cadence in particular went from zero to nine solid posts, which no prior audit anticipated. What's left open is consistent across all three prior audits and this one: the About page and Reviews page were never substantively rewritten (only their metadata was), the corporate page still isn't a real conversion page, the NAP conflict is unresolved and now visible on-page, and llms.txt still contradicts the brand's own June decision. None of these are big lifts — most are an afternoon each, same as the June 7 audit noted about the original five.
