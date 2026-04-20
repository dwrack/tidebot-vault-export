# Meta Pixel Audit — All Businesses

**Date:** April 14, 2026
**Status:** Critical issues found

---

## Summary

Audited all known business websites for Meta/Facebook pixel installation. Found 3 critical problems:

1. **Austin Kayak Tours has NO Facebook pixel at all** (money is blind)
2. **Pearl River Kayak Tours (NKST funnel) has NO Facebook pixel** (leaking conversions)
3. **Wild Louisiana Tours has NO Facebook pixel** (if this is yours, same problem)
4. **All NOLA FareHarbor sites share one pixel** (701301873334767) which may be fine if that's your pixel, but needs verification in Meta Events Manager

---

## Full Pixel Map

### NOLA Businesses (gravity_trails BM)

| Site | URL | FB Pixel | Other Tracking | Platform |
|---|---|---|---|---|
| NKST (main) | neworleanskayakswamptours.com | 701301873334767 | GA4, Mixpanel, Reddit | FareHarbor |
| Hidden Adventure Tours | hiddenadventuretours.com | 701301873334767 | GA4, Mixpanel | FareHarbor |
| Crescent City Kayak | crescentcitykayak.com | 701301873334767 | GA4, Mixpanel | FareHarbor |
| Admire NOLA (umbrella) | admirenola.com | 701301873334767 | GA4, GTM-TBS82FFN, Mixpanel | FareHarbor |
| NOLA Bike Bar | nolabikebar.com | 701301873334767 | GA4, TikTok, Mixpanel | FareHarbor |
| NOLA Party Barges | nolapartybarges.com | 701301873334767 | GA4, Reddit, Mixpanel | FareHarbor |
| Pearl River Kayak Tours | pearlriverkayaktours.com | **NONE** | GA4 only | Squarespace? |
| Wild Louisiana Tours | wildlouisianatours.com | **NONE** | GA4, GTM-KNZ49FZ, Mixpanel | FareHarbor |

**Action needed:**
- Verify pixel 701301873334767 belongs to your gravity_trails ad account (check in Meta Events Manager)
- Install pixel on pearlriverkayaktours.com immediately
- Install pixel on wildlouisianatours.com if this is your site
- All sites only fire PageView. Need to verify InitiateCheckout and Purchase events (NKST audit showed InitiateCheckout is broken)

### Austin (lskt BM)

| Site | URL | FB Pixel | Other Tracking | Platform |
|---|---|---|---|---|
| Austin Kayak Tours | austinkayaktours.com | **NONE** | GA4, TikTok, Mixpanel | FareHarbor |

**Action needed:**
- **CRITICAL: Install your LSKT ad account pixel immediately.** Zero conversion data flowing to Meta. Any ads running are optimizing blind.

### Houston (buffalo_bayou BM)

| Site | URL | FB Pixel | Other Tracking | Platform |
|---|---|---|---|---|
| Buffalo Bayou Kayak | buffalobayoukayak.com | 381452300055179 | GA4, GTM-TKMN5XSX, Mixpanel | FareHarbor |
| Houston Pedal Barge | houstonpedalbarge.com | 1559188957448084 | GA4, TikTok, Mixpanel | FareHarbor |

**Action needed:**
- Two different pixels for two businesses under same BM. Verify both pixels belong to the buffalo_bayou ad account.
- Check if InitiateCheckout and Purchase events are firing (likely same FareHarbor issue as NKST)

### Door County (dckt BM)

| Site | URL | FB Pixel | Other Tracking | Platform |
|---|---|---|---|---|
| Door County Kayak Tours | doorcountykayaktours.com | 421987437994175 | GA4, GTM-PPSHWZB, TikTok, Google Ads AW-1070576804 | FareHarbor |
| DC Detours | dcdetours.com | 421987437994175 | GA4, GTM-WT56WQPK, Mixpanel, Google Ads AW-1070576804 | FareHarbor |
| Ebike Tours | doorcountykayaktours.com/e-bike-tours/ | 421987437994175 (inherits) | Same as main site | FareHarbor |
| Airstream Sauna | doorcountykayaktours.com/airstream-sauna-rental/ | 421987437994175 (inherits) | Same as main site | FareHarbor |

**Action needed:**
- Both DC sites share pixel 421987437994175, which is good (same BM)
- Ebike and Sauna are subpages, so they inherit the main pixel. But there's no way to distinguish kayak vs. ebike vs. sauna conversions unless you set up separate custom events or use URL-based conversion rules.
- Check InitiateCheckout and Purchase events

### Portland (NO BM)

| Site | URL | FB Pixel | Other Tracking | Platform |
|---|---|---|---|---|
| Ebb & Ember | ebbandember.com | 1619838955837804 | GA4 G-YF8FPEWW4S | Période |

**Action needed:**
- Has its own pixel but NO Business Manager. Need to create a BM and ad account.
- Pixel has consent-based loading (GDPR). May reduce tracking if visitors decline cookies.
- Uses Période for bookings, NOT FareHarbor. Different data export process.

---

## Pixel-to-BM Verification Needed

| Pixel ID | Sites Using It | Expected BM | Verified? |
|---|---|---|---|
| 701301873334767 | 6 NOLA sites | gravity_trails | **NEEDS CHECK** |
| 381452300055179 | buffalobayoukayak.com | buffalo_bayou | **NEEDS CHECK** |
| 1559188957448084 | houstonpedalbarge.com | buffalo_bayou | **NEEDS CHECK** |
| 421987437994175 | 2 Door County sites | dckt | **NEEDS CHECK** |
| 1619838955837804 | ebbandember.com | none (no BM) | **NEEDS CHECK** |

---

## Conversion Event Status

From the NKST audit, InitiateCheckout is broken (3,338 landing page views, only 4 IC events). This is a FareHarbor integration issue and is likely broken on ALL FareHarbor sites.

**Events to verify on every site:**
- [ ] PageView (likely working everywhere)
- [ ] ViewContent (tour page views)
- [ ] InitiateCheckout (booking form opened)
- [ ] Purchase (booking completed)

---

## Priority Fix Order

1. **Today:** Install FB pixel on austinkayaktours.com (zero tracking = blind spend)
2. **Today:** Install FB pixel on pearlriverkayaktours.com (NKST funnel leak)
3. **Today:** Verify all pixel IDs belong to correct ad accounts in Meta Events Manager
4. **This week:** Fix InitiateCheckout event across all FareHarbor sites (likely a FareHarbor dashboard setting or custom code snippet)
5. **This week:** Set up BM + ad account for Ebb & Ember
6. **This week:** Create URL-based conversion rules for DCKT to separate kayak vs. ebike vs. sauna bookings

---

## All Known Domains by Business

### NOLA Kayak Swamp Tours (NKST)
- neworleanskayakswamptours.com (main)
- hiddenadventuretours.com (funnel)
- crescentcitykayak.com (funnel)
- pearlriverkayaktours.com (funnel, NO PIXEL)
- wildlouisianatours.com (funnel?, NO PIXEL)

### NOLA Party Barge
- nolapartybarges.com (main, also used for Houston)

### NOLA Bike Bar
- nolabikebar.com

### Umbrella
- admirenola.com (NOLA umbrella site)

### Austin Kayak Tours
- austinkayaktours.com (NO PIXEL)

### Buffalo Bayou Kayak
- buffalobayoukayak.com

### Houston Pedal Barge
- houstonpedalbarge.com

### Door County Kayak Tours
- doorcountykayaktours.com (main, also hosts ebike + sauna)
- dcdetours.com (funnel)

### Ebb & Ember
- ebbandember.com (NO BM)
