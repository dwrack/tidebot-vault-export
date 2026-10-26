# Private Saunas (V2): Stove + Flue Placement from LiDAR (Oct 15 2026)

Built 2026-10-15 from Davey's Scaniverse scan of the stove corner (`Assets/V2 Build Drawings/2026-10-15 LiDAR scan - East (Sunrise) stove corner (Scaniverse).ply`, 417K points) and the Torch TS-60F/80F installation manual (`Assets/V2 Build Drawings/Torch TS-60F-80F Installation Manual.pdf`, pages 5, 7, 8). Schematic: `Assets/V2 Build Drawings/2026-10-15 East (Sunrise) stove + flue placement from LiDAR.png` (plan, section, ceiling cross-section, ceiling height map).

This is the "mark the flue for the roofers" fallback from the [[Private Saunas (V2) — Site Walk with Grant (Oct 15 2026)]]. Companion to the Rev K coordination plan.

**Which sauna:** **East (Sunrise)**, the one with the round window (Davey, 2026-10-15). The scanned corner is the front wall meeting the east wall; the window RO that starts ~7" past the front-wall framing is the 6'×6' square RO behind the round trim. West (Sunset) not scanned yet; its stove corner mirrors this one, but rafter positions and the collar height need their own tape or scan.

---

## The three numbers (per stove, Rev C orientation: stove back to the front wall, intake neck through it)

| What | Number | Source |
|---|---|---|
| Flue centerline, out from the **finished** front wall | **10.58"** (= 4" clearance + 6.58" to the collar) | Torch p.7 TS-80F drawing: the 10.58 dimension runs from the clearance line, not the stove back |
| Flue centerline, out from the front-wall **stud face** | **≈11.8"** (10.58 + ~1¼" finish build-up; re-measure once the finish thickness is known) | derived |
| Flue centerline, along the front wall from the side-wall **finish** / **stud face** | **22.6" / ≈23.8"** (12" clearance + half of 21.12") | Torch p.7 |

The flue goes straight up from there. The intake-neck opening is 18" wide × 15" tall with its sill 3" AFF, centered on the stove width (so centered ≈23.8" from the side-wall framing).

> ⚠️ Correction: the site-walk note said "14⅝" from the finished face of the front wall." That added the 4" twice. It is **10⅝"**. Fixed there too.

## What the scan shows

| Item | Measured | Matters because |
|---|---|---|
| Front wall | studs 3½" deep, faces ~16" OC from the corner, sheathed outside | intake hole must land in a stud bay; the 18" opening centered at 23.8" spans ≈14.8" to 32.8", so the stud near 33" may need to move or the opening gets headed |
| Front wall thickness | 3½" studs + exterior sheathing/T&G + interior finish ≈ **5½–6"** | Torch: over 5" needs the **recessed intake box or flashing** (p.4). Rev K assumed 3¾". Ask Paul which part |
| Side wall window RO | starts ≈7" out from the front-wall framing, sill ≈6–8" AFF, head ≈75–79" | the stove sits beside glass for its full depth, 12" away; Rev K issues 1 and 2 still need Torch's OK on glass at 12" |
| Ceiling | exposed **2×6 rafters** (Grant confirmed 10/16) running parallel to the front wall, T&G on top. T&G at ≈90" AFF at the side wall, rising ≈1¼" per ft toward the door (≈92" at the flue) | the ceiling is the roof underside, so a **cathedral** support box, no attic shield |
| **Rafter positions** | first rafter ≈11–13" out from the front-wall framing (bottom ≈85"), next ≈25–27" | **the flue centerline (11.8") is dead on the first rafter** |
| Roof pitch | ≈1¼:12 (shallow shed) | flashing for 0/12–6/12; roofer wants mechanically seamed standing seam |

## The rafter conflict, and the fix

The 6" Class A needs a 12¼" square framed opening (DuraTech table 1, cathedral box) with 2" clear to any wood. Centered at 11.8" that opening runs from ≈5.7" to ≈18" out from the wall, straight through the first rafter. The stove cannot move away from the wall (the neck has to pass through it), and the rafter runs parallel to the wall, so sliding the stove along the wall does not help.

**Do this:** Grant cuts that rafter and headers it, doubled 2×6 headers on joist hangers at roughly 16" and 32" along the wall, trimmer on the open side, so the finished hole is 12¼" square (bigger is fine) centered on the flue. The support box and its trim hide the cut from inside. Tell Cameron the exact spot before panel layout so no seam lands there (that was Grant's own ask on 10/15).

Not recommended: offsetting the pipe with elbows to reach the next bay (Torch penalizes horizontals and elbows on draft; the connector run is only ~55").

## Pipe: what to order (per stove, 6" DuraVent, or the Selkirk/Metal-Fab equivalents)

Torch rules that drive this (manual p.5): Class A chimney rated ≥800°F with vertical termination (UL 103 HT Class A is rated 2100°F, so any of them qualify); cap ≥3 ft above the roof at the exit and ≥2 ft above anything within 10 ft; ≥6 ft of draft from the stove top; horizontals only in double-wall or insulated pipe; controls and flue by a licensed pro. Torch's own FAQ: double-wall black pipe from the stove to the ceiling, insulated chimney from the ceiling up.

**Why double-wall, not single-wall, inside the room:** the flue center is 10.58" from the front wall. DVL double-wall is 8" OD, so its surface is 6.58" from the wall, and DVL is listed at 6" to combustibles. Single-wall black pipe needs 18". Cement board over wood studs still counts as combustible. So the connector has to be DVL (or Class A all the way down).

| Qty | Part | Note |
|---|---|---|
| 2 | 6" DVL 24" sections (6DVL-24) | connector run ≈55" (92" ceiling − 3" box − ≈33" collar); tape the collar height |
| 1 | 6" DVL adjustable section (≈12–17") | takes up the slack |
| 1 | 6DVL-ADT DVL-to-DuraTech adapter | only if the supplier says the CS11 box does not accept DVL directly |
| 1 | 6DT-CS11 cathedral ceiling support box with its two-piece trim | 12¼" framed opening; must sit ≥3" below the T&G |
| 1 | 6DT-48 Class A | from the box, through the roof, up |
| 1 | 6DT-12 Class A | brings the cap to ≈44" above the roof surface (the roof's own high edge 8 ft away is ~10" higher than the exit point, so 36" is tight; 44" clears it with margin). Installed heights are 1¼" less per section |
| 1 | 6DT-SC storm collar | |
| 1 | 6DT-VC rain cap | |
| 1 | 6DT-RB extended roof bracket | required over 5 ft above the roof; order it anyway, this is a 4 ft stack on a float in Columbia wind |
| 1 | roof flashing, **decided with Cameron** | DuraTech 6DT-F6 fits 0/12–6/12 on a shingle roof. On mechanically seamed standing seam most roofers want a high-temp silicone boot (DuraVent universal rubber boot flashing or a Master Flash HT) on a flat pan they fabricate. Do not order flashing until he says which |
| 1 | tube high-temp (1000°F) sealant | storm collar and flashing |
| 1 | Torch recessed intake box or extension | if the finished front wall is over 5" (it will be) |

Skip: attic insulation shield (no cavity), wall thimble, elbows.

Double everything for two saunas. Prices not pulled; Rockford Chimney Supply, Woodland Direct and the local hearth shops all stock DuraVent, and Grant can price the Selkirk equivalent at his supplier.

## Before anyone cuts

1. Davey: scan the West (Sunset) stove corner the same way.
2. Grant: tape the as-built finish build-up on the front wall and the stove collar height off the floor (not in the manual, Torch box is ~32" tall). Both shift the numbers above by that much.
3. Grant: confirm the front-wall rafter spacing and header the first rafter at the flue.
4. Hannah or Davey to Paul at Torch (906-376-4076): recessed intake box for a 5½–6" wall; OK to have a window 12" from the stove side; CO detector location.
5. Cameron: flashing type for the standing-seam roof; mark the penetration center on the sheathing for him.

Verified 2026-10-15 against the scan and the manual. Finish thicknesses and collar height are assumptions until taped.


---

## 2026-10-16 addendum: detail drawings + double-check

**Drawing set (7 sheets):** `Assets/V2 Build Drawings/2026-10-16 East stove flue - rafter header + penetration detail.pdf`. Sheet 1 roof framing plan (cut R1, headers H1/H2, blocking B1/B2, 12¼" opening), 2 section through the flue, 3 section along R1, 4 intake-neck opening vs the studs, 5 heat shield / what is wood near the stove, 6 layout steps for Grant, 7 setback by finish.

**Corrections from the re-check (fresh load of the scan):**
- Rafters are **2×6** (Grant, 2026-10-16; the scan read 6.5–7" deep, which was wrong by about an inch). R1 center 12.0" out, R2 center 27.0" (≈16" OC). Headers H1/H2 are doubled 2×6, blocking single 2×6; drawing set re-issued.
- East-wall window RO starts **≈6"** out from the front-wall framing (not 7").
- Front-wall studs at 0, 14.5–16", 30.5–32", 37.5–39.5" (door king). Both middle studs fall inside the 18" intake opening: jacks + header + sill.
- DVL 6" OD is 7¼" (not 8"). Surface sits 7.0" from the front-wall finish, over the 6" listed. Conclusion unchanged: DVL double-wall, never single-wall.
- Torch p.7 re-measured in pixels: 10.58" is clearance-line → flue center. Stands.

**Setback depends on the finish (sheet 7).** Torch measures from the outer face of the finish, so the stove and the flue move out by the finish thickness:

| Stove-zone finish | build-up | flue center from stud faces (along / out) |
|---|---|---|
| A: ½" cement board + ⅜" tile on the studs | 1.0" | 23.6" / 11.6" |
| **B: ventilated shield, 1" spacer + CBU + tile (recommended)** | 2.0" | **24.5" / 12.5"** |
| C: ¾" T&G on ½" furring (sheets 1–6 drawn to this) | 1.25" | 23.8" / 11.8" |
| D: ¾" T&G on 1" furring | 1.75" | 24.3" / 12.3" |

All four land on rafter R1, so the header detail holds. Pick the finish first, then mark the flue, then cut. Tile does **not** reduce the 12"; it protects the wood and, built ventilated, keeps the studs cool. Both pony walls steel-stud + cement board so nothing combustible is inside the 12".

**West (Sunset):** mirror image (stove 12" off the west wall, flue 10.58" off the front-wall finish) but rafter and stud positions unknown until it is scanned. Do not reuse the East numbers there.

**Intake dimensions (added to sheets 2 and 4, 2026-10-16, Torch p.7/p.8):** wall opening 18" wide × 15" tall, sill 3" above finished floor, opening edge ≥13.5" from the finished side wall (we have 13.6"). Neck 14" wide, **5.02" long measured from the finished inside face**. Valve/intake box 5.16" deep × 15.66" tall on the far end of the neck, 2½" of open air under it, flashing on any wood below. Our front wall is ≈6" finish-to-exterior, so the 5.02" neck ends inside the wall: order Torch's recessed box / extension with Paul.


## 2026-10-16 (later): walls are 1⅞" thick inside, numbers re-issued

Grant is furring vertical then horizontal for an air gap, then ¾" cedar T&G: **1⅞" build-up on the walls** (ceiling unchanged). Torch measures from the finished face, so everything moves out by 1⅞" from the studs. Drawing set re-issued.

| | From the FINISHED face | From the STUD face |
|---|---|---|
| Stove back off the front wall | 4" | 5⅞" |
| Stove side off the east wall | 12" | 13⅞" |
| **Flue center, along the front wall** | 22.56" | **24.4"** |
| **Flue center, out from the front wall** | 10.58" | **12.5"** |
| 12¼" roof opening, along | | 18.3" → 30.6" |
| 12¼" roof opening, out | | 6.3" → 18.6" |
| Cut R1 between (headers outside) | | 15.3" → 33.6" |
| Blocking B1 / B2 (out) | | 4.8–6.3" and 18.6–20.1" |
| Intake RO 18" wide, centered on the flue | edge 13.5" from the east finish (Torch min 13.5": exactly at it) | 15.4" → 33.4" |
| Wall thickness at the neck | 3½" + ≈1¼" outside + 1⅞" inside = **≈6⅝"** | Torch neck is 5.02": recessed box required |

Rafter check: R1 sits at 11.2–12.8" out; the flue at 12.5" is still on it, at the far edge. Header detail unchanged. Front-wall stud at 14.5–16" now straddles the RO edge (15.4"); it gets cut and becomes the jack. DVL clearance to the finish is still 7.0" (pipe OD 7¼", center 10.58" from finish). The tile shield would add on top of 1⅞"; sheet 7 row D shows that case (2¾").


## Pipe height to order + where to call (2026-10-16)

Per sauna, 6" throughout: stove collar ≈33" → ceiling box bottom 89" = **≈56" of DVL double-wall** (2 × 24" + one adjustable 12–17"); box bottom → cap base ≈142" = **≈53" of Class A** (6DT-48 + 6DT-12; swap the 12" for a 24" if the roof build-up is over 6"). Total stack collar-to-cap ≈109" = **9 ft**. Two saunas: 4 × 6DVL-24, 2 × DVL adjustable, 2 × 6DT-48, 2 × 6DT-12, 2 × 6DT-CS11, 2 storm collars, 2 caps, 2 roof brackets, flashing per Cameron.

Torch requires a licensed pro for the flue. Phone numbers are from directories, confirm when calling:

| # | Who | Phone | Why |
|---|---|---|---|
| 1 | Lisac's Fireplaces & Stoves, 12518 NE Airport Way | 503-261-1000 | biggest hearth showroom in town, stocks DuraVent, has installers |
| 2 | American Chimney & Masonry, NE 50th | 503-644-0393 | CSIA-certified, does stove + flue installs, 4.9 stars |
| 3 | Portland Fireplace and Chimney, NE Halsey | 503-758-4710 | CSIA, installs and inspects; ask if DuraTech-trained |
| 4 | Buck's Stove Palace, SE Foster (or Homestead Stove Co, 503-282-3615) | 503-771-3374 | old-school stove shop, parts over the counter |
| 5 | Rockford Chimney Supply (online, ships in days) | 866-708-2446 | cheapest for the full 6" cathedral kit; Grant installs, chimney co. inspects |


## Call with Torch (Paul), 2026-10-16: confirms the plan

Davey's call notes (voice transcript, paraphrased): 6" double-wall black pipe inside, sold in fixed lengths plus a telescoping piece; Selkirk makes the Supervent line sold at Lowe's/Menards (DuraVent is the equivalent); the 1:12 ceiling needs a **cathedral support box**; above the ceiling switch to the insulated (shiny) Class A; storm collar, cap and roof bracket come later; metal roof → likely a **rubber boot flashing**, metal flashing is possible but he is less familiar; install through a **chimney guy, not HVAC** (Davey has a buddy), and just call it a stove or fireplace flue. Nothing in the call changes the drawings.

Selkirk equivalents if buying at Lowe's: 6" Supervent (JSC6) Class A lengths; Selkirk DSP 6" double-wall stovepipe + telescoping section; Supervent cathedral ceiling support box; Supervent adjustable flashing (0/12–6/12) or a high-temp silicone boot for the standing seam. Don't mix brands within the Class A run; the connector pipe can be either.


## 2026-10-19 status
- **Adam Reich (chimney) is a go for Friday 10/23.** Invoice coming 10/19. Flues go in Friday; stoves get set after the tile floor is laid.
- **Roofer note (Cameron):** start the standing-seam panel layout AT the pipe and work away from it, so no seam lands under the boot flashing if it can be helped. Added to Adam's brief and the sequence.
