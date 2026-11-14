# Before You Get In — guest intro video (Nov 2026)

**CURRENT (v3, 2026-11-13):** `Before You Get In - guest intro v3 (2026-11-13).mp4` (1:55, 1080p, silent). Web player with a Parts tab: https://claude.ai/artifact/8UNQzCW78WDitv6VnXQ7CH. v1/v2 (Davey: "horrible design") are in `_old/` as history.

## How it was built
Rebuilt as separate parts, each rendered and checked on its own before scenes used them: set (drawn from Davey's 11/13 photos + Blink stills), plan view, figure rig (scaled to the real 2.4 m cabin), water/steam effects, captions on a calm panel. Canvas engine, deterministic frames. Source in `v3-source/`. Re-render: `python3 build.py film` then `node film.mjs` (needs Chrome + ffmpeg), writes intro.mp4.

## Running order (safety first, door code last)
1. Hook: BEFORE YOU GET IN, "the door code is at the end" (tease)
2. Sauna first
3. Know the gasp (ladder in, breathe slow until it passes)
4. The river always moves (plan view: don't fight it, ride it to a ladder; front, back, pier)
5. Jump out, not down (front of the boat pushes you under; push off hard and away)
6. Off the roof? (you surface halfway down the boat; know the back ladder)
7. No lifeguard. Bring one.
8. Two minutes, tops
9. Throw, don't go in (rings on the stern rail and the pier)
10. Mind the steam
11. Quick ones: no alcohol, walk don't run, feet first, not after dark, dizzy sit down
12. Everyone signs the waiver
13. Then your door code shows up (in the booking, once every waiver is signed); end card

## Facts used (verified in the vault 11/13)
- Door code appears in the booking only after every guest in the party signs the waiver in their own name.
- Unstaffed, no lifeguard.


## v4 proposed (2026-11-13, Davey review, not yet rendered)
Davey: no staff on site, never go in after someone (pole or ring), flotation on anyone entering, in doubt stay out. "Sauna first" is a preference not a safety rule and is cut.

Running order: hook -> IN DOUBT, STAY OUT -> NO ONE IS ON SITE (you are the safety crew) -> FLOTATION ON (vest or swim buoy) -> know the gasp -> river always moves -> jump out not down -> off the roof -> THROW, DON'T GO IN (moved up) -> two minutes (shorter under 50F) -> mind the steam -> quick ones -> waiver -> door code.
End card: "In doubt, stay out. Vest on. Ladder in. Never alone."

Needs from Davey before render: (1) rings only, or hang a rescue pole at the stern ladder; (2) jumps allowed feet-first, or ladder only. Site prep: vests/buoys hung on the pier hook before the video says so.

## Open calls for Davey (v3)
- Jumping: the pasted checklist said "no diving or jumping, ladder only". The video follows Davey's own direction (jumping allowed with the push-off and roof rules) and says "feet first, no diving". Pick one.
- Time limit: video says two minutes (from the pasted checklist). Earlier draft said 1 to 3.
- Left out on purpose (too much for an intro): kids policy (13+ private with guardian, 18+ social), water temperature, algae advisories and wildlife, phones. "Staff can close the river" was dropped because the sauna is unstaffed.
- Rescue pole: location unknown, so the video shows only the throw rings.
- Audio: silent. Add music or voiceover if it plays somewhere with sound.
