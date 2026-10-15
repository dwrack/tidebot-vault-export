# Funnel Lab 03: Testing Infrastructure, what can split today

Verified 2026-10-14. Read-only audit: nothing deployed, committed, sent, or changed. Code sketches are in `03a Code Sketch/` (not installed anywhere).

**Bottom line:** almost nothing David owns can run a controlled split test today without a small build. The three native ones (Google Ads experiments, Meta A/B test, ActiveCampaign split) work but are starved for volume. The cheapest build that unlocks the most is two pieces that share one dependency: (1) variant assignment in `fh-lead-engine` (about 110 lines plus a 90-line report) and (2) one header script slot per FareHarbor site that loads our own `w.js` and `ab.js`. That covers email, popup, and on-site splits across 6 brands.

## 1. What can split today

"Can split" means: random assignment, sticky per person, outcome readable per variant.

| Surface | Can split today? | How | What is measured | Smallest build to fix |
|-|-|-|-|-|
| fh-lead-engine email drip (HPB enabled; npb, nkst, dckt, bbk, lskt built but `enabled:false`) | No | One copy path per step. No variant field, no assignment, `utm_content` is the step id only. | Nothing per variant. `sent[]` logs step ids. `status` booked/unsub exists. | `experiments.py` (48 lines, sketched), about 15 lines wiring, SES config set. See section 4. |
| fh-lead-engine popup (`w.js`) | No | One config per brand, served with `Cache-Control: public, max-age=300`, so a server-picked variant would be cached for everyone. GA4 events `lead_popup_view`, `lead_capture` only if gtag exists. | Submissions are stored; popup views are not stored server-side, so no denominator. | Client-side arm in widget (about 14 lines) plus a view beacon (about 18 lines). Also: the script is not on any site yet (see row 4). |
| SES sending itself (us-west-2, production, 62,500/day) | No native split | Raw MIME via `sesv2.send_email`. The Lambda env has no `SES_CONFIG_SET` (checked), so no open/click events are recorded at all for lead-engine or broadcast mail. | Delivery only, via account-level metrics. | Create config set + CloudWatch destination with message-tag dimensions. `nola-campaign` already does this (precedent), `hpb-campaign` has no event destination. 3 CLI commands plus `EmailTags` in `send_email` (6 lines). |
| FH WordPress sites with no GTM: nolapartybarges.com, neworleanskayakswamptours.com, houstonpedalbarge.com, lonestarkayaktours.com, austinkayaktours.com | No | GA4 loads straight from the FH theme (gated by Complianz). No Tag Manager. We cannot ship JS ourselves; FareHarbor controls the theme. Precedent that a custom head snippet is possible: lonestarkayaktours.com carries a Clarity snippet, and DCKT has an inline `gtag('config','AW-1070576804/...')`. Who edits that, and how, is unverified. | GA4 per-site property plus FH's network property `G-2CHJ9R6QSF` on every site. | One header line per site: `<script async src=".../ab.js?b=<brand>">`. ROLLOUT.md already waits on this same slot for `w.js`. Ask FH once for all five. |
| FH WordPress with GTM: doorcountykayaktours.com (GTM-PPSHWZB), buffalobayoukayak.com (GTM-TKMN5XSX) | Partial | GTM exists, so a Custom HTML tag can carry `ab.js`. Both containers currently hold no Custom HTML tags (read from public `gtm.js`, 2026-10-14). Who has publish access is unverified. | Same as above, plus GTM triggers. | Paste `ab_split.js` as a tag, add GA4 event tag, register 2 GA4 custom dimensions. About 30 minutes once access is confirmed. |
| Ebb & Ember, Squarespace (ebbandember.com) | Partial (can ship today, client-side only) | Footer Code Injection is already in use for the Periode attribution bridge, header for the DaySpa schema. `ab_split.js` can be appended to the Footer. No server-side option. | GA4 `G-YF8FPEWW4S`, Ads `AW-18333025587`, Meta pixel. Booking happens on Periode (server-side GA4/CAPI), so the clean outcome is the existing client-side `begin_checkout` ("Booking Start - Periode Click"). Per-variant paid bookings need the variant stapled onto the Periode link by the bridge (unverified that Periode keeps extra params). | Append snippet to Footer. Add the variant to the bridge's link decoration. Install Clarity (spec says to, zero matches in the HTML today). |
| Ebb & Ember Astro + Cloudflare Pages rebuild | Yes by design, not built | Spec item 6 says "cookie split at the edge, experiment_view and outcome events to GA4". Static pages make this easy: a Pages Functions middleware sets a cookie and serves `/b/...` or the base page, no flicker, no client-side swap. Booking is planned as our own flow with Periode only for payment, so we own the funnel events. | Whatever we instrument. | Nothing now. Build the middleware (about 25 lines) in the first sprint. Status: design direction picked 10/13 (A + B's Pick Your Sky + C's How It Goes), R2.1 on the artifact, build not started. |
| DCKT "find your fall ride" quiz (API Gateway + Lambda `dckt-quiz`) | Yes | The one live A/B in the portfolio. Cookie-sticky `random.choice("AB")`, `?v=A` or `?v=B` to force. A = email gate before result, B = result first. Per the memory note it went live 2026-10-14; I read the code, I did not hit the live URL (it would log a fake view). | Unique visitors per step per variant, two-proportion z-test in `quiz_stats.py`. | None. Reuse its pattern. |
| Microsoft Clarity | Partial | Segmenting by custom tag works (`clarity("set","exp_id","B")`, filter by tag in recordings and heatmaps). The tag is live on only one of 8 sites I checked. | Behavior (recordings, heatmaps), not conversion. | Install the tag everywhere via the same header slot or GTM. Fix the MCP (below). |
| Google Ads | Yes (native), low volume | Experiments (campaign-level A/B with traffic split) and ad variations; RSA asset reports. The `google-ads` MCP has `ads_query` and `ads_mutate`, so experiments can be read and, in principle, created via API. HPB account has 0 experiments (queried). | Clicks, CTR, conversions per arm, in Ads. | None for setup. Volume is the constraint, see section 2. |
| Meta Ads | Yes (native), UI only | Ads Manager "A/B test" splits audience exclusively. The `facebook` MCP has create/update for campaign, ad set, ad and creative, and insights, but no ad-study endpoint (checked tool list). | CTR, cost per result, per arm. | None. Run it in the UI. Only the Gravity/Admire account has enough volume (below). |
| ActiveCampaign (E&E sender since Aug 2026) | Partial, plan unverified | AC's campaign split testing and automation "split" action exist on its higher plans per AC's public docs; I did not log in, so David's tier is unknown. | Opens, clicks, per arm in AC. Opens are inflated by Apple Mail Privacy Protection. | Check the plan in AC. If it lacks split, assign by tag (hash of email, same function as the lead engine) and send two campaigns. |
| OpenCX bots (npb, nkst, dckt, hpb, bbk, lskt) | No native | MCP tools show workflows (`clone_workflow`, `activate_workflow`), AI profile, sequences, macros. No experiment or variant primitive. HPB has one active workflow, "Nudge unbooked inquiries" (5 nudges over 12 days, AI trigger). The widget script is on 6 FH sites, not on Austin or E&E. | Sessions, tags, handoffs, CSAT via `run_analytics_query`. | Pattern: clone workflow B, tag contacts A or B by email-hash parity, branch on the tag if the workflow editor allows it (unverified). Else alternate whole weeks ABAB. |
| FareHarbor checkout | No | No split testing in FH. Possible indirect arms: two items, two promo codes, two landing pages linking to different FH flows, UTM per variant. Booking export has `ref`, `email`, `item`, `gross`, `source` and no promo-code field (checked the jsonl schema), so a per-code readout needs FH's promo report. GA4 attribution is known to break through FH checkout (DCKT test 2026-05-12). | Bookings by email, item, ref string. | Pull bookings via the Public API (keys not created yet; `api-keys.json` absent, 2026-10-14) and match by email. |

## 2. Reality check: where the traffic is

Online bookings per day, 91 days ending Sep 29 (peak season), from the FareHarbor exports in `~/Projects/fareharbor-brief/data/bookings/` (non-cancelled, `source = online`):

| Brand | Online bookings/day | Distinct booker emails, all sources (91 d) |
|-|-|-|
| NOLA Party Barge (npb, the export is named neworleanspedalbarge) | 16.5 | 1,505 |
| DCKT | 10.8 | 1,137 |
| Lone Star | 6.1 | 600 |
| Buffalo Bayou | 2.7 | 284 |
| NKST | 1.8 | 182 |
| HPB | 1.7 | 150 |

Paid volume, last 30 days (to Oct 13):

| Account | Evidence | Verdict |
|-|-|-|
| Google Ads, Gravity Trails NOLA | NPB campaigns 30K to 40K impressions and about 1,100 to 1,400 clicks each, conversions 0 recorded on them; PMax 35K impressions, 33 conversions; pedal barge campaigns 16 and 64 conversions | CTR tests on the NPB ad groups are viable. Conversion tests are not. |
| Google Ads, Lone Star acct (also BBK, HPB) | 135 to 6,996 impressions per campaign, 1 to 34 conversions | CTR tests only on the two PMax campaigns. |
| Google Ads, Door County DeTours and HPB accounts | 0 impressions on enabled campaigns (DeTours); no enabled campaign with impressions (HPB) | Nothing to test. |
| Meta, Gravity/Admire | $4,555 spend, 389K impressions, 5.8K landing page views, 71 purchases | Only account with test-grade volume, and only for CTR or landing page views. 71 purchases cannot split into a powered purchase test. |
| Meta, Lone Star/Austin | $254, 1 purchase | Too small. |
| Meta, Buffalo Bayou | $899, 0 purchases | Too small. |
| Meta, DCKT | No spend in the window | Nothing. |

## 3. How every test is run (the protocol)

1. **One hypothesis, one change.** Write it as: "Changing X to Y will raise [one primary metric] from about P to about P x (1+L) for [audience] because [reason]." If you cannot name the reason, do not run it.
2. **Pick the metric before launch.** One primary (bookings, or the closest event we can attribute), two guardrails (unsubscribes, refund/cancel or revenue per lead). Opens are not a metric (Apple Mail Privacy Protection).
3. **Pre-compute the sample.** Run `python3 sample_size.py <baseline_pct> <lift_pct>`. If the answer exceeds 8 weeks of that surface's traffic, do not run it as written (section 3.3).
4. **Randomize by person, sticky.** Hash of email (email, lead engine) or first-party visitor id (site). Never alternate by day or by page unless nothing else is possible, because Saturday vs Tuesday alone swings bookings more than most copy tests.
5. **One live test per surface at a time.** Two tests on the same page contaminate each other.
6. **Check balance on day 2.** Arms should be within about 2% of each other once there are 1,000 exposures. If not, assignment is broken; stop and fix.
7. **Fixed end date, no peeking verdicts.** Run whole weeks (min 14 days, covers both weekend and weekday). Decide only at the planned sample, or at the planned stop date if traffic fell short.
8. **Log it** in `TheBrain/03 Projects/Active/Funnel Lab (Oct 2026)/` test log: hypothesis, dates, n per arm, result, decision, what changes permanently.
9. **Ship or kill.** Ship only if the primary beats at |z| > 1.96 and no guardrail moved against us. Otherwise "no evidence of difference" and keep the cheaper/simpler arm. A flat result is a result.

### 3.1 Sample size per arm

Two-sided two-proportion test, alpha 0.05, power 0.80. Calculator: `03a Code Sketch/sample_size.py` (pure stdlib; spot-check: 5% baseline, +20% lift gives 8,158 per arm, matching the standard tables).

```python
import math
from statistics import NormalDist
def n_per_arm(p1, rel_lift, alpha=0.05, power=0.80):
    p2 = p1 * (1 + rel_lift)
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)
```

| Baseline rate | +20% relative | +30% relative | +50% relative |
|-|-|-|-|
| 1% | 42,693 | 19,827 | 7,750 |
| 2% | 21,109 | 9,798 | 3,826 |
| 5% | 8,158 | 3,780 | 1,471 |
| 10% | 3,841 | 1,774 | 686 |

Numbers are sessions (or emails, or leads) **per arm**. Double them for the total.

**Rule of thumb that does not depend on the baseline:** you need roughly 415 conversions per arm to detect +20%, 190 for +30%, 75 for +50%. That is the number to compare with a brand's booking count.

Days to reach that, if a site-wide change touches all online bookings (peak-season rates from section 2, both arms combined):

| Brand | +20% (830 bookings) | +30% (380) | +50% (150) |
|-|-|-|-|
| NPB | 50 days | 23 | 9 |
| DCKT | 77 | 35 | 14 |
| Lone Star | 136 | 62 | 25 |
| Buffalo Bayou | 307 | 141 | 56 |
| NKST | 461 | 211 | 83 |
| HPB | 488 | 224 | 88 |

Read it plainly: a full-funnel booking test can finish in a season only on NPB and DCKT, and only for 30%+ lifts. Winter rates are lower, so these are floors.

### 3.2 Which metric you can afford

| Test type | Realistic primary metric | Why |
|-|-|-|
| Ad headline / creative | CTR (NPB ad groups, Gravity/Admire Meta) | Millions of impressions beat dozens of conversions. |
| Popup headline / offer | Popup view to email submit | Denominator is popup views, a few percent baseline, so 20% needs about 8K to 20K views per arm. Needs the view beacon. |
| Email subject / first paragraph | Click-through on the first link, then bookings as a guardrail | Click baselines of 5% to 15% need 1.7K to 8K sends per arm for +30% to +20%. Pool brands. |
| Landing page / hero | Click on Book button, then `view_book_form` | Far upstream of FH checkout, so we can measure it. Bookings per variant are not trustworthy through FH (GA4 loses attribution). |
| Offer ($25 vs bonus card) | Bookings by email match | Lead counts per brand are small. Pool and accept a 6-week test. |

### 3.3 When traffic is too low (most of the time)

Be honest about which of these you are doing; they answer different questions.

- **Make the swing bigger.** If a 20% lift is not reachable in 8 weeks, test a 50% idea (a different offer, a different page, not a different adjective). Section 3.1 says 50% needs a quarter of the traffic of 20%.
- **Pool across brands.** Same treatment on npb, nkst, dckt, bbk, lskt, hpb, analyzed together. Valid when the hypothesis is about the human (a subject style, an offer shape), not the place. Report per-brand only as a sanity check.
- **Move upstream.** Test on clicks, not bookings, and say so. Click lifts usually transfer to bookings but sometimes do not; keep a bookings guardrail even if underpowered.
- **Holdout for always-on programs.** For the drip, OpenCX nudges, retargeting: keep 10% of eligible people on no treatment and compare cumulative bookings per person over 4 to 8 weeks. This answers "is the program worth running at all", which is the more valuable question at our volume.
- **Sequential / Bayesian stop rule** when you must decide early: use a beta-binomial and stop only when P(B beats A) is above 95% and expected loss is below 0.2 percentage points, with a pre-set max date. Fewer days on average than fixed-horizon, more false wins; use it on reversible things (copy), never on pricing.
- **Bandit (Thompson sampling)** only for disposable, high-churn items where the cost of showing the weaker arm is small and you do not need to learn why: email subject lines, RSA headlines, social post hooks. Do not use it for insight tests, because it starves the loser and you never get a clean read.
- **Not acceptable:** before/after comparisons (Saturdays alone are about 43% of NPB boat bookings, per the broadcast copy notes; season and weather swamp any copy effect), and alternating days.

## 4. fh-lead-engine variant assignment, concrete spec

Facts (all read from `~/Projects/fh-lead-engine`, 2026-10-14):

- Stack: Lambda `fh-lead-api` (HTTP API, widget, capture, `/u`, `/booked`, `/broadcast`) and `fh-lead-runner` (EventBridge every 15 min), DynamoDB `fh-leads` (4 items now), SES us-west-2 (production, quota 62,500/day, 0 sent last 24 h), SMS off.
- Email: `common.send_email` builds raw MIME with one-click `List-Unsubscribe`, no config set, no tags. Unsubs are per brand.
- Brands: `hpb` enabled (wave CREW25, expires 2026-10-31); `npb`, `nkst`, `dckt`, `bbk`, `lskt` have copy fallback `generic` and are `enabled:false` with no waves. The widget script is not on any brand homepage today.
- Conversion hook exists: `POST /booked` (admin key) flips `status` to `booked` and stamps `booked_ts`, and the runner stops sending. The booking sync that calls it is not built.
- Data available for matching: FH export rows carry `email`, `created_at`, `gross`, `item`, `ref`. No promo-code field.

### Data fields

| Where | Field | Value |
|-|-|-|
| lead item | `variants` | map `{exp_id: "A" or "B"}`, written once at capture |
| lead item | `popup_v` | arm the visitor saw in the popup (from widget) |
| `sent[]` entry | `v` | `"exp_id.arm"` for steps touched by a test |
| email links | `utm_term` | `exp_id.arm` (GA4 session term; keeps `utm_content` = step id) |
| SES | message tags `exp`, `arm`, `brand` | enables per-arm CloudWatch metrics |
| counter items | pk `exp#brand#exp_id#arm`, attrs `views`, `leads` | popup denominators via atomic `ADD` (no status, so they never enter the `due-index` GSI) |

### Assignment rule

`arm = B if int(sha256(exp_id + "|" + email)[:8], 16) % 1000 < split * 1000 else A`. Deterministic, so no stored state is needed to recompute, resubmits cannot flip it, 20,000 simulated emails gave 51.1% B. Only leads created at or after `start` are enrolled, so an experiment never changes a flow already underway. One live experiment per brand per step.

Popup arms are chosen in the browser (cached `w.js`, so the server cannot choose): `localStorage fhlead_<brand>_v`, random 50/50, sent with the lead as `popup_v`, and a `POST /e` beacon on popup show increments `views`.

### Where the code goes

| File | Change | Lines |
|-|-|-|
| `engine/experiments.py` (new) | `EXPERIMENTS`, `assign`, `enroll`, `apply` | 48 (sketched) |
| `api.py` capture | `lead["variants"] = experiments.enroll(bk, email)`; read `popup_v` | 3 |
| `api.py` | `/e` beacon route with `ADD` counters | 18 |
| `api.py` widget cfg | pass `variants` copy per arm | 6 |
| `templates.py` `_pack` | call `experiments.apply`, pass tag to `utm` | 6 |
| `common.py` `utm`, `send_email` | `utm_term`; `EmailTags` + config set | 10 |
| `runner.py` | `rec["v"] = tag` | 2 |
| `widget.js` | pick arm, send `popup_v`, fire beacon | 14 |
| `deploy.sh` | add `SES_CONFIG_SET` to env | 1 |
| SES | config set `fh-lead-engine` + CloudWatch destination (dimensions from message tags, same pattern as `nola-campaign`) | 3 CLI commands |
| `experiments_report.py` (new, outside the Lambda) | per-arm readout | 90 (sketched) |

About 110 lines in the engine plus the report, half a day including a `success@simulator.amazonses.com` test run.

### How results are read

`python3 experiments_report.py <brand booking export.jsonl>`: scans `fh-leads`, groups by brand, experiment, arm, and counts a lead as converted if `status = booked` or the lead's email shows up in a non-cancelled booking created after the lead. Prints leads, booked rate, unsubs, revenue per lead, and a z-score per brand. Match-by-email undercounts both arms equally (people book with a different address), so it is fine for comparison and wrong as an absolute rate. Clicks come from GA4 by `utm_term`; SES opens are shown but never used.

Limits to state up front: a single brand's drip cannot power a booking-rate test (HPB books 1.7 per day); email tests must be pooled across brands, and the fastest honest outcome is click-through plus a bookings guardrail. Do not test the offer itself until the FH promo report is wired, because the export cannot say which code was used.

## 5. Client-side splits on the FH WordPress sites

Sketch: `03a Code Sketch/ab_split.js` (about 60 lines, syntax-checked with node, not run in a browser).

**How it behaves**
- First-party `localStorage` id (`fl_uid`), arm = FNV hash of `uid|experiment`, so every page agrees without a cookie per test.
- A short `visibility:hidden` guard (600 ms max) on only the element being changed avoids A flashing before B.
- On first exposure per session it fires `experiment_view {experiment_id, variant_id}` to `dataLayer`, to `gtag` as an event plus a user property, and to Clarity as a custom tag.
- `?fl=B` previews an arm, `?fl=off` permanently excludes the device (use it on staff phones), headless browsers are excluded.

**Install paths**

| Site | Path |
|-|-|
| DCKT, BBK | GTM Custom HTML tag, trigger Initialization (All Pages), then a GA4 Event tag on a Custom Event `experiment_view` with data layer variables `experiment_id`, `variant_id`. |
| NPB, NKST, HPB, Lone Star, Austin | One `<script async src="{API}/ab.js?b=<brand>">` line in the FH header slot, the same ask as `w.js`. Serve `ab.js` from the existing API Gateway (about 8 lines in `api.py`) so edits never need FH again. |
| E&E Squarespace | Append to the Footer injection after the Periode bridge. |
| E&E Astro | Skip the snippet; do it in the middleware. |

**One-time setup per GA4 property:** register `experiment_id` and `variant_id` as event-scoped custom dimensions (Admin, Custom definitions). They only populate after registration and are not backfilled.

**Gotchas I found**
- Complianz gates the GA and GTM scripts on every FH site (`type="text/plain"`), consent mode is `optout`, region `us`. In the US they run by default, so exposure is nearly everyone; a visitor who declines is excluded from both arms equally.
- GA4 loses source attribution through the FH checkout (DCKT test 2026-05-12). Treat on-site tests as ending at the Book click or `view_book_form`. Whether a user property set before checkout survives to the `purchase` event is untested; first experiment should be a test booking watched in GA4 DebugView.
- Mixpanel is also loaded by the FH theme on every site; it is FH's, not ours.

## 6. Measurement tooling status

| Item | Status (2026-10-14) |
|-|-|
| Clarity tag in homepage HTML | Found only on lonestarkayaktours.com (project id `s0h05r8fe6`). Not found on npb, nkst, dckt, hpb, bbk, akt, E&E, and not in either GTM container. |
| Clarity MCP project map | Lists 12 projects (npb, nkst, bbk, akt, hpb, dckt, nbb, ee, admire, dcd, hat, cck) but `s0h05r8fe6` is not among them. Every MCP call returned code 100 ("Error while retrieving data") for 4 projects I tried. `~/.config/clarity/session.json` is dated Jun 28, so the scraped session has probably expired (`node ~/.claude/mcp-servers/clarity/refresh-session.js`). Unverified whether projects exist or have data. |
| GA4 per site (from HTML) | npb `G-XXFJS3P16F`, nkst `G-MXM09J7C5Y`, dckt via GTM `G-MST0ZQM37C`, akt `G-3GN0411YKL`, hpb `G-GEW708KE42`, bbk `G-9J1S6JCPVY` and `G-CGV97LY2NK`, lskt `G-K04SMMHZ0Q`, E&E `G-YF8FPEWW4S`. All FH sites also carry the network property `G-2CHJ9R6QSF`. |
| Meta pixel | On all but austinkayaktours.com. HPB and Lone Star share pixel `1559188957448084`. |

## 7. Domains checked

| Domain | Result | Notes |
|-|-|-|
| nolapartybarges.com | 200 | The real NPB site (matches `brands.json`). |
| nolapartybarge.com (singular) | 403 | Not the site. Do not use. |
| neworleanskayakswamptours.com | 200 | NKST. |
| doorcountykayaktours.com | 200 (redirects to www) | DCKT, GTM. |
| ebbandember.com | 200 (redirects to www) | Squarespace. |
| austinkayaktours.com | 200 (www) | Books through the Lone Star FH shortname; no Meta pixel; no OpenCX. |
| houstonpedalbarge.com | 200 | HPB. This is the live site; the lead engine sends as "Houston Party Barge". |
| houstonpartybarge.com | 200 | Squarespace "Coming Soon" parking page, not a site. |
| buffalobayoukayak.com | 200 | BBK, GTM. |
| lonestarkayaktours.com | 200 | Lone Star, only site with Clarity. |

## 8. Build order (cheapest first)

1. **Ask FH for one header slot on all five non-GTM sites** (and confirm who can publish the DCKT and BBK containers). Costs an email. Unblocks popup, on-site splits, and Clarity at once.
2. **Lead-engine experiments + SES config set** (section 4). Half a day. First test: pooled welcome-email subject line across brands, measured on clicks with unsub and bookings as guardrails.
3. **E&E Footer: Clarity + `ab_split.js` + variant on the Periode links.** About an hour. First test: Book button label, measured on `begin_checkout`.
4. **Fix the Clarity MCP session and create the missing projects.**
5. **Google Ads CTR test on the two NPB campaigns and one Meta creative test on Gravity/Admire.** No build, volume is adequate for CTR only.
6. **FH Public API keys + `/booked` sync** (already on the ROLLOUT list). Turns every email test into a bookings readout.
7. **Edge split middleware** when the Astro build starts.

## Not verified

- Who can edit FareHarbor theme head code, and how fast.
- GTM publish access for DCKT and BBK.
- ActiveCampaign plan tier and its split-test availability.
- Whether Periode preserves extra query params on its minside links.
- Whether an OpenCX workflow can branch on a contact tag.
- Whether a GA4 user property set pre-checkout reaches the FH `purchase` event.
- Clarity project health (MCP session dead).
- Google Ads experiment creation behavior through `ads_mutate`; I only ran reads.
