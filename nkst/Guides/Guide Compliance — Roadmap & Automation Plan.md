# Guide Compliance — Roadmap & Automation Plan
*Created: 2026-03-30 | Review with Michelle: March 31, 2026*

> **Goal:** Get every active 2026 guide fully compliant (W-9, DL, signed ICA, CPR) before season peaks — and automate as much of the ongoing maintenance as possible so Michelle isn't chasing paperwork manually.

---

## The Problem, Plainly

Out of 13 active guides on the 2026 roster:
- **10 have no W-9 on file**
- **10 have no DL on file**
- **0 have a confirmed signed 2026 ICA** (current template had errors anyway)
- **Nick Napoda** — full-time guide, no email on file at all
- **Becks Walker** — W-9 on file, DL missing
- CPR status unknown across the board

This is a tax, liability, and scheduling risk. The fix is straightforward — it's just been manual and easy to let slip.

---

## Phase 1 — Stop the Bleeding (This Week)

**Goal:** Get contact info and kickstart document collection for all active guides.

| Action | Who | How | By When |
|---|---|---|---|
| Get Nick Napoda's email | Michelle | Ask him directly / check FareHarbor | Immediately |
| Fix ICA template errors | Owner review | See Legal folder — 5 key changes | Before any new ICA is sent |
| Confirm Alex Wallace = Ashe Burke? | Michelle | Quick check | This week |
| Confirm which guides are truly active 2026 | Michelle | Cross-check with schedule | This week |

---

## Phase 2 — Blast Collection (Week of March 31)

**Goal:** Send W-9 request, DL request, and ICA DocuSeal link to every active guide in one coordinated push.

**The sequence (can be done via GHL or manual text):**

**Day 1 — Text blast to all active guides:**
> "Hey [Name] — getting our 2026 files buttoned up before the season kicks off. Need 3 things from you: (1) a completed W-9, (2) a photo of your driver's license, (3) a signed contractor agreement — link coming separately. Takes about 10 minutes total. Reply with any questions."

**Day 1 — Follow-up email with:**
- W-9 download link (IRS PDF)
- DocuSeal ICA link (once template is fixed)
- Instructions for DL photo (reply to text or email)

**Day 4 — Follow-up text to non-responders:**
> "Hey [Name] — just following up on the W-9 / DL / agreement from earlier this week. Need these before your next shift. Let me know if you have any issues."

**Day 7 — Final nudge + flag to management:**
> Any guide who hasn't responded by Day 7 gets flagged — decision needed on whether to hold them from scheduling until compliant.

---

## Phase 3 — Build the Automation (GHL, with Chevy)

**Goal:** Never chase this paperwork manually again. Every new guide that gets added triggers a sequence automatically.

### Automation 1: New Guide Onboarding Flow
*Trigger: New guide contact added to GHL with tag "guide-new"*

1. **Immediately:** Send welcome text with their first shift details
2. **Hour 1:** Send email with ICA DocuSeal link + W-9 instructions + DL request
3. **Day 3:** If ICA not signed → reminder text
4. **Day 5:** If W-9 not received → reminder text
5. **Day 7:** If still incomplete → alert to Michelle (or owner) to hold from schedule

### Automation 2: Annual CPR Renewal Reminder
*Trigger: Date field "CPR Expiry" in guide contact record*

- **60 days before expiry:** Text — "Hey [Name], your CPR cert expires in 60 days. Here are some local options to renew: [link]"
- **30 days:** Text reminder
- **7 days:** Final notice + flag to management if not renewed

### Automation 3: Pre-Season Pulse (every February)
*Trigger: Recurring annual automation, fires Feb 1*

Send to all contacts tagged "guide-active":
> "Hey [Name] — season prep is starting! Quick check-in: Is your CPR cert still current? Any scheduling conflicts this spring/summer? Anything from last season you'd want us to do differently?"

### Automation 4: W-9 Annual Refresh
*Trigger: Recurring annual automation, fires January 1*

IRS requires a new W-9 when info changes. Good practice to refresh annually:
> "Hey [Name] — new year, new paperwork (sorry). Can you confirm your W-9 info is still current? If anything changed (address, SSN, business name), reply and we'll send a new form."

### Automation 5: Post-Tour Guide Check-In
*Trigger: Tour completed (from FareHarbor webhook, if connected to GHL)*

1 hour after tour end time:
> "How'd the tour go? Any wildlife sightings? Guest issues? Equipment concerns? Drop a quick note — even a voice memo."

---

## Phase 4 — Ongoing Pulse System

**Goal:** Keep a real communication loop with guides — not just compliance chasing. Good guides leave when they feel like a number.

**Monthly during season (May–October):**
> "Hey [Name] — how's the season going? Anything on your mind — guest feedback, gear issues, schedule needs? We want to hear it."

**End of season (November):**
Full debrief — what worked, what didn't, are they back next year. This is the best retention tool available.

**Annual review questions:**
1. What was your favorite tour / best wildlife sighting this season?
2. What's one thing we could do to make your job easier?
3. Any equipment issues we should address over the offseason?
4. Are you planning to be back next spring?
5. Any guests or moments that stood out?

---

## GHL Setup Requirements (Discuss with Chevy)

For the automations above to work, GHL needs:
- [ ] All guides imported as contacts with tag `guide-active` or `guide-new`
- [ ] Custom fields: `CPR Expiry Date`, `W9 on File (Y/N)`, `DL on File (Y/N)`, `ICA Signed (Y/N)`, `Solo Sign-Off Date`
- [ ] DocuSeal integrated (or Zapier webhook to trigger ICA send)
- [ ] FareHarbor webhook connected (for post-tour trigger — if possible)
- [ ] Onboarding workflow built and tested before sending

---

## What This Takes Off Michelle's Plate

| Task | Currently | After Automation |
|---|---|---|
| Chasing W-9s | Manual texts one by one | Auto-sequence, she just monitors |
| Sending ICA | Manual DocuSeal link send | Triggered on guide tag |
| CPR renewal tracking | Mental / spreadsheet | Automated reminder based on date field |
| Pre-season check-in | Forgotten or ad hoc | Fires every February automatically |
| Post-tour feedback | Rarely happens | Auto-text 1hr after every tour |
| Annual W-9 refresh | Never done | Fires every January |

**Net result:** Michelle goes from chasing paper to reviewing a dashboard. Her job becomes confirming things are done, not making them happen.

---

## Tomorrow's Walkthrough Agenda (March 31)

1. **Review the guide roster together** — confirm who's active, inactive, or on the fence
2. **Confirm Alex Wallace / Ashe Burke** — one name or two?
3. **Fix the ICA** — walk through the 5 key changes, sign off on revised template
4. **Draft the Phase 2 blast** — write the text/email together, schedule send
5. **Brief Chevy on Phase 3** — what needs to be built in GHL and timeline
6. **CPR status** — does Michelle know who's current? Can we get a quick verbal check?
7. **Nick Napoda's email** — make sure we leave with it

*Estimated time: 45–60 minutes*
