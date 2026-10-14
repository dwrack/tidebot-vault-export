# Guide Affiliate Links & QR Codes (Reference)

Single source for guide booking links. Updated 2026-10-14.

## The rules
- Guide earns **10% of tour price** on bookings made through their link or QR code, on **NKST tours and NOLA Party Barge**.
- Paid only after the tour **has run and is fully paid**. Never on future, cancelled, refunded, or unpaid bookings.
- Paid every 2 weeks with the semimonthly payroll run.
- No guest discount codes. The pitch is "book through me, it supports me directly."
- No guide links in paid ads or Google listings.

## How it works (updated 2026-10-14)
1. Each card's QR points to a short link we own: NKST guides `neworleanskayakswamptours.com/go/<slug>`, NPB crew `nolapartybarges.com/go/<slug>`.
2. The short link redirects to that person's page on their brand's site (`/guides/<slug>` on NKST, `/crew/<slug>` on NPB). The page features them, lists the tours they actually work first (from FareHarbor crew assignments in `Marketing/Affiliate Kit/crew-tours.json`), then the sister brand's trips. Every Book button is a FareHarbor item link with their code (`ref=asn-<code>`). Built by `Marketing/Affiliate Kit/pages.py`; bios go in the `bio` column of `people.csv`.
3. FareHarbor stamps the code on the booking (shows in the booking's online references). Payroll reads it from there.
4. Because the QR points at our short link, we can change where it goes later without reprinting cards.

**Status:** pages and `/go/` links are NOT live yet (waiting on WordPress app passwords for both sites). Do not print cards until every short link loads.

## Links
Full table with both tracked links per guide: `Marketing/Guide Cards/links.csv`

| Guide | Code | Short link | FH login email |
|---|---|---|---|
| Stephanie Lazensky | stephanielazensky | /go/stephanie | slazensky@gmail.com |
| Nick Napoda | nicknapoda | /go/nick | nnapoda@gmail.com |
| Josh Smith | joshsmith | /go/josh | Joshua.chs@yahoo.com (pay to spoilapoboy@yahoo.com) |
| River Bourne | riverbourne | /go/river | riverbourne.here@gmail.com |
| Michelle Healey | michellehealey | /go/michelle | mcnamml@gmail.com |
| Chelsea Hines | chelseahines | /go/chelsea | Chelseabrooke503@gmail.com |
| Alexis (Lexi) Hingle | alexishingle | /go/lexi | alexishingle023@gmail.com |
| Abbie Marks | abbiemarks | /go/abbie | abbiemarkswriting@gmail.com |
| Emily Clarke | emilyclarke | /go/emily | emchasc@gmail.com |
| Max (FH user maxbush, confirm) | maxbush | /go/max | mxbsh@protonmail.com |

Tracked link pattern:
- NKST: `https://fareharbor.com/embeds/book/neworleanskayakswamptours/?ref=asn-<code>&asn=<code>&full-items=yes&flow=876983`
- Party Barge: `https://fareharbor.com/embeds/book/neworleanspedalbarge/?ref=asn-<code>&asn=<code>&full-items=yes&flow=876976`

## Files (updated 2026-10-14, v2 design)
- Everything prints from `Marketing/Affiliate Kit/`: run `python3 print_kit.py` (or `python3 print_kit.py <code>` for one person).
- Who gets what: `people.csv` (kind = guide for NKST, crew for NOLA Party Barge, affiliate for outside partners). Outside affiliates get a seat-back sign only.
- Output in `out/`: `<code>-card.pdf` (2x3.5 in business card, vector, 1/8 in bleed), `_card-back.pdf` (shared back), `<code>-seatback.pdf` (5x7 sign). PNG previews alongside.
- All links: `Marketing/Affiliate Kit/links.csv`. River Umberger's short link is /go/riveru (River Bourne has /go/river).
- Guide photos go in `Marketing/Guide Cards/photos/<code>.jpg`, then re-run.

## Adding a new guide
1. Add a row to `Marketing/Affiliate Kit/people.csv` and run `python3 print_kit.py <code>`.
2. Create their `/go/<slug>` page.
3. Add them to the Affiliate Master sheet (NOLA tab) and ask FareHarbor to create their affiliate account on both dashboards.

## Open items
- [ ] `/go/` pages live (needs WordPress access, see Desktop "Set NKST WordPress Key.command")
- [x] Max = Max Bush (maxbush), confirmed 2026-10-14
- [ ] Party barge commission rate (assumed 10%) and which entity pays NPB commissions
- [x] Affiliate setup request sent to support@fareharbor.com 2026-10-14 (Kevin left FH)
- [ ] Guide photos
- [ ] Commission line in the payroll tool
- [ ] Print order

## Outreach log
- 2026-10-14: Affiliate setup request emailed to support@fareharbor.com from info@ (Kevin Schmitt left FH). 13 NKST guides + 14 NPB captains/crew, both companies, 10%. Asked for setup by Fri Oct 23.
- 2026-10-14: Slack DMs from TideBot to 22 people asking for a card photo and anything else they want on their card. Replies land in each TideBot DM (bot has im:history, so Claude can collect them).
  - NKST: Stephanie, Nick, Josh, River Bourne, River Umberger, Michelle, Chelsea, Lexi, Abbie, Emily, Max, Jeffrey
  - NPB: Ben, Kelly, Eddie, Ryan, Kingston, Calvin, Desi, Jarrett, Tom, Charles
  - Not in Slack, not DMed: Abbey Johnson (NKST, onboarding), Mike Burton, Carson Roberts, Todd (NPB). Kelly Young vs Kelly: only one Slack "Kelly", DMed that one.

- 2026-10-14: Follow-up to FH Support adding Ryan David Carr (NKST, 13 tours since June) and Tony Lombardino (NPB crew), both missed in the first list.
