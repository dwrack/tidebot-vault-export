# The Rose: Session Plan

_2026-09-29. How we split the Rose into focused working sessions, one per element of the flower and one per project area, without them stepping on each other. Draft for Davey to walk through. Nothing is spun up yet._

---

## Why a plan first

Today showed the risk. Two sessions edited the same model at once (v0.30 to v0.33 glass work in one, the lap in another). Version numbers collided, and the v0.34 ramp was a technical fix that took over the flower. Ten sessions editing one file would be worse. So each session needs its own workspace, one owner for the main model, and a fixed shape it isn't allowed to break without asking.

## The shape of it

**One hub, many rooms.**

- **The hub (this session).** The only session that edits `The Rose - 3D Model.html` and bumps its version. It holds the vision, keeps the whole-flower silhouette honest, and folds approved work from the rooms into the main model.
- **Element rooms (the flower).** One session per piece of the building. Each gets its own study folder and its own study page. It goes deep there: form, dimensions, materials, how people use it, and what it costs.
- **Project rooms (the business).** One session per area of the Master Plan: site, engineering, permits, money, brand, operations. These mostly write documents, not 3D.

## Element rooms

| # | Room | Covers | Starts from |
|---|---|---|---|
| E1 | Hot room | Tiers, pit, pistil stove, acoustics, drapes, the 12-minute round, the sensory layer | Brief s.4-7, Interior acoustics plan |
| E2 | Crown | Roof lounge, fire circle vs hearth, seating, dance floor, parapet petals, crown sound | Crown and DJ Booth Spec s.0-13 |
| E3 | DJ booth | Nested booth, show desk, petal canopy, leaded rose window, rain and gear | Crown spec s.7, v0.30-0.33 glass work |
| E4 | Jump petal | The climb, the 20 ft tip, climbing wall, how it lands on the crown, water depth. **First fix: the gap between the wall and the flower** (candidate saved in `Iterations/_candidates/`) | v0.12-0.26 changelog |
| E5 | Slide petal | The fallen-petal shape, channel, launch, exit, depth, rubber vs GFRP | Materials Plan, brief s.10 |
| E6 | Amphitheater petals | The three step bowls, the glass bridge petal, fire roses, jump rims, lounge seating | Brief s.17, round 3 decisions |
| E7 | Calyx and sepals | The float's look above water, sepals, kids' sepal slide, swim ladders | v0.16, v0.19 |
| E8 | Stem, leaves and gangway | Stem walkway, compound leaves, boat tie-ups, thorns, gangway and dock landing | v0.18-0.19, v0.29 |
| E9 | Skin, color and light | Petal material, deep rose palette, the night glow, stained glass across the flower | v0.24, v0.25, v0.30 |

**Access is not its own room.** Every element room follows the rule that code gets met out of sight. Stairs, lifts and exits get proposed in words to the hub first, never drawn straight onto the flower.

## Project rooms

| # | Room | Covers | Starts from |
|---|---|---|---|
| P1 | Site and City | Holman strategy, LOI, DSL lease, soundings, current, mooring without new piles, the Bud and future sites | Master Plan s.2 |
| P2 | Engineering and code | Naval architect shortlist, stability, occupancy and exits, gas certification, electrical, lightning | Master Plan s.3 |
| P3 | Permits | BDS pre-app, the permit path and timeline | Master Plan s.4 |
| P4 | Money and funding | Budget, Parts Catalog and raise stack, community funding, the Elevated Tides mark and entity blocker | Master Plan s.6, Funding Plan, Parts Catalog |
| P5 | Brand, name and pre-sale | Name clearance, social pre-sale with Jordan, the iteration video | Master Plan s.7, brief s.12 and s.20 |
| P6 | Operations | Program, staffing, events and DJ series, the ops trailer, commission curation | Master Plan s.8, brief s.21 |

Materials and fabrication (Master Plan s.5) splits across the element rooms, since each piece has its own materials.

## How each room works

1. **Its own folder:** `Operations/The Rose/Elements/E4 Jump Petal/` (or `Areas/P1 Site/`), holding:
   - `README.md`: what this element is, decisions made, open questions, dimensions
   - `CHANGELOG.md`: Davey's words and what changed, every round
   - a study page: that one element in 3D, in the drawing-set style and the model style, with its neighbors shown ghosted for context
   - `Iterations/`: every version kept, for the video
2. **An envelope it can't break alone.** A shared file, `Elements/Interfaces.md`, fixes where each element sits, its footprint, its height band and where it touches its neighbors (for example, the jump petal lands on the crown rim at about 34 degrees, 3.66 m above the river). Changing an envelope means asking the hub first.
3. **It never edits the main model.** When Davey approves a round, the room writes a short hand-off: what changed, the geometry code, and renders. The hub folds it into the main model as the next version, checks the whole-flower view, and publishes.
4. **Same rules everywhere,** written into every room's opening prompt:
   - Form over code
   - Keep every iteration
   - Holman stays off the record on anything public
   - Deep rose red palette
   - The stove is gas-fired, never wood
   - Ebb & Ember is spelled with the ampersand
   - No em dashes
   - Show Davey drafts before anything goes out
5. **The project rooms write documents.** They read the element rooms' READMEs but don't touch geometry.

## What the hub does next, once you approve

1. Write `Interfaces.md` with every element's envelope, measured from v0.33
2. Create the folders and seed each README from the brief, the changelog and the specs
3. Write each room's opening prompt so it stands on its own
4. Spin up the rooms you pick, as chips you click to open
5. Keep the main model on v0.33 until the first hand-off comes back

## Decisions for Davey (answer by number)

1. **Element list.** Are E1 to E9 the right cut? Merge or split any (for example, make the glass bridge petal its own room, or fold E9 into the others)?
2. **Project rooms now or later?** Open P1 to P6 alongside the design rooms, or keep design first and open the business rooms in a few weeks?
3. **Study page style.** Model look, drawing-set look, or both side by side (my pick: both)?
4. **Start order.** All at once, or three first? My pick: E4 jump petal (it has a live bug), E2 crown, E6 amphitheaters.
5. **Who approves envelope changes?** You, with the hub drafting the tradeoff, or the hub, which only brings you the big ones?
