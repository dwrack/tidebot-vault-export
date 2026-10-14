# Website Rebuild: Round 1 Feedback (Jonah, Oct 13 2026)

Jonah's response to the three iPhone homepages on the Oct 10 canvas (https://claude.ai/artifact/YCeQxCTJbCNiASWciHcVeg): A Social Ember, B River Hour, C Pull the Cord. Forwarded by Davey 2026-10-13. Governs round 2.

## Direction
- **Base = A (Social Ember)**, plus two pieces from the others: the 7-day "Pick your sky" list from B and the 3-step "How it goes" from C.
- Mock up the **desktop version of each page**, not just iPhone.

## Changes before building
1. Swap the Airstream "coming soon" block for the **two new private saunas** (they launch first).
2. New names: **Community Sauna**, **Private Party** (the whole big sauna), **Private Sauna 1** and **Private Sauna 2**.
3. **Prices are placeholders** until the pricing revamp is final (#pricing-revamp, Jonah's 10/12 grid).
4. **Email alerts instead of texts** for now.
5. **Lead with the river.** Nobody else in Portland has the Columbia as their cold plunge, so B's "THE COLUMBIA, WARMED." is the headline. Somewhere on the page say **we're docked** (people read "floating" as cruising).

## For the build
- Load [[Website Build Brief (Jonah, Oct 2026)]] + Jess's style guide at the start; check the work against both before showing Davey/Jonah.
- **No health claims**, and nothing that sounds like someone is there looking after guests.
- Show the **exact price, and whether it repeats, right above the Book or Join button**.
- **Track bookings through to Periode** so the ~$900/month Google Ads spend is attributable (GA4 + the Periode tracking bridge, see [[reference_periode_tracking_bridge]] / build spec #6).

## Process
- Live seat counts need **L to connect Periode**; Jonah loops her in.
- **L and Jonah review each round before anything goes live.**

## Decisions (Davey, 2026-10-13)
- Use **Community Sauna** as Jonah asked. Sunrise and Moonlight stay as session times under it. Do not rename in Periode / Ads / GBP until Jonah confirms.
- Desktop this round = **homepage only**.
- **One working artifact only:** https://claude.ai/artifact/YCeQxCTJbCNiASWciHcVeg. Deleted: Dusk, Daybreak, River Ritual, Redesign (copies in `Website Rebuild — Prototypes (Aug 2026)/`) and Style Atlas (copy in `Website Rebuild — Style Atlas (Oct 12 2026)/`).
- "Jess's style guide" = Brand Identity Packet + Jess's Website Audit. Summary: [[E&E Style Guide (Brand Packet + Jess Audit)]].

## Version log
Every publish carries a version label in the canvas history. The canvas also has a Version Log sticky.

| Version | Date | What changed |
|---|---|---|
| R1 | 2026-10-10 | Three iPhone directions (A Social Ember, B River Hour, C Pull the Cord) |
| R2.1 | 2026-10-13 | A's layout + B's Pick Your Sky + C's How It Goes; desktop board; river headline; docked callout; new names; Private Saunas 1+2 replace Airstream; email alerts; price + repeat line above every Book/Join; brand packet palette + Basal/Inter; no health or attendant wording |
| R2.2 | 2026-10-13 | Private Saunas 1+2 = 2 to 4 people, 1 hr 45 (Davey). All price lines moved to Jonah's 10/12 #pricing-revamp model (still placeholders, feedback due Fri 10/16): weekday 1 hr $35 / 2 hr $50, weekend 1 hr 45 $60, Private Party up to 12 $500/$600, small saunas $200/$250, memberships Weekday $100 / Anytime $150. Sunrise/Moonlight line removed (folded into weekday hour). |

## R2.1 check against brief + style guide (2026-10-13)
- Type sizes all on scale (12/14/16/20/25/31/39/49/61/76). Body 16, line-height 1.5, headings 1.1-1.25.
- Spacing all on the 4/8 scale. Buttons and inputs 48px. Two radii (12 components, 24 containers).
- Colors only from the packet (plus two derived neutrals #2C2C2A / #3A3A37 and white inputs). One accent: copper.
- No health or attendant wording found. "Docked" appears in the hero and footer. No SMS.
- Every Book / Join / notify button has the price and repeat line directly above it. The header Book button only scrolls to sessions.
- Not yet: real prices, weather, river temp, seat counts, V2 photos, capacity, opening date, membership tier. All shown as [brackets].
- Pre-launch checklist (privacy, 404, sitemap, analytics, spam protection, etc.) applies at build, not mockup.

## Community Sauna rename: search check (DataForSEO, 2026-10-13)
| Term | Oregon / mo | US / mo |
|---|---|---|
| social sauna | 10 | 170 |
| community sauna | 10 | 170 |
| public sauna | 30 | 4,400 |
| sauna portland | 1,300 | |
Neither name carries search traffic. The rename is a clarity and brand call, not an SEO one.

## "No texts" (Jonah item 4)
**Decided 2026-10-13:** Davey agrees. Email only on the site; the R1 text signups were overboard.
Refers to R1 boards A ("Text me when it's pouring" phone signup) and C ("Last seats tonight? We'll text"). Marketing texts need the Twilio A2P 10DLC campaign approved; last known status IN_PROGRESS (resubmitted 2026-06-03, unverified since). Jonah's own 10/12 pricing plan relies on texts too (day-10 first-timer nudge, 14-day member nudge), so the same approval gates both.
