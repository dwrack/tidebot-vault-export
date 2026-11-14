# Dock Safety Video — Storyboard (2026-11-13)

**v2 (same day):** redrawn to the real layout after Davey's photos + Blink stills (Ebb boat, Lounge, 23BJ cams). Source: `dock-safety-storyboard-v2.html`. v1 kept for reference.

Animated stick-figure safety explainer, same idea as the Ben's Bites "morning in my life" cutaway GIF but cleaner: one wide line-art cutaway of the sauna float, dock, ladders and river, camera pans scene to scene.

- Live artifact: https://claude.ai/artifact/8UNQzCW78WDitv6VnXQ7CH
- Source: `dock-safety-storyboard-v1.html` (this folder). Opens in any browser; space pauses, arrow keys step scenes.
- Status: DRAFT v2, MP4 rendered 11/13 (`Dock Safety — stick figure video v2 (2026-11-13).mp4`, 2:01, 1080p, silent). Waiting on Davey's scene cuts. Not shown to guests or team yet.
- Re-render: open `render-mp4.mjs` next to a `preview.html` wrapper of the storyboard (see scratch notes in the script), `node render-mp4.mjs`, then ffmpeg the webm to mp4. Headless Chrome records the page in real time at 1920x1080 via `#render` mode.

## Layout facts (from Davey 11/13 + photos + cams)
- Side view from the river, upstream LEFT. Boat moored alongside the pier, bow upstream, Mercury outboard on the stern. Lounge deck is on the pier beside the door.
- Three ladders: front of the boat (upstream corner, water side), back of the boat next to the motor, and the pier just downstream of the boat (the V2 finger dock).
- Front ladder is the worry: the current runs into the boat there and pushes a weak jumper back under the hull. Rule: push off hard, out and away.
- Jumping from the rooftop deck: people surface about halfway down the boat, already drifting. Rule: know the back ladder and pier ladder before climbing up.
- Rings: one on the stern rail, one at the pier corner by the door. Pole location still a guess (drawn on the pier).

## Scenes (14)
1. Title
2. Watch your step
3. The river moves (into the front, out past the back)
4. Front of the boat: push off hard, away from the hull (weak hop = under the hull)
5. Off the roof: you surface halfway down the boat; two exits downstream
6. Three ladders: front, back, pier
7. Cold shock (ladder first time, breathe out, 10 s)
8. Use a partner
9. Rescue pole
10. Throw ring
11. Don't stay in too long (1 to 3 min)
12. Steam burns
13. No alcohol, none at all; no diving
14. End checklist

## Open questions
- Where the rescue pole actually lives
- Is 1 to 3 minutes the number we want to say?
- Output: web page, or render to MP4/GIF for the waiver page, IG, and a dock sign QR

## Next
After scene cuts: re-render, add voiceover or burned-in captions if wanted, add to Style Menu as a new style. Known nit: in scene 5 the caption box sits over the hull (low camera); move the caption or raise the camera in v3.
