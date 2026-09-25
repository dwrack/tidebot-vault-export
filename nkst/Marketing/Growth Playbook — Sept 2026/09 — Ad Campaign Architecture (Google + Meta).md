# 09 — Ad Campaign Architecture (Google + Meta)

*Growth Playbook, September 2026. Facts come from [[00 — Fact Sheet & Open Questions]]. If a number here disagrees with 00, 00 wins.*

**Status: DRAFT. Nothing here is built or live.** All budgets are **PROPOSED**, with the assumptions stated. This file contains **no performance data** except what's quoted, with its source, from existing vault docs. Anything that touches Google Ads, Meta Ads Manager, FareHarbor, GA4 or the website needs David's sign-off.

---

## 0. Read this first: launch gates

Nothing in this plan should spend money until all four gates are cleared.

| # | Gate | Why | Source |
|---|---|---|---|
| G1 | **Google kayak purchase conversion restored.** "New Orleans Kayak Swamp Tours - GA4 (web) purchase" showed **Tracking status: Removed** on 2026-09-15 and 2026-09-17, and it was still Primary. | Smart Bidding can't optimize toward an action that doesn't record. Kayak spend since Sep 1 is unmeasured. | [[Google Ads/SmartAds Oversight Checklist]] |
| G2 | **Meta Purchase event firing** on the FareHarbor confirmation (GT Pixel 701301873334767). It broke on 2026-04-05 and the vault has no record of a fix. | This is the Meta Master Plan's own Phase 0 rule: "Don't launch purchase-optimized campaigns until you see Purchase events flowing again for at least 3-4 days straight." | [[NKST Meta Ads Master Plan]] |
| G3 | **Price of record: $65 or $69** (Fact Sheet open question 1). | Every headline marked **[PRICE]** below uses $65. If the live price is $69, those headlines are disapproval risks and they mislead guests. Swap them before launch. | 00 Fact Sheet |
| G4 | **Each landing page is live and matches its ad.** | The pages in §2 are being written in this playbook. An ad group whose page isn't live stays paused. It doesn't fall back to the homepage. | This file |

**Fishing has its own extra gate (G5).** See §5.

---

## 1. What this builds on and what it supersedes

| Existing doc | Kept | Superseded or changed here |
|---|---|---|
| [[NKST Meta Ads Master Plan]] (Apr 2026, $40/day) | Phase 0 pixel fix, purchase-not-traffic optimization, the retargeting windows (0–7d, 8–30d), the Messenger/OpenCX campaign, the purchaser lookalike (`6136553303296`), the 20% budget-step rule, the custom-audience list, and the "What NOT to Do" list. | **The single TOF Prospecting campaign splits into audience-specific campaigns** (Tourists, Locals, Groups, Private Events, Fishing), each with its own landing page. The $40/day total stays for Phase 1 but is re-cut (§8). **Copy corrections:** the plan says "2.5 hours" and "45 min from the Quarter." This file uses the Fact Sheet's "2 hours" and "about 35 minutes." |
| [[Meta Ads — Creative Testing Strategy]] (Mar 2026) | ICP, "up close, from a kayak" as the visual message, the testing order, and Variants A, B, C and E as a source bank. | **Variant D is retired.** It ends "Best story from your trip, guaranteed," which breaks the voice rules. The staged script queue in `Ad Research/Scripts/` (~50 files, unreviewed) is used here as a *source*, not re-scripted. |
| [[Marketing/Ad Copy Slate — July 2026]] | Hooks, footage map (Video A = wildlife, Video B = group paddling), and the end-card line "Come for the alligator. Stay for the quiet." | **Every "15 minutes" line is dead.** The slate's own correction says "30 minutes from Bourbon," and the Fact Sheet says "about 35 minutes from the French Quarter." This file uses the Fact Sheet. End cards must use **neworleanskayakswamptours.com**, not "NolaKayakTours.com" (see contradictions). |
| [[Google Ads/SmartAds Performance Review — 2026-05-06]] and [[Google Ads/SmartAds Oversight Checklist]] | Generic high-intent focus ("new orleans swamp tour" family), the 5x ROAS floor as the scale/pull-back line, the "up to 10% of gross revenue on ads" ceiling Michael set, and the Sep 1 switch to Maximize clicks while conversions are broken. | **Supersedes the two-campaign structure** (Nola-Kayak National at $60/day, Local at $25/day) with the audience-split structure in §3. **Doesn't adopt the competitor-conquest plan** (a 5% coupon on a named competitor's search terms). See §3.9. |
| [[Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026)]] | The keyword volume *corrections* (the "louisiana swamp tour" and "swamp tour near me" volumes are unreliable), the word-order finding ("swamp tour(s) new orleans" vs "new orleans swamp tours"), and "lead with facts, not mission." | Paid search is used to buy the high-volume **"swamp tour(s) new orleans"** word order that organic currently loses (#15–21), while the SEO fix lands. |

---

## 2. Landing-page map

Each campaign sends traffic to **its own page**. Within a campaign, an ad group may point at a sibling page when the intent is narrower. The homepage is used only for brand searches.

| Campaign | Primary landing page | Ad-group pages | Status |
|---|---|---|---|
| Brand | `/` (homepage) | — | Live |
| Tourists: Planners (out of state) | `/first-time-new-orleans-swamp-tour` | `/manchac-swamp-kayak-tour` (alligator / Manchac intent), `/kayak-swamp-tour-new-orleans` (kayak / eco / "not an airboat" intent), `/family-swamp-tours` (family intent) | Being written |
| Tourists: In Town | `/swamp-tour-near-french-quarter` | `/manchac-swamp-kayak-tour` | Being written |
| Locals (50-mile radius) | `/kayak-swamp-tour-new-orleans` | `/family-swamp-tours` (weekend family intent) | Being written |
| Groups (family reunion, school, scouts, team outings) | `/family-swamp-tours` | Corporate ad group: **no page exists.** Keep it paused until a "best-for" corporate page is built on the bachelorette-page template. The staged draft `corporate-team-building-swamp-kayak-tour-new-orleans` can serve as the page once it's published. | Being written / gap |
| Private Events (bachelorette, bachelor, bridal party, birthday) | Bachelor/bachelorette best-for page: `/bachelorette-bachelor-swamp-tour` *(slug PROPOSED; match the page file)* | — | Being written |
| Gifts (seasonal, Nov 15–Dec 24) | `/gift-cards` | — | **URL conflict:** the live gift page is `/gift-certificates/` (per the staged gift blog draft). [[11 — Gift Card Campaigns]] recommends keeping `/gift-certificates/` (Option A). If that's chosen, point the Gifts ads there. Pick one before launch. |
| Fishing (gated) | `/kayak-fishing-new-orleans` *(slug PROPOSED)* | — | **Doesn't exist.** The only content is the staged draft `Marketing/Blog Drafts - Staged/2026-08-14 - kayak-fishing-new-orleans-charter-guide.md`. See gate G5. |

**Page-to-ad match rule:** each page must show, above the fold, the same four facts the ads lead with: price [PRICE], 2 hours, pickup at 740 N Rampart (+$25) or self-drive about 35 min, and 4.9 from 1,400+ Google reviews. Past SmartAds calls said quality score was "broken on rank," so ad-to-page match is the cheapest fix.

---

## 3. Google Ads

### 3.0 Account structure and naming

**Account:** Gravity Trails | NOLA (CID 437-823-2023), the same account as NPB. Kayak and barge campaigns share it, so every NKST name starts with `NKST`.

**Naming convention**

```
Campaign:  NKST | G | {Type} | {Audience} | {Geo} | {Bid}
           e.g. NKST | G | Search | Tourists-Planners | US-exLA | MaxClicks
Ad group:  {Theme} | {Match}
           e.g. Swamp Tour NOLA | Phrase+Exact
Ad:        RSA | {Angle} | v{n} | {YYYY-MM}
           e.g. RSA | Pickup-Lead | v1 | 2026-10
Neg list:  NEG | {Name}
           e.g. NEG | Universal
```

**Transition from the SmartAds campaigns:** don't run the new campaigns alongside `Nola-Kayak - National` and `Nola-Kayak - Local` on the same keywords. Build the new campaigns paused. At launch, pause the two old campaigns, but don't delete them, so their history stays available for comparison. This depends on David's decision about the SmartAds engagement. The Oversight Checklist documents 11 weeks without vendor activity, so decide that first.

**Match types:** Phrase and Exact only at launch. Broad match comes later, and only on the Tourists: Planners campaign after G1 is fixed and the campaign has 30+ conversions in 30 days. Broad match needs a working conversion signal to behave.

### 3.1 Shared negative keyword lists

**Decision on "airboat": make it a negative on every core campaign, and send comparison searches to a separate, small, opt-in test.**

*Why:* someone searching "airboat tour new orleans" wants speed and an engine. That's a different product, and paying for their click to show them a silent kayak wastes money. But "airboat vs kayak" searchers are *choosing*, and the SEO audit calls airboat vs kayak "the #1 objection." Those searchers are worth reaching with the honest "silent kayaks, not airboats" line. The one-word negative `airboat` would block them, so they get their own campaign (§3.8) with its own negatives. If that test doesn't earn its keep within 30 days, drop it and keep the negative everywhere.

| List | Applies to | Keywords (phrase match unless noted) |
|---|---|---|
| **NEG \| Universal** | All NKST campaigns | job, jobs, hiring, careers, employment, salary, internship, volunteer, "tour guide license", free, "for free", groupon, coupon, "promo code", "discount code", "for sale", "buy a kayak", "used kayak", "kayak store", craigslist, walmart, academy, "swamp people", "swamp thing", shrek, movie, episode, cast, wallpaper, clipart, drawing, coloring, "swamp cooler", "swamp gas", minecraft, game, wikipedia, definition, "what is a swamp", "alligator vs crocodile", "crocodile vs alligator", recipe, "alligator meat", "alligator bite", attack, news, hurricane, flood |
| **NEG \| Motorized** | All except §3.8 Comparison | airboat, "air boat", airboats, "fan boat", "jet ski", pontoon, "swamp boat", "boat ride", "speed boat", "fan boat ride" |
| **NEG \| Wrong Geography** | All | florida, everglades, texas, "caddo lake", georgia, okefenokee, "south carolina", "myrtle beach", "atchafalaya basin tour", lafayette, "lake martin", houma *(Houma is a judgment call: it's a real swamp-tour town about 1 hr away. Review the search terms after 2 weeks.)* |
| **NEG \| Other Operators** | All | Fill this list from the "Direct competitors" table in [[NKST + NPB — Cross-Promo & Affiliate Campaign]] (8 names). Leave the names out of this file, since it may get shared. **This contradicts the SmartAds conquest plan.** See §3.9. |
| **NEG \| Off-Season** | All, Oct 1–Apr 30 | "honey island" (summer only per the Fact Sheet; Honey Island searches off-season would go to a tour we can't sell) |
| **NEG \| Fishing** | All except Fishing | fishing, fish, charter, angler, redfish, "speckled trout", bass, crabbing, shrimping |
| **NEG \| Self-Guided** | All except Locals | "rent a kayak", "kayak rental", rentals, "self guided" *(the Bayou Bienvenue rental is a separate product at ~$37 per GBP. Don't pay tourist-campaign CPCs to sell it.)* |

**Cross-campaign negatives (these stop our own campaigns competing with each other):**
- **Tourists: Planners** adds the negatives: "near me", tonight, today, tomorrow, "this weekend".
- **Tourists: In Town** adds the negatives: gift, "gift card", "gift certificate", bachelorette, bachelor, wedding, reunion, school, corporate.
- **Locals** adds the negatives: "french quarter", pickup, shuttle, hotel, "from new orleans", bachelorette, bachelor, wedding.
- **Groups** and **Private Events** each negate the other's core terms (reunion/school/team ↔ bachelorette/bachelor/bridal/birthday).
- **Brand** only takes brand terms. Every other campaign adds the negatives: "new orleans kayak swamp tours", "nola kayak tours", "kayak swamp tours".

### 3.2 Campaign: Brand

`NKST | G | Search | Brand | US | MaxClicks→tIS`

- **Goal:** protect the brand name. That includes the documented problem of another operator using "New Orleans Kayak Swamp Tours" as an ad headline (SmartAds review, May 6). Consider the trademark filing an open item there.
- **Geo:** United States. Location option: Presence or interest.
- **Bidding:** Target Impression Share, 90% absolute top, with a max CPC cap. If brand CPCs stay low, it doesn't need more.
- **Landing page:** `/`
- **Ad group: Brand | Exact+Phrase:** [new orleans kayak swamp tours], "new orleans kayak swamp tour", "nola kayak tours", "nola kayak swamp tours", "kayak swamp tours new orleans". Only add "kayak swamp tour" as a phrase if the search terms show brand intent.

**RSA: Brand**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | New Orleans Kayak Swamp Tours | 29 |
| H2 | Official Site, Book Direct | 26 |
| H3 | Silent Kayaks, Not Airboats | 27 |
| H4 | Rated 4.9 by 1,400+ Guests | 26 |
| H5 | Small Groups, 12 Guests Max | 27 |
| H6 | Manchac Swamp Wildlife Tour | 27 |
| H7 | Trained Naturalist Guides | 25 |
| H8 | French Quarter Shuttle Pickup | 29 |
| H9 | Paddling Since 2013 | 19 |
| H10 | No Experience Needed | 20 |
| H11 | Free Cancellation Up to 48 Hrs | 30 |
| H12 | Morning and Afternoon Tours | 27 |
| H13 | From $65 Per Guest [PRICE] | 18 |
| H14 | Instant Online Booking | 22 |
| H15 | Wild Gators, Never Baited | 25 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Silent kayaks, not airboats. Small groups with trained naturalist guides. Book direct. | 86 |
| D2 | Paddle the Manchac Swamp, about 35 min from the French Quarter. Shuttle available. | 82 |
| D3 | Rated 4.9 from 1,400+ Google reviews. No experience needed. Ages 8 and up. | 74 |
| D4 | Free cancellation up to 48 hours before your tour. Weather cancel means a full refund. | 86 |

Pin H1 to position 1.

### 3.3 Campaign: Tourists: Planners (out of state)

`NKST | G | Search | Tourists-Planners | US-exLA | MaxClicks→MaxConv`

- **Geo:** United States. **Exclude Louisiana** (Presence: "People in your excluded locations"). Target option: **Presence**, not "Presence or interest," so the campaign doesn't pay for Louisiana residents. The keywords themselves carry the New Orleans intent.
- **Audiences (Observation mode at launch, so bids learn without narrowing reach):** In-market: *Travel > Trips to New Orleans* (if listed; otherwise *Travel > Tourist Attractions* and *Hotels & Accommodations*). Custom segment of people who searched "new orleans hotels", "flights to new orleans", "things to do in new orleans", "new orleans itinerary". Past website visitors (GA4, 30 days). Exclude purchasers from the last 30 days (GA4 audience).
- **Ad schedule:** all hours. Planners book from home in the evening, so review the hour-of-day data after 30 days.
- **Devices:** no adjustments at launch.

| Ad group | Landing page | Keyword themes (match) |
|---|---|---|
| **Swamp Tour NOLA** (core, most of the budget) | `/first-time-new-orleans-swamp-tour` | [swamp tours new orleans], [swamp tour new orleans], [new orleans swamp tours], [new orleans swamp tour], "swamp tour from new orleans", "swamp tours near new orleans", "best swamp tour new orleans", "swamp tours in new orleans" |
| **First Timer / Planning** | `/first-time-new-orleans-swamp-tour` | "is a swamp tour worth it new orleans", "things to do in new orleans outdoors", "new orleans day trip swamp", "how much is a swamp tour in new orleans" |
| **Alligator / Manchac** | `/manchac-swamp-kayak-tour` | [alligator tour new orleans], "gator tour new orleans", "see alligators new orleans", "manchac swamp tour", "maurepas swamp tour", "manchac kayak tour" |
| **Kayak / Eco** | `/kayak-swamp-tour-new-orleans` | [kayak swamp tour new orleans], "kayak tours new orleans", "eco tour new orleans", "guided kayak tour louisiana swamp", "bayou kayak tour" |
| **Family** | `/family-swamp-tours` | "family swamp tour new orleans", "swamp tour with kids new orleans", "kid friendly swamp tour new orleans", "things to do with kids new orleans outdoors" |

**RSA: Tourists: Planners** (core ad group; the other ad groups swap H1–H3 for their theme)

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | New Orleans Swamp Tours | 23 |
| H2 | Swamp Tour Near New Orleans | 27 |
| H3 | Kayak the Manchac Swamp | 23 |
| H4 | Silent Kayaks, Not Airboats | 27 |
| H5 | First Swamp Tour? Start Here | 28 |
| H6 | No Experience Needed | 20 |
| H7 | Small Groups, 12 Guests Max | 27 |
| H8 | Rated 4.9 by 1,400+ Guests | 26 |
| H9 | French Quarter Shuttle Pickup | 29 |
| H10 | Gators Common Spring to Fall | 28 |
| H11 | Cypress Trees & Spanish Moss | 28 |
| H12 | Trained Naturalist Guides | 25 |
| H13 | From $65 Per Guest [PRICE] | 18 |
| H14 | Fall Dates Book Up Fast | 23 |
| H15 | Free Cancellation Up to 48 Hrs | 30 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | A calm 2-hour kayak eco-tour in the Manchac Swamp. Silent kayaks, not airboats. | 79 |
| D2 | Round-trip shuttle from 740 N Rampart St, or meet us at the launch in LaPlace. | 78 |
| D3 | Alligators are common spring through fall. We never bait them and never promise them. | 85 |
| D4 | Rated 4.9 from 1,400+ Google reviews. Ages 8+. Free cancellation up to 48 hrs out. | 82 |

*Theme swaps:* Alligator / Manchac H1–H3 = "Alligator Tour New Orleans", "Wild Gators, Never Baited", "Manchac Swamp Kayak Tour". Kayak / Eco = "Kayak Swamp Tour New Orleans", "Guided Kayak Eco-Tour", "No Motors, No Wake". Family = "Family Swamp Tour", "Kid-Friendly, Ages 8 and Up", "Tandem Kayaks for Families".

### 3.4 Campaign: Tourists: In Town

`NKST | G | Search | Tourists-InTown | NOLA-25mi | MaxClicks→MaxConv`

- **Why a separate campaign:** visitors already in New Orleans search differently ("near me," "tomorrow," "near the French Quarter"). Pickup is the deciding fact for them, and they can't be reached by a campaign that excludes Louisiana. This mirrors the Meta plan's travel_in idea.
- **Geo:** 25-mile radius around 740 N Rampart St. Presence.
- **Audiences (Observation):** In-market Travel / Tourist Attractions / Hotels. Exclude purchasers (30 days).
- **Overlap with Locals:** same geo, different keywords. The cross-campaign negatives in §3.1 keep them apart. We can't cleanly tell a visitor from a resident in Google Search, so keywords decide. *Assumption to test:* "swamp tour near me" searched from inside New Orleans is mostly visitors, so it lives here, not in Locals.
- **Ad schedule:** weight bids up 6 AM–2 PM for same-day and next-day decisions (+15% proposed), and review after 30 days.

| Ad group | Landing page | Keyword themes (match) |
|---|---|---|
| **Near the Quarter / Pickup** | `/swamp-tour-near-french-quarter` | "swamp tour near french quarter", "swamp tour with pickup new orleans", "swamp tour hotel pickup new orleans", "swamp tour transportation new orleans", "swamp tour near me", "swamp tours near me" |
| **Tomorrow / Today** | `/swamp-tour-near-french-quarter` | "swamp tour tomorrow new orleans", "swamp tour today new orleans", "last minute swamp tour new orleans" |
| **Gator Near Me** | `/manchac-swamp-kayak-tour` | "alligator tour near me", "gator tour near me", "kayak tour near me" |

**RSA: Tourists: In Town**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Swamp Tour Near French Quarter | 30 |
| H2 | Pickup at 740 N Rampart St | 26 |
| H3 | French Quarter Shuttle Pickup | 29 |
| H4 | In New Orleans? See the Swamp | 29 |
| H5 | Tours at 9, 11:30, 2 & 4:30 | 27 |
| H6 | Book Tomorrow's Swamp Tour | 26 |
| H7 | Round-Trip Van, +$25 Per Guest | 30 |
| H8 | Silent Kayaks, Not Airboats | 27 |
| H9 | Small Groups, 12 Guests Max | 27 |
| H10 | Rated 4.9 by 1,400+ Guests | 26 |
| H11 | No Experience Needed | 20 |
| H12 | No Car Needed | 13 |
| H13 | Wild Gators, Never Baited | 25 |
| H14 | From $65 Per Guest [PRICE] | 18 |
| H15 | Free Cancellation Up to 48 Hrs | 30 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Round-trip van from 740 N Rampart St, edge of the Quarter. Leaves 1 hr 15 min before. | 85 |
| D2 | Two hours in the Manchac Swamp with a trained naturalist. Silent kayaks, not airboats. | 86 |
| D3 | Skip the rideshare. There's no ride back from the launch, so our van brings you both ways. | 90 |
| D4 | Rated 4.9 from 1,400+ Google reviews. Ages 8+. Free cancellation up to 48 hrs out. | 82 |

### 3.5 Campaign: Locals (50-mile radius)

`NKST | G | Search | Locals | NOLA-50mi | MaxClicks→MaxConv`

- **Geo:** 50-mile radius around New Orleans. Presence. This reaches the Northshore, LaPlace and the River Parishes, and edges toward Baton Rouge's eastern suburbs. The launch is in LaPlace, so Baton Rouge proper, about 45 minutes from the launch, is worth a separate 30-day test radius around the launch site later.
- **Audiences (Observation):** Affinity *Outdoor Enthusiasts*, *Nature & Wildlife*, *Birding* (custom segment). Exclude purchasers (180 days) so past guests aren't retargeted with a first-visit pitch.
- **Ad schedule:** weight up Thursday–Saturday (+10% proposed) for weekend planning.
- **Angle:** "the swamp in your backyard." Locals drive, so self-drive to the launch leads. Fall is best, and winter means birds. The Creative Testing Strategy ICP already names locals "who've 'always meant to' do a swamp tour."

| Ad group | Landing page | Keyword themes (match) |
|---|---|---|
| **Local Kayak** | `/kayak-swamp-tour-new-orleans` | "kayak tours near new orleans", "kayaking near new orleans", "kayak tour louisiana", "guided kayak tour near me", "places to kayak near new orleans", "kayak lafitte" *(check search terms; Jean Lafitte is on the /tours/swamp/ title, but the Fact Sheet doesn't list it as a current tour)* |
| **Weekend Outdoors** | `/kayak-swamp-tour-new-orleans` | "things to do this weekend new orleans outdoors", "outdoor activities new orleans", "birding tour louisiana", "manchac swamp" |
| **Local Family** | `/family-swamp-tours` | "family activities new orleans weekend", "things to do with kids near new orleans outdoors" |
| **Self-Guided** *(optional)* | Bayou Bienvenue rental page (existing) | "kayak rental new orleans", "rent a kayak new orleans". Keep this only if David wants rentals pushed. Otherwise leave it out. |

**RSA: Locals**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Kayak Swamp Tour New Orleans | 28 |
| H2 | Paddle the Manchac Swamp | 24 |
| H3 | About 35 Min From the Quarter | 29 |
| H4 | Drive & Meet Us at the Launch | 29 |
| H5 | Weekend Kayak Tours | 19 |
| H6 | Silent Kayaks, Not Airboats | 27 |
| H7 | Best Season Is Fall | 19 |
| H8 | Winter Brings Migratory Birds | 29 |
| H9 | Tandem Kayaks, Ages 8 and Up | 28 |
| H10 | No Experience Needed | 20 |
| H11 | Trained Naturalist Guides | 25 |
| H12 | Rated 4.9 by 1,400+ Guests | 26 |
| H13 | Small Groups, 12 Guests Max | 27 |
| H14 | From $65 Per Guest [PRICE] | 18 |
| H15 | The Swamp in Your Backyard | 26 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Lived here for years and never paddled Manchac? Two quiet hours, about 35 min away. | 83 |
| D2 | Drive yourself and meet us at the launch in LaPlace. Morning and afternoon tours. | 81 |
| D3 | Silent kayaks, not airboats. Small groups and naturalist guides. Gators common in summer. | 89 |
| D4 | Rated 4.9 from 1,400+ Google reviews. Free cancellation up to 48 hours before your tour. | 88 |

### 3.6 Campaign: Groups

`NKST | G | Search | Groups | US | MaxClicks (lead-optimized after G1)`

- **Scope:** family reunions, school and homeschool field trips, scout and church groups, team outings. These are private tours from the [[Operations/Private Tour Rate Card]], 4–20 guests.
- **Geo:** United States. Presence or interest (group organizers plan from anywhere).
- **Conversion:** group bookings often start as an inquiry, not a checkout. The primary conversion is **Lead**: inquiry form submit, calls of 60+ seconds from ads, and OpenCX chats that capture a date. The FareHarbor private booking is secondary until offline import is set up (§7).
- **Bidding:** Maximize clicks with a CPC cap at launch, because volume will be too low for Smart Bidding. Move to Maximize conversions (Lead) at 15+ leads in 30 days.

| Ad group | Landing page | Keyword themes (match) |
|---|---|---|
| **Family Reunion** | `/family-swamp-tours` | "family reunion activities new orleans", "family reunion swamp tour", "large group swamp tour new orleans" |
| **School / Scout / Field Trip** | `/family-swamp-tours` | "field trip new orleans swamp", "school trip swamp tour louisiana", "homeschool field trip new orleans", "scout trip new orleans" |
| **Private Group** | `/family-swamp-tours` | "private swamp tour new orleans", "private kayak tour new orleans", "group swamp tour new orleans", "swamp tour for groups" |
| **Team Outing** *(PAUSED until a corporate page exists; see §2)* | corporate best-for page (TBD) | "team building new orleans outdoor", "corporate outing new orleans", "company outing new orleans" |

**RSA: Groups**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Private Group Kayak Tours | 25 |
| H2 | Family Reunion Swamp Tour | 25 |
| H3 | School & Scout Group Trips | 26 |
| H4 | Team Outing in the Swamp | 24 |
| H5 | Private Tours for 4 to 20 | 25 |
| H6 | Your Group, Your Own Guide | 26 |
| H7 | Clear Per-Guest Group Rates | 27 |
| H8 | Groups From $105 Per Guest | 26 |
| H9 | Tandem Kayaks, Ages 8 and Up | 28 |
| H10 | Silent Kayaks, Not Airboats | 27 |
| H11 | Trained Naturalist Guides | 25 |
| H12 | Rated 4.9 by 1,400+ Guests | 26 |
| H13 | Pickup From the French Quarter | 30 |
| H14 | Over 20 Guests? Call Us | 23 |
| H15 | No Experience Needed | 20 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Private kayak tours for groups of 4 to 20. Just your group and your guide on the water. | 87 |
| D2 | Family reunions, school trips, team outings. Ages 8+. Under-16s paddle tandem with adults. | 90 |
| D3 | Groups of 13 to 20 from $105 per guest on the 2-hour tour. Add French Quarter pickup, $25. | 90 |
| D4 | Silent kayaks, not airboats. Rated 4.9 from 1,400+ Google reviews. Tell us your date. | 85 |

*H8 and D3 are rate-card prices, which don't depend on the $65/$69 question. Still confirm the FareHarbor private items are live (rate card open item) before running them.* **Pause H4 while Team Outing is paused.**

### 3.7 Campaign: Private Events

`NKST | G | Search | PrivateEvents | US | MaxClicks (lead-optimized after G1)`

- **Scope:** bachelorette and bachelor parties, bridal parties, wedding welcome days, birthdays, anniversaries. The staged drafts `bachelorette-bachelor-party-swamp-tour-new-orleans` and `anniversary-honeymoon-kayak-tour-new-orleans` should link from the landing page.
- **Geo:** United States. Presence or interest.
- **Audiences (Observation):** Life events *Getting married soon* / *Recently engaged* (if still available), In-market *Wedding Services*, and a custom segment of people who searched "new orleans bachelorette", "nola bachelorette itinerary", "new orleans bachelor party".
- **Sister brand:** NOLA Party Barge runs its own campaigns in this account. Add the NPB brand terms as negatives here, and the NKST private-event terms as negatives on NPB, so the two brands don't bid against each other. Both brands take party groups, so coordinate the change with the NPB side.
- **Conversion:** Lead (primary) plus FareHarbor private booking, the same as Groups.

| Ad group | Landing page | Keyword themes (match) |
|---|---|---|
| **Bachelorette** | best-for page | "new orleans bachelorette activities", "bachelorette party ideas new orleans", "nola bachelorette things to do", "bachelorette swamp tour" |
| **Bachelor** | best-for page | "new orleans bachelor party ideas", "bachelor party activities new orleans", "bachelor party outdoor new orleans" |
| **Wedding / Bridal** | best-for page | "wedding welcome activity new orleans", "bridal party activity new orleans", "things to do with wedding guests new orleans" |
| **Birthday / Celebration** | best-for page | "birthday ideas new orleans outdoors", "private tour for birthday new orleans" |

**RSA: Private Events**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Bachelorette Swamp Tour | 23 |
| H2 | Bachelor Party Kayak Trip | 25 |
| H3 | Bridal Party Private Tour | 25 |
| H4 | Wedding Welcome Day Outing | 26 |
| H5 | Private Kayak Tour for Groups | 29 |
| H6 | Just Your Crew and a Guide | 26 |
| H7 | Birthday Swamp Tour | 19 |
| H8 | A Calm Morning After the Party | 30 |
| H9 | Groups of 4-6: $120 Per Guest | 29 |
| H10 | Private for 2 From $350 | 23 |
| H11 | French Quarter Shuttle Pickup | 29 |
| H12 | Silent Kayaks, Not Airboats | 27 |
| H13 | Rated 4.9 by 1,400+ Guests | 26 |
| H14 | No Experience Needed | 20 |
| H15 | Up to 20 Guests Per Tour | 24 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Your group, your own guide, the whole swamp to yourselves. Private tours for up to 20. | 86 |
| D2 | Groups of 4-6 from $120 per guest. 7-12 from $110. Add French Quarter pickup, $25 each. | 87 |
| D3 | A quiet two hours on the water between the late nights. Silent kayaks, not airboats. | 84 |
| D4 | Rated 4.9 from 1,400+ Google reviews. Ages 8+. Tell us your date and group size. | 80 |

### 3.8 Campaign: Comparison test (optional, Phase 2)

`NKST | G | Search | Comparison | US | MaxClicks`, **$5/day, 30 days, then keep or kill.**

- **Keywords (Exact / Phrase only):** [airboat or kayak swamp tour], "airboat vs kayak swamp tour", "kayak instead of airboat", "quiet swamp tour new orleans", "swamp tour without airboat".
- **Negatives:** NEG | Universal, NEG | Wrong Geography, NEG | Other Operators, plus "airboat ride", "airboat tours" (exact), "airboat rental".
- **Landing page:** `/kayak-swamp-tour-new-orleans`, with the staged draft `airboat-vs-kayak-swamp-tour-new-orleans` linked from it once published.
- **Copy rule:** only positive framing, "silent kayaks, not airboats." No knocks on airboats or anyone who runs them. Reuse the Kayak / Eco RSA plus H "Quiet Swamp Tour, No Motor".

### 3.9 Competitor keywords: decision

**Recommendation: don't bid on competitor brand names, and add them as negatives (NEG | Other Operators).** This supersedes the May 6 SmartAds action item to run a "5% coupon on [a named competitor's] search terms."

*Why:*
1. **Voice rule:** "Never name or bash a competitor." Bidding on the name doesn't name them in copy, but a coupon built to steal their searchers is a bash in spirit.
2. **Trademark policy:** Google generally allows bidding on a trademarked term as a keyword. It **restricts using the trademark in ad text**, and the owner can file a complaint. A conquest ad that "accidentally" shows their name through dynamic keyword insertion or a headline gets disapproved, and it invites a mirror-image fight. NKST is already in that fight in the other direction (see §3.2) and hasn't filed its own trademark yet.
3. **Economics:** competitor-name clicks usually cost more and convert worse than generic "swamp tour new orleans" clicks, which the SEO audit shows are the bigger prize anyway.

*If David still wants conquest:* run it as its own campaign (`NKST | G | Search | Conquest | …`) with **no DKI**, no competitor name in any asset, no coupon language in ads (the coupon lives only on the landing page), and a $5/day cap. Review it against Tourists: Planners CPA after 30 days.

### 3.10 Campaign: Fishing (GATED, build paused)

**Gate G5: confirm fishing is a live, sellable product before spending a dollar.**
- *Evidence it exists:* a "fishing charter" item is referenced in FareHarbor. The payroll notes say gratuity is off "on ... the fishing charter," and the Slack report lists "the fishing charter" among items with tips off. The GBP audit lists "Fishing / Crabbing / Shrimping Bayou Tour" as a service to add. The FAQ database has a Dec 2025 email thread "Re: Fishing Kayak Charter 12/13." The staged blog draft calls it "a real bookable product." Fishing photos exist in `Assets/Photos/`.
- *What's missing:* the Fact Sheet doesn't list it. There's **no price**, schedule, group size, guide assignment, launch location, or license-handling policy anywhere in the vault. There's **no landing page.**
- **Before building:** (1) David confirms fishing is offered this fall and winter, with price, duration, max group and who guides it. (2) Publish the fishing page, adapted from the staged draft `kayak-fishing-new-orleans-charter-guide` and cited as the source. (3) Confirm what the booking includes (the draft says "rod and basic tackle, a life jacket"). (4) Settle the license wording. The draft says anglers 16+ "most likely" need a Louisiana license.

`NKST | G | Search | Fishing | {Geo TBD} | MaxClicks`

- **Geo:** Google sets geo per campaign, not per ad group, so start with **US Presence**. Keywords carry "new orleans / louisiana." Add a Locals variant later if the local share is high.
- **Landing page:** `/kayak-fishing-new-orleans` (to be built).

| Ad group | Keyword themes (match) |
|---|---|
| **Kayak Fishing NOLA** | [kayak fishing new orleans], "kayak fishing charter new orleans", "guided kayak fishing louisiana", "kayak fishing guide new orleans" |
| **Species** | "redfish kayak charter new orleans", "bayou fishing trip new orleans", "speckled trout kayak louisiana" |
| **Crab / Shrimp** *(only if confirmed)* | "crabbing tour new orleans", "shrimping tour louisiana" |

**RSA: Fishing** *(every [VERIFY] item needs confirming before launch)*

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Kayak Fishing New Orleans | 25 |
| H2 | Guided Bayou Fishing Charter | 28 |
| H3 | Pedal-Drive Fishing Kayaks | 26 |
| H4 | Bass to Redfish, By Season | 26 |
| H5 | Hands-Free Pedal Kayaks | 23 |
| H6 | Fish Water Boats Can't Reach | 28 |
| H7 | Rod & Tackle Included [VERIFY] | 21 |
| H8 | Guide Picks the Spot Daily | 26 |
| H9 | Crabbing & Shrimping Too | 24 |
| H10 | No Boat Needed | 14 |
| H11 | Local Guides Who Fish Here | 26 |
| H12 | Rated 4.9 by 1,400+ Guests | 26 |
| H13 | Book a Bayou Fishing Trip | 25 |
| H14 | Small-Group Fishing Charter | 27 |
| H15 | Beginners Welcome | 17 |

*(H7's [VERIFY] tag is a note, not ad text. H9, H14 and H15 are also unverified.)*

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Guided kayak fishing in the bayous near New Orleans. Pedal-drive kayaks, hands-free. | 84 |
| D2 | Rod, basic tackle and life jacket included. Your guide picks the spot by season and tide. | 89 |
| D3 | Bass and bream in freshwater, redfish and trout toward the marsh. Catches never promised. | 89 |
| D4 | Anglers 16+ likely need a Louisiana fishing license. We'll walk you through it at booking. | 90 |

### 3.11 Campaign: Gifts (seasonal, Nov 15–Dec 24)

`NKST | G | Search | Gifts | NOLA-50mi + US | MaxClicks→MaxConv`

- **Geo:** 50-mile radius (locals giving locals) plus a US ad group for "new orleans gift" searches from out of state. Presence or interest.
- **Landing page:** `/gift-cards` (resolve the `/gift-certificates/` URL conflict first, §2).
- **Keywords:** "swamp tour gift certificate", "new orleans experience gift", "new orleans gift ideas", "gift card kayak tour", "unique gifts new orleans", "louisiana experience gift".

**RSA: Gifts**

| # | Headline (≤30) | Chars |
|---|---|---|
| H1 | Swamp Tour Gift Certificates | 28 |
| H2 | Give a Swamp Tour This Year | 27 |
| H3 | An Experience, Not More Stuff | 29 |
| H4 | Gift a Kayak Eco-Tour | 21 |
| H5 | Delivered to Their Inbox | 24 |
| H6 | Gift Certificates Never Expire | 30 |
| H7 | Last-Minute Gift, Sorted | 24 |
| H8 | For the Friend Who Has It All | 29 |
| H9 | Silent Kayaks, Not Airboats | 27 |
| H10 | Rated 4.9 by 1,400+ Guests | 26 |
| H11 | New Orleans Gift Ideas | 22 |
| H12 | Local Gift, Real Louisiana | 26 |
| H13 | Trained Naturalist Guides | 25 |
| H14 | Gift a Private Tour | 19 |
| H15 | Easy Online Checkout | 20 |

| # | Description (≤90) | Chars |
|---|---|---|
| D1 | Give two quiet hours in the Manchac Swamp. Gift certificates delivered by email. | 80 |
| D2 | Silent kayaks, not airboats. Small groups, trained naturalist guides, ages 8 and up. | 84 |
| D3 | Rated 4.9 from 1,400+ Google reviews. They pick the date that works for them. | 77 |
| D4 | Great for the local who's never been. They choose the date, we handle the rest. | 79 |

*H6 "Never Expire" comes from the ad-research pass 24 read of the live gift page. Re-check the page before launch, because some states regulate gift-certificate expiry language. H5 comes from the staged gift blog draft ("lands in their inbox right after you check out").*

### 3.12 Assets (extensions), all campaigns

| Asset | Content | Notes |
|---|---|---|
| **Sitelinks** (4–6 per campaign) | Tourists: "Pickup & Directions" → `/swamp-tour-near-french-quarter` · "First-Timer Guide" → `/first-time-new-orleans-swamp-tour` · "Manchac Wildlife Tour" → `/manchac-swamp-kayak-tour` · "Family Tours" → `/family-swamp-tours` · "Private Tours" → private-tour page · "Gift Certificates" → `/gift-cards` | Match sitelinks to the campaign. Locals leads with "Drive to the Launch"; Private Events leads with "Bachelorette Groups." |
| **Callouts** | Silent Kayak Eco-Tours · 12 Guests Max · Since 2013 · Ages 8+ · No Experience Needed · Naturalist Guides · Free Cancellation 48 Hrs · Tours Run in Light Rain | Each is 25 characters or fewer. "Silent kayaks, not airboats" is 27 characters, so it lives in headlines instead. |
| **Structured snippets** | *Tours:* Manchac 2-Hour, Extended 4-Hour, Whitney + Swamp Combo, Private Tours. (Honey Island only in summer.) | |
| **Price assets** | Manchac 2 hr from $65 [PRICE] · Extended 4 hr from $130 [PRICE] · Whitney Combo from $195 · Private groups from $105/guest | Michael added price assets on Aug 27–28 (Oversight Checklist). **Audit those against G3.** |
| **Call asset** | (504) 571-9975, call reporting on, calls ≥60 s count as a conversion (secondary for Tourists, primary Lead for Groups/Private) | Use a Google forwarding number in ads only. The website and GBP keep the real number for consistent listings. |
| **Location asset** | Link the GBP (740 N Rampart St) | The SEO audit flags GBP category and cluster issues. Link only the NKST listing. |
| **Image assets** | Cypress and moss, guests paddling, a guide pointing, a gator at a distance (Video A stills) | Square and landscape. **No airboat photos.** |
| **Lead form asset** | Groups and Private Events only. Fields: name, email, phone, date, group size, occasion. | Sync to GHL. Reply the same day. |
| **Promotion asset** | None. There's no live promotion. | Don't invent one. |

### 3.13 Bidding progression

| Stage | Trigger | Strategy |
|---|---|---|
| **A: Tracking broken (now)** | G1 not cleared | Maximize clicks with a max CPC cap. This is what Michael switched National to on Sep 1. Consumer campaigns **stay paused**, except Brand, until G1 clears, or run at 50% of proposed budget with a clicks goal as a deliberate, flagged exception David approves. |
| **B: Tracking fixed, low volume** | G1 cleared, fewer than 15 conversions per campaign in 30 days | Maximize clicks (CPC cap) or Maximize conversions with no target. Turn on enhanced conversions. |
| **C: Signal** | 15–30+ conversions per campaign in 30 days | Maximize conversion value. |
| **D: Scale** | 30+ conversions in 30 days, stable 2+ weeks | Target ROAS starting at the last 30-day actual, never above it. **Floor: 5x** (the SmartAds agreement). |

Groups and Private Events stay on Lead-based bidding until offline conversion import sends the FareHarbor private booking value back (§7).

### 3.14 PROPOSED Google budget split

*Assumptions:* (1) Monthly total **$3,000**, matching the May 6 target and the current ~$97/day kayak run-rate (Oversight Checklist, Sep 3–16). (2) The ceiling is Michael's stated **10% of gross revenue on ads**, across Google and Meta combined. (3) Nothing here is a forecast. The splits reflect intent volume per the SEO audit's corrected numbers and product value, not measured results. (4) Consumer campaigns don't launch until G1 clears.

| Campaign | $/day | $/mo (30.4 days) | Share | Rationale |
|---|---:|---:|---:|---|
| Brand | 5 | 152 | 5% | Cheap defense |
| Tourists: Planners | 40 | 1,216 | 41% | The biggest query family ("swamp tour(s) new orleans") |
| Tourists: In Town | 20 | 608 | 20% | High-intent, pickup-led |
| Locals | 12 | 365 | 12% | Smaller pool. Fall and winter are the local season |
| Groups | 8 | 243 | 8% | Low volume, high ticket |
| Private Events | 13 | 395 | 13% | $480–$2,100 tickets from the rate card |
| Fishing | 0 | 0 | 0% | Gated (G5). Once live, $5/day test taken from Planners |
| Comparison (Phase 2) | 0→5 | 0→152 | — | Taken from Planners when it starts |
| Gifts (Nov 15–Dec 24) | 0→10 | — | — | Seasonal. Take $5 from Planners and $5 from Locals during the window |
| **Total** | **98** | **~2,980** | 100% | |

---

## 4. Meta Ads

### 4.0 Structure and naming

```
Campaign:  NKST | M | {Objective} | {Audience} | {Stage}
           e.g. NKST | M | Sales | Tourists | Prospecting
Ad set:    AS | {Geo} | {Audience} | {Age} | {Placement}
           e.g. AS | US-exLA | Adv+ Broad | 25-55 | Adv+Placements
Ad:        AD | {Concept} | {Format} | v{n} | {YYYY-MM}
           e.g. AD | Silence-A1 | Reel | v1 | 2026-10
```

- **Account:** act_87863118 · **Pixel:** GT Pixel 701301873334767 (gate G2).
- **Objective:** Sales (Purchase) for Tourists and Locals once G2 clears. Leads (Instant Form or Messenger) for Groups and Private Events. Group volume is too low for purchase optimization to exit learning.
- **Kept as-is from the Master Plan:** `NKST | Purchase | Retargeting` (0–7d / 8–30d) and `NKST | Messenger | TOF (OpenCX)`. They're renamed to the convention above and are not re-specced here.
- **Voice rules for every ad:** "silent kayaks, not airboats," never promise gators, guests not customers, no "extreme," minimal exclamation marks, no competitor names. Use "about 35 minutes from the French Quarter." End card: "Come for the alligator. Stay for the quiet." · neworleanskayakswamptours.com.

### 4.1 Campaign: Tourists (Prospecting)

`NKST | M | Sales | Tourists | Prospecting` → **`/first-time-new-orleans-swamp-tour`** (ad set C → `/swamp-tour-near-french-quarter`)

| Ad set | Audience |
|---|---|
| **A: US Broad ex-LA** | US, **excluding Louisiana**, ages 25–55. Advantage+ audience on, with suggestions: *New Orleans*, *Travel*, *Ecotourism*, *Kayaking*, *Birdwatching*. Exclude purchasers (180d). |
| **B: Purchaser Lookalike** | Lookalike US 1% from GT Pixel purchasers (`6136553303296`, per the Master Plan; refresh it if the source is stale after the April pixel break). Exclude LA and purchasers. |
| **C: In New Orleans now** | People **traveling in** New Orleans (location: "People traveling in this location"), 25-mile radius, 21–65. This is the Master Plan's Phase 2 travel_in idea, pulled forward. Exclude purchasers. |

**Concepts**

**T1: "Silence" (Video A, wildlife reel)** · Ad sets A, B
- **Primary text:** The loudest thing out here is your own paddle. Two hours in the Manchac cypress swamp, about 35 minutes from the French Quarter. We use silent kayaks, not airboats, and keep it to 12 guests with a naturalist guide. Gators are common spring through fall, and never baited. No experience needed.
- **Headline:** Kayak the Manchac Swamp
- **CTA:** Book Now
- **Creative brief:** 9:16 Reel, 15–20 s, built from Ad Copy Slate spot A1. Frame 1 is the hook text over still water (DM Serif Display, yellow, lower third). The gator glide from Video A lands at about 4 s, then the warbler, then the owl. Ambient sound with a light VO. **Replace the slate's "fifteen minutes from the French Quarter" VO line** with "about thirty-five minutes from the Quarter." End card: "Come for the alligator. Stay for the quiet."

**T2: "First swamp tour? Here's the whole thing" (explainer carousel)** · Ad sets A, B
- **Primary text:** Planning New Orleans and wondering if a swamp tour is worth it? Here's exactly what happens. The van leaves 740 N Rampart St. You paddle a calm, current-free swamp for 2 hours with a trained naturalist. Then you're back in the Quarter by the afternoon. Rated 4.9 from 1,400+ Google reviews.
- **Headline:** Your First Swamp Tour, Explained
- **CTA:** Learn More
- **Creative brief:** 5-card carousel, 1:1. (1) Van at Rampart: "Pickup near the Quarter." (2) Guide briefing: "Safety briefing, then paddle." (3) Tandem kayak on glassy water: "No experience needed." (4) Wildlife: "Gators common in warm months. Never baited." (5) Review quote plus "4.9 · 1,400+ reviews." Use real, sourced review quotes only, never invented ones.

**T3: "In New Orleans? Tomorrow morning" (static)** · Ad set C only → `/swamp-tour-near-french-quarter`
- **Primary text:** You're already here. Tomorrow morning, trade Bourbon Street for two quiet hours in a cypress swamp. The van leaves 740 N Rampart St, so no car is needed and there's no rideshare hassle. Tours at 9:00, 11:30, 2:00 and 4:30.
- **Headline:** Van From the French Quarter
- **CTA:** Book Now
- **Creative brief:** 4:5 static. Morning-light cypress and moss photo from `Assets/Great new orleans kayak swamp tour photos/`. Minimal overlay: "740 N Rampart → the swamp." Test a version with the price after G3 clears.

### 4.2 Campaign: Locals

`NKST | M | Sales | Locals | Prospecting` → **`/kayak-swamp-tour-new-orleans`**

| Ad set | Audience |
|---|---|
| **A: Metro 50mi** | 50-mile radius around New Orleans, **people who live in this location**, ages 25–65. Advantage+ audience with suggestions: *Outdoor recreation*, *Kayaking*, *Birdwatching*, *Nature photography*. Exclude purchasers (180d). |
| **B: Local engagers** | IG engagers (90d) plus FB page engagers (90d), filtered by location to 50 miles. Exclude purchasers. |
| **C: Gift season** (Nov 15–Dec 24 only) → `/gift-cards` | 50-mile radius, 25–65, broad. Exclude purchasers from the last 30 days. |

**Concepts**

**L1: "The locals who've never been"** · A, B
- **Primary text:** You've lived here for years. You've heard the swamp stories. Have you actually paddled Manchac? It's about 35 minutes from the Quarter, two quiet hours with silent kayaks and a naturalist guide. Fall is the best season we have, and it books up fast.
- **Headline:** The Swamp in Your Backyard
- **CTA:** Book Now
- **Creative brief:** 9:16 Reel from Video B (group paddling under moss, POV). Hook text: "Lived here 10 years. Never been?" No VO. Ambient sound only, like slate spot B4. This draws on the pass-76 angle "the locals who've never been" (Ad Research). Pull its guardrails from that research doc.

**L2: "Winter birds" (seasonal, run Dec–Feb)** · A
- **Primary text:** When it cools off, the gators go quiet and the migratory birds show up. Herons, egrets, owls, and a guide who knows them by name. Winter tours run in the 40s–60s°F. Bring a layer.
- **Headline:** Winter in the Swamp
- **CTA:** Book Now
- **Creative brief:** 1:1 carousel of bird stills from `Assets/Clip Library/03 Wildlife`. Final card: "Silent kayaks, not airboats." Captions must be honest: these are birds you *may* see.

**L3: "Give the swamp" (gift)** · C only → `/gift-cards`
- **Primary text:** For the person who's done every restaurant in town: two quiet hours in a cypress swamp. Gift certificates arrive by email, and they pick the date.
- **Headline:** Swamp Tour Gift Certificates
- **CTA:** Shop Now
- **Creative brief:** 4:5 static. A gift-tag graphic over a cypress photo. Use the gift certificate design only once it's built in FareHarbor (Fact Sheet open question 4 covers the gift-card designs).

### 4.3 Campaign: Groups

`NKST | M | Leads | Groups` → **`/family-swamp-tours`**

| Ad set | Audience |
|---|---|
| **A: Family organizers** | US, 30–65, Advantage+ with suggestions: *Family reunion*, *Parents (kids 8–17)*, *New Orleans*. Instant Form: date, group size, occasion. |
| **B: Educators and group leaders** | US + LA, 28–65, suggestions: *Homeschooling*, *Scouting*, *Teachers*, *Field trip*. Instant Form. |

**Concepts**

**G1: "Your group, your guide"** · A, B
- **Primary text:** Family reunion, school trip, scout troop: we run private kayak tours for 4 to 20, just your group and a naturalist guide. Ages 8+, and under-16s paddle tandem with an adult. Groups of 13–20 run $105 per guest on the 2-hour tour. Tell us your date.
- **Headline:** Private Group Swamp Tours
- **CTA:** Get Quote
- **Creative brief:** 4:5 static or 9:16 short. A wide shot of a line of tandem kayaks, adults and kids together. **Gap:** the ad-research pass 36 notes that no tandem or family footage exists yet. Commission a shoot or use the best available small-group shot. Don't imply ages you can't show.

**G2: "The field trip they'll remember"** · B
- **Primary text:** A real Louisiana wetland classroom: cypress, wildlife, and why this swamp matters. Private tours for school and scout groups, with trained naturalist guides and a safety briefing on every trip.
- **Headline:** Swamp Field Trips
- **CTA:** Learn More
- **Creative brief:** 1:1 carousel: guide pointing out a cypress knee, a bird close-up, a group photo, and the "Two Swamps" restoration angle (Bayou Bienvenue and Sankofa CDC). Get approval before naming Sankofa.

### 4.4 Campaign: Private Events

`NKST | M | Leads | PrivateEvents` → **bachelor/bachelorette best-for page**

| Ad set | Audience |
|---|---|
| **A: Bachelorette planners** | US, women 24–38, suggestions: *Bachelorette party*, *Wedding planning*, *New Orleans*. Use the life event *Engaged (6 months)* and friends-of-engaged if Meta still offers them. Instant Form or Messenger. |
| **B: Travel-in party groups** | People traveling in New Orleans, 21–40, suggestions: *Bachelorette party*, *Bachelor party*, *Birthday*. **Coordinate with NPB,** which targets similar people. Exclude NPB's lead-form submitters (30d) if NPB wants the evening slot. |

**Concepts**

**P1: "Between the late nights"** · A, B
- **Primary text:** The weekend has enough brunches. Give your crew two quiet hours in a cypress swamp, with just your group and your guide. Private tours for up to 20. The van leaves the French Quarter, and you're back by the afternoon. Groups of 4–6 run $120 per guest.
- **Headline:** Bachelorette Swamp Tour
- **CTA:** Get Quote
- **Creative brief:** 9:16 Reel. A group of friends laughing in kayaks under moss, from `Clip Library/06 Guests & Social Proof`. Hook text: "The calmest part of the whole bach weekend." No alcohol shown on the water.

**P2: "Wedding weekend, day before"** · A
- **Primary text:** Out-of-town wedding guests asking what to do before the big day? A private swamp paddle works for every age, from 8 up. Tandem kayaks, calm water, and a naturalist guide. Up to 20 guests per tour.
- **Headline:** Wedding Welcome Day
- **CTA:** Get Quote
- **Creative brief:** 4:5 static of a mixed-age group in matching tees if available. Otherwise a wide group shot.

**P3: "Girls' trip" (review-led)** · A, B
- **Primary text:** A real, sourced guest review quote (pull from Google, with the reviewer's first name and permission policy checked). Then: private tours for your group, silent kayaks, and no experience needed.
- **Headline:** Your Crew, Your Own Guide
- **CTA:** Get Quote
- **Creative brief:** Review-overlay format (from the staged ad-script formats). The ad-research pass 36 found a real published "Girls Trip Guide to New Orleans" (Suiteness) that names NKST. The ad may say "as featured in" **only** if that's verified live.

### 4.5 Campaign: Fishing (GATED, G5)

`NKST | M | Sales | Fishing | Prospecting` → **`/kayak-fishing-new-orleans`** *(page doesn't exist)*

| Ad set | Audience |
|---|---|
| **A: Traveling anglers** | US ex-LA, 25–65, suggestions: *Fishing*, *Kayak fishing*, *Redfish*, *Bass fishing*, *New Orleans*. |
| **B: Local anglers** | 50mi, lives in, 25–65, suggestions: *Kayak fishing*, *Fishing*. |

**Concepts** (every fact needs verifying under G5)

**F1: "Water a boat can't reach"**
- **Primary text:** The best fishing around New Orleans is shallow, skinny water that a hull can't get near. We fish it from pedal-drive kayaks with a local guide who picks the spot by season and tide. Catches are never promised.
- **Headline:** Kayak Fishing New Orleans
- **CTA:** Book Now
- **Creative brief:** 9:16 Reel from the `Marketing/YouTube Scripts/Kayak Fishing the Bayou — Ep 1.md` footage if shot. Otherwise stills from `Assets/Photos/` ("aj kayak fishing.jpeg", "Kayak fishing in bayou sauvage.jpg"). **Don't use the "Louisiana [species] Fishing Tour.png" graphics** until their products are confirmed.

**F2: "Hands-free"**
- **Primary text:** Pedal-drive kayaks keep both hands on the rod. Rod, basic tackle and life jacket are included [VERIFY]. Freshwater bass and bream, or redfish and trout toward the marsh, depending on the season.
- **Headline:** Guided Bayou Fishing Charter
- **CTA:** Book Now
- **Creative brief:** 1:1 static, a POV shot over the kayak bow with a rod in frame.

### 4.6 Retargeting and Messenger (from the Master Plan, updated)

- Keep the Master Plan's 0–7d and 8–30d retargeting. **Update the copy:** replace "45 min from NOLA" with "about 35 minutes from the French Quarter" and "Spring dates" with the current season.
- **Add page-based retargeting splits** once the new pages are live. Visitors to the bachelorette page get P1. Visitors to `/family-swamp-tours` get G1. Everyone else gets the Master Plan's creative. The Extended and Combo upsells (Master Plan Phase 3) go to purchasers (180d).
- **Messenger (OpenCX / Magnolia):** keep it. *Note:* the Master Plan calls the bot "TideBot," but the Fact Sheet names the chat agent **Magnolia**. Use Magnolia.

### 4.7 PROPOSED Meta budget (Phase 1: $40/day, same as the Master Plan)

| Campaign | $/day | Notes |
|---|---:|---|
| Tourists (A $6 / B $4 / C $4) | 14 | Replaces TOF Prospecting ($20) |
| Locals | 5 | New |
| Private Events | 5 | New. Lead objective |
| Groups | 3 | New. Lead objective. Too low to exit learning, so judge on cost per lead, not the learning status |
| Retargeting | 10 | Unchanged |
| Messenger / OpenCX | 3 | Down from $10. Master Plan Phase 2 already planned $5 |
| Fishing | 0 | Gated |
| **Total** | **40** | ~$1,216/mo |

**Combined PROPOSED paid media:** Google ~$2,980 + Meta ~$1,216 = **~$4,200/month.** Check this against the 10%-of-gross-revenue ceiling each month, using FareHarbor gross, not ad-platform-reported revenue.

---

## 5. Fishing product check (summary of G5)

| Question | Known? | Source |
|---|---|---|
| Does a FareHarbor fishing item exist? | Yes (referenced) | Payroll Jul 16–31, Slack report Aug 1–15 |
| Has it been booked recently? | Unknown. One Dec 2025 email thread | FAQ Database |
| Price, duration, group size | **No** | — |
| Who guides it | Unknown. A guide named A.J. appears in fishing photos and the YouTube script | `Assets/Photos/aj kayak fishing.jpeg` |
| Launch location | Unknown. The draft mentions Bayou Bienvenue and Bayou Sauvage water | Staged draft |
| Licensing policy | Draft says anglers 16+ "most likely" need a license | Staged draft |
| Landing page | **No.** Only the staged draft `kayak-fishing-new-orleans-charter-guide` | Blog Drafts – Staged |

**Rule:** no fishing spend until every "No" and "Unknown" above is answered and the page is live.

---

## 6. Keyword-to-page quick reference

| Search intent | Campaign | Page |
|---|---|---|
| "new orleans kayak swamp tours" | Brand | `/` |
| "swamp tours new orleans" (out of state) | Tourists: Planners | `/first-time-new-orleans-swamp-tour` |
| "alligator tour new orleans", "manchac swamp tour" | Tourists: Planners | `/manchac-swamp-kayak-tour` |
| "kayak swamp tour new orleans", "eco tour" | Tourists: Planners / Locals | `/kayak-swamp-tour-new-orleans` |
| "family swamp tour", "swamp tour with kids" | Tourists: Planners / Groups | `/family-swamp-tours` |
| "swamp tour near me" (in city), "swamp tour pickup" | Tourists: In Town | `/swamp-tour-near-french-quarter` |
| "kayaking near new orleans" (resident) | Locals | `/kayak-swamp-tour-new-orleans` |
| "family reunion activities new orleans" | Groups | `/family-swamp-tours` |
| "new orleans bachelorette activities" | Private Events | best-for bachelorette page |
| "swamp tour gift certificate" | Gifts | `/gift-cards` |
| "kayak fishing new orleans" | Fishing (gated) | `/kayak-fishing-new-orleans` (to build) |

---

## 7. Conversion tracking requirements

**Owner:** David, with Kevin Schmitt (FareHarbor) for anything inside FareHarbor. Test every item by booking a real low-cost item in FareHarbor test or dashboard mode, then refunding it.

### 7a. FareHarbor purchase events

- [ ] **GA4 in FareHarbor:** confirm the NKST GA4 measurement ID is set in FareHarbor's analytics integration and that FareHarbor's checkout (lightframe on our domain) fires `purchase` with `transaction_id` (the FareHarbor booking ID), `value` (the booking total), `currency` = USD and `items` (item name, e.g. "Manchac Swamp Wildlife Kayak Tour").
- [ ] **Cross-domain:** the lightframe or fareharbor.com checkout must keep the GA4 session. Otherwise purchases show up as "(direct)" and the ads never get the credit. Test by clicking an ad-tagged URL (`?gclid=test`), booking, and checking GA4 DebugView.
- [ ] **Mark `purchase` as a key event** in GA4.
- [ ] **Why the Google action shows "Removed":** is it the GA4 key event being un-marked, the GA4↔Ads link, or FareHarbor's GA4 property? This is the #1 open question from the Oversight Checklist. Fix it, then re-import.

### 7b. GA4 → Google Ads

- [ ] Link GA4 ↔ Google Ads (CID 437-823-2023). Import `purchase` as the **Primary** conversion for the NKST campaigns. Use campaign-level conversion goals so NPB's `nolapedalbarges.com - GA4 (web) purchase` doesn't optimize NKST campaigns and vice versa.
- [ ] Turn on **enhanced conversions**, if FareHarbor exposes hashed email on the confirmation. Ask Kevin. If it doesn't, use GA4's user-provided-data collection.
- [ ] **Secondary (observe only):** `begin_checkout`, `view_item` (tour pages), calls ≥60 s, and `generate_lead`.
- [ ] **Lead (Primary for Groups / Private Events):** the inquiry form submit fires `generate_lead` on the thank-you state, plus the lead form asset and calls ≥60 s.
- [ ] **Offline conversions (Phase 2):** capture GCLID in a hidden field on the group and private inquiry form, store it in GHL, and upload the FareHarbor private booking value when the booking is made. Without this, Smart Bidding can't see that a $1,320 private came from an ad.
- [ ] **Attribution model:** data-driven (the Google default). Conversion window 30 days click, 1 day view.

### 7c. Meta Pixel + Conversions API (CAPI)

- [ ] **Pixel (GT Pixel 701301873334767):** PageView on every page, ViewContent on every tour and landing page, InitiateCheckout on the "Book Now" click, Purchase on the FareHarbor confirmation with `value`, `currency` and `content_name`, and Lead on the inquiry form or Messenger start. This is the Master Plan's Pixel Health Checklist, still open.
- [ ] **CAPI:** ask Kevin whether FareHarbor's Meta integration sends **server-side** Purchase events (CAPI) or browser-only. If browser-only, options in order of preference: (1) a FareHarbor-native CAPI setting if one exists, (2) a Meta CAPI Gateway, or GTM server-side on our domain fed by FareHarbor's booking webhook, (3) a Zapier-style bridge from the webhook to CAPI.
- [ ] **Deduplication:** browser and server events carry the same `event_id` (the FareHarbor booking ID), so Meta counts each booking once.
- [ ] **Domain verification:** verify neworleanskayakswamptours.com in Business Manager.
- [ ] **The Meta pixel audit** promised by FareHarbor's CRO team on May 6 has no recorded outcome. Get it in writing.

### 7d. UTMs (all paid and partner links)

```
Google:  auto-tagging ON (gclid). Also add a final URL suffix:
         utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}
Meta:    utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
Partner: utm_source=partner&utm_medium=referral&utm_campaign={segment}-{code}   (see 06 Partner Kit §3)
```

Partner and affiliate bookings are reported from FareHarbor's affiliate data, not GA4. Don't let a partner's QR booking count as an ad conversion (last-click with UTMs handles this).

### 7e. Sanity dashboard (weekly)

Three columns side by side: **FareHarbor online bookings (source of truth)**, **GA4 purchases**, and **Google Ads + Meta reported conversions.** If GA4 is more than 20% below FareHarbor online bookings, tracking is leaking. Fix it before judging any campaign.

---

## 8. Weekly optimization checklist (every Monday, about 45 minutes)

**Tracking first (5 min)**
- [ ] FareHarbor online bookings vs GA4 purchases vs platform conversions (§7e). Stop here if tracking is broken.
- [ ] Google: the conversion action status is "Recording," not "Removed" or "Inactive."
- [ ] Meta: Events Manager shows Purchase events in the last 24 hours, and the event match quality isn't falling.

**Google (20 min)**
- [ ] **Search terms report,** every campaign. Add negatives to the right shared list. Move good terms to Exact in the right ad group.
- [ ] Check the cross-campaign leakage: is a Locals term showing in In Town, or a Planners term in Brand?
- [ ] RSA asset ratings: replace "Low" assets after 2,000+ impressions, one or two at a time.
- [ ] Impression share, and lost to budget vs lost to rank, per campaign.
- [ ] Landing pages: speed, "Book" button working, prices matching ads (G3).
- [ ] Change history: log every change in this file's change log with date and reason. This matches the standard the SmartAds checklist holds the vendor to.

**Meta (15 min)**
- [ ] Frequency: prospecting ≤2.5 over 7 days, retargeting ≤5. Above that, rotate creative.
- [ ] Hook rate (3-second views ÷ impressions) and hold rate on Reels. Kill hooks under the bottom quartile of the account.
- [ ] Cost per result by ad set against the kill/scale rules (§9).
- [ ] Comments: answer questions within 24 hours in brand voice and hide spam. Comments are social proof on boosted posts.

**Business context (5 min)**
- [ ] Weather next 7 days. Pause same-day In Town bids on lightning days, and shift budget to later dates.
- [ ] Capacity: if a week's departures are close to full (FareHarbor forecast), cut prospecting for those dates and push the next open week.
- [ ] Season switches: Honey Island negatives (Oct 1 on, May 1 off), Gifts campaign (Nov 15 / Dec 24), winter-birds creative (Dec–Feb).

---

## 9. Kill / scale rules

*These are **thresholds**, not results. Starting targets use an assumed average order value that must be replaced with FareHarbor's real AOV in week 1.*

**Target CPA formula:** Target CPA = AOV ÷ 5, from the 5x ROAS floor. *Placeholder:* if AOV is $150 (for example 2 guests × $65 + a $25 shuttle for one — an assumption), target CPA is **$30**. The Master Plan's Meta "winner" line of CPA under $40 is close to this. Use the tighter number until real AOV is in.

### Google

| Rule | Trigger | Action |
|---|---|---|
| **Kill keyword** | Spend ≥ 2× target CPA with 0 conversions (after G1) | Pause it, or move it to Exact with a lower bid |
| **Kill ad group** | 30 days, spend ≥ 3× target CPA, 0 conversions | Pause it and check page-to-ad match |
| **Fix ad** | CTR < 3% on Exact core terms after 1,000 impressions | Rewrite the lowest-rated assets |
| **Pull back** | Campaign ROAS < 5x for 14 days (tracking verified) | Cut the budget 20%, and tighten keywords and geo |
| **Scale** | ROAS ≥ 5x for 14 days **and** lost IS (budget) > 10% | Raise the budget 20%, at most once every 7 days |
| **Hard stop** | Blended paid spend > 10% of FareHarbor gross revenue for the month | Freeze scaling and cut the lowest-ROAS campaign first |
| **Test end** | Comparison / Conquest after 30 days: CPA > 1.5× Planners | Kill it |

### Meta

| Rule | Trigger | Action |
|---|---|---|
| **Kill ad (Sales)** | $30+ spent with no Purchase (Master Plan rule), or CTR (link) < 1% after 1,000 impressions | Turn it off |
| **Kill ad (Leads)** | Cost per lead > $25 after $50 spend *(assumption: a private-tour lead is worth far more than a seat. Revisit after 10 leads)* | Turn it off |
| **Kill hook** | 3-second hook rate in the bottom quartile of the account after 2,000 impressions | Replace the first 3 seconds and keep the body |
| **Scale** | CPA ≤ target (or ROAS ≥ 5x) for 7 days | +20% budget every 3 days (Master Plan rule) |
| **Refresh** | Frequency > 2.5 (prospecting) or CTR drops 30% from its first-week level | New concept from the §4 bank or the staged script queue |
| **No-go** | Pixel Purchase not seen for 48 hours | Switch Sales campaigns to a Landing Page Views objective or pause them, and fix tracking |

---

## 10. Change log

| Date | Change | By | Reason |
|---|---|---|---|
| 2026-09-25 | File created (draft) | Claude | Growth Playbook Sept 2026 |

---

## 11. Contradictions found while building this

1. **Drive time.** The Fact Sheet says "about 35 minutes from the French Quarter." The Ad Copy Slate's correction says "30 minutes from Bourbon." The slate body, the end cards and the Meta Master Plan's "Tropical island" post say **15 minutes**. The Meta Master Plan and SEO audit say **45 minutes**. This file uses 35. Every "15 minutes" line in live or staged creative has to go.
2. **Tour length.** The Fact Sheet says "2 hours," then "2–2.5 hours on the water." The Master Plan and SEO audit say "2.5 hours." This file says "2 hours" / "2-hour." Settle one number in 00.
3. **Price.** $65 (vault) vs $69 (Google booking module) is open question 1. The ad-research passes also flag the live FAQ page listing **$59 self-drive / $79 with shuttle**, and the SEO audit cites "$65/$79/$195" on tour pages. So there may be **four** price points in public view. Every [PRICE] asset is blocked until one is picked.
4. **Domain.** The Ad Copy Slate end cards (30+ mentions across the vault) use **NolaKayakTours.com**. The Fact Sheet site is **neworleanskayakswamptours.com**. Confirm whether NolaKayakTours.com redirects. If it doesn't, the end cards send traffic nowhere useful.
5. **Review count.** 1,365 / 1,375 / 1,401 / 1,416 across docs. This file uses "1,400+," which is safe under the Fact Sheet's 1,401.
6. **Chat-bot name.** The Master Plan says "TideBot," and the Fact Sheet says **Magnolia** (OpenCX).
7. **Retired voice-breaker still in the testing doc.** Creative Testing Variant D ends with "guaranteed." It's retired here.
8. **Competitor conquest.** The SmartAds May 6 plan (5% coupon on a named competitor's terms) conflicts with the voice rule and is superseded here (§3.9).
9. **Gift URL.** The task and this playbook use `/gift-cards`, but the live page is `/gift-certificates/`.
10. **Fishing.** It's treated as "a real bookable product" in the staged draft and exists as a FareHarbor item, but it's not in the Fact Sheet and has no price anywhere in the vault.
11. **Jean Lafitte.** It's in the live `/tours/swamp/` title tag (SEO audit) but not a current tour per the Fact Sheet. Keep it out of ads.
12. **Honey Island.** The GBP and SEO plans chase the 9,900/mo "honey island swamp tour" keyword, but the Fact Sheet says the tour is summer only and gators are rare there. Paid search runs it only May–Sept.
