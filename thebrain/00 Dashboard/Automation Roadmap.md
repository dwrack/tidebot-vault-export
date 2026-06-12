# Automation Roadmap — Loops, Learning, and What's Next

Updated 2026-06-12. Companion to the 6 loops now running. Each item below has a concrete implementation plan and reuses rails that already exist (roster JSON, Google token files, tidebot Slack posting, `claude -p` drafting, tick-to-approve vault docs, launchd).

## Now running (don't rebuild)

| Loop | Schedule | Output |
|---|---|---|
| review-watch | Mon 7:33a CT | 00 Dashboard/Reviews/ (reply drafts, worst-first) |
| ad-optimizer | Mon 7:48a CT | 00 Dashboard/Ad Optimizer/ (tick-to-approve changes) |
| seo-watch | Mon 6:07a CT | 00 Dashboard/SEO/ (striking-distance + topics) |
| opencx-watch | Daily 8:53a CT | Slack to managers + helm + 00 Dashboard/OpenCX/ |
| morning-brief | Daily 7:20a CT | Daily brief + Home.md refresh |
| life-ops | Sun 7:12p CT | 00 Dashboard/Weekly/ |

Plus the ~20 pre-existing jobs (adreport, fhscrape, GBP posters, IG DM worker, reddit-finder, publisher, token refresh, vault sync, graphify-DCKT).

---

## Tier 1 — Infrastructure that protects everything else

### 1. Token-health sentinel
**Why:** Meta refresher failed silently for 6 days in June; Gmail token died unnoticed. Every loop downstream goes blind when a credential dies.
**Build:** node script, daily 6:40a PT. For each credential make ONE cheap real call: every `~/.config/google/tokens/*.json` (tokeninfo), google-ads.yaml (one GAQL), META token (debug_token), each OPENCX_KEY (GET /org/), Slack bot (auth.test), SendGrid (GET /user/profile). Any failure → red line in helm Slack + Home.md banner + email. ~Half day. **S**

### 2. Job watchdog
**Why:** launchd jobs that error every run look "fine" (exit 0, no output check). The meta-refresh failure pattern.
**Build:** nightly node script with a manifest of every job → expected artifact (log line today, dated file, state mtime). Checks artifacts, not exit codes. Reports misses to helm. Manifest lives in one JSON so new jobs are one line. **S**

### 3. Booking-flow synthetic check
**Why:** FareHarbor widgets and sites break silently; a dead checkout costs a whole day's bookings.
**Build:** Playwright (already installed) daily: load each production domain (roster `gsc_site` + FH-active list), click through to the FH booking iframe, assert availability calendar renders. Screenshot on failure → helm alert. **M**

---

## Tier 2 — Crisis speed

### 4. Review crisis alarm
**Why:** HPB took 7 one-stars on June 6; weekly review-watch is too slow for that.
**Build:** strip review-watch down to a count-only daily run (no Claude): new reviews per location in last 24h; trigger = 2+ at ≤2 stars, or any review matching refund/chargeback/scam/police. Alert → helm + manager channel. Reuses review-watch state + token. **S**

### 5. Pixel pulse (FH Purchase bug tripwire)
**Why:** NOLA Swamp + DCKT pixels haven't fired Purchase since April (open FH ticket). The moment FH fixes it, the parked Meta ad sets can launch.
**Build:** daily python (reuse adreport rails): bookings yesterday per biz (FH mirror dir) vs pixel Purchase events (`{pixel}/stats`). bookings>0 + purchases=0 → still broken; first day it fires → green alert "pixel fixed, launch the ad sets." **S**

### 6. Chargeback/refund watch
**Why:** disputes follow bad weekends (HPB storm). Refund requests also sit in OpenCX (one from April still open at LSKT).
**Build:** extend opencx-watch money-regex to tag refund/dispute separately + scan FH charges data for refund spikes per biz per week. Alert at 2x baseline. **S**

---

## Tier 3 — OpenCX deeper (the handoff system, end to end)

opencx-watch now reports drops daily. These close the loop so drops stop happening:

### 7. KB auto-builder
**Why:** ~50% of handoffs are "insufficient_knowledge." Zero help-center articles loaded in any workspace. Every article kills a recurring handoff forever.
**Build:** monthly job: pull `/handoff-analytics/` reasons + handoff summaries per workspace, cluster themes via `claude -p`, draft 5-10 HC articles per workspace in brand voice → stage in vault for approval → on tick, POST to `/hc/`. Same approve-gate pattern as ad-optimizer. **M**

### 8. FareHarbor actions for the AI
**Why:** other ~50% of handoffs are "insufficient_tools" — the AI knew what to do but couldn't check availability or send a booking link. Each workspace has exactly 1 action configured.
**Build:** this is config work in OpenCX, not code: add "send booking link" + "check availability" actions per workspace (OpenCX actions can hit FH availability endpoints). One sitting with the OpenCX dashboard. Highest ROI per hour in this whole doc. **S**

### 9. Handoff lead rescue
**Why:** dropped handoffs contain names + phone numbers of people trying to spend money (52-guest event with a phone number sat 37 days at HPB).
**Build:** extend opencx-watch: extract contact info from money-flagged handoff summaries → staged SMS/email drafts (Twilio + business gmail, never GHL) in a vault doc → tick to send. Recover the backlog first, then it runs on new drops. **M**

### 10. SLA + CSAT actually configured
**Why:** zero SLA targets and zero CSAT collection in all 6 workspaces, so there's no "handoff answered within X hours" standard to alert on.
**Build:** set SLA in each workspace dashboard (e.g. first human response < 4 business hours), then opencx-watch adds `/sla/analytics` breaches to the daily manager post. CSAT on = free trend data for the weekly review. Config + 20 lines of code. **S**

### 11. Auto-stale-closer
**Why:** managers answer guests on Messenger directly but never close the OpenCX ticket, so the backlog number lies.
**Build:** weekly: tickets idle 30+ days get a draft "close as stale?" list in the manager's Slack post; one reaction (✅) from the manager closes them via API. Needs a small TideBot reaction handler, or simpler: auto-close 45d+ with a note, log everything. Start propose-only. **M**

---

## Tier 4 — Learning loops (systems that get smarter)

### 12. Ad-optimizer outcome scorecard
**Build:** apply.py already logs applied changes with timestamps. Add a 14-days-later job: re-pull the campaign metrics, write "what happened after each applied change" to the Ad Optimizer doc. Earns the right to schedule auto-apply. **S**

### 13. Review mining → guide scoreboard
**Build:** monthly: all reviews (review-watch already fetches them) → `claude -p` extracts guide names + sentiment + product complaints → per-business scoreboard in vault + manager Slack. Feeds TideBot coaching and staffing. **M**

### 14. GBP post performance learning
**Build:** monthly: `gbp_get_insights`/post metrics for the last 30 days of posts (both posters log exactly what was posted when) → which types/topics/CTAs drive actions → rewrite next month's calendar JSON with `claude -p`, staged for approval. **M**

### 15. IG content learning
**Build:** monthly `organic_top_content` per account → format/topic winners → brief for the content engine (currently paused pending strategists; this gives them a data pack on day one). **S**

---

## Tier 5 — Revenue loops

### 16. Empty-slot promo trigger
**Why:** unsold seats 48-72h out are pure perishable inventory. BBK books same-day; perfect target.
**Build:** daily: FH availability/manifest (mirror dir) 2-3 days out per biz → occupancy below threshold → auto-stage a promo bundle (GBP post via existing poster, IG story draft, SMS blast draft to past local customers via Twilio) → tick to fire. Start with BBK + HPB. **L**

### 17. Smart review-request engine
**Why:** review velocity is the #1 GBP ranking lever and some listings are in a drought (Hidden Adventure).
**Build:** daily: yesterday's completed bookings (FH mirror) → SMS/email review ask with direct GBP review link, throttled (max N/day per listing), skip customers with OpenCX angry sessions. Twilio + business gmail. Needs your sign-off on the message template once. **M**

### 18. Win-back email engine
**Why:** 136k past customers, zero re-contact since the Meta audience upload.
**Build:** seasonal: segment per business (last tour date, season, party size, from `~/Projects/customer-audiences` data) → `claude -p` drafts campaign in brand voice → batch send via SES us-west-2 (production access, verified) with per-batch approval. Start DCKT (season starting). **M**

### 19. Weather-aware ops
**Build:** daily: NWS API forecast per city (free) → washout-risk flag per tour day → manager Slack heads-up + suggested ad pause for washout days (proposal in Ad Optimizer doc, not auto-pause). **M**

### 20. Lead-time-aware ad pacing
**Build:** weekly: per-biz booking lead-time curve (FareHarbor Reports data in each vault) vs current spend pacing → budget shift proposals into the existing ad-optimizer tick-to-approve doc. DCKT books 45d out, BBK same-day; spend timing should differ. **M**

---

## Tier 6 — Smaller but worth doing

- **21. GBP Q&A responder** — weekly, `gbp_list_questions` → draft answers → tick to post via `gbp_answer_question`. Clone of review-watch. **S**
- **22. Review-reply auto-poster** — extend review-watch with the same tick-to-approve gate: approved drafts post via the GBP reply API instead of copy/paste. **S**
- **23. Competitor pulse** — monthly snapshot of nemesis brands' GBP rating/review velocity (public data, Places API) → trend table feeding the Brand Nemesis Framework. **M**
- **24. AEO citation check** — monthly: ask ChatGPT/Perplexity/Claude "best kayak tour in [city]" via API, log who gets named → tracker per brand (E&E already has the tracker doc format). **M**
- **25. Social gap detector** — weekly: any business with no IG post in 7+ days → nudge in helm. Uses `organic_ig_posts`. **S**
- **26. Labor report portfolio-wide** — clone dckt labor-report for the other FH businesses. **M**
- **27. FH EOD charges first-pass** — automate the crew-pass of the daily charges review; you keep the manager pass. **M**
- **28. Insurance/renewal tracker** — vault doc of policies + dates (NBB insurance is the live one) → 30/7-day reminders. **S**
- **29. Graphify all business vaults** — clone the DCKT nightly job per vault, or one job iterating vaults. **S**
- **30. Morning-brief cross-wiring** — pulse table picks up opencx-watch dropped count, ad-optimizer pending count, token-sentinel status. One prompt edit in the skill. **S**

---

## Suggested build order

1. **#1 + #2 sentinel & watchdog** — protects all 29 jobs, would have caught both June failures
2. **#8 FareHarbor actions in OpenCX** — config-only, kills ~half of future handoffs
3. **#4 review crisis alarm** — June 6 already proved the cost
4. **#9 handoff lead rescue** — there's real money sitting in the current backlog
5. **#17 review-request engine** — compounding GBP ranking asset
6. **#12 outcome scorecard** — unlocks scheduled auto-apply for ads

Effort key: S = under a day, M = 1-2 days, L = several days.
