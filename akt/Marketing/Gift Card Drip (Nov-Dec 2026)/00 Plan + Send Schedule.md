# Gift Card Drip to Past Guests (Nov 17 to Dec 29, 2026)

**CURRENT STATUS (2026-11-15): built, tested to David, NOT sent to the list.** Waiting on David's go. One real test of email 1 (subject A, photo A) went to dwrack81@gmail.com. The preflight currently refuses a list send because the shared SES account's complaint rate is 0.173% (limit 0.05%). See Open items.

Same "gift drip" look as the New Orleans Kayak Swamp Tours drip: photo-led, calm serif, one button, no text on photos. Style Menu entry: Designed Email (`email-design`). Preview: `preview/All 7 Emails.html` in this folder.

## The idea
Seven emails to past guests. No discount, no code, no prices. The offer is the gift card itself: you choose the amount, it never expires (both on the live page, checked 2026-11-15). Angles: send someone the skyline view from the water, nothing to ship, winter is mild in Austin. Bat claims match the site: bats are here roughly March through early November, so no winter email promises them.

## Schedule
Email 1 goes the first weekday after David says go. Earliest Tue Nov 17. The calendar still fits all seven beats.

| # | Send | Subject A | Subject B | Photo A | Photo B | Photo C |
|---|---|---|---|---|---|---|
| 1 | Tue Nov 17 | Give them the view from the water | The best seat in Austin is on the water | Kayaks under the Congress Ave Bridge at sunset | Lone kayaker, skyline | Dusk skyline down the lake |
| 2 | Fri Nov 27 (Black Friday) | We're not having a Black Friday sale | No doorbusters on Lady Bird Lake | Turtle on a log | Downtown through a bridge arch | |
| 3 | Thu Dec 3 | Know someone visiting Austin? | Send them where you went | Bridge and tower, blue sky | Skyline behind the bridge | |
| 4 | Thu Dec 10 | For the person who's impossible to shop for | Three people on your list, one answer | Bats over the bridge crowd | Kayaker, towers behind | |
| 5 | Thu Dec 17 | No shipping deadline on this one | The gift that shows up in a minute | Graffiti railroad bridge | Aerial paddlers, railroad bridge | |
| 6 | Tue Dec 22 | It's not too late | Forgot someone? Print this tonight | Sunset kayaks | Dusk skyline | |
| 7 | Tue Dec 29 | Got an Austin Kayak Tours gift card? | Austin winters are made for this | Bridge and towers | Towers and trees | |

Email 6 moved from Dec 23 to Tue Dec 22 so the last-minute send lands before the holiday week. Email 7's main button goes to the Skyline Tour page, every other button goes to FareHarbor gift card checkout. Button text is "Buy a gift card" (email 7: "Pick a date").

## A/B test
Each email goes out in equal groups: subject A or B crossed with the photos (6 groups for email 1, 4 for the rest). Body copy and buttons are identical. Each address is hashed into one group, reshuffled per email, one ledger so nobody gets two versions.
- **Send:** `node send-ses.mjs --email em201-gift-give-the-view --ab --go` from `~/Projects/akt-tools/newsletter-2026/` (run from davids-mbp-2 for the real send).
- **Read it:** `node ab-report.mjs em201-gift-give-the-view` reads opens and clicks per group from CloudWatch (config set `akt-campaign`). Apple Mail pre-loads images, so compare groups with each other only. Ignore clicks the first day (mail scanners).
- **Sales:** FareHarbor `ref=aktgift_g01_<group>` shows which version sold. Subject winner = `a?` against `b?`. Photo winner = `?a` against `?b`.
- Read each email 3 days after it sends and move the winning pattern into the A slot of later emails.

## What is wired (verified 2026-11-15)
- **Gift card item:** FareHarbor item 35014 "Gift Card" on account `lonestarkayaktours`, the buy button on austinkayaktours.com/gift-card/. There is also an older item 46300 "Gift Certificate", not used. Austin Paddle Shack rentals sit in the same account, so this list is the whole Lone Star account, not only Austin tour guests.
- **Sender:** Austin Kayak Tours <info@lonestarkayaktours.com>, replies to austinkayaktours@gmail.com. austinkayaktours.com is NOT verified in SES, so the Lone Star domain is the only option until someone adds the DNS records. DKIM is green.
- **List:** fresh FareHarbor pull today, 20,698 unique emails. Against the Oct 12 export (20,716): 989 added, 1,007 no longer in FareHarbor. Mailable after dropping 57 invalid or booking-site relay addresses and 85 on the SES suppression list: **20,556**.
- **Bounces:** Bounce and Complaint go to SNS topic `akt-ses-events`, feedback forwarding is OFF on lonestarkayaktours.com. No bounce notices will land in the inbox.
- **Tracking:** SES config set `akt-campaign`, CloudWatch dimensions `campaign` and `cell`.
- **Unsubscribe:** hosted one-click link. Lambda `akt-unsubscribe` behind API Gateway `akt-unsubscribe-api`, copy of the NKST handler, own secret. Tested: valid link shows the confirmation page, bad link gives 403. It adds the address to the account-wide SES suppression list (same as every other brand), so an unsubscribe here also stops other brands' sends from this SES account. Mail-scanner prefetch of the link can unsubscribe people, same as NKST.
- **Pacing:** 20/sec with retry. Preflight refuses a send if feedback forwarding is on, relay addresses are on the list, the account is unhealthy, or 24h bounce is 3% or higher or complaints 0.05% or higher.
- **Photos:** `s3://akt-email-assets/email/` (public-read, us-west-2). Pro-style stills from Carousel Picks and the GBP originals, cropped to landscape, 31 to 263 KB each. Guest faces appear only tiny or from behind. Originals in `~/Projects/akt-tools/newsletter-2026/assets/_originals/`.
- **Code:** `~/Projects/akt-tools/newsletter-2026/` (`emails.mjs` copy, `build.mjs`, `send-ses.mjs`, `recipients.mjs`, `ab-report.mjs`, `crop.py`, `shots.mjs`, `unsubscribe-lambda/`). Layout checked at 640 and 390 wide, no overflow.

## Open items
1. **SES complaint rate blocks the send.** Account-wide, 24h complaint 0.173% and bounce 2.91% (checked 2026-11-15), left over from the Nov 6 NKST send. The rolling rate will not recover on its own while volume is near zero. Options: narrow Austin's list to guests who booked in the last 2 to 3 years (fewer old addresses, fewer complaints), or David overrides with `--skip-preflight`. Claude will not override on its own.
2. **Lone Star legal hold.** The guest-drips skill says the Lone Star CRM is under a Chapter 7 legal hold and the hold lifts only when David approves the first Lone Star send. This list is the Lone Star FareHarbor account. David's go is that approval, but selling never-expiring gift cards from an entity in bankruptcy is a question for counsel first.
3. **Confirm gift card details with FareHarbor or the crew:** that the card is emailed to the buyer right away, redeems on every tour and rental, and is entered as a code at checkout (email 7 says so).
4. **Winter schedule.** Email 7 says winters are mild and does not promise dates. Confirm which tours run Dec to Feb before send.
5. **Verify austinkayaktours.com in SES** (DNS records) if David would rather send from the Austin domain.
6. After each send: sweep austinkayaktours@gmail.com for replies and bounces, and rerun `node recipients.mjs` before the next email.
