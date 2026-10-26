# GBP AI Calling Audit, 2026-10-16

**Bottom line (verified 2026-10-16):** Google's AI calling for bookings and price checks is NOT available in Louisiana, so the toggle does nothing for the 13 NOLA listings. It can work for WI, TX and OR. Toggle is NOT flipped yet: Google blocks sign-in in headless Chrome, and Profile 14 (dwrack81, the account that manages all 31 listings) is signed out in the mbp-2 bridge Chrome. One sign-in from David on mbp-2 unblocks it. No live profile edits made.

## What Google actually says
- Setting: "Google automated calls and text messages" in Business Profile settings > Advanced settings. It has 3 toggles: Bookings and inquiries from customers, Keep your profile up to date, Post to your profile on your behalf. ([help 7690269](https://support.google.com/business/answer/7690269?hl=en))
- US availability: "all states except Indiana, Louisiana, Minnesota, Montana, and Nebraska." No category list on the help page. Tours aren't named as included or excluded, so category eligibility is unknown. Third-party claims (home repair, beauty, pet care) aren't backed by Google's page.
- Default state isn't documented. Listing must be verified to change it.

## Per-brand table

| Brand (primary listing) | State | Toggle before / after | Eligible (state) | AI Mode test (logged out, 10/16) | Facts wrong / missing | Fix needed |
|---|---|---|---|---|---|---|
| Door County Kayak Tours | WI | unchecked / pending | Yes | Shows up #1 for "book a kayak tour in Door County for 4". $69 Cave Point correct, $250 private. Links to booking page. Didn't offer to call/book | 6 WI listings show open 7 days mid-Oct; Door County Tours open 24/7; Cave Point Kayak Tours no hours; GBP snippet "Open daily!" | Fall hours, kill 24/7, services with prices, FareHarbor link |
| NOLA Party Barge | LA | unchecked / pending | **No (LA)** | Says "$400 total for up to 6" (from a Facebook post + Viator). Site says from $59/person | Price AI repeats doesn't match site | Services with $59 public / private pricing so Google has a first-party number; OpenCX training says both $59 and $63 |
| New Orleans Kayak Swamp Tours | LA | unchecked / pending | **No (LA)** | Price answer correct ($65, $130, $195). Not shown for generic "book a swamp tour in New Orleans for 4" (Cajun Encounters, Viator, Agoda win) | No prices on GBP; http site link | Services + prices, https |
| Crescent City Kayak | LA | unchecked / pending | **No (LA)** | Correct $65. Says Extended Manchac is 6 hr (NOKST says 4-5 hr) | Duration conflict between sites | Align extended tour length |
| Houston Party Barge | TX | unchecked / pending | Yes | $55/person and $800 private up to 26, from own site. Mixed in competitors | Description says "Houston Booze Cruise" | Rename in description, services with unit (per person vs per boat) |
| Buffalo Bayou Kayak | TX | unchecked / pending | Yes | Correct $55-65, booking steps right | **GBP description still says "Coming soon. Waiting for gear to arrive."** | Replace description (urgent) |
| Lone Star / Austin Kayak Tours | TX | unchecked / pending | Yes | Lone Star #2 in the 4-operator list for "Austin kayak tour for 4 Saturday", no price shown | Lone Star has no description; shares phone with Austin Kayak; Austin Paddle Shack no hours; Austin Party Barge CLOSED_TEMPORARILY | Description, services, own phones |
| Ebb & Ember | OR | unchecked / pending | Yes | Gives memberships $99/$149 correctly, adds a "$400/month tier" (that's the 10-punch pass). Drop-in seat price $39-59 missing | Expired July 3 special hours | Add services: seats $39-59, private $449-539, punch passes |

"unchecked" = couldn't read the toggle (dashboard-only, no API field).

Other listings found (31 total under accounts/109075056374613070632): Cave Point Paddle and Pedal, Door County Tours, Door County Bicycle Rentals, Door County Kayak and Bike, Door County Kayak, Cave Point Kayak Tours (WI); Austin Paddle Shack, Austin Party Barge (TX); Honey Island, NO Party Boats, Plantation & Swamp Tours NO, Admire NOLA, Hidden Adventure, NO Booze Cruise, Freaky Tiki, NO Plantation & Swamp Tours, NOLA Bike Bar, NO Zip Line (LA). Also non-tour: Paradise Casino, Paradise Marina, HTX Clean, Apres La Vie.

## Across-the-board findings
- **Nobody gets AI booking or calling yet.** Every booking query got "I cannot directly process bookings" plus links. Zero offers to call a business.
- **Zero listings have a price in the description.** The API returned no services, products or booking-link data for any of them, so "no prices on GBP" isn't confirmed. Check in the dashboard when signed in.
- NO Zip Line listing's website is a GetYourGuide affiliate link. Point it to the FareHarbor Zipline + Kayak combo.
- Every special-hours block is expired. Nothing set for Thanksgiving, Christmas or NYE 2026.
- 4 phone numbers shared across 8 listings. 10 listings link http instead of https.

## OpenCX phone agents
- **No phone agent exists on any of the 6 brand orgs** (npb, nkst, dckt, hpb, bbk, lskt). So nothing answers calls today, Google AI or human.
- Website crawls are fresh (10/11-10/16) for every brand except NPB, which has no website datasource at all.
- No FareHarbor live-availability action on any org. NPB's training mentions one that isn't listed.
- NPB training conflicts: $59 vs $63 public price. HPB, BBK and LSKT have no custom training (no prices, no booking link).

## Pending David
1. Sign Profile 14 (dwrack81) into Google in the mbp-2 bridge Chrome via Screen Sharing. The tab is already open on that Mac. Then I flip the toggle on every listing.
2. Approve the per-brand GBP fixes below before anything goes live.

## Proposed GBP fixes (nothing applied)

**Door County Kayak Tours (#15, plus #4, #5, #6, #17, #25, #1)**
- Add service items with price: "Cave Point County Park Kayak Tour" from $69/person, "Cave Point and Whitefish Dunes 1/2 Day Kayak Tour" from $145, "Door Bluff Shipwreck Kayak Tour" from $69, "Door Bluff Shipwreck 1/2 Day" from $145, "Cave Point E-Bike Rental" $30/hr, "Cave Point Ebike Tour" from $99 (year round). Link: https://fareharbor.com/embeds/book/doorcountykayaktours/?full-items=yes&flow=968496
- Add appointment/reservation link to the FareHarbor URL above on #15 (primary) and #6 (ebike item 208420/221394).
- Hours: replace 7a-4p x7 with fall/winter hours (or "by appointment") once David confirms season end; e-bike tour is year round.
- Description: append "Tours from $69 per person. Book online." 
- Fix #5: remove 24-hour hours. Fix #4: add hours. Consolidate or differentiate the 4 WI duplicates; give each its own phone or all (920) 868-1400.
- #1: delete "New for 2020!"; #1/#6/#17/#25 to https and winter hours.

**NOLA Party Barge (#12; also #21 Freaky Tiki, #9, #19)**
- Services: "Freaky Tiki / Twerkin' Tiki / Bayou Boogie / Party Queen Swamp Party Cruise" from $59/person (1 hr 45 min); "Sunset Cocktail Cruise & Seafood Boil" from $165; "Swamp Eco Tour: Gators and Bayou Birds" from $50 (2 hrs). Book link base: https://fareharbor.com/embeds/book/neworleanspedalbarge/?full-items=yes&flow=970762
- Description: add "Public seats from $59 per person; private boats for 6-26 guests."
- Clear/replace expired Dec 2025-Jan 2026 special hours; add Thanksgiving/Christmas/NYE 2026.
- #21 Freaky Tiki: point website to nolapartybarges.com Freaky Tiki booking (item 340933) if that is the live seller, and give it its own phone (shares 308-1041 with Bike Bar).

**New Orleans Kayak Swamp Tours (#26; also #7, #11, #13, #16, #22)**
- Services: "Manchac Swamp Kayak Tour" from $65 (2-2.5 hr), "Extended Manchac Swamp Kayak Tour" $130 (4-5 hr), "Whitney Plantation and Swamp Kayak Combo" from $195 (8 hr), "Honey Island Swamp Kayak Tour" from $65 (summer only), "Self-Guided Kayak Rental (Bayou Bienvenue)". Book: https://fareharbor.com/embeds/book/neworleanskayakswamptours/?full-items=yes
- Website to https. Add "from $65" to description.
- #7 Honey Island: fix typos, https, note seasonal; hours daily 9-5 vs "summer only" conflict.
- #11 Plantation & Swamp: replace "Swamp Tour Street" with a real address or SAB (hide address).
- admirenola.com on three listings: pick one canonical listing or give each a distinct landing page.

**Crescent City Kayak (#27; also #16 neighbor)**
- Services: Manchac Swamp Tour from $65 (2 hr), Honey Island from $65, Swamp & Plantation Combo from $195 (8 hr), Zipline + Kayak Combo from $195 (8 hr), Extended Manchac $130. Book base: https://fareharbor.com/embeds/book/neworleanskayakswamptours/items/11242/calendar/
- Description currently says only "2 hour"; add range of options and "from $65".
- Website https.

**Houston Party Barge (#20)**
- Services: "Houston Party Barge Cruise" from $55 (confirm per person vs per boat first), "Christmas Themed Booze Cruise" from $59 (seasonal), "Firework Show and Party Barge" from $69. Book: https://fareharbor.com/embeds/book/houstonpedalbarge/?full-items=yes&flow=478443
- Description: rename "Houston Booze Cruise" to Houston Party Barge for consistency; add price with unit.

**Buffalo Bayou Kayak (#10)**
- URGENT: delete "Coming soon. Waiting for gear to arrive."
- Services: "Houston Bat Bridge Kayak Tour" from $60, "Skyline Kayak Tour" $55, "Sunrise Serenity Tour" $55, "Main Street Walking Bar Tour" $65, "Downtown Walking History Tour" $59, "Buffalo Bayou Regatta Rental" from $90. Book: https://fareharbor.com/embeds/book/buffalobayoukayak/items/calendar/?full-items=yes&bookable-only=yes
- Description: replace with "Guided kayak and walking tours downtown Houston from $55; rentals from $90." Bat season ends in Nov, so verify bat tour hours.

**Austin Kayak Tours / Lone Star (#2, #3, #8, #14)**
- Give each listing its own phone; #2 and #3 share 766-5640.
- #3: write a description (currently none), add services: "Austin Skyline Tour" from $50, "Austin Bat Tour by Kayak" from $50, "Paddle Board Bat Tour" $55, "Kayak and Paddle Board Rentals" from $20. Book: https://fareharbor.com/embeds/book/lonestarkayaktours/?full-items=yes
- #2: expand 1-line desc; https.
- #8 Austin Paddle Shack: add hours; description should describe rentals (it currently copies bat-tour text) or point site to lonestarkayaktours.com FareHarbor.
- #14 Austin Party Barge: CLOSED_TEMPORARILY; if still shut, set permanently closed or drop hours; if reopening, update.

**Ebb & Ember (#18)**
- Services: "Social Sauna" $49 off-peak / $59 peak per person, "Sunrise Sauna" $39, "Moonlight Sauna" $39, "Private Sauna (up to 10)" $449-$539, "Punch Pass" 3/$159 5/$245 10/$400, "Ember Membership" $99-$149/month.
- Booking link: add the Periode booking URL as appointment link: https://minside.periode.no/bookinggroups/wE4l5rKVuae2oCBE93gz/XBS8E3lQehtlsunpb5Kx/2025-11-09 (verify the date-stamped URL still works; the homepage links to dated paths, so prefer an undated booking-group URL).
- Description already strong; append "Seats from $39." Remove expired July 3 2026 special hours.

**Zip Line (#24, not in the top 8 but worst website)**
- Replace the GetYourGuide URL with the FareHarbor combo: https://fareharbor.com/embeds/book/neworleanskayakswamptours/items/373531/calendar/ (Zipline + Kayak combo from $195) or the NOKST homepage.


## Appendix: raw location audit
# GBP facts audit (read-only), checked live 2026-10-16

**Tool limit:** `gbp_get_location` returned NO `attributes`, `serviceItems`, `placeActionLinks` (url_appointment/url_reservations/booking), or `moreHours` for any of the 27 locations. So "booking link on profile" and "services with prices" are UNVERIFIED (field absent from response, not confirmed empty). Description text, hours, phone, website, status, special hours are verified. Q&A API is dead (501, discontinued 2025-11-03). Next step: pull Business Profile API `placeActionLinks.list` and `serviceItems` directly, or check in the GBP dashboard.

Legend: Desc$ = description mentions a price (none do, all 27 = No). "Call for quote" text = none found anywhere. Seasonal flag = regular hours show 7 days/week today (mid-Oct).

## Main table

| # | Location | Phone | Website (GBP) | Booking link / services (unverified) | Regular hours | Seasonal / stale hours | Status | Problems |
|---|---|---|---|---|---|---|---|---|
| 1 | Cave Point Paddle and Pedal (WI) | (920) 473-4051 | http://www.cavepointpp.com/ | not returned | 7a-6p x7 | WI mid-Oct 7 days = likely stale; special hours all 2023-24 expired | OPEN | http; desc says "New for 2020!" (stale); old site/brand, overlaps DCKT |
| 2 | Austin Kayak Tours (TX) | (512) 766-5640 | http://www.austinkayaktours.com/ | not returned | 7a-7:30p x7 | ok for TX; special hours 2022 expired | OPEN | http; phone SHARED with Lone Star; desc is 1 line, no price/duration |
| 3 | Lone Star Kayak Tours (TX) | (512) 766-5640 | http://www.lonestarkayaktours.com/ | not returned | 10a-6p x7 | ok; special hours 2021 expired | OPEN | http; NO description at all; no address (SAB); phone SHARED with Austin Kayak Tours; FareHarbor account is lonestarkayaktours but austinkayaktours.com site books on it too |
| 4 | Cave Point Kayak Tours (WI) | (920) 282-2811 | https://www.doorcountykayaktours.com/ | not returned | NONE | missing | OPEN | no hours, no address; 3rd phone for the DCKT site; desc has no price |
| 5 | Door County Tours (WI) | (920) 363-6789 | https://www.doorcountykayaktours.com/ | not returned | 24 hours x7 (00:00-24:00) | WRONG (24/7); special hours 2019 | OPEN | hours 24/7 is false; phone SHARED with #6; bus tour category; desc has no price |
| 6 | Door County Bicycle Rentals and Tours (WI) | (920) 363-6789 | https://www.doorcountykayaktours.com/e-bike-tours/ | not returned | 7a-6p x7 | WI mid-Oct stale likely; special hours 2019-2021 expired | OPEN | title has trailing period; phone SHARED with #5; deep link ok but site has no e-bike rental hours/price in GBP |
| 7 | Honey Island Swamp Kayak Tours (LA) | (504) 717-4977 | http://honeyislandswampkayaktours.com/ | not returned | 9a-5p x7 | NOKST site says Honey Island tours are summer only, GBP says daily; Dec25-Jan26 special hours expired | OPEN | http; desc typos ("availble", "Olreans"); no price; "transportation available" with no price |
| 8 | Austin Paddle Shack (TX) | (512) 580-9401 | http://www.austinpaddle.com/ | not returned | NONE | missing | OPEN | no hours; http; desc is the Austin Bat Tour text (different brand voice, no price); different domain from the 2 Austin kayak listings |
| 9 | New Orleans Party Boats (LA) | (504) 264-6046 | https://neworleanspartyboats.com/ | not returned | 9a-8p x7 | Dec25-Jan26 special hours expired | OPEN | 3rd NOLA party-boat site/phone beside NOLA Party Barge (264-1056); desc no price; address 2360 N Villere |
| 10 | Buffalo Bayou Kayak Tours & Rentals (TX) | (832) 305-5794 | https://www.buffalobayoukayak.com/ | not returned | 9a-6p x7 | Dec25-Jan26 special hours expired | OPEN | **desc says "Coming soon. Waiting for gear to arrive."** (false, site sells tours $55-$90); no price |
| 11 | Plantation & Swamp Tours New Orleans (LA) | (504) 226-8012 | https://www.admirenola.com/ | not returned | 7a-6p x7 | special hours expired | OPEN | address is literally "Swamp Tour Street" (fake); same website as #13 and #22 (3 listings -> 1 site); no price |
| 12 | Nola Party Barge - Swamp Tour Party Boat (LA) | (504) 264-1056 | https://www.nolapartybarges.com/ | not returned | 10a-9p x7 | special hours expired (Dec25-Jan26) | OPEN | best desc of the set but no price; phone matches site |
| 13 | Admire New Orleans (LA) | (504) 608-5322 | https://www.admirenola.com/ | not returned | 7a-8:30p x7 | special hours expired | OPEN | no storefront address; same site as #11, #22; desc says "world's best boat tour" (superlative); no price |
| 14 | Austin Party Barge (TX) | (512) 348-7369 | https://austinpedalbarge.com/ | not returned | 7a-8p x7 | n/a | **CLOSED_TEMPORARILY** | name says Party Barge, domain says pedalbarge; hours still shown while closed; no price; decide reopen/permanent close |
| 15 | Door County Kayak Tours (WI) | (920) 868-1400 | https://www.doorcountykayaktours.com/ | not returned | 7a-4p x7 | **WI mid-Oct 7 days = stale**; special hours 2023 expired | OPEN | phone SHARED with #17; site homepage shows no hours; "#1 rated" claim; no price |
| 16 | Hidden Adventure Swamp & Plantation Tours (LA) | (504) 534-5527 | http://www.hiddenadventuretours.com/ | not returned | 8a-8p x7 | special hours expired | OPEN | http; address 435 Esplanade is next door to Crescent City Kayak (437 Esplanade); different domain/brand; no price |
| 17 | Door County Kayak and Bike (WI) | (920) 868-1400 | http://docokayakbike.com/ | not returned | 8a-6p x7 | **WI mid-Oct stale** | OPEN | http; phone SHARED with #15; different domain (docokayakbike.com); desc 1 line, no price |
| 18 | Ebb & Ember Floating Saunas (OR) | (503) 308-1293 | https://www.ebbandember.com/ | not returned (site books on minside.periode.no) | 6a-10p x7 | matches site "daily 6am-10pm"; special hours 2026-07-03 expired | OPEN | **no price in desc** though site has $39-$59/seat, $449-$539 private, memberships $99/$149; booking is non-FareHarbor (Periode) so confirm a booking link exists |
| 19 | New Orleans Booze Cruise (LA) | (504) 507-8644 | https://nolaboozecruise.com/ | not returned | 8a-9p x7 | special hours expired | OPEN | 3rd NOLA party-boat brand; desc written in 3rd person; no price |
| 20 | Houston Party Barge (TX) | (832) 974-0365 | https://www.houstonpedalbarge.com/ | not returned | 8a-10p M-Th, 8a-11:30p F/Sa/Su | special hours expired | OPEN | desc says "Houston Booze Cruise" (name mismatch); domain "pedalbarge"; no price |
| 21 | The Freaky Tiki (LA) | (504) 308-1041 | https://nolaboozecruise.com/the-freaky-tiki/ | not returned | 10a-6p x7 | special hours expired | OPEN | phone SHARED with NOLA Bike Bar (#23); but nolapartybarges.com sells "The Freaky Tiki from $59" (NPB site) while this listing sends to nolaboozecruise.com; no price |
| 22 | New Orleans Plantation & Swamp Tours (LA) | (504) 226-5402 | https://www.admirenola.com/ | not returned | 7a-7p x7 | special hours expired | OPEN | 3rd listing on admirenola.com; 2nd phone (226-5402 vs 226-8012); no address; no price |
| 23 | NOLA! Bike Bar (LA) | (504) 308-1041 | https://www.nolabikebar.com/ | not returned | 8a-8p x7 | special hours 2023-24 expired | OPEN | phone SHARED with Freaky Tiki; "Lousiana" typo in desc; no price |
| 24 | New Orleans Zip Line Tour (LA) | (504) 285-2593 | **https://www.getyourguide.com/...zipline...?partner_id=8M6T7L0&utm_medium=online_publisher** | not returned | 8a-8p x7 | special hours expired | OPEN | **website is a GetYourGuide affiliate link** (leaks commission, sends AI agents to a competitor listing); no address; desc no price |
| 25 | Door County Kayak (WI) | (920) 471-4820 | http://www.doorcountykayak.com/ | not returned | 9a-6p x7 | **WI mid-Oct stale** | OPEN | old competitor-style brand? primary category "Tourist attraction"; http; desc says "call ahead", "reservation only" (closest thing to call-for-quote); 4th WI phone |
| 26 | New Orleans Kayak Swamp Tours (LA) | (504) 571-9975 | http://www.neworleanskayakswamptours.com/ | not returned | 7a-7p x7 | has 2027-02-09 closed (Mardi Gras) = good | OPEN | http; desc no price; phone matches site |
| 27 | Crescent City Kayak - Swamp Tours (LA) | (504) 434-2860 | http://www.crescentcitykayak.com/ | not returned | 8a-8p x7 | special hours expired | OPEN | http; desc says "2 hour" tour but site has 2h/4-6h/8h options; no price |

## Cross-profile problems

**Shared phone numbers**
- (512) 766-5640: Austin Kayak Tours + Lone Star Kayak Tours
- (920) 363-6789: Door County Tours + Door County Bicycle Rentals and Tours
- (920) 868-1400: Door County Kayak Tours + Door County Kayak and Bike (and it is the number on doorcountykayaktours.com)
- (504) 308-1041: The Freaky Tiki + NOLA! Bike Bar
- WI profiles pointing at doorcountykayaktours.com: #4, #5, #6, #15 (4 listings, 4 different phones, site shows (920) 868-1400)
- admirenola.com: #11, #13, #22 (3 listings, 3 phones)

**Wrong or risky websites**
- #24 Zip Line: GetYourGuide affiliate URL
- http (no TLS): #1, #2, #3, #7, #8, #16, #17, #25, #26, #27

**Stale text**
- #10 "Coming soon. Waiting for gear to arrive."
- #1 "New for 2020!"
- #5 open 24 hours
- WI seasonal: #1, #6, #15, #17, #25 (and #5) show open 7 days in mid-October. Door County season is effectively over except ebike year-round; set winter hours or mark by appointment.
- Every special-hours block is expired (Dec 2025 - Jan 2026 for LA/TX; 2019-2024 elsewhere). Only #26 has a future one. No Thanksgiving/Christmas/NYE 2026 set anywhere.

**Missing hours:** #4 Cave Point Kayak Tours, #8 Austin Paddle Shack.

**Price in description:** 0 of 27. **Call-for-quote text:** none (only #25 "call ahead", "reservation only").

## Website headline prices (one WebFetch each, 2026-10-16)

| Brand | Site | Headline prices | Booking | Site phone | GBP phone match |
|---|---|---|---|---|---|
| Door County Kayak Tours | doorcountykayaktours.com | Cave Point Kayak Tour from $69; Cave Point + Whitefish 1/2 day from $145; Door Bluff Shipwreck from $69; Door Bluff 1/2 day $145; E-bike rental 1h $30 / 2h $60 / 3h $90; Cave Point Ebike Tour from $99 (year round) | FareHarbor `doorcountykayaktours` | (920) 868-1400 | #15 yes; #4/#5/#6 no |
| NOLA Party Barge | nolapartybarges.com | Freaky Tiki / Twerkin' Tiki / Bayou Boogie / Party Queen from $59; Sunset Cocktail Cruise & Seafood Boil from $165; Swamp Eco Tour from $50 | FareHarbor `neworleanspedalbarge` | (504) 264-1056 | #12 yes |
| New Orleans Kayak Swamp Tours | neworleanskayakswamptours.com | Manchac Swamp Kayak from $65; Extended Manchac $130 (was $195); Whitney Plantation + Swamp combo from $195; Honey Island from $65 (summer only); BYOB Swamp Party Cruise from $59; monthly pass $65 | FareHarbor `neworleanskayakswamptours` | (504) 571-9975 | #26 yes |
| Crescent City Kayak | crescentcitykayak.com | Manchac $65; Bayou Boogie $59; Plantation + Swamp combo $195; Zipline + Kayak combo $195; Honey Island $65; Extended Manchac $130 | FareHarbor (same NOKST account) | (504) 434-2860 | #27 yes |
| Houston Party Barge | houstonpedalbarge.com | Party Barge Cruise from $55; Christmas Booze Cruise from $59; Fireworks + Party Barge from $69 (per person vs per boat NOT stated) | FareHarbor `houstonpedalbarge` | (832) 974-0365 | #20 yes |
| Buffalo Bayou Kayak | buffalobayoukayak.com | Bat Bridge Kayak from $60; Skyline Kayak $55; Sunrise Serenity $55; Walking Bar Tour $65; Walking History Tour $59; Regatta Rental from $90 | FareHarbor `buffalobayoukayak` | (832) 305-5794 | #10 yes |
| Austin Kayak / Lone Star | austinkayaktours.com | Skyline Tour from $50; Bat Tour by Kayak $50; Paddle Board Bat Tour $55; 4th of July Fireworks $85; Kayak and SUP rentals from $20 | FareHarbor `lonestarkayaktours` | 512-766-5640 | #2/#3 yes (both) |
| Ebb & Ember | ebbandember.com | Social Sauna $49 off-peak / $59 peak per person; Sunrise and Moonlight $39; Private party (up to 10) $449 / $539; punch passes 3/$159, 5/$245, 10/$400; memberships $99 and $149/mo | Periode (minside.periode.no), not FareHarbor | (503) 308-1293 | #18 yes |

Note: neither site homepage lists operating hours, so GBP hours cannot be cross-checked against site text (only Ebb & Ember publishes "daily 6am-10pm", which matches).


## Appendix: OpenCX audit
OpenCX audit, read-only, run 2026-10-16

| Brand | Phone agent? | Number | Price answer | Booking link | Live availability | Website crawl (last) | Gaps |
|---|---|---|---|---|---|---|---|
| NPB (NOLA Party Barge, NBB) | NO (list empty) | none | Partial: custom training says $350 private deposit, "$59/person public, $800 private" examples, "only $63" phrasing (inconsistent $59 vs $63, unverified) | Yes, training says lead with booking link when date given | Training references fare_harbor_action_check_availability, but list_actions shows only Update Contact; action not visible via MCP (unverified) | NO datasource at all | No website crawl, no phone agent, price inconsistency, FH action not in actions list |
| NKST (Crescent City / Honey Island) | NO | none | NO. Search returned only crawled pages (cookie-banner text, 404 "Page Not Found" pages), no prices | Only a training note "booking link availability", no actual URL | No (only Update Contact action) | 2026-10-11 (5 days), 384 pages | No prices, crawled 404 pages and cookie banners pollute KB, no FH availability action |
| DCKT (Door County) | NO | none | NO. Only crawled pages (404 blog image pages, cookie text) | Training: send booking link with earliest slot preselected; no URL in KB | No | 2026-10-15 (1 day), 232 pages | No prices, 404 pages crawled, no availability action |
| HPB (Houston Pedal Barge) | NO | none | Unclear. Crawled blog "How much does it cost to rent a party boat" exists, preview is only cookie text; zero custom training | None | No | 2026-10-12 (4 days), 52 pages | No custom training at all, no booking link, no availability |
| BBK (Buffalo Bayou) | NO | none | NO (crawled pages only, previews are cookie text) | None | No | 2026-10-15 (1 day), 53 pages | No custom training, no prices, no booking link, no availability. Crawled "Page Not Found" Kemah page |
| LSKT (Austin Kayak / Paddle Shack / Lone Star) | NO | none | NO (crawled pages only) | None | No | 2026-10-16 (today), 165 pages | No custom training, no prices, no booking link, no availability. Stale 2018/2021 blog posts in KB |

Notes
- No crawl older than 60 days (oldest is NKST, 5 days). All datasources active, 168h interval, no errors.
- Zero phone agents on any of the six servers. Any "phone agent" use today is not configured.
- Only action on every brand: Update Contact (contact PATCH/PUT). No FareHarbor availability action visible on any brand. NPB training text names fare_harbor_action_check_availability, so it may be a native/integration tool not exposed via list_actions; verify in the OpenCX dashboard.
- Website content previews are dominated by cookie-consent boilerplate, so price content may exist deeper in page text; search ranking was low (scores 9-16) for price queries. Treat "no price" as "not surfaced", not proven absent. Use include_content=true on one page per brand to confirm.
- Custom training depth: NPB best (pricing, deposits, sold-out, times, booking link), NKST/DCKT minimal (booking-order rules, dog, bathroom), HPB/BBK/LSKT none found.
