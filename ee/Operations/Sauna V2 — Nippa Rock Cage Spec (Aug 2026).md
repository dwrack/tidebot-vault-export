# Sauna V2 — Custom Rock Cage Spec (Nippa G-Series)

> **OBSOLETE 2026-09-08.** Nippa replied Aug 21: gas stoves not being sold ("changes being made") and no accessory rock surrounds. We pivoted to Torch (2× 80k NG, order #XBOFD). The Part B free-standing skirt concept may carry over to Torch (they allow free-standing surrounds) but would need re-drawing for Torch dims. Current state: `Private Saunas (V2) — Build Status (Sept 2026).md`. The fabrication spec below (316L, slots, thermal expansion, passivation) is still good reference if a skirt gets re-specced.

Created 2026-08-12. For the two V2 saunas ("Sunrise" and "Sunset"), each getting a Nippa natural-gas stove.

Related: [[Sauna V2 — Design Notes (Aug 2026)]], Sauna V2 Build Plan memory

**Drawing set (send this link to Nippa):** https://claude.ai/code/artifact/3d20cf50-0232-4d1a-924b-042003b2d384 — dimensioned plan, elevations, load-path diagram and slot detail. Private until shared from the page's share menu.

**Direction locked (Davey, 2026-08-12):**
- Geometry: **hybrid** — tall rock basket on top + 3-sided rock skirt, open front
- Fabrication: **Nippa builds to our drawing**, ships mounted on the stoves
- Material: **316L stainless, bead-blast matte**

---

## 1. What we actually know about the stove

Pulled from nippa.com G-Series pages, 2026-08-12. Everything here is published spec, not assumption.

| Spec | G-60 | G-75 | G-90 |
|---|---|---|---|
| BTU | 60,000 | 75,000 | 90,000 |
| Body L × W × H | 18" × 18.5" × 28" | **22" × 18.5" × 28"** | **22" × 18.5" × 28"** |
| Rated room volume | 750 ft³ | 1,200 ft³ | 2,000 ft³ |
| Flue | 4" dia w/ draft diverter | same | same |
| Clearance to combustibles | 24" | 24" | 24" |
| Clearance to non-combustibles | 6" | 6" | 6" |
| Min. clearance to ceiling | 40" | 40" | 40" |
| Fuel | NG or LP | NG or LP | NG or LP |
| List price | $3,900 | $3,900 (starting) | $3,900 (starting) |

Also published for the gas line generally:
- Stock rock capacity: **140–160 lbs**
- Combustion air extension opening: **14"W × 24"H × 11"D**
- Standard equipment: 1-hour timer, thermostat, pilot light, safety shut-off valve, combustion air extension, draft diverter

**The useful finding: G-75 and G-90 are the same box.** The builder is still researching heater-to-room ratio given the larger glass area on both saunas. That decision does not block this. As long as we land on G-75 or G-90, the cage drawing is identical. Only a drop to G-60 changes it (body gets 4" shorter in length).

Nippa LLC — 8862 US-31, Beulah, MI · 231-882-7707 · Discover@nippa.com · Mon–Fri 9–5 ET

---

## 2. Three constraints that shape the whole design

### 2.1 The 40" ceiling clearance is the hard ceiling on basket height

Nippa requires a minimum 40" clearance to the ceiling. **We do not yet know what that 40" is measured from** — top of the stove body, top of the rock bed, or top of the draft diverter. It matters enormously:

- If measured from the 28" stove top, ceiling sits at 68" minimum. A 10" basket eats 10" of that and puts us out of spec unless the ceiling goes up.
- Every inch of extra rock depth is an inch the builder has to add to the ceiling height.

This is TBD-5 below and it is the single question that most affects the design. **It also needs to reach the builder before he finalizes ceiling heights on Sunrise and Sunset.** Adding it after framing is expensive; adding it now is free.

### 2.2 The top plate has a rated rock load, and the heat exchanger is under it

Piling extra rock on the firebox top loads the heat exchanger and slows heat transfer through the bed. Nippa rates the stock bed at 140–160 lbs for a reason. We should not blow past that number on our own authority.

**This is why the skirt is the right move.** The 3-sided skirt is a free-standing weldment that carries its own load to the deck — the stove sits inside it, the skirt does not hang off the stove. That gets us most of the added thermal mass without touching the appliance's rated load at all, and it keeps Part B outside the scope of anything that could void the certification.

### 2.3 The combustion air extension may kill the rear panel

Nippa publishes the combustion air extension opening as **14"W × 24"H × 11"D**. The stove is only 18.5" wide and 28" tall. That opening is nearly the entire rear face.

If the air extension exits the back, **the rear rock channel cannot exist** and we fall back to a two-sided skirt (roughly 90 lbs less rock per stove). Find this out before Nippa quotes, not after. TBD-6.

### 2.4 This is a boat

Every pound of rock is a pound on the float. See the weight table in §5. Two stoves fully skirted can add 600–1,000 lbs to the platform. That needs to land in the builder's load calc before the float is ordered, not after.

---

## 3. The design

Two separate parts. They ship together and read as one piece, but they are engineered differently and only one of them touches the appliance.

### Part A — Top basket ("the crown")

Bolts to the existing top-plate rock rail. This is the part Nippa has to own, because it modifies a listed gas appliance.

| Item | Spec |
|---|---|
| Footprint | 22" × 18.5" outer, flush with the stove body |
| Height above top plate | **8" nominal** — hold pending TBD-5, go to 10–12" if the 40" datum allows and the builder raises the ceiling |
| Rock depth | ~7" usable |
| Flue passthrough | Cut and framed around the 4" collar + draft diverter, per TBD-2. Rock must not contact or bear on the diverter. |
| Attachment | 5/16"-18 316 SS hardware into existing top-plate points. **Slotted holes, 3/16" oversize in the long axis** (see §4.3). No field welding to the appliance. |
| Rock spec | 2"–4" Nippa-supplied or equivalent peridotite/olivine. Larger stone on top, no fines. |

### Part B — 3-sided skirt

Free-standing. Left, right, and rear rock channels on a welded leg frame. **Front stays fully open** for the burner, gas valve, pilot, thermostat, 1-hour timer, and safety shut-off.

| Item | Spec |
|---|---|
| Configuration | 3 sides, open front, self-supporting on its own legs to the deck |
| Standoff from stove skin | **1" air gap.** Rock is heated by radiation and convection in the gap, not by direct conduction against the skin. Confirm acceptable per TBD-8. |
| Channel depth (rock thickness) | **4" nominal** — see the weight table before committing |
| Channel height | **16" nominal**, top edge flush with the underside of the top basket, bottom edge ~12" above deck. Keeps the controls zone clear and cuts the weight roughly in half vs. a full-height skirt. |
| Rear cutout | Required if the combustion air extension exits the rear (TBD-6). Must not be obstructed. |
| Load path | Skirt carries its own weight to the deck. It does not touch or hang from the stove. The stove is removable without disassembling the skirt. |
| Rock spec | 3"–5" peridotite/olivine. No water contact here, so bias toward mass over surface area. |

**Do not use Columbia River rock.** Non-porous water-rounded stone traps moisture and can spall or burst at temperature. Sauna stone only.

---

## 4. Fabrication spec

### 4.1 Material

- **Perforated panels:** 11 ga (0.120") 316L stainless
- **Frame, corner posts, top and bottom rails, channel floors:** 3/16" (0.187") 316L stainless
- 316L, not 304. Constant humidity plus water thrown on hot metal on a river platform will tea-stain 304 within a few seasons. 316L's molybdenum content is the whole reason to pay the premium here.

### 4.2 Slot pattern

Waterjet preferred over laser for the perforated panels — no heat-affected zone means less warping on thin 316L.

| Item | Spec |
|---|---|
| Slot size | 7/8" W × 4" H, full radius ends |
| Web | 3/4" all around |
| Layout | Staggered, 50% row offset |
| Open area | ~45% |

The 7/8" slot width is deliberate: it is comfortably narrower than the smallest 2" stone, so nothing works its way out, while 45% open area keeps convection through the bed alive. Below about 30% open the rock at the bottom of the basket never comes up to temperature.

### 4.3 Thermal expansion — the thing that kills stainless rock cages

316 stainless expands at roughly 9.9 × 10⁻⁶ in/in/°F. Across the 22" long axis with a 500°F swing that is **0.11", call it 7/64"**. A fully welded box with tight bolt holes will bow, crack a weld, or pull its fasteners.

Mitigations, all of them:
- Every fastener hole slotted 3/16" oversize in the long axis
- No fully-welded closed boxes. Corner posts bolted, or slip joints at two of four corners.
- 3/16" frame stock (not 11 ga) everywhere load is carried, so the frame stays stiff enough not to oil-can
- Nickel-based high-temp anti-seize on all threads
- All-metal 316 lock nuts or safety wire. Split lock washers will not survive the thermal cycling.

### 4.4 Welding and finish

- TIG (GTAW), 316L filler, back-purge on all visible faces
- Blend all welds, then bead blast
- **Glass bead #80–120, dedicated stainless-only media.** If the shop blasts with media that has touched carbon steel it embeds iron particles and the part rusts in a season.
- **Passivate after blasting** per ASTM A967 (citric or nitric). Call this out explicitly on the drawing — it is the step shops skip.
- No paint, no powder coat, no plating. It burns off.

### 4.5 Tolerances

- ±1/32" on cut features
- ±1/16" on overall weldment
- Flatness on mating faces to the top plate: 1/16" over the full span

### 4.6 Quantity

- **2 complete sets** (Sunrise + Sunset)
- 1 spare hardware kit per set
- Ship installed on the stoves where practical; skirt may ship knocked down flat to save freight

---

## 5. Weight table — pick a number before Nippa quotes

Rock at ~105 lb/ft³ loose-packed peridotite. Per stove, skirt only.

| Skirt height | 3" deep | 4" deep | 5" deep |
|---|---|---|---|
| 14" | 160 lbs | 213 lbs | 266 lbs |
| **16" (rec.)** | **182 lbs** | **243 lbs** | **304 lbs** |
| 22" (full height) | 251 lbs | 334 lbs | 418 lbs |

Add per stove: ~40 lbs extra top rock over stock, plus ~60–80 lbs of 316L steel.

**At the recommended 16" × 4":** roughly **+345 lbs per stove, +690 lbs across both saunas.** That number goes to the builder for the float load calc.

If the float math gets tight, drop to 16" × 3" and save 120 lbs across both boats. The thermal difference at that margin is small; the buoyancy difference is not.

---

## 6. TBD register — what we need from Nippa

Numbered so the reply can be checked off item by item.

| # | What we need | Why it matters |
|---|---|---|
| TBD-1 | Top plate outer dimensions and existing rock-rail geometry. **DXF or STEP preferred**, dimensioned PDF acceptable. | Can't draw the basket without it |
| TBD-2 | Flue collar centerline (X,Y from a stated datum corner), collar OD, and draft-diverter footprint OD + height above the top plate | Basket has to frame around it with clearance |
| TBD-3 | Max rated rock load on the top plate in lbs, and whether it can be exceeded with a redesigned basket | Governs how tall the crown can go |
| TBD-4 | Heat exchanger / burner tube layout beneath the rock bed. Any zones that must stay clear or must stay covered. | Uneven rock coverage over a heat exchanger is how they crack |
| TBD-5 | **What is the 40" minimum ceiling clearance measured from?** Top of body, top of rock, or top of diverter? | Highest-priority item. Drives the builder's ceiling height on both saunas. |
| TBD-6 | Combustion air extension: which face it exits, and its position. Confirm the 14"W × 24"H × 11"D opening. | Rear skirt panel may need a cutout |
| TBD-7 | Face locations of gas valve, pilot access, thermostat sensing bulb, 1-hour timer, safety shut-off | Confirms the open front is on the correct side and nothing is buried |
| TBD-8 | Max allowable skin temperature, and whether a 1" standoff rock channel on 3 faces is acceptable | The whole skirt concept depends on this yes |
| TBD-9 | Certification listing (CSA / ANSI Z21.__ or equivalent) and what modifications void it. **Will a Nippa-fabricated cage keep the stove listed?** | Gas permit and insurance on a commercial floating structure |
| TBD-10 | Existing threaded bosses or mounting tabs on the top plate available for bolting | Avoids drilling the appliance |
| TBD-11 | Stove dry weight, and whether cages can ship installed | Float load calc + freight |
| TBD-12 | Their stock rock spec: type, size range, lbs supplied per stove | So we match, and so we know how much extra to order |

---

## 7. Sequence

1. **Send the Nippa email** (draft below) with the TBD register. Ask for the DXF first — everything downstream waits on it.
2. **Simultaneously, get TBD-5 to the builder and Kyle.** Ceiling height is a framing decision and it is live right now.
3. Nippa returns drawings → we produce dimensioned CAD for the cage → Nippa quotes.
4. Confirm G-75 vs G-90 once the builder finishes the heater-to-room ratio research. Cage unaffected either way.
5. Approve, deposit, and put the cages on the same PO as the stoves so they ship together.

**Open items owned by us:** none of this is blocked on the interior-wood conflict or the window decisions. It can run in parallel.

---

## 8. Draft email to Nippa

> **To:** Discover@nippa.com
> **Subject:** Custom rock cage spec for two G-Series gas stoves — commercial floating sauna

Hey,

We're building two commercial floating saunas on the Columbia River in Portland and we'll be running a Nippa gas stove in each one. Likely G-75 or G-90 depending on where our builder lands on heater-to-room ratio, though I understand those two share the same body.

We want to add more thermal mass than the stock rock bed gives us, and we'd like you to fabricate the cages so they arrive mounted on the stoves. Two parts:

1. A taller rock basket that bolts to the existing top-plate rail
2. A free-standing 3-sided rock skirt around the sides and back, open at the front for burner and control access. The skirt carries its own weight to the deck and would not hang off the stove.

Both in 316L stainless, bead-blast finish, since we're on the water year-round.

Before we can draw anything, we need some numbers from you:

1. Top plate outer dimensions and the existing rock rail geometry. A DXF or STEP file would be ideal, a dimensioned PDF works too.
2. Flue collar centerline location, collar OD, and the draft diverter footprint and height above the top plate.
3. Max rated rock load on the top plate, and whether that can be exceeded with a redesigned basket.
4. Heat exchanger and burner tube layout under the rock bed. Any zones that need to stay clear, or that need to stay covered.
5. This one's the most urgent: **what is the 40" minimum ceiling clearance measured from?** Top of the stove body, top of the rocks, or top of the draft diverter? Our builder is finalizing ceiling heights right now and a taller rock bed changes his framing.
6. Which face the combustion air extension exits, and its position.
7. Where the gas valve, pilot access, thermostat bulb, 1-hour timer, and safety shut-off sit, so we put the open face on the right side.
8. Max allowable skin temperature, and whether a rock channel standing off 1" from three faces is acceptable to you.
9. What the stove is listed under, and whether a cage you fabricate keeps that listing intact. This matters for our gas permit and our insurance.
10. Any existing threaded bosses or mounting tabs on the top plate we can bolt to instead of drilling.
11. Stove dry weight, and whether you can ship the cages installed.
12. Your stock rock spec — type, size range, and pounds supplied per stove.

Once we have 1 through 4 we'll send dimensioned drawings for you to quote. Quantity is two complete sets.

Could you get us the top plate drawing and the answer to #5 by **Friday, August 21**? The rest can follow.

Thanks!

Ebb & Ember
sauna@ebbandember.com

---

## 9. Notes and cautions

- **Do not order rock from a landscape supplier.** Peridotite/olivine sauna stone only. River rock and granite spall.
- Nippa's willingness to weld extra cages was noted back in the original stove evaluation. Hold them to it, and get the listing question (TBD-9) answered in writing, not on a phone call.
- If Nippa declines to fabricate, fallback is a local Portland waterjet shop cutting Part B only — the free-standing skirt touches nothing on the appliance, so it can be built without their sign-off. Part A cannot.
- Budget: not estimated here. Get Nippa's quote on the drawing package rather than guessing.
