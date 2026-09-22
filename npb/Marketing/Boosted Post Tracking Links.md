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
