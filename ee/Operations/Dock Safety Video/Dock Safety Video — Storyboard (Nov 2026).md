# Before You Get In — guest intro video (Nov 2026)

**CURRENT (v4, 2026-11-13):** `Before You Get In - guest intro v4 (2026-11-13).mp4` (2:11, 1080p, silent). Web player with a Parts tab: https://claude.ai/artifact/8UNQzCW78WDitv6VnXQ7CH. v3 moved to `_old/`; v1/v2 (Davey: "horrible design") are there too.

**v4 changes (Davey review 11/13):** sauna-first cut (a preference, not a safety rule). New scenes up front: In doubt stay out; No one is on site (no staff, no lifeguard); Flotation on (vest or swim buoy on everyone who goes in). Throw scene moved ahead of Two minutes and now names the rescue pole (it hangs horizontal inside the pier rail next to the throw ring; drawn into the set). Jumping stays allowed: feet first, away from the boat, push off hard. End card: In doubt stay out. Vest on. Ladder in. Never alone.

## How it was built
Rebuilt as separate parts, each rendered and checked on its own before scenes used them: set (drawn from Davey's 11/13 photos + Blink stills), plan view, figure rig (scaled to the real 2.4 m cabin), water/steam effects, captions on a calm panel. Canvas engine, deterministic frames. Source in `v3-source/`. Re-render: `python3 build.py film` then `node film.mjs` (needs Chrome + ffmpeg), writes intro.mp4.

## Running order v4 (safety first, door code last)
1. Hook: BEFORE YOU GET IN, "the door code is at the end" (tease)
2. In doubt, stay out
3. No one is on site
4. Flotation on
5. Know the gasp
6. The river always moves (plan view)
7. Jump out, not down (feet first, away from the boat, push off hard)
8. Off the roof?
9. One in, one watching
10. Throw, don't go in (ring + rescue pole inside the pier rail, ring on the stern)
11. Two minutes, tops (shorter when the water is cold)
12. Mind the steam
13. Quick ones: no alcohol, walk don't run, feet first away, not after dark, dizzy sit down
14. Everyone signs the waiver
15. Door code; end card

## Facts used (verified in the vault 11/13)
- Door code appears in the booking only after every guest in the party signs the waiver in their own name.
- Unstaffed, no lifeguard.


## Settled 11/13
- Jumping allowed, feet first and away from the boat.
- Rescue pole exists: horizontal inside the pier railing, next to the throw ring.

## Open calls (history, v3)
- Jumping: the pasted checklist said "no diving or jumping, ladder only". The video follows Davey's own direction (jumping allowed with the push-off and roof rules) and says "feet first, no diving". Pick one.
- Time limit: video says two minutes (from the pasted checklist). Earlier draft said 1 to 3.
- Left out on purpose (too much for an intro): kids policy (13+ private with guardian, 18+ social), water temperature, algae advisories and wildlife, phones. "Staff can close the river" was dropped because the sauna is unstaffed.
- Rescue pole: location unknown, so the video shows only the throw rings.
- Audio: silent. Add music or voiceover if it plays somewhere with sound.
