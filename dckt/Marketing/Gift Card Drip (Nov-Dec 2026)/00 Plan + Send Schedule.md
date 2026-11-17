# Gift Card Drip to Past Guests (Nov 17 to Dec 29, 2026)

**CURRENT STATUS (2026-11-16): built, tested, NOT sent. Design pass done 2026-11-16 (opaque logo band, enhanced photos, square split crops, two close-up guest photos removed, copy trimmed). List recounted today: 30,639 mailable.** One test of email 1 went to David's inbox. Nothing has gone to the list. The send is also blocked by the SES preflight (see "Blocker" below). Style: the Style Menu "Designed Email" gift drip look (photo-led, calm serif, one button), same as the NKST drip.

Preview (all 7 at phone width + the A/B photo grid): `preview/All 7 Emails.html` in this folder.

## Blocker: SES preflight refuses the send
- Checked 2026-11-15 (CloudWatch, account-wide, us-west-2): complaint rate **0.173%** (the sender's gate is 0.05%, AWS reviews accounts at 0.1%) and bounce rate **2.91%** (gate 3%, AWS reviews at 5%).
- The account is shared by every brand. These numbers are left over from the NKST send on Nov 6 (28k emails), and almost nothing has been sent since, so they will not drop on their own. DCKT has never been mailed from SES at this scale, about 16,700 of its addresses last booked in 2022 or earlier, and 6,134 have no booking date at all.
- `--skip-preflight` exists but only David can authorize it. Claude did not use it.
- Recommended: send in recency waves and read the rates between waves (below). Wave 1 is small enough to move the account numbers a little but not to hurt them.

## Send schedule (one day each, paced 20/sec)

| # | Send | Subject A | Subject B | Angle |
|---|---|---|---|---|
| 1 | Tue Nov 17 (or the first weekday after David says go) | Give them the sea caves | A gift for someone who has enough stuff | The opener |
| 2 | Fri Nov 27 (Black Friday) | We're not having a Black Friday sale | No doorbusters at the sea caves | Deadpan no-sale |
| 3 | Thu Dec 3 | Know someone headed to Door County? | Send them where you went | Send a friend |
| 4 | Thu Dec 10 | For the person who's impossible to shop for | Three people on your list, one answer | History buff, needs a break, the two of you |
| 5 | Thu Dec 17 | No shipping deadline on this one | The gift that shows up in a minute | Nothing to ship or wrap, 3 steps |
| 6 | Tue Dec 22 | It's not too late | Forgot someone? Print this tonight | Last minute, print it tonight |
| 7 | Tue Dec 29 | Unwrapped a Door County gift card? | Pick your day for next summer | Use it next summer, or buy your own |

All seven beats fit the calendar, nothing merged or dropped. DCKT is closed for the season, so every angle is a gift for next summer's paddle. No discounts, no codes, no prices, no safety claims. Signed "The crew at Door County Kayak Tours". Button text is "Buy a gift card" everywhere except email 7's main button ("Pick your tour", goes to the Cave Point tour page); email 7's "Nobody got you one?" link is the buy link.

## Ramp for email 1 (recency waves)
The list is cold. Mail newest guests first and read the account rates after each wave. `--since` filters on last booking date; the ledger skips anyone already sent, so waves never double-send.

| Wave | Who | Count | Command adds |
|---|---|---|---|
| 1 | Booked 2025 or later | 3,494 | `--since 2025-01-01` |
| 2 | Booked 2023 or later | about 4,300 more | `--since 2023-01-01` |
| 3 | Booked 2020 to 2022 | about 7,900 more | `--since 2020-01-01` |
| 4 | Everyone else, including 6,134 with no booking date | about 15,000 more | no `--since` |

Stop and look if a wave pushes bounce past 3% or complaints past 0.05%. Emails 2 to 7 go to everyone the earlier waves reached.

## A/B test
Six groups for email 1 (subject A or B, crossed with three hero photos), four groups for emails 2 to 7 (subject x two photos). Body and buttons are identical. Each address is hashed into one group, reshuffled for every email, one ledger so nobody gets two versions. Wave 1 groups are about 600 each, so only a large gap (roughly 25%+) is a real result.

| # | Photo A | Photo B | Photo C |
|---|---|---|---|
| 1 | Kayak entering a sea cave | Tandem kayak from above, clear water | Shipwreck outline, one kayaker |
| 2 | Calm coast, no people | Rock ledges and horizon, no people | |
| 3 | Kayaks at Cave Point from above | Kayaks along a forested bluff | |
| 4 | Kayaks under a limestone cliff | Peninsula from the air | |
| 5 | Wooded point from the air | Shipwreck wide, two kayaks | |
| 6 | Kayaks along the shoreline | Kayaker under a stone arch | |
| 7 | Kayaks along a bluff | Kayak over a shipwreck | |

## How to read results
- **Opens and clicks:** `cd ~/Projects/dckt-tools/newsletter-2026 && node ab-report.mjs em201-gift-next-summer` (campaign key = the email file name; reads CloudWatch, SES config set `dckt-campaign`). Opens run high because Apple Mail pre-loads images, so compare groups with each other only. Early clicks are mostly security scanners, so read clicks 3 days after the send. Test sends are tagged `test` and excluded.
- **Sales:** FareHarbor shows the version that sold: the buy link carries `ref=gift_g01_aa` (email number, then subject letter, then photo letter). Subject winner = aa+ab+ac against ba+bb+bc. Photo winner = aa+ba against ab+bb (and ac+bc for email 1).
- **After each email:** move the winning pattern (people vs none, question vs statement) into the A slot of the next ones in `gift-emails.mjs`, rebuild, re-upload nothing unless photos change.

## Tracking and safety wiring (verified 2026-11-15)
- SES config set `dckt-campaign` created: CloudWatch destination, dimensions `campaign` and `cell` from message tags, events send, delivery, open, click, bounce, complaint, reject.
- Identity `doorcountykayaktours.com`: Bounce and Complaint go to SNS topic `dckt-ses-events`, feedback forwarding is now OFF (it was ON, which is what flooded NKST's inbox). Changed by Claude today.
- Unsubscribe: hosted one-click link plus `List-Unsubscribe-Post`, no mailto. Suppressed and unsubscribed addresses are dropped when the list is built (9,486 on the account-wide SES suppression list; 2,122 of them were on DCKT's export).
- Booking-site relay addresses (GetYourGuide, Viator, TripAdvisor, Expedia and similar) are filtered out of the list, and the preflight re-checks that.
- Pacing 20/sec with retry (SES limit is 31/sec). Preflight refuses a list send unless forwarding is off, no relay addresses are on the list, the account is healthy, and 24h bounce under 3% and complaints under 0.05%.

## The list
- Fresh pull from FareHarbor 2026-11-15: **32,773 customers** (the May 14 export had 31,751): 3,488 new addresses, 1,543 of them booked since May 15; 2,466 old addresses are no longer in FareHarbor's customer list.
- Mailable after suppression, relay filter and bad addresses: **30,639**.
- FareHarbor has no "agreed to be emailed" field, so this is every customer with an email minus opt-outs and bounces, same as past sends.

## After each send (do not skip)
1. Sweep info@doorcountykayaktours.com for bounce notices, out-of-office and replies; report counts. With forwarding off there should be almost no bounce mail.
2. Check account bounce and complaint rates before the next wave or email.
3. Read `ab-report.mjs` 3 days in.

## Where it lives
- Code: `~/Projects/dckt-tools/newsletter-2026/`: `gift-emails.mjs` (copy), `gift-build.mjs` (layout, A/B cells), `send-ses.mjs` (`--ab`, `--since`, pacing, preflight), `ab-report.mjs`, `recipients.mjs` (relay filter), `render-check.mjs`, `gift-preview.mjs`. Backups of the old sender and recipients builder: `*.bak-20261115`. The summer 2026 series files are untouched.
- Built files: `out/em201-gift-next-summer.html` through `em207-gift-your-seat.html` (+ `.aa` etc. group files).
- Photos: `assets/gift-*.jpg` (1200px, 68 to 205 KB), originals in `assets/_originals/`, uploaded to `s3://dckt-email-assets/email/` (cache-bust ASSET_V 20261115a). Pro drone and DSLR stills from `Assets/DCKT/DCKT Photos/Cave Point/`. No guest faces are identifiable (guests are small or seen from above). There is no winter or ice footage in the library.
- Gift card item in FareHarbor: item 5784 ("Buy your Gift Card" on /gift-cards/). Page checked 2026-11-15: gift cards do not expire, are emailed right away, and are good on any tour or in-store purchase.
- Send commands (from the folder, on davids-mbp-2 for the real send):
  - Wave 1 live: `node send-ses.mjs --email em201-gift-next-summer --ab --since 2025-01-01 --go`
  - One test: `node send-ses.mjs --email em201-gift-next-summer --ab --test <address> --variant aa --go`

## Other gift emails and ads (checked 2026-11-15): nothing is actually scheduled
- The TheBrain portfolio notes say "gift-card email scheduled Dec 1/14, SES smoke test passed." Looked for it everywhere: laptop `dckt-tools`, davids-mbp-2 (launchd, cron, project folders), the CRM database `crm_dckt` (only anniversary and win-back views, `send_enabled` is false, zero sends), AWS EventBridge and Scheduler (only the 15-minute lead runner), and the vault. **No Dec 1 or Dec 14 send exists.** It is a plan line, not a job. The only earlier gift material is the Nov 5 draft plan (`Marketing/Gift Certificate Emails 2026/00 Plan.md`, one built email, never sent), which this drip replaces.
- **Rule: this drip is the only gift email stream, one per week.** The Dec 3 and Dec 17 sends cover the Dec 1 and Dec 14 weeks. If a Dec 1 "2027 early-bird" or Dec 14 gift email gets built later, do not send it as a gift email: drop it, or move the early-bird (dates open Jan 5) to January. Nobody gets two gift emails in one week.
- **Meta ads:** paused campaign "DCKT Holiday Gift Cards 2026" (2 gift-card ads, $10/day) is due on Dec 20 to warm audiences. It does not collide with email. Exclude gift card buyers from the audience when it goes on.

## Open items
1. **David's go**, and what to do about the preflight (wait, ramp, or skip-preflight on his say).
2. **Footer address:** emails use 8442 State Hwy 42, Fish Creek (the legal address). The site footer shows a Jacksonport address. Pick one.
3. **FareHarbor checks before email 1:** a gift card redeems on every tour, and `?ref=gift_g01_aa` on the buy link shows up on the gift card sale. If the ref does not land, read gift sales by date instead.
4. **Copy to confirm:** email 7 says "back on the water next season" (no date promised); email 1 says Door Bluff has a shipwreck you can see through the water (matches the drone footage and the Door Bluff Shipwreck tour).
5. **Wreck photos:** the vault says the Door Bluff tour visits the Schooner Fleetwing; the drone wreck shots are not labeled, so copy says only "a shipwreck you can see through the water at Door Bluff". Confirm they are that wreck before any caption names it.
6. **Buy link:** someone removed `&full-items=yes` from the FareHarbor buy link in `gift-emails.mjs` on 2026-11-16 (the brief asked for it). Both forms return 200. Left as is.
7. Not in this drip on purpose: bonus credit, named denominations, SMS (needs the checkout opt-in).
