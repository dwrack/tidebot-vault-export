# Cave Point conditions strip (PARKED 2026-10-16)

*David, 2026-10-16: no weather forecasting on the public site for now; it might drive people away from booking. This file keeps the design and the verified data sources so it can be switched on later. Code: `~/Projects/dckt-site/src/data/conditions.ts` and `src/components/Conditions.astro` (built, tested against live Open-Meteo on 2026-10-16, not rendered on any page).*

## What was built and tested

- **Sources (verified 2026-10-16):** Open-Meteo forecast at 44.95N 87.04W (wind, gusts, direction, sky code, temp, sunrise/sunset, hourly, 7 days) and Open-Meteo marine at the same point (wave height, period, direction; `length_unit=imperial`). No key, CORS allowed, free. NDBC buoy 45002 (mid-lake) gives an observed cross-check (wind 13.6 kt, seas 3.6 ft at 05:50 EDT on 2026-10-16). NOAA CO-OPS 9087072 Sturgeon Bay Canal returned no water-temperature product. Open-Meteo has no lake temperature variable. Water temp would come from NOAA GLERL or the guides.
- **Strip:** one honest line in the Scout voice ("Glass. Days like this are why the caves exist."), then air temp, wind + gusts, wave height, and a GREEN/YELLOW/RED dot. Off-season the line says tours are back Memorial Day weekend.
- **Thresholds (proposed, never confirmed):** GREEN under 12 mph and under 1.5 ft; YELLOW under 18 mph and under 2.5 ft; RED above. Taken from the 2026 cancellation analysis and the GREEN/YELLOW/RED playbook.
- **7-day row:** day chips with high temp, max wind, max wave, color.
- **Architecture:** build-time snapshot in a data attribute, refreshed in the browser; production version would be a Cloudflare Pages Function `/api/conditions` cached 15 minutes in KV.
- The Elevated Tides site does the same thing for sauna sessions (`~/Projects/elevatedtides-site/src/data/conditions.ts`, Open-Meteo + USGS river gauges, canvas sky with real sun and moon positions).

## If it comes back: softer versions that still reassure

1. **No numbers, just the promise.** "We check the wind at dawn and text you before you drive out." (This is what ships now, in the copy.)
2. **Season-only, positive-only.** Show the strip only when the lake is GREEN, hide it otherwise. Nobody sees a red day; calm days get a nudge to book the morning slot.
3. **Private, for the team.** Same strip on an unlisted `/ops/conditions/` page the guides use for the 7am call; nothing public.

## Photo options (unchanged, parked)

See 00 Plan.md section 4: real camera (hardware $250 to $450 plus LTE $10 to $15/mo, or a free guide-photo routine through the TideBot group DM) versus Higgsfield-generated state frames keyed to the forecast (one-time credits, honest label). Nothing bought or generated.
