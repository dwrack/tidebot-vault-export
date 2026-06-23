# Pinterest Strategy & Execution Plan — DCKT

_Created 2026-06-22. Account: **@dckayaktours** (Door County Kayak Tours, llc.)_

## Account audit (as of 2026-06-22)

A 7-year-old account left to drift, not a blank slate.

- **541 followers · 1.2k following · 706 monthly views.** Following > followers, near-zero reach = run like a personal account, never optimized for traffic.
- **Last 30 days: 664 impressions, 52 engagements, 5 saves.** Functionally dormant.
- **4 ad campaigns in history, 0 active.**
- Website is linked (doorcountykayaktours.com) but need to confirm it's **claimed/verified**, not just typed in the bio (claiming unlocks pin analytics + attribution on all pins linking to the site).

### Boards (8)
| Board | Pins | Age | Disposition |
|---|---|---|---|
| All Pins | 147 | 2y | keep |
| Pin Our Products | 25,900 | 4d | INVESTIGATE — likely group board or feed dump, not ours |
| Eco Kayak Tours | 73 | 4mo | keep, rename to keyword |
| Cool Door County | 46 | 6y | keep, rename to keyword |
| Door County Cave Kayak Tours | 13 | 2y | keep → "Cave Point Sea Caves" |
| Door County T-Shirts | 11 | 7y | HIDE (merch discontinued) |
| Burning man | 8 | 6y | HIDE (off-brand) |
| Door County Biking | 1 | 2y | keep → "Door County Ebike" |

Decision (David, 2026-06-22): **hide off-brand boards, don't delete.** Investigate the 25.9k board before touching it.

## What's working (the signal)

Top pins, last 30 days:
1. **Ephraim: Things to Do in the White Village** — 156 imp, 22 eng
2. **Baileys Harbor: Things to Do on the Quiet Side** — 65 imp, 9 eng
3. **Door County Kayak Tours | Kayaking and Ebike Tours** (brand/sales pin) — 57 imp, **1 eng**

**Takeaway:** Town "things to do" guide pins win; the salesy brand pin gets impressions but ~zero engagement. Pinterest is a planning/search engine. Lead with destination guides that link to blog posts, never "book our tour." This matches the existing town pillar pages (Baileys Harbor, Fish Creek, Ephraim).

## Strategy

- **Pinterest = visual search engine.** Keyword everything: pin title (first 40 chars matter most), description, board names, bio. Pull keywords from Pinterest's own search autocomplete.
- **Vertical 2:3 pins (1000x1500).** Blog heroes are landscape; crop to vertical with `sips`. Naturally tall shots (overhead paddlers, bluffs, sea cave mouths) perform best.
- **Saves + outbound clicks are the scored metrics**, not likes. Every pin links back to the matching blog post.
- **One blog post = 2–3 pins** (different hooks, different images, same URL). Volume without new content.
- **Pins compound 3–6 months.** Posting now during peak season (May–Oct window) pays out all season.

## Board plan (keyword-named)

- Door County Kayaking
- Cave Point Sea Caves (rename existing cave board)
- Things to Do in Door County
- Door County Travel Guide
- Wisconsin Adventure Travel
- Door County Ebike (rename biking board)

## First content batch (priority order — proven formats first)

1. Town guides (Ephraim, Baileys Harbor, Fish Creek) — already top performers
2. Cave Point sea caves
3. Shipwreck / clear-bottom
4. Half-day bluff picnic tour

## Posting cadence

A few fresh pins/day beats a one-time dump. Once API Standard access lands → move to a scheduler (launchd, same as GBP poster).

## API vs Playwright

- **Now: Playwright** (David's choice). Posts publicly today, no approval. Brittle, can't pull analytics cleanly.
- **Parallel track: apply for Pinterest API v5 Standard access.** Trial access only creates sandbox pins (visible to creator only) — useless for publishing. Standard requires an app review (screen-recording of the integration, proper OAuth). Days to ~2 weeks. The API is the only clean way to pull per-pin outbound clicks/saves and to schedule posting. Token handled via a one-click `.command` (OAuth), never pasted in chat.

## Status / next actions

Done 2026-06-22:
- [x] Investigated `Pin Our Products` (25.9k) + `Eco Kayak Tours` — both gone from profile (were group/collab boards). Nothing to clean.
- [x] **Archived 9 off-brand boards** (verified each shows "Archived"): Peace Signs, Funny, Burning man, Door County T-Shirts, Door County Friends, Stuff I Want to Make, Your Pinterest Likes, Gearage Cool Gear, Landscaping Ideas for Business. Public profile now shows only on-brand boards. Reversible (archived, not deleted).
- [x] Confirmed `doorcountykayaktours.com` is **already claimed** (attribution live).
- [x] **Rewrote bio** (live): "Door County kayak tours and e-bike rentals in Wisconsin. Paddle the sea caves at Cave Point and the Door Bluff cliffs. Beginner-friendly and family-friendly. Book early in the day for the calmest water."
- [x] Fixed duplicate `playwright` MCP definition (removed project scope; kept persistent-profile local) — was causing disconnects.

Done 2026-06-23 (Batch 01):
- [x] Built reusable pin generator: `~/Projects/dckt-tools/pinterest/make_pin.py` (1000x1500, hook + CTA overlay).
- [x] Created 5 keyword boards: Cave Point Sea Caves, Door County Travel Guide, Door County Kayaking, Door County E-Bike Rentals, Things to Do in Door County.
- [x] **Published 8 hook-forward pins**, each linking to a real blog/tour page (manifest: `Pinterest Pins/_batch01_manifest.md`):
  1. Cave Point Sea Caves (cliff jump) → cave-point blog
  2. Clearest Water aerial → cave-point blog
  3. Ephraim town guide → Ephraim post
  4. Calmest Paddle (eco) → /kayak-tours/
  5. E-Bike Rentals → /e-bike-tours/
  6. Door Bluff Shipwreck → /kayak-tours/
  7. Baileys Harbor town guide → Baileys post
  8. 7 Adventurous Things to Do → things-to-do post

Remaining:
- [ ] Batch 02: Fish Creek town, sauna, pregnancy-safe paddle, clear-bottom shipwreck angle, SUP
- [ ] Set posting cadence / scheduler (don't dump all at once long-term)
- [ ] Consider native **Instagram auto-publish** + **RSS auto-publish** to Pinterest
- [ ] Start API v5 Standard access application (parallel)

Public boards kept: All Pins (147), Door County Cave Kayak Tours (13), Cool Door County (46), Door County Travel Tips (19), Best Places to Stay in Door County (2), Door County Events (2), Door County Biking (1).
