# Before You Get In — guest intro video (Nov 2026)

**CURRENT (v5, 2026-11-13):** `Before You Get In - guest intro v5 (2026-11-13).mp4` (2:30, 1080p, silent). v4 moved to `_old/`. Web player with a Parts tab: https://claude.ai/artifact/8UNQzCW78WDitv6VnXQ7CH. v3 moved to `_old/`; v1/v2 (Davey: "horrible design") are there too.

**v5 changes (Davey 11/13, late):** both boat ladders hang off the bow and stern ENDS, not the port side. Outboard removed (being sold). "One in, one watching" now reads DON'T RIVER PLUNGE ALONE, followed by a new scene: no partner, skip the river, use the Downpour or the shower under the stairs (both cold fresh water). Life ring + rescue pole drawn on the bow rail. New close-up scene: rescue pole, untwist, pull it long, twist to lock; reach from the deck, never jump in. Throw scene caption: rings at the front of the boat and on the pier (stern ring removed).

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
9. Don't river plunge alone
9b. No partner? Skip the river: the Downpour or the shower under the stairs
10. Throw, don't go in (rings at the bow and on the pier)
10b. The rescue pole: untwist, pull it long, twist to lock
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
- (Davey 11/13 late) Life ring + rescue pole on the fore of the boat. Pole extends by untwist, extend, twist to lock. Ladders are on the fore and aft ends. Outboard is being sold, not drawn.
- ASSUMED, not checked: where the Downpour sits on the boat deck (drawn on the bow deck).

## Open calls (history, v3)
- DECIDED 2026-11-13 (Davey): jumping stays allowed with the rules in the video (feet first, push off hard at the front, know the back ladder before a roof jump). No diving. The pasted "ladder only" line is rejected.
- Time limit: video says two minutes (from the pasted checklist). Earlier draft said 1 to 3.
- Left out on purpose (too much for an intro): kids policy (13+ private with guardian, 18+ social), water temperature, algae advisories and wildlife, phones. "Staff can close the river" was dropped because the sauna is unstaffed.
- Rescue pole: location unknown, so the video shows only the throw rings.
- Audio: silent. Add music or voiceover if it plays somewhere with sound.
