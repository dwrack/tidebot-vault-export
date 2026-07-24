# NPB Ops & Marketing Deep Dive — July 2026

Built 2026-07-18 from FareHarbor Advanced Bookings (availability dates Jan 2018 – Jul 18 2026, cancelled-refunded excluded), the Crew Summary report (Jan 1 – Jul 18 2026), and 60 days of #nola-party-barge Slack history. Raw data: [[npb-ads-data-pack.json]] and `npb-bookings-2018-2026.csv` in this folder.

## The one-paragraph story

NPB grew fast from 2020 to a $2.23M peak in 2023, went flat in 2024 (more bookings, less money per booking), then contracted two years straight: Jan–Jun revenue fell 22.8% in 2025 and another 16.4% in 2026. The decline is a volume problem, not a pricing problem, and it is not evenly spread: the two tiki boats are holding while everything else fades. Freaky Tiki is only down 8% this year; Bayou Boogie and Party Queen have lost 60-70% of their 2023 business. Pricing per head has actually stabilized ($81/pax, $249/booking, party of 3), so the fix is filling seats on the right products at the right times, which is exactly what ad dollars can do.

## Multi-year trend

| Year | Bookings | Pax | Revenue | $/booking | $/pax |
|---|---|---|---|---|---|
| 2020 | 237 | 372 | $159,548 | $673 | $429 |
| 2021 | 2,791 | 9,656 | $1,104,691 | $396 | $114 |
| 2022 | 5,550 | 17,421 | $1,695,489 | $305 | $97 |
| 2023 | 8,537 | 25,255 | $2,231,776 | $261 | $88 |
| 2024 | 9,782 | 27,937 | $2,199,413 | $225 | $79 |
| 2025 | 7,088 | 19,975 | $1,598,851 | $226 | $80 |
| 2026* | 3,100 | 9,494 | $772,801 | $249 | $81 |

*2026 through July 18.

Same-window (Jan–June only, all complete months):

| Year | Pax | Revenue | YoY rev |
|---|---|---|---|
| 2023 | 11,545 | $1,073,374 | +40.2% |
| 2024 | 13,374 | $1,073,732 | flat |
| 2025 | 10,017 | $829,016 | -22.8% |
| 2026 | 8,290 | $693,151 | -16.4% |

The silver lining in 2026: party size is back up (2.82 → 3.06) and $/booking recovered from $225 to $249. Fewer groups, slightly bigger and better-paying ones. July is pacing behind even the -16% trend ($80k through the 18th vs $179k for all of July 2025), though last-minute weekend bookings will close some of that gap.

## Where the decline actually lives (Jan–Jun revenue)

| Item | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| The Freaky Tiki | $367k | $372k | $346k | $319k |
| The Twerkin' Tiki | — | $252k | $229k | $191k |
| The Bayou Boogie | $258k | $158k | $105k | $99k |
| The Party Queen | $199k | $117k | $96k | $59k |
| Private Pirate Pontoon | $59k | $17k | $7k | $3k |

Two things jump out:

1. **2024 was never really flat.** Twerkin' Tiki launched and put up $252k, but Bayou Boogie dropped $100k and Party Queen dropped $82k the same window. The new boat mostly cannibalized the fleet, then in 2025 the whole pie shrank.
2. **The tiki brand is the business now.** Freaky + Twerkin' = 74% of 2026 revenue. Bayou Boogie and Party Queen have lost well over half their business since 2023, and the Pirate Pontoon is functionally dead ($3k this year). That's an argument for the pirate rebrand concept already floating in this vault: the asset is idle, and the pirate identity would give it a reason to exist again.

## Seasonality (2021–2025 combined, share of annual revenue)

May–September carries 61.7% of the year. July is the single biggest month (13.7%), and the Feb–March ramp (4.4% → 7.6%) is real, driven by Mardi Gras and spring weather. December and January together are 3.5% of the year.

Product-level wrinkle: **Chill Mural pedal tour is a spring product** (59% of its revenue lands Feb–May, near zero after August), and **Irish Channel pub crawl is a shoulder-season product** (peaks March and Sep–Oct). They fill exactly the months the tiki boats don't.

## Day of week and time of day

Fri–Sun = 90% of revenue, and that concentration has not budged since 2022 (82% in 2021, 90-91% every year since). Saturday alone is 44-50%. The weekday-revenue optimism from June: real but tiny; Tuesday + Wednesday combined are still under 4% of revenue. Monday and Thursday are the only weekdays with a pulse (~2.7% each).

Best times (share of 2021-25 revenue): 2pm (24.9%), 4pm (24.7%), 6pm (20.0%), 12pm (18.2%). The 10am slot only works on Saturdays (2,419 pax in 2024-26 vs ~450 on Fri/Sun) — that's a proven Saturday-morning market, not a daily one.

Strongest single blocks (2024-26 pax): Sat 4pm (6,611), Sat 2pm (6,361), Sat 12pm (4,939), Sat 6pm (4,663), Fri 2pm (4,093), Fri 4pm (3,902).

## Crew workload (Jan 1 – Jul 18, 2026) vs Slack presence

1,778 crew-shifts across 26 people; top three carried 63%.

| Crew | Shifts | Bookings | Pax | Slack msgs (60d) |
|---|---|---|---|---|
| Eddie | 494 | 1,868 | 5,956 | 0 |
| Ben Thrower | 378 | 1,436 | 4,206 | 8 |
| Calvin | 242 | 1,010 | 3,192 | 27 |
| Charles | 156 | 648 | 2,004 | 0 |
| Tom | 150 | 754 | 2,056 | 71 |
| Kingston | 132 | 564 | 1,554 | 18 |
| Ryan | 114 | 560 | 1,578 | 0 |
| Kelly | 112 | 504 | 1,740 | 27 |
| Jarrett | 104 | 438 | 1,278 | 15 |

The playbook's warning holds here: chat activity is a terrible proxy for workload. Eddie is running a quarter of the operation and says nothing in Slack. Sophia Bevans is the #1 poster (76 msgs) with zero manifest shifts — makes sense, she's running the beverage program, not boats. Tom is the only person who's both high-workload and high-visibility. Worth remembering for recognition, scheduling asks, and who actually needs SMS-first comms.

## What this means for Meta + Google Ads

Use [[npb-ads-data-pack.json]] as the source of truth when building campaigns. The plays, in priority order:

1. **Defend the heroes, don't spread.** Freaky Tiki and Twerkin' Tiki are what people buy (74% of 2026). Creative, landing pages, and the bulk of prospecting spend go there. Bayou Boogie and Party Queen get remarketing/overflow positioning, not prospecting budget, until they're repositioned.
2. **Budget follows the calendar.** Heavy May–August, ramp starting mid-February (Mardi Gras + spring), taper October, near-dark Dec–Jan. August and September are still big months (12.7% + 10.5%) — don't let spend fall off a cliff after July 4th; the back half of summer is where 2025 bled.
3. **Fish Tue–Fri for the weekend.** Bookings shifted last-minute (in-week for that weekend, per the May analysis), so weight delivery Tue–Fri even though rides happen Fri–Sun. Don't buy weekday-ride demand that doesn't exist; the products that fill weekdays are private charters, not $80 seats.
4. **Sell the slots that sell.** 2pm and 4pm anchor the day; the ad-visible inventory story is "afternoon golden hour on the bayou." Saturday 10am is a proven second market (brunch cruise angle) worth its own creative test.
5. **ROAS math inputs:** AOV $249, party of 3.06, $81/head. A $25 CPA on a booking is a 10x return before repeat/word-of-mouth.
6. **Counter-seasonal products exist — use them.** Chill Mural (Feb–May) and Irish Channel (Mar, Sep–Oct) deserve small dedicated campaigns exactly when tiki demand is soft, instead of generic year-round neglect.
7. **The two-year decline is the brief.** Spend didn't cause the fade of Bayou Boogie/Party Queen, and spend alone won't fix it. But volume is the whole problem (price is holding), so paid + the FB organic poster + YouTube drip pushing the two hero boats in peak windows is the highest-confidence lever available.

## Rerun

To refresh this: "run the FareHarbor deep-dive playbook on NPB" with the playbook doc. Note for next time: the shortname is `neworleanspedalbarge` (not pbarge), and the FareHarbor report UI can silently stop polling after a network blip — if "Generating..." runs past ~3 minutes, hit `/api/v1/companies/neworleanspedalbarge/reports/<id>/` directly; the report was likely done long ago.
