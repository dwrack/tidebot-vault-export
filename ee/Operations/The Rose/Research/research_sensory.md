# The Rose: sensory systems research (sound, touch, scent, light, acoustics, control)

Prepared 2026-09-26 for the Ebb & Ember "Rose" communal floating sauna design brief. 30-50 bathers, 3-tier stadium benches around a central heater, 30-36 ft diameter, 80-100 C air, löyly bursts.

Confidence key: **[V]** = verified on a manufacturer/retailer page during this research. **[E]** = my engineering estimate or industry rule of thumb, not verified. Prices are list/retail seen online in Sept 2026 unless marked.

---

## 0. The one design rule that drives everything

**Almost no audio or electronic part survives the hot room.** The published ceilings are low:

| Part | Published max temp | Source |
|---|---|---|
| ButtKicker LFE (coil thermal cutout) | trips at ~70-75 C | [V] manuals.plus LFE guide |
| Harvia Bluetooth sauna speaker SAC80500/501 | 65 C | [V] harvia.com |
| Harvia LED strip | 60 C (140 F) | [V] wcsaunas.com |
| Marine speakers (Polk DB, Kicker KM) | 60-70 C | sweatdecks.com (blog, not mfr) |
| EOS 16 cm steam-room speaker | 80 C | [V] eos-sauna.com |
| **EOS sauna loudspeaker 945429 (10 cm, 25 W)** | **120 C, IP65** | [V] eos-sauna.com |
| **Cariitti LED strip** | **125 C** | [V] bsaunas / cariitti |
| **Cariitti glass fiber (light only, no electricity)** | **180 C** | [V] saunaplace.com |
| Neodymium magnets (most exciters) | start losing strength ~80 C (N grade) | [E] |

In a 3-tier sauna the air stratifies hard: roughly 90-100+ C at the ceiling, 80-90 C at top-bench head height, and often only 35-50 C down in the cavity under the lowest tier and at floor level [E]. So the architecture is:

- **Electronics live in a cool ring:** under the lowest tier, in a ventilated service plenum, or outside the envelope entirely.
- **Only passive things enter the hot zone:** glass fiber tails, wood, waveguide slots, and the one proven 120 C speaker (EOS).
- Every cool-ring cavity gets its own fresh-air supply (the sauna's intake air, pulled in low anyway) and a temperature sensor wired to the control system that mutes the amps if it goes past ~55 C.

---

## 1. Tactile transducers (feel it, don't hear it)

### Models

| Model | Power / impedance | Freq | Price | Notes |
|---|---|---|---|---|
| **Clark Synthesis AW339 All-Weather** | 135 W cont., 4 Ω; wants 125-150 W amp | 10 Hz-17 kHz | not listed; typically ~$230-280 [E] | [V] Built for rain and humidity, hot tubs, wood decks, boat hulls. Clark recommends it for steam rooms. Not rated for underwater use. Mount with slow-cure epoxy or screws. **Best fit.** |
| Clark TST239 Silver | 125 W amp at 4 Ω | wide | ~$150 [E] | Indoor/dry only. No |
| ButtKicker LFE | needs 400-1500 W amp | 5-200 Hz | $349.95 | [V] Most force; thermal cutout ~70-75 C; not moisture-rated. Great for a riser under a whole tier, but big amps |
| ButtKicker Advance | n/a | n/a | $199.99 | [V] price only |
| ButtKicker Concert | n/a | n/a | $349.95 | [V] Drum-throne unit |
| ButtKicker Mini LFE | n/a | n/a | $109.99 | [V] |
| ButtKicker amp BKA1000-P | 1000 W | | $599.99 | [V] (ButtKicker store showed everything "sold out" on 2026-09-26, so check supply) |
| Dayton TT25-8 Puck | 15 W RMS, 8 Ω | 20-80 Hz | ~$27 each | [V] Tiny. Fine for per-seat accent in a dry bench, not moisture-rated |
| Dayton BST-1 | 50 W RMS, 4 Ω | | ~$50-60 [E] | Pro shaker, not moisture-rated |
| Aura Pro AST-2B-4 | 50 W RMS, 4 Ω | 20-80 Hz | $55-86 | [V] Classic cheap shaker, not moisture-rated |

**Pick: Clark AW339.** It's the only one here that is actually sold for wet, humid, outdoor and spa installs, and its 10 Hz-17 kHz range means it can carry some upper-bass "texture" (river, heartbeat, drum), not just thump. ButtKickers hit harder, but they're a dry home-theater product with a 70 C self-protect switch.

### Mounting under timber benches
- **Mount to the bench structure, not the seat slats.** Bolt a 2x6 blocking cross-member between bench joists and hang the transducer from it (the ButtKicker riser method, [V] audioholics / ButtKicker guide). Put it **on the underside, inside the cavity below each tier**, where it's coolest.
- **Clark density rule** [V]: one AW339 per ~4 ft x 4 ft of soft-wood deck. Estimate for The Rose: 3 tiers at about 0.6 m deep around a 9-11 m circle is roughly 35-45 m² (380-480 ft²) of bench. That's **24-30 units** at full density, or **18 units** if you do 6 petals x 3 tiers, one per zone, and accept softer coverage. [E]
- **Heat shield:** line the underside of the top tier's cavity with foil-faced mineral wool so radiant heat from the tier above stays out. Supply cool intake air into the cavity. Add one thermistor per cavity. [E]
- **Wood as resonator:** cedar and spruce benches transmit low frequency well. Keep bench tops floating on rubber isolators so vibration stays in the seating zone. **Isolate the bench frame from the hull/deck with elastomer pads.** Otherwise the whole floating structure (and the water) becomes a subwoofer, and the neighbors on the dock feel it too. [E]
- **Moisture:** löyly condensate drips through slats. Face the transducer down or put a drip shield above it, and use tinned, silicone-jacketed wire. [E]

### Amps and zoning for ~40 seats
- 18 zones (6 petals x 3 tiers) at 150 W each. Use Q-SYS-native multichannel amps, e.g. **QSC CX-Q 8K4 (8 ch)**. Three of them cover 24 channels with spares. Roughly $6-9k each installed [E, unverified]. The budget route is 3-5 generic 4-channel class-D install amps at $800-1,500 each [E].
- Amps go in the dry electrical room, never in the cavity. That means long speaker runs, so use 12-14 AWG.
- Each zone gets its own DSP channel with a low-pass filter (~80-120 Hz for body feel), a limiter, and a level trim. Then a wave can **roll around the ring petal by petal**, or climb tier to tier.

### Precedents
- Clark says their TSTs are used in therapy chairs, therapy beds and massage tables [V clarksynthesis FAQ]. Vibroacoustic therapy uses 30-120 Hz [V vibroacousticsolutions / Hisooth EssenceVibe table].
- Anderson Acoustics (UK) builds live-edge wood "tactile sound benches" and lists saunas as a use [V].
- Cedarbrook sells PQN "wet/dry transducer speakers" that use the sauna wall as the radiator, $200/pair, no temperature rating published [V].
- I found **no published large-sauna precedent with per-seat tactile audio.** The Rose would be first-of-kind, which is worth saying in marketing.

---

## 2. Heat-rated speakers and "drivers outside the envelope"

**Options inside the hot room:**
- **EOS sauna loudspeaker (item 945429):** 25 W / 50 W peak, 8 Ω, 10 cm fiberglass cone, **120 C**, IP65, 90-19,000 Hz, 90 dB 1W/1m [V]. About $150-250/pair via dealers. This is the only in-room speaker I'd trust. A ring of 6-12 would give full-range coverage, one or two per petal. Mount them low: seated ear height at the lowest tier, facing up and across (sweatdecks says 3-4 ft from floor, below the hot layer).
- Harvia ceiling passive speakers, reportedly 120 C, $150-250/pair (sweatdecks blog, not confirmed on a Harvia spec sheet). Harvia's own Bluetooth unit is only 65 C, so don't use it.
- Tylö passive ceiling speakers exist, but no temperature spec was found.

**Better idea: drivers in the cool ring, sound through the wood.**
- Put good ordinary install speakers or small subs (any brand) in the ventilated cavity under the lowest tier and behind the bench risers. They fire through **slotted riser boards or perforated/slatted grilles**. Wood slats with 10-15 mm gaps are acoustically near-transparent [E], so the speaker sees ~40 C, not 90 C.
- Same trick in the rib bases. If the petal ribs are hollow boxes at floor level, each one can be a **ported waveguide** with the driver at the cool bottom and the opening at knee height.
- The ceiling is not an option for drivers. That's the hottest air.

**Exciters (wall-as-speaker):**
- Dayton DAEX32EP-4 "Thruster", 40 W, 4 Ω [V]; DAEX32Q/U 20 W variants [V]. About $20-40 each.
- **Heat problem:** their 3M VHB adhesive pads and neodymium magnets are not rated for 80-100 C. Only use them on bench backrests or lower wall panels in the <60 C zone, **screwed on, not taped**. Good for "the bench back sings" moments. Bad as the main system. [E]

---

## 3. Directional, steered and spatial audio

### What the big names are
| System | What it is | Realistic for The Rose? |
|---|---|---|
| **Holoplot X1/X2** (Sphere Vegas) | 3D beamforming + wavefield synthesis matrix arrays. X2 does up to 12 separate sound fields per array and is weather/humidity rated [V] | **No.** Price on request (six figures for a system [E]), no 90 C rating, and in a 10 m wooden bowl the beams just bounce off the curved walls. Overkill |
| **d&b Soundscape** (En-Scene/En-Space) | Object-based spatial mixing + room emulation on d&b DS100 processor | No. $30k+ processor plus d&b speakers that can't take the heat [E] |
| **L-Acoustics L-ISA** | Object-based immersive, needs L-Acoustics speakers | No, same reasons |
| **Meyer Spacemap Go** | Free app/firmware, but it runs on a Meyer Galaxy processor (Galaxy 816 was ~$12k per gearspace) [V-ish] | Maybe as a Tier 3 luxury, not needed |
| Genelec (Smart IP, SAM monitors) | High-quality install speakers, Dante/AES67 | Good cool-ring driver choice, but they don't do steering |
| **Holosonics Audio Spotlight AS-16iX** | Ultrasonic parametric beam, 1-2 listeners, $1,799 [V] | **No in the hot room.** Electronics aren't heat-rated, hot humid air soaks up ultrasound, and the beam reflects off hard wood. Could work in the cool-down lounge |
| Focusonics Model A/B | Ultrasonic beams, Model A for 3-15 m [V] | Same issues |
| Brown Innovations SoundDome | Acrylic dome "shower" over one listener [V] | No (plastic dome, heat) |

**Honest take:** in a 30-36 ft round wooden room you don't need beamforming. What reads as "sound goes to your seat" is really **a ring of discrete zones plus the tactile seats.** Pan a sound from one petal's speaker and shaker to the next and it feels like it's traveling. The shakers are what make it personal: sound you feel can't leak to the next seat, and a beam can't beat that.

### Tiered recommendation
- **Tier 1 (build this), ~$35-60k equipment [E]:** Q-SYS Core 8 Flex (8x8 Dante included, expands to 32x32 [V], street ~$4-6k [E]) + 6-12 EOS 120 C speakers or cool-ring drivers behind slats + 18 Clark AW339 tactile zones + 3 x 8-ch amps + 1-2 subs in the cool ring. Do object-style panning in QLab (cue-based matrix) or Q-SYS.
- **Tier 2 (+$10-20k):** add a spatial renderer, e.g. FLUX SPAT Revolution (software) or a Meyer Galaxy running Spacemap Go, so an Aufguss host can "draw" sound paths live on an iPad.
- **Tier 3 (don't):** Holoplot or L-ISA. It's a lot of money for a room this size and heat, and it pushes the brand toward nightclub.

---

## 4. Scent

### "scentcannon": who they are
- **Scent Cannon** (scentcannon.com), **Kittery Point, Maine**. Founder listed on Kickstarter as "Jacob" (project `j8k3/scent-cannon`). The site links Instagram **@vj8k3_productions**, Facebook `scent.cannon`, and YouTube **@scentcannon** [V]. The user referenced the handle "scentcannon", probably the same outfit.
- **What it is:** a vortex-ring cannon. It "uses the natural shape of the torus to propel the air mixture forward" and shoots scent mixtures, fresh air for cooling, and fog. Newer models have **sensors to target hot, smelly or dry areas**, and **two scent drivers per cannon so scents blend over time**. **Version 2 due late 2026.** Patent pending. They sell mostly as an **event service ("olfactory jockeys")**. No public specs or pricing [V scentcannon.com/about].
- **Why vortex rings suit this:** each ring carries a small, sealed packet of scent that stays intact until the ring breaks up. You get a targeted "puff" at a person or tier instead of flooding the room, and use less fragrance (PMC 10255882 research on vortex olfactory displays [V]).

### Commercial ring/scent cannons
| Device | Specs | Price |
|---|---|---|
| Haunted Hills "Fog Cannon" | vortex ring cannon, 50-100 ft range, you supply the fog machine, surface mount [V] | $300 |
| Global Special Effects "Stadium Scent Machine" (Beyond Tent) | 1,100 CFM, 25 oz/hr, **DMX 4-ch**, **74 dB @ 10 ft**, 35 lb [V] | $4,999.99 |
| Evilusions Scent Cannon | haunt-industry scent blaster | n/a |
| Olorama Professional Generator | 10 or 20 scents (20 = two synced units), **DMX (4 consecutive channels) + UDP**, built for 4D cinema/museums [V] | quote only |
| OVR ION / Omara | wearable/near-face VR scent, $40 cartridges [V] | Not relevant (personal device) |

The Beyond Tent unit is too loud (74 dB) for a calm room. Olorama is the pro DMX-triggered "scent cue" box, but it has to live outside and be ducted in.

### Ambient scenting (whole-room baseline)
- **AromaTech** AroMini / AromaPro BT / AirStream BT: cold-air nebulizing, HVAC-tie-in, 4,000-15,000 ft² [V]. Retail roughly $400-1,500 [E].
- **ScentAir Stream** (HVAC-integrated) and **Prolitec** (ScentAir Pro): service-contract models, quote only [V].
- In a sauna these go **on the fresh-air intake duct outside the hot room**, never in it.

### Traditional + automated infusion (the real primary scent)
- Scent in a sauna has always come through **löyly/Aufguss**: diluted essential oil in water poured on stones (5-10 drops per liter; never neat oil on stones) [V viworo / icecoldtubs / kemitron].
- **EOS AromaTec II** automated dosing: water 50-600 ml plus essence 0-9 ml per cycle, peristaltic pumps, **1, 2 or 3 fragrances**, programmable cycles [V]. **Harvia Autodose (SASL1):** timed pours every 1-10 min or on button press [V]. Either one can be triggered by a relay from the show controller [E, confirm with EOS/Harvia that dry-contact triggering is supported].
- Aufguss hosts use scented ice balls that melt slowly on the stones [V].

### Heat and safety red flags
- **Flammability:** eucalyptus flash point is ~39-54 C (102-130 F) [V organicaromas / libertynatural]. **That's below the room's air temperature.** Neat oil on 300 C stones is a fire and smoke risk. Heater surfaces run >200 C [V kemitron].
- **Pyrolysis:** oils hitting rocks >200 C break down into formaldehyde and acrolein. Synthetic fragrance and bad carrier oils make it worse. Guest reactions reported include nausea and skin burning (thyme, oregano, mint, cinnamon, frankincense) [V Culture of Bathe-ing].
- **Fog in a sauna:** glycol fog fluid near a 90 C heater is a bad idea. It's irritating, it sets off smoke detection, and propylene glycol flashes around 99 C [E]. **Run ring cannons on plain scented air or water mist only, no glycol fog.** Rings may also dissipate faster in the room's strong convection [E]. Prototype first.
- **Lingering:** wood absorbs scent. Keep one house palette and change it seasonally, not hourly. Purge between sessions with the exhaust fan at max for 5-10 min [E]. Post an allergen notice and keep one fragrance-free session per day.
- **Cannon placement:** mount the cannon **outside the envelope**, firing through a small port in the wall. The electronics stay cool, and it can shoot **cool** outside air. A cool, scented ring landing on the top tier at 90 C is probably the best single "4D" moment available here. [E]

### Proposed Pacific NW / Rose palette (all natural, water-diluted)
1. **Douglas fir** (needle oil): opening breath, bright and green
2. **Western red cedar** (cedarleaf/Thuja, used sparingly because thujone is strong) plus the room's own cedar
3. **Rose** (rose otto is very costly, so use rose geranium or a small rose absolute blend): the "bloom" at the peak
4. **Petrichor**: geosmin notes are hard to do naturally. Vetiver plus a mineral/wet-stone accord, delivered as a cool ring or mist, not on stones
5. **River / cold water**: menthol/peppermint plus cucumber-green, used at the cool-down fade
6. Winter option: birch tar (tiny amount), smoky and traditional Finnish

---

## 5. Lighting for shadows

### Heat-rated hardware
- **Cariitti Premium Glass Fiber set:** 8/11/21 spots, VPAC27 projector, **2700 K**, glass fibers to **180 C**, heater lens included, dimmable (push-dim), 5-yr warranty, **$1,300** [V saunaplace]. Warm white only, no RGB.
- **Cariitti Standard set:** VPL10 projector, 3000 K, 6 or 16 spots [V].
- **Cariitti Starlight / "Sauna Starry Sky":** VPAC27 + 75 or 100 glass fiber tails, ~$560-1,025 [V]. This is the dark-adapted star ceiling.
- **Cariitti LED strip (side or top emitting):** −40 to **+125 C** [V]. **Harvia LED strip is only 60 C, so avoid it** [V].
- VPAC projectors are IP65 [V]. **DMX control was not confirmed** for Cariitti. Plan on either (a) dimming them with 0-10 V/phase dimmers driven by a DMX dimmer pack, or (b) using a DMX-native fiber illuminator from a theatrical fiber-optic supplier outside the room. [E]

### Casting rib shadows (petal ribs)
- A light at the **center** puts ribs edge-on to the source, so **no shadows**. Shadows need **off-axis point sources.** [E]
- **Grazers at rib bases:** one lensed fiber tail or a 125 C LED point at the foot of each rib, aimed up the rib's side. Each rib then throws a long shadow across the curved ceiling. [E]
- **Sundial chase:** put one point source per petal around the perimeter and cross-fade them slowly around the ring (e.g. one lap per 12-min Aufguss). The rib shadows **sweep across the dome like a sundial.** It costs almost nothing extra and fits the ritual. [E]
- **Heater glow:** the Cariitti heater lens plus warm uplight on rising löyly turns the steam into a visible, lit column. That's the natural centerpiece.
- **Projection through a window:** an IP65 gobo projector outside a tempered/heat-glass window can throw leaf-shadow or **water-caustic ripple** patterns (river light) into the room. Keep it very dim. [E]
- **Circadian:** 2700 K daytime, fading to ~1800-2200 K amber in evening sessions, with no blue. Full dark plus star ceiling for "night löyly." [E]
- **Firelight:** keep flicker to a slow, subtle drift on the heater zone only. Fast flicker reads as nightclub or Halloween. [E]

---

## 6. Acoustics

### Size and reverb math [E]
- A 9-11 m (30-36 ft) diameter room at 250-400 m³ means an average ceiling height of ~3.5-4.5 m. Total surface is about 280-320 m².
- **Target RT60 ~0.6-0.8 s (mid-freq), occupied.** That's intimate, speech intelligible for the Aufguss host, soft music, calm. Much longer and 40 people talking turns into a roar. Much shorter feels dead and closet-like.
- Bare wood (α ≈ 0.10) × ~300 m² ≈ 30 m² sabins. 40 seated, towel-clad bathers add ≈ 0.3-0.4 m² each ≈ 14 m². Sabine for V = 320 m³: **~1.2 s occupied, ~1.7 s empty.** Too live.
- To reach ~0.7 s you need **~30 m² more sabins ≈ 50-60 m² of slatted absorber** (α ~0.55) spread around the room. That's roughly a third of the wall and upper-wall area.

### How to build it hot-proof
- **Slatted wood over mineral wool.** Rock wool (Rockwool/ROXUL basalt) is non-combustible and dimensionally stable in heat [V saunaburg]. Leave 10-20 mm gaps between slats with 50-100 mm wool behind. Slats with exposed edges absorb better than a flat perforated face [V patent summary].
- **Wood wool (Troldtekt-type) does not belong in the hot cabin** [V wallpanelspro]. Keep it for the changing rooms and lounge.
- The foil vapor barrier stays behind the wool, against the structure.

### The round-room problem (the big one)
- Concave circular walls and domes **focus sound**. You get a hot spot at the center and a "whispering gallery" creep around the wall, so a whisper on one side is heard clearly on the far side [V Wikipedia whispering gallery, Slate, gearspace].
- The central heater sits at the focal point, which luckily blocks and scatters some of it. Mitigation:
  1. **Break the curve.** The rose-petal plan already helps. Make each petal wall **faceted or scalloped (convex out)**, not a smooth arc. Convex = scatter; concave = focus. This is the single most important acoustic move.
  2. **Ribs as diffusers.** Deep, irregular rib spacing breaks up the creep along the wall. Timber QRD/skyline diffusers on the upper walls work well; 2D diffusers fit circular geometry best [V gearspace].
  3. **Absorb the dome/upper ceiling** so the dome doesn't re-focus to the center.
  4. Put the heater guard/rock cage near the center as a scattering object (a "center sculpture" is a known fix [V gearspace]).
- Get an acoustic consultant to run a quick ray-trace model once the geometry is set. It's a few thousand dollars and cheap insurance [E].

### Outside noise and neighbors
- **Portland Title 18:** commercial/mixed-use limit 65 dBA; residential limits are lower, with 5 dBA subtracted 10 pm-7 am [V portland.gov]. Check the exact receiving zone in Figure 1 (18.10.010) and any Parks/Harbor permit conditions.
- Tactile bass helps here. Clark notes deck-mounted TSTs give sub-bass that doesn't bother neighbors [V]. **The risk on a float is structure-borne.** Bench vibration and subs can drive the hull and deck. Use elastomer isolation between bench frames and hull, and keep in-room subs small.
- Bridge traffic and river noise coming in: the sauna's insulated, massive wall assembly already helps. Put the door on the quiet side, and use a vestibule [E].

---

## 7. Immersive precedents worth citing

- **Aufguss WM (World Masters/Championship)**, since 2007. Show Aufguss is a staged performance with music, lighting, costume, props and scent [V aufguss-wm.com, thermea.com]. Aufguss WM USA Nationals ran in 2025-26 (hosted by Bathhouse) [V].
- **Bathhouse Williamsburg (NYC):** new ~700 ft², **80-person event sauna**, custom-built with a **full sound and lighting package** and a daily Aufguss program [V abathhouse.com]. **The closest US precedent to The Rose's scale.** They lean loud and tribal, which is the opposite of E&E's calm register and a useful contrast to point at.
- **Thermea (Whitby, Winnipeg):** "Aufgusshow" competitions [V].
- **Othership (NYC/Toronto):** guided themed sessions ("Sound Immersion", "Arctic Tundra"), aromatherapy, towel work, curated soundscapes, hidden light sources, cedar-scented air [V othership.us, retaildesignblog].
- **AIRE Ancient Baths:** candlelight, signature **orange-blossom scent** (commissioned perfumer), water sound, and a sound bowl to close the session [V beaire.com]. The model for a *signature house scent*.
- **Therme Group:** multisensory "Forest Bathing: Lupuna" at Therme Euskirchen [V].
- **Löyly Helsinki (Avanto Architects):** faceted timber "cloak" of 4,000 pine planks [V]. A reference for faceted timber, which is also good acoustics.
- **Culture of Bathe-ing (Domino Park, 2026):** sauna by Rintala Eggertsson; their Substack argues about scent in sauna [V].
- Sphere Vegas (Holoplot), Meow Wolf, teamLab: cite for "immersive" vocabulary only. Their tech doesn't transfer to 90 C.

---

## 8. Control: one brain, timed scenes

**Recommended stack [E]:**
- **Q-SYS Core 8 Flex** as the audio + control brain. It handles DSP for every zone, Dante, 8 GPIO (relay triggers for the EOS/Harvia dosing unit, cannon solenoids, exhaust purge), thermal-sensor inputs with auto-mute, and an **iPad operator panel (Q-SYS UCI)** [V specs; price E].
- **QLab 5 on a Mac mini** as the show timeline. It plays multichannel stems per zone (tactile + speakers), sends DMX/Art-Net to lights and Olorama, and sends network cues to Q-SYS. Each session is one QLab cue list: "12-min Aufguss", "Night Löyly", "Silent Sauna", "Sound Bath".
- **DMX/Art-Net gateway** (e.g. ENTTEC ODE) → dimmers for the fiber illuminators and 125 C LED, scent devices.
- Alternatives: **Crestron** is overkill and costly. **BrightSign** is fine for a single looping show but weak on interactivity. **Madrix** is for pixel-mapping LED, which you don't need here.
- The operator (Aufguss host) gets 4-6 big buttons: *Start ritual / Next round / Löyly now / Cool ring / Hold / Fade out*. Plus a hard **"all off, lights up"** safety button.

**Sample 12-min Aufguss scene [E]:**
1. 0:00: house fades to 2200 K, star ceiling up, low drone on tactile (35 Hz, barely there)
2. 1:00: host speaks (EOS ring, no reverb added)
3. 2:00: first pour (Douglas fir via AromaTec). Tactile swell rolls petal to petal. Sundial light chase begins
4. 5:00: second pour (cedar/rose), towel work, rhythm felt through benches, tier by tier
5. 8:00: peak (rose). Heat plus lit steam column. Tactile at max (still quiet in the air)
6. 10:00: **cool vortex ring** to each petal in turn (river/petrichor)
7. 11:00: silence, sound-bowl strike through the bench backs (exciters), lights to star-only
8. 12:00: exhaust purge, lights to 2700 K

---

## Rough budget (equipment only, excluding install) [E]

| System | Low | High |
|---|---|---|
| Tactile: 18-30 Clark AW339 + 3 amps + cabling | $12k | $30k |
| In-room/cool-ring speakers + subs | $3k | $12k |
| Q-SYS Core + Dante + iPad + QLab/Mac mini | $7k | $15k |
| Fiber lighting (3-4 Cariitti sets + star ceiling) + 125 C LED + DMX dimming | $6k | $15k |
| Gobo/caustic projector outside a window | $1.5k | $6k |
| Scent: EOS AromaTec II (3 essences) or Harvia Autodose + 1-2 ring cannons + intake nebulizer | $4k | $15k (Olorama/pro cannon) |
| Acoustic slat + rock wool (~60 m²) | carpentry line item | |
| Acoustic consultant (ray-trace + commissioning) | $3k | $10k |
| **Total** | **~$37k** | **~$105k** |

---

## Sources
- ButtKicker LFE guide (thermal switch): https://manuals.plus/m/1f73f0099addd12b8d19b4afc0df7b2b61e0ad4b74c4899cccf3c1d416a1b4ab ; product/store: https://thebuttkicker.com/collections/all ; install: https://www.audioholics.com/subwoofer-reviews/buttkicker-lfe-kit
- Clark Synthesis AW339: https://clarksynthesis.com/all-weather/ ; FAQ: https://clarksynthesis.com/faq/
- Dayton TT25-8: https://www.daytonaudio.com/product/1104/tt25-8-puck-tactile-transducer-mini-bass-shaker ; exciters: https://www.daytonaudio.com/category/169/exciters
- Aura AST-2B-4: https://www.parts-express.com/Aurasound-AST-2B-4-Pro-Bass-Shaker-299-028
- Anderson Acoustics tactile benches: https://andersonacoustics.co.uk/services/tactile-sound/
- Harvia speaker: https://www.harvia.com/en-US/products/SAC80501/waterresistant-sauna-speaker-harvia-black
- EOS sauna loudspeaker: https://www.eos-sauna.com/en/products/accessories/sauna-loudspeakers ; steam: https://www.eos-sauna.com/en/products/steam/loudspeaker-for-steam-rooms
- Sauna speaker overview: https://sweatdecks.com/blogs/news/sauna-audio-speaker-heat-rated-options ; https://cedarbrooksauna.com/wet-dry-sauna-speakers/
- Holoplot X1/X2: https://www.holoplot.com/products/holoplot-x1 ; https://audioxpress.com/news/holoplot-addresses-targeted-reinforcement-challenges-with-x2-compact-matrix-arrays
- Spacemap Go: https://meyersound.com/product/spacemap-go/ ; https://gearspace.com/threads/immersive-audio-and-object-based-mixing.1349136/
- Holosonics: https://www.touchwindow.com/p/AS-16iX.html ; Focusonics: https://www.focusonics.com/ ; Brown Innovations: https://www.browninnovations.com/sound-dome
- Q-SYS Core 8 Flex: https://www.qsys.com/products-solutions/q-sys/processing/core-8-flex/
- Scent Cannon: https://scentcannon.com/ ; https://scentcannon.com/about ; https://www.kickstarter.com/projects/j8k3/scent-cannon ; https://www.youtube.com/@scentcannon
- Vortex olfactory display research: https://pmc.ncbi.nlm.nih.gov/articles/PMC10255882/
- Fog cannon: https://hauntedhillsproductions.com/Fog-Cannon-p140839482 ; Stadium Scent Machine: https://beyondtent.com/products/stadium-scent-machine
- Olorama: https://olorama.com/product/compact-scent-generator/ ; DMX: https://olorama.com/integration-guide-how-to-activate-smells-through-dmx/
- AromaTech: https://aromatechscent.com/collections/extra-large-space-scent-diffusers ; ScentAir: https://scentair.com/scentair-stream-diffuser ; Prolitec: https://prolitec.com/
- OVR: https://ovrtechnology.com/products/omara-pro-scent-display
- EOS AromaTec II: https://www.eos-sauna.com/en/products/dosing-units/aromatec-ii ; Harvia Autodose: https://www.harvia.com/en/products/SASL1/autodose-steam-automat
- Oil safety: https://www.kemitron.com/blog/safe-enjoyment-why-diluted-natural-fragrances-are-the-best-choice-for-saunas ; https://organicaromas.com/blogs/aromatherapy-and-essential-oils/are-essential-oils-flammable/ ; https://viworo.com/en/pages/essential-oils-in-the-sauna ; https://cultureofbathing.substack.com/p/wet-debates-scent-or-sin
- Cariitti: https://www.saunaplace.com/products/cariitti-premium-glass-fiber-lighting-set ; https://www.saunaplace.com/products/cariitti-starlight-fiber-light-set-for-sauna-ceiling ; https://cariitti.fi/en/products/projectors/vpac-led-projector ; LED strip: https://bsaunas.com/product/cariitti-sauna-led-strip-light-set-2m-no-led-driver/ ; Harvia LED: https://wcsaunas.com/products/harvia-led-strip-light
- Acoustics: https://en.wikipedia.org/wiki/Whispering_gallery ; https://gearspace.com/board/studio-building-acoustics/979102-acoustic-treatment-large-circular-room-made-steel-concrete.html ; https://www.researchgate.net/publication/320107116_Circular_music_rooms_design_and_evaluation_methods ; https://saunaburg.com/blogs/wiki/mineral-wool-insulation ; https://wallpanelspro.com/en-us/blogs/news/wood-wool-acoustics-in-pools-spas-and-wellness-rooms
- Portland noise: https://www.portland.gov/code/18/10 ; https://www.portland.gov/code/18/10/010
- Precedents: https://aufguss-wm.com/ ; https://thermea.com/whitby/aufgusshow ; https://www.abathhouse.com/journal/williamsburg-sauna-expansion ; https://www.abathhouse.com/aufguss-wm-nationals-2026 ; https://www.othership.us/experience ; https://retaildesignblog.net/2024/08/19/othership-sauna-by-futurestudio/ ; https://beaire.com/en/aire-magazine/aire-scent-sebastien-lacouture-perfumer-scentmate ; https://www.thermegroup.com/our-story ; https://www.dezeen.com/2016/06/30/avanto-architects-loyly-coastal-sauna-helsinki-faceted-timber-cloak/ ; https://www.archpaper.com/2026/02/culture-of-bathe-ing-lands-domino-park-sauna/
