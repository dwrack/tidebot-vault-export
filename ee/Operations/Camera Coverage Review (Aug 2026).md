# Camera Coverage Review — Aug 2026

Live frames pulled from every Blink camera on 2026-08-13. Snapshots saved to `~/blink-snapshots/`.
Of the 14 cameras on the account, **4 are Ebb & Ember**. The rest are NOLA (3 floodlights/lot cams) and Door County (Boat, plus the house/garage/workshop/parking group).

## What we actually have

| Camera | Covers | Verdict |
|---|---|---|
| **Wired Floodlight 23BJ** | High overhead of the lounge deck: chairs, side benches, planters, string lights, dock edge and water line | **Best camera we have.** Don't touch it |
| **Lounge** | Eye-level down the covered walkway: gear/hook wall, fire extinguisher, walkway, out toward the finger dock | Good image, but it **duplicates 23BJ** across most of the lounge deck. Re-aim candidate |
| **Ebb boat** | The sauna itself, entrance door, ring buoy, "NO LIFEGUARD ON DUTY" sign, water on both sides | **Worst framed, most important view.** See below |
| **Stove** | Inside the stove cavity, on the burner flame | Fine. Ops/diagnostic, not security. Leave it |

## The one real problem

The **Ebb boat** camera is the only thing watching the sauna entrance and the water people get into, and it is badly obstructed:

1. **Two pilings run straight down the middle of frame.** They split the shot in three and partly hide the sauna doorway.
2. **A kayak is parked in the lower-right corner**, eating roughly a fifth of the frame including part of the dock edge.

That's the camera you'd actually want footage from if someone got hurt in the water. Fix in this order: move the kayak (free, today), then shift the camera far enough off the pilings to get a clean line on the door and the water entry.

## Gaps

1. **No coverage of the ramp / gangway approach from shore.** Nothing sees who arrives. That's the access-control gap, and it's where someone walks in without a waiver.
2. **No coverage of the cold-plunge pool** planned for V2. That's the drowning-risk zone, and the "no lifeguard on duty" sign is already right there.
3. **Wasted overlap** between Lounge and 23BJ on the same deck.

## Recommendation

| Move | Why |
|---|---|
| Re-aim **Lounge** toward the ramp/entry approach | Kills the overlap with 23BJ and closes the biggest gap for free |
| Reposition **Ebb boat** off the pilings + move the kayak | Restores the only view that matters in an incident |
| Leave **23BJ** and **Stove** alone | Both are doing their job |
| Add **one new camera on the cold-plunge pool** when the V2 saunas are set | New risk surface, no coverage |

That's one purchase, two re-aims, and moving a kayak.

## Note on privacy

All four are outdoor. Nothing points into the sauna interior, the bathroom, or the storage closet that's becoming the third changing room. Keep it that way when the closet gets converted.

Re-run the snapshots any time with:
`cd ~/.config/blink-ee && BLINK_OUT="$HOME/blink-snapshots" ./venv/bin/python snapshots.py`
