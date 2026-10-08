# Fall 2026 E-Bike Site Swap

*Started 2026-10-07. Approved by David: e-bike rental becomes the fall hero, kayak tours marked as back in 2027.*

## Status

**Nothing on the live site has been changed yet.** WP login reached the 2FA step (code sent to dwrack81@gmail.com) and stopped there: pulling the code from personal Gmail was blocked by the session's permission guard. Next run needs David to type the 2FA code into the Claude Chrome window (or allow the Gmail read), then the steps below take about 20 minutes.

Before screenshots (taken 2026-10-07, public homepage):
- `Screenshots/homepage-before-2026-10-07-desktop.png`
- `Screenshots/homepage-before-2026-10-07-mobile.png`

## FareHarbor check (public availability API, 2026-10-07)

| Item | FH id | October | November |
|---|---|---|---|
| Cave Point E-Bike Rental ($30/hr) | 221394 | Bookable every day Oct 7 to 31 | Bookable every day |
| Cave Point E-Bike Tour, guided ($99) | 208420 | Slots open Oct 7 to Oct 12 only (10am/12pm/2pm) | None |
| All kayak tours (5669, 5784, 23855, 156126, 156132) | | None | None |

**David: the guided tour still takes bookings through Oct 12.** If staff are gone, close those slots in FareHarbor. The site plan below does not promote the guided tour either way.

## The "before" state (record for revert)

**Homepage hero** (row `#hero-row-1`, video-row/hero-row)
- Background image: `/wp-content/uploads/sites/2281/2023/06/33117483_194537807836293_65012739570925568_o.jpg`
- H1: `Door County Kayak Tours`
- Subhead: `More than just kayaking!`
- Section heading under it: `Top Rated Tours in Door County!`

**Homepage activity grid** ("Top Rated Tours", row-4 activity-grid), current order:
1. Cave Point County Park Kayak Tour
2. Cave Point and Whitefish Dunes 1/2 Day Kayak Tour
3. Door Bluff County Park Shipwreck Kayak Tour
4. Door Bluff Shipwreck 1/2 Day Kayak Tour
5. Cave Point E-Bike Rental
6. Cave Point Ebike Tour

**/activities/ page:** same kayak-first order (Cave Point, Half-Day, Door Bluff, Door Bluff Half-Day, Eco Estuary, then E-Bike Rental, E-Bike Tour, Quad Bike, Paddle Board).

**"Choose Your Activity" tiles:** Kayak (left), E-Bike Tours (right).

## Planned changes (when logged in)

1. **Activity grid order (homepage + /activities/):** move Cave Point E-Bike Rental to slot 1. Leave every kayak activity in place, same slugs, just below. Leave the guided e-bike tour where it is (do not promote).
   - On this FareHarbor theme the grid order comes from the homepage ACF "activity grid" relationship field (drag order) and, on /activities/, from each activity's menu order / the archive's ordering field. Check which one controls it before touching anything; write down the exact field and old values here.
2. **Hero:** swap background to an existing media-library e-bike shot. Best candidate: `/wp-content/uploads/sites/2281/2020/02/curvy-road-cave-point-ebike-tour.jpg` (fallback `Cave-Point-Fat-Tire-E-Bike-Rentals.jpg`). Note: the library has **no true fall-color e-bike still**, so the curvy-road canopy shot is the closest. Check it renders at 1600w without blurring.
   - H1 stays `Door County Kayak Tours` (brand + SEO). Subhead: `Fall color by e-bike` 
   - Add/point the hero button: `Book an E-Bike` linking to `/activities/e-bike-rental/`.
3. **Kayak note:** one small line under the grid heading or in the callout banner: `Kayak tours return May 2027. E-bike rentals are open daily this fall.` (Plain text, no popup.)
4. **Do not** delete anything, change slugs, or unpublish kayak activities.

## How to revert (spring 2027, before kayak season)

1. Hero: restore background `.../2023/06/33117483_194537807836293_65012739570925568_o.jpg`, subhead `More than just kayaking!`, remove the e-bike button (or point it back to the old target, record it here when changed).
2. Activity grid: drag back to the order listed above (Cave Point kayak first, e-bike rental fifth).
3. Delete the "Kayak tours return May 2027" line.
4. Compare against the before screenshots in `Screenshots/`.

## Change log

| Date | Change | Old value | New value | By |
|---|---|---|---|---|
| 2026-10-07 | none yet, blocked at WP 2FA | | | Claude |
