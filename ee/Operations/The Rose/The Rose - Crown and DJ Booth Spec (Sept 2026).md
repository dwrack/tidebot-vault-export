# The Rose: Crown and DJ Booth Spec

2026-09-28 · detail pass on the top of the Rose (the crown lounge) and the nested DJ booth. Built from model v0.29. Numbers marked *est.* are before any engineer, code official or vendor has seen them.

Related: [[The Rose - Design Brief (Sept 2026)]] (decisions 33, 48, 52, 59, 60, 65, 69), [[The Rose - Materials Plan (Sept 2026)]], `Iterations/CHANGELOG.md`.

---

## 0. The short version

- **The crown is small.** Full Rose: 6.6 m across, about 34 m² (~370 sq ft). Rose 1.0 at 62% scale: 4.1 m across, about 13 m² (~140 sq ft). A booth, a fire, benches and a dance floor all fit on the full Rose only if the fire moves off-center. On Rose 1.0 they don't all fit, full stop.
- **My layout for the full Rose:** booth nested in the south rim (as now), a **hearth arc** (one curved gas fire) on the north side, a warm bench ring around the rest of the parapet, and the middle left open as the dance floor. The DJ looks north across the dancers, over the fire, to the Hawthorne.
- **Two things in the current model don't survive code and need a call from you:** the jump petal can't be the only way off the roof (section 6), and the parapet needs to rise where people sit (section 3).
- **Sound plan:** lots of small speakers close to people, aimed down and in, plus transducers in the floor and benches so the kick is felt, not broadcast across the river. Target about 95 dBA on the floor, and a hard limiter the DJ can't touch.

---

## 1. What's there now (model v0.29)

| Item | Current model |
|---|---|
| Crown deck | Flat disc, radius 3.3 m, 0.85 m above the hot-room roof plate (about 3.5 m above the water) |
| Plenum under the deck | 0.85 m void between hot-room roof and crown deck |
| Parapet | 10 upright bud petals, ~1.0 to 1.2 m tall, the crown's rail |
| Crown style | Three options still open: flat deck, sunken fire circle, terraced bowl (Master Plan decision) |
| DJ | "Nested": half-round booth sunk 0.6 m into the south rim, DJ faces north, petal canopy overhead (v0.21, v0.23) |
| Access | Jump petal spirals inward onto the crown rim, **the only way up** (v0.26) |
| Flue | Removed in v0.25. The stove vents through a stack on the north wall |
| Sound drawn | 4 parapet speakers aimed inward, 2 subs under the crown deck firing down |
| Poofers | Ring on the parapet tips added v0.22, removed in v0.25 along with the climbing-wall nozzles |

Two knock-on effects of v0.25 nobody has caught yet:
- The booth's cable route was "up the flue chase." The flue is gone, so the chase is gone. The booth needs its own chase (section 7).
- The "fire circle around the flue" option has nothing at its center anymore. That frees the center for dancing.

---

## 2. Layout (full Rose)

```
                        N  (cove, jump petal, Hawthorne)
              .-~~~~~~~~ parapet petals ~~~~~~~~-.
           .'  bench     ~~ HEARTH ARC ~~   bench  '.
         .'             (gas, 1.8-2.2 m)             '.
        /  bench        0.9 m clear zone      bench    \
       |                                                |
   W   |  jump           DANCE FLOOR          bench     |   E
 river | landing           ~14-16 m2                    |  shore
       |  (keep clear)                                  |
        \  bench                              bench    /
         '.        [ DJ BOOTH, sunk 0.6 m ]          .'
           '.      [ service stair ]  canopy       .'
              '-.______________________________.-'
                        S  (Marquam, Tilikum)
```
Jump landing position is approximate; confirm in the model. Keep it at least 1.5 m from the booth's end.

**Floor budget, full Rose (est.):**

| Zone | Area | Notes |
|---|---|---|
| DJ booth + service stair head | ~5 m² | One element under the canopy |
| Jump landing pad | ~1.5 m² | Keep-clear, no bench |
| Bench ring (~240° of the parapet, 0.45 m deep) | ~6 m² | ~13 m of bench |
| Hearth arc + clear zone | ~4 m² | Burner plus 0.9 m to anything soft |
| **Dance floor** | **~14-16 m²** | Disc about 4.3 m across |
| Circulation slop | rest | |

**People (est.):** ~20 seated on the ring, 15-20 dancing comfortably (about 0.75 m² each), 25-30 packed. Plan an operating cap of **40 on the crown** plus the DJ and a host. The naval architect confirms that against freeboard; crowd on the crown is dead center, so heel is not the issue, raised center of gravity is.

**The shot:** from the shore and the Hawthorne you see dancers silhouetted between a fire and a glowing red booth. From the booth, the DJ sees faces, then flame, then the Hawthorne lift towers. From the dance floor, the crowd looks south at the DJ with the Marquam and the Tilikum's lights behind. (The Tilikum's lights shift color with the river's conditions, which is a nice free backdrop.)

---

## 3. Seating

**Bench ring on the parapet**
- Seat 45 cm high, 42-45 cm deep, 5-8° back tilt. The parapet petals are the backrest, leaning out ~12°.
- Surface: thermally modified hardwood slats (or the same PIP rubber as the floor if you want one material), finished rose. Slats drain; wet bodies sit here all night.
- **Warm benches.** A hydronic loop under the seat, fed from the sauna plant's waste heat, holding ~30-35°C. Coming off a cold plunge onto a warm bench in the open air is the thing people will talk about. Same idea as the heated amphitheater steps in brief section 17.
- Towel hooks on the parapet backs, **none within 1.5 m of the hearth**.
- Drink ledge: a 12 cm lip on the parapet top between petals. No glass on the crown.

**The guard problem.** Code measures guard height from anything you can stand on, and a bench counts. So wherever there's a bench, the parapet must reach **1.07 m (42 in) above the seat**, about 1.5 m above the deck. Right now the petals are ~1.0-1.2 m above the deck. Options: taller parapet petals behind the benches (reads more like a closing rose anyway), or a glass top-up between petals. Where there's no bench (landing, booth), 1.07 m over the deck is fine. On a roof this high over a deck, with people dancing after a sauna, a guard is non-negotiable even with the no-guard stance on the jump edges.

**Views while seated.** Seated eye height behind a 1.5 m parapet sees sky and the bridge tops, not the water. That's fine: the bench faces in, toward the fire and the floor. The water view is the standing view.

---

## 4. Dance floor

**Size:** ~4.3 m disc in the middle, ~14-16 m². It's a "last hour of the night" floor, not a club. Big enough for 20 people who know each other.

**Surface.** The Materials Plan puts PIP playground rubber on the roof lounge. Good for lounging, **bad for dancing**: barefoot pivots on high-grip rubber burn skin and torque knees. Put a different disc in the middle:
- Synthetic teak (boat-deck material) or sanded marine-grade hardwood, 1-2% slope to the drains.
- Test both wet and barefoot before choosing: one pivot, one slide, one jump on a wet sample. Five minutes, cheap.
- A thin inlay line where the rubber meets the dance disc so people's feet know the change.

**Structure.**
- Design the crown for **100 psf assembly load** (already in the brief) and **rhythmic activity**. A crowd bouncing in time is a different load from a crowd standing. The Engineer of Record checks floor stiffness to rhythmic-activity guidance (AISC Design Guide 11); a normal roof span of ~6.6 m in CLT may be too lively and need a mid-support ring.
- The float: heave period on a float this size is roughly 1.5-2 s, far from a ~2 Hz beat, so bounce resonance is unlikely. One-line check for the naval architect, not a worry.

**Keeping the dance out of the sauna.** The hot room is directly under the dance floor. Build the crown deck as a **floating floor**: its own frame on rubber isolation pads over the insulated roof, with a 100-150 mm air gap. That's already noted in the acoustics plan for footsteps. Dancing makes it mandatory. Even then, program it: DJ sets run during a "party round" or after the last quiet session, and the set can be piped softly into the hot room's bench transducers so the sauna becomes the chill room.

---

## 5. Fire: the hearth arc

**Recommendation:** one curved gas fire on the north side, not in the center.

Why not the center: a center fire pit kills the dance floor, and a ring of barefoot, towel-wrapped, sauna-flushed dancers circling an open flame is the one scene the fire marshal will picture first.

**Spec (est.)**
- Curved linear burner, 1.8-2.2 m long, following the parapet arc at ~r 2.2 m. Burner at 55-65 cm, set in a low stone or blackened-steel trough.
- Built as the crown's **fire rose**: steel petals lean over the flame toward the floor as reflectors, same family as the five amphitheater fire roses (brief section 17). One more commission slot.
- ~100-150k BTU/hr natural gas, off the same service as the stove.
- **Listed appliance** (CSA/ANSI Z21.97, outdoor decorative gas), electronic ignition with flame sensing, auto shutoff on flame-out.
- Non-combustible base with an air gap above the CLT roof. Manufacturer and Portland Fire set the final clearances.
- Glass wind lip on the outboard (north) side and ends. Summer wind is NNW, so it blows the heat across the floor toward the crowd. With the lip, that's a pleasant warm breeze, not a flame lean.
- Anemometer interlock: fire off above a set gust speed (~20 mph, tune after a season of dock wind data).
- Lava rock or fire glass rated for rain, with a drained burner pan and a lid for winter. Wet media pops.
- Clear zone 0.9 m minimum to the bench and floor edge; nothing hanging within 1.5 m.
- Controls: on/off and flame height at the show desk, a manual gas shutoff reachable from the crown, an E-stop at the booth and one at the jump landing.

**Crown poofers.** They went out in v0.25 as collateral when you said to remove the climbing-wall triangles. If you want them back on the parapet tips: they're "flame effects before an audience" (NFPA 160), so they need a permit per event from Portland Fire, a qualified operator (not the guest DJ), a key switch plus a dead-man button, and set clearances from the crowd. Doable, but a different class of problem from a listed fire pit.

---

## 6. Getting up and down (the part that needs a decision)

The jump petal as the **only** route onto the crown works as art and fails in three practical ways:

1. **Code.** Occupant load is computed from area, not from a posted cap. The crown's floor and bench area works out to roughly 60-70 people by the code's factors (5 sq ft per standing person, 18 in of bench per seated person). Over 49 means two separate ways off. Brief decision 1 already assumes A-3 assembly.
2. **Rescue.** Sauna heat, dancing, and possibly alcohol is the classic recipe for a faint. You can't carry a stretcher down a spiral jump ramp.
3. **Night.** At the end of a set, the only way down would pass an unguarded jump edge in the dark.

**Recommendation:**
- Keep the jump petal as the ceremonial way up, by day.
- Add a **service stair behind the booth**, rising through the south service ring and arriving under the canopy. Minimum 44 in wide (the code width once you're over 50 people), enclosed in the same rose skin so it reads as part of the booth petal.
- It doubles as the DJ's load-in (nobody carries CDJs up a jump ramp) and the fire and sound techs' route.
- During night sets, **gate the jump petal at the crown landing**. Everyone comes and goes by the stair.

---

## 7. DJ booth

**Placement:** keep "nested" as is. South rim, sunk 0.6 m, DJ faces north. The DJ's head sits at the crowd's shoulder height, which answers your "not worshipped" note.

**Working surface**
- Desk 2.0-2.2 m wide, 0.75 m deep, 1.0-1.05 m above the booth floor. That fits a house setup of 4 players plus a mixer (~1.8 m) with room for a laptop.
- Because the booth floor is 0.6 m below the crowd, the desk sits only ~0.4 m above the dance floor. Add a **front ledge 20 cm higher than the desk and 30 cm deep** so spilled drinks and leaning elbows stop before the gear.
- Anti-fatigue mat, a lean bar at the back, a small hidden shelf for the DJ's water and bag.
- **House rig so guest DJs only bring a USB stick.** Standard 4 players plus mixer, two booth monitors aimed at the DJ only, one handheld mic for the host.
- **Vinyl:** on a float with 20 people bouncing 3 m away, turntables will skip. If you want vinyl nights, the decks need a suspended or isolated shelf. Otherwise, a house rule: digital only.

**Show desk (separate from the DJ)**
- A keyed side panel at the booth's east end, for the staff show operator, not the guest DJ.
- Runs: lights (DMX over the network), hazer, every fire (the crown hearth, five amphitheater fire roses, any poofers), sauna cues (vortex-ring cannon, Aufguss cues), and audio zone levels.
- One touch screen with presets: *Sunset*, *Hearth*, *Set*, *Last Song*, *Close*. A guest DJ sees audio only.
- E-stop kills all fire and flame effects, mutes nothing (you want the host's mic to work in an emergency).

**Weather**
- The v0.23 petal canopy covers the DJ. Its back faces south, which is good: SSW storm fronts hit the closed side.
- Add a **bud hood**: a hinged petal lid that closes and locks over the desk when the booth is dark, rated for driving rain. The booth literally closes like a bud.
- Gear lives in a dehumidified locker under the desk when not in use. Don't leave players out in Portland from October to June.
- Plus a roll-down clear front curtain for rainy-night sets.

**Heat and humidity.** The booth sits in the plenum right above a sauna, under rose-red surfaces that soak up summer sun. Electronics want under ~35°C and dry. Give the booth pit a quiet vent fan with a temperature sensor, and seal it from the hot-room vapor barrier.

**Power and cabling**
- New chase: from the south service ring, up alongside the service stair into the booth pit (replaces the dead flue chase). Carries power, audio network (Dante), DMX, fire control lines, hazer fluid.
- Dedicated audio circuits with clean power and a small UPS so a trip doesn't kill the set mid-song.
- It's a floating building, so NEC 553 (floating buildings) and 555 (marinas) apply, including ground-fault protection that pro audio can nuisance-trip. The electrical engineer designs for it; flag it early.
- Lightning: the crown and jump petal are the highest points on the water. Lightning protection (NFPA 780) goes in the structural scope.

---

## 8. Sound on the crown

**Philosophy (same as the hot room):** close, many, and felt. Sound carries over water a long way, downtown sits across 300 m of it, and RiverPlace and South Waterfront condos are close by. The I-5 decks behind the dock give a constant noise floor on the east side that masks a lot; the west side is where complaints would come from.

**Levels (targets, est.)**
- Dance floor center during sets: ~95 dBA average. Clubs run 100-105; 95 on a small floor with tactile bass feels plenty.
- Sunset / hearth: 75-80 dBA.
- A hard limiter per zone, locked by staff, and a logging sound meter at the rim plus one at the dock's end so there's a record if anyone complains.
- **Portland noise code** (Title 18) sets limits at the receiving property line, and they're low at night for residential neighbors, roughly 50-55 dBA *(verify with the Noise Control Office)*. Amplified outdoor sets will likely need a noise variance. This is a pre-app conversation, not a design detail.

**Speakers**
- **6 compact weatherproof point-source speakers** built into parapet petals (up from the 4 drawn), aimed inward and down at 30-40° with short 3-4 m throws. Level falls off fast past the rail.
- **2 subs in the booth base** firing north across the floor, set up as a cardioid pair so bass cancels behind the booth (south and southwest, toward downtown and the condos). This replaces the two drawn under the crown deck, which would have pumped bass straight into the sauna ceiling.
- **Tactile transducers under the dance disc panels (8-12) and the bench ring (6-8)**, above the isolation pads. You feel the kick through your feet, so the subs can run lower. This is the crown's version of the hot room's seat transducers.
- Outdoor-rated (IP55 or better), stainless hardware, nothing near the stove vent stack on the north wall.
- One DSP handles zones: crown, hot room, amphitheaters, jump, kids' slide. The show desk can send the set to the hot room at low level or cut it.

**Cost (rough, before quotes):** a pro-grade crown system (speakers, subs, amps, DSP, transducers, monitors, mic) is ~$40-80K installed, depending on brand tier. Only part of that is inside the brief's sensory line.

---

## 9. Light and effects

- **Low and warm.** Step lights at the landing and stair, a glow line under the bench ring, the fire, and the petal glow (v0.24). No overhead lights.
- A few small IP65 color fixtures in the parapet washing up into the booth canopy and across the dancers.
- **No flashing red or green** visible from the channel: those are navigation signals. A steady rose glow is probably fine. Confirm with the Coast Guard (Sector Columbia River) during permitting.
- **No lasers.** Outdoor laser shows need an FDA variance and aviation notice, and aiming near bridges and boats is asking for trouble.
- Haze: one small low-output hazer for light beams on still nights. It blows away on most nights anyway.
- Brand-fit effect worth testing: a **cold air burst** from the parapet at the drop, like the vortex ring in the hot room. Cold air on hot skin, not CO2 fog.

---

## 10. Safety and running it

- A crown host at every set: fire, headcount, water, the gate at the jump landing.
- Water station on the crown, and an AED at the booth.
- Adults only on the crown after dark.
- Operating cap 40, counted at the stair.
- If there's any alcohol program, it lives downstairs, and no glass comes up.
- The show operator (not the guest DJ) runs fire. If poofers come back, that person is the qualified flame-effect operator.

---

## 11. Weight on the crown (est., for the naval architect)

| Load | kg |
|---|---|
| 40 people at 80 kg | 3,200 |
| Booth structure, canopy, gear, subs | 500-700 |
| Hearth (steel fire rose, burner, media) | 300-600 (stone would double it) |
| Benches, parapet top-ups, speakers | 400-600 |
| **Total** | **~4.4-5.1 t, about 3.5 m above the water** |

Centered, so it doesn't heel the float, but it raises the center of gravity. Steel over stone for the hearth for this reason.

---

## 12. Rose 1.0 (the ~30 ft version)

At 62% scale the crown is ~4.1 m across and ~13 m². After the booth, stair head and landing, about 7-8 m² is left.

**Recommendation:** Rose 1.0's crown is a **listening lounge**, not a dance floor. Booth, a small tabletop fire rose (not a hearth arc), 10-12 on a bench ring, about 15 people total. Dancing happens on the float deck and amphitheater petals, with the crown DJ playing down to them. The full Rose is where the roof becomes a dance floor.

---

## 13. Decisions for Davey

1. **Fire placement:** hearth arc on the north side (my pick), or a center fire pit with a flush lid that turns into the dance floor on no-fire nights?
2. **Second way off the roof:** service stair behind the booth, with the jump petal gated during night sets (my pick). Without it, the crown likely can't hold more than ~49 people or get permitted as an assembly roof.
3. **Parapet height behind benches:** taller petals (~1.5 m) or glass top-ups between petals?
4. **Crown poofers:** bring them back (permit per event, qualified operator) or leave fire to the hearth and the amphitheaters?
5. **Sound ceiling:** ~95 dBA with tactile floor (my pick), or keep it quieter (~88) and lean harder on the transducers?
6. **Vinyl:** build an isolated turntable shelf, or digital-only house rule?
7. **Rose 1.0 crown:** listening lounge, no dance floor (my pick)?
8. **Model it:** want this layout drawn as v0.30 (hearth arc, bench ring, dance disc, service stair, bud hood, updated speaker positions)?

---

## 14. What if the jump petal is a ramp? (2026-09-28)

Davey's question: make the jump petal a ramp up to the crown. Measurements from model v0.29. All heights above water; the float deck is 0.51 m above water and rides the river, so these heights hold at any river stage.

**Fixed heights today**

| Point | Above float deck | Above water |
|---|---|---|
| Hot-room wall top | 2.15 m | 2.66 m |
| Crown deck | 3.15 m | **3.66 m (12 ft)** |
| Jump petal peak | ~5.0 m | **~5.5 m (18 ft)** |
| Today's jump petal walk to the crown | ~14 m of path, stair-steep | |

**Ramp rules that set the length (IBC 1012)**
- Exit ramp: 1:12 max. Non-exit pedestrian ramp: 1:8 max.
- Max 0.76 m (30 in) of rise per run, then a 1.52 m (60 in) landing. Landings top and bottom.
- Guards both sides where the drop is over 0.76 m, handrails both sides, 36 in minimum clear width (44 in once the crown counts over 50 people).

**The three ways to do it**

| | Crown height (water) | Ramp length | Laps of the full Rose (47 m) | Notes |
|---|---|---|---|---|
| A. 1:12 exit ramp, crown as is | 3.66 m | ~47 m (5 runs, 4 landings) | **1 full lap** | Also makes the crown wheelchair accessible |
| B. 1:12, crown lowered 0.5 m (thin plenum) | 3.16 m (10.4 ft) | ~39 m | ~0.85 lap | Booth can't sink 0.6 m anymore without cutting into the hot-room ceiling. Saves 8 m, costs the nested booth |
| C. 1:8 ramp, not an exit | 3.66 m | ~34 m | ~0.75 lap | Still needs the service stair as the exit |

**The jump on a ramp petal**
- An exit ramp needs guards the whole way. The jump happens from a gated gap in the guard, not an open edge.
- Two jumps: a **ramp-top launch at crown level, 3.66 m (12 ft)**, and a short stair (not ramp) up the petal tip to **~5.5 m (18 ft)** for the big jump. The tip stays sculpture-steep because it isn't part of the route.
- Depth under each (rule of thumb, verify with soundings and an aquatic safety consultant): diving-platform standards want ~3.8 m under a 5 m platform. Plan 3.5 m+ under the 12 ft launch and 4 m+ under the 18 ft tip, at the lowest river stage.

**Rose 1.0.** Ramp length does not shrink with the flower: the hot room needs the same head height, so the crown rise stays ~3.15 m. On Rose 1.0 (29 m lap) a 1:12 ramp is 1.6 laps and a 1:8 ramp is 1.2 laps. Rose 1.0 gets stairs, or a crown you reach from the dock.

**Recommendation.** Option A, built as the Spiral petal character (v0.28): the amphitheater rims already curl into each other as a walkway. Grade that walkway at 1:12 and it becomes one continuous ramp that climbs once around the whole flower, over the jump petal and onto the crown. The rose becomes a literal inward spiral, the roof becomes accessible, and the rolled petal edges are the guards. Keep the service stair as the second exit (still required over 49 people). Cost: ~47 m x ~1.4 m of ramp (~66 m2, about twice the crown's area) inside the float edge; the naval architect weighs it.
