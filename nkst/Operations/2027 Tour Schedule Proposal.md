# 2027 Tour Schedule (approved by David 2026-10-10)

Rule: copy 2026, change as little as possible. FareHarbor times map to OTA pickup times (1 hr 15 min earlier), so every time change = a manual edit on Viator + GetYourGuide (+ Airbnb if still connected).

Last 2026 tour on the books: Dec 31, Manchac 2:00 PM.

## Manchac Swamp Wildlife Kayak Tour (item 11242)
| Period | Times | Change vs 2026 |
|---|---|---|
| Jan 1 - Feb 28 | 11:30, 2:00 | Dropped 9:00 (coldest, ran ~1 in 4 days) and 4:30 (never ran) |
| Mar 1 - Jun ~7 | 9:00, 11:30, 2:00, 4:30 | Same |
| Jun ~8 - Jun 30 | 9:00, 11:30, 2:00, 5:00 | Same |
| Jul 1 - Aug 31 | **8:15**, 11:30, 5:00 | 9:00 -> 8:15 (pickup 7:00), 2:00 closed |
| Sep 1 - Sep 30 | 9:00, 11:30, 2:00, 5:00 | Same |
| Oct 1 - Oct 31 | 9:00, 11:30, 2:00, 4:30 | Same |
| Nov 1 - Dec 25 | 11:30, 2:00 | Dropped 9:00; 4:30 off (same as 2026) |
| Dec 26 - Dec 31 | 9:00, 11:30, 2:00 | 9:00 kept for the busiest week of December |

## Extended Manchac (177480), Whitney Combo (39172), Rentals (225451)
Same as 2026. Extended: 10:00 Jan-Feb, 9:30 Mar-May & Oct-Dec, 8:30 Jun-Sep. Whitney: 8:00 on its 2026 days. Rentals already open through 2027.

## OTA edits required
- Jul 1 - Aug 31: Manchac morning option 7:45 pickup -> 7:00 pickup (tour 8:15). Remove 12:45 pickup (2:00 tour) for those dates.
- Nov-Feb: 7:45 pickup option not offered (closes automatically once FareHarbor has no 9:00).
- Check Airbnb: no Airbnb bookings found in a ~75-booking reseller sample since Jun 2025.

## Why (evidence)
- Jul-Aug 2025 + 2026: 2:00 ran 0 times, 11:30 ran once. Guides (Stephanie, River, Michelle) all flagged midday summer heat; River had heat exhaustion twice; guest lightheaded 7/18.
- Feels-like at Manchac: Jul 92F at 9am, 100F at 1pm. Jan 44F at 9am, 54F at 2pm.
- Jan 2026: 93 Manchac departures offered, 20 ran.
- Wild Louisiana (Manchac Magic): winter 10:00/1:00, spring 10:00/1:00/2:30/4:00, summer 10:00/4:00. No overlap with our times; summer 8:15 puts us 2 hrs ahead of them.
- OTA mix: Viator ~85% of reseller bookings, GetYourGuide ~15%; resellers ~14% of guests.

## Build status
- [x] FareHarbor 2027 availabilities built 2026-10-10 via Availability Schedules "Manchac 2027" (100674), "Extended Manchac 2027" (100676), "Whitney Combo 2027" (100677). Verified per month via API; same capacity, customer types, pickup route 949, custom field + resource groups as 2026. Extended: 10:00 Jan-Feb, 9:30 Mar-May + Sep 16-Dec, 8:30 Jun 1-Sep 15. Public booking page confirmed bookable.
- [ ] Viator Jul-Aug time edit
- [ ] GetYourGuide Jul-Aug time edit
- [ ] Airbnb connection check
- [ ] Public booking page spot-check (Jan, Apr, Jul, Dec 2027)
