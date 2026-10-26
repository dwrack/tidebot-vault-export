# The Rose: 3D Print Spec (Oct 2026)

_2026-10-15. Print-ready two-piece model of the full Rose: a base with the whole interior, and a roof crown that lifts off. Files, scale, print settings, assembly, and the list of design items still open before (or after) printing. Confidential: Holman stays off the record. Davey hands files to Ben; nothing here goes out from Claude._

Files live next to this note in `Operations/The Rose/3D Print Model/`. Generator: `make_rose_stl.py` (v0.5). Old Sept 26 files (v0.4) are in `_v0.4_archive/`, history only.

---

## 1. What changed from the Sept 26 files (audit)

| Check | v0.4 (Sept 26) | v0.5 (now) |
|---|---|---|
| Watertight | No. Every part was a pile of overlapping shells; base had 41 inverted faces, roof 720 zero-area triangles, petals 15,260 non-manifold edges | Yes. Each part is ONE boolean-unioned solid (manifold3d). Script prints a watertight / single-body check per part |
| Roof registration | None. Roof plate just sat on the wall tops | 3 pins on the base (on the door lintels) drop into 3 pockets under the roof plate. Seats with 0.0 mm3 overlap (checked by boolean intersection) |
| Interior with the roof off | Tiers, pit, altar, pistils, aisle steps, 3 doors, bridge window | Same, cleaned up: tiers overlap into each other (no sliver cavities), pistil tubes thickened to a printable 1.4 mm, guard rail ring kept |
| Petals | v0.4 flat open petals + separate outer "fire cups" as their own STL (stale since v0.9) | Amphitheater petals (viewer v0.9+), unfurl rim, fused to the base. Jump petal spirals onto the crown as in the viewer (v0.26/v0.41) |
| Roof form | Tall closed bud (drum to 4.2 m, oculus 4.8 m), stale since v0.10 | Low crown lounge (deck at 3.0 m, parapet petals, two-layer bud skirt, vent stack), matching viewer v0.52. `--roof bud` still builds the old one |
| Slide | "Stem slide" launching from the roof (v0.4 idea, superseded by decisions 39 and 76) | Slide petal P2, the fallen-petal form (viewer v0.17), as a snap-on part with 2 pegs |
| Stem and leaves | 3 leaves hanging off the old roof slide | Stem landing on sepal G2 (v0.45) with a socket; chainable stem segments; one compound-leaf module that pegs into the stem |
| Orientation | Mirror image of the viewer (the old writer skipped the v0.26 compass flip) | Matches the viewer. North marker = small raised tab on the hull under the bridge window (petal 0 faces the Hawthorne) |
| Sepals | Not in the STL | Four curling sepals, kids' sepal slide at G6 (12 degree ramp), flat stem landing at G2 |

Verified 2026-10-16 by script (after the ramp fix): all 5 parts watertight, 1 body each, base/roof overlap 0.0 mm3, base/slide overlap 0.0 mm3. Check renders (colored, with 1.7 m scale figures): `Check Renders/c1_jump_petal_stair.png`, `c2_landing_on_crown.png`, `c3_assembled.png`, `c4_interior_roof_off.png`.

## 2. The pieces

| File | What it is | Prints as | 1:100 (mm) | 1:75 (mm) | 1:50 (mm) |
|---|---|---|---|---|---|
| `rose_base_interior.stl` | Float, calyx, sepals, pit, 3 tiers, 3 aisles, stone altar with 12 pistils, guard rail, hot-room wall with 3 doors and the bridge window, fire rings, 3 amphitheater petals, jump ramp petal with climbing wall, stem landing, 3 roof pins, 2 slide sockets, north tab | Flat on its hull, one piece | 172 x 191 x 60 | 229 x 255 x 80 | 343 x 382 x 120 |
| `rose_roof_crown.stl` | Ceiling plate, drum, crown deck, 9 parapet petals (gap where the ramp lands), 2-layer bud skirt, stove vent stack, 3 pin pockets underneath, notch carved for the jump ramp | Plate down, crown up | 97 x 95 x 21 | 129 x 126 x 28 | 193 x 190 x 43 |
| `slide_petal.stl` | Fallen-petal slide P2 with heel block, 2 pegs, 2 legs to the table | Legs down, as modeled | 74 x 67 x 44 | 99 x 89 x 59 | 148 x 134 x 89 |
| `stem_segment.stl` | 12 m of the 1.5 m stem walkway. Peg one end, socket the other, 2 leaf sockets on the swim side. Print several and chain them | Flat | 120 x 15 x 7 | 160 x 20 x 8 | 240 x 30 x 12 |
| `leaf_module.stl` | One compound leaf: stalk + 5 leaflets. Pegs into a stem socket. Print 4 (decision 45: four leaves, five leaflets each) | Flat | 106 x 113 x 8 | 142 x 150 x 9 | 212 x 225 x 13 |
| `the_rose_1-75.3mf` | All five parts in one 3MF, laid out side by side, mm | | | | |

Ready-made sets: `3D Print Model/` = 1:75 (default). `3D Print Model/1-100/` = 1:100. Any other scale: `python3 make_rose_stl.py --scale 50 --out 1-50`.

Pegs and pins are print-scale, not design-scale: pins 2.4 mm dia x 3 mm, pockets 2.9 mm; pegs 3.0 mm x 4 mm, sockets 3.5 mm. Thinnest printed skin is 1.4 mm at any scale (`MIN_T_MM`), so sepals, pistils and parapets stay printable at 1:100.

## 3. Scale: pick one

The base is the widest part: the flower with petals is about 19.1 m across the jump-petal axis at full size (the float itself is 15.0 m). Bed needed = 19,100 / scale, in mm.

| Scale | Base footprint | Float dia | Tier rise | Wall | Fits a 180 mm bed (Bambu A1 mini class) | Fits 220-256 mm (Ender 3, Prusa MK4 250x210, Bambu P1/X1 256) | Service printer (SLA 300-580 mm) |
|---|---|---|---|---|---|---|---|
| 1:100 | 172 x 191 | 150 | 4.5 mm | 2.2 mm | No (191 > 180). 1:110 does: 174 x 174 | Yes | Yes |
| 1:75 | 229 x 255 | 200 | 6 mm | 2.9 mm | No | No (255 is past a 256 bed once you add a brim). 1:80 = 239 fits a 256 bed | Yes |
| 1:50 | 343 x 382 | 300 | 9 mm | 4.4 mm | No | No | Yes (JLC3DP SLA bed 580 x 580 x 380; Craftcloud partners vary) |

Bed-size cutoff for Ben: ask for his bed's X and Y. 180 mm bed = print 1:110 (`--scale 110`). 220 mm or bigger = 1:100. 256 mm = 1:80 is the largest that fits. Anything bigger than 1:80 is a service job.

**Recommendation:** two prints, not one.
1. **1:100 on Ben's printer now** (or 1:110 if his bed is 180). Cheap, a weekend, and it proves the two-piece idea in your hand. Interior detail is still readable at 1:100 (benches 6 mm wide, 4.5 mm risers, pistils 1.4 mm).
2. **1:50 resin from a service for the January activation and the City.** 300 mm float, benches 12 mm wide, a model you can walk a council member around. Order it only after the Section 5 items that change the shape are settled, since a resin hero print is the expensive one.

Leaves, stem and slide print as separate snap-on parts at every scale. They are the modular bits in the design (Oct 15 call: core is one structure, leaves and the slide petal are modular), so showing them as removable is honest. The roof lifts off; the slide pulls out; leaves plug into the stem; the stem plugs into the landing.

## 3b. Printing big on a small printer (added 2026-10-17)

Any scale now prints on any bed. The generator cuts every part that is too big into a grid of pieces, drills matching dowel sockets on both sides of every cut, and writes a loose `dowel_pin.stl` (3 mm x 8 mm). Print the pins, push the pieces together, and add a drop of glue on the base and roof seams. The roof still lifts off as one piece once its quarters are pinned.

```bash
python3 make_rose_stl.py --scale 50 --out 1-50 --bed 180
```

Ready now: `1-50/split_bed180/` (1:50, sized for a 180 mm bed, the smallest common hobby bed). Checked by script: every piece is a valid solid, fits 174 mm, and every separate chunk in a piece has at least 2 dowel sockets.

| Bed | Base | Roof | Slide | Leaf (each, print 4) | Dowels |
|---|---|---|---|---|---|
| 180 mm (built) | 6 pieces | 4 | 1 | 4 | 34 + 2 spares |
| 220 mm (arithmetic, run `--bed 220`) | 4 | 1 | 1 | 2 | fewer |
| 256 mm (arithmetic, run `--bed 256`) | 4 | 1 | 1 | 1 | fewer |
| **305 mm, Ben's bed (12 x 12 in, confirmed 2026-10-17), built** | **4** | **1** | **1** | **1** | **10 + 2 spares** |

Three crumbs under 400 mm3 (pistil tips and a rail sliver where a cut crosses the pit) print as loose bits: glue them or skip them.

Material at 1:50, est.: about 3,500 cm3 of solid model, so roughly 1.5 kg of PLA at normal infill ($25-40 of filament) and several days of printer time spread over the pieces. Estimate only, Ben's slicer gives the real number.

**Recommendation now:** send Ben `1-50/split_bed305/`. Base in 4 pinned quarters; roof, slide petal, stem segments (print 3) and leaves (print 4) each print whole. Checked: every file a valid solid, all fit 299 mm, each base quarter carries 4-6 dowel sockets. Loose bits to glue: a few pistil-tip crumbs and one small 3 cm3 chunk in quarter B2.

## 4. Print paths (estimates, verify with a quote)

| Path | What to send | Material and settings | Rough cost | Turnaround | Notes |
|---|---|---|---|---|---|
| **Ben's small printer** (recommended first) | The `1-100/` folder: 5 STLs or the single 3MF. Tell him the bed size cutoff above | PLA (or PETG). 0.2 mm layers, 0.4 nozzle, 3 walls, 15-20 % infill. Base: flat on the hull, no supports needed except tree supports under the jump ramp ribbon and the curling sepals. Roof: plate down, tree supports under the bud skirt. Slide: legs down, supports under the blade. Stem and leaf: flat, none. Brim on the roof and slide | ~150-250 g filament, call it $5-10 of material | 12-20 h of printing across the parts, so 1-3 days of his evenings | A 1:100 base is a 6-8 h print on its own. If his slicer flags thin walls on the parapet petals, let it thicken them; they are decorative |
| **Portland shop / library** | Same files | FDM or SLA | Multnomah County Library 3D printing is free (Albina 3D lab, Rockwood programs) but in person only, program signups open 3 weeks ahead, no remote jobs: too slow for this. Protolabs Network (hubs.com) lists Portland partners with instant quotes; JawsTec quotes "architecture" but prints in Idaho and ships (about 2 days to Portland ZIPs) | Shop: days to 2 weeks | Good if you want to pick up a 1:50 resin print locally. Ask for SLA grey resin, 50 micron, light sanding, no paint |
| **Online service** (recommended for the hero) | 1:50 set (run `--scale 50 --out 1-50`) | SLA resin (grey or white) for the base, roof and slide; FDM or SLS nylon for stem segments and leaves (they are flat and take knocks) | Brief section 8 estimate: $150-600 at 1:50 resin, more with finishing. JLC3DP lists SLA from $0.30 with 2-day build, FDM from $1.00 with 3-day build (starting prices, not this model). Expect $150-400 for the five 1:50 parts before shipping; paint adds 15-20 % after JLC's July 2026 price change | Build 2-3 days plus 1-2 weeks shipping from JLC3DP; Craftcloud partners vary by region | Upload the same files to Craftcloud and JLC3DP, choose SLA and FDM for each, and compare. Check the quote includes supports removal and shipping |

Resin vs FDM: resin for the base and roof (smooth tiers, crisp pistils, parapet petals hold their edge); FDM is fine for the stem and leaves, and for the 1:100 test. Do not paint the hero print; grey or white resin reads as a model and photographs well next to the Airstream.

## 5. Finalize before printing

Status key: **decided** = settled in the docs and in the print; **open** = not decided; **print-safe** = not decided, but the print's guess doesn't mislead anyone and can change in the script later.

| # | Item | Status | Print shows | Source |
|---|---|---|---|---|
| 1 | Interior: 3 tiers (r 2.0-2.6, 2.6-3.2, 3.2-3.75 m), 45 cm rise, pit 0.6 m deep | decided (model v0.2, viewer P block) | Yes | Brief section 4 still lists older tier radii (1.70-2.35 etc.); the viewer numbers win |
| 2 | Stove: one gas stone altar on the pit floor with 12 pistil stamens | decided (decisions 2, 15) | Yes | Brief section 6 |
| 3 | Stepped aisles from each door to the pit | print-safe (3 aisles drawn; the viewer still lacks them) | Yes | Pathways section 3: aisles cost ~6-9 seats, realistic count 48-51 |
| 4 | Capacity: design to 49 or accept assembly code at 50+ | **open** (Jonah, Oct 15 call; ~57 seats drawn) | Nothing to show either way | Team call notes item 18 |
| 5 | Inverted crown on the hot-room ceiling (decision 74) | open, print-safe to skip | Not modeled; it is inside the roof and never seen on the model | Brief section 22, Crown spec section 15 follow-up |
| 6 | Doors: 3 x 0.9 m at clefts D1-D3, bridge window at petal 0 | decided for now | Yes | Decision 5 |
| 7 | Door concept: vestibules in P6/P7, a ~1.8 m round-change petal door, which side | **open** (decision 76, Davey not sure) | 3 plain doors | Pathways section 8, Master Plan section 9 |
| 8 | D3 pile-up (door + kids' slide + ramp foot in one cleft) and the inner lane | **open** (Pathways decisions 1 and 2) | Print pulls the ramp foot out of the cleft so it clears the wall; kids' slide stays at G6 | Pathways sections 0 and 2 |
| 9 | Petal count: 5 petals, 5 sepals | decided (decisions 4, 44) | Yes | |
| 10 | Petal character (Unfurling vs Wild A/B/C) | open, print-safe (print = unfurl rim; `--petals classic` for the other) | Unfurl | Master Plan section 1 |
| 11 | Crown layout: flat deck vs sunken fire circle vs terraced bowl; hearth arc; DJ booth nested south rim; service stair | **open** (decision 33, Crown spec decisions 1-3) | Flat deck with parapet petals, no booth, no stair | Crown spec |
| 12 | Jump petal: ramp spiral onto the crown as the only way up (decision 69) | decided; climbing holds not printed | Stepped petal stair + climbing wall back | Reworked 2026-10-17 after Davey's check: the viewer's geometry is a 150% grade at the foot and narrows to 1.0 m on a 51% downgrade, which nobody can walk. The print is now one stepped stair-ribbon: foot at deck level by the jump-petal fire, 2.6 m wide, 0.17 m risers up to the 5 m jump platform (held flat ~2 m), then risers down through the parapet gap to land flush on the crown deck, never under 1.3 m wide. Roof carries a slot so it lifts clean. Design still owes a real decision: stair (as printed) vs the 1:12 lap in Crown spec section 14. Foot lands in the D3 cleft, which is the open pile-up (item 8) |
| 13 | Slide: one slide petal P2, removable | decided (decisions 39, 76; Oct 15: removable) | Snap-on part, v0.17 fallen-petal form | The 2026-09-30 group stair and curled exit (v0.48) are NOT in the print yet; the heel is not pushed out 1.2 m |
| 14 | Leaf count: 4 compound leaves, 5 leaflets, L2 is the boat leaf | decided (decisions 45, 71) | One leaf module, print 4 | Leaflet width 2.0 m is an assumption (viewer records 4.8 m length only) |
| 15 | Walkable leaf stalks | **open** (Pathways decision 5) | Stalk is a 0.3 m tube | |
| 16 | Stem: starts at the G2 landing, no railing, walkway to the last leaf, boom on to the fire pier (~150 m) | decided (decisions 43, 47, 55, v0.45/46); full-length emergency route **open** (Pathways decision 4) | Landing + 12 m segments; print as many as the table allows | A 150 m stem is 1.5 m long at 1:100, so the print shows 2-3 segments as a gesture |
| 17 | Base float outline: 15.0 m circle (R 7.5) in the model vs 14.0 m in brief section 4 vs the 55 ft target; and Rose 1.0 (~30 ft, Holman) vs full Rose | **open** (fork 2026-09-27) | Full Rose, 15.0 m circle | Rose 1.0 / the Rosebud is a separate smaller build (Jess's name, Oct 15) |
| 18 | Screen petals P6/P7, standing lounge G7, cold petal P5, rain cascade under the slide | open / requested, not in print | Not modeled | Master Plan section 10, decision 75 |
| 19 | Kids' sepal slide climb-out | **open** (lobes removed v0.44) | Plain ramp | |

Items 4, 7, 8, 11 and 17 are the ones that change the printed shape. For a 1:100 test print, ignore them and print. For the 1:50 hero print, settle at least 11 (crown) and 17 (float size), or accept that the hero shows today's answer.

## 6. Assembly

1. Base on the table, north tab (under the bridge window) toward the Hawthorne side of whatever you set it on.
2. Roof: line the three pockets up with the three pins on the door lintels. It only fits one way. Lift straight up to show the interior.
3. Slide petal: two pegs into the two sockets on the deck at petal P2 (southwest of the bridge window, between doors D2 and D3). Legs rest on the table.
4. Stem: first segment's peg into the landing socket at G2 (between the bridge petal and the west lounge, river side). Chain more segments peg to socket.
5. Leaves: peg into the stem's side sockets, leaflets toward the swim side.

If pins are tight after printing, a twist of a 2.5 mm drill in the pockets is the fix. If loose, a dab of PVA.

## 7. Changing the model

Everything is in `make_rose_stl.py`. Full-size dimensions in meters at the top (copied from the viewer's P block), print sizes in millimeters below them. `python3 make_rose_stl.py --table` prints the scale table. `--check` runs the seat test. Needs `pip3 install numpy scipy networkx trimesh manifold3d`; without them the script still writes STLs but as overlapping shells (slicers cope, services may not).

Not ported from the viewer (v0.52) and worth adding when decided: slide-petal group stair and curled exit (v0.48), screen petals and G7, rain cascade, DJ booth, crown fire circle or bowl, inverted ceiling crown, climbing holds, drapes, people.

Sources used for the print-path estimates (2026-10-15): [Protolabs Network Portland](https://www.hubs.com/3d-printing/oregon/portland/), [JawsTec Portland page](https://www.jawstec.com/3D-Printing-Service-Portland-Oregon.html), [Multnomah County Library 3D printer policy](https://multcolib.org/3d-printer-policy-makerspace), [JLC3DP](https://jlc3dp.com/), [JLC3DP July 2026 pricing update](https://jlc3dp.com/news/materials-finishing-pricing-update-july2026), [CGTrader service roundup, Feb 2026](https://www.cgtrader.com/blog/top-5-best-3d-printing-service-providers).
