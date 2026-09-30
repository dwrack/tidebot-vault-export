# The Rose: Slide Petal Study

_2026-09-30. Element E5 (slide petal), sketched in chat with Davey. Nothing folded into the 3D model yet. The hub folds this into the next model version once approved._

Sketch: `Renders/Slide Petal Study/slide-petal-group-stair-and-exit-2026-09-30.svg`

## v0.35 as modeled (measured from `buildFallenPetal`)

| | |
|---|---|
| Lip (launch) | 3.0 m above deck, 3.5 m above water, 6.25 m from center. Same height as the crown floor |
| Heel | rises 3.0 m over ~1.3 m of run, 62-85 deg. Base 1.2 m wide, ~15 cm off the hot room wall |
| Ride | ~7.7 m lip to water, slope builds from 9 to 37 deg |
| Exit | steepest point (37 deg) is where it meets the water. No runout |
| Width | 5.2 m max; spoon channel 0.85 m deep at the margins |
| Tip | ~12.9 m from center, ~5.4 m past the 7.5 m float edge |
| Support | two steel legs in the model, placeholder only |

## Decisions (Davey, 2026-09-30)

1. **Climb up the back of the petal.** Not from the crown, not from the jump petal.
2. **Groups of 2 to 5 go up at once** and slide together.
3. **3 lanes, tapered.** Keeps the petal's narrow attachment closer to the fallen-petal look. Groups of 5 climb in two waves and launch together.
4. **Curl the exit.** Flatten into a runout, then the tip curls down and under the water.

## The group stair (sketch numbers)

- Ship's-ladder pitch, ~65 deg, ~10 treads over the 3.0 m rise. One-way up: everyone leaves by sliding.
- 3 lanes, ~0.6 m each at the foot. ~1.9 m wide at the base, widening to ~2.7 m at the lip, following the petal's taper.
- 4 rails, each a raised petal vein fanning up the back, ending in a grab curl at the crest. Everyone has a rail for each hand.
- Climbers face out, go over the crest and sit. They land already facing down the slide.
- Needs the petal pushed out ~1.2 m from the hot room to open a ~1 m slot at the foot of the stair. The heel still sits on the float.
- Grippy treads; playground rubber (PIP) on the slot floor, since a slip lands on the deck, not the water.

## The curled exit (sketch numbers)

- Short near-flat lip for launching, then a steep middle drop.
- ~2.3 m runout at ~5 deg, about 0.5 m above the water.
- Tip curls down and under the surface, like a blown rose petal reflexing. No upturned kick (that launches riders).
- Tip lands ~14.5 m from center, ~1.7 m farther than v0.35.

## Open

- [ ] Launch pad for 5: a nearly flat strip ~3.5 m wide at the lip plus a grab bar; lip is 2.7 m today
- [ ] Structure under the longer cantilever (ribs or a stem-like strut instead of two legs)
- [ ] Depth under the new tip at low river (soundings)
- [ ] Insurance: add the group stair to the broker call on jumps, slide and climbing wall
- [ ] Lifeguard at the lip every slide hour; controls each group's launch
- [ ] Hub approval: the 1.2 m push-out changes the petal's envelope against its neighbors

## Idea: an inflatable slide petal (Davey, 2026-09-30)

A custom inflatable petal, designed by us and brought in, instead of (or before) the GFRP shell.

- **Why it fits:** swim season is only July to September. An inflatable comes out for the summer and gets stored for nine months. It could open the slide in year one, before the permanent build, and show insurers and sponsors that people want it.
- **Worries Davey raised:** cleaning, and how easily it breaks.
- **Other risks:** PVC near the fire nooks and stove heat; punctures or vandalism overnight on a public dock; UV wear; whether it can hold a crisp curled petal and a 3 m lip; constant blower vs sealed airtight chambers.
- **Open:** quotes and lifespan from open-water inflatable makers (not researched yet).

## Hand-off to the main model (2026-09-30)

- Davey asked to add this to the main Rose model. The main model was being edited live by other sessions (v0.45/v0.46), so per the Session Plan this went to the hub as a hand-off instead of a direct edit.
- Code: `Iterations/_candidates/slide-petal-group-stair-and-curled-exit.js`, a drop-in replacement for `buildFallenPetal`. Tested in a scratch copy on v0.45: renders, no console errors.
- Blender scene: `Blender/slide_petal_scene.py` (same geometry), renders in `Renders/Slide Petal Study/`.
- Hub to check: gangway S1 and kids' sepal slide G6 clearance after the 1.2 m push-out.
