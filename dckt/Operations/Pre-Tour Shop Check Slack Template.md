# Pre-Tour Shop Check — Slack Template
*Beat 2 of the 11-beat pathway. Posted by front desk (Jessica / Lea / opener) in `#dckt-tour-logs` at the start of each day, one per scheduled tour.*

---

## Purpose

Two jobs in one Slack post:

1. **Operational check** — confirms every guest is checked in, waiver signed, video acknowledged, and any health/pregnancy/allergy flags are surfaced before the guide gets to the dock briefing
2. **Pre-flight for the guide** — when the guide opens Slack on the way to the launch, they should be able to read this post once and know everything they need before they meet the group

This post happens BEFORE the guide records the dock briefing video. The dock briefing video starts the day's tour thread; the pre-tour shop check post can either be its own message that the guide threads off of, OR posted as the first reply once the guide creates the thread. Pick one and stay consistent — see "Threading convention" below.

---

## When to post

- **Standard:** ~30 minutes before scheduled launch time, once all guests have checked in at the shop
- **Walk-up additions:** Edit the existing post (or reply in the thread) when a walk-up is added; don't make a new post
- **No-show:** Edit the post to reflect actual headcount. Don't delete the no-show line — strikethrough it so we have the record

---

## Threading convention

For the 2026 season, run it this way:

1. Front desk creates a **standalone message** in `#dckt-tour-logs` at the start of the day for the upcoming tour
2. Guide later starts a **separate thread** with the dock briefing video (because the briefing video is the legal record-anchor)
3. Guide replies to the briefing thread with a link back to the pre-tour shop check post for cross-reference

Why split: the pre-tour check happens before the guide is on-site. If we forced one thread, the guide would need to track down the existing message and reply to it from the dock with the briefing video. Two messages, cross-linked, is cleaner.

If this gets clunky in practice, switch to "one thread per tour, started by front desk" in v2.

---

## The post — copy/paste template

```
🛶 Pre-tour shop check | 2hr Cave Point | [date] | launch [time]
Guide: [name]
Group: [size] guests
Booking #: [FareHarbor confirmation]

Checked in:
✅ [Name 1] — first-timer
✅ [Name 2] — 2nd visit
✅ [Name 3] — first-timer

Waivers: ✅ all signed
Safety video: ✅ all acknowledged (3 pre-watched, 0 in-shop)

Health/special flags:
- [Name 2] disclosed asthma (inhaler with her)
- [Name 3] first-timer, nervous swimmer — flagged to guide

Conditions check (front desk's first read):
Air [X]°F / Water [X]°F / Wind [X] mph / Sky [clear/partly/overcast]
Provisional call: GREEN

Notes:
- Birthday in the group ([Name 1]) — guide do something
- Party of 3 arrived 15 min early
```

---

## What every section means

**Header line:** Tour type + date + launch time. Makes it scannable when scrolling the channel.

**Guide:** Who's on the tour. Drives Slack notifications if @mentioned.

**Group:** Headcount as confirmed in person. Should match FareHarbor + walk-ups.

**Booking #:** For incident retrieval. Link to FareHarbor manifest if your Slack supports it.

**Checked in:** Names from the manifest, each with visit-count flag pulled from FareHarbor customer history. This is the guide's pre-read for the Paddler's Circle ritual at Beat 11. **Visit count is critical — guide needs it before launch.**

**Waivers + Safety video:** Simple ✅. If anything failed, call it out: "❌ [Name] waiver missing, signing now."

**Health/special flags:** This is the most legally important section. Anything disclosed during the private health check (Beat 2):
- Allergies (especially food, bee stings)
- Pregnancy (especially trimester)
- Heart, respiratory, seizure, diabetes
- Recent surgery
- Anxiety / nervous swimmer
- Anyone who is NOT a confident swimmer
- Any medication that affects judgment or thermal regulation

If a flag is sensitive (pregnancy, mental health), use first name only or party name. Slack is searchable; don't put medical detail in a way that creates HIPAA-adjacent concerns.

**Conditions check:** Front desk does a first read on the weather; guide does the final call at the dock per `Operations/Cold Water Go-No-Go Protocol.md`. If front desk's first read is RED or borderline YELLOW, ping the guide via `@guide` so they know before they start the drive to the launch.

**Notes:** Anything else worth knowing — birthdays, returning guests with stated preferences from last visit, guests who arrived early/late, group dynamics.

---

## When to escalate via Slack mention

- `@guide` — anytime there's a flag the guide needs to see before they get to the dock (health, conditions concern, special occasion)
- `@manager` (Bella or Jessica) — anything that needs a manager call: a YELLOW condition needing approval, a walk-up that pushes group size over 14, a no-show pattern, a guest who arrives impaired
- `@owner` (David) — actual incidents, system failures, anything that smells like a lawsuit. Don't overuse.

---

## What to do if check-in is incomplete at launch time

If a guest hasn't checked in 15 min before launch:

1. Call them from the shop phone (FareHarbor has their number on the manifest)
2. If they don't answer, mark in the Slack post: `❌ [Name] no-show as of [time], called, voicemail`
3. Tour proceeds with confirmed guests
4. Refund/reschedule handling per FareHarbor policy

---

## Example posts

### Example 1 — Clean GREEN day

```
🛶 Pre-tour shop check | 2hr Cave Point | 2026-06-15 | launch 10am
Guide: Bella
Group: 8 guests
Booking #: FH-298471

Checked in:
✅ Tompkins party (4) — all first-timers
✅ Reyes party (2) — first-timers
✅ Karim party (2) — Karim 3rd visit, partner first-timer

Waivers: ✅ all signed
Safety video: ✅ all acknowledged (6 pre-watched, 2 in-shop)

Health/special flags: none

Conditions check:
Air 72°F / Water 64°F / Wind 8 mph SW / Sky clear
Provisional call: GREEN

Notes:
- Karim returning — Paddler's Circle 3-visit postcard ready at the dock
```

### Example 2 — YELLOW day, flagged

```
🛶 Pre-tour shop check | 2hr Cave Point | 2026-05-23 | launch 9am
Guide: David
Group: 6 guests
Booking #: FH-298502

Checked in:
✅ Lawson party (4) — first-timers, kids 12 and 14 with parents
✅ Park (2) — first-timers

Waivers: ✅ all signed
Safety video: ✅ all acknowledged (4 pre-watched, 2 in-shop just now)

Health/special flags:
- Mrs. Lawson disclosed mild asthma (inhaler with her, controlled)
- 12-year-old: nervous swimmer per parent, wearing PFD all tour

Conditions check:
Air 58°F / Water 51°F / Wind 14 mph NE / Sky overcast
Provisional call: YELLOW

@David — please confirm YELLOW go/no-go. Sweep guide needed; Jessica is available.
All guests confirmed in synthetic layers (verified at check-in).

Notes:
- Lawson group is here for a memorial trip — be gentle, no theatrics
```

---

## Saving this post for the record

Slack archives the channel weekly to Google Drive (`DCKT > Guide Logs > YYYY > MM`). The pre-tour shop check post is part of the per-tour record alongside the dock briefing video and closeout. 7-year retention applies.

---

## Open items for David / Bella to redline

- [ ] Confirm threading convention (separate post + briefing thread, vs. one unified thread)
- [ ] Confirm channel name: `#dckt-tour-logs` vs. `#dckt-guide-logs` vs. other
- [ ] Decide who owns the daily morning posts: Jessica (incoming manager) is the natural fit; Lea backs up
- [ ] Add a checklist line for FareHarbor charges if it makes sense (or leave for end-of-day rollup)
- [ ] Decide whether visit count is auto-pulled into FareHarbor manifest export (would simplify the "Checked in" section)

---

*DRAFT v1 — written 2026-05-14. Locked for Bella training week May 18-19 walkthrough.*
