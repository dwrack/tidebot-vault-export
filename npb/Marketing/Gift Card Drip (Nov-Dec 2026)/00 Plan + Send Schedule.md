# NPB Gift Card Drip to Past Guests (Nov 17 to Dec 29, 2026)

**CURRENT STATUS (2026-11-15, checked live today): built, tested, NOT sent to the list.** Seven emails with A/B cells are built. One test of email 1 went to David only (2026-11-15, subject A, photo A). Nothing goes to guests until David says go in the gift-card-drip session. The send preflight currently REFUSES a list send (see "Before the first send").

Preview: `preview/All 7 Emails.html` (phone-width, scroll sideways) and `preview/A-B Subjects + Photos.html`. Style: the NKST "gift drip" look (photo-led, calm serif, one button), adapted to NPB: teal and cream, the logo's own deep blue masthead, boat-on-the-water photography. Style Menu entry: Designed Email (`email-design`).

## The idea
Seven emails, about one a week, to past guests. No discount, no code, no prices. The offer is the gift card itself: any amount, no expiration date, good for any trip. Most past guests are visitors, so the angles are "give the crew a boat day," "send a friend where you went," and "nothing to ship," not "come back this weekend."

## How the gift card really works (checked 2026-11-15, differs from the NKST copy)
- FareHarbor item 116006 "Gift Card" on `neworleanspedalbarge`. Description: "A gift card in any amount, with no expiration date. Good for any trip we run." Sales are final.
- At checkout the buyer adds the recipient's email and a personal note. FareHarbor emails the recipient right away. A buyer who wants to send it later enters their own email and resends. (Source: FareHarbor help, Gift Card FAQs, local copy in `~/Projects/fareharbor-help`.)
- So the copy says "sent by email with a note from you," never "emailed to you in a minute." The NKST emails say the latter.
- The NPB site has no gift card page (`/gift-certificates/` and `/gift-cards/` both 404 on 2026-11-15). Every Buy button goes straight to FareHarbor checkout with `ref=gift_gNN_<cell>&full-items=yes`.
- The same FareHarbor account also holds NOLA Bike Bar tours, so the guest list includes some Bike Bar guests. The copy never mentions the bike bar. Decision for David below.

## Schedule (dates moved 2026-11-15)
Email 1 goes the first weekday after David says go, earliest Tue Nov 17. All seven beats still fit, nothing merged. Email 6 moved from Wed Dec 23 to Tue Dec 22.

| # | Send | Subject A | Angle |
|---|---|---|---|
| 1 | Tue Nov 17 | Give the whole crew a boat day | The opener |
| 2 | Fri Nov 27 | We're not having a Black Friday sale | Deadpan no-sale |
| 3 | Thu Dec 3 | Know someone headed to New Orleans? | Send a friend |
| 4 | Thu Dec 10 | For the person who's impossible to shop for | Three people, one answer |
| 5 | Thu Dec 17 | No shipping deadline on this one | Nothing to ship |
| 6 | Tue Dec 22 | It's not too late | Last light |
| 7 | Tue Dec 29 | Unwrapped a boat day? | Use it, or get your own |

Email 7's button goes to the boats page (`/our-boats/`); the closer link goes to the gift card checkout. Every other button goes to the gift card checkout.

## A/B test
Every email splits guests into cells: subject A or B, crossed with hero photo A or B (email 1 also has photo C, so six cells). Body copy and buttons are identical. Each address is hashed into a cell, reshuffled per email, one ledger so nobody gets two versions.

| # | Subject B | Photo A | Photo B | Photo C |
|---|---|---|---|---|
| 1 | A gift for someone who has enough stuff | Boat on blue water, group aboard | Boat at golden hour, marsh island | Boat head-on with red paddlewheel |
| 2 | No doorbusters on the bayou | Storm clouds over old wrecks and cypress | Two boats under gray sky, bridge | |
| 3 | Send them where you went | Boat along a marsh bank | Striped-canopy boat close up | |
| 4 | Three people on your list, one answer | Boat head-on, deck full | Boat turning at dusk | |
| 5 | Nothing to wrap, nothing to track | Boat from directly above | Boat cruising into a pink sunset | |
| 6 | Forgot someone? Fix it in a minute | Orange sunset over still water | Boat lit pink at the dock at night | |
| 7 | Got a gift card? Here's how to use it | Boat on open blue water | Thatched tiki boat at dusk | |

Side by side: `preview/A-B Subjects + Photos.html`.

## How to read results
- **Opens and clicks:** `cd ~/Projects/npb-tools/newsletter-2026 && node ab-report.mjs em201-gift-whole-crew` (reads CloudWatch, SES config set `npb-campaign`). Apple Mail pre-loads images and security scanners click links, so opens run high and early clicks are mostly bots. Compare cells with each other only, and read 3 days after a send.
- **Sales:** FareHarbor refs `gift_g01_aa` etc. Subject winner = aa+ab+ac against ba+bb+bc. Photo winner = aa+ba against ab+bb (and ac+bc for C).
- Carry the winning pattern into the A slot of the later emails.
- Gift sales per cell will be too few to judge on their own. Do not call a winner on fewer than about 25% difference in clicks.

## The list (pulled fresh 2026-11-15)
- FareHarbor customer profiles pulled: 46,984 with an email (June export: 41,801).
- Mailable after cleanup: **45,368**. Removed: 388 invalid or booking-site relay addresses (GetYourGuide, Viator, TripAdvisor and similar), 1,228 on the SES suppression list or the 21-address NPB text opt-out file (applied as email opt-outs to be safe).
- Versus June: 8,514 addresses are new since the June export, 4,947 June addresses are gone or no longer mailable. Net +5,183 raw.
- No booking-site relay address is on the list. `recipients.mjs` drops them for good.
- FareHarbor has no "agreed to email" field, so as with past NPB sends the list is every customer with an email minus opt-outs.

| Last booking | Addresses |
|---|---|
| 2024 or later | 19,028 |
| 2022 to 2023 | 12,068 |
| Before 2022 | 2,632 |
| No booking date on record | 11,640 |

## Tracking and unsubscribe (wired and tested 2026-11-15)
- Sender: `NOLA Party Barge <info@nolapartybarges.com>`, domain verified in SES us-west-2. Reply-To the same.
- SES config set `npb-campaign`: CloudWatch with dimensions `campaign` and `cell`. The test send is tagged `cell=test` so it stays out of the A/B counts.
- Bounce and Complaint for the domain now go to SNS topic `npb-ses-events`, and bounce forwarding to the inbox is OFF (it was on, which would have flooded info@ exactly like NKST's send did).
- Hosted one-click unsubscribe: Lambda `npb-unsubscribe` behind API `jdgz4o9xb2`. Tested: page link returns the confirmation, one-click POST returns 200, a bad token returns 403. Test address cleaned from the suppression list. Header is URL form with `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, never mailto.
- Photos: S3 bucket `npb-email-assets` (public read, created 2026-11-15), originals kept locally in `assets/_originals/`, never uploaded. All web files under 170 KB.
- Code: `~/Projects/npb-tools/newsletter-2026/` (`emails.mjs` copy, `build.mjs` layout, `send-ses.mjs`, `recipients.mjs`, `ab-report.mjs`, `preview.mjs`).

## Before the first send (the preflight is the gate)
1. **Preflight currently fails.** On 2026-11-15 the account's 24-hour complaint rate is 0.173% (limit in the sender: 0.05%) and the bounce rate is 2.91% (limit 3%). Both come from the Nov 6 NKST send and SES scores them account-wide, so NPB inherits them. The sender refuses until they fall. Recheck right before send; do not use `--skip-preflight` unless David says so.
2. **Send in recency waves, not one blast.** 11,640 addresses have no booking date and 14,700 are from 2022 or earlier, which is where bounces live. Suggested: wave 1 `--since 2024-01-01` (19,028), read bounce and complaint rates, then `--since 2022-01-01 --until 2024-01-01`, then the oldest and undated last, each on its own day. The cell hash is stable across waves and the ledger stops double sends. This is slower than NKST's one-day blast on purpose.
3. Confirm in FareHarbor that a gift card redeems on every trip (the copy says "good for any trip we run," which matches the item description).
4. Run the send from davids-mbp-2, not the laptop.
5. After the send, sweep info@ for bounces and replies and report counts.

Send command for wave 1 of email 1 (dry run first, then add `--go`):
```
node send-ses.mjs --email em201-gift-whole-crew --ab --since 2024-01-01
```

## Open items
- David's go to send (copy approved, then wave plan).
- Include the Bike Bar guests? They are in this FareHarbor account and cannot be separated in the export. Recommended: yes, same ownership and same card.
- The unsubscribe link suppresses on a plain page load (the Lambda acts on GET). A mail scanner that opens the footer link could unsubscribe a guest by accident. Same pattern as NKST. Fixing it means changing the shared Lambda, so it is not done here.
- The unsubscribe suppression is account-wide in SES, so an NPB opt-out also blocks that address for the other brands that send through this AWS account.
