# Adtouch Waiver Chasing — FareHarbor Add-On

**Status (2026-10-31):** HOLD. David: "wait till we get OpenCX SMS approval, then let's do this." Nothing sent. Trigger = OpenCX toll-free SMS verified (FH ticket 5848935, confirm due 11/2; see [[00 Dashboard/OpenCX SMS Toll-Free Verification Tracker]]). Then pick pilot brand and email Peter about overlap before FareHarbor.

## What it is
Cold email from Peter at Adtouch Labs (6 Centerpointe Dr Suite 700, La Palma, CA 90623), received 2026-10-31. FareHarbor dashboard add-on that:
1. Scans upcoming reservations daily for missing waivers (works with FareHarbor waivers, SmartWaiver, Wherewolf).
2. Texts the customer to get it signed.
3. AI answers reply texts using the reservation details, passes anything else to the team.

Pricing: $0.15 per booking that needs chasing, texts included. No platform fee mentioned.
Reference customers: Sea Serpent (FL, FH waivers), Holo Holo (Maui, SmartWaiver), Body Glove (HI, Wherewolf).

## How to turn it on
Email FareHarbor support, ATTN: Ladina Brackle, ask to add Adtouch to the dashboard. One email per FareHarbor company (each brand is its own FH company, so one ask per brand or one email listing all of them).

## Brands that could use it (all FareHarbor, all waiver-gated)
DCKT, Cave Point, Detours, NPB, HPB, NOLA Booze Cruise, Tiki Boats, NKST, Austin Kayak / Paddle Shack, Lone Star, BBK, Gravity / Hidden Adventure.
Not applicable: Ebb & Ember, Elevated Tides (not on FH).

## Open questions before go-live
- **OpenCX overlap.** OpenCX already texts customers for several brands (NPB, HPB, DCKT, NKST, BBK, LSKT) and owns the SMS lane. Adtouch sends from its own number and its own AI answers replies. Two bots texting the same customer about one booking is the risk. Ask Peter: can replies route to our OpenCX number, or can Adtouch send only the waiver nudge and hand every reply to the team instead of answering?
- **What number sends the text, and does it show the brand name?**
- **Timing.** When does the first nudge go out (24h before? on booking?) and how many follow-ups.
- **Reference check.** Sea Serpent is a kayak op in FL; worth one email to them before rolling out to 12 brands.
- **Pilot.** Start with one brand (NPB has the highest volume and most no-waiver walk-ups), measure for 30 days, then roll out.

## Next actions
- [ ] David picks pilot brand(s)
- [ ] Claude drafts the FareHarbor support email (signed by the business, no personal name) and the questions email to Peter; David approves both
- [ ] After FH adds it: confirm texts fire on a test booking before trusting it
- [ ] Add to the Systems Grid as the waiver function owner for each brand

## Source
Screenshot of the email, saved in chat 2026-10-31 (Gmail, 120 unread view). Reply-to is Peter at Adtouch Labs; exact address not captured, pull it from the Gmail thread before replying.
