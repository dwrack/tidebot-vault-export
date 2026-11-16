# Gift Card Drip to Past Guests (Nov 17 to Dec 29, 2026)

**CURRENT STATUS (verified 2026-11-15): built, not sent.** Seven emails with A/B cells are built. One test of email 1 went to David's inbox on Nov 15. Nothing has gone to the list. The list send is waiting on David's go and on the SES health check passing (see Open items).

Style: "Designed Email" from the Style Menu, in the photo-led gift drip look first built for NKST (one big photo, calm serif headline, one button), with HPB's yellow button and navy type.

## The idea
Seven emails to past guests (7,183 mailable). No discount, no code, no price claims. The offer is the gift card itself: it never expires and is good toward any cruise. Angles are the groups HPB already sells to: the crew, the group chat, the bachelorette, the birthday crew, the office team. Copy uses "boat" and "night on the water" and never the word pedal outside the brand name.

## Schedule

| # | Send | Subject A | Angle |
|---|---|---|---|
| 1 | Tue Nov 17 | Get the whole crew on the water | Opener: give them a night on the water |
| 2 | Fri Nov 27 | We're not having a Black Friday sale | Deadpan no-sale |
| 3 | Thu Dec 3 | Know a group that needs a night out? | Send it to the group chat |
| 4 | Thu Dec 10 | For the group that has everything planned except this | Bachelorette, birthday crew, office team |
| 5 | Thu Dec 17 | No shipping deadline on this one | Nothing to ship, 3 steps |
| 6 | Tue Dec 22 | It's not too late | Last call, print it tonight |
| 7 | Tue Dec 29 | Unwrapped a night on the water? | Use it, or buy your own |

All seven beats fit the calendar. If David's go comes after Nov 17, email 1 goes the first weekday after the go and the rest keep their dates. If the go slips past about Nov 24, fold email 1 into email 2.

## A/B test
Every email goes out in equal groups, about 1,200 each for email 1 (six groups) and about 1,800 each for emails 2 to 7 (four groups). Subject A or B, crossed with the hero photo. Body copy and button are identical. Side by side: `preview/A-B Subjects + Photos.html`.

| # | Subject B | Photo A | Photo B | Photo C (email 1 only) |
|---|---|---|---|---|
| 1 | A gift for the one who has everything | Two silhouettes at sunset | Ice-packed cooler trough | Boat at the dock, blue sky |
| 2 | No doorbusters on Clear Lake | Yellow boat sign | Boat at dock, clouds |  |
| 3 | Send it to the group chat | Deck with yellow bar | Boat at dock, side view |  |
| 4 | Three groups on your list, one answer | Empty deck, long bar | Ice-packed cooler trough |  |
| 5 | The gift that shows up in your inbox | Boat at dock, canopy | Boat at dock, blue sky |  |
| 6 | Forgot someone? Print this tonight | Sunset from the rail | Two silhouettes at sunset |  |
| 7 | Got a gift card? Pick a date | Boat at dock, blue sky | Boat at dock, side view |  |

No guests' faces are identifiable in any hero. HPB's phone shots mostly show guests, so the photos lean on the boat, the deck and the sunsets.

## How to read results
- **Opens and clicks:** `node ab-report.mjs em201-gift-whole-crew` in `~/Projects/hpb-tools/newsletter-2026/` (counts come from SES via CloudWatch, set `hpb-campaign`, by campaign and cell). Opens run high because Apple Mail pre-loads images, so compare groups with each other only. Early clicks are mostly security scanners, so read clicks about 3 days in.
- **Sales:** FareHarbor refs carry the cell, for example `gift_g01_ab`. GA4 campaign `gift_2026`, `utm_content` such as `g01ab_cta`. HPB's GA4 has no purchase events (see the GA4 status note), so FareHarbor gift card sales by ref are the real read.
- **Subject winner** = cells starting with a against cells starting with b. **Photo winner** = second letter. Move the winning pattern into the A slot of later emails.

## Where it lives
- Code: `~/Projects/hpb-tools/newsletter-2026/` (`emails.mjs` copy, `build.mjs` layout, `send-ses.mjs`, `recipients.mjs`, `ab-report.mjs`, `build-preview.mjs`). Built files in `out/`.
- Photos: `assets/` and `assets/_originals/`. Uploaded to `s3://hpb-email-assets/email/` (public read).
- Send: `node send-ses.mjs --email em201-gift-whole-crew --ab --go` after the preflight passes. Paces at 20 per second, about 6 minutes for the list. Keep the laptop awake (`caffeinate -i`).
- Test one cell: add `--test <address> --variant ab`.

## Safety wiring (done 2026-11-15)
- Sender: Houston Pedal Barge, info@houstonpedalbarge.com, SES us-west-2, domain verified, MAIL FROM `mail.houstonpedalbarge.com` verified.
- Bounces and complaints go to SNS topic `hpb-ses-events`. Feedback forwarding is OFF, so bounce notices no longer land in the inbox.
- Config set `hpb-campaign` now has a CloudWatch destination (dimensions campaign and cell).
- Hosted one-click unsubscribe: Lambda `hpb-unsubscribe`. Tested: link page loads, bad token is refused, one-click POST returns 200. Header `List-Unsubscribe` is the URL form with `List-Unsubscribe-Post`. Unsubscribes land on the SES account suppression list.
- Preflight in `send-ses.mjs` refuses a list send if the account is unhealthy, bounce rate is 3% or more, complaint rate is 0.05% or more, relay addresses are on the list, or forwarding is on.
- Booking-site relay addresses (GetYourGuide, Viator and similar) are dropped from the list for good.

## List
FareHarbor customer export pulled 2026-11-15: 7,249 customers (the previous file, from May 14, had about 7,022). 7,183 are mailable after removing 13 invalid or relay addresses and 53 on the SES suppression list. FareHarbor has no "agreed to be emailed" field, so the list is every customer with an email, minus opt-outs, same as past sends.

## Open items
1. **David's go to send.** Nothing goes to the list without it.
2. **SES health is blocking the send.** The 24 hour complaint rate on the shared account read 0.173% on Nov 15 (limit in the preflight is 0.05%) and bounce rate 2.91%. Recheck right before the send. Do not use `--skip-preflight` without David saying so.
3. **Gift card facts to confirm with one test purchase:** that the card is emailed (to the buyer or the recipient) right after checkout, and that it works toward every cruise. The FareHarbor item says "a gift card with a value of your choosing and no expiration date." The copy says "Delivered by email" and "Good toward any cruise."
4. **Photo provenance.** The silhouette sunset and the deck-rail sunset came from the old HPB Facebook library. Connor should confirm both were shot on HPB boats. Two other sunset photos in that library show another company's boat (a New Orleans "Bayou Boogie" and a Fort Lauderdale "Paddle Pub") and were left out.
5. **Where info@houstonpedalbarge.com lands.** Replies and any bounce stragglers go there. Sweep it after the send.
6. **Houston Booze Cruise** shares this FareHarbor account and this gift card item, so the same card works for both. The emails say Houston Pedal Barge only.
7. **Unsubscribe is account-wide.** The hosted link adds the address to the shared SES suppression list, so an HPB unsubscribe also blocks that address for the other brands that send through this AWS account. Same as NKST.
8. No SMS in this drip. SMS needs its own opt-in list and approval.
