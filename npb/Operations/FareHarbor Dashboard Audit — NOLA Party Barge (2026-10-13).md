# FareHarbor Dashboard Audit: NOLA Party Barge (2026-10-13)

Read-only audit of the neworleanspedalbarge dashboard against the FareHarbor capability map. Every status below is "as read from the dashboard on 2026-10-13" unless it says otherwise. One live check was added: Meta pixel stats pulled 2026-10-13.

**Read this first: what the dump can and cannot see.** The dump is innerText, so it captured labels, lists and audit logs but not form values. Four things follow:
- Item tabs Options & Prices, Availability and Communication came back empty or "Not found" for all 20 items. Prices, customer type setup, reminder timings and notification toggles per item are therefore not readable.
- Online Booking tabs show the form layout but not the values (cutoff hours, min/max, sold-out text, deposit amounts, checkbox states). I inferred on/off only where a field's presence changes the layout, and I say so.
- Text areas (company policies, confirmation notes, cancellation notes) are blank in the dump. That does not mean they are empty.
- Canned Messages, Booking Flows and the Waivers signed list showed "Loading...". Bank & Payments sub-tabs returned "Not allowed" for the logged-in user.

Where the audit logs (Recent Activity and per-item history) gave real evidence, I used them. They are the best source in the dump.

**Business snapshot from Reports (read 2026-10-13):** last 7 days 60 bookings (down 43.4% vs last year), 178 pax (down 55.4%), $8,677.03 gross (down 65.5%). 2026 booking total paid $1,140,359.18, 72.32% of last year (down 22.6%). Booking source this week: Online Direct 59, FHDN API 1. Next payout $740.83 scheduled 2026-10-13. Customer directory: 53,655 customers. Insights and Opportunities says 10 opportunities are waiting.

---

## 1. Top 10 fixes, ranked by revenue impact

| # | Fix | On now (as read 2026-10-13) | Switch on / change | Where | Effort |
|---|---|---|---|---|---|
| 1 | Abandoned cart email and online cart | Nothing in the dump shows either. Meta shows InitiateCheckout firing only a few times a day (about 25 in the week of Oct 6 to 12) against roughly 90 Purchase events, so most carts are not being measured or chased. | Verify and enable Orders and online cart, then Abandoned cart recovery. FareHarbor sends one email 2 hours after drop-off. It cannot be customized. | Dashboard gear (Advanced company settings) > Bookings / Abandoned cart. Online cart may need Support. | 15 minutes to check, Support if cart is off |
| 2 | Sell add-ons on private boats as priced custom fields, and rebuild "Private Shuttle" | The Custom Fields page shows six plain text questions only (weight, group size, where visiting from, recipient fields, bow fishing level). No priced add-ons. "Private Shuttle" is a $400 customer type with note "15 passengers max". Combos: 0. Cross-sell partners: none. Suggested items: selections not readable. | Create priced checkbox/dropdown fields for shuttle, cooler and ice, speaker or DJ, decorations, photo package. Keep Private Shuttle out of the customer-type list so it stops counting as a head. Add 1 to 3 combos or suggested items on the confirmation page. | Settings > Custom Fields > New custom field; item > Options & Prices > whole-booking fields; Settings > Suggested Items; Settings > Combos | 2 to 4 hours. Customer type edits can break OTA/API connections, so run them past Support first |
| 3 | Jingle on the Bayou has no availabilities | Bookability On, added to 2 booking flows, "Create availabilities" row shows no future-availability count (every other live item shows one). | Create the December dates, or switch bookability off until they exist. A live item with nothing to book is a dead end for anyone who finds it. | Items > Jingle on the Bayou > Availability; Availability Schedules | 20 minutes |
| 4 | Stop hand-toggling closed / call / waitlist, and confirm the pontoon is not mostly shut | The audit log shows Jeff changing statuses by hand across the six main items at least 12 times in 9 days (e.g. closed 10/8 9:41 AM, call 10:59 AM, crew added 1:07 PM; waitlist set again today at 7:33 AM). On 9/26 he closed 634 Luxury Pontoon availabilities. No empty-departure auto-close rule is visible on the tiki boats (the pedal tours show "9:00 PM 1 day before"). | Move the closing logic into rules: a "No bookings" auto-close time vs a "1+ bookings" time, a custom sold-out message, and let crew assignment drive readiness. Confirm the 634 pontoon closures are intentional. | Item > Booking > Bookability > Booking Restrictions; Items > Availability updater | 2 hours, plus a 10 minute question to Jeff |
| 5 | Replace low-quality photos on the money items | "Item using low-quality images" flag on Twerkin' Tiki, Bayou Boogie, Party Queen, Luxury Pontoon, EcoTour, Seafood Boil, both pedal tours, Walk on the Wall Side, Jingle, both gift items. Freaky Tiki is not flagged. | Upload 5 or more photos at 1800px wide, 10 at a time. Photos feed Lightframe, Marketplace score, Google Things to Do and OTAs. | Items > item > Listing > Photos | 1 to 2 hours plus shoot or export time |
| 6 | Review requests and reminders on every customer-facing item | Michael set a follow-up on 9/24/26 for Seafood Boil and Birding: "Review Request - All Trips (Follow-up)", 2 hours after start or end. The visible logs for the six main boats show no follow-up change, so those may be unset. Google review URL and survey URL live on Info & Policies > Social Media, which was not captured. | Copy the same follow-up to Freaky, Twerkin', Boogie, Queen, Pontoon, EcoTour. Confirm the Google review link is in Social Media. Turn on reminder emails and texts. | Items > item > Settings > Notifications; Settings > Info & Policies > Social Media; Canned Messages | 45 minutes; texting needs Support to enable |
| 7 | Attribution cleanup | "How did you hear about us?" was removed from the Default custom field group by FareHarbor on 3/5/26. Eleven GA4 streams are attached; four fire on all FareHarbor pages including other brands' IDs. Meta CAPI is set up, but its Source URL is nolapedalbarge.com, the old domain. | Re-add a required "How did you hear about us?" dropdown. Remove GA4 streams that are not NPB. Update the CAPI Source URL to nolapartybarges.com. Add the Online ref tag to every embed. | Settings > Custom Fields; Settings > Analytics & Tracking; Settings > Book Buttons & Embeds | 1 hour (GA4 removals need a quick decision first) |
| 8 | Deposits and balance links on private charters | Deposit fields are visible (so deposits appear on) for Freaky, Twerkin', Boogie, Queen and EcoTour. Pontoon and Seafood Boil show "Allow deposits" with no amount fields (so off). VIP Client Party had a $350 deposit offset removed in 2023. Amounts and "require deposit" states are not readable. | Confirm the deposit amount on each private product, turn deposits on for the pontoon, make sure the balance payment link is live for group planners. | Item > Booking > Bookability > Online Payments | 30 minutes |
| 9 | Midweek price schedule or dynamic pricing pilot | Price sheets: Online, Direct, Direct | No Deposit, GYG, Who2Call. Price Planner page empty. No sign of price schedules. Public seat prices look flat at $59 or $63. | Ask Support about price schedules with capacity or time rules for Tue to Fri public seats only. Leave private boats alone. | Settings > Price Sheets > Price Schedules; Support builds it | Needs Support |
| 10 | Distribution check-up: Google Things to Do, FHDN, Marketplace | An affiliate record exists for Google, FHDN, FHDN API, GetYourGuide, Viator and Tripadvisor, but only 1 of 60 bookings this week came from FHDN API. Affiliate Rule blocks FHDN on 1 item. Marketplace quality score is hurt by the photo flag. | Ask Support whether Things to Do is live and for which 10 items, whether ChatGPT eligibility follows the FHDN opt-in, and which item the FHDN block covers. | Settings > Integrations > OTA Connections; Affiliate Rules | Needs Support |

---

## 2. The 100-question checklist

Statuses: On, Off, Partial, Can't tell from dump, N/A. "Q hist" means the item's audit log. Quotes are from the dump file named.

### Items and availability

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | Item Setup Checklist green? | Can't tell | Overview lists "Complete / Using defaults / Incomplete" without state icons. 7 items show "Using default cancellation notes". | Open each of the six boats and screenshot the checklist. |
| 2 | Content Builder description and 5+ photos at 1800px? | Partial | "Item using low-quality images" on 12 of 20 items (not Freaky Tiki). | Fix per Top 10 #5. |
| 3 | Retail items set as retail? | On | "Retail item" label under Gift Card, Gift Certificates, Retail. | None. Gift Certificates is Private with 0 flows: archive when unused. |
| 4 | Availabilities from schedules, next year duplicated? | On | "Duplicated 365 availabilities to 2027" (FareHarbor, 7/7/26); boats show 1,439 to 2,783 future availabilities. | Jingle on the Bayou has none: see Top 10 #3. |
| 5 | Cutoffs per item, empty vs booked? | Partial | Pedal tours: "9:00 PM 1 day before" on No bookings. Birding "8:00 PM 1 day before", Jingle "2:00 PM 1 day before". Tiki boats show no cutoff text. | Set no-bookings and booked cutoffs on the six boats. |
| 6 | Negative cutoffs or Open override for last-minute? | Can't tell | No cutoff values captured. | Ask Jeff whether same-day booking after start is ever needed. |
| 7 | Custom sold-out message? | Partial | "Call to book / Message" fields present on most items; Bayou Boogie and Gift Card layouts lack the Message field. Text not captured. | Set "Sold out, call or text us" text; align Boogie. |
| 8 | Waitlist enabled on full-prone items? | Partial | "Full or overbooked ... Waitlist" option present; Jeff sets status to waitlist often. Auto seat-opened email not visible. | Confirm auto-email is on in company settings. |
| 9 | Reservation timer? | Can't tell | Not shown. | Ask Support; useful on Halloween weekend. |
| 10 | Boats and crew as resources? | On | Resources: Freaky Tiki Vessel 25, Mega Pedal Bike Barge 22, Bayou Cruiser 1 and #2, Online Boat Seats 18, Offline Boat Seats 8, Shuttle 1 (page 1 of 2 only). Captain and Deck Hand assigned in the calendar. | Rename legacy resources; read page 2. |
| 11 | Seat maps? | N/A | No seat map evidence; tikis sell by boat or seat. | Skip. |
| 12 | Capacity per customer type? | Can't tell | Not captured. | Check Private Charter and Private Shuttle on each boat. |
| 13 | Private charter types exclusive? | Can't tell | "Private Charter" type exists; pontoon shows capacity 1. | Verify exclusive flag so min/max party size does not interfere. |
| 14 | Public headlines with photos? | Partial | 2 headlines, no photos. Availability headlines in use: "HALLOWEEN BOAT PARTY!!!", "Networking Night for Business Owners", "BLACK N' TAN", "NAVY N' GRAY". | Add photos to headlines; retire the 2023 "SPOOKY SEASON" one after Halloween. |
| 15 | Flows structured so new items are added? | Partial | 14 flows on Freaky, including six "ASN Pedal + Swamp (name)" affiliate flows. Default Booking Flow lacks Pontoon, EcoTour, Seafood Boil. | Prune legacy affiliate flows; decide what the Default flow should show. |

### Pricing and fields

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 16 | Price sheets deliberate? | On | Online, Direct, Direct \| No Deposit, GYG, Who2Call (Online); invoice sheets Billing 15/25, Referral 10/15/20 (FHDN). | Fine. Remove sheets with no affiliate. |
| 17 | Price schedules as company default? | Can't tell | Price Schedules tab not captured; Price Planner page empty. | Ask Support. |
| 18 | Dynamic Pricing 2.0 discussed? | Can't tell | No evidence. | Top 10 #9. |
| 19 | Price previews including fees and taxes? | Can't tell | Not captured. | Ask Support. |
| 20 | Add-ons as priced custom fields? | Off | Custom Fields page lists only text inputs; "Bottle Service Packages" header on venue rental removed 11/5/25. | Top 10 #2. |
| 21 | Conditional fields? | Can't tell | Not captured. | Use to hide corporate questions on public seats. |
| 22 | Adjustable pricing for staff? | Can't tell | Not captured. | Useful for comps; check permission. |
| 23 | Tax types correct? | Can't tell | Tax tab not captured. | Have the accountant confirm. |

### Bookings, check-in and operations

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 24 | Check-in with custom statuses? | On | "Checked in", "Checked In - Signed Waiver", "No show", "Late Arrival - 5 past the hour". | Check auto no-show. |
| 25 | QR scanning per item? | Can't tell | Multi-scan: no rules. Item QR toggle not captured. | Low priority. |
| 26 | Saved manifests as defaults? | Can't tell | New Manifest "still in preview". | Save a captain manifest. |
| 27 | Custom calendars by role? | On | "Pedal Barge Cruise", "Mega Pedal Bike Barge", "All Barges", "Everything", "margaret". | Rename legacy; new items do not auto-join filtered calendars. |
| 28 | Crew assigned in Dashboard? | On | "Added Captain: Eddie", "Deck Hand: Jarrett", etc. (10/8/26). | Confirm crew notifications. |
| 29 | ICS subscription for captains? | Can't tell | Subscribe to Calendar page URL blank in dump. | Share per captain. |
| 30 | Orders and online cart? | Can't tell | Not shown. | Top 10 #1. |
| 31 | Abandoned cart email? | Can't tell | Advanced company settings not captured. | Top 10 #1. |
| 32 | Online rebooking or cancel + policies per item? | Partial | Items set to "cancellation policy Default"; an API affiliate uses "Default - API". Online rebooking not shown. | Ask Support; weather days are the use case. |
| 33 | Bulk rebooking for weather? | Can't tell | Changelog 6/9/26 announces Bulk Booking Actions. | Confirm enabled before hurricane season ends. |
| 34 | Private Events configured? | Can't tell | Not in nav. VIP Client Party and Paradise Venue Rental exist. | Ask Support whether it suits group-planner contracts. |
| 35 | Walk-up bookings without name? | Can't tell | Not shown. | Low priority. |

### Customers and CRM

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 36 | Customer directory with tags? | On | "53655 total customers"; "Returning" tag visible. | Add tags for planners and corporate. |
| 37 | Email-list opt-in and Contacts export? | Partial | "sms" yes-no field created 6/27/26. Email subscribe box not visible. | Export Contacts monthly into the win-back list. |
| 38 | CRM or email integration? | Off | Integrations shows only "Subscribe to Calendar" and "OTA Connections". A "Pabbly webhook" user exists. | Webhook tab needs Support; use for the lead engine. |

### Campaigns, gift cards, memberships, upsell

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 39 | Discount Codes and Campaigns both enabled? | Partial | Campaigns on (about 47 codes). Discount Codes absent from nav. | Ask Support to enable Discount Codes. |
| 40 | Valid or blackout dates and max uses? | Can't tell | Not captured. | Review GET10, SAVE10, MAY20, STREET. |
| 41 | Campaigns report monthly? | Can't tell | Not shown. | Add to Monday review. |
| 42 | Promo field visible, not hidden? | Can't tell | "Promo Code (Other Items)" multi-campaign field exists on Default group (created 8/21/25). | Uncheck "Hide code input behind a link" on private boats. |
| 43 | Gift cards sold online with designs? | Partial | Gift Card retail item in Default Booking Flow; Michael set 464 availabilities to auto 9/23/26; 37 cards, $3,692.65 outstanding, all "Never expires". | Check card designs; consider expiry rules where legal. |
| 44 | Gift card credit instead of refund? | Can't tell | Not shown. | Use for weather cancellations. |
| 45 | Memberships? | Off | Not in nav. | Not a priority. |
| 46 | Combos? | Off | "0 Combos". | Top 10 #2. |
| 47 | Cross-sell combos? | Off | "No results found". | Low priority. |
| 48 | Suggested items active? | Partial | A flow named "Suggested Items" holds EcoTour and Seafood Boil. Default Suggested Items selections not readable. | Verify on a test booking. |

### Communication and waivers

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 49 | Reminder emails on every item? | Can't tell | Communication tabs empty. | Check the six boats. |
| 50 | Reminder texts and opt-in? | Partial | "sms" yes-no field exists. Texting enablement not visible. | Ask Support to enable texting. |
| 51 | Follow-ups with review and survey URL? | Partial | Seafood and Birding set 9/24/26 to "Review Request - All Trips (Follow-up)" at 2 hours. Others unknown. | Top 10 #6. |
| 52 | Confirmation notes cover arrival, parking, weather? | Can't tell | Text areas blank in dump. Seafood confirmation notes edited 9/23/26. | Read the live confirmation email. |
| 53 | Locations with Place IDs? | Partial | 8 locations with Place IDs; Port Orleans Brewery "Missing or incomplete"; "Bayou Beer Garden" appears 3 times; Nola Bike Bar location has 0 items. | Delete duplicates; fix the incomplete address. |
| 54 | Canned messages for weather? | Can't tell | Page shows "Loading...". One canned message known: "Review Request - All Trips (Follow-up)". | Create weather-delay and "we are on our way" messages. |
| 55 | FareHarbor Waivers enabled? | On | "Nola Party Barge Waiver" on 22 items; "Bike waiver2025" on 2. | Fine. |
| 56 | Waiver links and QR? | Off | QR/Link column "-"; "Enable now" in nav. | Enable for group planners to pre-sign. |
| 57 | Staff notifications? | Can't tell | Not captured. | Subscribe David, Michael, Jeff to cancellations and disputes. |
| 58 | FareHarbor Agent? | Off | "Setup progress 0/4". Affiliate "FH Agent (OpenCX) - USD" exists. | Decide FH Agent vs your own OpenCX build before setup. |
| 59 | Translations? | Can't tell | Not captured. One Swiss guest in the week's list. | Low priority. |

### Payments

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 60 | Payment Setup Checklist green? | Can't tell | Checklist text shows (bank verification, billing, recurring transfers) though payouts run: "Payout frequency Daily", "Payments processor ✓". Sub-tabs "Not allowed". | Have someone with payments permission screenshot it. |
| 61 | 6% booking fee relevant? | N/A | Applies under $35,000 online direct volume; NPB is at $1.14M. | Billing method on file: can't tell. |
| 62 | Deposits on high-value items? | Partial | See Top 10 #8. | Same. |
| 63 | Payment links for balances? | Can't tell | Label "Allow customers to make payments to underpaid bookings" present. | Check it is ticked. |
| 64 | Apple Pay, Google Pay, Link, Afterpay? | Can't tell | Not captured. | Test checkout on a phone. |
| 65 | AVS? | Can't tell | Not captured. | Only if fraud shows up. |
| 66 | Refund Reserve recurring transfer? | Can't tell | Checklist line "Activate recurring transfers" visible. | Confirm. |
| 67 | Clear statement text? | On | "Card statement text New Orleans Party". | Fine. |
| 68 | Dispute alerts and check-in evidence? | Partial | Check-in statuses on. Alerts unknown. | Subscribe to dispute emails. |
| 69 | Ledgers needed? | N/A | Single business. | Skip. |
| 70 | Card readers and Tap to Pay? | Can't tell | Changelog only. | Dock is optional for dock walk-ups. |
| 71 | Dock active? | Can't tell | "Flip to Tip" announced 10/7/26. | Tipping fits the dock check-in. |

### Distribution

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 72 | In FHDN? | On | Affiliates "FareHarbor Distribution Network - USD", "FHDN API - USD"; price sheet "Referral - 20% (FHDN)"; one FHDN API booking this week. | Fine; see Section 6. |
| 73 | FHDN API payouts set up? | Can't tell | Bank pages blocked. | Ask the person with payments access. |
| 74 | Marketplace quality maximized? | Partial | Low-quality image flags; 30+ future availabilities met on the boats. | Photos. |
| 75 | Google Things to Do connected? | Can't tell | Affiliate "Google - USD" exists. | Ask Support. |
| 76 | In ChatGPT? | Can't tell | Follows FHDN opt-in; gift items are ineligible. | Ask Support. |
| 77 | OTA connections reviewed? | Partial | Affiliates: GetYourGuide - USD - API, TripAdvisor Experiences/Viator - USD - API; sheets "GYG", "Billing - TripAdvisor/Viator". OTA Connections tab not captured. | Review API fee and rate parity. |
| 78 | Hotels and concierges with QR or codes? | Partial | Affiliates like Q Hotel Management, Rampart Treehouse, Pepps Pub, InteleTravel, Mosswood Events. "AceHotel" gift card $850. QR use not visible. | Issue QR links with a tracked sheet. |
| 79 | Affiliate rules limiting OTA peak? | Partial | One rule: "Permanent Rule- Do not sell ... FHDN or FHDN API", 1 item. | Add a peak-weekend cap on OTAs. |
| 80 | Affiliate blocks? | Off | "No affiliate blocks have been created yet". | Use for hotel partners. |
| 81 | Affiliate categories? | Off | Category column empty on visible rows. | Label crew, hotels, OTAs. |

### Website and tracking

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 82 | Lightframe on every page? | Can't tell | Embed generator present; site not crawled. | Check nolapartybarges.com source. |
| 83 | Online ref tag on every embed? | Can't tell | Not captured. | Check. |
| 84 | GA4 connected? | On | 11 GA4 streams listed. | Prune. |
| 85 | company_shortname dimension? | Can't tell | Multiple dashboards share streams. | Confirm in GA4 admin. |
| 86 | Meta CAPI with one pixel? | On | Pixel 701301873334767 with an access token. Source URL "https://nolapedalbarge.com/". Live check 2026-10-13: Purchase events fired on every day of Oct 6 to 12. | Update the Source URL. |
| 87 | GA4 purchase imported to Google Ads? | Can't tell | No Google Ads conversion type listed here. | Check in Google Ads. |
| 88 | Cookie consent tool? | Can't tell | Changelog mentions Consent Mode V2. | Check the site. |
| 89 | Price Sync on FareHarbor Sites? | Can't tell | "FareHarbor Sites" affiliate and "FHS" GA4 streams suggest a Sites setup. | Ask Support. |
| 90 | FB and IG links using Link type? | Can't tell | Not captured. | Check. |

### Reporting and admin

| # | Question | Status | Evidence | Recommendation |
|---|---|---|---|---|
| 91 | Pace report weekly? | Can't tell | Pace report exists per changelog. | Add to Monday. |
| 92 | Item occupancy reviewed? | Can't tell | Not shown. | Look for under 50% departures at 11 AM and 3 PM weekdays. |
| 93 | Booking source and affiliate reports saved? | Partial | Booking Source tile on Reports home. | Save reports. |
| 94 | Insights reviewed? | Partial | "10 opportunities available". | Read them. |
| 95 | Webhooks or Zapier? | Partial | "Pabbly webhook" user (Trainee). No webhook tab in Integrations. | Needs Support for the lead engine. |
| 96 | QuickBooks or Xero? | Can't tell | Not captured. | Ask the accountant. |
| 97 | Users verified, 2SV, least privilege? | Partial | 93 users, 74 active; 4 active Directors (David, Jeff, Michael, "nola ebike tours"); 14 active Deckhand/Crew, 39 active Guides; "Ai" agent user info@gravitytrails.com as Manager with Reporting. 2SV tab not captured. | Remove the other-brand Director; deactivate unused. |
| 98 | Multi-dashboard reporting? | Can't tell | Outside users from Door County Kayak and New Orleans Kayak Swamp Tours show in logs. | Fine. |
| 99 | Auto-archive reviewed? | Partial | Campaigns from 2020 (PRIVATE100 to PRIVATE350, LOCAL) still listed. | Archive stale codes. |
| 100 | Google ratings on book form? | Can't tell | Not shown. | Ask Support if reviews are 100+ at 4.2+. |

---

## 3. Per-item review

Prices and capacity come from the Items list and the bookings calendar. Customer type prices and notification settings were not readable (see top note).

### The Freaky Tiki (340933)
- $59 to $1,200, up to 25 guests, 1 hr 45 min, "BYOB tiki boat on the bayou". Resource "Freaky Tiki Vessel" 25. Calendar capacity 25. Departures 11, 1, 3, 5.
- 1,725 future availabilities. In 14 booking flows (most of any item). Bookability On.
- Online booking: deposit fields visible, so deposits appear on; amount not readable. Auto-close hours not readable; no no-bookings cutoff text shown.
- Photos not flagged low quality. Last 7 days: 26 bookings, $6,625.40, top item.
- Odd: it is in six legacy "ASN Pedal + Swamp (name)" flows.

### The Twerkin' Tiki (488558)
- $59 to $1,200, up to 25, "The loud one". 2,017 future availabilities, 13 flows. Deposit fields visible.
- Low-quality image flag. Last 7 days: 18 bookings, $6,376.80.
- Custom calendars include "Mega Pedal Bike Barge" and "Pedal Barge Cruise" (legacy names).
- Awkward: Oct 14 5 PM is a "Networking Night for Business Owners" headline on a standard slot, with no photo.

### The Bayou Boogie (116007)
- $59 to $800, up to 18, "Easier to fill". Calendar capacity 18. 2,000 future availabilities, 13 flows.
- Online booking layout differs from the other boats: the "Message" field is missing under Call to book. Check the sold-out text.
- Low-quality image flag. 6 bookings, $2,265.46 last 7 days.
- Many 1:00 PM and 3:00 PM slots show "Full 1 0" on busy days, meaning one private booking filled the boat.

### The Party Queen (289593)
- $59 to $900, listing says "Up to 26 guests". Calendar and the Mega Pedal Bike Barge resource show 22. That is a capacity mismatch of 4 seats between the listing and what can be sold. Offline Boat Seats (8) plus Online Boat Seats (18) add up to 26, so the 26 may be a legacy figure.
- 1,439 future availabilities, 13 flows. Low-quality image flag. No bookings in the last 7 days report.

### Luxury Pontoon Private Charter, up to 6 (294180)
- $350 flat. Two pontoons run as headlines "BLACK N' TAN" and "NAVY N' GRAY" at 11, 1, 3, 5 on some days, one unlabeled pair on others. Capacity 1 (the whole boat).
- 2,783 future availabilities. 12 flows. Not in the Default Booking Flow.
- Deposits: "Allow deposits" shown with no amount fields, so off.
- Jeff closed 634 pontoon availabilities on 9/26/26 and has been flipping call/waitlist since. Michael changed the item cancellation notes 9/25/26, so the pontoon carries item-specific cancellation text that may not match the others.
- Low-quality image flag. No bookings in the last 7 days report.

### Bayou & Wildlife Alligator EcoTour (514442)
- $50 per person, 2 hours, "Private available", bathroom onboard. 10:00 AM daily, capacity 18. 381 future availabilities, 11 flows. Deposit fields visible.
- Customer types in the company list: Person (21+), Adult (16+), Young Adult (18 to 20), Youth (13 to 15), Child (12 and under). Age bands overlap: a 16 or 17 year old fits Adult and Youth, an 18 to 20 year old fits Adult and Young Adult. Check which ones are attached to this item.
- 2 bookings, $253.75 last 7 days. Low-quality image flag. Tagged by Jeff 9/7/26 "Wildlife, Sightseeing Tour, Guided Tour".

### Sunset Cocktail Cruise & Seafood Boil (448372)
- $89.99 to $165, 2.5 hours, 5:30 PM Monday to Friday on the calendar, 184 future availabilities. The $89.99 price point is the only non-whole-dollar listed price besides the $59.88 pattern below.
- Has its own booking restriction "Sunset Cruise & Seafood Boil". Deposits off (no amount fields). 12 flows including "Suggested Items".
- Follow-up: set 9/24/26 by Michael to "Review Request - All Trips (Follow-up)", 2 hours after start or end. Confirmation notes edited 9/23/26.
- Calendar shows "0" with no capacity number on these rows, unlike the boats. Check capacity setup.

### Related items living in this company
- **Irish Channel Pedal Pub-Crawl (501258) and NolaBikeBar Mid-City (608684):** NOLA Bike Bar tours. 3,557 and 380 future availabilities. "9:00 PM 1 day before" no-bookings cutoff. Michael set 416 Mid-City availabilities to call on 9/2/26. Resources "Pedal Bike Bar 1" is 11 seats vs a 14-person product, Bar 2 is 14.
- **Louisiana Coastal Birding (656296):** 25 future availabilities, follow-up set 9/24/26.
- **Jingle on the Bayou (685427):** no future availabilities, see Top 10 #3.
- **DOCKED, VIP Client Party, Office, Paradise Venue Rental, Winter Day, Gift Certificates, Retail:** bookability Off, Unlisted or Private as intended. DOCKED has a $45 headline and is in 0 flows.

### Cross-item oddities
- **Private Shuttle:** a customer type at $400 with note "15 passengers max • Roundtrip transportation..." sits in the same list as people types. It inflates pax counts and reports, and any customer type edit can break API connections.
- **Other junk types:** "ADULT SUMMER CAMP / Campers", "Private Boat Battle", "Private Pedal Bike Bar", "Person Pedal Bike Barge Cruise Gift Certificate". Legacy pedal wording sits in customer types, gift certificate campaigns, calendar names, GA4 stream names and flow names. Your own rule is not to reference pedaling to customers, so anything customer-visible needs a rename.
- **Cancellation policy inconsistency:** 7 items show "Using default cancellation notes"; the rest carry item-level notes (the pontoon was edited on 9/25/26). Policies named "Default" and "Default - API" also exist. The text is not in the dump, so whether they conflict is unverified. Read them side by side.
- **Promo code field:** "Promo Code (Other Items)" multi-campaign field exists on the Default group (created 8/21/25). Whether it shows on each boat could not be checked.
- **Price pattern:** guests list at $59.00, $63.00 and $59.88 per person across the last two weeks. The $59.88 figure is consistent with $59 plus about 1.5%. FareHarbor staff added a "Credit Card Processing Fee" custom field to the Default group on 12/2/24. See question 1.

---

## 4. Communication audit

| Message | Status (read 2026-10-13) | Timing | Notes |
|---|---|---|---|
| Confirmation email | Can't tell (always on by design) | On booking | Company, item and headline notes. Headline "If booking w/ a group, make sure y'all book the same boat and time!" exists as a confirmation note. |
| Reminder email | Can't tell | Not visible | Per-item tab empty. Check each boat. |
| Reminder text | Can't tell | Not visible | Needs Support to enable. An "sms" yes-no field exists (6/27/26) for consent. |
| Follow-up / review request | Partial | 2 hours after start or end | Confirmed only for Seafood Boil and Birding (9/24/26, Michael). Message "Review Request - All Trips (Follow-up)". |
| Review link / survey URL | Can't tell | n/a | Info & Policies > Social Media tab not captured. |
| Canned messages | Can't tell | n/a | Page "Loading...". |
| Public headlines | On | n/a | 2 company headlines, no photos. |
| Waitlist signup / seat-opened email | Can't tell | n/a | Waitlist status in use. |
| Abandoned cart | Can't tell | 2 hours after drop-off if on | Not customizable. |
| Waiver request | On | In confirmation and reminders | Waiver on 22 items. |
| Gift card emails | Can't tell | n/a | Designs not captured. |

What is missing versus the map: weather-delay and arrival canned messages, texting follow-ups (FareHarbor cannot send them, so the Twilio review text you already run covers that), waiver links, seat-opened waitlist email, and a visible review URL. FareHarbor does not email across date ranges or run campaigns. Keep the 33k win-back list in SendGrid and export Contacts into it.

Overlap warning: your own post-trip review text and the new FareHarbor follow-up email can both go out on the same trip. Decide which owns the review request, or stagger them.

---

## 5. Tracking audit

| Item | Status (read 2026-10-13) | Evidence | Concern |
|---|---|---|---|
| Meta Pixel | On | Pixel ID 701301873334767 | Matches the known pixel. |
| Meta Conversions API | On | An access token is stored; Source URL is "https://nolapedalbarge.com/" | Stale domain. Update to nolapartybarges.com. |
| Live pixel check (2026-10-13) | Healthy | Oct 6 to 12: Purchase fired on most hours with sales; InitiateCheckout and fareharbor-click events present | Purchase counts exceed the 60 FareHarbor bookings, likely because browser and server events both count. Check dedupe in Events Manager. |
| GA4 streams | Partial | 11 streams. Four fire on all FareHarbor pages: Hidden-Adventures GA4, Hidden Adventures, FHS - nolabikebar.com, FHS - neworleanspedalbarge - A24. Others say "Only activated when present on external page": tiki boats site, FHDN tripoutside, FHDN hijinkslife, nolaactivities, admirenola twice. | Cross-brand data pollution. Which ID is property 322288940 is not visible; ask. Admire Nola IDs are duplicated (same ID twice). |
| Google Ads conversion | Can't tell | No Google Ads type in the list | If Google Ads imports GA4 purchase, it inherits the stream issues above. |
| Custom pixels (TikTok, others) | Off | Not listed | Support only. |
| Consent Mode V2 | Can't tell | Changelog 7/1/26 | Needs the site's consent tool. |
| Attribution survey | Off | "How did you hear about us?" removed 3/5/26 | Top 10 #7. |

Security note: the Meta access token is readable in plaintext in the local dump files under `~/Projects/fareharbor-help/dash/`. They are not in iCloud, but delete or redact them when this audit is done, and rotate the token if the files were ever copied elsewhere.

---

## 6. Distribution audit

| Channel | Status (read 2026-10-13) | Evidence |
|---|---|---|
| Direct crew and referral affiliates | On | 96 affiliates, mostly individual crew and guides at Referral - 10% (some 15%). Several businesses: All About New Orleans Tours, Q Hotel Management, Pepps Pub, Ragin Cajun Airboat Tours, Book Nola. |
| FHDN | On (low volume) | FHDN and FHDN API affiliates; "Referral - 20% (FHDN)". 1 FHDN API booking of 60 this week. One permanent rule: do not sell to FHDN or FHDN API on 1 item. |
| FareHarbor Agent / OpenCX | Partial | Affiliate "FH Agent (OpenCX) - USD" exists and FH Agent setup shows 0/4. Check its price sheet is $0 commission. |
| Google Things to Do | Can't tell | "Google - USD" affiliate exists. Ask Support. |
| ChatGPT | Can't tell | Follows the FHDN opt-in; gift items are excluded. |
| Viator / Tripadvisor | On | "TripAdvisor Experiences/Viator - USD - API"; invoice sheet "Billing - TripAdvisor/Viator" (0%). |
| GetYourGuide | On | "GetYourGuide - USD - API"; price sheet "GYG". |
| Airbnb Experiences, Booking.com | Can't tell | OTA Connections tab not captured. |
| Who2Call (call center) | On | Price sheet "Who2Call (Online)", "$5 Flat Rate Commission - Who2Call", and a $5 count custom field added 4/11/25. Confirm that field is hidden on the public book form. |
| Marketplace | Can't tell | Page not captured. |
| Affiliate blocks | Off | "No affiliate blocks have been created yet". |
| Affiliate categories | Off | Empty on visible rows. |

---

## 7. Questions for David

1. Is a card processing surcharge being charged to guests? The "Credit Card Processing Fee" custom field was added in Dec 2024 and a $59.88 pattern appears next to $59.00. Which items carry it, and is it disclosed on the booking page?
2. Did Jeff mean to close 634 pontoon availabilities on 9/26, and is the daily closed, call, waitlist toggling a crew-readiness workflow?
3. Which GA4 measurement ID belongs to property 322288940, and may I recommend removing the Hidden Adventures, Bike Bar and Admire Nola streams?
4. Do you want to keep the old pedal names in customer types, calendar names and flow names, or rename them (customer-visible ones first)?
5. Who has payments permission to confirm the Payment Setup Checklist, refund reserve and FHDN API payout account? The dump was blocked there.
6. Is Jingle on the Bayou supposed to be on sale yet, and what dates?
7. Do you want FareHarbor Agent, or will your OpenCX build replace it? Setup progress is 0/4 and an OpenCX affiliate already exists.
8. Who owns the review request, the FareHarbor follow-up email or the Twilio text?
9. The "nola ebike tours" account is a Director on this dashboard. Is that intentional?
10. Gift cards hold $3,692.65 across 37 cards and none expire. Do you want to keep it that way?

---

## 8. Appendix: pages that failed to load or looked empty

- Item tabs Options & Prices, Availability, Communication: empty or "Not found" for all 20 items.
- Item Online Booking tab for EcoTour, Irish Channel Pedal, Gift Card: "That didn't work. Please try again." Form values are not captured on any item.
- Canned Messages, Booking Flows: "Loading...".
- Waivers (signed list): "Loading..." placeholder rows. Templates tab loaded.
- Price Planner (beta): heading only.
- Bank & Payments: only the overview; ended with "Not allowed". Tabs Bank Accounts, Billing, Refund Reserve, Tax, Cards, Payment Types, Devices, Ledgers not captured.
- Users: Outside Users, Permission Groups and 2-Step Verification tabs not captured.
- Info & Policies: Logo & Contact, Social Media, Cancellation Policies, General, Health & Safety, Open Hours tabs not captured; text areas blank.
- Integrations: OTA Connections tab and the calendar subscription URL not captured.
- Resources: page 2 of 2 not captured.
- Affiliates: only page 1 of 10 rows captured (the affiliate dropdown list gives the names).
- Gift Cards: Card Types and Card Designs tabs not captured.
- Price Sheets: Price Schedules tab not captured.
- Book Buttons & Embeds, Cross-Sell Partners, Combos, Suggested Items: loaded but only the shell and empty states.
- Not in nav at all: Discount Codes, Memberships, Orders/Cart settings, Marketplace, Private Events, Advanced company settings (gear).
- Item logs: "Load more" was not expanded, so older history is hidden on most items.
