# The Rose: Design Brief v0.1

_Started 2026-09-26 from Davey's directive. Working draft. Confidential: this touches Holman Dock, which is off the record until the full team approves strategy (see [[Holman Dock — Pilot Program Plan (Aug 2026)]]). No outbound on any of this._

Companion files in this folder:
- `3D Print Model/make_rose_stl.py` plus 5 STL files (1:60 desktop print, roof lifts off)
- Interactive 3D model: https://claude.ai/artifact/VPwztPdkTQfPb23vPh2yzz
- Raw research notes: `Research/` (structure, heat, sensory, business)

---

## 1. The idea in one paragraph

Portland is the Rose City. The Rose is a round communal sauna shaped like an opening rose, floating on the Willamette with the Hawthorne Bridge behind it. Five petals ring a sunken center. Inside, 40 to 48 people sit on three tiers of stadium benches that step down into a pit around one big stone heater, so the fire sits in the middle of the crowd like a campfire. Each petal's roof is a flat, railed terrace where 8 to 10 people sit outside between rounds. Sound is felt through the benches instead of blasted through speakers, scent arrives in cool vortex rings, and light comes from low sources that throw the petal ribs across the ceiling like a sundial. Curtains drop from the ceiling to shrink the room when it's quiet. Next to it, a small dark Thorn sauna for 6 to 8, and a green Stem waterslide that spirals off a petal terrace into the river and lands swimmers on a leaf-shaped float. It's a sauna, a stage, and a sculpture, and it should sell out weddings.

## 2. What changed after research (read this first)

These are the findings that change the plan. Everything else in this doc is detail.

1. **Holman Dock sits just south of the Hawthorne Bridge, not next to OMSI.** The backdrop is the Hawthorne (1910, the oldest operating vertical-lift bridge in the US), not Tilikum. That's a better story anyway. Tilikum is ~0.9 mi south with the Marquam in between. Check sightlines on site before any rendering promises a bridge.
2. **Holman itself is a small-craft dock, not a sauna berth.** Ordinance 191700 (May 2024) moved it to PP&R for non-motorized boats, on a DSL license that runs to 2034. A 150,000 lb assembly building won't hang off it. Plan the Rose on **its own piles and its own DSL lease, next to Holman**, using Holman for access. This fits Phase 2/3 of the pilot plan, not Phase 1.
3. **Nobody can stamp a 3D-printed plastic structure for 50 people in a hot room.** There's no code path, and printable plastics soften at or below sauna air temperature (PLA ~55C, PETG ~75C, ASA ~95C; the ceiling runs 90-100C). **Print the model, the molds, and the outside skin. Build the structure and hot room in timber.** Still a genuine first: no full-scale printed sauna exists anywhere that we found.
4. **Heat source is a real fork.** Portland Parks commercial rules exclude fuel-based equipment. Our fleet runs on gas. The Rose at Holman probably has to be **electric (EOS)**, which means a big shore-power service. See section 6.
5. **Stability is fine if we don't cantilever.** A wide circle is very stable. Crowd on one side heels it ~2.4 degrees on a heavy float; Portland's limit is 4. What binds is edge freeboard, so the petals stay inside the float edge and roof occupancy is capped per petal.
6. **"Sphere" audio is the wrong tool.** Beamforming arrays (Holoplot, the Las Vegas Sphere system) bounce around a small round wooden room and nothing is heat rated. What makes sound feel like it's reaching your seat is a ring of zones plus **transducers in the benches**. That's cheaper and more personal.
7. **Round rooms focus sound** (whispering gallery, hot spot in the middle). The petal plan is the fix, but only if petal walls are **faceted or convex**, never smooth arcs.
8. **Never glycol fog, never neat oil on stones.** Eucalyptus oil flashes at 39-54C, below room temperature. Scent rides on water, diluted, and the cannons fire cool air from outside the wall.

## Decisions (Davey, 2026-09-26)

| # | Item | Decision |
|---|---|---|
| 1 | Occupancy | **Full bloom.** ~57 inside + ~40 on the terraces, about 95-100 total. Designed as A-3 assembly from the start |
| 2 | Heat | **EOS natural gas, custom.** EOS sells gas heaters through its KUSATEK line, built as standard or bespoke units. See section 6 |
| 3 | Certification | **Certify the room with the stove in it, not the stove itself.** The engineer and inspector sign off the space: clearances, combustion air, flue, gas piping, ventilation, fire separation |
| 4 | Petals | **Petals fan out and run from the deck up past the terraces.** The petals are the walls and the terrace guards. Done in model v0.2 |
| 5 | Doors | **3 doors**, in the clefts where petals overlap, none beside the bridge petal |
| 6 | Stones | **Stones curve outward like pistils.** A cage of 12 steel stamens fanning up and out from the altar, stones clustered along them and knotted at the tips. The flue is the center of the flower |
| 7 | Leaves | **Three swim-out leaves off the Stem**, alternating sides, each tied to the slide by a short petiole walkway |
| 8 | This week | Sensory test in the current sauna (spec in section 15) + model revision 2 (done) |
| 9 | Name | Keep brainstorming (section 16) |

## Decisions, round 3 (Davey, 2026-09-26, v0.8 to v0.9)

| # | Item | Decision |
|---|---|---|
| 22 | Movement | **Dropped.** Petals are fixed |
| 23 | Guards | **No guards on jump edges.** Glass rail only on the dock-side lounge petals where jumping isn't allowed. Davey's framing: a water structure in a grey area of the code. Carry-forward: insurer sign-off, depth markings at every jump edge, lifeguards |
| 24 | Water entry | **Stepped entry petals** under each slide petal, deck level to below the water |
| 25 | Petals | **Amphitheater petals:** the inside of each non-slide petal is stadium seating arching up from a fire pit at the bottom. Saddle rim gives jump heights ~1 to 2.9 m into the cove |
| 26 | Doors | **Offset screen petals** hide the dock-side doors |
| 27 | Lounges | Dock-side petals = chill lounges facing the bridge. Furniture still open (the bug-chair try was a miss; if we revisit, commission a real furniture artist) |
| 28 | Rejected | Outside spiral stadium ramp; bug chairs; bloom/bud movement |
| 30 | Layout | **Jump petal centered between the two slide petals**, facing the cove; north slide petal keeps a glass base for the bridge view (v0.10) |
| 31 | Leaves | **Bigger leaf floats** (about 2x), for lounging on the water (v0.10) |
| 32 | Petal character | **Unfurling** is the favorite so far (v0.11 default) |
| 33 | Roof | **Crown lounge on top of the sauna**, three options in the model: flat deck, sunken fire circle, terraced bowl. The flue rises through the center inside glass |
| 34 | Jump petal | **Deck level on the left to 35 ft above water on the right** (Jonah wants height; 35 ft allows a double back flip). Needs 16-17 ft of water across the landing at the lowest river stage (10 m platform standard) and a naval architect's check on a 35 ft element on a float. Consider a dedicated pile for the tall petal |
| 35 | Swim reach | **Stem boom runs ~150 m north, under the Hawthorne, to the fire station pier.** It's the Portland Fire & Rescue Station 21 fireboat pier, so the fire bureau's berth access and the bridge owner (Multnomah County) are now in the conversation |
| 36 | Jump petal height | **Scaled back to ~20 ft above water** (v0.12), in proportion with the rose; supersedes the 35 ft version. Landing needs roughly 12-13 ft of water at low river |
| 29 | Options | Petal lineup page with 6 characters: https://claude.ai/artifact/T99tEHYyXiAS9PSg8cT4uA |

## Decisions, round 2 (Davey, 2026-09-26, model v0.3 to v0.7)

Full log with Davey's words per version: `Iterations/CHANGELOG.md`.

| # | Item | Decision |
|---|---|---|
| 10 | Thorn sauna | **Removed** |
| 11 | Roof | **No flat roof deck.** The five petals rise, bend out and open flat; the open petals are the hangout decks. Hot-room roof is a closed bud |
| 12 | Petal guards | **No glass windscreen on the petals** (looked wrong). Code still wants 42 in guards on occupied decks, so this needs a quieter answer: a raised petal-edge lip plus cable/net, or cap the decks as supervised zones. Engineer's call |
| 13 | Fires | **Sheltered, inside each petal:** a cupped outer petal under every open petal holds a fire nook and bench. Each petal = deck above, fire nook below |
| 14 | Glass | **Bridge petal glass** from deck to bend; its fire nook gets a glass windbreak |
| 15 | Pistils | **Wire cages** curving up and out, a heating pipe running up through each and looping back down, stones in and around them. This is a custom heat exchanger around the gas burner: EOS/KUSATEK builds it bespoke, we certify the room |
| 16 | Symmetry | **Explore wild.** Four petal characters in the model: Classic, Wind-swept, Wild bloom, Unfurling. Pick or mix |
| 17 | Slides | **Two petals are group slides**, petal-shaped, drooping side by side into the swim cove |
| 18 | Movement | **Explore petals that open and close.** Bloom/Bud modes in the model. See below |
| 19 | Second sauna | **The Bud across the river**: a permanently closed rose on the west bank, facing the Rose |
| 20 | Drapes | **Partition drapes only**, circle drape removed. Two modes: full, or two petals curtained off |
| 21 | Site | Holman = **Kerr Public Dock** on Google Maps. Rose moors off the dock's outer tip; swim cove between the Rose and the shore |

### Keeping swimmers in (from the Google Maps look at the dock)
- The dock is one long float (~95 m in current imagery) angling out northwest from the Esplanade. Boats moor along its shore side mid-dock. Audrey McCall Beach is just north, then the Hawthorne Bridge.
- The Willamette flows north here, toward the bridge. **Anything that floats, swimmers included, drifts downstream to the north.**
- Plan: the Rose moors off the dock tip with the dock between it and the channel. The slide petals face the shore and land in the calm water between the Rose and the beach.
- **The Stem becomes the downstream swim boundary:** a floating boom from the flower to the shore, curving around the north side of the cove. The three Leaves float inside it as rest and climb-out platforms.
- **A lane line on the upstream (south) side** from the dock to the shore keeps swimmers away from the moored boats.
- The result is a swim cove of roughly 95 x 60 ft (estimate from imagery). To-scale overlay: `The Rose - Site Overlay (Holman-Kerr Dock).png`.
- Unknowns: cove depth (the slides land nearer the shore, where it shallows), whether the City allows a boom tied to the beach, boat traffic to the dock tip, and the Audrey McCall Beach users. Soundings first.

### Open and closed: two experiences, one building
- **The Bloom (open):** summer, day, sunset. Petal decks, slides, fire nooks below. Social.
- **The Bud (closed):** winter, rain, night. Petals rise and lean in, closing a covered ring between the hot room and the petals, a warm cloister out of the wind. Lit from inside, it glows like a lantern. The shell becomes a sound room for quiet sets.
- **The Opening:** a daily sunset ritual, a few minutes long, watched from the shore. Petals move only when empty.
- **Reality check:** petals that carry 8 people each at 100 psf and also move means engineered hydraulic actuators, locking pins and a controls safety case. Precedent: the Milwaukee Art Museum's Burke Brise Soleil opens and closes daily. Estimate +$300K to +$1M. Cheaper routes: move only the slide petals, go seasonal (crane or manual changeover twice a year), or make only lightweight fabric/printed petal tips kinetic.

### The Bud across the river
- A permanently closed, smaller sauna (~20-24) on the west bank. The RiverPlace/Hawthorne Bowl site from the City siting brief fits.
- Dark, quiet, silent sessions: the introvert to the Rose's extrovert.
- Paddle between them (our kayak DNA). When the Rose opens at dusk, the Bud glows back.
- Separate site, separate permit path. Estimate $0.7-1.5M.

## Model v0.2 (2026-09-26)

What changed from v0.1, in both the 3D viewer and the STL script:
- **Outer petals:** five flared shells, 3.75 m tall with rounded rims curling back at the top. They start ~4.75 m out at the deck and flare to ~6 m, overlapping in a spiral. The slit where one petal overlaps the next is the doorway, so you slip in between petals. The rims rise ~1.1 m above the terraces, so the petals are the guards.
- **The void between the hot room and the petal skin is the cool service ring:** amps, transducer feeds, scent cannons, drape motors, ducts, and the stair up to the terraces. That solves "where do the electronics live" for free.
- **Bridge petal is glass** with three ribs.
- Pit widened to 2.0 m radius so the Aufguss host has room to work. Tier rise 45 cm. Ceiling dropped to 2.15 m at the wall (about 1.4 m over the top bench).
- 3 doors (was 4). Seats inside now ~57 (fewer aisles).
- Float grew to **49 ft** so the fire lounges fit outside the petal bases. Petals still stay inside the float edge.
- One low, wide gas stone altar with the pistil stone cage and a flue up through the oculus (replaces the 5-module crown).
- Three leaf floats along the Stem.
- New STL: `rose_petals.stl` (lifts off with the roof). `leaf_floats.stl` replaces `leaf_float.stl`. The STL slide leaves from a different petal than the viewer's; cosmetic, fix in v0.3.

## 3. Site: the puzzle pieces

The whole area is one composition. The Rose is the bloom; everything else is the garden around it.

| Piece | What it is | Where | Notes |
|---|---|---|---|
| **The Rose** | 40-48 seat communal sauna + 5 roof terraces | Own piles, beside Holman Dock | Bridge-facing petal is glass |
| ~~The Thorn~~ | Removed 2026-09-26 | | |
| **The Stem** | Green enclosed waterslide from a petal terrace to the river | Off the river-side petal | Summer only, swim season July to Sept. See section 10 before anyone gets attached |
| **The Leaves** | Three leaf-shaped swim-out floats off the Stem, one where the slide lands, each with a ladder | Along the slide, 10-25 m off the Rose | Double as the swim float the City wanted in Phase 1 |
| **Fire lounges** | Two sunken conversation rings on the deck between petals | Rose deck, river side | Parks fuel ban applies; electric/ethanol "fire" or a water-mist flame effect may be the only legal option |
| **Carved shoreline** | Terraced seating cut into the bluff/bank, facing the Rose and bridge | Holman upland / bluff | Public-benefit piece for the City: free to sit, watch, picnic |
| **Service** | Changing, showers, restrooms, electrical room, storage | Phase 1 trailer; Phase 2 permanent on the gravel lot | Same ops package as the pilot plan |

**Other city spots.** The Rose is one building type that can repeat as a "garden" across the river system: Rose at Holman (flagship), a Thorn-only pop-up anywhere a small float can tie up, a Rose-class build at Zidell someday (best water in the 2016 City study), and RiverPlace/Hawthorne Bowl for a second Thorn. Each site gets a different flower later if we want a series (Iris, Camas, Oregon Grape) and the Rose stays the original.

## 4. The building

Working dimensions. These numbers drive both the STL files and the 3D model; change them in `make_rose_stl.py`.

| Element | Size | Why |
|---|---|---|
| Float | 46 ft (14.0 m) diameter, ~4-4.5 ft deep, concrete-encapsulated EPS | Carries ~150 kips; mass damps wakes; petals stay inside the edge |
| Freeboard to deck | 20 in (0.51 m) | Portland Title 28 minimum for occupied floor |
| Wall line | r = 4.25 m +/- 0.5 m, 5 lobes (31 ft across the petals) | Lobes are the petals; clefts between them hold drapes |
| Sunken pit | 0.6 m below deck, 3.4 m across | Cut into the float hull. Lowers the crowd's center of gravity and gains tier height without a taller building |
| Tier 1 | r 1.70-2.35 m, seat 0.45 m above pit | Coolest seats (~70-75C). Kids-of-heat tier, first-timers |
| Tier 2 | r 2.35-3.00 m, +0.50 m rise | ~80-85C |
| Tier 3 | r 3.00-3.60 m, +0.50 m rise | ~90-100C. Behind it, a standing alcove in each petal at deck level |
| Seats | ~46-48 at 0.78 m per person | Target was 30-50 |
| Ceiling | 2.55 m at the wall, rising to a 5.2 m oculus over the heater | Keeps ~1.2 m clear over the top bench (standard), and a small heated volume for the headcount |
| Doors | 4, one in the nose of each petal, with an aisle stepping down to the pit | 50+ occupants need 2 exits with panic hardware; 4 is comfortable |
| Bridge petal | No door: a 2.4 m wide glass panel from 0.9 to 2.3 m | Seated view of the Hawthorne from every tier |
| Roof | Flat CLT terraces over each petal at 2.75 m, glass guards at 1.07 m (42 in), bud-petal fins curling up around a center drum | 100 psf assembly load. One external stair; roof terraces need their own egress path |
| Heater | The Stove Crown: 5 modules in one stone altar, one per petal | See section 6 |
| Heated volume | ~190 m3 open, ~125 m3 with two petals curtained, ~85 m3 inner circle only | Drives heater size and warm-up time |

**Structure (recommended):** glulam ring beam, curved glulam or CNC-LVL radial ribs (one rib per facet), CLT petal decks, vapor-closed insulated envelope. Hot room lined in thermally modified aspen or alder (not cedar inside; same conflict we flagged on V2). Exterior skin: charred cedar or printed ASA panels on a timber subframe.

**Rough loads (estimate, to be replaced by the engineer's takeoff):** float ~70 kips, superstructure 50-60 kips, people ~17 kips (90 people x 185 lb, the Coast Guard standard weight), misc ~7 kips. ~150 kips total, ~2.4 ft draft.

**Stability rules we design to:**
- Design heel of 2 degrees or less under worst-case crowding (Portland max is 4).
- Roof crowd weight under ~10-12% of displacement. Cap roof terraces at 8 per petal to start, with a host.
- Heavy things low and central: stones, heater, tanks.
- No cantilevers past the float. A circle is a stability gift; don't give it away.
- Never tow it with guests and never market a "cruise." A permanently moored, unpowered structure isn't a vessel (Lozman, 2013), so the building code applies, not Coast Guard inspection. Towing people flips that.

## 5. Sectionable space: the drapes

The drapes do two jobs: they shrink the heated volume on slow days (less power, faster warm-up) and they let us sell part of the room as a private buyout while the rest runs public.

**Three modes, all modeled in the 3D viewer:**

| Mode | Drapes | Seats | Heated volume | Heater load (est.) |
|---|---|---|---|---|
| Full bloom | All up | ~46 | ~190 m3 | ~100-110 kW |
| Three petals | 2 petals closed off | ~28 | ~125 m3 | ~65-70 kW |
| Inner circle | Ring drape down at r = 3.0 m (top tier closed) | ~26 | ~85 m3 | ~50 kW |

**How to build them:** pivoting timber panels at the stove end plus silicone-fiberglass drop drapes at the outer clefts. Details in section 6. Closing a petal also switches off that petal's heater module in the Stove Crown.

**Operational rule:** drapes only move between sessions, never with people seated under them.

## 6. Heat

> **Updated 2026-09-26: Davey chose EOS natural gas.** The electric analysis below stays as the fallback if gas is refused.
>
> **EOS gas = the KUSATEK line.** EOS lists KUSATEK gas-powered heater systems "as a standard solution, as well as an individual special solution." Models named: KUSATHERM 90, 120 and 240. Up to **1,400 kg of stone per unit**, max height 80 cm (low and wide, which suits a sunken altar), a "HOT button" for Aufguss stone temperature, natural gas. Installed at Therme Erding (the world's largest spa) and Badewelt Sinsheim (Guinness record largest sauna). Output in kW isn't published. Contact: EOS Saunatechnik GmbH, Driedorf, Germany, +49 2775 82 0, info@eos-sauna.de. US channel is ThermaSol. Source: eos-sauna.com/en/wellness-facilities/gas-powered-sauna-heaters
>
> **Certification, per Davey: we certify the room with the stove in it, not the stove.** The engineer of record and inspector sign off the space: clearances, combustion air, the flue out the oculus, gas piping on a float, CO detection, ventilation. What to expect so it doesn't surprise us: KUSATEK units carry German gas approval (DVGW), not a US listing, and Oregon's gas code expects appliances to be listed or approved. The standard fix is a **one-time field evaluation label** (CSA or Intertek inspects the installed unit on site). It's a fee and a visit, not a redesign. Ask EOS/ThermaSol if any US installs already went through it.
>
> **Sizing:** ~105 kW is about **360,000 BTU/hr**. The biggest off-the-shelf US gas sauna stoves are 80-85K BTU (Scandia, Torch), so a KUSATHERM, or several Torch units in one altar, is the only way to get there. NW Natural service sized for ~400K BTU/hr down the gangway.
>
> **Holman conflict to manage quietly:** Parks dock rules ban stoves, heaters and flame on docks. That rule covers the Parks dock. The Rose on its own piles and its own DSL lease is a separate structure, the way our Columbia boats are. The LOI needs to say that plainly.
>
> **Pistil stone cage:** custom, ours, around the KUSATEK core. The EOS stone capacity and clearances govern, so send them the pistil drawing and have them approve the cage before fabrication.

**Bottom line:** the Rose needs roughly **100-110 kW of electric heat** with all five petals open, and Holman has no power at all. The heater decision is really a power decision.

**Why electric.** Parks dock rule PRK-1.17 bans "open flames, live coals ... stoves, and heaters" on docks, the 2026 commercial guidelines ban fuel-based equipment and generators, and Parks provides no electrical service on docks (the only power on offer is 110V/20A). Gas and wood are out at Holman. Even electric heat needs explicit carve-out language in the LOI, which is one more reason the Rose should be its own permitted structure beside the dock rather than equipment on it.

**Sizing (for our 190 m3 room, not a generic one).** Big commercial rooms run well under 1 kW/m3: the EOS Mega is 72 kW for 130-160 m3, about 0.5 kW/m3. The hidden load is fresh air. 40 people need ~10 L/s each, heated from 5C to 90C, which is ~40 kW on its own in winter.

| Mode | Seats | Volume | Heat installed (est.) | Current at 480V 3-phase |
|---|---|---|---|---|
| Full bloom | ~46 | ~190 m3 | ~100-110 kW | ~130 A |
| Three petals | ~28 | ~125 m3 | ~65-70 kW | ~85 A |
| Inner circle | ~26 | ~85 m3 | ~50 kW | ~60 A |

Plan a **400A, 480V 3-phase service** brought down the gangway from PGE, a step-down transformer on the float, and expect demand charges on a 100+ kW peak. That utility run is probably the single biggest cost and schedule item nobody has priced yet.

**The EOS question.** EOS (German, ~80% owned by Harvia since 2020) makes the big Aufguss-arena heaters (Mega HD 42-72 kW, Goliath, Zeus, Herkules), but they're **400V European units**. The US lineup stops at the Mythos S45 (12-15 kW, 208V, ~$10.4K). A Mega here means a 480-to-400V transformer and a UL/ETL field evaluation for the Oregon inspector. US channel: ThermaSol, Round Rock TX (800-776-0711). No public Mega pricing; guess $15-30K each.

**Recommended: the Stove Crown.** Five heater modules clustered in one custom stone altar at the center, **one module facing each petal**. Five petals, five heaters, ~20 kW each = ~100 kW. This solves three problems at once:
1. Zoning works. Close a petal, switch off its module. (A single central stove leaks heat into every closed sector, since they all touch it at the point.)
2. Redundancy. One module down doesn't cancel the night.
3. Code. UL-listed units (Harvia Virta Pro HL200E: 20 kW, 208V, 58A, ~$3.9-4.9K each) behind the transformer is the easy inspection path. The custom part is the stone cage and cladding, not the electrics.

The altar holds 300-600 kg of stone in total, which is what gives it that deep, soft Aufguss löyly. EOS's biggest single heater only carries ~150 kg, so clustering is the way to get there either way. If Davey wants the EOS name on it specifically, the ask to ThermaSol is: can they supply Mega-class units with a UL path, or build a custom crown around US-listed elements?

**Tiers and air.**
- Expect 10-15C per tier (Pust in Oslo runs 75/85/100C on three levels). Tier 1 is the gentle row for first-timers.
- 40-45 cm tier rise, 105-120 cm from top bench to ceiling. Going taller just wastes kW. Our model is at 50 cm rise; tighten to 45 in the next revision.
- At least 6 air changes per hour and 9-12 L/s per person. Supply low near the stove, exhaust low on the far side, plus a ceiling purge vent (our oculus).
- A Saunum-style ducted air-mixing loop, fans outside the hot room, switched off during Aufguss.
- Leave a 1.2-1.5 m working ring around the stove guard for the Aufguss host, with a floor drain. (Our pit is 1.7 m radius with a 1.1 m guard, so ~0.6 m. **Widen the pit** to ~2.0 m radius in the next revision.)
- Aufguss water rule of thumb: ~20 g per m3, so ~4 L per full infusion here.

**Automation from EOS worth wanting:** AromaTec II (dosed water + up to 9 ml scent, 1-3 scents), AquaDisp (timed splashes), the Watermill (a 1.7 m wheel that pours every 30-60 min, a theatrical object in its own right), and EOSphere (drops hot stones into a lit water tank for a steam burst).

**The drapes, revised.** No sauna anywhere has drop-down insulated drapes that we found, and off-the-shelf insulated curtains are vinyl and bubble foil that fail at 100C+. The approach that works:
- **Pivoting insulated timber panels at the stove end** of each cleft to close a petal (sealed edges matter more than R-value).
- **Drop drapes at the outer part of each cleft and for the ring drape:** silicone-coated fiberglass skins (rated to 260C, pass NFPA 701) quilted over mineral wool, on a track whose motors or counterweights sit outside the hot room.
- Drapes stow in a ceiling slot, above the bench line but insulated from the hot layer.

**Occupancy threshold to decide early:** 49 people or fewer in the whole building (interior + roof) may keep it out of A-3 assembly occupancy, which is lighter on egress, fire and sprinklers. 50+ is A-3. Our full-bloom plan (46 inside + ~40 on the roofs) is A-3. Confirm with BDS in the pre-app meeting before designing around either answer.

## 7. The 4D layer: sound, touch, scent, light

**The one rule:** almost no electronics survive the hot room. Amps, drivers, transducers, projectors and scent machines live in a cool ring under the lowest tier or outside the wall. Only glass fiber, wood and a few 120C-rated parts go inside. Every cool cavity gets intake air and a temp sensor that auto-mutes the amps past ~55C.

### Touch (felt, not loud)
- **Clark Synthesis AW339** transducers, the only ones we found sold for wet, humid installs (hot tubs, boat hulls; Clark recommends them for steam rooms). ButtKickers hit harder but cut out at 70-75C and aren't moisture rated.
- 15 zones minimum (5 petals x 3 tiers), up to ~30 units at Clark's one-per-4x4-ft density. Bolted to blocking under each tier, not to the seat slats. Heat shield above each one.
- Three 8-channel amps in the dry electrical room. Each zone has its own channel so a wave can roll around the ring petal by petal or climb tier to tier.
- **Isolate the bench frames from the hull** with elastomer pads. On a float, bass that reaches the hull turns the whole building and the water into a subwoofer.
- No large sauna anywhere does per-seat tactile audio that we found. That's a first worth saying out loud.

### Sound (directed, not blasted)
- A ring of zones, one or two speakers per petal: **EOS 945429** sauna speakers (120C, IP65) inside, or ordinary install speakers in the cool cavities firing through slotted bench risers.
- Pan a sound from one petal's speaker and shakers to the next and it moves around the room. That's the "sphere" effect at a fraction of the cost.
- Skip Holoplot/L-ISA/d&b. Six figures, not heat rated, and it pushes the brand toward nightclub.
- Optional upgrade later: FLUX SPAT Revolution or Meyer Spacemap Go so a host can draw sound paths live on an iPad.

### Scent
- **Primary scent = löyly.** EOS AromaTec II automated dosing (1-3 essences, 0-9 ml per pour) or Harvia Autodose, triggered from the show controller.
- **The signature moment: a cool vortex ring.** A cannon mounted outside the wall fires cool scented air through a port at the top tier at the peak of a round. Cool air landing on skin at 90C is probably the best single "4D" beat available here.
- **Scent Cannon** (the Instagram account Davey mentioned) is a small outfit in Kittery Point, Maine: a vortex-ring cannon with two blendable scents and targeting sensors, V2 due late 2026, sold mostly as an event service. No public specs or price. Worth a conversation about a custom install or a rental for the launch. Cheap test rig first: a $300 fog-ring cannon run on scented air only.
- **Pro DMX scent box:** Olorama (10-20 scents, quote only), ducted in from outside.
- **Rose City palette** (all natural, water-diluted): Douglas fir (opening), cedarleaf (sparing), rose geranium/rose blend (the bloom, at the peak), petrichor accord as a cool ring, river-cold peppermint at the fade. Winter: a trace of birch tar.
- **Safety:** no glycol fog, no neat oil on stones (pyrolysis into formaldehyde and acrolein), one house palette at a time because wood soaks up scent, a 5-10 minute exhaust purge between sessions, and one fragrance-free session a day.

### Light
- **Shadows need off-center sources.** A light in the middle casts no rib shadows. Put a point source at the base of every rib and cross-fade them around the ring once per round: the rib shadows sweep across the dome like a sundial.
- Cariitti glass fiber (2700K, fibers to 180C), Cariitti LED strip (rated 125C; Harvia's is only 60C), and a fiber star ceiling in the dome for "night löyly."
- Light the löyly: a warm uplight on the heater turns each pour into a lit column of steam.
- Outside a heat-rated window: a dim gobo projector throwing river-caustic ripples into the room.
- 2700K daytime, fading to 1800-2200K amber at night, no blue. Slow drift only; fast flicker reads Halloween.
- Outside at night: warm rose uplights under each petal. The Rose glows from across the river, which is the photo that sells it.

### Acoustics
- Bare wood gives ~1.2 s of reverb occupied, 1.7 s empty. Target 0.6-0.8 s so a host's voice carries and 40 people chatting doesn't roar. That takes ~50-60 m2 of slatted timber over rock wool.
- **Round rooms focus sound.** Fixes: faceted or convex petal walls (never smooth arcs), deep irregular rib spacing as diffusers, absorb the dome, and let the heater tower scatter the center.
- Get an acoustic consultant's ray-trace ($3-10K) once geometry is set.
- Portland noise code: 65 dBA in commercial zones, lower near residential, minus 5 dBA at night. Seat transducers are our friend here.

### Control
One brain: **Q-SYS Core 8 Flex** (audio zones, relays for the dosing unit and cannons, heat-sensor auto-mute) plus **QLab on a Mac mini** running each session as a timeline and sending DMX. The host gets an iPad with six buttons: Start ritual, Next round, Löyly now, Cool ring, Hold, Fade out. Plus a hard "all off, lights up."

**Sample 12-minute round:**
1. 0:00 House fades to 2200K, star ceiling up, a barely-there 35 Hz drone in the benches
2. 1:00 Host speaks
3. 2:00 First pour, Douglas fir. Tactile swell rolls petal to petal. Sundial chase begins
4. 5:00 Second pour, cedar and rose. Towel work, rhythm felt through the benches tier by tier
5. 8:00 Peak, rose. Lit steam column. Benches at max, room still quiet
6. 10:00 Cool vortex ring to each petal in turn, river/petrichor
7. 11:00 Silence. A sound bowl struck through the bench backs. Stars only
8. 12:00 Exhaust purge, lights to 2700K, doors open to the terraces

**Sensory equipment budget:** ~$37K to ~$105K before install.

## Interior acoustics plan (v0.13 geometry)

**Goal:** a hot room that feels calm and warm at every occupancy. Target reverb 0.5-0.7 s whether it's empty or full, crowd noise under ~65 dBA, and the host's voice clear without a mic.

**Where we are (estimate, Sabine, ~180 m3 room, ~230 m2 of wood surface):**

| Occupancy | Bare wood | With ~35 m2 of treatment |
|---|---|---|
| Empty | ~1.3 s (echoey) | ~0.7 s |
| Half (~28) | ~0.9 s | ~0.6 s |
| Full (~57) | ~0.7 s | ~0.5 s |

People are the best absorber in the room, so a full session is fine even untreated. The problem is quiet and half-full sessions, which are most of them. The target is about 35 m2 of absorptive surface, roughly 15% of the room.

**1. Absorb in three places**
- **Upper ceiling (the bud):** slatted thermo-wood over 50-100 mm stone wool, with 10-20 mm gaps. This is the biggest, least-touched surface. Stone wool is non-combustible and fine at sauna temperatures. The foil vapor barrier goes behind the wool, never in front of it, or it reflects.
- **Bench risers:** slotted riser boards with wool behind them. The same cavities already house the speakers and transducers, so one detail does two jobs.
- **Upper walls behind the top tier:** above head height, where hands and wet towels don't reach.

**2. Break up the round shape.** Round rooms focus sound to the middle and let whispers crawl around the wall.
- Make the lobe walls **faceted** (flat 1-1.5 m panels), never smooth arcs. This is the single biggest fix.
- Run the petal ribs down the ceiling as **timber diffusers**, at irregular spacing.
- The stone altar and pistil cages at the center already scatter sound from the focal point.
- Tilt the bridge-view glass 5-8 degrees so it doesn't flutter-echo with the wall opposite.

**3. Keep outside noise out.** The roof lounge now sits right on top of the hot room.
- **Float the crown deck** on rubber isolation pads over the insulated roof, so footsteps, the fire circle and roof chatter don't drum on the ceiling. The 100-150 mm of insulation the heat needs anyway helps a lot.
- **Isolate the benches** and the transducer blocking from the hull with elastomer pads.
- The **doors** open onto the amphitheaters, where there's fire and chatter. Tight heat seals already help; add soft-close hardware.

**4. Make it tunable.** Build the ceiling absorbers as **removable cassettes**. Measure reverb after the build (a sine-sweep test, or a consultant's $3-10K commissioning), then add or pull cassettes until it sounds right. Partition drapes in wool felt add absorption when they're down.

**5. Set it through operations.**
- House sound stays low (60-65 dBA). Bass goes through the benches, not the air.
- Run silent sessions and quiet hours; the Aufguss sessions are the loud ones.
- A decibel meter on the host's iPad, so "too loud" is a number, not an argument.

**In the model (v0.14):** faceted walls, irregular ceiling ribs over a slatted absorber ceiling, slotted risers. Not yet modeled: tilted window glass, isolation pads under the crown deck.

**Budget:** about $15-35K for slat-and-wool ceiling and riser treatment, plus $3-10K for acoustic ray-trace and commissioning (est.).

## 8. 3D printing: what gets printed

| Print it | Build it in timber/steel/concrete |
|---|---|
| **The scale model** (now; files in this folder) | Primary structure: glulam ring beam and ribs |
| Molds and formwork for the curved ribs and float pods | Float: concrete-encapsulated EPS |
| Exterior petal skin panels in ASA or basalt-PETG on a timber subframe | Hot-room lining and benches: thermo-aspen/alder |
| Guard infill panels, light fins, signage, door pulls | Heater enclosure, stone cage, anything within code clearance of the heater |
| The Stem slide shell (or conventional FRP) | Stairs, guard posts, drape tracks |
| Acoustic baffles in the changing rooms and lounge | |

**Path:** CAD in Rhino 8 + Grasshopper ($995) with Karamba3D for early structure and Orca3D for hydrostatics. Hand clean geometry plus a weights-and-CG spreadsheet to the PE (SAP2000/RISA) and naval architect (GHS/Maxsurf). Pilot 1-2 full-size printed exterior petal panels from a large-format shop. UMaine's printer (96 x 32 x 18 ft) could print the whole shell, but access is a sponsored research partnership, likely six figures.

**The scale model (this week):**
- Files: `3D Print Model/`. 1:60 scale, the float is 233 mm across, fits a Bambu X1/P1 bed.
- Print `rose_base_interior.stl` and `rose_roof_removable.stl` separately; the roof lifts off to show the tiers and pit. The slide needs supports.
- Change any dimension in the script, run `python3 make_rose_stl.py`, reprint. `--scale 50` for 1:50.
- Service route if we don't print in house: Craftcloud or Xometry, ~$150-600 at 1:50, $600-2,500 at 1:25 (resin, finished).
- Party trick for the City meeting: float the model in a tub and load one side with pennies. Not an engineering test, but it makes the stability conversation real.

## 9. Certification: who signs what

| Role | Scope | Candidates |
|---|---|---|
| Oregon PE, Engineer of Record (Title 28 requires one) | Float, piles, moorage, gangway, superstructure | KPFF, Moffatt & Nichol, WSP (ex-BergerABAM), Reid Middleton, or whoever stamps Topper's floats |
| Naval architect | Weight/CG, stability, wake and wind cases, post-build inclining test | Elliott Bay Design Group (did a floating pool/entertainment barge study), Glosten, Art Anderson, Impact Naval Architects |
| Architect of record | A-3 assembly occupancy, egress, fire | TBD. Kyle (Zen Sauna) for sauna design inside the envelope |
| Geotech | Piles | Via the PE |
| Acoustic consultant | Ray-trace + commissioning | $3-10K |
| Float builder | Float + moorage | Topper (Woodland WA, 360-657-9981). Ask if they'll carry a building or only supply the float |

**Code path:** Portland BDS will likely treat the Rose as an OSSC A-3 assembly building on an engineered float, with Title 28 flotation rules layered on. That's new for the City, so start with a pre-application conference. In-water permits for new piles (Army Corps Section 10, NMFS consultation for salmon, DEQ 401, City river overlay review) are the long pole: estimate 12-24 months, and pile driving only in the summer in-water work window.

**Right first spend:** a $15-40K feasibility and stability study from a naval architecture firm, using our model and weights. It turns the drawings into something the City and a lender can believe.

## 10. The Stem slide: honest read

Put it in every render. Open it in year two.

- **Depth:** the water-slide standard wants 3 ft minimum at the exit, up to 4'6". In a river that swings ~16 ft seasonally, design for 8-10 ft at low water and a floating exit (the Leaf) that rides the river. Nobody has published soundings at Holman; we need our own.
- **Current:** the City bans beaches above 3 ft/s. Summer near-shore is 0-1 ft/s, but Holman sits beside the Hawthorne Bridge piers, where current speeds up. Measure before designing.
- **Water quality:** City testing in 2025 had 100% of samples under the E. coli standard, but Holman isn't a test site. No contact for 24-48 hours after heavy rain (CSO outfalls).
- **Insurance:** standard liability policies usually exclude slides. Specialty coverage plus a lifeguard on every slide hour.
- **Season:** July to September only (the river is snowmelt-cold before July).
- **Precedents:** Copenhagen's Kalvebod Bølge harbour slide; Berlin's Badeschiff, which started as a City art project and became an icon.
- **Why keep it anyway:** it's the single most shareable image in the whole set, and a green stem off a rose is the design's punchline. Year one, the Stem can stand as a sculptural element and stair-rail with the Leaf as a swim float. Year two, it opens.

## 11. Money

### Build budget (order of magnitude, before any quotes)

Every line here is an estimate from the research, not a bid. Treat it as a range to test, not a number to raise against yet.

| Line | Low | High | Notes |
|---|---|---|---|
| Feasibility + stability study (naval architect) | $15K | $40K | The first real spend |
| Design + engineering fees (architect, SE, NA, MEP, acoustics, permit consultant) | $120K | $300K | ~8-15% of build |
| Permits, DSL lease setup, in-water permitting, soundings | $30K | $80K | Est. |
| Float, 46 ft concrete/EPS | $350K | $650K | ~1,660 sf at $200-400/sf. A 40 ft float saves ~25% |
| Piles, moorage, gangway | $120K | $250K | Est. |
| Superstructure: glulam, CLT, envelope, thermo-wood interior, 3 tiers, terraces, guards | $400K | $700K | Custom curved timber is the expensive part |
| Stove Crown: 5 heater modules, stone altar, controls | $50K | $140K | Low = Harvia Virta Pro; high = EOS Mega with transformer and UL field eval |
| Electrical service: PGE 480V/400A, transformer, dock feeders | $120K | $300K | Nobody has priced this yet. Biggest unknown |
| Ventilation + air mixing | $30K | $60K | |
| Sensory package (touch, sound, scent, light, control) + install | $60K | $145K | Equipment $37-105K |
| Drapes + pivoting panels | $30K | $80K | |
| The Thorn (sauna + hex float + gangway) | $120K | $220K | |
| Fire lounges + carved shoreline seating | $50K | $150K | Shoreline depends on the upland lease |
| Service trailer / changing / showers (Phase 1 ops) | $60K | $120K | Same ops package as the pilot plan |
| **Subtotal: the Rose garden, year one** | **~$1.55M** | **~$3.2M** | |
| Stem slide + Leaf float (year two) | $150K | $350K | |
| Contingency, 20% | $340K | $710K | |
| **All in** | **~$2.0M** | **~$4.3M** | |

**How to shrink it without losing the idea:** a 40 ft float instead of 46; a single heater service at 208V if PGE makes 480V painful; printed or charred-cedar skin instead of CLT petals; the Thorn as a phase-two add; the shoreline carving as the City's in-kind contribution.

### Revenue sanity check (illustrative, assumptions stated)

- Public sessions: 46 seats x 40% average occupancy x $38 average ticket x 5 sessions/day x 330 days = **~$1.15M/yr gross**. For reference, the whole current operation did ~$261K net from Nov 2025 to Aug 2026 with far smaller rooms, so this assumption needs real testing.
- Buyouts (research estimate for a 2-3 hour block; no Portland sauna offers a 30-50 person buyout today):

| Use | Price per block |
|---|---|
| Weekday corporate | $3.5-5K |
| Weekend party | $5.5-7.5K |
| Peak Saturday wedding | $7.5-10K |
| Signature dates (solstice, Rose Festival, NYE) | $10-12K+ |

For comparison: a 25-50 guest Portland wedding runs ~$21-26K all in; micro-wedding venues charge $2.8-10K; Portland Spirit charters at $1,000/hr. Two wedding/corporate buyouts a week at ~$6K is ~$600K/yr on its own. The Finnish bridal-sauna tradition gives weddings a real story, not a gimmick.

### Funding stack (how others did it)

| Source | Realistic | Precedent |
|---|---|---|
| **Founding presale** (refundable until permits clear) | $350-500K if about half the ladder sells | Portal sold 400+ founding memberships in month one |
| **Community investment round** (Wefunder, revenue share) | $250K-1M | Sisu + Löyly ~$75K from 71 investors; Grotto $1.3M; Helsinki's Allas Sea Pool raised EUR 0.8-1.1M from its crowd plus public loans |
| **Material / presenting partners** | $50-150K each, 1-3 of them | Trosten (Oslo) was built with a Hydro aluminum sponsorship and made TIME's Greatest Places 2025 |
| **Grants** | $25-50K | Travel Portland visitor-experience grants (for-profits have won); RACC $1-5K (window open to Oct 28); Travel Oregon only through a nonprofit or PP&R |
| **City in-kind** | Lease credits | PP&R has ~$270K restricted for Holman upkeep against ~$74K/yr of costs, about 3.6 years. An operator who takes over dock upkeep solves the City's problem. That's our lease leverage |
| **Debt** | The balance | SBA 7(a)/504 against the presale + buyout book |
| Rewards crowdfunding (Kickstarter) | $25-45K | Low ceiling; use it for the model and film, not the build |

**Cautionary tale:** NYC's Plus Pool raised ~$314K on Kickstarter over 10 years ago and still isn't open. Take refundable deposits only until the permit path is real.

## 12. Selling it before it exists (Jordan's idea)

Davey's framing: use social media to prove demand and pre-sell the Rose, with Jordan (our former PR lead at Early Bird, still on call for gut-checks) helping shape it.

**The sequencing rule.** Holman is off the record. Naming the site publicly before the team approves strategy, the LOI is signed, and City comms are aligned would break that. So:

| Stage | What's public | Trigger to move on |
|---|---|---|
| 0. Private (now) | Nothing. Model, renders, feasibility study, this doc | Team approves strategy |
| 1. Tease | "A rose is coming to the Willamette." No site, no founder names. The 3D print, the scent-ring test, the tactile bench prototype | Name cleared by the attorney |
| 2. Waitlist | Free waitlist, then $25 refundable deposit | LOI signed |
| 3. Reveal | Site, renders, founding ladder, press (Jordan) | City comms aligned |
| 4. Build in public | Grant's-style build diary, weekly | Permits in hand |

**Founding ladder (draft, research estimate):**
- Free waitlist, then a $25 refundable deposit
- 500 **Petal** founding memberships at $600-900 (20-30% off, locked for life)
- 100 **Thorn Circle** at ~$2,500 (private Thorn nights, first buyout dates)
- 12 **Petal Patrons** at $10K (a petal named for a rose variety of their choosing, never a person's or brand's name on the Rose itself)
- 1-3 material or presenting partners at $50-150K. Sell naming on elements (the Stove Crown, the Stem, the Leaf), never on the Rose

**Content we can make before a single permit:**
- Time-lapse of the 3D-printed model coming off the printer; the roof lifting off to show the tiers
- The model floating in a tub, pennies on one petal
- A scent-ring cannon test on the current dock (cool air only)
- **Prototype the sensory layer in the existing sauna first**: two Clark transducers under one bench and one scent ring. It de-risks the tech and it's the best teaser we have: "feel the next thing we're building."
- The interactive 3D model as a landing page for the waitlist (after stage 1)

**Ask Jordan:** a short project engagement for the stage 3 reveal (press list, exclusive, fact sheet), and a gut-check on the ladder pricing. Don't re-open the full retainer.

**Name.** No US sauna turned up using "Rose City Sauna" or "The Rose Sauna" (nearest is Under The Rose Sauna House in Vancouver, BC). "The Rose" alone is a weak, crowded mark. Options: "The Rose by Ebb & Ember," or **"Testout"** after the Madame Caroline Testout rose, the variety Portland planted along 20 miles of streets for the 1905 exposition and the origin of the Rose City name. Web check only; the attorney clears it before stage 1. "Portland Rose Festival" is a registered mark, so any co-branding needs a license.

## 13. Brainstorm bank

Unsorted on purpose. Add freely; we'll let them fall into place.

**Ritual and program**
1. **The Bloom:** at sunset the five exterior petal lights come up one at a time, then the crown. A daily 60-second moment people gather on the shore to watch.
2. **Hear the river:** a hydrophone under the float feeds live river sound into the benches. You feel the Willamette moving under you.
3. **Bridge lift cue:** when the Hawthorne lifts, the room gets a special light and sound cue. Guests will wait for it.
4. Aufguss masters in residence; host a US Aufguss WM qualifier on the Willamette.
5. Silent sessions, sound-bath sessions, star-ceiling night löyly, a fragrance-free session daily.
6. Tier 1 family sessions at gentler heat.
7. Live musicians on a roof terrace, piped into the room through the benches.
8. **Revive the Big Float.** HAP's July river celebration ended in 2022. The Rose could anchor a new one.
9. Rose-hip tea and rose-water cold towels at the door. Rose ice balls melting on the stones at the peak.
10. Solstice, equinox, full-moon and Rose Festival week programming.

**Weddings and events**
11. Finnish bridal sauna: the Thorn as the getting-ready room, vows on the bridge-facing terrace, the whole party in the Rose after.
12. Proposal package in the Thorn, with a scent ring timed to the question.
13. Corporate buyouts with the drapes: half the room private, half public.
14. Rose Festival partnership: we sponsor them (they lost $1.1M in 2024 and merged parades for 2026), not the other way round. Royal Rosaria court sauna.

**Design details**
15. Petal names: each petal named for a Portland rose variety or International Rose Test Garden winner (PP&R runs both the Test Garden and Holman).
16. Signature scent commissioned from a Portland perfumer.
17. Rain chains off each petal tip. In Portland rain the Rose weeps into the river. Ties to the Downpour.
18. Cold stations at each cleft: a Downpour bucket or a small waterfall per petal.
19. Heat recovery: exhaust air warms the changing rooms and heated benches on the fire lounges.
20. The Watermill: EOS's 1.7 m pouring wheel, as a slow kinetic sculpture on one wall.
21. Printed exterior petals with a lattice (Branch-style) that glows from inside at night.
22. The Leaf doubles as the public swim float the City asked for.
23. Exterior petal color shifts with the season: blush in spring, deep red in winter.

**Marketing and money**
24. Founding members get a mini Rose, 3D-printed from the same files as the model.
25. Instagram filter that drops the Rose onto any water.
26. A short documentary: from a desktop print to a floating building.
27. Material partners with an Oregon story: an Oregon mass-plywood or glulam maker for the ribs, a Portland metal shop for the Stem.
28. The Rose as a series: Iris, Camas, Oregon Grape at other city spots, the Rose stays the original.
29. Steelhead (Live Nation, 3,500 people, opens summer 2027) is next door. Post-show sessions. Also: schedule sound programs around their show calendar.
30. OMSI District's public plaza (planned just north of Tilikum, $15-17M of City infrastructure) is the Phase 3 hook for a permanent Rose.

**Accessibility (not optional)**
31. At least one door with a level route and a wheelchair space at the alcove on tier 3 height. The sunken pit and tiers make this hard; design it in from revision two, not as a retrofit.

## 14. Open questions for Davey

Answer by number. Some are also in the chat.

1. **Site:** keep Holman as the flagship target (own piles beside the dock), or design the Rose to be site-agnostic and pick Holman vs Zidell vs RiverPlace later?
2. **Occupancy cap:** 49 people total (possibly avoids A-3 assembly rules, fewer roof seats) or full bloom at ~46 inside + ~40 on the roofs (A-3)?
3. **Heat:** Stove Crown of 5 UL-listed modules (easier), or push ThermaSol for EOS Mega units (the name you asked for, harder permit path)?
4. **Float size:** 46 ft (current model, generous deck) or 40 ft (~25% cheaper float)?
5. **Roof terraces:** all 5 petals, or 3 (river and bridge side) to keep weight and egress simpler?
6. **Fire lounges:** worth fighting the Parks fuel ban, or go straight to an electric/water-mist flame effect?
7. **Stem slide:** year-two opening OK, or is it a day-one must?
8. **The Thorn:** day one, or phase two?
9. **Name:** The Rose by Ebb & Ember, Testout, or something else? (Attorney clears it before any tease.)
10. **Jordan:** want me to draft a short project-scope note to Jordan for the reveal? (Draft only, for your OK.)
11. **Model print:** print in house (buy a ~$1K printer) or send to Craftcloud/Xometry?
12. **First spend:** OK to shortlist 3 naval architecture firms for a $15-40K feasibility and stability study? (Nothing goes out without your OK, and Holman stays unnamed until the team approves.)
13. **Prototype in the current sauna:** OK to spec two tactile transducers and one scent-ring test for the existing boat?
14. **Who leads:** Hannah B leads Holman. Does she lead the Rose too, or does this sit with you and Kyle?
15. **Budget ceiling:** what total are you willing to raise and borrow for the whole garden? That decides float size, the Thorn and the slide.

## 15. Sensory test in the current sauna (this week)

Goal: feel the two riskiest ideas before designing around them, and get teaser footage. Budget ~$1.2-1.8K. Installer: Grant or Zach Hull.

**Kit**
| Item | Qty | Est. |
|---|---|---|
| Clark Synthesis AW339 all-weather tactile transducer | 2 | ~$500 |
| 2-channel class-D install amp, 150 W/ch | 1 | $200-400 |
| miniDSP 2x4 HD (low-pass at ~100 Hz, limiter) or an amp with built-in LPF | 1 | ~$225 |
| Bluetooth receiver + tinned, silicone-jacketed 14 AWG speaker wire | 1 | ~$80 |
| Temperature logger probe for the bench cavity | 1 | ~$30 |
| Fog-ring / vortex cannon, run on air only (no glycol fog) | 1 | ~$300 |
| Food-grade fir and rose-geranium oils, cotton pads | | ~$60 |

**Install**
1. Bolt both transducers to a 2x6 block between bench joists on the underside of the **lowest** bench, never to the slats. Drip shield above each. Probe in the same cavity.
2. Amp, DSP and receiver **outside** the hot room, in a dry box.
3. Scent cannon **outside the sauna** first, on the cool-down deck, firing cool air across the lounge. Scent comes from a few drops on a cotton pad inside the chamber. Never in the hot room on day one.

**Test**
- 3 sessions over two weeks: a quiet drone, a slow heartbeat, river sounds. Low volume only.
- Watch the cavity temp. Stop if it passes ~55C.
- Ask 5 guests per session: could you feel it, was it too much, would you pay more for it.
- Film it for stage-1 teasers: no founder names, no Holman.

## 16. Name bank (brainstorm, not cleared)

Top three picks first.

1. **Hawthorn** - hawthorn is in the rose family (Rosaceae), and the Hawthorne Bridge stands over it. Two meanings, one word. (The bridge is spelled with an e, after Dr. J.C. Hawthorne; the plant without. Pick one on purpose.)
2. **Nootka** - after Rosa nutkana, the wild rose native to the Pacific Northwest. Local, botanical, ownable.
3. **Testout** - after the Madame Caroline Testout rose Portland planted along 20 miles of streets in 1905, the origin of the Rose City name.
4. **Corolla** - the botanical word for the ring of petals. Also a car, which hurts.
5. **The Rose by Ebb & Ember** - plain and clear.
6. **Rosarium** - Latin for rose garden; fits the whole site with Thorn, Stem and Leaves.
7. **Rosa** - short, warm, hard to trademark.
8. **Bloom** - verb and noun; "the Bloom" as the sunset ritual.
9. **Rose Hip** - playful; also the tea at the door.
10. **Pistil** - named after the heart of the flower and the stones.
11. **Wildrose** - loose, outdoorsy.
12. **Floribunda** - a rose class that blooms in clusters; long but lovely.
13. **Ember Rose** - ties directly to the brand.
14. **Rosewater** - a sauna on the water, named for a scent.
15. **Madame** - short for Madame Testout; a bit of attitude.
16. **The Garden** - the collection name, with the Rose as the flagship.
17. **Nutkana** - the Latin half of Nootka; more ownable, harder to say.
18. **Thornrose** - the Grimm name for Sleeping Beauty (Dornröschen). Dreamy, a little dark.

All still need the attorney's trademark check before anything public.

## Status

- [x] Concept, research (4 tracks), parametric model, STL files for a 1:60 print (2026-09-26)
- [x] Interactive 3D model published: https://claude.ai/artifact/VPwztPdkTQfPb23vPh2yzz (local copy: `The Rose - 3D Model.html`)
- [ ] Davey answers section 14
- [x] Revision 2 of the model (flared petals, 3 cleft doors, pistil stones, 3 leaves, wider pit, 45 cm tiers)
- [x] v0.3 to v0.7 in the viewer (see Iterations/CHANGELOG.md)
- [ ] STL files are at v0.4 classic geometry (open petals, bud roof, fire cups). Wild variants, slide petals, stem boom and the Bud are viewer-only so far
- [ ] Pick a petal character, then v0.8: faceted hot-room walls (acoustics), accessible route, petal-edge guard solution
- [ ] Soundings and current in the cove before slide design
- [ ] Print the scale model
- [ ] Naval architect shortlist (no outreach until approved)
- [ ] Sensory prototype in the existing sauna
