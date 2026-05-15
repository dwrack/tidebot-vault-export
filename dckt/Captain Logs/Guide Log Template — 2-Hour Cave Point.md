# Guide Log — {{date}} — 2-Hour Cave Point Tour — {{launch_time}}

**Guide:** {{guide_name}}
**Launch Point:** {{launch_point}}
**Tour Time:** {{launch}} - {{return}}
**Paddler Count:** {{count}}   **Manifest in FareHarbor:** [link or screenshot]

---

## Pre-Launch Conditions

- **Air temp:** {{air}}°F   **Water temp:** {{water}}°F
- **Wind:** {{wind}} mph from {{direction}}
- **Wave height:** {{waves}} ft
- **Sky / forecast next 2 hrs:** {{forecast}}
- **Specific hazards today:** {{hazards}}

## Pre-Launch Safety Check

- [ ] All guests have signed digital kayaking waiver in FareHarbor
- [ ] Headcount matches manifest
- [ ] Each guest fitted with PFD, visually inspected
- [ ] Paddles distributed, sized to each guest
- [ ] Whistle on guide and on sweep (if applicable)
- [ ] First aid kit + tow line on guide's kayak
- [ ] Weather rechecked within 30 min of launch
- [ ] No guest visibly impaired
- [ ] Disclosed allergies on manifest reviewed (if half-day food, not applicable here)

**Issues found and how resolved before launch:**
> {{note}}

---

## Audio/Video Dock Briefing

**Recording started:** {{time}}   **File name:** {{file}}.mp4 or .m4a

**Recording posted to Slack channel:** `#dckt-guide-logs`   **Posted at:** {{time}}

**Briefing script (guide reads aloud on camera/audio — hit every numbered item):**

> *"This is [guide name] with Door County Kayak Tours. Today is [date] at [time]. We're launching from [dock]. I'm recording this safety briefing as part of our standard operating procedure. Wind is [X] mph from [direction], water temp [X], wave height [X] feet, forecast next two hours is [X]. We have [X] paddlers on the 2-hour Cave Point sea caves tour. I'm going to walk through the safety briefing now and ask each of you to verbally confirm at the end."*
>
> 1. **PFD.** "Everyone is wearing a Coast Guard approved PFD I personally fitted. PFD stays on the entire time on the water, no exceptions."
> 2. **Dock launch pinch.** "When you're entering and exiting the kayak, keep your hands inside the kayak or on the paddle shaft. Fingers can be crushed between the kayak and the dock, or between two kayaks. I'll assist each of you."
> 3. **Sit-on-top behavior.** "These are sit-on-top kayaks. They can flip. There's no spray skirt holding you in. If you come off, stay with your paddle, stay with the kayak if possible, signal me, do not swim for shore."
> 4. **Cave hazards.** "Inside the sea caves there are low rock ceilings that can hit your head, walls that can scrape kayaks, and wave surge that pushes you against rock. Enter only when I signal. One kayak at a time when I tell you. Duck when I say duck."
> 5. **Cold water.** "Lake Michigan is cold even on warm days. Cold shock is real. If you flip, stay with the kayak, hold the paddle, I will come to you."
> 6. **Weather change.** "If I call return to shore, every paddler turns and follows me immediately. No questions on the water. Lightning, wind, or wave change can require an immediate exit."
> 7. **Signals.** "Three whistle blasts means emergency. Raised paddle means you need my attention. I'll use hand signals for stop, follow, return, and gather."
> 8. **Spacing and group rule.** "Stay one kayak length back from the paddler in front of you. Do not pass me. Do not fall behind the sweep. Do not paddle away from the group."
> 9. **Sober.** "Anyone under the influence of alcohol or impairing substances cannot paddle today. No exceptions."
> 10. **Personal items.** "Phones, sunglasses, keys are at your own risk. Dry bags are available at the shop."
>
> *"Any questions before we launch? [pause] OK, I need each of you to say your name and 'I understand' on this recording."*
>
> Guest 1: [name] — [response]
> Guest 2: [name] — [response]
> Guest 3: [name] — [response]
> (continue for full group)
>
> *"Group photo at the dock now. Recording ending at [time]."*

**Group photo at dock:** [ ] taken   **Filename:** {{photo}}.jpg

---

## Mid-Trip / End-of-Trip Slack Check-In

Guide posts a short check-in to `#dckt-guide-logs` near the end of the tour (last 10 minutes on the water or immediately after take-out). Same Slack thread as the pre-launch briefing video. Format:

```
End-of-trip check | 2hr Cave Point | [date] [launch time] | guide [name]
Trip quality (1-5): __
Mechanical / gear issues: YES / NO — [detail]
Incidents or guest complaints: YES / NO — [detail]
Asked for reviews: YES / NO
```

A YES on incidents or mechanical issues triggers an `@manager @owner` mention in the same Slack post so it surfaces immediately. No SMS, no GHL workflow — Slack channel is the system of record.

---

## Post-Trip

**Return time:** {{time}}

**Incidents during tour (check all that apply):**

- [ ] None — routine trip
- [ ] Guest fell off kayak or capsized
- [ ] Guest injury (cut, sprain, pinch, head bump, other)
- [ ] Near-miss in cave, with rock, with another paddler, with motorized boat
- [ ] Equipment malfunction or gear failure
- [ ] Weather decision (cut tour short, rerouted, sheltered)
- [ ] Guest complaint requiring intervention
- [ ] Other watercraft incident
- [ ] First aid administered
- [ ] Tow used
- [ ] Other

**Details:**
> {{what happened, what was done, outcome — be specific. If injury, name and exact body part affected.}}

**Post-trip audio/video addendum recorded:** [ ] yes  [ ] no
**Filename and Slack post:** {{file}} → posted at {{time}}

## Post-Trip Equipment

- [ ] All kayaks rinsed and racked
- [ ] PFDs hung to dry
- [ ] Paddles racked
- [ ] First aid restocked if used
- [ ] Tow line and whistle returned to bin
- [ ] Damaged gear flagged in Slack: {{detail}}

---

## Slack + File Routing

1. **Audio/video pre-launch briefing** → posted in `#dckt-guide-logs` with caption `Pre-launch | 2hr Cave Point | [date] [time] | guide [name]`
2. **Group photo** → same Slack thread
3. **Mid-trip captain log SMS** → handled by GHL automation, replies stored in GHL contact record
4. **Post-trip incident audio/video** (only if incident occurred) → same Slack thread, caption `Incident addendum`
5. **This Guide Log file** → saved as `Guide Log — YYYY-MM-DD — 2hr Cave Point — [launch time].md` in `Captain Logs/` folder, with links to all Slack uploads
6. **Audio/video files auto-backup** → Google Drive `DCKT > Guide Logs > YYYY > MM` (set up via Slack-to-Drive integration or Zapier)

**Retention:** Minimum 7 years from tour date for both audio/video and written log. Do not delete until cleared by attorney.

---

## Wisconsin Recording Note

Wisconsin is a one-party consent state for audio recording (Wis. Stat. § 968.31). The guide is a party to the conversation and may record without separate consent. However, **the script discloses recording up front** as best practice and to support admissibility. For groups including minors, prefer audio-only unless a parent has verbally agreed on the recording. Do not film faces of minors in promotional or non-safety contexts; this log is for safety/legal use only and is not a media release.

---

*Transcribed from guide audio/video log posted to Slack. Original audio/video retained for liability and incident review.*
