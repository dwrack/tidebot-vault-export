# Waterfall Plunge — Design Brief (working draft)

**Started 2026-09-23 from Davey's directive.** Multi-fall cold water feature on the floating docks: pumps Columbia River water up and drops it in several cascades for cold plunge + water massage. On-demand timer, not continuous. Enclosed space (mossy walls or similar). Davey + Jonah both like the enclosure idea.

Sibling to the Downpour (see `Downpour Productization — Project Brief (Aug 2026).md`). Where the Downpour is one 60L dump, this is sustained falling water you sit or stand under.

## Decisions (Davey, 2026-09-23)

| # | Item | Decision |
|---|---|---|
| 1 | Placement | **B: public deck, near the lounge** |
| 2 | Who | Every guest, included |
| 3 | Falls | Three, three shapes: **a wide sheet (max 2 ft wide), a vertical downpipe column, an angled pipe jet** |
| 4 | Trigger | Push button |
| 5 | Cycle | **180 seconds** |
| 6 | Posture | Both sit and stand |
| 7 | Temp | River temp, no chiller |
| 8 | Enclosure | Moss wall, maybe some stone |
| 9 | Roof | Open |
| 11 | Pumps | One big pump + manifold |
| 12 | Power | 120V exists on the dock near the spot |
| 13 | Permits | Not going to the attorney; handle ourselves (ODFW screen self-cert + a Water Resources check are still worth 2 phone calls) |
| 14 | Timing | After the V2 private sauna build |
| 15 | Name | Undecided, wants more ideas (see section 6) |
| 16 | Oslo | The Well (Kolbotn) has a rain / waterfall room; use as reference |
| 17 | Product | Not a sellable product, just for us |

Open: name (6), weir/pipe details (4), exact spot on the deck relative to the lounge, Grant's number.

---

## 1. The reference: utase-yu

Japan's onsen have had this for centuries. **Utase-yu** (打たせ湯, "striking water") is water released from height so the pressure of the fall massages shoulders and back. The bather sits on a low stool or ledge under it. Facilities usually run 2-4 spouts side by side so a group can sit under them together. The stated caution in the Japanese guides: don't sit under a strong stream too long, it goes from massage to tension. That argues for the timer as a feature, not just a water saver.

Ours is the cold version. There's no widely known cold utase-yu in the US that I could find in a first pass, which is the story: a Nordic cold plunge crossed with a Japanese waterfall bath, on the Columbia.

Sources: samurai-sauna-magazine.com utase-yu guide, japan-guide.com onsen types, Wikipedia "Onsen."

## 2. Experience design (proposed)

- **Three falls, three characters** (decided): 
  - *The sheet*: a wide weir, ~18-24" lip, ~7 ft up. Full-body curtain, the gentle one, and the photo.
  - *The column*: a vertical 1.5" downpipe from ~9 ft. Narrow, heavy, the utase-yu shoulder massage. Sit on the ledge, back to it.
  - *The jet*: a pipe angled ~30-45 degrees from the wall at ~6 ft, so water arrives at an angle across the back/neck instead of straight down. Standing. A ball valve on this branch sets how hard it hits.
- Utase-yu cue: guests turn their back to the column, not their face. A small sign or a bench that only fits one way solves it.
- **Trigger:** a big push button (decided). One press = one 180-second cycle (decided), timer relay, adjustable. Cycle ends, falls stop, silence. The theatre of turning it on is half the product. Three minutes under the sheet at 45F is a long time in January; that's the point, and guests can step out.
- **Seating:** a cedar or basalt ledge under the two lower falls; standing under the tall one.
- **Floor:** open-grate or slatted so water goes straight back to the river. No basin to keep clean.
- **Enclosure:** three walls + open river side, no roof (decided). Moss wall with some stone (decided). Guest steps in from the deck, it's a different room. Rain falls into it, which is on-brand.
- **Sound:** falling water on grating is loud. Good inside the enclosure, might be a nuisance to the sauna next door. Enclosure walls help.

## 3. Placement options on the docks

| Option | Where | Pro | Con |
|---|---|---|---|
| A | V2 platform, the enclosed "pool" already earmarked as future private cold plunge | Private-sauna upsell; gate already planned; fresh build, so Grant can frame it in | Adds scope/weight to a build already fighting the mid-Oct date; only private guests get it |
| B | Public deck near the existing Downpour | Every guest gets it; content machine next to the proven Downpour reel | Existing deck, retrofit framing; noise near the main sauna |
| C | Its own small float, tied alongside | Isolates weight and noise; can move it | Another float, gangway, mooring; TC Diving scope |

**Decided: B, near the lounge.** Next: pick the exact footprint. Constraints to check on site: distance to the nearest 120V outlet, clear water under the intake spot (no float or log directly below), which wall of the lounge it shares (noise), and where the button lands so it's visible from the sauna door.

Weight note: pumps and water column are trivial. The enclosure is where the pounds go, especially if it's stone. Same float-balance story as V2. Give Grant + TC Diving a number before committing to basalt.

## 4. Water system

**Source:** Columbia River, straight from under the dock. Non-consumptive: it falls back into the river.

**Intake:** submersible pump hung off the dock in a screened cage, 3-4 ft below surface (above silt, below the warm skin in summer). ODFW's small-pump screening criteria (self-cert form): perforated openings 3/32" max, approach velocity 0.2 ft/s or less for a passive screen, 27% open area. At our flow that's a screen box roughly 2 ft x 2 ft x 1 ft. Cheap to do right; also keeps the pumps from eating debris. Whether we technically need a water-use permit for a non-consumptive pump is unknown to me and should go to Oregon Water Resources Dept or the attorney (see Q13). Do not assume it's exempt.

**Flow sizing (standard pond-industry rule):** 100 GPH per inch of spillway width for a sheet, 200 GPH/in for a heavy "Niagara" fall. Massage needs the heavy end. Working assumption:

| Fall | Width | Target flow at the lip |
|---|---|---|
| Low sheet | 12" | ~1,500 GPH |
| Mid massage | 6" | ~1,200 GPH |
| Tall column | 4" | ~1,000 GPH |

Rated pump GPH is at zero head. At 8-10 ft of lift plus hose losses, a "5,000 GPH" pond pump delivers roughly 3,000-3,500. **Decided: one big pump + manifold.** Sizing: ~3,700 GPH total at the lips, at ~9-10 ft head plus manifold losses, wants an 8,000 GPH class pump.

| Pump | Rated | Watts | Max head | Notes |
|---|---|---|---|---|
| **Pond Boss 8000 GPH (PW8000)** | 8,000 | 600 | 29.5 ft | Asynchronous, vortex impeller, 20 ft waterfall rated. Lowes/Amazon stock. Cheapest of the three. **Pick.** |
| Aquascape AquaSurge 4000-8000 | 7,793 | 660 | 28 ft | Adjustable flow by wireless remote. Nice, but the ball valves already do that job; roughly double the price. |
| EasyPro TB8000 | 7,800 | ? | high head, stainless | Commercial grade; consider if the Pond Boss dies early. |

Manifold: 2" from the pump up to the header, tee to three branches, a PVC ball valve on each so the sheet/column/jet get tuned once and left. Buy one spare pump; when it fails in February you want a swap, not a shipping wait. Energy: 600 W x 3 min = 0.03 kWh per cycle, call it a penny. Fifty cycles a day is nothing.

**Pump candidates (pond/waterfall class, all pass 1/4" solids, all 120V):**
(5,000 GPH class, kept for reference only, too small for three falls on one pump: HydroFlow 5000 354 W / Pond Boss PW5000 230 W / Jebao APP-5000.) Prices need confirming at order time.

**Why not a real cold-plunge chiller pump:** we're not chilling anything. The river is the temperature it is. If we ever want colder water in August (Columbia surface runs high 60s to ~70F in late summer), that's a chiller + closed loop + insulated reservoir, a completely different and much more expensive machine. Park it.


**Sheet height ceiling (Davey Q, 2026-09-24):** sheet is max 2 ft wide (decided). A 2 ft sheet at ~2,000 GPH is ~0.5" thick at the lip, breaks into drops within 2-3 ft of fall, and those drops hit terminal velocity (~25-30 ft/s) around 10-12 ft of fall. Above that: no harder, only wider, more mist, more wind drift, less pump flow. Hardness is flow x velocity and velocity is capped, so to hit harder, pump more water, not higher. Recommend 7-8 ft lip; 10 ft is the ceiling worth building. Column (pipe jet) stays coherent longer and hits harder than the sheet at any height.

**Plumbing:** 1.5" or 2" flex PVC from pumps to a header on the enclosure roof, then a weir box per fall (a plastic waterfall spillway box, or a cedar trough with a straight lip). Straight-lip weir = clean sheet. Notched lip = ropes of water, hits harder. The tall column can be a plain pipe outlet.

**Control:** momentary push button (decided) into a 180 s delay-off timer relay (or a Shelly-type smart relay with auto-off) into a contactor for the pumps. GFCI on everything, it's 120V on a wet dock over the river. Electrician (Neil at Boones Ferry, already on V2) should spec the circuit. Winter: pumps stay submerged so they don't freeze; the above-water header needs to drain when off, so slope it back to the pumps or add a drain-down valve.

**"Saves water" honestly:** it's river water going back to the river, so the timer saves electricity, noise, and pump life, not water. Fine to say "on demand" in copy; don't say water conservation.

## 5. Enclosure

Davey + Jonah want mossy walls. What holds up in a splash zone on the Columbia:

- **Living moss, PNW native, on rough substrate.** Moss colonizes rough, shaded, constantly damp surfaces on its own here. Basalt or split cedar shake in the splash zone, shaded, and it will green up within a season or two. Seed it with sheet moss / Oregon native moss (Kindbergia, Dicranum) pressed into the substrate. Cheap, gets better with age, and it's the actual Gorge look.
- **Commercial exterior moss panels** (e.g. Moss Acres 4x4 exterior panels on capillary mat). Turnkey, but every guide says moss walls want rain/distilled water, misting every other day, and no direct sun. Constant river-water splash and summer sun on the open side will stress panels. Use them on the dry back wall only, if at all.
- **Preserved moss:** indoor only. Dies wet. No.
- **Alternatives / hybrids:** sword ferns + moss in a living wall on the shaded wall; black-stained cedar slats (matches V2 exterior) with moss allowed to take the base; corten steel back panel behind the falls (rust + water is a look, and it drains). Basalt column stack at the tall fall is the most "Gorge" but the heaviest.

**Decided: moss wall, maybe some stone, open top.** Proposed build: the wall behind the falls is the moss wall, stacked basalt or rough split cedar shake, seeded with PNW native moss and kept wet by the falls themselves plus a drip line on a timer for dry weeks. Side walls black cedar slats to match V2, moss allowed to take the bottom third. Stone only where it earns it (behind the column, under the sheet) because of float load. Skip commercial panels.

**The Well reference (Kolbotn, from Davey's Oslo tour):** their themed shower rooms include a Waterfall and a "rain" experience, and waterfall grottos. Worth pulling any photos/video Davey took for Grant and Kyle: what the walls were made of, how the water landed, how the drain was hidden.

## 6. Name

Wants to sit next to "The Downpour" (definite article, one water word). Davey wants more ideas (9/23). Grouped:

**Nordic (matches the brand's Nordic ritual positioning, and the Oslo trip)**
- **The Foss** — foss = waterfall in Norwegian and Icelandic (Gullfoss, Vøringsfossen). Four letters, ownable, and the origin story writes itself: went to Oslo, came home with a foss. My first pick.
- **Fossen** — "the waterfall." Same idea, softer.
- **The Regn** — rain. Weaker, sounds like "reign."

**Columbia / Gorge**
- **The Cascade** — Cascade Range, Cascade Locks, literally what it does. Safe pick.
- **The Spillway** — Bonneville is 40 miles upriver; a spillway is exactly this, river water going over a lip on purpose. Industrial Columbia, very Portland.
- **The Tailrace** — the water leaving a dam. Obscure, tough.
- **The Freshet** — the spring snowmelt surge on the Columbia. Beautiful word, needs a sign to explain it.
- **Horsetail** — a real Gorge falls, and "horsetail" is the technical name for a fall that stays in contact with the rock, which is what the angled jet does. Sneaky-good.
- **Bridal Veil / Latourell / Elowah / Wahclella** — Gorge falls names. Elowah and Wahclella are Indigenous-origin words, so I'd leave those.

**Plain English, Downpour family**
- **The Falls** — strong in copy ("under the falls"), generic to own.
- **The Torrent** — hard, matches the column.
- **The Deluge** — the Downpour's big brother. Maybe too much.
- **The Spill** — short, playful.
- **The Squall** — weather word, sits right next to Downpour.

Shortlist I'd put to Jonah: **The Foss, The Spillway, The Cascade.** Whichever wins, the three falls can carry their own small names on the button plate (Sheet / Column / Jet, or Foss / Fall / Rain).

## 7. Rough cost (ballpark, unpriced)

| Item | Ballpark |
|---|---|
| 8,000 GPH pump + spare + screen cage + 2" manifold + weirs | $1,000-1,600 |
| Controls, GFCI circuit, electrician | $800-2,000 |
| Enclosure framing, cedar, roof, grating (Grant) | $4,000-10,000 depending on stone |
| Moss/plants/basalt | $500-2,500 |
| Floats if needed (TC Diving) | ? |

Rough guess $7-16K all-in, dominated by carpentry. Get Grant's number before believing any of it. Do not price the guest experience until this exists.

## 8. Regulatory / safety flags (to confirm, not assumptions)

- Pump intake screen: ODFW small-pump criteria, above.
- Non-consumptive river pumping: check with Oregon Water Resources Dept whether a permit or exemption applies.
- DSL lease / marina lease: does adding a structure need marina landlord OK? Same question as V2.
- Water quality: falling water aerosolizes. After heavy rain / CSO events the City advises no contact for 24-48 hrs on parts of the Willamette; check what applies at our Columbia location and whether we already have a rain-day rule for the plunge.
- 120V over water: GFCI everything, licensed electrician, cord management.
- Slip hazard: wet grating + bare feet. Grippy grating, handrail under the tall fall.

## Still open (for Davey / Jonah)

1. **Name:** The Foss, The Spillway, or The Cascade? (Or another from the list.)
2. **Exact spot** by the lounge: which wall, and is the water below it clear for the intake?
3. **Sheet width:** 18" or 24"? (24" wants a bigger share of the pump.)
4. **Jet angle:** aim for upper back/neck (steeper) or across the shoulders (shallower)?
5. **Ledge:** cedar bench under the column, or a basalt slab?
6. **Photos from The Well:** anything to file in Assets/ for Grant and Kyle?
7. **Who runs the ODFW screen self-cert and the Water Resources call:** me, or Jonah?

## Next steps

- [ ] Davey: name + spot + The Well photos
- [ ] Claude: sketch/mockup of the enclosure and three falls once the spot is known
- [ ] Claude: BOM with live prices (pump, spare, screen, manifold, weir, timer relay, button, GFCI)
- [ ] Grant: framing + weight number after V2 wraps
- [ ] Neil: circuit + control spec
- [ ] ODFW self-cert form + one call to Oregon Water Resources re: non-consumptive pumping
