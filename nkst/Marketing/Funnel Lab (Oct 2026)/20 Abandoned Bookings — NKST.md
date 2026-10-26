*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for NKST.*

# Abandoned Bookings: NKST (split from file 20)

Question: are we capturing lost bookings with the FareHarbor dashboard and engaging them?

Short answer: the switch is on everywhere, but so far it has recovered almost nothing, and nobody can see how many carts are being abandoned. All figures verified 2026-10-14 via the FareHarbor dashboard (read-only). No guest names or emails in this file, counts only.

## Table

Windows: "since go-live" means since the online cart and the abandoned-cart flag turned on (the first order-bearing online booking in each report landed within hours of the flag change, so the two went live together). Online = booking source "online", cancelled bookings excluded. Gross is booking total before refunds.

| Brand | Abandoned email on? (date, who) | Online cart on? | Online bookings since go-live (guests, gross) | Recovered (abndcrt): bookings / guests / $ | Share of online | Ref tags seen |
|---|---|---|---|---|---|---|
| NKST (neworleanskayakswamptours) | Yes. Set 9/25/26 11:05 AM by FareHarbor staff (Melanie LH) | Yes, live 9/25 | 73 (149 guests, $15,961) | 0 / 0 / $0 | 0% | Site URLs, ad click tags, SM.SBD.FHS, OpenCX, an email tag (nl_em01_manchac) |

Sources for the table:
- Abandoned flag state: verified 2026-10-14 via Settings > Advanced (`/dashboard/settings/advanced/`), checkbox "Enable abandoned cart emails" is checked for all six.
- Who and when: verified 2026-10-14 via the Settings > Bank & Payments activity feed ("Set Enable abandoned cart emails to true"). NPB's entry was found by paging back through the feed.
- Online cart: could not verify via a dashboard setting (it has no visible toggle; FareHarbor staff enable it). Verified indirectly 2026-10-14 via the Advanced Bookings report, where the first online booking carrying an order record appears the same day as the flag, and FareHarbor's help article says the abandoned flag only shows when Online cart is enabled.
- Recovered and online counts: verified 2026-10-14 via Reports > Advanced > Bookings, created-date window 9/1 to 10/14/26, "Online Booking Reference" containing `abndcrt`. DCKT's two earlier recoveries are from our cached booking export (data/bookings), not re-pulled.

## Window totals, 9/1 to 10/14/26 (all online bookings, uncancelled)

| Brand | Online bookings | of which cart orders | abndcrt |
|---|---|---|---|
| NKST | 135 | 67 | 0 |

## Retargeting signals available (Analytics & Tracking pages, verified 2026-10-14, nothing changed)

- GA4: every brand has FareHarbor's GA4 integration connected (NPB 10 properties, NKST 9, DCKT 5, BBK 4, HPB 5, LSKT 8, many are shared network and sister-site properties). Per FareHarbor's help articles that integration sends view_item_grid, view_calendar, view_item_description, view_book_form, add_to_cart and purchase. It does NOT list a begin_checkout event. So a "got to the booking form but did not buy" GA4 audience is built from view_book_form and add_to_cart minus purchase.
- Meta Pixel: NPB and NKST share pixel 701301873334767. DCKT has 421987437994175. BBK has 381452300055179 and 1559188957448084. HPB has 499229350418216 plus three others (some shared with BBK and LSKT). LSKT has 1559188957448084. Which standard events the FareHarbor flow fires into Meta (InitiateCheckout etc.) is not shown on these pages, so unverified. NPB's pixel also has a server-side token stored (not copied here).
- Shared pixels across brands (NPB/NKST, BBK/HPB/LSKT) mean a Meta audience built on one will mix brands unless filtered by URL.

## Ref tags (how much can we tag and match later)

The Online Booking Reference column is populated on most online bookings. Values in the 9/1 to 10/14 window, top by count:

| Brand | Top ref values (count) |
|---|---|
| NKST | neworleanskayakswamptours.com (90); SM.SBD.FHS (10); site plus ad tag (9, 4, 3, 2); blank (6); admirenola.com (4); honeyislandswampkayaktours.com (2); site plus nl_em01_manchac (1) |

What this tells us:
- The reference is auto-filled with the referring site, and ad click IDs and any `?ref=` value get appended after it with a comma (example: site URL, then the tag). So a custom tag does survive into the report.
- Our own tags already work. Cached export (2026 bookings) shows `npb-winback-w01/w02/w03` on NPB, `nl_em01_manchac` on NKST, `OpenCX` on NPB/NKST/DCKT, `austinwelcomecenter` on LSKT. Tagging quiz-lead booking links with `?ref=quiz-<brand>-<variant>` is feasible and we can count conversions per tag with the same report.
- A tag only shows if the guest books through that exact link and the ref is not dropped. Blank refs are high at HPB (64%) and LSKT (38%), so expect some leakage.

## What this means

1. The native abandoned-cart email is on for all six brands, but it is a thin net. One plain email, 2 hours after drop-off, only if the guest typed an email at checkout, and only for the cart flow. Result so far: 0 recovered bookings across about 480 online bookings since go-live, and only 2 recoveries ever at DCKT in 2026 (about 0.13% of its online bookings, $395). Treat it as a free floor, not a recovery program.
2. The windows for NKST and NPB are only 19 days and BBK, HPB and LSKT only 6 days, so 0 is not yet a verdict on the email itself. It is a verdict that we are not seeing a meaningful lift. Recheck on 11/15 with the same pull.
3. We cannot see how many carts are being abandoned. The dashboard has no abandoned-cart report, no count of emails sent, no open or click data. So "capturing" is true only in the sense that the email fires. We cannot calculate a recovery rate.
4. We are not engaging them beyond that one email. FareHarbor's email is not customizable (no brand voice, no discount, no SMS, no second touch). Everything beyond it is on us.
5. The best next lever is outside FareHarbor: GA4 audiences from view_book_form and add_to_cart minus purchase (these events exist), Meta audiences from the pixel (event list unverified), and tagged `?ref=` links on every email, SMS and quiz link so we can match leads to bookings later.
6. Open items: confirm with FareHarbor support whether they can share abandoned-cart send and recovery stats; confirm which Meta events the FareHarbor flow fires; DCKT enable date is unknown (no log entry).

Method note: all dashboard pages were read with GET only. Booking counts came from the Advanced Bookings report (a report-generation request, the same call the Reports page makes). No settings were changed, nothing was saved or sent.
