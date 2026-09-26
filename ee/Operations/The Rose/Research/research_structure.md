# The Rose: Structure, Platform, Code and Fabrication Research

Prepared 2026-09-26 for the design brief. Numbers marked **(est.)** are my engineering estimates or rules of thumb, not sourced quotes. Everything else has a source link. None of this replaces a stamped design.

---

## 0. Red flags first

1. **Holman Dock is not "next to OMSI" and is not a sauna dock today.** It sits on the east bank just south of the Hawthorne Bridge. OMSI is roughly 0.5 mi further south, and Tilikum is about 0.9 mi south with the **Marquam (I-5) Bridge in between**, so the Tilikum "backdrop" is distant and partly behind Marquam. Check sightlines on site before the renderings promise it. ([Portland ordinance 191700](https://www.portland.gov/council/documents/ordinance/passed/191700), [portlandbridges.com photo](https://www.portlandbridges.com/00,LM1K0IMG17603,30,0,1,0-portland-oregon.html), [WWeek on The Dock](https://www.wweek.com/culture/2017/06/13/everything-you-needed-to-know-about-portlands-hottest-summer-hangout-the-dock/))
2. **Ownership and use restrictions.** Ordinance 191700 (passed May 8, 2024) transferred the dock from Prosper Portland to PP&R at no cost, with $270K in restricted maintenance funds. The stated use is public recreational river access "particularly for small, non-motorized watercraft" (rowing clubs, kayaks, canoes). The DSL authorization is a **license expiring Sept 7, 2034**, not a commercial lease. The upland piece runs on an annual $1 ODOT permit. A 150,000 lb commercial assembly structure is well outside the dock's current purpose. Plan on the Rose having **its own piles, moorage and DSL lease**, sitting next to Holman rather than on it. ([ordinance 191700](https://www.portland.gov/council/documents/ordinance/passed/191700))
3. **DSL requires a waterway lease for all commercial activity** and for any structure of 2,500 sf or more. New leases run 5 years starting July 1, 2027 (renewals up to 15), and insurance is a lease condition. Structures can't extend more than 25% of the waterway width from the bank. The Lower Willamette River Management Plan can restrict uses. ([DSL waterway authorizations](https://www.oregon.gov/dsl/waterways/pages/authorizations.aspx), [DSL insurance changes](https://www.oregon.gov/dsl/waterways/Documents/WaterwayAuthorizations_Insurance.pdf))
4. **In-water permitting (est., standard for Portland reach):** new piles mean a USACE Section 10/404 permit, NMFS ESA consultation for listed salmon and steelhead, DEQ 401 water quality certification, and City River overlay/greenway land-use review. Pile driving is limited to the in-water work window, typically around July to October for the lower Willamette. Budget 12-24 months for permits.
5. **Portland Title 28 is written for floating homes and boathouses, not assembly buildings.** Commercial loads come from the building code. BDS will likely treat the Rose as an **OSSC (IBC-based) A-3 assembly occupancy on an engineered float**, with Title 28 flotation rules layered on top. That is a novel path, so expect a pre-application conference and possibly Alternate Methods requests. ([Title 28 definitions](https://www.portland.gov/code/28/02/020))
6. **A 3D-printed polymer structure has no code path for an occupied assembly building.** A PE can't just "certify a print." Structural polymer would need ICC-ES evaluation or an OSSC 104.11 alternate-materials approval backed by test data (creep at 90C, fire, UV, water). Inside the hot room, plastic interior finish triggers ASTM E84 flame spread limits, and most printable polymers soften at or below sauna air temperatures. Print the non-structural and cool-side parts only (see section 3).
7. **The 3D-construction printing industry is shaky.** Mighty Buildings went up for sale in Jan-Feb 2025 after layoffs, ICON had major layoffs, and Diamond Age liquidated. Don't build the schedule around a startup. ([3DPI](https://3dprintingindustry.com/news/mighty-buildings-up-for-sale-following-headcount-reduction-235813/), [3DPrint.com](https://3dprint.com/315768/house-3d-printing-company-mighty-buildings-up-for-sale/))

---

## 1. Floating platform options (30-40 ft diameter)

### Load picture for a 36 ft circle (est.)
- Footprint: about 1,018 sf.
- Float self-weight (concrete/EPS): about 60-80 psf, roughly 70,000 lb.
- Superstructure (timber shell, 3-tier benches, insulation, roof decks, heater + stones, fire features): about 50-60 kips.
- People: 40 inside plus about 50 on the petal roofs (5 petals x 10) = 90 x 185 lb (the USCG AAWPP), about 16,700 lb.
- Misc (water, ballast, rails, slide landing): about 7,000 lb.
- **Total displacement about 150,000 lb, which is about 2,400 cu ft of fresh water, for a draft of about 2.4 ft.** Add the Title 28 minimum of 20 in to finished floor and the **float depth is about 4-4.5 ft**, before any reserve buoyancy for water-logging, snow, or later additions.

### Options compared

| Option | Typical use | Pros | Cons | Cost signal |
|---|---|---|---|---|
| **Concrete-encapsulated EPS float** (Bellingham Marine Unifloat, Poralu, and the Portland floating-home style of precast concrete box with steel grid over EPS) | Marinas, Portland floating homes, Arctic Bath (concrete pontoons) | 50+ yr life, heavy and so low in the water, quiet, damps wake motion, fire-resistant deck, familiar to BDS | Heavy to transport. Custom circular/petal shape means custom forms. Crane and barge needed | Concrete docks are quoted at **$200-600/sf** installed ([Fixr](https://www.fixr.com/costs/build-dock), [HomeGuide](https://homeguide.com/costs/cost-to-build-a-dock)). For about 1,000-1,300 sf: **$250K-600K (est.)** for float plus moorage |
| **Timber/steel-framed deck on encapsulated EPS float drums** (Topper's standard) | Commercial and public docks | Cheaper and lighter, shape-flexible, Topper is local (Woodland WA) | Lighter means more motion. Drums are typically at 16-18 in freeboard. Frame must carry concentrated heater and bench loads | Wood/EPS floating docks run about $15-40/sf for simple docks. A heavy engineered platform is more like **$80-150/sf (est.)** |
| **Steel pontoon/barge** (Von Sauna used a Louisiana-built barge) | Floating saunas, event barges | Stiff, fabricator-friendly, can be shaped polygonally (a 14- or 16-gon approximates a circle), void tanks give reserve buoyancy | Corrosion and painting cycles. Hot, loud steel deck. Needs cathodic protection and haul-out surveys | Small barges run about **$1,900-3,000/linear ft** for simple 120 ft hulls. A new 80x30 deck barge was listed at $2.75M ([OpenTug](https://opentug.com/blog/the-cost-of-building-a-barge), [LatestCost](https://latestcost.com/how-much-do-barges-cost-practical-price/)). Custom round: **$300K-700K (est.)** |
| **HDPE modular cubes** (Candock, EZ Dock) | Kayak and PWC docks | Cheap, fast, DIY | Only about **60 psf buoyancy per layer** for Candock, and freeboard is low. Won't carry 150+ psf of combined dead and live load or satisfy an assembly-occupancy reviewer. Joints flex under a crowd | $25-80/sf ([Candock](https://candock.com/products/g2-cube), [Hiseadock](https://www.hiseadock.com/modular-floating-dock-prices-guide/)). **Rule out for the Rose.** Fine for the Thorn or the slide landing |
| **Hybrid: steel or glulam ring frame over EPS-concrete pods** | Custom floating buildings | Pods placed under the heavy zones (heater core, bench rings, petal tips) and trimmed later | More engineering hours | (est.) similar to concrete EPS |

**Recommendation:** go with a concrete-encapsulated EPS float, or steel-ring-framed EPS pods, sized for 150-180 kips with a 20-30% buoyancy reserve. Mass is your friend for a crowd on a roof in boat wakes.

### Topper Industries (topperfloats.com)
- Woodland, WA, 45+ years. Customers include federal, state and local agencies and marine contractors.
- Frames: aluminum, galvanized or painted steel, pressure-treated timber, glulam. Flotation: concrete- or poly-encapsulated EPS block, tub floats, aluminum pontoons. Decking: PT timber, FRP grating, aluminum, cedar, ipe, concrete.
- Standard freeboard is 16-18 in, with custom heights available. They engineer for site wake, current and anchoring. Phone (360) 657-9981.
- No public floating-building portfolio, so ask whether they will carry a building on their float or only supply the float and moorage while someone else's PE does the building. ([Topper floating docks](https://topperfloats.com/floating-docks/), [Topper home](https://topperfloats.com/))
- Note: the ordinance does not name Holman's original builder. The brief's "built by Topper Floats" claim is unverified.

---

## 2. Stability: crowds on the roof

### The physics in plain terms
- **Metacentric height GM = KB + BM - KG.** BM = I/V, where I is the waterplane second moment of area and V is displaced volume. For a circle, I = pi r^4 / 4.
- Wide, shallow circles have **enormous BM**. For the 36 ft circle: I is about 82,400 ft^4 and V about 2,400 ft^3, so **BM is about 34 ft**. Even with the KG raised by roof crowds (whole-structure KG maybe 6-8 ft), **GM comes out around 25-30 ft (est.)**. Initial stability is not the weak point.
- **Heel from asymmetric crowding:** tan(theta) = heeling moment / (displacement x GM).
  - Worst case (est.): all 50 roof people move to the bridge-view petals, about 12 ft off center (111,000 ft-lb), plus 40 interior people shift 6 ft (44,400 ft-lb). Total is about 155,000 ft-lb.
  - At GM = 25 ft that gives **about 2.4 degrees**. At GM = 10 ft (if the float is lighter or narrower than assumed) it gives **about 5.9 degrees, which fails Portland's 4 degree limit.**
- **The real binding constraint is edge freeboard, not GM.** At 2.4 degrees the lee edge 18 ft out drops about 9 in. Portland requires clearance to never fall below one-third of normal. With a 20 in normal clearance, the minimum is 6.7 in, so 20 - 9 = 11 in passes. Petals that cantilever past the float edge make this worse.
- **Portland Title 28.06.040(E)(4)(a):** max list **4.0 degrees**, or clearance above water at the first floor no less than one-third of normal, **whichever is more restrictive**. Resisting moment must exceed applied moment. Min 20 in from waterline to finished floor for occupied structures and 12 in for walkways. **The float, piling, moorage and gangway must have an Oregon-registered Engineer of Record.** Title 28 floating-home live load is 40 psf main floor plus 10 psf upper floors; **commercial uses take building-code loads**. ([28.06](https://www.portland.gov/code/28/06), [28.06.040](https://www.portland.gov/code/28/06/040))
- **Useful cross-check, USCG passenger heel criterion (46 CFR 171.050).** GM >= (N x W x b)/(displacement x tan T), using 185 lb per person, with T the lesser of 14 degrees or the angle that immerses half the freeboard. It doesn't legally apply to a non-vessel, but NAs use it as a benchmark. ([eCFR 171 Subpart B](https://www.ecfr.gov/current/title-46/chapter-I/subchapter-S/part-171/subpart-B), [AAWPP rule](https://www.federalregister.gov/documents/2010/12/14/2010-30391/passenger-weight-and-inspected-vessel-stability-requirements), [USCG stability best practices](https://www.dco.uscg.mil/Portals/9/DCO%20Documents/5p/CG-5PC/CG-CVC/CVC3/references/Stability_Reference_Guide.pdf))

### What the NA/PE will actually check
1. **Weight and CG takeoff** for every element: float, benches, heater stones, stored water, roof crowd. Later an **inclining test or float-trim survey** after construction to verify.
2. **Intact stability** under load cases: lightship; full interior; full roof; everyone on one sector; crowd plus 100-yr wind on the superstructure; crowd plus boat wake. Wakes near the Hawthorne harbor wall are real (the Portland Spirit, jet boats).
3. **Freeboard and edge immersion** vs Title 28 limits. Also check water getting onto the deck at the slide exit and plunge ladders.
4. **Local float strength** (punching under the heater, bench columns, petal support posts).
5. **Mooring:** piles or dolphins, collars, current, **flood stage** (the Willamette rose about 28+ ft at Portland in the 1996 flood, est.), drift logs, ice, and seismic seiche. See ASCE's guidance on permanent moorings for nearshore floating structures. ([ASCE Civil Eng. 2023](https://www.asce.org/publications-and-news/civil-engineering-source/civil-engineering-magazine/issues/magazine-issue/article/2023/09/how-to-design-permanent-moorings-for-nearshore-floating-structures))
6. **Superstructure** to OSSC/ASCE 7:
   - Occupied roofs used for assembly take **100 psf live load**. Assembly areas are 100 psf, and stadium seating with fixed seats is also listed in ASCE 7 Table 4.3-1.
   - Guards of 42 in with a 50 plf / 200 lb concentrated load (IBC 1015/1607.9).
   - Snow and ponding, wind (Portland about 98 mph ultimate, est.), and seismic, though a float isolates much of this.
7. **Egress/fire** (OSSC chapter 10):
   - An occupant load of 50 or more needs 2 exits, and those doors need panic hardware. 3-4 entrances helps here.
   - Occupied roof decks need their own egress paths (IBC 503.1.4, 1006).
   - A gas heater means mechanical code combustion air. Consider a **sprinkler/standpipe question** for A-3 with more than 100 occupants or more than 12,000 sf (probably not triggered, est.).

### Rules of thumb (est.)
- Keep **roof-deck crowd weight under about 10-12% of displacement**, and cap roof occupancy per petal with signage and a host.
- Aim for **design heel of 2 degrees or less** under worst-case crowding so there's margin under Portland's 4 degrees.
- Put ballast and heavy stuff (stones, heater, water tanks) at the center and low.
- Give petals **their own float lobes** instead of cantilevering them past a round float.
- A circle is a stability gift, so don't give it away by cantilevering.

### Vessel vs building
- A permanently moored, non-self-propelled structure not practically designed to carry people or things on water is **not a "vessel"** under 1 USC 3, per *Lozman v. Riviera Beach* (2013). So USCG inspection (Subchapter T/K) does not apply and the building code does. ([Justia Lozman](https://supreme.justia.com/cases/federal/us/568/115/), [Jones Walker summary](https://www.joneswalker.com/en/insights/lozman-v-city-of-riviera-beach-florida-all-that-floats-is-not-a-vessel.html))
- **Don't market "cruises," and don't tow it with guests aboard.** Doing either flips it toward vessel status. The current Columbia sauna "boat" is marketed as a boat, so be deliberate about which regime each unit is in.

### Who certifies
- **Oregon-licensed PE (structural; SE for complex work) as Engineer of Record** for the float, moorage, gangway (Title 28 requirement) and the superstructure.
- **Naval architect** for hydrostatics and stability, working under or alongside the PE.
- **Geotech** for piles.
- **Architect of record** for an A-3 occupancy (Oregon requires a registered architect above certain occupancy and size thresholds, est., so confirm with BDS).
- PNW firms to shortlist:
  - **Elliott Bay Design Group** (Seattle). Did a feasibility and concept design for a 300x100 ft floating pool and entertainment barge. ([EBDG floating entertainment](https://www.ebdg.com/floatingentertainment), [EBDG barges](https://www.ebdg.com/barges))
  - **Glosten** (Seattle). Floating piers and mooring analysis, including the McMurdo floating pier. ([Glosten](https://www.linkedin.com/company/glosten))
  - **Art Anderson Associates** (Bremerton). Naval architecture plus waterfront and civil under one roof. ([artanderson.com](https://artanderson.com/))
  - **Impact Naval Architects** (Bainbridge Island). Small, nimble. ([impactnavarch.com](https://impactnavarch.com/))
  - **Foss Maritime naval architecture** (floating structures). ([Foss](https://www.foss.com/marine-services/naval-architecture-and-marine-engineering/))
  - Also worth calls (from my knowledge, not verified here): **KPFF** (Portland/Seattle, marinas and waterfront), **Moffatt & Nichol** (Portland), **WSP (ex-BergerABAM, floating bridge/pontoon expertise)**, **Reid Middleton** (marinas).
  - Also the **Portland floating-home engineers** that local float builders use. Ask Topper and the Portland floating-home builders who stamps their floats.

---

## 3. Large-format 3D printing

### What exists
- **UMaine ASCC:**
  - 2019 printer: 100 x 22 x 10 ft at about 500 lb/hr.
  - **3Dirigo**: 25 ft, 5,000 lb boat printed in 3 days from a wood-cellulose/plastic blend, 3 Guinness records. ([UMaine 3Dirigo](https://composites.umaine.edu/advanced-manufacturing/3dirigo/), [3DPI](https://3dprintingindustry.com/news/umaine-develops-worlds-largest-3d-printed-boat-and-polymer-3d-printer-163224/))
  - **Factory of the Future 1.0** (Apr 2024, Ingersoll): **96 x 32 x 18 ft**, about 500 lb/hr thermoplastic. A 36 ft Rose shell would fit in one bed. ([UMaine news](https://umaine.edu/news/2024/04/umaines-new-3d-printer-smashes-former-guinness-world-record-to-advance-the-next-generation-of-advanced-manufacturing/), [WBUR](https://www.wbur.org/news/2024/04/24/umaine-3d-printer-biohome))
  - **BioHome3D**: 600 sf, wood flour plus a corn-based bio-resin (PLA-type). Floors, walls and roof were printed in 4 modules and assembled in half a day. ([UMaine BioHome3D](https://composites.umaine.edu/advanced-manufacturing/biohome3d/), [GBA](https://www.greenbuildingadvisor.com/article/u-maine-prints-a-wood-fiber-house))
  - UMaine works through funded research partnerships (MTI boatbuilder cluster, Navy/Navatek $5M, ORNL SM2ART). **Access is a partnership, not a print shop.** Expect a sponsored-research agreement, likely six figures (est.). ([3DPI MTI grant](https://3dprintingindustry.com/news/umaine-receives-500000-to-enable-3d-printing-of-large-scale-boats-141810/))
  - **Wood-PLA softens around 55-60C and is wrong for a sauna hot room.**
- **Branch Technology** (C-Fab freeform lattice, about 20x less material than layered printing) does facade panels. Pricing is by quote only. It's a candidate for exterior petal skins or feature ceilings on the cool side. ([Branch](https://branchtechnology.com/), [VoxelMatters](https://www.voxelmatters.com/branch-technologys-c-fab-process-used-for-giant-3d-printed-facade/))
- **Mighty Buildings** was up for sale in 2025, so don't plan on them.
- **Concrete printing** (ICON etc.) is **too heavy** for a float. Walls at about 145 pcf would roughly double the superstructure weight and wreck the stability math. Use it only for an on-shore element, if anywhere.
- **Printed boats and molds:**
  - Al Seer Marine's 11.98 m, 20-passenger printed water taxi (2023).
  - Printed hull composites using recycled PETG plus basalt fiber show more than 90% strength retention and less than 0.4% water absorption after 24 months of saltwater immersion. ([VoxelMatters](https://www.voxelmatters.com/all-aboard-3d-printed-boats/), [Voltage Vessels](https://www.voxelmatters.com/voltage-vessels-3d-prints-boat-hull-with-proprietary-composite/))
  - Thermwood prints **CF-ABS yacht hull molds** (51 ft). CEAD Faber Navalis prints 4 m-wide hulls. Caracol does robotic LFAM. ([Thermwood](https://www.voxelmatters.com/thermwood-3d-prints-single-hull-mold-for-a-51-foot-long-yacht/), [CEAD maritime](https://ceadgroup.com/segments/large-format-additive-manufacturing-maritime-industry/), [Caracol marine](https://www.caracol-am.com/industries/marine))
  - Pellet feedstock runs about $2-4/lb vs $30-50/lb for filament. ([FacFox](https://facfox.com/docs/kb/scaling-up-cutting-costs-why-fgf-pellet-3d-printing-is-a-game-changer-for-large-scale-parts))
- **Printed saunas:** I found **no full-scale 3D-printed sauna** in searches. Searches surfaced only printed accessories (ladles, noted as needing PETG/ABS over PLA). The Willamette Sauna Festivaali (Feb 2026, Milwaukie Bay Park) had a polycarbonate-panel sauna on a floating platform. That is a sheet product, not a print. ([Portland Monthly Feb 2026](https://www.pdxmonthly.com/health-and-wellness/2026/02/portland-oregon-river-floating-sauna))
  - So the Rose would be a genuine first, which is good for PR and bad for permitting.

### Heat tolerance (sauna air is 80-100C at the ceiling; benches run about 40-60C surface)

| Material | HDT (approx) | Sauna hot room? |
|---|---|---|
| PLA / wood-PLA (BioHome3D-type) | 55-60C | No, it creeps and sags |
| PETG / recycled PETG | about 70-75C | No inside. OK outside (UV-stabilized) |
| CF-PETG / basalt-PETG | about 80-90C (est.) | Marginal, not near the ceiling |
| ABS / CF-ABS | about 95-100C | Marginal, and styrene odor when hot |
| **ASA** | **about 95-100C** | Best practical exterior polymer (UV-stable). Marginal inside |
| PC | about 110-120C | Near-heater capable, but hard to print large and yellows under UV |
| PEI (Ultem), PEEK | 170-200C+ | Survives, but **$50-150+/lb** pellets and very hard to print large (est.) |

Sources: [Siraya ASA](https://siraya.tech/blogs/news/asa-filament-properties), [Snapmaker heat-resistant guide](https://www.snapmaker.com/blog/heat-resistant-filament/), [Digitmakers PC/ABS/ASA/PA-CF](https://www.digitmakers.ca/blogs/news/heat-resistant-parts-comparing-pc-abs-asa-and-pa6-cf), [Wellwhisk HDT chart](https://wellwhisk.com/3d-filament-heat-resistance-chart/)

**Fire code:** IBC chapter 8 sets interior finish classes by occupancy (A-3 needs Class A or B in exits and corridors, and B/C in rooms, per Table 803.13). Chapter 26 requires plastic composites to show flame spread of 200 or less under ASTM E84. Printed polymers generally have no E84 data, so testing would be needed. ([IBC 2024 ch.8](https://codes.iccsafe.org/content/IBC2024P1/chapter-8-interior-finishes), [IBC ch.26](https://codes.iccsafe.org/content/IBC2015/chapter-26-plastic), [Table 803.13 explainer](https://datadrivenaec.com/insights/ibc-interior-finish-requirements))

### Realistic split: what to print vs what to build

| Print it | Build it conventionally |
|---|---|
| **Formwork and molds** for curved petal ribs (bent-lam forms) and for GFRP or concrete float pods. This is the highest-value use of the printer | **Primary structure:** glulam or steel ring beam and radial ribs |
| **Exterior petal shell and cladding panels** in ASA or CF-PETG/basalt-PETG, UV-stable, on a timber subframe | **Hot-room lining and benches:** thermally modified aspen, alder or spruce |
| Roof-deck **guard infill** panels and light-diffuser fins on the exterior | **Float:** concrete/EPS or steel |
| Acoustic baffles in the **changing and cool zones** | Heater enclosure, stone cage, flues (steel, masonry, per the heater manufacturer's clearances) |
| The stem **waterslide** trough could be a printed or FRP molded shell (FRP is the proven slide material) | Stair and ladder structure, guards' posts |
| Signage, handles, the Thorn's exterior | Drapes: fabric plus a steel track |

**Suggested path:** do the CAD and print a scale model now. Commission 1-2 full-scale **exterior petal panels** from a LFAM shop (CEAD/Caracol/Thermwood customers, or a UMaine partnership) as a pilot. Keep structure and the hot room in timber.

### Scale model
- 36 ft at **1:50 is about 8.6 in** diameter, desktop FDM or SLA in one piece. At **1:25 it's about 17.3 in**, so print the core plus separate petals and a **removable roof ring** to show the stadium seating.
- Use SLA (Formlabs-class resin) for detail, or FDM PLA/PETG for size.
- Services: **Craftcloud** (compares quotes across printers), **Xometry** (SLA and Formlabs resins), **Shapeways** (large-format SLA). ([Xometry SLA](https://www.xometry.com/capabilities/3d-printing-service/stereolithography-3d-printing/), [Shapeways SLA](https://www.shapeways.com/3d-print-material-technology/stereolithography))
- Budget (est.): **$150-600 at 1:50, $600-2,500 at 1:25** multi-part with finishing. Or buy a Bambu/Prusa (about $700-1,200) and iterate in house, which is cheaper if there will be more than 3 revisions.
- A model also serves as a weight-and-CG sanity tool: load it with pennies for the crowd and float it in a tub. This is not an engineering test, but it's persuasive in PP&R meetings.

---

## 4. CAD and engineering workflow

1. **Rhino 8 + Grasshopper** ($995 perpetual, Mac and Windows, Grasshopper included) for the parametric rose: petal count, radius, rib spacing, seat tiers, drape tracks. ([Rhino buy](https://www.rhino3d.com/buy/))
2. **Karamba3D** inside Grasshopper for early structural feedback on rib and shell sizing (free trial and educational licenses, paid commercial; see karamba3d.com/buy). ([Karamba3D](https://karamba3d.com/))
3. **Hydrostatics:** Orca3D (a Rhino plug-in for hydrostatics and stability, sold with Rhino; [Orca3D](https://orca3d.com/products/rhino-8)), or a quick Grasshopper waterplane script. This gives the NA a head start. **Fusion 360** also works for shop-level parts and CNC toolpaths, but Rhino is the better architecture and float tool.
4. **Handoff:** the PE rebuilds in **SAP2000/ETABS or RISA** for stamped calcs. The NA uses GHS or Maxsurf for stability. Deliver clean Rhino and STEP geometry plus a **weights and CG spreadsheet**.
5. **Fees (est.):**
   - Structural engineering usually runs about **5-10% of construction cost**. Naval-architecture design fees are often quoted at **10-15% of build cost** for custom boats, with simple drawing packages from $3-5K. ([Cad Crowd rates](https://www.cadcrowd.com/blog/what-are-boat-design-costs-naval-engineering-rates-for-marine-services-companies/))
   - For a **$1-2M floating assembly building**, plan on **$120K-300K total professional fees**: architect of record, SE, NA stability, mooring/geotech, MEP/fire, permitting consultant.
   - A **feasibility and concept stability study** from EBDG/Glosten-class firms is typically **$15K-40K (est.)** and is the right first spend.
   - Post-construction inclining or trim survey: about **$5K-15K (est.)**.

---

## 5. Timber for the petal geometry

| Approach | Where it fits | Cost signal |
|---|---|---|
| **CNC-cut glulam or LVL ribs** (curves cut from straight blanks) | Petal ribs and ring beam. Simplest to engineer | Straight glulam about $9-34/lf. **Curved glulam about $60-120/lf for moderate radius, $90-180/lf on the West Coast for tight radius or deep sections** ([LatestCost](https://latestcost.com/glulam-beam-cost/), [curved glulam guide](https://partner.kurlon.com/news/curved-glulam-beams-cost-price-ranges-drivers-and-ways-to-save-2026-8211-adnan-painting-and-remodeling.html)). Local fabricators: Western Archrib, Structurlam/Mercer, Calvert (est., verify) |
| **Bent lamination** (shop-glued over forms, including 3D-printed forms) | Sweeping petal edges, bench fronts | Mostly labor. Forms are the cost, which is where printing helps |
| **Kerfed plywood / ply ribs** | Non-structural soffits on the cool side | Cheap. **Keep it out of the hot/wet room** (glue lines, delamination) |
| **Thermally modified wood** (aspen, alder, spruce, radiata) | Hot-room lining, benches, backrests. Stable, low resin, no pitch | About **$8+/bf** pre-finished; sauna boards about $3.60-9.40/lf ([Montana Timber](https://www.montanatimberproducts.com/product-applications/thermally-modified-wood/), [Finnish Sauna Builders](https://finnishsaunabuilders.com/collections/sauna-wood-parts/899), [Sauna Marketplace](https://saunamarketplace.com/product-category/sauna-materials/sauna-wood/)). Note that thermally modified wood loses some bending strength, so **don't use it as primary structure** |
| **CLT** | Flat petal roof decks (diaphragms that take 100 psf and 8-12 people), bench-tier platforms | Priced per project. The Mass Timber Price Index publishes an index, not $/sf ([MTC 2024](https://masstimberconference.com/report/content/mass-timber-price-index-2024/)). Budget **about $35-60/sf supplied (est.)**. Heavy, so it counts against displacement |

**Recommendation:** use a glulam ring beam plus radial curved glulam or CNC-LVL ribs. Put CLT or plywood-on-joist flat decks over each petal, with a vapor-closed, insulated envelope. Line the hot room in thermo-aspen or alder, and clad the exterior in printed ASA panels or charred cedar.

---

## 6. Precedents worth pulling for the brief
- **Arctic Bath** (Harads, Sweden, 2020): a circular timber floating spa on **concrete pontoons** with a central cold bath, saunas and 6 rooms, frozen into ice in winter. It's the closest analog to a round communal floating wellness building. ([Designboom](https://www.designboom.com/architecture/sweden-floating-circular-arctic-bath-hotel-opens-lule-river-01-23-2020/), [Archello](https://archello.com/project/arctic-bath))
- **Big Branzino** (Stockholm): a timber sauna on a steel catamaran hull with a recessed roof terrace. ([Dwell](https://www.dwell.com/article/big-branzino-sandellsandberg-arkitekter-floating-sauna-dbe6a523))
- **Von Sauna** (Kirkland, WA): barge built in Louisiana, sauna room built in Michigan, 18 seats. **Wild Haus** (Ballard-built). ([Future Tides](https://www.futuretides.org/floating-sauna-wild-haus-von-sauna-seattle-pacific-northwest/), [Traveling Tessie](https://www.travelingtessie.com/allposts/floating-sauna-in-seattle))
- **EBDG floating pool and entertainment barge study** (300x100 ft).
- **Fjord floating sauna** (SF Bay, shipping containers, 2025). ([Dezeen](https://www.dezeen.com/2025/07/03/fjord-floating-sauna-shipping-containers-san-francisco-bay/))
- **Human Access Project** (Portland Willamette access advocates; Guss sauna partner): a natural ally for the City conversation. ([HAP Guss](https://humanaccessproject.com/programs/guss_sauna))
