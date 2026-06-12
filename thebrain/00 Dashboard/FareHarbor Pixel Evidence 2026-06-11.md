# FareHarbor Meta Pixel Evidence Packet
*Pulled 2026-06-11 from the Meta Graph API (pixel /stats endpoint), window May 28 - Jun 11, 2026 (15 days). For Zendesk tickets 5530616 / 5552487 / 5586048 / 5602915.*

## The one-line finding

FareHarbor's checkout fires zero Meta pixel events for doorcountykayaktours and the Gravity Trails companies (neworleanskayakswamptours, neworleanspedalbarge), while it fires correctly for lonestarkayaktours and buffalobayoukayak in the same Meta Business account. The pixels themselves are healthy. The connection on FareHarbor's side is what's missing.

## Event totals by pixel (May 28 - Jun 11)

| Pixel | Company | PageView | InitiateCheckout | Purchase |
|---|---|---|---|---|
| 421987437994175 | DCKT (doorcountykayaktours) | 8,183 | 6 | **0** |
| 701301873334767 | Gravity Trails (NKST + NPB) | 56,568 | 43 | **0** |
| 1559188957448084 | LSKT (lonestarkayaktours) | 7,330 | n/a | 117 |
| 381452300055179 | BBK (buffalobayoukayak) | 5,425 | 336 | 22 |

DCKT alone booked roughly 13 reservations a day in this window and NPB 16-23 a day. That is several hundred completed checkouts with zero Purchase events reaching Meta.

## The proof: events by source domain

Same window, same pixels, aggregated by the URL that fired the event:

| Pixel | Events from own website(s) | Events from fareharbor.com |
|---|---|---|
| DCKT 421987437994175 | 8,118 | **0** |
| Gravity Trails 701301873334767 | 55,700+ | **0** |
| LSKT 1559188957448084 | 7,234 | **118** |
| BBK 381452300055179 | 5,660 | **23** |

Two things fall out of this:

1. On the healthy pixels, the fareharbor.com event counts match the Purchase counts almost exactly (118 vs 117, 23 vs 22). Purchases come exclusively from FareHarbor's checkout domain. That is the only place they can come from.
2. The broken pixels have never received a single event from fareharbor.com in this window. The websites fire thousands of PageViews fine, so the pixels work. FareHarbor's checkout simply is not wired to them for these companies.

This rules out: David's website code, GTM, the Meta Business account, ad account permissions, and the pixels themselves. The variable that differs is FareHarbor's per-company conversion-tracking configuration.

## The specific ask for FareHarbor

1. Compare the Facebook/Meta conversion tracking config for **lonestarkayaktours** and **buffalobayoukayak** (working) against **doorcountykayaktours**, **neworleanskayakswamptours**, and **neworleanspedalbarge** (broken). Whatever is set on the first two is missing or wrong on the other three.
2. Attach pixel **421987437994175** to doorcountykayaktours, and pixel **701301873334767** to neworleanskayakswamptours and neworleanspedalbarge, with the full funnel (PageView, InitiateCheckout, Purchase with value) firing in the checkout flow.
3. Make one test booking on each of the three companies and confirm the Purchase event arrives in Meta Events Manager > Test Events before closing the ticket.

## What we can verify on our side

- Meta Events Manager > each pixel > **Test Events**: watch live while FH makes the test booking.
- Events Manager > **Diagnostics** tab on the two broken pixels (should be clean since nothing fires).
- Events Manager > Data Sources > each pixel > Settings: confirm "connection method" (browser vs Conversions API) on the working pixels so FH replicates the same method.

## Draft reply for the ticket

Subject: Pixel data isolating the Purchase tracking bug to FareHarbor's config (tickets 5602915 / 5586048)

Hi team,

We pulled 15 days of raw event data from the Meta API for all four of our pixels and can now isolate this precisely.

Our two working companies (lonestarkayaktours, buffalobayoukayak) receive Purchase events exclusively from the fareharbor.com domain: 118 and 23 events respectively, matching their booking counts.

Our two broken setups received ZERO events from fareharbor.com in the same 15 days: pixel 421987437994175 (doorcountykayaktours) and pixel 701301873334767 (neworleanskayakswamptours and neworleanspedalbarge). Both pixels fire thousands of PageViews from our own websites, so the pixels are healthy. FareHarbor's checkout is just not connected to them for these companies.

Could you compare the Meta conversion tracking config on lonestarkayaktours/buffalobayoukayak against the three broken companies, copy that setup over, then run one test booking on each so we can confirm the Purchase event in Test Events? We're happy to watch Test Events live on a call. Hundreds of bookings a week are invisible to Meta right now and it is blocking our ad program.

Thanks,
David
