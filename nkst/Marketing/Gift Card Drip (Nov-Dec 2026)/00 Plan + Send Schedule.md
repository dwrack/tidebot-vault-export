# Gift Certificate Drip to Past Guests (Nov 6 to Dec 29, 2026)

**CURRENT STATUS (2026-11-06): email 1 SENT to the full list on David's go, 11 days ahead of the original Nov 17 slot.** Emails 2 to 7 are built and not sent. Older lines below that say "not sent" or give Nov 17 for email 1 are history.

## What changed on 2026-11-06 (David's direction)
- **Email 1:** subject and headline are now "Gift them the quiet", button is "Buy a gift card". Sent in six groups: 2 subjects x 3 hero photos (kayaks under golden cypress / cypress reflection with no people / kayaks from above).
- **Buy buttons go straight to FareHarbor checkout** (gift card item 6232) with `ref=gift_g01_<cell>`, so FareHarbor shows which version sold. Applies to every email in the drip.
- **Open and click tracking is on.** SES configuration set `nkst-campaign`, counts in CloudWatch by email and test group. Read with `node ab-report.mjs em201-gift-give-the-swamp` in the newsletter folder. Opens run high because Apple Mail pre-loads images, so compare groups with each other only. This reverses the June 2026 "no SES tracking" call, at David's request.
- **List refreshed from FareHarbor** (was the May 14 export): 30,939 customers, 28,207 mailable after unsubscribes and bounces. 856 added, including 479 who booked since May 15. About 1,400 old addresses with no booking on record are no longer in FareHarbor's customer list and were left out.
- **Open question:** FareHarbor's customer data has no "agreed to be emailed" field, so the list is every customer with an email, minus opt-outs, same as past sends. If there is a consent checkbox at checkout, tell Claude where it lives and the list can be filtered to it.
- **Next:** read email 1 on Mon Nov 9 (3 days in), move the winning subject style and photo type into the A slot of emails 2 to 7, and decide whether email 2 still waits for Black Friday or a new email fills Nov 17.

## Email 1 send log (2026-11-06, about 1:45 to 2:20 pm CT)
- 28,207 accepted by SES in two runs (the first hit the rate limit at 4,995; the sender now paces at 20/sec and retries).
- Checked about 15 minutes after the send finished: account status HEALTHY, account bounce rate 2.7% (SES reviews accounts at 5%), complaint rate 0.03%. The bounce figure was still catching up. **Recheck before email 2.** The per-email tracking showed about 3,800 bounce events, which does not match the account rate; unexplained as of this check.
- Booking-site relay addresses can't receive mail (David, 2026-11-06). 82 were on the list (GetYourGuide, Viator). `recipients.mjs` now drops them for good. 25 GetYourGuide "could not be sent" notices landed in info@.
- Bounced and complained addresses are suppressed automatically by SES. List after this send: 27,043.
- Inbox sweep of info@ (same afternoon): 25 relay bounces, 3 out-of-office, 0 human replies, 1 automated spam-report notice. Sweep the inbox again after every send.
- First tracking read (too early to call): opens 7.2% subject A vs 7.5% subject B; photos within a point of each other. Early clicks are mostly mail security scanners, so ignore clicks until Monday.

Preview: `preview/All 7 Emails.html` in this folder (email 1 there predates the Nov 6 edits).

## The idea
Seven emails, about one a week, to the past-guest list (28,905 mailable as of 2026-10-16, about 95% visitors). No discount, no code, no price claims. The offer is the certificate itself: emailed right away, never expires. That matches the live page (checked 2026-11-05: "Gift certificates do not expire and are immediately emailed to you") and the no-discount rule in the website standards. The one holiday discount we ran on Instagram (Dec 2025, 20% off) reached a third of baseline, so this goes the other way.

Because most of the list lives somewhere else, the angles are "send someone where you went" and "nothing to ship," not "come back this weekend."

## Schedule

| # | Send | Subject | Angle | Hero photo |
|---|---|---|---|---|
| 1 | Tue Nov 17 | Give them the quiet | The opener: give the swamp | Red kayaks under golden cypress (2018 drone shoot) |
| 2 | Fri Nov 27 | We're not having a Black Friday sale | Deadpan no-sale | Bare winter cypress, turtle on a log |
| 3 | Thu Dec 3 | Know someone headed to New Orleans? | Send a friend | Five red kayaks from above |
| 4 | Thu Dec 10 | For the person who's impossible to shop for | Birder / needs a break / the two of you | Channel through gold canopy, from the air |
| 5 | Thu Dec 17 | No shipping deadline on this one | Nothing to ship or wrap, 3 steps | One red kayak in a narrow channel |
| 6 | Wed Dec 23 | It's not too late | Last minute, print it tonight | Sunset cypress silhouette |
| 7 | Tue Dec 29 | Unwrapped a swamp tour? | Use it this winter, or buy your own | Kayak bow on still water |

Email 7's main button goes to the Manchac tour page. Every other button goes to `/gift-certificates/`.

## A/B test (added 2026-11-06)
Every email goes out in four equal groups of about 7,200: subject A or B, crossed with hero photo A or B. Body copy and buttons are identical. Side by side: `preview/A-B Subjects + Photos.html`.

| # | Subject A | Subject B | Photo A | Photo B |
|---|---|---|---|---|
| 1 | Give them the quiet | A gift for someone who has enough stuff | Kayaks under golden cypress | Cypress mirrored in still water (no people) |
| 2 | We're not having a Black Friday sale | No doorbusters in the swamp | Bare winter cypress, close | Gray sky reflection, wide |
| 3 | Know someone headed to New Orleans? | Send them where you went | Kayaks from above | Kayak bow, first person |
| 4 | For the person who's impossible to shop for | Three people on your list, one answer | Gold canopy from the air | Barred owl |
| 5 | No shipping deadline on this one | The gift that shows up in a minute | One kayak from above | Red kayak at dusk |
| 6 | It's not too late | Forgot someone? Print this tonight | Sunset cypress silhouette | Sun over the lake, from the air |
| 7 | Unwrapped a swamp tour? | Winter is the best time to use it | Kayak bow on still water | Kayaks under golden cypress |

- **Send:** `node send-ses.mjs --email em201-gift-give-the-swamp --ab --go`. Each address is hashed into a cell, reshuffled for every email, one ledger so nobody gets two versions. Test one cell: add `--test <address> --variant bb`.
- **Read it:** GA4, campaign `gift_2026`, sessions by `utm_content` (`g01aa_cta`, `g01ab_cta`, `g01ba_cta`, `g01bb_cta`). Subject winner = aa+ab against ba+bb. Photo winner = aa+ba against ab+bb. FareHarbor refs carry the same suffix (`gift_g01_ab`).
- **Limits:** there is no open tracking (David's call, June 2026), so subject lines are judged on clicks, not opens. With about 14,400 people per side and click rates around 1%, only a gap of roughly 25% or more between sides is a real result. Gift sales per cell will be too few to judge on their own.
- Read each email 3 days after it sends. Carry the winning pattern (people vs no people, question vs statement) into the later emails by swapping the A slot.

## Where it lives
- Content: `~/Projects/nkst-tools/newsletter-2026/emails.mjs` (n 201 to 207, layout `gift`). Layout: `renderGift` in `build.mjs`. Backups of both files: `*.bak-20261105`.
- Built files: `out/em201-gift-give-the-swamp.html` through `out/em207-gift-your-seat.html` (+ .txt).
- Photos: `assets/gift-*.jpg` (12 files, 140 to 500 KB), originals in `assets/_originals/`. Sources are the 2018 Fall Drone Shoot and `Assets/Carousel Picks`. No guest faces close enough to identify.
- Tracking: FareHarbor `ref=gift_g01` to `gift_g07`, GA4 campaign `gift_2026`.

## Before the first send
1. Upload the photos: `aws s3 cp assets/ s3://nkst-email-assets/email/ --recursive --exclude "*" --include "gift-*.jpg" --content-type image/jpeg --region us-west-2`, then bump `ASSET_V` in build.mjs and rebuild.
2. Test send to David: `node send-ses.mjs --email em201-gift-give-the-swamp --test <address> --go`.
3. Confirm in FareHarbor that a gift certificate redeems on every tour. Every email says "good toward any tour we run."
4. Buy-flow check: open the gift page with `?ref=gift_g01` and confirm the ref lands on the FareHarbor gift card sale. If it does not, gift revenue has to be read from FareHarbor gift card sales by date instead.
5. Send each email in ONE day (28.9k is under the 62,500/day SES quota). The old `drip.sh` pace of 4,500/day would take a week, which breaks the Black Friday and Dec 23 emails. Run the sends from davids-mbp-2, not the laptop.
6. Email 2 says the bald eagles come back in December and email 7 says through February (from the Holiday Plan). Change it if the guides say otherwise.

## Not in this drip (on purpose)
- The free cypress with $130+ cards from the Growth Playbook: tree cost is still unconfirmed, so it is not advertised.
- Named denominations (Date Morning, etc.): not built in FareHarbor.
- SMS: separate opt-in list, separate approval.
