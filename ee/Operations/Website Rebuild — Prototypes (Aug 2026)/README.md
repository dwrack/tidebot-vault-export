# Website Rebuild — Homepage Prototypes (Aug 2026)

Three homepage directions for the new ebbandember.com, built ahead of the Sept 9 kickoff. Self-contained HTML files (photos + BASAL font embedded), so they open straight in a browser. These are the visual-feel prototypes; production is the Astro + Cloudflare Pages build per `../Website Rebuild — Static Site Plan (Sept 2026).md`.

## Shareable links (private Claude artifacts)

- **Pitch page for the group** (start here): https://claude.ai/code/artifact/d5f93075-cd30-4d91-b811-4a39d1113a3b
- Concept 01 · Dusk (dark, Bathhouse register): https://claude.ai/code/artifact/d783a020-0394-4a11-96cf-5299cf5b0a89
- Concept 02 · Daybreak (light Nordic, Löyly register): https://claude.ai/code/artifact/084ab00f-c550-4ced-bd64-f14779f7229e
- Concept 03 · River Ritual (cinematic editorial, Sky Lagoon register): https://claude.ai/code/artifact/4419e32f-0609-43c3-94b9-0389ccc554f4
- **Elevated Tides · Vision** (marina-wide "Wellness on the water", WebGL water hero + live USGS river data): https://claude.ai/code/artifact/fa87df6a-c553-457f-936b-db59e92781e2

## v2 additions (2026-08-27)

- **Live river data:** every page shows the Columbia's temperature from USGS gauge 14105700 (The Dalles), fetched on load with the build-time reading (72°F, Aug 27) baked in as fallback. Elevated Tides also shows streamflow (147,000 ft³/s) and gauge height. Free API, no key, hourly updates. The artifact preview sandbox may block the live fetch; production (Astro/Cloudflare) fetches it client-side or via a cached Worker.
- **Video loops:** real footage cut to short muted loops: golden-hour dock (Dusk hero), the Downpour pour (Dusk), rooftop leap (Daybreak), burning sunset (River Ritual hero + Elevated Tides closing). Embedded as base64→blob in the prototypes; production ships them as normal mp4 files. Every video has a still-photo poster fallback.
- **Copy pass:** rewritten more poetic across all pages per Davey's note.
- Note: the CDP debug Chrome on this machine cannot decode video at all (verified with a 7KB test clip), so loop playback couldn't be visually verified there. Files validated with ffmpeg; posters guarantee graceful fallback.

## What's inside every concept

- Copy in brand voice (ritual over transaction, real river, no "float" as a noun, fuel unsaid)
- Real Google reviews quoted verbatim (4.9★, 106 reviews as of Aug 26, 2026)
- LocalBusiness + FAQPage JSON-LD, answer-first intro copy (SEO/AEO/GEO)
- BASAL display + Inter body per brand guide
- Photos from `Assets/Photos/` only; every person shown is consent-cleared (2026-06-23 clearance). The minor's clips were not used.

## Verify before anything ships

- Hours (prototypes say daily 7am–10pm, from Aug IG), session length (1 hr 45 min), pricing ($49/$59 social, $449/$539 private) — confirm against Periode
- Booking CTAs are placeholders; production wires them to Periode
- About page stays "the team" only (standing rule)
