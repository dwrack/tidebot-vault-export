# BBK SEO/AEO/GEO Audit — Pass 6, 2026-08-16 (verification-only vs. Pass 5, 2026-08-15 23:21)

**STAGED — PENDING DAVID'S APPROVAL — 2026-08-16**

**REPORT ONLY. Nothing changed live on the site, WordPress, GBP, or any ad account.**

## Why this is short

Pass 5 was finished at 23:21 on 2026-08-15, roughly 3 hours before this pass started. A full `/seo-audit` + `/tech-seo` re-run right now would be near-total duplication of Pass 5 — nothing material has changed. This pass exists to independently verify that claim rather than skip it silently, and to flag the one thing that did change (a speculative note in Pass 5 that turned out wrong).

## What was independently re-checked

1. **GSC/GA4 MCP access — still absent, now confirmed from a second, independent session.** `.mcp.json` lists only `gmail-bbk`, `gbp`, `meta-organic`, `playwright`, `opencx`, `clarity`. A fresh ToolSearch for "search console," "GA4/analytics," and "GSC PageSpeed Insights" surfaced nothing beyond generic `WebSearch`/`WebFetch`. This is no longer just "Pass 5 said so" — it's been confirmed twice, from two separate sessions, same result. **This is a real environment gap, not a one-off fluke.** The fix is still: find out which Google account owns the `google-site-verification` tag (`ZTdimCkZr-kTmPpOzczYnKjJzsqLccPSKlkof0W0bU4`) and get GSC/GA4 access wired in.
2. **Live site — unchanged.** `post-sitemap.xml` still 11 posts, same Nov 2023 dates. `robots.txt` still has the same two orphaned `Disallow:` lines outside any named user-agent block. Homepage `google-site-verification` tag unchanged. No new posts published, no pricing/schema changes.
3. **PageSpeed Insights — one correction to Pass 5.** Pass 5 speculated the daily quota exhaustion might reset overnight. It didn't — direct curl against the keyless PSI v5 endpoint still returns `429 RESOURCE_EXHAUSTED` as of 2026-08-16. `node`/`nodejs` is also still missing from PATH, so the dedicated `~/Projects/tech-seo/psi-run.mjs` runner still can't execute either. Net effect: **zero Core Web Vitals/Lighthouse data for BBK across 6 checks now, 2 days running.** If David wants this unblocked, it needs a working Node.js install in this environment plus a `PSI_KEY`, not just a retry.
4. **No new SEO/keyword docs appeared** in the Marketing folder since Pass 5 beyond the routine ad-research/Meta Ads passes (unrelated to SEO) already logged.

## Fix list — unchanged from Pass 5, still the live priorities

Nothing below is new. See Pass 5 for the full write-up and reasoning; repeating headlines only so this doc stands alone:

**Quick wins:** publish the bat bridge blog draft first (peak season, still unpublished), then the other 14 staged drafts in Pass 5's priority order; add "From the Blog" internal links between the bat tour page / corporate-events page and their matching drafts; chase down who owns the `google-site-verification` tag; clean up the two orphaned `robots.txt` `Disallow:` lines; stop retrying the htowndads.com fetch programmatically (confirmed 3 ways it's a bot-detection wall, needs a human to check in-browser); confirm paddlingmag.com/Houstonia outreach green-light with David.

**Strategic:** set a fixed publish cadence for the 15 staged drafts rather than pushing them all live at once; run the 3 remaining June drafts through `/content-gate`; merge the alligator-safety draft into the existing 2023 pillar post rather than publishing it standalone; send the paddlingmag.com/Houstonia outreach (signed Connor Champaign, never David, per CLAUDE.md); merge the 8 thin history posts into one pillar with 301s; get Node.js + `PSI_KEY` working in this environment; resolve GSC/GA4/GBP access — still the single most-repeated blocker across 6 passes now.

## Recommendation for future passes

At this cadence (6 SEO passes across ~24 hours with no live-site changes and no new data source), further same-day passes have very low marginal value until one of two things happens: (a) someone publishes some of the 15 staged drafts, or (b) GSC/GA4/PSI access gets resolved. Suggest the next SEO pass be triggered by one of those events rather than a fixed schedule, or spaced at least a few days apart until there's new ground to cover.

---
*Verification-only pass. Did not re-run the full crawl, did not re-check paddlingmag/Houstonia (unchanged since Pass 3), did not evaluate brand-voice/factual content of the staged drafts. Did not touch the live site, WordPress, GBP, or any ad account.*
