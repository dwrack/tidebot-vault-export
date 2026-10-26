# Houston Party Barge — Meta Deep Dive (2026-10-21)

Sources: Ads Manager (Buffalo Bayou/Houston account 1015419897308486), lifetime data for the ad "In-Market - Party Barge"; vault files read by a research agent (FareHarbor reports, Funnel Lab, Customer Voice, Organic Readout, Meta draft variants). Read-only: nothing was changed or published during this dive.

## Status after today's restart
Ad set "In-Market - Adult - Party Barge", $10/day, "Learning limited", spending again. Lifetime: $1,062 spent, 16 purchases, $3,940 value, 3.71x, $66 per purchase, **$246 average purchase**.

## Who the ad was built for and who actually bought
| Age | Spend | Purchases | Cost/purchase | Value | ROAS |
|---|---|---|---|---|---|
| 18–24 | $43 | 1 | $43 | $483 | 11.2x |
| 25–34 | $292 | 9 | $32 | $1,948 | 6.7x |
| 35–44 | $406 | 6 | $68 | $1,508 | 3.7x |
| 55–64 | $25 | 0 | – | $0 | – |
| 65+ | $0.17 | 0 | – | $0 | – |
| 45–54 | about $296 (not shown separately; this is the remainder) | 0 | – | $0 | – |

Ages 45+ are about $320 (30% of lifetime spend) with no purchases. Ages 25–44 account for 15 of the 16 purchases (9 + 6), and 18–24 for the other one.

| Gender | Spend | Purchases | Cost/purchase | ROAS |
|---|---|---|---|---|
| Women | $708 | 8 | $88 | 3.06x |
| Men | $346 | 8 | $43 | 5.13x |

Men got a third of the spend and half the purchases, at half the cost.

| Placement (partial; hidden rows not read) | Spend | Purchases | Cost |
|---|---|---|---|
| Facebook Feed | $545 | 8 | $68 |
| Instagram Stories | $118 | 1 | $118 |
| Facebook Stories | $22 | 1 | $22 |
| FB in-stream reels | $5 | 1 | $5 |
| Marketplace | $2.83 | 1 | $2.83 |
| Not read (remaining placements) | about $369 | 4 | about $92 |

Tiny placements with one purchase each are noise, not a signal.

## Facts that matter from the vault
- Public seat $55 (vault says $59–69); whole barge $800 up to 26 (vault says $800–950); 2 hours; BYOB; Bluetooth speaker; covered; restroom.
- 34 of 44 recent bookings were Saturday tours; 38% booked same day; median lead time 4 days (Oct 10 report).
- Average booking fell from $282 (May) to $195 (Oct). Forecast for the next 90 days is $9,867, 62% below last year, with $0 on the books on Sep 24. The file says to push, not trust it.
- 64% of online bookings have a blank booking-reference tag; GA4 shows 0 purchases. The Meta pixel is the only purchase signal.
- Only about 12 of the 26 seats are usable according to three reviews; 12 reviews say 2 hours felt short.
- Customers say "vibe", "boat ride", "cruise", rarely "party barge". Review lines that could become ad copy are in Customer Voice section 8.
- 35% of shopper chats ask whole barge vs seats; 76% of shopper chats ended with no booking link or contact.
- Bachelorette is about 2% of reviews; birthdays are 8%; friends/group 19%; corporate is 0.5% of reviews but 15% of chats.
- 9 draft Meta ad variants already exist (Marketing/Meta Ads — Draft Ad Variants, 2026-08-15). Best fits here: #5 birthday ($800 for up to 26), #8 BYOB bar-tab math, #9 "book private to skip cancellation risk".

## Problems with the current Party Barge ad
1. **One ad, one creative.** The ad set has a single ad, so nothing can be tested and creative fatigue can't be spotted.
2. **Generic copy.** "Book a private party barge and cruise with your crew, your drinks, and your playlist blasting. It's boat day." Headline "Perfect for birthdays, reunions, or just because." No price, no capacity, no night/sunset hook, no BYOB specifics, none of the review language.
3. **Running under the "Buffalo Bayou Kayak Tours" Facebook Page and Instagram profile (@buffalobayoukayak)**, not Houston Pedal Barge. The vault describes HPB as based in Clear Lake/Seabrook/Kemah with a FareHarbor item called "Houston Party Barge Cruise", and says no HPB-specific Meta data exists. The $246 average purchase fits HPB's $195–$283 average booking, but I could not read the ad's destination URL, so **which business's site and FareHarbor item this ad sends traffic to is unverified.**
4. **Budget too small to learn.** At $66 per purchase, $10/day buys about one purchase every six to seven days. Meta flags "Learning limited".
5. **Retargeting for Party Barge is off.** The three "RT - Party Barge" ads are all off ($1.68 total spend ever).
6. **Weak tracking behind the ad.** Blank reference tags on 64% of FareHarbor bookings; no GA4 purchases.

## Recommended changes (none applied yet)
1. **Confirm the ad's destination and the page owner** (see problem 3) before spending more.
2. **Narrow age to 25–44 (maybe 21–44)** — the data points there. Leave both genders in; women are two thirds of the spend and half the purchases, men are the cheaper buyers.
3. **Raise the budget** from $10 to $30–40/day to give Meta enough purchases to learn, or switch the optimization event to Initiate Checkout for more signal. Review after 7 days.
4. **Add 2–3 new ads in the same ad set** (same audience), each testing one idea: price anchor ($800 whole barge vs bar-tab math), the Saturday-night/sunset "vibe" angle in customer words, and a birthday angle.
5. **Fix the copy**: use real review language ("Bring your own bottle. Hook your music to their Bluetooth, and vibe out."), state capacity honestly, include the whole-barge-vs-seats answer, and show a price.
6. **Turn on Party Barge retargeting** ($5/day) once the prospecting audience has grown.
7. **Fix attribution**: use URL tags (e.g. `?ref=meta-pb-...`) so FareHarbor bookings can be matched to Meta.
8. **Seasonality**: push Saturday evenings and the holiday-party angle for November–December; the forecast is weak and there was nothing on the books on Sep 24.

## What was applied later on 2026-10-21 ("Do 1–6")
| # | Change | Result |
|---|---|---|
| 1 | Confirm Page and destination | Done. Page "Buffalo Bayou Kayak Tours"; destination `buffalobayoukayak.com/pedal-barge-party-cruise-in-houston/` with `utm_source=facebook&utm_medium=paid&utm_campaign=awareness_partybarge`. The page sells the same Seabrook barge ($59/seat ages 8+, $800 whole boat up to 26, BYOB, Bluetooth speakers, party lights, captain, 1 hr 45 min, 72-hour cancellation, FareHarbor). |
| 2 | Age 21–44 | **Done later the same day** after the pixel was connected (see update below). The ad set was 21–55; 45+ had spent about $320 with no purchases. |
| 3 | Budget $30/day | Done. Ad set now $30/day, status "Learning". |
| 4 | 3 new ad variants | **Done later the same day.** B Price Split, C Vibe and D Birthday are published in the same ad set (same creative as the original, new copy), in Meta review. Copy below. |
| 5 | Party Barge retargeting | Done. RT Party Barge Image 1, Image 2 and Video are on ($5/day); Image 1 delivering, the other two in Meta review. |
| 6 | URL tags | Done. Each variant carries `utm_content` (price-split, vibe, birthday). The destination URL already had utm_source/medium/campaign, and B and C repeat those three in the URL-parameter field (harmless duplicates); D adds only utm_content. |

### Update — pixel fixed, items 2, 4, 6 completed (2026-10-21)
Michael confirmed he is a full admin (Business Settings > People: Full access). The pixel 381452300055179 ("Buffalo Bayou Kayak Tours Pixel") was only connected to the Lone Star ad accounts; I connected the Buffalo Bayou/Houston ad account (1015419897308486) to it in Business Settings > Data Sources > Datasets & pixels. The pixel is shared with the Lone Star accounts, so datasets mix across brands. After that the age cap (21–44) and the three variants published. Note: the duplicated ads still show a "WhatsApp number required (#2446880)" warning in the editor; it did not block publishing. Meta also suggested raising the budget to $360/day; that was declined. Ad set is $30/day.

Final state: Party Barge ad set $30/day, ages 21–44; ads: original (Active), B Price Split, C Vibe, D Birthday (all in review). Family and General kayak ad sets off. Retargeting campaign on (two kayak ads + three Party Barge ads).

**Blocker:** Meta error #1815045: "Your ad account (1015419897308486) doesn't have access to this pixel (381452300055179). Go to the Data Sources menu in Business Settings to manage your pixels." Every ad set edit and new ad publish in this ad account fails until that pixel is assigned to the ad account. Budget changes and on/off toggles still work. Not touched: Business Settings, and I did not create a new dataset or change the optimization goal (either would break purchase tracking).

### Copy for the 3 variants (facts from the landing page)
1. **Price split** — Primary: "Planning a night out for the group? $800 gets your whole crew on a private party barge with a captain driving. Bring your own drinks and your own playlist. Split it between 20 friends and it's $40 a head." Headline: "$800 for the whole barge." Description: "📍Houston · BYOB". utm_content=price-split
2. **Vibe** — Primary: "Bring your own bottle. Hook your phone to the Bluetooth speakers and vibe out. 🎶 The party lights come on, a captain drives, and pedaling is optional. Book a private barge for your crew." Headline: "Your playlist. Your drinks. Your crew." Description: "📍Houston · Private party barge". utm_content=vibe
3. **Birthday** — Primary: "Birthday boat, sorted. 🎂 Bring the drinks, snacks and playlist. We bring the barge, the captain and the party lights. $800 for the whole boat, up to 26 guests." Headline: "Your birthday, your boat." Description: "📍Houston · $800 whole barge". utm_content=birthday

CTA "Book now"; URL: `https://buffalobayoukayak.com/pedal-barge-party-cruise-in-houston/?utm_source=facebook&utm_medium=paid&utm_campaign=awareness_partybarge&utm_content=<value above>`. Check the capacity claim first (three reviews say only about 12 seats are usable).

## Open questions for Michael / David
- Which Facebook Page and website should the Party Barge ads belong to?
- Is the second barge running (affects the "up to 26" claims and capacity)?
- Real price: $55 or $59–69 per seat; $800 or $800–950 per barge.
- Cancellation policy: 72 hours (live site) or 48 (vault).
