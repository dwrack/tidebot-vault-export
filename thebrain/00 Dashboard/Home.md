# Davey Jones' Locker — Command Center

*Last refresh: 2026-09-20 (Total MCP outage — Gmail, GBP, Google Ads, Meta, GSC, and GA4 all failed on 3 separate attempts. General internet confirmed fine via direct curl/WebFetch, so this is the auth/server layer, not the network. FareHarbor's nightly scrape didn't run either — newest file is still 9/18 data. HPB's TikTok pull failed again on `ECONNREFUSED`, 3rd run in a row. No live numbers today; see [[Daily Briefings/2026-09-20|today's brief]] for the full outage writeup.)*

## Right now
- [[Daily Briefings/2026-09-19|Today's brief]]
- [[03 Projects/Active/Project Kanban|Project board]]
- [[Brand Gallery]]
- [[_Needs Attention]]

## Top 3 actions
<!-- top3:start -->
1. **Portfolio-wide — every authenticated data source is down at once.** Gmail, GBP, Google Ads, Meta, GSC, and GA4 all failed 3 straight attempts; FareHarbor's overnight scrape didn't run either. Run `claude mcp list` and check the scraper cron.
2. **HPB TikTok — 3rd consecutive failed pull.** Playwright still returns `ECONNREFUSED`. Needs a manual relaunch of the debug browser, not another retry.
3. **DCKT — carried forward, unconfirmed today.** Google Ads was dark for 9 straight days as of 9/18; likely day 10 now but can't be reverified until access is back.
<!-- top3:end -->

## Pulse — last 7 days
<!-- pulse:start -->
| Signal | Yesterday | 7-day avg | Δ |
|---|---|---|---|
| Gmail unread | — | — | — |
| Unreplied GBP reviews (all biz) | — | — | — |
| FH bookings (all biz) | — | — | — |
| FH revenue (all biz) | — | — | — |
| Total ad spend (G+M) | — | — | — |
| Total ad-attributed conversions | — | — | — |
<!-- pulse:end -->
*Total outage today — every authenticated data source (Gmail, GBP, Google Ads, Meta, GSC, GA4) failed on 3 separate attempts, and FareHarbor's nightly scrape didn't run. General internet confirmed fine (curl/WebFetch both worked instantly), so this sits at the MCP server/auth layer. HPB's TikTok pull failed again on `ECONNREFUSED`, 3rd run in a row. No `meta-organic` MCP connected this session either. Full writeup in today's brief.*

## Business tiles

![[Business Tiles/Tiles]]

## Recent briefings
<!-- briefs:start -->
- [[Daily Briefings/2026-09-20]] (today)
- [[Daily Briefings/2026-09-19]] (1 day ago)
- [[Daily Briefings/2026-09-18]] (2 days ago)
- [[Daily Briefings/2026-09-17]] (3 days ago)
- [[Daily Briefings/2026-09-16]] (4 days ago)
- [[Daily Briefings/2026-09-15]] (5 days ago)
- [[Daily Briefings/2026-09-14]] (6 days ago)
<!-- briefs:end -->

## Maps
- [[02 People]]
- [[03 Projects]]
- [[04 Finance]]
- [[Brand Nemesis Framework]]

<!-- ad-optimizer:start -->
> 📉 Ad Optimizer: 0 changes to approve, 9 advisories — see 00 Dashboard/Ad Optimizer
<!-- ad-optimizer:end -->
