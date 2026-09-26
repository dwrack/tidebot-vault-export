# The Rose: heat, stove, tiers, drapes (research notes)

Prepared 2026-09-26 for the Rose design brief (30-50 bather circular communal floating sauna, Holman Dock proposal). Numbers marked **[est]** are my engineering estimates, not vendor figures. Everything else is sourced below.

---

## 0. Red flags first

1. **The Holman Dock rules are stricter than "no fuel equipment".** PP&R's Short Term Boat Launch and Moorage Rules (PRK-1.17), rule 5: "Open flames, live coals, or devices containing or using them or other combustible materials, including but not limited to barbecues, hibachis, stoves, and heaters, are not permitted on docks." Rule 4: "No garbage, electrical or waste water services are provided on PP&R docks." The 2026 commercial activity guidelines add: "We do not allow generators, fuel-based motors, or similar items." And the only utility PP&R lists is 110V/20A electricity at $36.50/month. So:
   - Gas and wood are out unless the lease/LOI explicitly carves out an exception. Don't plan on one.
   - Even electric "heaters" arguably sit inside rule 5's wording. Get written carve-out language in the LOI.
   - **There is no power at the dock.** A 480V 3-phase service (roughly 400A) means a new PGE service, a transformer somewhere on the bank, and a cable run down the gangway. That's likely the single biggest cost and schedule item in the whole heat plan.
2. **EOS's big event heaters are not US products.** The EOS Mega HD (42-72 kW), Goliath (18-36 kW), Zeus HD, and Herkules XL are specified at 400V 3N~ 50/60 Hz (European 230/400V wye). EOS's US site only lists the Mythos, Cubo Avantgarde, Gracil, and Invisio lines. Using a Mega in Portland means a 480-to-400/230V transformer plus a UL/ETL field evaluation to get past the Oregon electrical inspector. It's doable, but it's a custom import path, not a catalog order.
3. **EOS is Harvia now.** Harvia bought about 80% of EOS Group in April 2020. EOS North America runs through ThermaSol (1958 Steam Way, Round Rock TX 78665, 800-776-0711, sales@thermasol.com). That's the channel to ask whether they'll supply the Mega HD with US electrical, or a UL path for it.
4. **50 bathers is an occupancy trigger.** Under the IBC, an assembly space with fewer than 50 occupants is classified Group B; at 50 or more it becomes A-3. A-3 brings heavier egress, fire, and sprinkler requirements, plus NFPA 701 on any drapery. **Cap posted occupancy at 49** unless you want the A-3 path. Confirm this with Portland BDS, since a floating structure adds its own jurisdiction questions.
5. **No sauna precedent for insulated drop-down drapes turned up.** Industrial insulated curtains exist, but the common ones (Goff's, AmCraft R-series) are vinyl and polyethylene bubble-foil built for freezers and warehouses. They will soften or off-gas at sauna ceiling temperatures of 100-130°C. A sauna-rated drape would be a custom build.
6. **A central stove fights radial zoning.** If drapes cut the circle into sectors, every sector touches the stove at the middle. A closed sector still gets heat at its apex and leaks around the guard rail. See section 4 for the fix: a modular stove core where each module faces a sector.

---

## 1. EOS and comparable big-room heaters

### EOS Saunatechnik (Driedorf, Germany; Harvia Group)

| Model | kW | Rated room volume | Stones | Supply | Notes |
|---|---|---|---|---|---|
| **EOS Mega HD** | 42 / 48 / 54 / 60 / 72 | 65-80 / 70-90 / 80-100 / 100-130 / 130-160 m³ | ~150 kg | 400V 3N~ 50/60Hz, 3x16A fuse control | EOS calls it the "most powerful electric sauna heater in the world". 100H x 120W x 80D cm, 110-120 kg empty. Infusion area 70 x 110 cm. Copper busbar HD wiring. |
| EOS Mega S HD | 36-48 | smaller | ~100 kg | 400V | 100 x 90 x 80 cm |
| EOS Goliath HD / 34.G | 18 / 24 / 30 / 36 | 24-35 up to 65-75 m³ | ~75 kg | 400V | 18 elements kept away from the stone basket. Triple-shell stainless. |
| EOS Zeus HD / Zeus L HD | 12-36 | 14-18 up to 65-75 m³ | ~100 kg | 400V | 8 mm steel wall, floor-standing |
| EOS Herkules XL S120 HD (and Vapor) | 18 / 24 / 30 | 24-35 / 35-45 / 45-65 m³ | 2 rock stores, up to 120 kg | 400V | Vapor version has built-in evaporator |
| EOSphere | not enough to heat a room on its own | n/a | n/a | n/a | Event piece. The heated rock basket lowers into a lit water tank for a "steam shock". Needs a separate main heater. Won the 2019 Golden Wave prize. |
| EOS Watermill set (with Goliath) | 18-36 | 24-75 m³ | n/a | 400V | Mill wheel 1700 x 1200 x 980 mm, tips water onto a cascade over the heater at 30/45/60 min intervals. Needs a permanent water line. |
| EOS Mythos S45 (US) | 12 / 15 | 634-880 ft³ (15kW) | 45 kg (99 lb) | **208V 3ph 60Hz** | US price about $10,441 for the 15 kW (The Sauna Place). Needs Touch3 control plus power box. This is the biggest *US-spec* EOS heater I found. |
| KUSATEK (gas, "powered by EOS") | 10-120 per system, up to 240 combined | custom | custom | DVGW/CE gas | Made to order. EOS itself pitches Kusatek for event saunas over 100 m² with 150+ guests. Not CSA/UL listed, and ruled out at Holman anyway. |

- **Controls:** EOS Touch 3 (US), EmoTec D (US), EOS App module NA, emergency button. The EU list compatible with the Mega adds Econ 4, Compact DC/HC, and EmoStyle.
- **Custom and multi-heater:** EOS markets "individual solutions" through Kusatek, and pitches multiple Megas for arena-scale rooms. It does not advertise a one-off custom electric tower. For 300-600 kg of stone you'd cluster 2-4 Megas, or build a custom stone cage around them. I couldn't find public pricing for the Mega. Estimate $15-30k per unit landed **[est]**; get a ThermaSol quote.

### US-listed alternatives (the easy path)

- **Harvia Virta Pro HL200E / HL220:** 20-21.6 kW, rated to 1,130 ft³ (about 32 m³). 208V 3ph, 58.2A, needs two separate 60A 3-phase circuits. UL listed. Minimum 264 lb (120 kg) of stones. **$3,900-4,950 each.** Seven units give about 140 kW for about $30-35k in hardware.
- **Scandia Ultra:** tops out at 18 kW. It's offered at 480V, but **Scandia's 480V models are not UL listed** (only the 208/240V ones are).
- **Helo Pro:** 14.4 kW, 132 lb rocks. **Helo Himalaya:** up to about 10.5 kW, 100 kg rocks.
- **Saunum Air L:** 10 / 13 / 15 kW with patented air mixing. Too small on its own at this scale, but the mixing principle scales (see section 3).
- **Kastor (Helo group):** the Saga 22/30 is wood-fired only (130-180 kg stones, 12-30 m³). No big Kastor electric turned up.
- **Tylö/Sauna360 commercial:** nothing above about 18 kW turned up in searches. Not verified.

### How the big European rooms do it

- **Therme Erding** runs a 200-seat event sauna, billed as the world's largest of its kind, and a 100+ person log banya that hosted a 100-nation Aufguss record at 75°C. They don't publish heater kW.
- **Therme București:** 9 dry and 4 wet saunas, about 300 bathers at once. No published kW.
- **SALT Árdna (Oslo):** 80-90 people, amphitheater tiers, only 50-60°C, one big glass wall. That's a useful reminder that a huge social room can run cooler.
- **Pust Kadettangen (Oslo):** a 20-person, 3-level room, **electric**, about 75 / 85 / 100°C by tier.
- **Rule of thumb (Harvia):** 1 kW per m³, plus 1.2 m³ of extra volume for every m² of glass, stone, or other uninsulated surface (1.5 for bare log walls). **At large volumes vendors undercut this.** The EOS Mega is rated at 72 kW for 130-160 m³, which works out to about 0.45-0.55 kW/m³. The practical big-room band is **0.5-0.8 kW/m³**, and a room this size ends up with multiple heaters.

---

## 2. Heat load sizing for the Rose

### Volume

| Case | Floor | Avg height | Volume |
|---|---|---|---|
| Low | 700 ft² | 11 ft | 7,700 ft³ = **218 m³** |
| Mid | 800 ft² | 12.5 ft | 10,000 ft³ = **283 m³** |
| High | 900 ft² | 14 ft | 12,600 ft³ = **357 m³** |

For scale, a 30 ft circle is 707 ft² and a 36 ft circle is 1,018 ft². Tiered benches don't reduce the air volume you have to heat by much.

### Load build-up for the mid case (283 m³) **[est]**

- **Ventilation** dominates. Finnish public-sauna practice is about 9-12 L/s of fresh air per person. At 40 people and 10 L/s, that's 400 L/s. Heating winter river air at 5°C up to 90°C takes about **41 kW** of continuous load.
- **Bathers soak up heat.** Skin is cooler than the air, so each person absorbs roughly 0.2-0.3 kW. At 40 people that's about **8-12 kW**.
- **Envelope:** about 335 m² of floor, roof, and wall at U≈0.25, plus about 15 m² of glass. That's roughly **8-10 kW** at a delta-T of 85K. Wind and the river underneath push it up.
- **Löyly recovery and heat-up of the wood surfaces and stones:** this drives the installed margin.
- **Vendor-table method:** 283 m³ plus 18 m³ of glass-equivalent, at 0.45-0.55 kW/m³ (the Mega ratio), gives **135-165 kW**. At 1 kW/m³ it would be about 300 kW, which is unrealistic here.

**Recommended installed capacity (mid case):**

| Mode | Heated volume | Installed kW online | 480V 3ph current | 208V 3ph current |
|---|---|---|---|---|
| Full open (40-49 bathers) | ~283 m³ | **~140-150 kW** | ~168-180 A | ~390-416 A |
| 2/3 zone | ~190 m³ | **~95-100 kW** | ~114-120 A | ~264-278 A |
| 1/3 zone | ~95 m³ | **~50-55 kW** | ~60-66 A | ~139-153 A |

Figure about 1.5 hours to preheat from cold at full open. Holding temperature takes about half the installed kW. The 1/3 and 2/3 figures assume the unused zone is a warm buffer behind an insulated drape. A leaky drape pushes these toward full-open numbers.

**Service size [est]:** the heaters draw about 180A at 480V. Continuous-load sizing at 125% puts the heater feeder at 225A. Add ventilation fans, lighting and sound, showers and water heating, a cold-plunge chiller if there is one, and control power, and you land at a **400A 480V 3-phase service**. If the heaters are 208V units (Harvia), put a step-down transformer on the float, 150-225 kVA **[est]**. Expect a PGE demand charge on a 150 kW peak.

### Floating-dock electrical

- Oregon runs the **2023 OESC**, which is the 2023 NEC plus Oregon Table 1-E, effective Oct 1, 2023. Check whether a 2026 adoption lands before permit.
- **NEC 553 (Floating Buildings):** a single set of feeder conductors, and the main overcurrent device needs ground-fault protection **not exceeding 100 mA**.
- **NEC 555.35 (2023):** feeders on docking facilities need listed GFPE of 100 mA or less. Shore-power receptacle branch circuits get 30 mA GFPE. Other receptacles get 4-6 mA GFCI. Starting Jan 1 2026, facilities with multiple shore-power receptacles need leakage-current measurement.
- **Nuisance-trip risk:** big resistive heaters leak some current when the elements are wet and have just been shocked with löyly. That leakage stacks up across many elements. Seven or more heaters behind one 100 mA main GFPE can trip. Split the load into several feeders with coordinated GFPE, spec heaters with low-leakage elements, and keep element spaces dry. Ask the heater vendor for leakage per element.
- Galvanic and ELCI issues come up if boats tie up alongside. Isolate the sauna's grounding from moored vessels.
- NFPA 303 (marinas) points to the same electrical principles.

### Fuel alternatives

- **Gas (the Torch 80k BTU stoves in use now):** about 23 kW input each. It would take about 6-7 of them, or a Kusatek custom system (DVGW-certified only), to heat the Rose. Holman rules out open-flame devices on docks. Gas only works at a different site.
- **Wood:** same Holman ban. On top of that there's the smoke downtown, a big wood stove eats roughly 10 m³ of air per kg of firewood, and you'd need a stoker on staff. Wood makes great löyly, but it isn't allowed here.
- **Electric:** the only viable Holman option. You get clean zoning, since heaters can be switched per sector, and automatic infusion. The cost is a new utility service and demand charges.

---

## 3. Stratification, tiers, and ventilation

- **Temperature by tier:** Pust Kadettangen measures about 75 / 85 / 100°C across 3 levels, so each tier runs roughly 10-15°C hotter than the one below. Without mixing, floor-to-ceiling difference in a sauna can hit 45°C (80°F). Saunum-style mixing cuts that to about 26°C.
- **Tier geometry:**
  - Tier rise 40-45 cm (16-18 in). That puts the lower bench at footrest height for the person above.
  - Top bench ceiling clearance **105-120 cm** (41-47 in).
  - Finnish "Rule of 230": bench height plus ceiling clearance comes to about 230 cm.
  - Bench depth: roughly 60 cm for sitting and 45-50 cm for footrest tiers, standard practice **[est]**.
  - **Three tiers** is the sweet spot for 30-50 people. It matches Pust and Árdna, and it gives a gentle, medium, and hot choice.
  - **Ceiling:** don't just build tall. Take the top bench height plus about 1.1 m and cap it there. Extra height above that is wasted kW (see the 14 ft case). A conical or domed roof also puts the hottest air over the top tier and not out in the middle of the room.
- **Ventilation for 30-50 bathers:**
  - Finnish RT 91-10480 calls for at least **6 air changes per hour** during use, and at least 3 m³ of room per person. The Rose has 5-9 m³ per person, which is fine.
  - Fresh air about **9-12 L/s per person** (20-25 cfm) holds CO₂ under roughly 700 ppm. ASHRAE 62.1 office-style is about 15 L/s.
  - German practice is 4-6 ACH, never below 2.
  - Put the supply low, behind or under the stove, or about 50 cm above the stove per VTT. Put the exhaust low on the opposite side, under the benches. Add a ceiling purge vent that opens after sessions.
  - For a room this size, run mechanical supply and exhaust with a CO₂ sensor and modulate it. Pre-temper the supply air with heat recovery if the budget allows, since ventilation is about 40 of the roughly 60 kW running load.
  - Fans and motors should sit outside the hot envelope. Any in-room fan needs a high-temperature rating (smoke-exhaust class fans are rated 200°C+).
- **Scaling Saunum-style mixing:** a ducted recirculation loop that pulls from the ceiling crown and discharges low near the stove or through the bench risers. Custom, but simple. Sequence it to shut off during Aufguss so the towel work isn't fighting a fan.

---

## 4. Movable thermal partitions and drapes

**Precedent:** I found no commercial sauna using drop-down insulated drapes to resize the hot room. This would be novel. That's good for the story and a risk for execution.

### Materials (continuous service temperature, humidity behavior)

| Material | Temp rating | Humidity / hygiene | Verdict |
|---|---|---|---|
| Silicone-coated fiberglass cloth (welding and oven curtain) | 260°C continuous (coating ~287°C, glass ~550°C). Meets NFPA 701 Test 2 and FM 4950 | Waterproof, wipeable, doesn't hold odor | **Best face fabric** |
| PTFE-coated glass cloth | ~260°C | Non-stick, very cleanable | Good. Stiffer and pricier. |
| Aluminized silica cloth | ~1000°F | Reflects radiant heat | Use as an inner layer facing the stove |
| Aramid (Nomex/Kevlar) | ~200°C | Absorbs some moisture | Fine, but no advantage over coated glass |
| Wool felt | OK to ~100°C, naturally flame-resistant | Soaks up sweat and steam, mildews, holds odor | Warm look, bad hygiene in a public room. Only for accents. |
| Mineral wool / fiberglass batt quilted between coated-glass skins | Fiberglass insulation to ~450°F | Must be fully encapsulated | The insulating core. Gets R-4 to R-8 in 1-2 in. |
| Vinyl and PE bubble-foil (Goff's Climate Curtain, R-8 per panel, stackable to R-20; AmCraft R4/R5) | Freezer and warehouse temps | **Fails at sauna temps** | Don't use. The format (quilted, retractable) is the part worth copying. |

### Mechanisms

- **Theater hoists** (JR Clancy/Wenger, ADC, Rose Brand): motors and controls aren't rated for 100°C+ air at 100% RH. JR Clancy doesn't publish environmental ratings. **Keep all motors, drums, and electronics outside the thermal envelope.** Use a stainless or galvanized line shaft through sealed ceiling penetrations, or a hand-operated counterweight or line set, which is simpler and quiet. A roll-drop format (roll the drape onto a batten) keeps the stored bundle up in the hottest air, so the skins need the full 260°C rating.
- **Tracks:** stainless 316, since this is river air plus chlorides from sweat. Use bottom weights or a floor channel to seal the base, plus a side seal against the bench riser. Air leakage around the edges will cost more than conduction through the fabric.
- **Code:** in an A-3 (50+) room, draperies must meet NFPA 701 under IBC 806. Coated glass passes. In a B occupancy (under 50), still spec NFPA 701 for insurance.

### Rigid alternatives

- **Pivoting timber "petal" walls:** full-height insulated panels (thermo-aspen or alder skins over 50 mm mineral wool with a foil vapor retarder) on floor pivots, swinging out from the stove core to close a sector. This fits the rose-petal plan. Petals open means one big room. Petals closed, only the heated sectors are in use.
- **Operable folding walls** (Hufcor-type on an overhead track): the concept works, but stock seals, laminates, and acoustic cores aren't sauna-rated. You'd be building a custom sauna-grade version.

### Recommendation

1. Use **2-3 fixed radial "petal" wing walls** that run from the outer wall partway in.
2. Close each sector with a **pivoting insulated timber panel at the stove end**. That panel does the real thermal work.
3. Add an **optional silicone-glass quilted drape** that drops at the outer edge, where the timber can't reach, run by counterweight or by a motor mounted outside the room.
4. Pair the partitions with a **modular stove core**: 3 heater modules, each facing one sector. Closing a sector switches off its module. That solves the red flag about the central stove heating every sector.

That gives three real zones (1/3, 2/3, full), each sealed and each with its own heater.

---

## 5. The stove as centerpiece

- **Stone mass:** the Mega HD holds about 150 kg and the Herkules XL has 2 stores up to 120 kg. For a 300-600 kg "altar", cluster 2-4 Megas, or run 6-7 Virta Pros each with 120+ kg, inside a shared custom stone cage or plinth. Stone weight is fine structurally for the float but has to go into the float trim and ballast calculation.
- **Guard rails:** commercial heaters need a guard on every accessible side. Typical is about 2-3 in from the heater body, and the rail itself at least 2 in from benches. Follow the chosen heater's manual, since EOS and Harvia list their own clearances.
- **How Aufguss masters work:**
  - Pour with a ladle from back to front across the stones, never in one gush, to avoid a steam burn to the master.
  - Water rule of thumb is about **20 g per m³ per infusion**, so about **5-6 L** for the full Rose (283 m³), split over 3 rounds.
  - Towel techniques include the helicopter, pizza, and walzer.
  - The design needs a clear working ring of about 1.2-1.5 m **[est]** around the stove guard so the master can walk and swing a towel, a floor drain at the stove, and a hose bib.
  - The EOS Mega's 70 x 110 cm infusion area is sized for this.
- **Automatic infusion (EOS):**
  - **AquaDisp:** automatic splash at preset intervals or on a push-button.
  - **AromaTec II:** doses 50-600 ml of water and 0-9 ml of essence per shot, in 1, 2, or 3 fragrance versions.
  - **Watermill:** a rotating wheel with scoops that tips water on a 30/45/60 min cycle. A visual centerpiece, 1.7 m tall.
  - **EOSphere:** lowers the heated rock basket into a lit water tank for the "steam shock". Needs a separate main heater.
  - All of these can run a scheduled "Rose bloom" infusion every hour when no master is on shift.
- **Scent:** essence goes into the infusion water through AromaTec's dosing channels, or through ice balls with oils melting on the stones, the common Aufguss trick. Use sauna-grade water-soluble essences only. Straight oils flash and are a fire risk.

---

## Sources

- EOS Mega HD (US page): https://www.eos-sauna.com/us/products/finnish-sauna-heaters/eos-mega-hd
- EOS Mega S HD: https://www.eos-sauna.com/en/products/event-sauna-heaters/eos-mega-s-hd
- EOS Goliath HD: https://www.eos-sauna.com/us/products/finnish-sauna-heaters/eos-goliath-hd ; 36 kW spec https://www.sanel.lv/en/electric-sauna-heaters-eos/eos-goliath-34g-ii-360-kw-electric-sauna-heater
- EOS Zeus HD: https://www.eos-sauna.com/en/products/finnish-sauna-heaters/eos-zeus
- EOS Herkules XL S120 HD: https://www.eos-sauna.com/en/products/finnish-sauna-heaters/eos-herkules-xl-s120-hd
- EOS Watermill: https://www.eos-sauna.com/en/products/sauna-heater/eos-watermill-sauna-set-with-goliath-heater
- EOSphere: https://www.eos-sauna.com/us/products/event-sauna-heaters/eosphere
- EOS AquaDisp: https://www.eos-sauna.com/en/products/classic/dosing-systems/aquadisp ; AromaTec II: https://www.eos-sauna.com/en/products/dosing-units/aromatec-ii
- EOS US product list: https://www.eos-sauna.com/us/products
- EOS commercial heater range: https://www.eos-sauna.com/en/wellness-facilities/electric-sauna-heaters
- KUSATEK gas: https://www.eos-sauna.com/en/wellness-facilities/gas-powered-sauna-heaters ; https://www.kusatek.de/en/products/kusatek-independent
- EOS Mythos S45 US price: https://www.saunaplace.com/products/eos-mythos-s45-electric-sauna-heater ; https://artofsteamco.com/products/eos-14-948011
- Harvia Group brands / EOS acquisition: https://harviagroup.com/brands/ ; https://en.wikipedia.org/wiki/Harvia
- Harvia Virta Pro: https://www.harvia.com/en-US/products/HL220400/virta-pro-hl220-216-kw-black ; https://www.saunaplace.com/products/harvia-virta-pro-20
- Scandia Ultra 480V not UL: https://www.saunaplace.com/products/scandia-ultra-18240-or-18208
- Helo Pro 14.4: https://www.steamandsaunaexperts.com/store/p1414/helo-pro-14-4kw.html ; Kastor Saga: https://helosauna.com/products/kastor-saga
- Saunum Air / Air L: https://us.saunum.com/product/saunum-air-l/ ; https://saunamarketplace.com/product/saunum-air/
- Harvia sizing rule (glass 1.2 m³/m²): https://support.harvia.com/hc/en-gb/articles/22158995674524-How-do-I-select-the-correct-heater-power
- Therme Erding: https://therme-erding.com.de/en/sauna.html ; record: https://www.eap-magazin.de/Nachricht/Weltrekordversuch:-Therme-Erding-sucht-ueber-100-Nationen-fuer-Sauna-Aufguss.html
- Therme București: https://www.hotspringsguides.com/hot-springs/therme-bucuresti-romania
- SALT Árdna: https://www.salted.no/rdna-english
- Pust Kadettangen: https://www.pust.io/en/badstue/kadettangen-fellesbadstuen/
- Bench and ceiling rules: https://havenofheat.com/blogs/sauna-guides/sauna-ceiling-height-bench-height-the-finnish-rule-of-230 ; https://www.homesaunatips.com/build/benches/
- Ventilation: https://saunologia.fi/in-english/finnish-sauna-essentials-part-5/ ; https://support.harvia.com/hc/de-de/articles/21953036825628-Bel%C3%BCftung-der-Sauna ; https://thermalfinn.com/sauna-builds/sauna-ventilation/
- NEC 555.35 / 553: https://up.codes/s/ground-fault-protection-of-equipment-gfpe-and-ground-fault-circuit-interrupter ; https://www.thebuildingcodeforum.com/forum/threads/nec-article-555-marinas-boatyards-floating-buildings-and-docking-facilities-2023-nec.36422/
- Oregon OESC 2023: https://www.oregon.gov/bcd/codes-stand/pages/oesc-adoption.aspx
- PP&R PRK-1.17 dock rules: https://www.portland.gov/parks/documents/prk-117-short-term-boat-launch-and-moorage-rules-full-text-policy/download
- PP&R 2026 commercial guidelines: https://www.portland.gov/parks/documents/general-guidelines-commercial-activity-2026/download
- Holman Dock transfer: https://www.koin.com/news/politics/popular-eastbank-esplanade-docks-transferred-to-portland-parks-recreation/
- Goff's climate curtains: https://www.goffsenterprises.com/products/industrial-curtain-walls/climate-curtain-walls/
- AmCraft insulated / high-temp curtains: https://amcraftindustrialcurtainwall.com/products/industrial-curtain-walls/high-temperature-curtains/
- Silicone fiberglass ratings / NFPA 701: https://gocorp.com/shop/sheeting/silicone-coated-fiberglass-sheeting-welding-cloth/ ; https://www.tectop-new-material.com/news/how-silicone-coated-fiberglass-fabric-boosts-safety-compliance-in-industrial-facilities/
- JR Clancy hoists: https://www.jrclancy.com/hoists.php
- Aufguss technique / water rule: https://kueng.swiss/en/magazine/sauna-infusion-home ; https://www.abathhouse.com/journal/a-sauna-master-explains-the-aufguss-sauna-ritual
- Heater guard clearances: https://tahoesaunacompany.com/blog/sauna-heater-clearances
