# Private Saunas (V2) — Electrical Design + Quote Package (Nov 9 2026)

**Status 2026-11-09 (later):** Davey: no panel, one circuit, outlets only. Rev AJ supersedes Rev AI (kept as the "if we ever want a panel" version). Drawing: `Assets/V2 Build Drawings/2026-11-09 Private Saunas V2 Electrical Set (Rev AJ).html`. No emails sent yet.

**Rev AJ in one paragraph:** the dock pedestal is 30 A (Davey 11/9), so a standard 30 A marine cord runs to a 30 A twist-lock inlet at the SE corner, with one 20 A GFCI breaker in a weatherproof box behind it (20 A outlets can't sit on a 30 A breaker). No panel, no combining two receptacles (770 W of 2,400). Seven GFCI outlets with in-use covers: E2 at each sauna's SW corner (24 V LED drivers plug in, Rev U), E6 inside each stove box (Inkbird), E11 at the water heater, E14 in each locker cubby. No heat tape outlet (Davey 11/9); the PEX gets drained for freezes. Load about 520 W of 2,400. Dimming by inline 24 V push-knob dimmers on the LV leads by the door, no 120 V switch. Keep the junction boxes under hatches and the empty conduit stubs (fire pits, both float edges) since the deck only opens once. One circuit of outlets is the easiest fit for an Oregon minor label.

---
*Rev AI below is history (11/9 morning): three circuits and a float panel.* Drawing: `Assets/V2 Build Drawings/2026-11-09 Private Saunas V2 Electrical Set (Rev AI).html` (sheets E-100 plan, E-101 room lighting, E-200 one-line, E-001 devices, J-001 junction boxes, L-001 load). Replaces E-001 and the electrical rows of U-001 in the Rev AH coordination set.

## Where things stood before today
- Rev U (10/17) cut electrical to the bone: one 20 A GFCI circuit tapped off "dock power" (tap point never confirmed), one outlet per sauna where the LED driver plugs in, a low-voltage box on the bench wall. No panel, no dimmers, no driver box, no phone chargers.
- 10/15 site walk wanted two LED runs per sauna on separate push-knob dimmers (Davey's Airstream style), a couple of small art spots outside, no can lights ever. That never made it back into the drawing set.
- Quotes: Powerall Electric, Jobber #946, **$6,420**, dated 10/7, sent to sauna@ 10/8, forwarded to Jonah 10/9. Powerall followed up 10/10 and 10/13 with no reply from us. Scope lines are not in the email body. Jonah (10/8) called $6k high and noted Powerall sits at the high end. Someone said "Young bid it as well" (10/8), but no Young quote exists in Slack, Gmail or the shared record. Neil at Boones Ferry Electric (Kyle's contact, 503-519-6236) was only ever introduced on 8/31; no quote. Jonah asked again 11/9: "Are we waiting on other electrical quotes?"
- Nobody has written down what dock power exists: amps, pedestal type, where the nearest free receptacle is.

## The design (Rev AI)
**Feed.** A marine shore-power cord from the nearest pedestal receptacle to an inlet on the float, like the boats and floating homes around us. Inlet at the southeast corner (same corner the gas comes aboard, beside the East gate) so staff reach it from the walkway without crossing a guest deck. Inlet and float panel are 50 A 125/250 V hardware (about $400 more than 30 A gear) with a 30 A adapter if the pedestal only offers 30 A. Today's load is about 2,300 W with a vacuum running, so 30 A works; 50 A is what makes a chiller or second heater possible later without redoing the inlet.

**Float panel (FP).** Lockable NEMA 3R box at the inlet, 50 A 2-pole main with 30 mA ground fault, surge protector, 8 spaces, 3 used. Inside: a duplex for the Wi-Fi mesh node and Blink sync module, and a smart relay for exterior lights.

**Three circuits (kept to 3 on purpose, see permits):**
| Ckt | Feeds | Notes |
|---|---|---|
| C1 20 A GFCI | Both saunas' lighting pods (E9): 24 V drivers A (cove E10) + B (bench + backrest strips E4), dimmed by the E5 push-knob pair outside each door | Hard-wired, serviced from outside, nothing 120 V inside the hot rooms |
| C2 20 A GFCI | Tankless heater E11 (about 140 W freeze protection), heat-tape outlets E13 at the water entry and the center-wall riser | Red label: never off in winter |
| C3 20 A GFCI | Convenience outlets E2 (one per sauna, now free for staff tools), stove boxes E6 with a receptacle each for the Inkbird, locker USB outlets E14 (optional), CO alarms, one 24 V driver for exterior lights (2 art spots per side E12, lantern lamp E15, step markers at ramp and gate E16, optional) | |

**Junction boxes, all under lift-out hatches:** JB-0 at the inlet; JB-1 East sauna SW corner; JB-2 base of the center wall (heater, with a capped stub up the wall); JB-3 West sauna SW corner; JB-4/5 under each intake box (stove boxes). **Empty conduit with pull strings:** S1/S2 at both fire-pit spots (beside the gas stubs), S3 at the zen lantern (used now, 24 V), S4 west edge at the ramp landing (future waterfall pump), S5 east edge at the zen deck (future 240 V chiller or a third sauna). Trunk is 1" conduit along the north edge of the shared utility lane under the front deck; branches ¾".

**Lighting per sauna (E-101):** high cove on all four walls skipping 3'-4" over the stove (Cariitti Sauna Ultra Ambient, 125 °C, pending Cariitti's OK for a gas-sauna ceiling); strips under the upper and lower bench nosings plus one behind the upper backrest; two 24 V push-knob dimmers in a weatherproof box on the latch side of the door at 44"; drivers in a vented weatherproof pod at the SW corner above the E2 outlet. E3 stays as a sealed low-voltage box in the upper back corner for a sensor. No fixture, outlet or switch inside the hot room.

## Permits, honestly (checked 2026-11-09)
- Portland Title 28, 28.03.020 A.1 item 8: a permit is required for "any new and/or alteration to any electrical... installation on a floating structure." 28.02.020 defines a floating structure as anything on flotation held by piling or mooring; a boat is a vessel that is not a floating structure. Our float is a floating structure. The cord-and-plug hookup makes us look like the neighbors but does not exempt the on-float wiring on paper.
- The state exemption list (OAR 918-309-0000) exempts plugging portable equipment into existing receptacles and work done under a minor label. It does not exempt new branch wiring or a panel.
- **Practical path: Oregon minor installation label.** Licensed electrical contractors buy them (10 for $140, so about $14 each), no plan review, one inspection included, up to 3 new circuits at 60 A or less, one label per job site. Excludes service/panel *replacement*, underground work, pools/hot tubs (Art. 680). That is why Rev AI is held to 3 circuits. Open question for the electrician: does Portland treat a float as a qualifying job site for a label. If yes, this is a $14 line on the quote, not a permit process. If no, it is a regular electrical permit with inspection; the design does not change.
- Sources: portland.gov/code/28/03/020, portland.gov/code/28/all, oregon.public.law/rules/oar_918-309-0000, oregon.gov/bcd/minlab/Pages/el-scope.aspx.

## Load (L-001, Rev AI history; Rev AJ is about 520 W, no heat tape)
LED cove 180 W + bench strips 80 W + heater 200 W + heat tape 250 W + Inkbirds/Wi-Fi/cameras 40 W + exterior lights 40 W + one staff tool 1,500 W = about 2,300 W. 30 A at 125 V gives 3,600 W; 50 A at 125/250 V gives 12,000 W. Future: fire-pit igniters, waterfall pump 600 W, chiller 450 to 1,100 W (Penguin 1/2 to 1 HP, 120 V) or larger at 240 V.

## Walkthrough questions (Davey + Grant + Mario + electrician)
1. Nearest pedestal to the SE corner, receptacles on it (30 A 125 V L5-30, 50 A 125/250 V SS2-50), one free? Photo of its label and breaker.
2. Cord length and route, slack for river level, does it cross the walkway.
3. Does the pedestal breaker have 30 mA ground fault already; if not the float main carries it.
4. Bonding: stoves, flues, gas pipe, heater cabinet to the equipment ground. No metal hull, galvanic isolator is the electrician's call.
5. Trunk lane under the front deck with Grant and Mario: power north edge, water, gas south edge, a few inches apart.
6. Minor label: does a float count as a job site; put the label on the quote.

## Electricians to quote (3 to 4 bids)
| Who | Contact | Why / status |
|---|---|---|
| Powerall Electric LLC (CCB 240396) | quote #946 thread in sauna@ | Already quoted $6,420 on the old one-circuit scope. Send Rev AI and ask for a re-quote on this scope. Two unanswered follow-ups from them; reply. |
| Boones Ferry Electric (Neil) | Neil@boonesferryelectric.com, 503-519-6236 (office 503-682-4936, CCB 88482, 4.8 to 4.9 stars) | Kyle's contact since 8/31, never quoted. Residential shop, good reviews. |
| Young Electric LLC | 503-706-9867, 9999 SW Wilshire St, Portland | Hot tubs, generators, 40 years. Fits the "young bid it" mention if that is who it was; confirm with Jonah. |
| Schooner Creek Boat Works (marine electrical) | 503-735-0569, 3255 N Hayden Island Dr | Hayden Island boatyard, does complete boat electrical systems. Best bet for someone who has wired shore-power inlets and panels; confirm they hold an electrical contractor license for the label. |
| Also ask | the moorage operator | who wired their dock pedestals; that electrician already knows this dock |

## Quote request (from sauna@, signed as the business; not sent as of 11/9 evening)
Attachment: `Assets/V2 Build Drawings/2026-11-09 Private Saunas V2 Electrical Set (Rev AJ).pdf`

Subject: Electrical quote request - two floating saunas, one shore-power circuit, Hayden Island

Hi [name],

We're Ebb & Ember, the floating sauna on the Columbia at 173 NE Bridgeton Rd. We're finishing two small private saunas on a new 18 x 36 ft float next to our existing one and would like a quote on the electrical. The plan set is attached. The short version:

- Stoves and water heater are natural gas, so the electrical is light: about 520 W total.
- Power comes from the dock pedestal, which is 30 A. Standard 30 A shore-power cord to a 30 A twist-lock inlet at the float's southeast corner.
- One 20 A GFCI breaker in a weatherproof box behind the inlet, then one circuit. No panel.
- 7 weatherproof GFCI outlets with in-use covers: 2 for the 24 V LED drivers (one per sauna, outside at the corner), 1 at the tankless water heater, 1 in each stove control box, 1 in each locker cubby.
- Everything in conduit under the deck with junction boxes at lift-out hatches, and a few capped empty stubs for later.
- Nothing 120 V inside the hot rooms. Lighting is 24 V strip with inline dimmers.

Two things we'd like your read on in the quote:
- Whether this fits under an Oregon minor installation label (one new circuit, one job site).
- What you need from the pedestal. We'll send a photo of its label and breaker.

Timing:
- Framing is done and the walls are open. Rough-in has to happen before the deck boards go down, ideally the week of November 17.
- A site visit this week or next would be great; any morning works.
- Could you send a quote by Friday, November 14?

Thanks!
Ebb & Ember
sauna@ebbandember.com | (503) 308-1293

Recipients (status 11/9 evening):
- Boones Ferry Electric (Neil, Neil@boonesferryelectric.com): Gmail DRAFT in sauna@ with the PDF attached, opens "Kyle at Bench Sauna passed along your name." Not sent.
- Schooner Creek Boat Works (info@schoonercreek.com, 503-735-0569): Gmail DRAFT in sauna@ with the PDF attached, opens "You're the closest yard to us and this is a shore-power job." Not sent.
- Powerall Electric (quote #946 $6,420): their emails come from Jobber's notification address, so a reply goes nowhere. No public email found; phone (971) 533-1279 per CCB. Call, or ask Jonah for the email he used to request the quote; then send the same note with "Thanks for the October quote, the scope changed, here is the updated design for a re-quote."
- Young Electric LLC: no public email, only the form at youngelectricco.rynosites.com/contact-us. Phone (503) 706-9867. Confirm with Jonah whether this is the "Young" who bid. Paste the bullets into the form or call.

## Open for Davey
- Say send: Neil + Schooner Creek drafts go out as is. Powerall and Young need an email address (Jonah) or a phone call.
- OK sending the quote request to Powerall (re-quote), Boones Ferry, Young, Schooner Creek.
- Who answers Jonah's 11/9 "are we waiting on other electrical quotes" in #private-saunas-build.
- Add the electrician to the float walkthrough (U-002) so the tap point, cord route and hatch spots get settled in one visit.
