# Gift Certificate Drip to Past Guests (Nov 17 to Dec 29, 2026)

**Status (2026-11-05): BUILT, NOT SENT.** Nothing has been uploaded or mailed. Preview: `preview/All 7 Emails.html` in this folder.

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
