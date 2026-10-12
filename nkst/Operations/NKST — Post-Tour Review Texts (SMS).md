# NKST — Post-Tour Review Texts (SMS)

**Status (2026-10-12):** LIVE since 11:50am CT. First run texted 6 guests from Oct 11 tours. Same system NPB has run since 2026-09-24, one codebase, NKST gets its own folder, phone number, copy, and database.

## What it does

- 90 minutes after a tour ends, every guest phone on the booking (the booker plus every waiver signer) gets one text asking for a Google review, with the guide's first name pulled from the FareHarbor crew assignment.
- 2 days later at 11:00 a nudge goes to anyone who didn't click the link, didn't reply, and didn't opt out.
- Sends only 9:00 to 18:00 CT. A tour ending after 16:30 texts the next morning at 10:00.
- Never texts: cancelled, rebooked, or weather-cancelled bookings (checked again at send time), no-shows, non-US/CA numbers, gift cards, anyone texted in the last 7 days, trips older than 48 hours.
- STOP opts the guest out at Twilio; the relay swallows the keyword and never forwards it to staff.
- Pacing: max 60 texts per 10-minute run.

## The pieces

| Piece | Where |
|---|---|
| Data feed | FareHarbor booking webhook id 13146 (Booking All Fields, new + updated + cancelled) on David's user under Settings > Users > david > Webhooks, posting to the Tailscale Funnel on davids-mbp-2 |
| Backup feed | FareHarbor dashboard manifest via the daily scrape's login cookie (optional, never blocks a send) |
| Sender | Twilio +1 504-226-5402 (already on the registered 10DLC campaign; calls already forward to 571-9975). Guest replies relay to the NKST line 504-571-9975 once the relay update is installed |
| Review link | neworleanskayakswamptours.com/r/XXXX, a Redirection-plugin rule (id 44) that 302s to the Google review form and logs the click. The nudge skips clickers |
| Code + config | davids-mbp-2: `~/Projects/fareharbor-brief/review-sms/poll.mjs` (shared with NPB) run with `REVIEW_BRAND_DIR=~/Projects/fareharbor-brief/review-sms-nkst` (config.json, review-sms.db, review-sms.log, .webhook-token) |
| Schedule | launchd `com.djl.nkst-review-sms`, every 10 minutes |
| Alerts | #helm-ops once a day if the webhook goes quiet 48h or the cookie dies |

## The copy (A/B, 7 arms, each guest gets one, sticky)

Guide name fills in when FareHarbor has a crew member on the trip; otherwise the "no guide" version sends.

- A (control): thanks for paddling with Stephanie! A quick Google review helps our guides
- B: The gators are still talking about your group. Return the favor with a review
- C: No essay needed. 'Saw a gator, loved it' counts. Stephanie will take it
- D: Reviews are how Stephanie proves to Mom that swamp guide is a real job
- E: 'Best part of our trip' is our #1 review line. Copy-paste it, we won't tell
- F: Stephanie reads every review out loud to the dog. Make that tail wag
- G: You survived the swamp and Stephanie's jokes. Least you can do is a review

Every arm starts "NOLA Kayak Swamp Tours:" and ends with the link + "STOP to opt out". All under 160 characters with the longest guide name on the roster.

Nudge: "nudge from Stephanie. Got 60 seconds? A Google review means a lot to our guides." (NPB data says the nudge drives under 1% of clicks; easy to turn off by setting `sms2_days_after` very high or deleting `sms2`.)

## Running it

```
ssh davidrack@100.113.229.1
cd ~/Projects/fareharbor-brief/review-sms
REVIEW_BRAND_DIR=../review-sms-nkst node poll.mjs --status    # who's queued / sent / clicked
REVIEW_BRAND_DIR=../review-sms-nkst node poll.mjs --ab        # click rate per arm
tail -f ../review-sms-nkst/review-sms.log
```

Guides need to be assigned as crew on every availability in FareHarbor or the text says "paddling with us" instead of their name.
