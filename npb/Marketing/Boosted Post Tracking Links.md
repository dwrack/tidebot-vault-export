# Boosted Post Tracking Links

Created 2026-09-22. Use these as the link on any boosted post so GA4 and the Meta pixel can attribute bookings to the boost.

| Boosting from | Use this link |
|---|---|
| Facebook | https://nolapartybarges.com/boost |
| Instagram | https://nolapartybarges.com/boost-ig |

Each is a 302 redirect (WordPress Redirection plugin, IDs 7 and 8) to the homepage with UTMs:
- /boost -> ?utm_source=fb&utm_medium=boost&utm_campaign=boosted_post
- /boost-ig -> ?utm_source=ig&utm_medium=boost&utm_campaign=boosted_post

## Where to read results
- GA4 (nola-pedal-barge, 322288940): Reports > Acquisition > Traffic acquisition, filter session source/medium = fb / boost or ig / boost. Purchase + revenue columns work (FareHarbor purchase events already flow into this property, 514 in the last 30 days).
- Meta: the pixel (701301873334767) is already on the site and fires Purchase. Ads Manager only shows those purchases if the boost is paid from ad account act_87863118. Boosts paid from a personal card / the IG app show zero conversions no matter what link is used.

## Why a link and not "a tag"
The GA4 tag and Meta pixel live on the site, not in the link. The link just carries UTM labels so the visit gets filed under "boost" instead of generic facebook.com / instagram.com referral.

## Seafood cruise video links (added 2026-09-23)

Land on the dedicated page https://nolapartybarges.com/sunset-cocktail-cruise-seafood-boil/ (has GA4, the Meta pixel, and the FareHarbor book button for item 448372). One link per video cut so GA4 can show which edit sold. Redirection plugin IDs 9-18.

| Video cut | Facebook boost | Instagram boost |
|---|---|---|
| 01 Crab Boil On A Boat | nolapartybarges.com/seafood-01 | nolapartybarges.com/seafood-01-ig |
| 02 Dinner In New Orleans | nolapartybarges.com/seafood-02 | nolapartybarges.com/seafood-02-ig |
| 03 Skip The Restaurant | nolapartybarges.com/seafood-03 | nolapartybarges.com/seafood-03-ig |
| 04 What You Get | nolapartybarges.com/seafood-04 | nolapartybarges.com/seafood-04-ig |
| 05 Fast Cut | nolapartybarges.com/seafood-05 | nolapartybarges.com/seafood-05-ig |

UTMs carried: utm_source=fb|ig, utm_medium=boost, utm_campaign=seafood_cruise, utm_content=ad01..ad05.

Reading results in GA4 (322288940): Explore or Reports > Acquisition > Traffic acquisition, filter session campaign = seafood_cruise, add secondary dimension session manual ad content (ad01-ad05). Purchases and revenue are per item, so filter item name = Sunset Cocktail Cruise & Seafood Boil (7 sold / $1,155 in the 90 days to 2026-09-23, so expect small numbers).

If the videos run from Ads Manager instead of as boosts, skip the short links and paste this into the ad's URL parameters field so it matches the existing fb/paid convention:
utm_source=fb&utm_medium=paid&utm_campaign=seafood_cruise&utm_content={{ad.name}}
