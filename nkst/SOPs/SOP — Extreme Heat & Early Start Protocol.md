# SOP — Extreme Heat & Early Start Protocol

*Created 2026-08-11 from River B.'s heat exhaustion report (August 2026)*
*Status: **DRAFT — trigger temperature pending David's sign-off.** Scripts below are approved for use now.*

> **The short version:** On forecast-hot days we ask each booked group to move up to an earlier start rather than changing the published time across FareHarbor and every OTA. We frame it as an upgrade, not a warning. Guides never eat a double-tour heat day in silence.

---

## Why this exists

August 2026: a guide came off two back-to-back tours with heat exhaustion. The team looked at moving the 9am start to 8:15am for all of August in FareHarbor, but the published time is mirrored across GetYourGuide, Viator, Airbnb Experiences and the website, so a blanket change is a large, error-prone lift for a handful of dangerous days.

The call: keep the published times, shift **per group, per day** when the forecast crosses the trigger. Revisit a permanent seasonal start-time change for **July–August 2027** — that decision goes in the annual planning cycle, not mid-season.

---

## Trigger

**Recommended (pending sign-off):** forecast high of **95°F or above**, or **heat index 105°F or above**, at the tour location during the tour window.

River's field read, for the record: 92°F+ is where it starts to bite, 97°F is dangerous. The 95/105 line splits that and gives one number guides don't have to interpret.

Checked against NOAA / National Weather Service for the tour parish, not a phone default weather app.

| When | Who | Action |
|---|---|---|
| 48–72 hrs out | Contractor / office | Scan the week's forecast against the trigger. Flag hot days in Slack. |
| 24–48 hrs out | Office (preferred) or guide | Send **Text 1** to every booked group on a flagged day. |
| 24 hrs out | Office | Update FareHarbor booking time for groups that said yes. Message OTA-booked guests through the platform. |
| Night before | Guide | Send **Text 4** confirming the new meet time. |

**Who sends it:** office by default. Guides often don't have the guest's number until the night before, and OTA bookings route through the platform. Guides flag the date, the office runs the outreach.

---

## Which tours actually need the shift

Tour times are 9am · 11:30am · 2pm · 4:30pm.

- **9am → 8:15am.** The clean, easy move. This is the one the scripts below are written for.
- **11:30am and 2pm** are the genuinely brutal slots on a 97°F day and they have nowhere earlier to go. On trigger days these are the tours to watch for guide load, not just guest comfort.
- **4:30pm** cools off on the back half and is usually fine.

**Open item for David:** on a 97°F+ day, is the 2pm a tour we run at all, or do we consolidate it into the 4:30? Not decided.

---

## Guide load rule

No guide runs **more than one tour** on a trigger day without explicitly agreeing to it and confirming they've got shade, fluids and a break between. Two tours in that heat is how we got here.

If a guide isn't comfortable running an assigned tour on a trigger day, they say so to the contractor **as early as possible** — that's not flaking, that's the system working. The contractor finds coverage or moves the guests. A guide is never in the position of privately deciding between their own health and stranding a group.

---

## The texts

Copy-paste ready. Keep them in the guide phone bookmarks and in [[New Orleans Kayak Swamp Tours — SOP Guest Communication Templates]].

### Text 1 — the ask (24–48 hrs out)

> Hey [Name]! It's [Guide] with New Orleans Kayak Swamp Tours. Quick heads up on your [day] tour: the forecast is showing [97] that afternoon, so we're offering an earlier start at 8:15am instead of 9. Cooler paddle, way more wildlife moving around, and the water's glassy that early. It's genuinely the better tour. Does 8:15 work for your group?

Why it works: gives a reason, gives a benefit, asks one yes/no question. Framed as an upgrade. Nobody cancels over being offered the better slot.

### Text 2 — if they hesitate

> Totally get it, that's an early one. If 8:15 is a stretch we can keep you at 9, just want you to know what you're walking into: it'll be in the mid-90s with full sun and no shade out there. Bring double the water you think you need, a hat, and long sleeves if you have light ones. Either way we've got you.

Informative, not alarming. Puts the choice on them without a lecture.

### Text 3 — group can't move and the tour isn't going out

Guide raises it with the contractor **first**, never straight to the guest. Then the guest gets:

> Hey [Name], following up on [day]. With the heat where it's headed we're not able to run the 9am. We can move you to 8:15 that morning, put you on another day this week, or refund you in full, whichever is easiest. Let me know and I'll take care of it.

Three options, all painless. Refund on the table upfront ends the argument before it starts.

### Text 4 — night-before confirm (once they've agreed)

> Confirmed for 8:15am tomorrow! Meet us at [location]. Bring water, sunscreen, and shoes that can get wet. See you out there.

### OTA bookings (Viator, GetYourGuide, Airbnb)

Send **Text 1** through the platform's message thread first — OTA guests often haven't given a real phone number. Add:

> I'll update your booking on [Viator] once you confirm so everything matches.

Then update the booking. Don't update it before they confirm or the platform notification contradicts the ask.

---

## Language rules

- **Never** promise or imply the tour is safe, or that moving the time makes it safe. Say cooler, more comfortable, better wildlife. (See [[feedback_never_assure_safety]] standard across all vaults.)
- Don't lead with heat danger. Lead with the upgrade. The danger framing is Text 2, and only if they push back.
- Don't apologize for the ask. We're offering them something better.
- No em dashes, no corporate phrasing. These read as a person texting.

---

## On-water heat management (guide-side)

On any trigger day, regardless of start time:

- Extra water in the van, more than you think you need, plus a cooler with ice
- Say it in the safety briefing: drink before you're thirsty, tell me if you feel off
- Watch for the early signs in guests **and in yourself**: headache, nausea, stopped sweating, confusion, cramping
- Build in a shade stop — cypress cover or the bank — and make it part of the tour, not an emergency
- Anyone showing heat symptoms: get them off the water, into shade, cool water on the neck and wrists, cold fluids. If they stop sweating or get confused, that's heat stroke, call 911.
- Log it in the tour audio log and file an Incident Report if a guest or guide needed intervention

---

## Logging

Every heat-triggered shift goes in the cancel/change log at `Operations/Tour Cancel Log.md` with reason "heat shift." Two things it buys us: the pattern data to decide the 2027 summer start times, and a record that we acted on a known condition.

---

## Open items

| Item | Owner | Status |
|---|---|---|
| Confirm the trigger number (95°F / heat index 105 recommended) | David | Open |
| Decide whether 2pm runs at all on 97°F+ days | David | Open |
| Permanent July–August start-time change for 2027 | David | Deferred to annual planning |
| Add heat protocol to the Comprehension Quiz | Contractor | Open |

---

*See also: [[SOP — Weather Decision Flowchart]] · [[Kayak Tour Guide Handbook 2026]] · [[New Orleans Kayak Swamp Tours — SOP Guest Communication Templates]]*
