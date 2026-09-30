# The Rose: Design Sync Audit

_2026-09-30. Checks every Rose doc and page against the day's changes: stem lands at G2 (v0.45), no stem railing (v0.46), land-side facilities (decided), cold side (requested), doors (undecided). 12 documents, one auditor each plus a skeptic who tried to refute every finding (141 findings confirmed, 72 rejected). Nothing has been edited yet; this is the fix list. Line numbers refer to the files as of 09:31; find each edit by its quote._

**Short answer: no.** The 3D model and the changelog are current. Every other Rose record is behind on at least one of today's changes. The worst problems:

- Design Brief decision 43 still starts the stem at the "Rose north edge".
- The Pathways doc still says the stem walkway starts "under P3, unreachable" and has a "rail on the river side".
- The Drawing Set still draws the stem rail.
- The Petal Lineup and Sizes pages (both published links) still show the old stem start on its hump, with the rail.
- Master Plan sections 9 and 10 and Pathways sections 8 and 10 write the undecided door concept, and P5 as the cold petal, as if they were decided.

## 1. Completeness

### The model is now v0.48, not v0.46
Other sessions shipped two more versions after the audit snapshot (the audit copies are from 09:31, the live file from 09:40):
- **v0.47:** P6 moved back 0.5 m onto sepal G3 and turned calyx green. The pocket between door D1 and P6, flanked by P4 and P5, is now **G7, a standing lounge** (~2.5 m deep, with a 42 in lean ledge).
- **v0.48:** the slide-petal group stair, launch pad and curled exit are merged into P2. The heel moved 1.2 m out from the hot room.

What that changes in the fixes below:
- **Doors (E):** the P6 vestibule proposal and "big door at D1 toward the cold side" now land in the G7 standing lounge, behind a wall. They no longer lead straight to the water.
- **Cold side (D):** Master Plan s.10's "split between P5 and the D1 pocket" would now take G7. G7 also sits in the same river-side zone Davey wants for the cold side. That's a new interaction to put to him.
- **Showers under P2 (D):** the push-out is built now, not proposed, so the headroom check is more urgent.
- **Version stamps:** every version fix below uses v0.48.

The audit copies match the vault byte for byte, with three exceptions: `The Rose - 3D Model.html` (v0.47 and v0.48 appended), `Iterations/CHANGELOG.md`, and `The Rose - Slide Petal Study (Sept 2026).md` (a hand-off section was added). Apart from the version strip and footer, the model page prose is unchanged since the audit, so every prose finding still stands. Its line numbers refer to the audit's `_model_page_prose.html`. In the live file, find each edit by its quote.

### Records the audit didn't cover

| Record | What it shows | Action |
|---|---|---|
| `Operations/The Rose/The Rose - Site Overlay (Holman-Kerr Dock).png` (the model page embeds a copy as `rose_site_overlay.png`) | Stamped v0.18. Stem goes straight north from the Rose's north edge; "North petal: glass base"; all 4 leaves on the swim side | Regenerate (R1) |
| `Renders/The Rose v0.24 - *` (9 stills + flythrough mp4), `Renders/Drawing Set v2/*.png` (v0.33) | Old stem start and the river-side rail | Keep as history. Don't use them in the Jordan pack or on social |
| `Renders/Slide Petal Study/*` + `Blender/The Rose - Slide Petal Study.blend` | Stem on the wrong side, looping around the cove | Re-render or caption (R5) |
| `3D Print Model/*.stl` (5 files) | v0.4 roof-top slide stem | History, label only |
| Claude memory `project_the_rose_sauna.md` (outside the vault) | Stops at v0.42; the MEMORY.md index says v0.21. Missing v0.43-v0.48, C, D, E | Update memory (low) |
| `Operations/Strategic Plan - Oslo Offsite (Sept 2026).md` L189 | "Design far along (v0.28)" | Change to v0.48 (low) |
| `Operations/Building on the Water — Title 28 Brief (Sept 2026).md` | Current. Its float rules bear on F and B: walks 36 in wide on 2 opposite sides of a commercial float (28.06.060), 6 ft main walkway, 5 ft gangway, second gangway past 250 ft | Cross-reference only: the Pathways doc should cite it next to the "no flat lane" and "one gangway" findings, and next to the 1.5 m unrailed walkway |
| `Holman Dock/Holman Dock — Pilot Program Plan (Aug 2026).md` | Showers and changing in a gravel-lot trailer or building | Matches C. No action |
| Published copies: Rose (VPwztPdkTQfPb23vPh2yzz), Drawings (3YPJ5WeXQgorx8iH3AFLMW), Petal Lineup (T99tEHYyXiAS9PSg8cT4uA), Sizes (W9RF3nKMB3fnWVJ4Bh1PhY) | Fixing the local HTML doesn't update these links | Republish after the edits. Also confirm VPwzt is serving v0.48 |

Nothing else in the vault describes the stem, the rail, the land side or the cold side. The Waterfall Plunge brief, the Master Action List, the How-To Guides, Hiring, the Marina Site Plan and the City Floating Sauna folder don't mention them.

## 2. Fix list

Severity: **H** = contradicts today's change or presents the door concept / P5 as decided; **M** = a clear omission or stale state; **L** = secondary.

### text-edit

#### High

1. **Design Brief L67** (A)
   Find: `| 43 | Stem | **One boom, dock to dock:** Rose north edge to the fire station pier tip under the Hawthorne, ~150 m (v0.18). Two mooring points, plus mid-span anchors |`
   Replace: `| 43 | Stem | **One boom, dock to dock:** from the **stem landing on sepal G2** (flat, flush with the deck, between bridge petal P3 and west lounge P4, river/northwest side; v0.45) to the fire station pier tip under the Hawthorne, ~150 m (v0.18). The boom leaves the float at water level, runs out past P3's rim, then bends north. Two mooring points, plus mid-span anchors. Open: no flat deck route yet from the gangway (D2) to G2; the inner lane is a proposal (Pathways doc) |`

2. **Master Plan L170** (A)
   Find: `- [ ] **Stem root at G2** + fix the D3 / kids' slide / ramp-foot pile-up. Pathways doc, Fix 2.`
   Replace (two lines):
   `- [x] **Stem root at G2**: done in v0.45. The stem grows from the gap between P3 and P4; sepal G2 lies flat as the stem landing, flush with the deck (~1.45-1.6 m wide), out to the float edge where the 1.5 m walkway starts. Still open: no flat deck route from the gangway to G2 (the inner lane above would fix it).`
   `- [ ] **Fix the D3 / kids' slide / ramp-foot pile-up.** Pathways doc, Fix 2.`

3. **Master Plan L156** (E)
   Find: `### Doors: easy and quick to open, big enough to empty fast (the numbers are in the Pathways doc, section 8)`
   Replace: `### Doors: a proposal, not decided (Davey 2026-09-30: not sure yet). Goal: easy and quick to open, big enough to empty fast (numbers in the Pathways doc, section 8)`
   Add a line under it: `_Nothing below is a decision or in the model. Vestibules, a ~1.8 m petal door and which side it faces are all still open. Since v0.47 the D1 pocket is the G7 standing lounge behind the green wall P6._`

4. **Master Plan L171** (E)
   Find: `- [ ] **Doors in the model**: vestibules in P6/P7, big petal door on the cove side, stepped aisles inside, cold steps outside.`
   Replace: `- [ ] **Door concept: Davey to decide** (not sure yet, 2026-09-30). Options: vestibules in P6/P7, a ~1.8 m petal door for round changes, which side it faces (cove, or D1 toward the cold side; D1 now opens onto the G7 standing lounge, v0.47), cold steps outside. Nothing goes in the model until he picks. Stepped aisles inside the hot room are needed either way (Pathways section 3).`

5. **Pathways L27** (A+B)
   Find: `| Stem walkway | 1.5 m, ~120 m | Walk out to the leaves | **Starts under P3, unreachable** (fix: root at G2). Ends at the last leaf, so it's no route to land |`
   Replace: `| Stem walkway | 1.5 m, ~120 m, no railing (v0.46) | Walk out to the leaves | **Starts at the G2 stem landing (v0.45)**, flush with the deck. Still no flat deck route to it from the gangway (needs the inner lane, Fix 1). Ends at the last leaf, so it's no route to land |`

6. **Pathways L111** (B)
   Find: `| Stem walkway | 1.5 m x ~120 m walkable, rail on the river side |`
   Replace: `| Stem walkway | 1.5 m x ~120 m walkable, no railing: open both sides like a dock (v0.46, decision 47) |`

7. **Pathways L168** (E)
   Find: `- **The petal door: a round-change door.** ~1.8 m pair of leaves on the cove side, opened by the host at the end of each round, straight out to **cold steps** into the river. It's also the big egress door. A pair of petal-shaped leaves opening outward is a nice moment on its own: the flower opens and the round spills into the water.`
   Replace: `- **Option: a petal door for round changes.** A ~1.8 m pair of leaves, opened by the host at the end of each round, out toward the cold water. Which side it faces is open (decision 10): D1 toward the river-side cold features Davey asked for (Master Plan section 10; since v0.47 D1 opens onto the G7 standing lounge behind the green wall P6, not straight to the water), or the cove for swimmers. It would also be the big egress door. A pair of petal-shaped leaves opening outward is a nice moment on its own: the flower opens and the round spills out.`

8. **Pathways L192** (D, E)
   Find: `10. **Big-door side:** D1 (west) straight into the cold petal (my pick since the cold side moved to P5, Master Plan section 10), or the cove side?`
   Replace: `10. **Big-door side (only if there is a big door):** D1 (west), toward the river-side cold features Davey asked for (my pick; P5 as the cold petal is my recommendation, not a decision, Master Plan section 10; D1 now opens onto the G7 standing lounge, v0.47), or the cove side?`

9. **Materials Plan L43** (A)
   Find: `| **Sepals** | GFRP or printed ASA shells on the float edge, calyx green | Light, shaped | Fender function: they take dock bumps, so make them replaceable |`
   Replace (3 rows):
   `| **Sepals G3, G4, G5** | GFRP or printed ASA shells on the float edge, calyx green, curling to the water | Light, shaped | Fender function: they take dock bumps, so make them replaceable. G3 also carries the green screen wall P6 since v0.47 |`
   `| **Sepal G2: stem landing** (v0.45) | Same build-up as the calyx deck: green PIP rubber over composite deck panels on the float structure, flush with G1, ~1.45-1.6 m wide, from beside the hot room to the float edge | It's the root of the stem and a walkway, not a fender | Carries all stem foot traffic and the stem's tie-in at the float edge. No step, no hump |`
   `| **Sepal G6: kids' slide** | GFRP shell, gel-coated, same fabricator as the slide petal | Smooth, repairable | Climb-out lobes removed in v0.44; a new climb-out is still to be chosen |`

10. **Parts Catalog L81** (C). Move this row into the new land-side subsection (Medium 31).
    Find: `| **Changing trailer and showers** | Phase 1 ops | 1 | $30-60K | An outdoor retailer |`
    Replace: `| **Land-side changing, lockers, showers and toilets** | On land up top (bluff + gravel lot), not on the float (Davey 2026-09-30; Master Plan section 9). Phase 1 trailer vs permanent building still open | 1 | $30-60K for a Phase 1 trailer; full land-side band TBD after the land-side concept plan | An outdoor retailer |`

11. **Model page, Calyx piece** (`The Rose - 3D Model.html`; audit prose L242) (A)
    Find: `<p>The float deck is sepal green, and five pointed sepals reach out between the petals and curl to the water. One of them is a gentle kids' slide, a shallow ramp into the water with feathered side steps to climb back out, tucked away from the climbing wall.</p>`
    Replace: `<p>The float deck is sepal green, and five pointed sepals reach out between the petals. Four curl down to the water. The fifth, between the bridge petal and the west lounge, lies flat and flush with the deck as the stem landing: about 1.5 m wide, running from beside the hot room out to the float edge, where the stem walkway starts. One of the four curling sepals is a gentle kids' slide, a shallow ramp into the water, tucked away from the climbing wall. It still needs a new way to climb back out.</p>`

12. **Model page, Decisions open** (audit prose L338) (A)
    Find: `<li>Should the stem boom carry a walkway so people can walk out to the leaves?</li>`
    Replace: `<li>Stem: still open are a flat deck route from the gangway to the stem landing (an inner lane around the hot room is proposed), whether the walkway should run the full ~150 m to the fire pier as a gated emergency route, and whether the leaf stalks become walkable.</li>`

#### Medium

**Design Brief**

13. **L161.** Find the whole line starting `| **The Stem** | Green enclosed waterslide from a petal terrace to the river |`.
    Replace: `| **The Stem** | Floating boom, ~150 m, with a 1.5 m walkway open on both sides like a dock (no railing, v0.46) out to the last leaf; beyond that a swim boom to the fire station pier | Grows from the stem landing on sepal G2, flush with the deck, between bridge petal P3 and west lounge P4 (river/northwest side, v0.45) | Downstream swim boundary. The waterslide is now slide petal P2, see section 10 |`

14. **L14.**
    Find: `Next to it, a small dark Thorn sauna for 6 to 8, and a green Stem waterslide that spirals off a petal terrace into the river and lands swimmers on a leaf-shaped float.`
    Replace: `A slide petal drops into the swim cove. The green Stem grows from a flat sepal landing between the bridge petal and the west lounge: a walkway open on both sides like a dock runs out to the last leaf, and a swim boom carries on ~150 m north to the fire station pier.`

15. **L68.** Find the whole decision 44 row.
    Replace: `| 44 | Sepals | **Five, symmetric** (v0.19). Four curl to the water. **G2 (between P3 and P4) lies flat, flush with the deck, as the stem landing** (~1.45-1.6 m wide, from beside the hot room to the float edge where the 1.5 m walkway starts; no step, no hump; v0.45). One is the **kids' sepal slide** (G6): 12-degree ramp into the water. Its feathered side lobes were removed in v0.44 (they read as stepping stones), so G6 needs another climb-out idea. Sited at the low end of the jump petal; climbing holds only on the tall half |`

16. **After L97 (the decision 73 row), insert** (C, D, E; numbers 74+ are free):
    `| 74 | Land side | **Arrival, check-in, lockers, changing, showers and toilets live on land above the dock** (Davey, 2026-09-30). The bluff and gravel lot are ours to design. Not modeled. Plan in Master Plan section 9 |`
    `| 75 | Cold side | **Requested by Davey (2026-09-30), not modeled:** the back of the sauna (river side, opposite the swim cove) gets plunge buckets, river-pumped waterfalls and rinse showers, plus a few fresh-water showers under slide petal P2. Which petal hosts it is **open**: P5 as a cold petal is Claude's recommendation, not a decision. Master Plan section 10 |`
    `| 76 | Doors | **Open** (Davey 2026-09-30: not sure yet). On the table, not decided: small vestibules in screen petals P6/P7, a ~1.8 m petal door the host opens for round changes, and which side it faces (cove, or D1 toward the cold side). The model keeps D1-D3 at 0.9 m until he picks. Pathways doc section 8, Master Plan section 9 |`

17. **After L8, add to the companion list** (F):
    ```
    - `The Rose - Master Plan (Sept 2026).md`: one-sheet status of every workstream; section 9 = land side (decided) + door options (proposal), section 10 = cold side (requested, not modeled)
    - `The Rose - Pathways and Capacity (Sept 2026).md` (2026-09-30): circulation findings and proposals, not decisions. No flat lane around the float (the fire roses sit ~0.5 m off the lobed hot-room wall), a pile-up at D3 / kids' slide G6 / the P1 ramp foot, leaves are swim-only, the crown has one stair (T1), one gangway to land
    ```

18. **L411** (B).
    Find: `Year one, the Stem can stand as a sculptural element and stair-rail with the Leaf as a swim float. Year two, it opens.`
    Replace: `Year one, the slide petal (P2) can stand as sculpture; year two, it opens. The Stem is no longer a slide or a stair-rail: it's the floating boom with a 1.5 m walkway open on both sides like a dock (no railing, v0.46), rooted at the G2 stem landing (v0.45).`

19. **L528** (D; conflicts with Davey's request).
    Find: `18. Cold stations at each cleft: a Downpour bucket or a small waterfall per petal.`
    Replace: `18. ~~Cold stations at each cleft: a Downpour bucket or a small waterfall per petal.~~ Superseded 2026-09-30: Davey wants the cold side at the back of the sauna (river side, opposite the cove), not at every cleft; the G2 cleft is now the stem landing. See decision 75.`

**Master Plan**

20. **L67** (B).
    Find: `| Insurance: liability with jump edges, no rails, slide, climbing wall | **open, could reshape the design** |`
    Replace: `| Insurance: liability with jump edges (glass guards only where P1 is over hard surfaces, v0.43), the open stem walkway (no rail since v0.46, boats alongside), slide, climbing wall | **open, could reshape the design** |`

21. **L141** (E).
    Find: `6. **The ritual on the Rose:** in through the hot-room vestibules, out the big door to the cold water, rest in the amphitheaters, crown later.`
    Replace: `6. **The ritual on the Rose:** into the hot room (door concept still open; vestibules and a big round-change door are proposals, see Doors below), out to the cold water, rest in the amphitheaters, crown later.`

22. **L157** (E).
    Find: `Each gets a **small vestibule** hidden in its screen petal (P6, P7), so the outer and inner doors are never open together. That cuts heat loss from latecomers and early leavers by most of the ~4 MJ a round would otherwise lose.`
    Replace: `**Proposal, not decided:** a small vestibule hidden in each screen petal (P6, P7), so the outer and inner doors are never open together. Est. it would save most of the ~4 MJ a round otherwise loses to latecomers and early leavers. (v0.47 moved P6 onto sepal G3 and made the space behind it the G7 standing lounge, so a D1 vestibule would now take lounge space.)`

23. **L158** (E).
    Find: `- **Round-change door: a wide petal door, ~1.8 m (a pair of leaves)** on the cove side (now likely D1 facing the cold petal, see section 10), opened by the host only at the end of a round. It leads straight to the cold steps and the river. It's also the hot room's big egress door.`
    Replace: `- **Option: a round-change petal door, ~1.8 m (a pair of leaves)**, opened by the host only at the end of a round, leading to the cold steps and the river; it would also be the hot room's big egress door. Which side it would face is open: the cove, or D1 toward the cold side (section 10's suggestion; D1 now opens onto the G7 standing lounge). Not decided.`

24. **L210** (E).
    Find: `- **The big round-change door should face the cold petal, not the cove.** Most people go cold first. My pick is D1 (west): D2 is where the gangway lands, and swimmers can take the inner lane around to the cove. This replaces the cove-side door in section 9 and Pathways decision 10.`
    Replace: `- **If there is a big round-change door (door concept still undecided), it should probably face the cold side, not the cove.** Most people go cold first. My pick would be D1 (west): D2 is where the gangway lands, and swimmers could reach the cove by the inner lane if that gets built. Since v0.47, D1 opens onto the G7 standing lounge, so a big door there would empty a round into the lounge first. This is a proposal set against the cove-side option in section 9, the same open question as Pathways decision 10, not a change to either.`

25. **L218** (E).
    Find: `- [ ] Move the big petal door to D1 facing the cold side (update the Pathways doc and section 9).`
    Replace: `- [ ] Once Davey settles the door concept: if there is a big petal door, decide whether it faces the cold side (D1) or the cove, then update the Pathways doc and section 9.`

26. **L151** (C).
    Find: `| Toilets | Land block sized by the plumbing code, **plus 1-2 near the water** | A guest 2 hours into the ritual won't walk 100 m back up. Float or dock-head WC needs a pump-out or sewer line |`
    Replace: `| Toilets | Land block sized by the plumbing code (Davey 2026-09-30: toilets on land). Open question for Davey: 1-2 more near the water? | A guest 2 hours into the ritual won't walk 100 m back up. Any WC at the dock head or on the float needs a pump-out or sewer line, and goes against the on-land call unless he OKs it |`

27. **L7.**
    Find: `concept and 3D model are far along (v0.17, 17 iterations in one day)`
    Replace: `concept and 3D model are far along (v0.48 as of 2026-09-30)`

**Pathways and Capacity**

28. **L166** (E).
    Find: `**The design:**`
    Replace: `**Proposal (not decided; Davey isn't sure about the doors yet):**`

29. **L167** (E).
    Find: `- **D1, D2: everyday doors.** 0.9 m, light, glazed so you see who's coming, no latch (roller catch plus soft closer; that also avoids panic-hardware rules), swing out. Each opens into a **vestibule tucked behind its screen petal (P6, P7)**, about 1.5-2 m deep, room for 3-4 people. The silhouette doesn't change.`
    Replace: `- **Option: D1, D2 as everyday doors.** 0.9 m, light, glazed so you see who's coming, no latch (roller catch plus soft closer; that also avoids panic-hardware rules), swing out. Each could open into a **vestibule tucked behind its screen petal (P6, P7)**, about 1.5-2 m deep, room for 3-4 people. Since v0.47 the space behind P6 is the G7 standing lounge, so a D1 vestibule would take lounge space. If the big door goes at D1 (decision 10), only D2 keeps an everyday vestibule door.`

30. **L191** (E).
    Find: `9. **Doors:** vestibules in P6/P7 + a ~1.8 m petal door on the cove side for round changes (my pick), or a 1.8 m pair at every door?`
    Replace: `9. **Doors (open, Davey not sure yet):** vestibules in P6/P7 + one ~1.8 m petal door for round changes (my pick; which side is decision 10), a 1.8 m pair at every door, or keep today's 3 x 0.9 m?`

31. **L49** (A).
    Find: `| G2, NW | River, Hawthorne | New stem root (proposed) |`
    Replace: `| G2, NW | River, Hawthorne | Stem landing (v0.45): sepal G2 lies flat, flush with the deck, ~1.45-1.6 m wide, out to the float edge where the 1.5 m stem walkway starts. Still no flat route to it from D2 |`

32. **L185** (A).
    Find: `3. **Stem root at G2:** confirm, built together with the inner lane so the gangway can reach it.`
    Replace: `3. **Stem root at G2:** done in v0.45 (G2 is now the flat stem landing). Still open: reaching it from the gangway, which is the inner lane in decision 1.`

33. **L190.**
    Find: `8. **Model it:** draw 1-3 as the next version (v0.42; another session already published v0.41 for the jump ramp)?`
    Replace: `8. **Model it:** draw 1-2 (inner lane, D3 fix) as the next version, v0.49? The stem root (3) went in as v0.45; the live model is v0.48.`

34. **L29** (G).
    Find: `G6 is the only climb-out on the flower itself, and it's in the D3 pile-up`
    Replace: `G6's climb-out steps were removed in v0.44 (they read as stepping stones), so the flower itself has no climb-out right now and G6 needs a new one. It's also in the D3 pile-up`

35. **L13** (G, missed by the audit).
    Find: `but T1 (about 1 m wide) is its only stair. That's legal only while the crown stays under 50 people, and it's still a poor rescue route.`
    Replace: `but T1 is its only way up, and since v0.42 it's seat-steps: 39 cm bench steps beside a walking aisle of ~20 cm half steps, ~0.65 m wide (est., measure in the model). That likely falls short of a code stair even under 50 people (36 in minimum width, ~7 in max riser), and it's still a poor rescue route. Ask the code consultant.`

36. **L100** (G, missed by the audit).
    Find: `| Code | A single ~1 m stair is OK only below 50 people.`
    Replace: `| Code | A single stair at least 36 in (0.91 m) wide is OK only below 50 people. Since v0.42, T1's walking aisle is ~0.65 m of ~20 cm half steps (est.), so it likely doesn't count as that stair.` (the rest of the row is unchanged)

**Materials Plan**

37. **L44** (A, B). Find `| **Stem boom** | HDPE pipe float sections (green, the swim-lane industry standard) with a walkway option | Floats, flexes with the river, cheap | Anchored at both ends and mid-span |` and replace it with 2 rows:
    `| **Stem walkway** (G2 landing to the last leaf, ~120 m) | 1.5 m grippy composite or open-grate deck on a wider float section, green; rub strips and cleats (thorns S4/S5) along the river edge. No railing (v0.46): edge safety comes from the deck itself (grip surface, a contrasting edge strip, proposed) | Walkable, open both sides like a dock (decision 47) | Needs a wider float section than a plain boom. A transition piece where it ties to the float at the G2 landing, riding the river swing against the rigid float |`
    `| **Stem boom** (last leaf to the fire station pier) | HDPE pipe float sections, green (the swim-lane standard) | Floats, flexes with the river, cheap | Anchored at the fire station pier tip and mid-span; the pier tie-in still needs the fire bureau (Master Plan s.2) |`

38. **After L41, add** (D):
    `| **Cold side** (requested by Davey 2026-09-30; river side, opposite the cove; which petal is still open, P5 is the recommendation) | River falls: one ~8,000 GPH pump + 316 stainless manifold and spouts, pump on isolators off the hull, intake cage; 4-6 tipping buckets (~10-20 L) on pull chains; 2-3 river-water rain heads; deck in drained grating or PIP rubber falling to the river | Same system as The Cascade on the current docks | Spray walls for the NNW summer wind; river water only, straight back to the river |`
    `| **Fresh-water showers under the slide (P2)** | 3-4 stainless heads, small heater on the gas service, fresh-water tank or the fire-station potable line | Rinse after a river swim | ~2.1 m headroom at the heads (check under the v0.48 pushed-out blade); drainage; no soap on the float |`

39. **L16 + L48** (F; a 1 m apron doesn't fit).
    - L16: Find `- Under the fire rings. Keep a 1 m stone or steel apron around every fire.` Replace: `- Near the fires. The fire roses sit ~0.5 m off the hot-room wall and the first amphitheater step starts ~0.8 m from the flame (Pathways doc s.2), so a flat 1 m apron doesn't fit. Take the clearance from the fire unit's listing and the fire marshal; whatever falls inside it must be non-combustible (the hot-room wall face toward the fire, the first step's tread and riser), unless the fires move out (inner lane, Pathways Fix 1, proposed).`
    - L48: Find `| **Fire nooks** | Gas or ethanol fire rings in steel/stone (Parks may block open flame; confirm) | Sheltered, controllable | 1 m non-combustible apron |` Replace: `| **Fire roses (F1, F3-F5)** | Gas or ethanol fire rings inside steel fire roses (blackened steel or polished stainless, both modeled); Parks may block open flame, confirm | Sheltered, controllable | Clearance per the unit's listing reaches the hot-room wall and the first step; see the note above |`

40. **L34.**
    Find: `| **Flue** | Double-wall stainless, through the crown inside a tempered glass ring | Code clearances through the roof lounge | 3 ft above the roof deck minimum |`
    Replace: `| **Vent stack (H4)** | Double-wall stainless side stack on the north wall, in the service ring (no center flue, decision 64) | Code clearances | EOS/KUSATEK to confirm a horizontal or short-vertical vent (a power vent may be needed) |`

41. **L36, L53, L61** (decision 65).
    - L36: replace `Choice of: charred cedar (shou sugi ban) planks; printed ASA panels; GFRP shells; standing-seam metal in rose color` with `Choice of: GFRP shells; printed ASA panels; standing-seam metal, all in deep rose red (charred cedar ruled out, decision 65)`.
    - L53: replace the whole `1. **Petal skin:**` line with `1. **Petal skin:** GFRP (smooth, colored, the same trade as the slide, so one fabricator does both) or printed ASA panels (the story, unproven outdoors at this size); charred cedar is out (decision 65). My pick: GFRP for the slide, jump petal and the curled sepals (G3-G6); GFRP or printed ASA for the amphitheaters, chosen after a sample day.`
    - L61: replace `- A charred cedar board.` with `- A printed ASA panel in deep rose red, with its E84 flame-spread data.`

42. **L42** (missed by the audit).
    Find: `| **Stepped entry petals** | Aluminum or composite frames, PIP rubber treads, stainless ladder rungs | Wet, submerged part of the time | Sacrificial anodes on anything submerged |`
    Replace: `| **Climb-outs (G6 and ladders)** | Aluminum or composite frames, PIP rubber treads, stainless ladder rungs | Wet, submerged part of the time | The stepped entry petals under the slide were dropped in v0.20. G6 is the only climb-out on the flower and needs a new one since v0.44 (still to choose). Sacrificial anodes on anything submerged |`

**Parts Catalog**

43. **Restructure L65 and move 2 rows** (C). After the garden table, add `### The land side (up top: bluff and gravel lot, Davey 2026-09-30; Master Plan section 9)`. Move the changing row (High 10) and the host station row (L82, Low) into it.

44. **After L49, add** (D; "Band TBD" is a placeholder, don't invent numbers; don't name P5). Mark each row "requested 2026-09-30, not modeled; placement and counts are proposals (Master Plan section 10)":
    `| **River falls** | River-pumped waterfalls at the back of the sauna, river side, opposite the swim cove. Exact petal still open | set | Band TBD once modeled | A pump or plumbing trade; a patron |`
    `| **Plunge buckets** | Tipping buckets on pull chains beside the falls (4-6 proposed), one maker | TBD | Band TBD | Members; one metalsmith as a commission |`
    `| **Rinse showers** | Rinse heads at the back of the sauna, plus a few fresh-water showers under the slide petal P2 | set | Band TBD | A plumbing trade, in-kind |`

45. **L70** (A).
    Find: `| **The sepals** | Five green fins, one a kids' slide | 5 | $5-15K each | Patrons; a family for the kids' slide |`
    Replace: `| **The sepals** | Five green sepals: four curl to the water, one of them (G6) the kids' slide; the fifth (G2) lies flat, flush with the deck, as the stem landing where the walkway meets the flower (v0.45) | 5 | $5-15K each | Patrons; a family for the kids' slide |`

46. **L73-74.** Leaves count is 4, not 3.
    - L73: replace with `| **Leaf floats** | Four compound leaves (L1-L4; L2 on the river side doubles as boat tie-up); veins inlaid by a woodworker or boat builder | 4 | $25-50K each | A paddle shop, a boat builder, a swimwear brand |`
    - L74: replace with `| **Leaflets** | Each of the five leaflets on each leaf | ~20 | $2,500 each, ~$50K | Members |`
    - Then re-add the intimate-parts totals in sections 3 and 4.

**Session Plan**

47. **L30** (A, B). Find the whole E8 row and replace it with:
    `| E8 | Stem, leaves and gangway | Stem landing (sepal G2, flat and flush with the deck between P3 and P4, shared with E7), stem walkway (1.5 m, open both sides like a dock, no rail), compound leaves, boat tie-ups, thorns, gangway and dock landing. Open from the Pathways doc (proposals, not decisions): no flat deck route from the gangway to G2 yet, leaves swim-only, stem to the fire pier as an emergency route | v0.18-0.19, v0.29, v0.45-0.46, Pathways and Capacity doc s.1 and s.5 |`

48. **L44** (C). Find the whole P6 row and replace it with:
    `| P6 | Operations | Program, staffing, events and DJ series, commission curation, and the land side: arrival, check-in, lockers, changing, showers and toilets on land above the dock (bluff and gravel lot, Davey 2026-09-30). Still open: Phase 1 trailer vs Phase 2 building, 1-2 toilets at the water, sizes pending the session model | Master Plan s.8-9, brief s.21, Pathways and Capacity doc s.9 |`

49. **L33** (F, E). After `never drawn straight onto the flower.`, append:
    `Every room reads The Rose - Pathways and Capacity (Sept 2026).md first (findings and proposals, not decisions): no flat lane around the float because the fire roses sit ~0.5 m off the lobed hot-room wall, the D3 / kids' slide / P1 ramp-foot pile-up, swim-only leaves, one stair (T1) to the crown, and one gangway to land. The door concept (vestibules in P6/P7, a ~1.8 m petal door for round changes, which side it faces) is not decided. No room changes D1-D3 or draws vestibules or a petal door until Davey decides.`

50. **After L31, insert E10** (D):
    `| E10 | Cold side (requested, not modeled) | Plunge buckets, river-pumped falls and cold rinse at the back of the sauna (river side, opposite the swim cove); a few fresh-water showers under slide petal P2. Using P5 as the cold petal is a recommendation, not a decision. v0.47's G7 standing lounge sits in the same river-side zone | Master Plan s.10, Waterfall Plunge brief |`
    Also, at L78, change `Are E1 to E9 the right cut?` to `Are E1 to E10 the right cut?`

51. **L70.**
    Find: `1. Write `Interfaces.md` with every element's envelope, measured from v0.33`
    Replace: `1. Write `Interfaces.md` with every element's envelope, measured from the live model (v0.48: the stem leaves from the flat G2 landing between P3 and P4 with no rail; P6 is a green wall on G3 with the G7 standing lounge behind it; P2 has the group stair)`

52. **L40** (F, missed by the audit). Find the whole P2 row and replace it with:
    `| P2 | Engineering and code | Naval architect shortlist, stability, occupancy and exits (second way off the float, crown stair, round cap), gas certification, electrical, lightning | Master Plan s.3, Pathways and Capacity doc (findings and proposals, not decisions), Title 28 brief |`

**Review Prep**

53. **After L42** (C), insert:
    `- [ ] Land-side program sized and priced (Master Plan s.9; Davey 2026-09-30: arrival, check-in, lockers, changing, showers and toilets on land above the dock). Planning sizes are est. until the session model is set; Phase 1 trailer vs Phase 2 building and 1-2 toilets at the water are still open. Check the catalog's $30-60K changing line against it.`
    Also add to the section 6 table: `| Land-side program cost (host pavilion, lockers, changing, showers, toilets, BOH) | Master Plan 9 | Decided on land 2026-09-30; the stack only carries a $30-60K changing trailer line |`

**Slide Petal Study**

54. **Add to Open** (D; updated for v0.48):
    `- [ ] Fresh-water showers under P2 (Davey's request 2026-09-30, Master Plan s.10, not modeled): 3-4 heads, ~2.1 m headroom, drained floor, fresh-water supply plus a small heater. The 1.2 m push-out is now in the model (v0.48), so the covered deck under the blade with 2.1 m headroom is small (est.). Measure it in v0.48 before placing heads, and keep wet shower traffic out of the stair queue.`

**Crown and DJ Booth Spec**

55. **L295.**
    Find: `Supersedes the section 14 recommendation. Drawn in model v0.34.`
    Replace: `Supersedes the section 14 recommendation. Drawn in model v0.34. **Reverted 2026-09-29:** Davey rejected the lap as chaotic. The live model went back to v0.33, so the crown stays 3.15 m above the float deck and the hot room keeps its height. Crown access was then redone inside the jump petal (v0.39-v0.42: T1 seat-steps up to the crown landing C7, T2 rim ramp for jumpers only, not an exit). Sections 14 and 15 stay as a record of the detour. Neither is a current recommendation.`

56. **L3.**
    Find: `Built from model v0.29.`
    Replace: `Built from model v0.29. **Status 2026-09-30 (live model v0.48):** written before the v0.34 lap (drawn, then reverted; sections 14-15 are a record only); v0.35 moved the DJ to the center of the crown under the rose-window roof (C2/C3), made the flat deck the default and took the fire off the crown; v0.39 added the crown landing C7; v0.40-v0.42 made the T1 seat-steps inside P1 the way up, with the T2 rim ramp for jumpers only; v0.43 added glass guards wherever P1 is over a hard surface. Sections 0, 2, 4, 5, 6, 7, 8, 9, 11 and 13 still assume the nested south-rim booth, a crown fire or the old spiral access. The service stair (decision 2) is still undrawn. The v0.45-v0.48 changes don't touch the crown.`

57. **L246** (missed by the audit).
    Find: `2. **Second way off the roof:** service stair behind the booth, with the jump petal gated during night sets (my pick).`
    Replace: `2. **Second way off the roof:** a service stair to the crown (it was 'behind the booth' for the nested booth, so the location needs a new pass now that the booth is central), with only the T2 jump route gated during night sets (my pick).`

**Model page** (`The Rose - 3D Model.html`, then republish VPwzt)

58. **Lede (audit prose L98), three edits:**
    - Replace `The other petals are amphitheaters: stadium steps arch up from a fire pit at the bottom to a rim you can jump from at any height between about 1 and 3 m.` with `The bridge petal is an amphitheater: stadium steps arch up from a fire pit to a rim you can jump from at any height between about 1 and 3 m. The two river-side lounges have the same steps and fires behind a glass rail.`
    - Replace `Two petals droop into a calm swim cove as group slides, and the green stem floats around the cove to keep swimmers in.` with `The slide petal droops into a calm swim cove. The green stem grows out of the gap between the bridge petal and the west lounge: a flat sepal landing, flush with the deck, walks you straight onto a 1.5 m walkway, open on both sides like a dock, that runs out to the last leaf. Past that the stem carries on as a boom around the cove to the fire station pier and keeps swimmers in.`
    - Delete ` Under the slide petals, stepped petals walk you down into the water.`

59. **Stem piece (audit prose L243):**
    - Change the h3 `Dock to dock, and you can walk it` to `From the flower to the pier; walk it to the last leaf`.
    - Replace `about 150 m, with a walkway on top, open on both sides like a dock.` with `about 150 m. A 1.5 m walkway runs on top from the landing out to the last leaf, open on both sides like a dock; past that the stem is a swim boom. From the gangway there's no flat deck route to the landing yet (an inner lane around the hot room is proposed).`

60. **Stepped entry piece (audit prose L238)** (D). Set the tag to `Under the slide`, the h3 to `Fresh-water rinse (requested, not modeled yet)`, and the p to:
    `A few fresh-water showers are planned under the slide petal, the rinse after a river swim before going back into the heat. Lukewarm, and no soap on the float. Headroom under the slide still needs checking. The old stepped plates came out in v0.20, and since the kids' slide lost its climb-out lobes in v0.44, the flower has no dedicated climb-out yet.`

61. **Decisions open (audit prose L334)** (E, D, F). Add:
    `<li>Doors: how many, where, and which way they face. On the table, not decided: small vestibules in the screen petals P6/P7, and a ~1.8 m petal door the host opens for round changes.</li>`
    `<li>Cold side on the river-side back of the sauna (plunge buckets, river-pumped falls, rinse showers): which petal carries it? Claude recommends P5; not decided.</li>`
    `<li>Crown access: the seat-step stair inside the jump petal is the crown's only stair, so the crown caps at 40 until a service stair is drawn.</li>`

62. **Jump petal piece (audit prose L233):** replace `One sweeping petal between the two slides.` with `One sweeping petal beside the slide.`

**Drawing Set** (pair with Geometry 1-2 below)

63. **L446:** replace keynote 10 with `[10,'Sepals curl down to the water. G2, between P3 and P4, lies flat as the stem landing',P(252*D,8.6,DECK-0.3),['axon','plan','roof','model']],`. After keynote 13, add `[14,'Stem landing (G2). Flat and flush with the deck, 1.45-1.6 m wide, from beside the hot room to the float edge. The stem walkway starts here',P(324*D,6.8,DECK+0.05),['axon','plan','roof','model']],`

64. **L447:** replace keynote 11 with `[11,'Stem. Starts flush at the G2 landing between P3 and P4. 1.5 m walkway, open both sides like a dock, out to the last leaf. The boom runs on north to the fire station pier, ~150 m in all',V3(-7.0,0.55,-17.5),['axon','plan','roof','model']],`

65. **L111 title block + L186 comment.** Pick one:
    - After a full regeneration: `Model v0.48, 30 Sept 2026`.
    - After a stem-only patch: Geometry `Model v0.33, stem per v0.46`, plus a row `Not yet redrawn: v0.35 centre DJ booth and flat crown; v0.36-v0.44 jump petal (wall lean, T1 seat-steps, T2 rim ramp, glass guards, S11-S13 buoy zones); v0.47 green wall P6 + G7 standing lounge; v0.48 slide group stair`.
    - Don't write the current version until the whole set is redrawn.

**make_rose_stl.py**

66. **L9:** replace `re-print. The same numbers drive the 3D viewer, so keep them in sync.` with `re-print. FROZEN AT v0.4 (2026-09-26): the 3D viewer is now v0.48 and this file has NOT been kept in sync. It still has the v0.4 roof-top slide stem, spiral-stair columns, three simple leaf floats, five deck petals and a centre flue; there is no calyx, no sepals or G2 stem landing, no amphitheaters, jump petal or crown. Regenerate from the live model before printing.`

67. **L14:** replace the stem line with `  stem_slide.stl           v0.4 only: the stem as a roof-top waterslide. Superseded: since v0.45 the stem is a 1.5 m walkway leaving the flat G2 landing (cleft between P3 and P4) flush with the deck; no railing since v0.46.`

#### Low (find, then replace)

**Design Brief**
- **L401:** `## 10. The Stem slide: honest read` becomes `## 10. The slide petal (P2): honest read`
- **L436:** replace the row with two rows: `| Slide petal P2 (year two) | $150K | $350K | Carried over from the old Stem-slide figure |` and `| Stem: ~150 m boom, 1.5 m open walkway float section (decision 47), thorns/cleats, four compound leaves | TBD | TBD | Not priced yet |`
- **L162:** `| **The Leaves** | Four compound leaves (five leaflet floats each): three swim-side lounging leaves plus boat leaf L2 on the river side | Along the stem walkway | Swim-to only: the stalks are 0.3 m tubes, not walkways (Pathways doc section 5; walkable stalks still open). Double as the swim float the City wanted in Phase 1 |`
- **L163:** `| **Fire roses** | Steel fire roses at the foot of each amphitheater petal (F1 in P1, F3, F4, F5), seats stepping up behind | Inside the petals, not on the deck: the deck between petals is five small cleft pockets (~4-6 m2 each, Pathways doc), and G2 is now the stem landing | Parks fuel ban applies; the LOI needs carve-out language |`
- **L557:** `7. **Slide petal (P2):** year-two opening OK, or is it a day-one must?`
- **L374:** `| Molds for the slide petal's GFRP shell (decision 39, Materials Plan) | Stairs, guard posts, drape tracks |`
- **L184:** `| Doors | 3 (D1-D3), 0.9 m, in the clefts between petals (v0.2). Door concept still open: vestibules in P6/P7 and a ~1.8 m petal door are proposals, not decisions (Pathways s.8) | 50+ occupants need 2 exits with panic hardware |`. Above the section 4 table, add `_v0.1 baseline numbers. Float, roof and heater have since moved on (decisions 2, 11, 56, 64). The 3D model and CHANGELOG are current._`
- **L48:** replace `Glass rail only on the dock-side lounge petals where jumping isn't allowed.` with `Glass rail on the dock-side lounge petals where jumping isn't allowed, and (v0.43) 42 in glass guards on jump petal P1 wherever a fall would land on something hard (deck, roof, seat rows); the jump edge itself stays open.`
- **L405:** replace `design for 8-10 ft at low water and a floating exit (the Leaf) that rides the river.` with `design for 8-10 ft at low water under the slide petal's tip, which lands in the cove (curled exit and short runout, in the model since v0.48). The leaves hang off the stem, not the slide exit.`
- **L432:** `| ~~The Thorn (sauna + hex float + gangway)~~ | ~~$120K~~ | ~~$220K~~ | Removed 2026-09-26 (decision 10). Recompute the subtotal and all-in without it |`. L440 and Q8 (L558) are stale for the same reason.
- **L529:** `19. Heat recovery: exhaust air warms heated benches on the fire lounges (changing rooms are on land now, decision 74).`

**Master Plan**
- **L168:** `- [ ] **Toilets at the water?** Ask Davey first (his 2026-09-30 call puts toilets on land). If yes: dock-head vs float WC; pump-out vs sewer.`
- **L131:** replace `arrival, check-in and lockers live on land above the dock, and all the land up top is ours to design.` with `arrival, check-in, lockers, changing, showers and toilets live on land above the dock, and all the land up top (bluff + gravel lot) is ours to design.`
- **L231:** `4. **Insurance broker call** on jumps, slide, climbing wall and unrailed edges, including the open stem walkway (no rail since v0.46, boats tied alongside). Do this before engineering so we don't design what can't be insured.`
- **L91:** `| 3D print: scale model | open (files at v0.4; regenerate from the current model, v0.48 or later, once petals lock) |`
- **L159:** replace `- **One-way flow:** the round leaves by the big door toward the water while the next round enters through the vestibules at the same time.` with `- **One-way flow (only if both the big door and vestibules are built):** the round would leave by the big door toward the water while the next round enters through the vestibules at the same time.`
- **L160:** replace `The big door needs a ~1.5 m stepped aisle` with `A big door, if built, would need a ~1.5 m stepped aisle`
- **L217:** `- [ ] Davey to pick where the cold side goes: P5 as the cold petal (Claude's recommendation, not decided), or split between P5 and the D1 pocket (since v0.47 that pocket is the G7 standing lounge, so this would take lounge space).`
- **L186, L188, L219** (P5 assumed):
  - L186: prefix with `If P5 is picked: `
  - L188: `**What would go in the cold petal (wherever it lands):**`
  - L219: `- [ ] Model it once Davey picks the spot: falls off the chosen petal's rim, buckets on the ribs, showers under P2, drained deck.`
- **L202:** `1. Gangway (the required pre-rinse is already done on land, section 9), then an optional rinse at the slide showers.`
- **L24:** `| Calyx, sepals, stem boom, leaf floats | done in model | Stem grows from the flat G2 landing (v0.45), walkway has no rail (v0.46), G6 needs a new climb-out (v0.44), P6 is a green wall on G3 with the G7 standing lounge (v0.47) |`

**Pathways**
- **L99:** `| Way up / down | T1 seat-steps wrapping F1 inside P1 (v0.42): a walking aisle of 16 half steps (~20 cm) on rows 0-1 beside 8 bench-height seat steps (~39 cm); glass guards where it's high over the deck and roof (v0.43). T2 rim ramp is jumpers only (22-28°), **not an exit** |`
- **L170:** replace `The petal door needs a ~1.5 m stepped aisle inside` with `A petal door, if built, would need a ~1.5 m stepped aisle inside`
- **L176:** replace `and ideally **1-2 toilets at the water**.` with `and maybe **1-2 toilets at the water** (open question for Davey: his 2026-09-30 call puts toilets on land).`
- **L55:** after `not a lobby.`, append ` Two pockets have changed since this was measured: G2 is now the stem landing (v0.45), and the D1 pocket between P4 and P5 is the ~2.5 m deep G7 standing lounge behind the green wall P6 (v0.47). Re-measure at v0.48 (P2 also moved 1.2 m out).`

**Materials Plan**
- **L38:** `| **Jump petal (P1)** | Steel-framed cantilever off its own float lobe or pile; GFRP or aluminum skin; PIP rubber on the T2 rim ramp; T1 seat-steps (bench-height, ~39 cm rise) in thermo-wood or PIP over composite; 42 in laminated glass guards with a slim steel top rail and posts wherever a fall would land on something hard (v0.43), open at the jump edge | Load path for 20+ people at ~5 m up | Naval architect + PE from day one |`
- **L47:** `| **Glass (bridge petal, lounge rails, P1 guards, rose-window roof)** | Laminated tempered glass; heat-rated glass at the hot room; leaded stained glass in the crown bud petals and the rose-window roof | Safety, bridge view, night glow | Tilt the hot-room pane 5-8 degrees for acoustics |`
- **After L50, add:** `| **Buoy lines (S12, S13)** | Marine swim-line floats on anchored lines: orange/white around the climbers' pen, yellow on the jump zone's outer arc | Keeps climbers' falls and jumpers apart | Soundings (~12-13 ft at low river) before fixing positions |`
- **Also add:** `| **Standing lounge G7 lean ledge** (v0.47) | Thermo-wood or hardwood ledge at 42 in along the inside of the green wall P6 | Hands and drinks, wet all day | Oil like the other outdoor wood |`
- **L46:** `| **Crown (C1)** | Flat deck (v0.35 default): PIP rubber on isolation pads over the CLT/insulated roof, built as a floating floor; DJ booth C2 at the center under the leaded-glass rose-window roof C3; no flue (v0.25). Stone or steel fire ring only if the fire-circle option comes back (off by default) | Soft, quiet underfoot | Crown spec s.4 says PIP is bad for dancing and proposes synthetic teak or hardwood where people dance; needs a pass now that the booth is central |`
- **L45:** `| **Leaf floats (L1, L3, L4 swim side; L2 boat tie-up, river side)** | EPS-core floats with PIP rubber or EVA decks, green; L2 adds rub strips and cleats for pull-up boats | Soft to lie on, wet all day | Swim-to for now: the 0.3 m stalks aren't walkable (Pathways s.5). Ladder on the swim side of each swim leaf |`
- **L41** (v0.48): the veins are now 4 stair handrails, 0.9 m over the nosings. Add `structural core (steel inside a GFRP vein) where they're handrails (v0.48)` to the Why/Watch-outs.
- **Pink to deep rose red** on L10, L17, L40, L55, L58, L60 (decision 65).

**Parts Catalog**
- **L82:** change the description to `The welcome and check-in, on land at the top of the gangway (host pavilion, Master Plan section 9)` and move the row into the land-side subsection.
- **L162:** `7. **Counts:** OK for me to pull rib, stone, plank and leaflet counts from the current model (v0.48) now, flagged as provisional?` Also add `; the model is now v0.48` to L22.
- **L71:** `| **The stem boom** | The boom from the stem landing (sepal G2, between P3 and P4) to the fire station pier (~150 m); a 1.5 m walkway, open on both sides like a dock, runs from the landing to the last leaf | 1 | $75-150K | A marine contractor as builder-sponsor; or a paddle brand |`
- **L50:** `| **Climb-out steps** | Ways out of the river on the flower itself: G6's climb-out still to be designed (lobes removed v0.44); the v0.8 stepped entry petals were dropped in v0.20 | TBD | Band TBD once designed | Patrons; a rubber or decking partner |`

**Crown spec**
- **L5:** add `[[The Rose - Pathways and Capacity (Sept 2026)]] (section 4: T1 is the crown's only stair, 40 cap; findings, not decisions)` to Related.
- **L135:** `3. **Night.** At the end of a set, everyone leaves by one route, the T1 seat-step aisle inside P1. Since v0.43 its high edges have glass guards, but T1 and the T2 jump ramp both start at the crown landing C7, and T2 climbs to the open jump edge. In the dark, one wrong turn at C7 leads there.`
- **L141:** `During night sets, **gate the T2 rim ramp (the jump route) at the crown landing C7**. The T1 seat-steps stay open. Until the service stair exists, they are the only way up and down; once it does, T1 plus the service stair give the crown its two ways off.`
- **L138:** `- Keep the jump petal as the way up: the T1 seat-steps for everyone, the T2 rim ramp for jumpers by day.`
- **L252:** append `(Overtaken: v0.30 became the stained glass pass, and v0.35 moved the DJ to the center under the rose-window roof with no crown fire. Redo this list after the central-booth pass.)`
- **L289:** prefix `(Overtaken: see the revert note under section 15. Since v0.40-v0.42 the way up is the T1 seat-steps inside P1; the T2 rim ramp is for jumpers only and is not an exit.)`

**Session Plan**
- **L29 (E7):** `| E7 | Calyx and sepals | The float's look above water, sepals (G2 is now the flat stem landing, shared with E8; G3 carries the green wall P6 since v0.47; G3-G6 curl to the water), the G7 standing lounge, kids' sepal slide G6 (needs a new climb-out since v0.44; sits in the D3 pile-up, Pathways doc Fix 2, a proposal), swim ladders | v0.16, v0.19, v0.44, v0.45, v0.47 |`
- **L74:** `5. Hold the main model at its current version (v0.48 as of 2026-09-30) until the first hand-off comes back`
- **L26 (E4):** `| E4 | Jump petal | The climb, the jump point (~5.0 m over the deck), climbing wall (lean v0.36, flows into the upper skirt v0.37), how it lands on the crown (C7), water depth, T1 seat-steps, T2 rim ramp, glass guards over hard surfaces, buoy zones S11-S13 | v0.12-0.26, v0.36-0.44 changelog |`
- **L81:** replace `(it has a live bug)` with `(most changed, v0.36 to v0.44; the wall gap was fixed in v0.37)`
- **L25 (E3):** `| E3 | DJ booth | Center booth under the rose-window roof (v0.35 default), nested booth and petal canopy as options, show desk, leaded rose window, rain and gear | Crown spec s.7, v0.30-0.33 glass work, v0.35 |`
- **E5 (v0.48):** `| E5 | Slide petal | Group stair up the heel, launch pad, drop, runout and curled tip (merged into the main model as v0.48); still open: launch pad width, rib structure, depth under the tip, showers under P2, inflatable option | Slide Petal Study, v0.48, Materials Plan |`

**Review Prep**
- **After L115:** `| Cold side cost (requested, not modeled): falls pump, buckets, cold rinse, fresh-water showers under P2, water line | Master Plan 10 | Not in the catalog or the budget range; P5 as the cold petal is a recommendation only |`

**Slide Petal Study**
- `- [ ] Hub approval: the 1.2 m push-out changes the petal's envelope against its neighbors` becomes `- [x] Hub approval: merged as v0.48 (clearance checked: 2.7 m to the S1 gangway edge, 2.2 m to the G6 kids' slide).`
- **Add to Open:** `- [ ] Circulation to the stair foot (Pathways doc, proposals only): the ~1 m slot between the hot room and the heel is reached only from the D2 pocket (gangway landing) or the D3 pocket (already a pile-up); the proposed inner lane would run through the same strip. Settle the slot, the lane and where a group waits, with the hub.`
- **Add to Open:** `- [ ] Guards: v0.43 put 42 in glass guards on the jump petal wherever a fall lands on something hard from over 30 in. Does the same rule apply to the P2 group stair and the sides of the launch pad? Davey set it for the jump petal only, so ask before drawing.`

**Model page**
- **L240:** `<p>The way up is a run of seat-steps inside the jump petal: benches you can sit on or climb, wrapping around its fire from the deck to the crown landing. The rim is a jumpers' ramp, not a way down. It's the crown's only stair, so the crown caps at 40 people until a service stair is drawn.</p>`
- **L258:** `<b>Rails only where you can't jump, or where a fall would hit something hard.</b> Glass on the lounge petals, and glass guards on the jump petal wherever a fall would land on the deck or roof. The stem walkway is open on both sides, like a dock. Everywhere else the rims are jump edges into the cove: depth markings, lifeguards on duty, and the insurer on board before opening.`
- **L220:** `<li>One slide petal droops into the swim cove, and a few fresh-water rinse showers are planned under it (requested, not modeled yet).</li>`
- **L218:** `<li>The jump petal faces the cove beside the slide petal: sit on the seat-steps around its fire, climb to the rim, and jump from the stretch that hangs out over the water. The bridge petal to the north is an amphitheater, and the hot room keeps its bridge view through the bridge window.</li>`
- **L304:** `<tr><td>Slide petal</td><td class="num">1 · ~4 m wide</td><td>Group slide; exit ~4 m past the float edge</td></tr>` (re-measure the exit distance against v0.48)
- **L307:** replace `One custom gas altar; flue out the oculus` with `One custom gas altar; vents through a small stack on the north wall`
- **L337 (Bud) and L342 (NA shortlist):** remove. Both were answered 2026-09-27.
- **L340 (float size):** remove. Decided: as big as the site allows, 55 ft target.
- **L3:** meta description becomes `Concept model v0.48.`
- **L302:** `<tr><td>Amphitheater petals</td><td class="num">P3, P4, P5 + jump petal P1 · rims ~1-2.9 m</td><td>~25 people each (est.); glass on the lounges and on P1 over hard surfaces, open jump edges elsewhere</td></tr>`
- **L208:** replace `Permanent power, data and gas-control lines run up inside the flue chase.` with `Permanent power, data and gas-control lines run up to the booth; the center flue that would have carried them is gone (v0.25), so that route still needs drawing.`
- **L324:** `Ops trailer, permits, shore seating` becomes `Land-side ops (Phase 1 trailer; full land side not priced), permits, shore seating`
- **L233** climbing-wall sentence: `Its back is a climbing wall that starts below the waterline, nearly plumb where the petal is low and overhanging hard near the peak, flowing up into the sauna's upper skirt. Climbers fall into a buoyed pen inside the buoy line; jumpers land outside it. Glass guards run wherever a fall would land on the deck or roof, and the low end feathers into the deck by the kids' slide.`
- **New pieces to add:** the G7 standing lounge (v0.47) and the v0.48 group slide (3-lane stair up the heel, launch pad, curled tip). There is no prose for either yet.

**Other**
- **Oslo Strategic Plan L189:** `(v0.28)` becomes `(v0.48)`.
- **Claude memory** `project_the_rose_sauna.md`: append v0.43-v0.48 plus C, D and E (as undecided). Change the MEMORY.md index line from "v0.21" to "v0.48".

### regenerate-artifact
- **R1 (M, A). Site overlay.** Redraw at v0.48, then save it both as the vault file `The Rose - Site Overlay (Holman-Kerr Dock).png` and as `rose_site_overlay.png` on the page, published via `files`. The stem leaves the NW gap between P3 and P4 at G2, runs out past P3's rim and bends north. Mark the walkway end (S8) at the last leaf, put L2 on the river side, drop "North petal: glass base", and stamp it v0.48. Keep Holman unnamed on the published page. Until the redraw exists, remove the `<img>` (audit prose L203) instead of republishing the v0.18 image.
- **R2 (M). Petal Lineup (T99t) and Sizes (W9RF).**
  - **Best fix:** replace Petal Lineup L112-942 and Sizes L107-937 with the live v48 viewer body. In `The Rose - 3D Model.html` as of 09:40, that's L32727-33798, from `const TAU` through `tick();`; re-find it if the file has changed. The P/CLEFT constants must come along, so don't start at `const O`. Wrap it as `window.createRose=function(){ ... };`, confirm it still reads ROSE_OPTS {host, variant, lite, view, scale, onReady}, and bump the eyebrow and footer to v0.48.
  - **Sizes only:** the 1.0 panel scales the rose but not the stem. Scale the first two stemPts by `O.scale`, or hide the stem when scaled.
  - **Minimum patch if not regenerating:**
    - Move stemPts to G2 (PL 711 / Sizes 706).
    - Change `if(k===3) continue;` to `if(k===3||k===0) continue;` and add the live `// v0.45 stem landing` block (PL 241 / Sizes 236).
    - Delete the rail posts and top rail (PL 720-723 / Sizes 715-718).
    - Change the comment to `// v0.19: the stem is a walkway out to the leaves. A 1.5 m deck rides on top of the boom.` + `// v0.46: no railing (Davey). Open both sides, like a dock.` (PL 714 / Sizes 709).
    - Delete the G6 lobes and leave the comment `// v0.44: the feathered edge lobes (read as green stepping stones) are removed` (PL 732-733 / Sizes 727-728).
    - Petal Lineup L92/L97: "all six" becomes "all seven".
  - **If neither is done, caveat the footers:**
    - Petal Lineup L107: `<footer>Concept v0.28, 26 Sept 2026 (viewer code as of v0.35, 29 Sept). This page compares petal characters only. The stem, sepals, jump petal and kids' slide are drawn as they were then; in the live model (v0.48, 30 Sept) the stem starts from a flat sepal landing at G2, between P3 and P4, and has no railing. Wild versions are seeded, so each one is reproducible and can be tuned petal by petal.</footer>`
    - Sizes L102: the same wording, ending `Loads are estimates until a naval architect runs them.</footer>`
  - Republish both links.
- **R3 (M). Drawing Set (3YPJ).** Regenerate from v0.48, or apply Geometry 1-2 plus text edits 63-65, then republish.
- **R4 (M). Rose artifact (VPwzt).** Republish after the model-page edits, and confirm it serves v0.48.
- **R5 (L). Blender.** After Geometry 3, rebuild the .blend (`-- build`) and re-render `Renders/Slide Petal Study/`, or caption the existing stills "stem schematic, not current".

### model-or-geometry-change
1. **Drawing Set L344-345 (H, B).** Delete the stem top rail at +1.5 and the 13 posts. Keep L346 (thorns) and the gangway rails at L361. Change the L339 comment to `// ---- stem walkway north, 1.5 m, open both sides like a dock (no rail), one compound leaf; gangway south to the dock ----`
2. **Drawing Set L333 (H, A).** Take 324 out of `[36,108,252,324]` (G2 no longer curls). Draw a flat landing at 324° instead, at deck height, from r ~5.9 to 7.75 m, half-width 0.72-0.80 m, per the live model's v0.45 block (`c=CLEFT[0], r0=5.9, r1=7.75, hw=u=>0.72+0.08*u`). Optional: add 180 to the loop so G4 appears, since the drawing never had it.
3. **slide_petal_scene.py L290-296 (M, A).** Delete the stem and both leaves. Add to the header: `The stem is left out: it leaves the flat G2 stem landing at 180 deg here (between Amphi_216 = P3 and Amphi_144 = P4) as an open 1.5 m walkway with no railing, and this scene is mirrored and not turned to the real site.` If a stub is wanted in the shots, use only `tube("Stem", [(-7.4, 0.0, 0.12), (-11.0, 0.0, 0.12), (-17.4, -5.0, 0.12)], 0.42, M["stem"])`, with no posts, rail or leaves. The P2 geometry here now matches v0.48.

### leave-as-history
- **`make_rose_stl.py` geometry and the 5 STLs (v0.4).** Don't splice in a stem. Label them only:
  - L286: `# ---------------- stem slide (v0.4 only, superseded) ----------------`
  - L220: `# spiral stair columns (v0.4 only; gone from the live model: the CLEFT_TH[0] gap is now the flat G2 stem landing and T1 seat steps in P1 are the way up)`
  - Regenerate the whole print from the live model once the petals lock.
- **`Iterations/CHANGELOG.md`, per-version screenshots and viewers, `_candidates/*.js`.** The slide candidate is merged (v0.48); the v0.35 climbing-wall candidate was superseded by v0.37.
- **Crown spec sections 14-15 and L310** (stem under the reverted lap). Annotate per items 55, L252 and L289; don't delete.
- **Community Funding Plan section 4 table** (L75 "The Stem slide", L84 "Changing trailer and showers"). L65 already marks it superseded; optionally delete it and point to the Parts Catalog. Optionally change L134 "planting the sepals" to "finishing the sepals". The C and D fixes live in the Parts Catalog.
- **Design Brief old decision rounds and sections 1-21.** The broad staleness (46 ft float, electric Stove Crown, CLT terraces, flue out the oculus, title "v0.1", status L677, no rows for v0.31-v0.48) needs one structural rewrite pass after these targeted edits, not line patches.
- **Renders:** `The Rose v0.24 - *` (9 stills + flythrough) and `Drawing Set v2/*.png`. Keep them archived. Any render for the Jordan pack or social should be shot fresh from v0.48.

## 3. Per-document status

| Document | Reflects | Status | Issues |
|---|---|---|---|
| Design Brief | Decisions to v0.30 (73), with decision 47 patched for v0.46; body v0.1-v0.2 | stale | 19 |
| Master Plan | Header v0.17; s.9-10 written 09-30 before v0.45; doors and P5 written as decided | stale | 21 |
| Pathways and Capacity | Geometry v0.40/41; before v0.45-v0.48; doors written as the design | stale | 17 |
| Materials Plan | v0.1 (09-27), ~v0.19-v0.24 | stale | 14 |
| Parts Catalog & Raise Stack | v0.21 counts (09-29) | stale | 9 |
| Community Funding Plan | 09-27/29, no version; element table already superseded | minor stale | 2 (history) |
| Crown and DJ Booth Spec | v0.29; v0.34 section not marked reverted | stale | 9 |
| Session Plan | v0.33 | stale | 12 |
| Review Prep | 09-29, money only | minor stale | 2 |
| Slide Petal Study | P2 as of the v0.35 study; its design is now in the model as v0.48 | minor stale | 4 |
| Model page prose (3D Model.html / VPwzt) | Strip and footer v0.48, stem piece v0.46; rest v0.9-v0.22 | stale | 23 |
| Drawing Set (3YPJ) | v0.33 geometry, still has the stem rail | stale | 5 |
| Petal Lineup (T99t) | Labeled v0.28, code ~v0.35 | stale (geometry only) | 7 |
| Sizes (W9RF) | Labeled v0.26, code ~v0.35 | stale (geometry only) | 6 |
| make_rose_stl.py + STLs | v0.4 | stale (frozen) | 4 |
| slide_petal_scene.py + .blend + renders | E5 study; schematic stem | minor stale | 1 |
| Site Overlay PNG (not audited) | v0.18 | stale | 1 |
| Renders v0.24, Drawing Set v2 PNGs (not audited) | v0.24 / v0.33 | history | 0 |
| Claude memory project_the_rose_sauna.md (not audited) | v0.42 | stale | 1 |
| Oslo Strategic Plan (not audited) | Cites "v0.28" | minor stale | 1 |
| Title 28 Brief (not audited) | Current | current (cross-reference only) | 0 |
| 3D model geometry + Iterations/CHANGELOG | v0.48 | current | 0 |