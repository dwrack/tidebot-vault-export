# NKST — Post-Tour Review Texts (SMS)

**Status (2026-10-12, 3:05pm CT):** LIVE since 11:50am CT. Copy v2 (guest's first name, photo asks, no "Google") installed 3:01pm. Spring/summer catch-up turned on 3:03pm: 1,066 past guests (Mar 1 to Oct 10), 80 texts a day, newest trips first, about 13 days to clear. Same system NPB has run since 2026-09-24, one codebase, NKST gets its own folder, phone number, copy, and database.

## What it does

- 90 minutes after a tour ends, every guest phone on the booking (the booker plus every waiver signer) gets one text asking for a review, with the guest's own first name and the guide's first name pulled from the FareHarbor crew assignment.
- 2 days later at 11:00 a nudge goes to anyone who didn't click the link, didn't reply, and didn't opt out. The nudge opens with "Any issues? Just reply here." so unhappy guests get a human instead of a second review ask.
- Sends only 9:00 to 18:00 CT. A tour ending after 16:30 texts the next morning at 10:00.
- Never texts: cancelled, rebooked, or weather-cancelled bookings (checked again at send time), no-shows, non-US/CA numbers, gift cards, anyone texted in the last 7 days, trips older than 48 hours.
- STOP opts the guest out at Twilio; the relay swallows the keyword and never forwards it to staff.
- Pacing: max 60 texts per 10-minute run.

## Guest replies

- A guest texting back to 504-226-5402 lands on the NKST line 504-571-9975 as "[NKST] +1504xxxxxxx: their message".
- To answer, text 504-226-5402 from the 571-9975 line starting with the guest's 10-digit number, e.g. `5045551234 So sorry about that, call me at ...`. The guest sees it from 226-5402. Without a number prefix it goes to the most recent guest who texted in, which is a gamble while the catch-up is sending 80 a day: always prefix.
- Photos texted back arrive the same way (MMS).

## The pieces

| Piece | Where |
|---|---|
| Data feed | FareHarbor booking webhook id 13146 (Booking All Fields, new + updated + cancelled) on David's user under Settings > Users > david > Webhooks, posting to the Tailscale Funnel on davids-mbp-2 |
| Backup feed | FareHarbor dashboard manifest via the daily scrape's login cookie (optional, never blocks a send) |
| Sender | Twilio +1 504-226-5402 (already on the registered 10DLC campaign; calls already forward to 571-9975). Guest replies relay to the NKST line 504-571-9975 |
| Review link | neworleanskayakswamptours.com/r/XXXX, a Redirection-plugin rule (id 44) that 302s to the Google review form (star rating, text, "Add photos" button) and logs the click. The nudge skips clickers |
| Code + config | davids-mbp-2: `~/Projects/fareharbor-brief/review-sms/poll.mjs` (shared with NPB) run with `REVIEW_BRAND_DIR=~/Projects/fareharbor-brief/review-sms-nkst` (config.json, review-sms.db, review-sms.log, .webhook-token). Catch-up list builder: `review-sms/catchup-pull.mjs` (read-only against FareHarbor) |
| Schedule | launchd `com.djl.nkst-review-sms`, every 10 minutes |
| Alerts | #helm-ops once a day if the webhook goes quiet 48h or the cookie dies |

## The copy (A/B, 11 arms, each guest gets one, sticky)

`{first}` is the guest's first name (dropped cleanly, comma and all, if FareHarbor has none or it's junk). Guide name fills in when FareHarbor has a crew member on the trip; otherwise the "no guide" version sends. Every arm starts "NOLA Kayak Swamp Tours:" and ends with the link + "STOP to opt out". All under 160 characters with a 9-letter guest name and the longest guide name.

- A (control): Christine, thanks for paddling with Stephanie! A quick review helps our guides
- B: The gators are still talking about you, Christine. Return the favor with a review
- C: No essay needed, Christine. 'Saw a gator, loved it' counts. Stephanie will take it
- D: Christine, reviews are how Stephanie proves to Mom that swamp guide is a real job
- E: 'Best part of our trip' is our top review line, Christine. Steal it, we won't tell
- F: Stephanie reads every review out loud to the dog, Christine. Make that tail wag
- G: Survived the swamp and Stephanie's jokes, Christine? Least you can do is a review
- H (photo): Swamp photos, Christine? Drop one in a review, Stephanie would love to see it
- I (photo): Stephanie wants to see your photos, Christine. Post your best one with a review
- J (photo, no guide): We'd love to see your swamp photos, Christine! Post your favorite with a review
- K (photo + IG): Snap any photos, Christine? Post one in a review or tag @kayaknola for Stephanie

Nudge (2 days later, non-clickers only): "Any issues, Christine? Just reply here. Otherwise a quick review helps Stephanie:"

Not doing: a star-gate page that routes 4-and-under to a private form. Google's review policy bans selectively soliciting positive reviews and the FTC's 2024 review rule treats it as suppression. The nudge's reply line is the compliant version.

## Spring/summer catch-up (started 2026-10-12)

One late review ask per phone for Mar 1 to Oct 10 guests who were never texted. 80 a day, newest first, same safety skips, no second text. Five arms with the trip month filled in:

- L1: We meant to ask in April, Christine. A gator ate the to-do list. Quick review?
- L2: Christine, how was your April paddle with us? One line counts:
- L3: Stephanie forgot to ask for your review in April, Christine. Mortified. Fix it?
- L4: A few months late asking about April, Christine. Fast paddlers, slow texters:
- L5: Better late than never, Christine. How was the April paddle? 'Loved it' counts:

Staged list by trip month: Mar 231, Apr 239, May 169, Jun 101, Jul 104, Aug 74, Sep 111, Oct 37. NPB's run shows the age curve: 3-week-old trips click 13.6%, 2-month-old trips 3.6%, so expect single digits on spring.

Rental promo for the Bayou Bienvenue location goes by email, not SMS (marketing text to numbers collected for booking updates is the TCPA pattern, and the 10DLC campaign is registered for review requests).

## Running it

```
ssh davidrack@100.113.229.1
cd ~/Projects/fareharbor-brief/review-sms
REVIEW_BRAND_DIR=../review-sms-nkst node poll.mjs --status      # who's queued / sent / clicked
REVIEW_BRAND_DIR=../review-sms-nkst node poll.mjs --ab          # click rate per arm, incl. catch-up L1-L5
REVIEW_BRAND_DIR=../review-sms-nkst node catchup-pull.mjs --report   # catch-up progress by month
tail -f ../review-sms-nkst/review-sms.log
```

Turn the catch-up off: set `catchup.enabled` to false in `review-sms-nkst/config.json`. Backups of every config and code version sit next to the files (`*.bak-first-20261012-1301` is the pre-v2 state).

Guides need to be assigned as crew on every availability in FareHarbor or the text says "paddling with us" instead of their name.
