# Pixel + NAP Fixes (2026-11-16)

## FareHarbor reply on Meta pixels (HPB)
Source: Stephanie Schwartz (FH Enterprise Account Mgmt), 11/12, screenshot of the HPB FareHarbor integrations. New account rep: Lauren Thomassen (cc'd, traveling that week, "will be in touch").

| Pixel in FareHarbor | Label | Server-side (CAPI token + source URL)? | Notes |
|---|---|---|---|
| 499229350418216 | Houston PBarge Pixel | YES, source URL houstonpedalbarge.com | Only pixel getting server-side Purchase events. Not the one the ads use. |
| 381452300055179 | (none) | NO, browser only | This is the pixel the HPB ads optimize on. Explains "bookings but no Purchase". |
| 1559188957448084 | (none) | NO, browser only | Pixel on houstonpedalbarge.com. |
| CPJLM3BC77U0TG5MFUGG | (none) | NO | That's a TikTok-format ID sitting in a Meta slot. Misconfigured; ask FH to remove. |
| TikTok pixel | Custom code | n/a | "Edit to see setup" |

Stephanie's offer: FH can add an access token + event source URL to the Ads pixel (381452300055179) so Purchases come through server-side.

Fix (pick one):
- Recommended: point the ads at 499229350418216 (already has CAPI) OR give FH a CAPI token for 381452300055179. One pixel, one dataset.
- Ask FH to delete the TikTok ID from the Meta list.
- Security: the screenshot in that email shows the 4992... CAPI access token in plain text. Rotate it in Events Manager after the fix.

## Houston Booze Cruise IG link
Live 11/16: @houstonboozecruise bio link = `http://houstonboozecruise.com/` (2 redirects before landing on https://www.houstonboozecruise.com/). Instagram only allows link edits in the mobile app, logged in as @houstonboozecruise.
Fix: IG app > Edit profile > Links > change to `https://www.houstonboozecruise.com/`.

## NPB NAP (checked live 11/16)
Canonical (recommended): **NOLA Party Barge, 2101 Paris Road, New Orleans, LA 70129, (504) 264-1056, https://nolapartybarges.com**

| Where | Shows now | Change to | Edit at |
|---|---|---|---|
| GBP main | "Nola Party Barge - Swamp Tour Party Boat" | "NOLA Party Barge" (keyword suffix risks a suspension) | business.google.com |
| Website schema + og:site_name | "New Orleans Party Barge" | "NOLA Party Barge" | WP SEO/schema settings |
| Facebook page (89k) | "New Orleans Party Barge" | "NOLA Party Barge" (only if you pick NOLA) | Page settings |
| neworleanstikiboats.com | NPB address + phone under "New Orleans Tiki Boats"; schema phone malformed "++15042641056" | fix phone to +15042641056 | that site's CMS |
| GBP sibling "New Orleans Party Boats" | 2360 N Villere St, (504) 264-6046, neworleanspartyboats.com | leave (10/31 decision), confirm it's a real 2nd location | — |
| IG @nolapartybarge | link www.nolapartybarges.com | fine | — |

Muse was partly wrong: no live "Pedal Barge" name or "Tiki Tours" domain; nolapedalbarge.com just redirects.
DECIDED 2026-11-16 (David): **NOLA Party Barge**.

## HPB NAP (checked live 11/16)
Canonical (recommended): **Houston Pedal Barge, 2515 E NASA Pkwy, Seabrook, TX 77586, (832) 974-0365, https://houstonpedalbarge.com**

| Where | Shows now | Change to | Edit at |
|---|---|---|---|
| GBP | "Houston Party Barge", 2511 East NASA Pkwy #101 | name + address to canonical (once dock address confirmed) | business.google.com |
| Website schema + Contact page title | "Houston Party Barge" | "Houston Pedal Barge" | WP SEO plugin, Contact page |
| Website /contact/ | placeholder "(999) 999-9999" (2x) | delete | WP Contact page |
| Facebook / IG | "Houston Pedal Barge" | check About phone/address/link | Page settings, IG app |

DECIDED 2026-11-16 (David): name **Houston Pedal Barge**. Still open: dock 2515 or 2511 #101? (Memory rule: never market pedaling; "Party Barge" may be the better public name. If so, flip FB/IG instead of GBP.)

Not verified: FareHarbor company profiles, Yelp, TripAdvisor, Apple Maps, FB About fields.
