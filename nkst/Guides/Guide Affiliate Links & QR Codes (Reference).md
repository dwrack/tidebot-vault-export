# Guide Affiliate Links & QR Codes (Reference)

Single source for guide booking links. Updated 2026-10-14.

## The rules
- Guide earns **10% of tour price** on bookings made through their link or QR code, on **NKST tours and NOLA Party Barge**.
- Paid only after the tour **has run and is fully paid**. Never on future, cancelled, refunded, or unpaid bookings.
- Paid every 2 weeks with the semimonthly payroll run.
- No guest discount codes. The pitch is "book through me, it supports me directly."
- No guide links in paid ads or Google listings.

## How it works
1. Each card's QR code points to our own short link: `neworleanskayakswamptours.com/go/<name>`.
2. That page shows two buttons, **Swamp Kayak Tour** and **NOLA Party Barge**, each a FareHarbor link tagged with the guide's code (`ref=asn-<code>`).
3. FareHarbor stamps the code on the booking (shows in the booking's online references). Payroll reads it from there.
4. Because the QR points at our short link, we can change where it goes later without reprinting cards.

**Status:** the `/go/` pages are NOT live yet. Do not print cards until every short link loads.

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

## Files
- Cards (print-ready, 2x3.5 in, 300 dpi, 1/8 in bleed): `Marketing/Guide Cards/print/<code>.pdf`
- QR codes alone (PNG + SVG): `Marketing/Guide Cards/qr/<name>.png|svg`
- Guide photos go in `Marketing/Guide Cards/photos/<code>.jpg`, then run `python3 make_cards.py` in that folder.

## Adding a new guide
1. Add a row to `GUIDES` in `make_cards.py` (display name, full name, code, slug) and run it.
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
