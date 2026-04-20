# DCKT — GHL Automation Workflows Spec
*Ready to build once DCKT location ID + PIT token are in*

---

## Overview

Two automation tracks:
1. **Customer-facing** — from first contact through post-tour advocacy
2. **Guide-facing** — from hiring through end of season offboarding

All workflows live in GHL → DCKT sub-account → Automation.

---

## TRACK 1 — Customer-Facing Automations

---

### Workflow 1: Missed Call → Lead Nurture
**Trigger:** Inbound call → not answered
**Delay on first message:** 60 seconds max

| Step | Delay | Channel | Message |
|---|---|---|---|
| Message 1 | Immediate | SMS | "Hi! This is Door County Kayak Tours — sorry we missed your call! Any questions? Book online at doorcountykayaktours.com or text us back anytime 😊" |
| Check: did they reply or book? | Wait 24hrs | — | If yes → stop. If no → continue |
| Message 2 | +24 hrs | SMS | "Hey [Name] — still thinking about getting out on the water? Cave Point is one of the most stunning places in Wisconsin and we'd love to take you there. Here's what guests say: [TripAdvisor link]. Spots fill fast on weekends!" |
| Check: did they reply or book? | Wait 48hrs | — | If yes → stop. If no → continue |
| Message 3 | +72 hrs | SMS | "Last one from us, [Name]! We have a few openings this weekend if you're still interested. No experience needed — we take care of everything. Book in 2 minutes: doorcountykayaktours.com 🙌" |
| End | — | — | Remove from sequence |

**Tags to apply on entry:** `lead-missed-call`
**Tags to remove on booking:** `lead-missed-call` → apply `booked`

---

### Workflow 2: Booking Confirmation + Upsell
**Trigger:** New booking created in FareHarbor → webhook → GHL contact tagged `booked`

**Step 1 — Check: returning guest?**
- If contact has tag `returning-guest` → go to **Workflow 2B (Returning)**
- If not → go to **Workflow 2A (First-timer)**

#### Workflow 2A — First-Timer Booking

| Step | Delay | Channel | Message |
|---|---|---|---|
| Booking celebration | Immediate | SMS | "🎉 You're on, [Name]! We confirmed your [TOUR] on [DATE] at [TIME] — so excited to have you. Is this a special occasion? Let us know and we'll make it extra memorable!" |
| Upsell check | +30 min | SMS | "Quick question — have you thought about going private? For your group it's only a little more and you get the whole experience to yourselves. Just reply 'private' and we'll sort it out!" |
| Wait for reply | 4 hrs | — | If they reply 'private' → hand off to human |

#### Workflow 2B — Returning Guest Booking

| Step | Delay | Channel | Message |
|---|---|---|---|
| Welcome back | Immediate | SMS | "Welcome back, [Name]! 🙌 We noticed this isn't your first time — we love that. Your guide knows you've been before. We've got something a little different planned. Can't wait." |

---

### Workflow 3: Pre-Tour Anticipation Arc
**Trigger:** Booking confirmed + tour date set
**Branch on:** First-timer vs returning guest (tag-based)

#### First-Timer Arc

| Step | Timing | Channel | Message |
|---|---|---|---|
| T-3 days | 3 days before tour | SMS | "Hey [Name]! 3 days until your Cave Point paddle 🌊 Those sea caves are only reachable by water — you're about to see something most people never will. Your guide takes care of everything. Any questions?" |
| T-1 evening | Evening before tour | SMS | "Tomorrow's the day, [Name]! Your guide [GUIDE] is pumped to take you out. Quick checklist: ✅ Hat, sunglasses, sunscreen ✅ Light layers (no cotton) ✅ Water shoes ✅ Camera 📸 Meet at Schauer Park Boat Launch at [TIME]. See you there!" |
| Day-of | 2 hrs before tour | SMS | "Good morning [Name]! Today's the day 🙌 [GUIDE] is heading to the launch now. See you at [TIME] at Schauer Park — look for the blue van. Get pumped!" |

#### Returning Guest Arc

| Step | Timing | Channel | Message |
|---|---|---|---|
| T-3 days | 3 days before tour | SMS | "Hey [Name] — you've done this before so you know what you're in for. This time your guide has something a little different planned. We'll talk when you get here. See you [DAY]." |
| T-1 evening | Evening before tour | SMS | "Tomorrow, [Name]! Your guide [GUIDE] knows it's your [3rd] time out with us. Schauer Park Boat Launch, [TIME]. Same blue van — new experience. 🌊" |
| Day-of | 2 hrs before tour | SMS | "Morning [Name]! [GUIDE] is on the way to the launch. Conditions look great. See you at [TIME] — something good is coming today." |

---

### Workflow 4: Weather Cancellation — Cave Point Only
**Trigger:** Manual tag applied: `cancel-cave-point` on booking record
**Time sensitivity:** Must go out by 7:00 AM

| Step | Delay | Channel | Message |
|---|---|---|---|
| Cancellation notice | Immediate | SMS | "Hello from Door County Kayak Tours. Unfortunately due to unsafe wind/wave conditions we won't be running Cave Point today. We have our [ECO TOUR / BLUFF TOUR / ESTUARY TOUR] available — want to switch, or reschedule? Let us know and we'll take care of you!" |
| No reply follow-up | +2 hrs | SMS | "Hey [Name] — still want to get out on the water today? We have [ALTERNATE TOUR] running — reply 'yes' and we'll move you over. Otherwise we're happy to find you a new date!" |

---

### Workflow 5: Full Weather Cancellation
**Trigger:** Manual tag: `cancel-all-tours`

| Step | Delay | Channel | Message |
|---|---|---|---|
| Cancellation | Immediate | SMS | "Hello from Door County Kayak Tours. Due to weather we won't be running any tours today. We'd love to get you back out — visit doorcountykayaktours.com to rebook, or reply here and we'll help you find a new date!" |

---

### Workflow 6: Post-Tour Fan Sequence
**Trigger:** Tour completion (manual tag `tour-complete` applied by guide via GHL mobile, or FareHarbor webhook)
**Branch:** First-timer vs returning guest

#### First-Timer Post-Tour

| Step | Timing | Channel | Message |
|---|---|---|---|
| Warm close | 1 hr after | SMS | "That was incredible, [Name]! So great having you with us today 🌊 Hope Cave Point blew your mind. If you got any shots, tag us — we'd love to share them! @doorcountykayak" |
| Review ask | 3 hrs after | SMS | "Hey [Name] — one small favor? If your guide [GUIDE] and the crew made your day, a quick TripAdvisor review means the world to our small team. Takes 2 min: [LINK]. Thank you! 🙏" |
| Re-engagement | +7 days | SMS | "Hey [Name]! Hope you're still feeling that Door County magic 🌲 You did Cave Point — have you tried the Sunset Tour? Totally different vibe, completely worth coming back for. Reply 'sunset' and we'll check availability!" |
| End of season | October | SMS | "Hey [Name] — wrapping up an amazing season! We hope we made your Door County trip unforgettable. We open bookings for next summer in [MONTH] — want us to reach out when spots go live? Reply 'yes' 🙌" |

#### Returning Guest Post-Tour

| Step | Timing | Channel | Message |
|---|---|---|---|
| Personal close | 1 hr after | SMS | "That was a good one, [Name]. Thanks for coming back — you're part of what makes this place special. Hope the [specific moment] stuck with you. 🌊" |
| Review ask | 3 hrs after | SMS | "Hey [Name] — you've been with us a few times now, and that means the world. If you have a minute, a review on TripAdvisor helps other people find us: [LINK]. You know what to say better than anyone 😊" |
| Annual close | +7 days | SMS | "Hey [Name] — is there something you haven't done yet that you want to try next time? Sunset paddle, fall colors, something else? Reply and we'll make a note — we'll have it ready when you come back." |
| Milestone (3rd visit) | Same day | Internal task | **Create task for David:** "Send personal note to [Name] — 3rd visit. Consider mailing Paddler's Circle token." |

---

### Workflow 7: Referral Engine
**Trigger:** Tag `tour-complete` + tag `review-sent`
**Delay:** 24 hours after post-tour sequence starts

| Step | Delay | Channel | Message |
|---|---|---|---|
| Referral ask | +24 hrs from tour | SMS | "One more thing, [Name] — if you have friends or family visiting Door County this summer, we'd love to take care of them. Share this link and they get $10 off, and we'll send you a thank-you too: [REFERRAL LINK]" |

---

### Workflow 8: Lead Re-Engagement (Seasonal)
**Trigger:** Scheduled — every March when season opens
**Audience:** All contacts tagged `past-customer`

| Segment | Message |
|---|---|
| 2+ visits | "Hey [Name] — season opens in a few weeks. You've been with us [N] times. You get first pick before we go public. Want me to grab you a date?" |
| 1 visit | "Hey [Name]! Door County Kayak Tours season is almost here 🌊 Hope to see you back this summer — spots always go fast. doorcountykayaktours.com" |
| Lead (never booked) | "Hey [Name]! Summer in Door County is almost here — we'd love to finally get you out on the water. Any questions? doorcountykayaktours.com" |

---

## TRACK 2 — Guide-Facing Automations

---

### Workflow G1: New Guide Hire Welcome
**Trigger:** Contact created with tag `guide-hired-2026`

| Step | Delay | Channel | Message |
|---|---|---|---|
| Welcome | Immediate | SMS | "Welcome to the DCKT crew, [Name]! 🙌 David here. So pumped to have you on the team this season. We'll get you set up with everything you need. First step — check your email for onboarding instructions." |
| Onboarding email | +1 hr | Email | Full onboarding email: housing info, training dates, system access links, gear checklist |
| Training reminder 1 | 3 days before training | SMS | "Hey [Name]! Training camp starts [DATE] at [TIME] — make sure you've read the Training Manual and have your gear list ready. Any questions before then?" |
| Training reminder 2 | Day before training | SMS | "Tomorrow's the day, [Name]! Training at [TIME], [LOCATION]. Bring: [GEAR LIST]. See you there!" |

---

### Workflow G2: Shift Notification
**Trigger:** Tour assigned to guide in scheduling system
**Send:** 24 hrs before shift

| Step | Delay | Channel | Message |
|---|---|---|---|
| Shift reminder | 24 hrs before | SMS | "Hey [Name]! Reminder — you've got a [TOUR NAME] tomorrow at [TIME]. [X] guests booked. Meet at Schauer Park by [PREP TIME]. Check the weather and text David if anything looks off. See you out there! 🚣" |
| Day-of confirmation | 2 hrs before | SMS | "Morning [Name]! Today's [TOUR] at [TIME]. Guests confirmed. Weather: [CONDITIONS]. You're good to go — see you at the launch!" |

---

### Workflow G3: Weather Cancel → Guide Alert
**Trigger:** Tag `cancel-cave-point` or `cancel-all-tours` applied
**Fires simultaneously with customer cancellation workflow**

| Step | Delay | Channel | Message |
|---|---|---|---|
| Guide alert | Immediate | SMS | "Hey [Name] — [Cave Point / all tours] cancelled today due to [conditions]. [Alternate tour is running / no tours today]. David will follow up with details. Stand by." |

---

### Workflow G4: End of Season Offboarding
**Trigger:** Manual tag `end-of-season-2026` applied to guide contacts

| Step | Delay | Channel | Message |
|---|---|---|---|
| Close out | Immediate | SMS | "Hey [Name] — what an incredible season. Thank you for everything you gave to DCKT guests this year. End-of-season checklist is in your email — complete it before your last day. David wants to connect with you before you head out." |
| Housing notice | +1 day | Email | Housing checkout instructions, deposit return timeline, final paycheck info |
| Re-hire seed | +2 weeks | SMS | "Hey [Name] — hope you're settling back in. We'd love to have you back next season. If you're interested, let David know by [DATE] and we'll hold your spot. You were a huge part of what made this summer great." |

---

## Tags Reference

| Tag | Meaning |
|---|---|
| `lead-missed-call` | Called, didn't answer, in nurture |
| `booked` | Has an active booking |
| `returning-guest` | 2+ prior bookings in FareHarbor |
| `tour-complete` | Tour has been completed |
| `review-sent` | Review request has been sent |
| `past-customer` | Has completed at least 1 tour |
| `cancel-cave-point` | Cave Point tour cancelled today |
| `cancel-all-tours` | All tours cancelled today |
| `guide-hired-2026` | New guide, 2026 season |
| `end-of-season-2026` | End of season triggered |
| `paddlers-circle-3` | 3rd visit milestone reached |

---

## Build Priority Order

1. Workflow 1 — Missed Call + Lead Nurture *(highest immediate ROI)*
2. Workflow 2 — Booking Confirmation + Upsell
3. Workflow 3 — Anticipation Arc (first-timer)
4. Workflow 6 — Post-Tour Fan Sequence
5. Workflow 4/5 — Weather Cancellation flows
6. Workflow 3B — Returning Guest Anticipation
7. Workflow 7 — Referral Engine
8. Workflows G1–G4 — Guide-facing (build with Bella)
9. Workflow 8 — Seasonal Re-engagement (March 2027)

---

*Related: [[DCKT AI Chat-SMS Bot — SOP & FAQ Training Guide]]*
*Related: [[DCKT — Guide Training & Customer Journey Playbook]]*
*Related: [[DCKT — Systems Integration Hub]]*
