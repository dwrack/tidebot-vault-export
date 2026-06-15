# YouTube Action Plan — New Orleans Kayak Swamp Tours

*Built 2026-06-13 using the portfolio method: [[YouTube Channel Playbook — All Businesses]]. This is the second brand through the system after NOLA Party Barge. Cast and series design lives in [[YouTube Cast & Series 2026]]. Scripts in `Marketing/YouTube Scripts/`.*

Channel: **New Orleans Kayak Swamp Tours**, @neworleanskayakswamptours, id `UCNLC1hBSxXF0zqCzndY8rig`. 43 videos, 181 subscribers, 567K lifetime views at start.

Managed through the `youtube-nkst` MCP, which is channel-locked to this channel and will hard-stop if pointed anywhere else. Do not use `youtube-npb` on this channel.

---

## Step 1 — What the data actually says

Pulled YouTube Analytics for the trailing 12 months (2025-06-13 to 2026-06-13).

**Traffic sources (the reality check):**

| Source | Views | % |
|---|---|---|
| ADVERTISING (paid) | 66,760 | ~89% |
| EXT_URL (website embeds) | 4,048 | ~5% |
| YT_SEARCH (organic) | 1,793 | ~2.4% |
| Everything else | ~600 | ~1% |

Same story as NPB: the channel looks healthy on the surface (72.8K views, 76% retention) but **89% of it is paid advertising.** There is almost no organic engine. The job here is not more views, it is conversion and building an organic base that compounds.

**Organic search terms people actually use to find us (the gold):**

1. **manchac swamp bridge** (the #1 organic term)
2. new orleans swamp tour
3. swamp tour new orleans
4. honey island swamp tour
5. honey island swamp
6. jean lafitte swamp tour
7. new orleans fishing
8. kayak fishing

The lesson: people search **the swamp, the place, and fishing.** Almost nobody searches "kayak rental." So we title for the swamp, the Manchac bridge, Honey Island, gators, and fishing, not for the product. The bridge term is the standout, and the bridge carries the Julia Brown haunting legend, which is story + SEO in one keyword.

---

## Step 2 — Repackage in place (DONE, with a small tail)

Every public video was edited in place (no re-uploads, so view history and ranking are preserved). Each got:
- A new title that front-loads a real Step-1 search term, then a hook. (Colon separators, no em dashes, per house style.)
- A description with a one-line hook + booking link with per-video UTM + the brand boilerplate + 3 hashtags.
- A consistent 15-tag set built from the Step-1 terms, weighted per video (fishing videos get the fishing tags up front, bridge video gets Julia Brown / haunted tags, etc.).

**Booking links by video type** (all carry `?utm_source=youtube&utm_medium=video&utm_campaign=<slug>`):
- Manchac videos → `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/`
- Honey Island videos → `/tours/swamp-kayak-tours/honey-island-kayak-swamp-tours/`
- Extended / Shell Bank → `/tours/swamp-kayak-tours/shell-bank-half-day-extended-bayou-adventure/`
- Everything else → `/tours/swamp-kayak-tours/`

**Cross-brand cleanup:** `G6TBWhZKTT8` was a Door County Zip Line "Spokesnail" promo sitting on the NKST channel. Set to **unlisted** (it belongs to a different business). Reversible if David wants it back.

**Channel branding:** description rewritten around the silent-kayak / Manchac / Honey Island / gators / fishing / restoration story with a booking link, and keywords set to the full Step-1 term list.

### Quota tail — finish after midnight Pacific 2026-06-13
The YouTube Data API daily quota (shared OAuth project, also used by the NPB rebuild today) ran out before the last 4 videos. **38 of 42 are fully done.** Re-run these 4 once quota resets:

| Video ID | New title | Link type / slug |
|---|---|---|
| `J_tLI9nIGb0` | Kayaking the New Orleans Swamp: Manchac Bayou | general / kayaking-swamp |
| `P5GRpe2paa0` | 360 Swamp Tour by Kayak: New Orleans Manchac Bayou (VR) | general / 360-swamp |
| `mYF3yjf-e9w` | Swamp Shake: Fun on a New Orleans Kayak Swamp Tour | general / swamp-shake |
| `_J2No6Em6GE` | New Orleans Funk: Street Music in the Big Easy | general / nola-funk |

(`eBxRw2p8gZo` did go through before the quota wall.) Use the same description template and tag set as the rest. Drafts of all four are ready in `Marketing/YouTube Scripts/_repackage-tail.md`.

---

## Step 3 — The storytelling layer (the subscriber engine)

Full design in [[YouTube Cast & Series 2026]]. In short, the NKST cast (calmer and more naturalist than NPB's party energy):

1. **The Manchac Bridge series** — anchored on the #1 search term + the Julia Brown haunting legend. Story + SEO goldmine.
2. **The Bayou Report** — a naturalist host doing a weekly conditions-and-wildlife update that drives this-weekend bookings.
3. **Hank the Heron** (mascot) — a great blue heron with a dry, watchful naturalist personality. A calmer counterweight to NPB's Alfred the gator, and a real bird people see on every tour.
4. **Kayak Fishing the Bayou** — an untapped search lane ("new orleans fishing," "kayak fishing") we already have footage for.
5. **Honey Island Swamp Monster crossover** — a recurring "did we just see it?" bit shared with the sister Honey Island brand. Best pure story hook in the portfolio.

---

## Step 4 — Conversion plumbing (manual, do in Studio)

The API cannot do these. ~20 minutes in YouTube Studio:
- **Pin a comment** with the booking link on the top videos: `MtkbjS1OuOw` (467K), `N8XLyvQcdT0` (39K), `7zOnhtJsQxE` (22K Honey Island), `kt4HQpbhwhA` and `wBB97_Yy2NA` (baby gator), `fMUlR38rOzc` (Manchac bridge), `B7gsteXj45s` (kayak fishing).
- **End screens + "subscribe" cards** on those same winners.
- **Avatar / profile pic**: confirm it is the clean NKST logo (API cannot set it).
- The @handle is already correct (@neworleanskayakswamptours), nothing to do there.
- Embed the best long-form Manchac walkthrough on the matching website tour page as the booking-closer.

---

## Step 5 — The repeatable engine

- **Playlists (built):** Manchac Swamp Tours by Kayak `PLMGswIMe1ETw`, Honey Island Swamp Tours `PLPZe5AVO42s8`, Alligators & Swamp Wildlife `PLeyZVEDsQt9U`, Kayak Fishing the New Orleans Bayou `PLfky8Vcb7afg`, Meet the Guides & Guest Stories `PLMrxLYjo3jUM`, Bayou Restoration & Our Eco Mission `PLaiDojYJaG7k`. **Seeding mapping is below** (also blocked by the quota wall, finish after reset).
- **Cadence:** 3-4 Shorts/week from the footage library + 1 weekly Bayou Report + 1-2 long-form/month. Lean on the seasonal and weather angles, winter is a strong booking window here.
- **Monthly:** re-pull the Step-1 traffic + search reports, double down on whichever pillar holds retention and converts.

### Playlist seeding mapping (run after quota reset)
Add winners first so a single view becomes a binge.

- **Manchac `PLMGswIMe1ETw`:** MtkbjS1OuOw, N8XLyvQcdT0, AhQWd2UQ1qI, 1elM5JvrjJk, fMUlR38rOzc, 5-zA-PbwPVQ, ywO7UDRXKpM, Ac-ZTXW5TMc, oYrobgKDuvQ, nbFJIjFcfl0, e4lOnYdY9Ss, J_tLI9nIGb0, P5GRpe2paa0, HWu3dvzC0_o, uru8T7t1Mj8
- **Honey Island `PLPZe5AVO42s8`:** 7zOnhtJsQxE, RUeJtAJKQCs
- **Wildlife `PLeyZVEDsQt9U`:** kt4HQpbhwhA, wBB97_Yy2NA, fMUlR38rOzc(optional), Hp1UAG7qmcs, 8-KOh8MSPTI, 4hBDfmDoxxg, 1SiY97I3kmI, 4kEq_kzIzlY, IVt0LvTAMT0, BPgWytD1AfQ
- **Kayak Fishing `PLfky8Vcb7afg`:** B7gsteXj45s, vyvEm3GD9mU, eYX1qyYte68
- **Guides & Guests `PLMrxLYjo3jUM`:** e20_WGo0IcQ, 1kb7rjPmbWk, B5HO0UeBO2k, tOHOAHmC9iU, gW7sb0QPEE8
- **Eco / Restoration `PLaiDojYJaG7k`:** WBz6ZLFKDl8, npl5xISVubo, GzetYF9EfT8

(The two New Orleans music clips, jnriGzJUJtM and _J2No6Em6GE, stay out of the swamp pillars on purpose.)

---

## Status log
- **2026-06-13:** Step 1 data pulled (89% ads confirmed). 38/42 videos repackaged in place. Door County cross-brand video unlisted. Channel branding + keywords updated. 6 pillar playlists created. Cast + scripts written. **Blocked on API quota for: 4 remaining video edits + all playlist seeding + (manual) pinned comments/end screens.** Resume after midnight Pacific.
