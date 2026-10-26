# OpenCX SMS Toll-Free Verification Tracker

Started 2026-10-16. All 6 OpenCX numbers are toll-free, owned by OpenCX's Twilio (not ours), so this is **Toll-Free Verification**, not 10DLC. Per [OpenCX docs](https://docs.open.cx/sms/compliance), the OpenCX team files it; we send them the data. Carriers silently block texts from unverified numbers.

**History (verified in Gmail 2026-10-16):** all 6 brands were emailed to Mo (mo@open.cx) May 2-4, 2026, but written as A2P 10DLC, the wrong program for toll-free numbers. No reply from OpenCX found. David nudged Aug 25. Corrected Toll-Free packet SENT to mo@open.cx 2026-10-16 from dwrack81@gmail.com, asking OpenCX to file by Oct 23. Entities confirmed by David 2026-10-16: NPB + NKST = Gravity Trails; DCKT = its own LLC; HPB/BBK/Austin = Lone Star Kayak Tours, LLC.

**Real blocker (per FareHarbor, verified in Gmail 2026-10-16):** OpenCX's third-party SMS vendor never completed verification for ANY FareHarbor/OpenCX operator (Cody Sharkey, Jul 15). Sep 14 FH support (ticket #5796065): Open onboarding a new vendor, target end of Sept. Missed. Oct 16: follow-up sent to Cody (cc Kevin Schmitt) asking by **Wed Oct 21** for vendor status, toll-free filing confirmation, written go-live date, and FareHarbor Agent access + pricing as backup if Open misses mid-Nov.

EINs are on file in each vault but are NOT copied here. David gives them to OpenCX directly.

## Status

| Brand | Number | Legal name (draft) | Contact | Status | Blocker |
|---|---|---|---|---|---|
| NOLA Party Barge | 888-403-7303 | Gravity Trails, LLC dba NOLA Party Barge | Jeffrey Chitek or JT Sides | Sent to OpenCX 10-16 | Vault says a different number, 888-618-9606, was "pending since Jun". Which one? |
| NO Kayak Swamp Tours | 888-560-6251 | Gravity Trails, LLC dba NKST | Michelle Healey | Sent to OpenCX 10-16 | Entity: Gravity Trails vs Apres Assets vs new NKST LLC |
| Door County Kayak Tours | 844-699-5219 | Door County Kayak Tours LLC | Bella or Jessica | Sent to OpenCX 10-16 | Privacy page says texts come "from Gravity Trails". Fix |
| Houston Pedal Barge | 855-516-9065 | Lone Star Kayak Tours, LLC dba Houston Pedal Barge | Connor Champagne | Sent to OpenCX 10-16 | LSKT LLC status (bankruptcy notes) |
| Buffalo Bayou Kayak | 855-957-0702 | Lone Star Kayak Tours, LLC dba Buffalo Bayou Kayak | Connor Champagne | Sent to OpenCX 10-16 | Same LSKT status question |
| Lone Star / Austin Kayak | 888-384-5051 | Lone Star Kayak Tours, LLC dba Austin Kayak Tours | Unknown (Connor?) | Sent to OpenCX 10-16 | Same + no Austin contact + site fixes below |

## Packet fields (same for every brand unless noted)
- Business type: private for-profit LLC
- Use case: customer care + booking notifications (confirmations, reminders, weather/water updates, replies to guest questions from the AI agent). Promos only if David wants them declared.
- Opt-in: guest gives mobile number at FareHarbor booking/waiver, or texts the number first. Policy Section 12 covers consent, STOP/HELP, 1-5 msgs per booking, msg & data rates.
- Sample message: "Hi {name}, this is {Brand}. You're booked for {tour} on {date} at {time}. Meet at {location}. Reply HELP for help, STOP to opt out."
- Monthly volume to declare: NPB 1,500 / NKST 900 / DCKT 800 / HPB 500 / BBK 500 / LSKT 900
- Privacy URLs: `{site}/privacy-statement-us/` (all have the SMS Section 12 except austinkayaktours.com). Use lonestarkayaktours.com for Austin.

## Website fixes that raise approval odds
1. austinkayaktours.com: no SMS clause, no terms page. File Austin under lonestarkayaktours.com instead.
2. lonestarkayaktours.com privacy page: contact block says "New Orleans Kayak, LA 70185". Fix.
3. DCKT, HPB, BBK privacy pages: sender name should be the legal LLC, not "Gravity Trails" or the brand alone.
4. All sites: no explicit SMS consent checkbox at booking. Most common rejection reason. Ask FareHarbor about adding one.

Sources: vault Entity Canon files, A2P 10DLC docs in NPB/NKST vaults, live site fetches 2026-10-16.
