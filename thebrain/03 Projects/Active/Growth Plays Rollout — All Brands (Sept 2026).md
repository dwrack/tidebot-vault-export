# Growth Plays Rollout — All Brands (Sept 2026)

Ranked most needle-moving to least. Source bank: [[Marketing Ideas (Tom Orbach) — Tour Business Swipe File (Sept 2026)]]. Skill: `/growth-plays` (loads this file, routes a play to a brand, updates status below).

Ranking logic: direct revenue on existing traffic/spend first, then rebook/referral, then top-of-funnel buzz. Low effort beats high effort at equal impact. Every play is approval-gated before anything outbound.

Brand codes: NPB (NOLA Party Barge), NKST (NOLA Kayak Swamp Tours), DCKT (Door County Kayak Tours + Ebike + Airstream Sauna), E&E (Ebb & Ember, Portland, Période not FH), LSKT (Austin/Lone Star Kayak), HPB (Houston Pedal Barge), BBK (Buffalo Bayou Kayak). Sibling/SEO brands (Admire NOLA, Honey Island, Crescent City Kayak, Austin Paddle Shack, DC Detours, Hidden Adventure, Tiki Boats, Booze Cruises) inherit plays 5, 6, 8, 10 through their sites and content only. NOLA Bike Bar is excluded until revive-or-sell is decided.

Owners: Jeffrey Chitek (NOLA), Connor Champaign (TX, batch asks only, never drip), David + Claude (DC, E&E, all sites/email/ads).

---

## The ranked list

| Rank | Play | Why it moves the needle | Brands | Effort | Owner | Status |
|------|------|------------------------|--------|--------|-------|--------|
| 1 | Credit-over-refund on weather cancels | Keeps revenue that currently walks out the door. 30-65% of credits get spent. Every kayak brand weather-cancels. | NKST, DCKT, BBK, LSKT, NPB, HPB | Low | David/Claude (FH policy + OpenCX copy), managers execute | Two versions + live test drafted 2026-10-14 (Funnel Lab 10) |
| 2 | Dollar value on email/lead capture so ads optimize for it (added 2026-10-07) | Makes the ad spend already running buy cheaper leads, not just clicks. Fire a Lead event with value = lead-to-book rate x avg booking (NPB 2025 boats: $224/booking). Meta and Google bid toward it. | NPB first, then every brand with a pixel | Low-Med | Claude (pixel/GA4 + Google Ads conversion value) | Not started |
| 3 | Post-price opt-in + nurture funnel: "$10 off your first trip," "text me when Saturdays open," or "win a private weekday party boat" (added 2026-10-19, 3rd arm 10-20) | Catches the shoppers who saw the price and left, without hiding prices. 3-tap capture in the OpenCX widget already on the sites, then 4-5 touches timed to their trip date, FH `ref=` links. Makes play #2 possible (gives it leads and a lead-to-book rate). Absorbs the maybe-later capture from #20. Spec: `03 Projects/Active/Post-Price Opt-In Funnel — All Brands (Oct 2026).md`. | NPB pilot, then HPB, NKST, BBK, AKT; DCKT 2027; E&E via Période | Med | Claude builds + drafts, David approves copy and offer | Spec staged 2026-10-19. Tool corrected 10-22: existing fh-lead-engine (newsletter mode, no codes), NOT Mautic. NPB's live early-access bar still feeds a dead GHL form. Still blocked on A2P marketing check + SES complaint rate |
| 4 | "How did you hear about us?" on every FH checkout (added 2026-10-08) | GA last-click hides social: Onera saw <2% social in GA vs 60%+ in guest surveys, one Reel = $78k. Our NKST/DCKT purchase pixels don't even fire. Self-reported source tells us which content and ads actually book, so plays 2, 6 and the 532 content system get funded on evidence. | All FH brands; E&E via Période | Low | Claude drafts the FH custom field, David/managers turn it on | Two versions drafted 2026-10-14 (Funnel Lab 11) |
| 5 | Meta video-viewer retargeting pools (ThruPlay audiences) (added 2026-10-08) | Turns ad spend into a warm pool for pennies: Reel views run ~$0.01-0.05, then 50%/95% viewers get booking ads. No pixel needed to build the pool, so it works even where NKST/DCKT purchase pixels don't fire. | All brands with Meta spend (NPB, NKST, HPB, BBK, LSKT, DCKT next season, E&E) | Low | Claude builds campaign + audiences, David approves budget | Built into Funnel Lab test card 2, 2026-10-14 |
| 6 | Fake-choice question before the price shows (added 2026-10-13) | One question on the booking page before any price: 'What matters most today? A) the best slot and full experience B) the lowest price.' A self-selects into peak/private/upgrade, B assumes off-peak is the floor. The supplement brand that did it raised prices 30% and sold more. Page element only, no checkout change. | E&E first (peak vs off-peak exists), then NPB (private vs social cruise), NKST/DCKT (sunset vs midday) | Low | Claude drafts copy + page mock, David approves | Copy drafted in E&E pricing survey doc |
| 7 | Van Westendorp pricing survey for the banya launch + who-the-customer-is from reviews (added 2026-10-13) | Pricing is the biggest profit lever and the banya has no price yet. Four questions (too expensive / too cheap to trust / would have to think / bargain) to the E&E list, sliced by who-they-came-with and sauna habit. Review read already done: local Portlander, friend groups and families, celebrating, price never mentioned. | E&E list for the banya; rerun for any new product (NPB new boat, DCKT ebike/sauna) | Low | Claude drafts, David approves the send, Jonah sees results | Survey staged 2026-10-13 |
| 8 | Repeat-guest program: "Guest since," anniversary text, honoree post | Rebooks and referrals are the cheapest revenue. FH has the data already. Red Wing Wall of Honor. | All FH brands | Low-Med | Claude builds the FH pull, David approves sends | Not started |
| 9 | Honest-signal ad creatives: 1-star review ads | New angle into ad spend that's already running. Snowbird "Too advanced." | NKST, NPB, DCKT, HPB | Low | Claude via /ad-research + /ad-scripter | Night shift drafting lines 2026-10-15 (Funnel Lab) |
| 10 | Proof of humanity on every touchpoint | Conversion lift on existing traffic. Sites, OpenCX handoff copy, booking confirmations, footers. | All brands + sibling sites | Low | Claude, David approves copy | Not started |
| 11 | Instagram Close Friends as a private media list (added 2026-10-13) | Puresport pitched its launch to creators and press via a Close Friends Story series instead of email; the tactic became the coverage. Costs nothing, feels like an invite, works for every launch we have queued. | E&E (V2 saunas, banya), NPB (Tales 2027), DCKT (opening weekend), NKST | Low | Claude builds the list per brand, David/manager adds them, Claude drafts the Story series | Not started |
| 12 | Original data studies + journalist bait + Reddit search domination (upgraded 2026-10-21) | Journalists most want data. Our ~156k FH bookings (2019-2026) answer buyer questions nobody else can: how far ahead to book, what weather cancels trips. Recurring yearly reports re-earn links and AI citations. Never publish totals, revenue or declines. Plan: `03 Projects/Active/Original Research Studies — Link Earning Plan (Oct 2026).md`. | NPB (booking-window report) first, then all kayak brands (Rain Check), NKST/LSKT (wildlife logs), E&E (sauna survey) | Med | Claude computes + drafts via /press-release, David approves | 5 studies scoped 2026-10-21, lead-time numbers pulled; waiting on go for NPB study |
| 13 | Cancel-your-competitor offer from a guide's personal account | Converts high-intent shoppers already comparing. "Show me your airboat confirmation." Personal account, not brand. | NKST (vs airboats), NPB (vs big party boats), DCKT (vs Peninsula Kayak) | Low | Guide posts, David approves | Not started |
| 14 | Sponsored dock + boat naming partner (beverage brand, year-round) (added 2026-10-07) | New cash, not more bookings. ~19-25k boat guests a year who all have to buy their own drinks before boarding. Extends the Tales 2027 package to 12 months. Licensing caveats (no sampling while BYOB/unlicensed). | NPB (HPB later) | Med-High | David approves pricing, Jeff/JT walk-ins, Claude drafts | Pitch drafted 2026-10-07 |
| 15 | Shareable proof: name-first certificates, challenge coins, milestone leaderboards | Guests post their own name, not our logo. UGC without asking. | DCKT (Death's Door), NKST, BBK, LSKT | Low | Claude designs, dock prints | Not started |
| 16 | Be the contra/gifting sponsor at other people's events (added 2026-10-10) | Puts the brand in a room of exact-fit customers for the cost of a few comped sessions, and a gifting yes this year becomes a paid partner next year. Pitch a named person, one vivid "moment" (sauna/breathwork break, VIP gifting, presented-by boat ride), never price in the first email, follow up every 4 business days x3-5 in the same thread. Template: `03 Projects/IG Saved Ideas/Lead Magnets/Jess Williamson - Brand Sponsorship Guide (event sponsor pitch).pdf`. Also the playbook if a brand hosts its own ticketed event. Run it with `/event-sponsor`; pipeline in `Event Sponsorships — Tracker.md`. | E&E first (Portland wellness, founder, run-club events), then NPB/Admire NOLA (bachelorette + conference events) | Low | Claude drafts pitches, David approves | Not started |
| 17 | Branded awnings/boat canopies (added 2026-10-07) | Every guest photo and every passing boat carries the handle. One-time print cost. Doubles as sponsor inventory for play 10. | NPB, HPB | Low | JT gets quotes, Claude designs | Not started |
| 18 | Captain POV content (Meta smart glasses) (added 2026-10-07) | Hands-free footage every trip feeds the 532 content system without a deckhand filming. Needs a guest-consent line and no footage at the helm. | NPB, NKST (DCKT next season) | Low-Med | Jeff picks 1-2 captains, Claude edits | Not started |
| 19 | Anti-marketing stunt: "We spent the ad budget on ___" | One buzz post per brand per season. The post is the ad. | NPB (second-line band), DCKT (free trips for teachers), BBK (bayou cleanup) | Low-Med | David picks, Claude films/writes | Not started |
| 20 | Small conversion wins: maybe-later capture, footer content, off-hours upgrade, weather-triggered promo | Each is a few points on existing traffic. Bundle into one site sprint. | All sites | Low | Claude | Not started |
| 21 | Fans on board (guest comfort, added 2026-10-07) | Cheaper than a bad review. Heat is the summer complaint risk on covered boats. Ops, not marketing, so it sits low. | NPB, HPB | Low | Jeff/JT | Not started |
| 22 | Corporate/group social proof: "Booked every year since 2022," logos grouped by group type. LinkedIn corporate/retreat pitching lives in NPB 2027 Sponsorship + Events Plan, Track B | Private-events pages convert better with relevant proof. | NPB, HPB, BBK, DCKT | Low | Claude, managers supply names | Not started |
| 23 | Value recap email: "14 miles with us across 3 trips" | Season-end rebook nudge. Same data as play 5. | All FH brands | Low | Claude, after play 5 | Not started |
| 24 | April 1 "World's first ___ for ___" stunt | $0 viral shot. Wiz CISOtopia. One brand, one day. | NKST or NPB | Med | David + Claude, Q1 2027 build | Not started |
| 25 | Fake-mistake email | Works once or twice a year. Save for a real promo. | Any with a list | Low | Claude, gated | Parked |
| 26 | Free adjacent tool (water temp, gator activity, swamp weather page) | SEO asset that pulls to booking. Slow payoff. | NKST, DCKT | Med-High | Claude | Parked |
| 27 | Premium-positioning audit per brand: 5 levers (Specificity, Counterposition, 3% Rule, One Person, Veblen) (added 2026-10-16) | Most of our pages read generic and price off the competitor. Score each brand's hero page + top FH item on the five lenses, fix the weakest lever, then stage a premium/private anchor price. Feeds plays #5 and #6 with the positioning they need to hold. Run with `/premium-positioning`; theory in `06 Learning/Premium Brand Tactics — 5 Levers (byjoeym, Oct 2026).md`. | E&E and NPB first (private tiers already exist), then DCKT (Death's Door), NKST (vs airboats) | Low | Claude audits + drafts, David approves copy and any price | E&E homepage audited 2026-10-16: 3/10, Counterposition + One Person both 0; hero/session rewrite staged in `Ebb and Ember/Marketing/Premium Positioning — Homepage (Oct 2026).md`, David kept 'ritual' (2026-10-16), hero drafts reworked around the three phases with the river as the cold; waiting on hero pick |
**Planning frame (not a play):** set the revenue target per brand first, then work back to how many plays it takes to close the gap. NPB starting point: `FareHarbor Reports/Forecast — 2026-09-24.md` puts the next 90 days at $178k vs $264k same window last year (-33%).
---

## Phasing

**Now through Oct 31 (NOLA + TX in season, DC wrapping).**
- Play 1: write the credit policy and the OpenCX + FH cancellation copy. Roll to NKST and BBK first (most weather cancels), then everyone.
- Play 2 (new): put a dollar value on NPB lead capture (Meta Lead event + Google Ads conversion value). Need the lead-to-book rate from OpenCX/FH first.
- Play 3 (new): add a required "How did you hear about us?" dropdown to every FH item's checkout (Instagram, TikTok, Facebook, Google search, Google Maps, TripAdvisor, Viator/Expedia/GetYourGuide, friend/family, hotel/concierge, been before, other + "tell us more"). One FH setting per brand. Monthly tally per brand vs GA4.
- Play 4 (new): launch one ThruPlay Reel campaign ($5-10/day) for NPB as the test, build 50%/95% viewer audiences, then a retargeting booking ad set with Advantage+ audience off. Read cost per pool member and retargeting ROAS after 3 weeks, then roll to the other brands.
- Play 5: build the FH customer export pull for one brand (NKST). Output: guest-since list, repeat-guest count, anniversary calendar. Draft the anniversary text and the first honoree post. Stage for approval.
- Play 6: pull real low-star lines per brand, run through /ad-research gap check, ship one honest-signal creative per brand into the existing Meta sets.
- Play 7: rewrite site footers, OpenCX handoff openers, and booking confirmation sign-offs. Name the human. Stage.

**Nov through Dec (DC off-season, NOLA holiday parties, TX mild).**
- Play 10: sponsor pitch (NPB/Ideas/Sponsored Piers draft) to local brewery/seltzer walk-ins first, after David prices it. Pair with Tales 2027 outreach so each brand gets one ask.
- Play 12 + 13: awning quotes; one captain trial with smart glasses.
- Play 8: one journalist-bait angle per NOLA brand for holiday/haunted season. Reddit: target threads that already rank for "[city] kayak tour reddit."
- Play 9: draft the cancel-your-competitor post for NKST from a guide's voice. Approve, post, screenshot swaps.
- Play 11: design the Death's Door certificate and a challenge coin. Order before Q1.
- Play 17 + 18: corporate proof on private-event pages; season-end value recap to DCKT and NKST repeat guests.

**Q1 2027 (pre-season build).**
- Play 14: pick one anti-marketing stunt per brand for opening weekend.
- Play 15: one site sprint across all brands for the small conversion wins.
- Play 19: build the April 1 stunt for one NOLA brand.
- Repeat-Guest Wall installed at each dock before opening day.

---

## Metrics (what "worked" means)

| Play | Metric | Baseline needed |
|------|--------|-----------------|
| 1 | % of weather-cancel value retained as spent credit | Current refund total per brand per month |
| 2 | Cost per lead and cost per booking on Meta/Google after value-based bidding | Current CPL, lead-to-book rate |
| 3 | % of bookings by self-reported source per brand, monthly, vs GA4 channel split | None today (GA4 last-click only) |
| 4 | Cost per 50%-viewer pool member; retargeting CPA/ROAS vs prospecting | Current Meta prospecting CPA per brand |
| 5 | Rebook rate of past guests, 12 months | FH repeat-customer % today |
| 6 | CTR and ROAS vs current best creative | Existing Meta creative matrix |
| 7 | Booking conversion rate on site + OpenCX handoff-to-book | GA4 + OpenCX |
| 8 | Editorial mentions, Reddit referral sessions | GA4 referral, press log |
| 9 | Redeemed switches, screenshots posted | Count |
| 10 | Signed sponsor dollars per season | $0 today |
| 11 | UGC posts tagging the brand per month | IG tag count |
| 15 | Reach and saves on the stunt post | IG insights |
| Opt-in funnel (#3, added 10/19) | Opt-in rate of people shown the offer; FH bookings by ref=optin-* within 30 days | None today |

---

## Rules that travel with every play
- Nothing outbound sends without David's tick. Stage in `_Staged for Approval`.
- Sign as the business, never a person's name, on any outbound (guide-voice posts are the exception and go from the guide's own account with their OK).
- No pedaling as a feature. NOLA Bike Bar is a street vehicle, not a vessel. E&E is Portland.
- Under-$10 FH balances are deposit-box leftovers, not credits. Ask before touching.
- Connor gets one batched ask, not five drips.

## Status log
- 2026-09-24: plan created from the Tom Orbach swipe file. Nothing started yet.
- 2026-10-07: added 5 plays from David's Oct 2 Apple Note (NPB): lead-capture value (#2), sponsored dock/boat partner (#8), branded awnings (#10), captain POV glasses (#11), fans on board (#14). Duplicates skipped: corporate/retreat LinkedIn pitch (already NPB 2027 Sponsorship Plan Track B, noted on #15), costume trunk (already NPB Add-On Menu #51 + Action Tracker #66, due Oct 10). Revenue-target-first logged as a planning frame, not a play. Old plays 2-14 renumbered.
- 2026-10-08: added "How did you hear about us?" checkout question as #3 (Ben, Onera / Modern Hospitality Accelerator newsletter: GA <2% social vs 60%+ surveyed). Ranked above repeat-guest because it's a one-setting change that tells us where every other play's money should go. Old 3-19 renumbered to 4-20.
- 2026-10-08: added Meta video-viewer retargeting pools as #4 (adapted from a LinkedIn click-discouraging-headline hack; on Meta just run ThruPlay and build viewer audiences). Ranked above repeat-guest: direct revenue on existing ad spend, low effort, no pixel dependency. Old 4-20 renumbered to 5-21.
- 2026-10-10: added "be the contra/gifting sponsor at other people's events" as #12 (Jess Williamson Brand Sponsorship Guide, IG DM lead magnet). E&E first. Ranked mid: top-of-funnel with near-zero cost. Old 12-21 renumbered to 13-22. Note: play numbers cited in the Phasing and Metrics sections above 11 are now +1.
- 2026-10-10: /carousel skill built (anti-slop blog-to-IG carousel, real photos, HTML templates); NKST pilot staged in NKST Marketing/Carousels - Staged/.
- 2026-10-10: /event-sponsor skill built for #12 (both directions: be the sponsor, or land sponsors for our own event). Pipeline lives in `Event Sponsorships — Tracker.md`; chief-of-staff Event radar now flags due follow-ups too.
- 2026-10-13: added 3 plays from David's "18' wide" Apple Note (4 IG reels, transcribed): fake-choice price gate (#5), Van Westendorp pricing survey for the banya + review-based customer profile (#6), IG Close Friends media list (#10). Vic Chang reading list filed in the swipe file, not ranked. Old 5-22 renumbered to 7-25 (Phasing/Metrics numbers above 4 now shift by +2, above 9 by +3). E&E deliverable staged: `Ebb and Ember/Marketing/Pricing Survey — Van Westendorp + Customer Profile (Oct 2026).md`.
- 2026-10-13: /creative-director run across every brand. One hero per brand staged in `Launches/2026-10-13 Creative Director — All Brands Launch Slate.md`: NPB "No Costume, No Boarding" (Bass Pirates Oct 31), NKST "The Marshmallow" (public face of #12), E&E "Rain Opening Day" (yearly slot, ties to #10 Close Friends list), LSKT "Reverse Bridge" + nightly bat countdown (#14), BBK "Drainage Ditch" (#18 cleanup becomes the day-3 swarm piece), HPB "Conference Room" (#21, organic only), DCKT "First Ice" (new yearly series, waits on the freeze), NBB Krewe of Boo park-and-film (zero cost). Status: all Staged, nothing posted. First decision: the Connor batch message (Austin's bats leave within two weeks).
- 2026-10-16: added premium-positioning audit as #26 (byjoeym reel: Specificity, Counterposition, 3% Rule, One Very Specific Person, Veblen Effect). `/premium-positioning` skill built with audit / price / person / counter / rewrite modes. Ranked after the parked plays' neighbors on purpose: it's a positioning layer under #5 and #6 rather than a standalone revenue play; promote it once a brand audit shows a lever worth a price move.
- 2026-10-19: added post-price opt-in funnel as #3 (from the Tom Barnes CRO review: never gate prices, capture after). Ranked right under lead-value because it creates the leads #2 needs and works on traffic we already have; Med effort keeps it below #1-2. Old 3-26 renumbered to 4-27 (Phasing/Metrics numbers above 2 now shift by +1). Old #19 small conversion wins is now #20 and loses its maybe-later piece to #3.
- 2026-10-20: #3 got a third A/B arm (win a private weekday party boat, sweepstakes rules + consolation $10 code). Tool decided: Mautic. Found NPB's sitewide 'Get early access' bar -> giveaway page -> retired GHL form.
- 2026-10-21: #12 upgraded with original research (BuzzStream 'PR for GEO'). Kept at #12, no renumber: top-of-funnel, but the cheapest link source we have since the data already exists. Headline finding: NPB median booking lead time 16.8 days (2021) to 6.1 (2026). Study #4 (gator/bat logs) unparks #26.
- 2026-10-22: David: newsletter only, no discount codes until pricing is fixed. NPB newsletter funnel built and deployed in the lead engine (hosted signup page + 4-email flow). Waiting on a wp-admin login to swap the dead GHL form and add the popup script. Mautic dropped. Rollout standards logged in every vault CLAUDE.md.
