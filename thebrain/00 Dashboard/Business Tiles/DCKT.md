---
business: DCKT
display_name: Door County Kayak Tours
city: Door County
bookings_today: 0
revenue_today: 0
lead_time_days: 0
ad_spend_yday: 38
status: yellow
alert: "data stale — FH scrape missing (2SV re-approval needed); 10 unreplied reviews unchanged, 16 days, against DCKT's own 48hr SLA"
updated: 2026-09-03
tile_type: business
goal_q4_metric: weekly_booked_revenue
goal_q4_target: 7000
goal_q4_baseline: 7000
goal_q4_note: "Hold through season close. Fix the long-transit route by Oct 15 and restore a 48-hour review reply SLA."
goal_q4_horizon: 2026-09-01/2026-11-30
---

<!-- live:start -->
- **Goal pace: unavailable this run.** FareHarbor's scrape has now failed 2 of the last 3 days for this business (timeout, not malformed data) — most recent valid point is Sep 1, now 2 days stale. Last known trailing pace: 112% of goal as of Sep 1. The root cause is identified: the DCKT Labor Bot's own EOD email says FareHarbor revenue is stale because a 2SV re-approval is needed — run `cd ~/Projects/fareharbor-brief && FH_HEADED=1 node scrape.js --setup`. See today's brief Action Item #4.
- **Review-reply backlog unchanged at 10, now 16 days old (Aug 18 → Sep 1) — zero replies went out overnight** while NPB and NKST both cleared their backlogs same-day. This is the business whose own goal note calls for a "48-hour review reply SLA" — that SLA has now run 8x over. [Reply here](https://business.google.com/n/5837086547118336383/reviews/Ci9DQUlRQUNvZENodHljRjlvT21KUllVdHNORnA2YjFwUE1UZDJORE4zYW5rMVdFRRAB).
- **Google Ads yesterday: $31.73 spend, 25 clicks, 2 tracked conversions, $42.20 value, 1.33 ROAS.** 7-day: $200.49 / 18 conv / 2.54 ROAS — holding roughly steady.
- **Meta (act_10153674414451399): $5.85 yesterday**, one retargeting campaign, no purchase action logged.
- **Labor for the day that did run: $486.86 labor cost, 26.9 hrs, 4 on shift** (per the DCKT Labor Bot) — operations are fine, this is a data-pipeline and review-reply problem, not an ops problem.
- GSC: "door county kayak tours" #8.3 / 34 clicks off 116 impressions — brand term climbing (was #8.7/30 clicks Sep 2), real movement.
<!-- live:end -->

## Quick links
- FareHarbor: [doorcountykayaktours](https://fareharbor.com/embeds/book/doorcountykayaktours/)
- GBP location: 5837086547118336383
- Site: https://www.doorcountykayaktours.com/
