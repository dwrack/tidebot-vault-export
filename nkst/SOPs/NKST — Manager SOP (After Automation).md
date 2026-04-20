# NKST — Manager SOP (After Automation)

**Company:** Apres Assets LLC dba New Orleans Kayak Swamp Tours / Nola Kayak Tours
**Version:** Automated Operations Playbook (GHL Live)
**Last Updated:** March 2026

> This document describes how to manage NKST operations after GoHighLevel (GHL) automation is fully live. Your job is no longer to execute routine tasks — it's to oversee systems, catch exceptions, and handle the things automation cannot. Read this carefully: the manual SOP habits will slow you down here. Trust the system. Watch the dashboards. Act on exceptions.

---

## Before vs. After — Where Your Time Goes

| Task | Before (Manual) | After (Automated) |
|---|---|---|
| Booking confirmation to guest | Manager or FareHarbor only | GHL webhook sends instantly on booking |
| What-to-bring info to guest | Manual text or email | GHL pre-tour sequence (message 2 of 4) |
| Day-before reminder to guest | Manual text or email | GHL pre-tour sequence (message 3 of 4) |
| Post-tour review request to guest | Manual text/email (or not done) | GHL sends automatically after tour |
| Missed call follow-up | No follow-up until voicemail checked | Auto SMS text-back within seconds |
| FAQ responses (website/SMS) | Manager or owner answers every one | Chatbot handles ~80% without human |
| Guide manifest + night-before SMS | Manager texts each guide manually | GHL sends automatically night before tour |
| Guide schedule confirmation | Manual text exchange | Guide gets auto-confirmation from GHL |
| Weather cancellation blast | Manager calls/texts every guest manually | One-click broadcast in GHL to all affected |
| Group inquiry capture | Ad hoc — email, call, lost in shuffle | GHL form → auto CRM entry → auto follow-up |
| Review requests | Manual or skipped | Auto-SMS with direct Google/TripAdvisor links |
| Guide compliance tracking | Spreadsheet | GHL compliance dashboard with expiry alerts |
| Monthly email campaigns | Owner or not done | GHL scheduled campaigns |
| LDWF quarterly report | Manual data pull | FareHarbor CSV → manager formats + submits |
| Add-transport requests | Manager handles manually | Chatbot captures name/date/headcount → flags manager to process in FareHarbor |
| "Didn't get confirmation" requests | Manager looks up booking and resends | Chatbot collects info → triggers FareHarbor confirmation resend |
| Day-of lost guest | Manager or guide handles by phone | Chatbot sends location info immediately + escalates to human |
| Weight/size questions | Manager or guide answers by phone | Chatbot answers directly from FAQ |
| Post-tour review request | Fully manual or skipped | Fully automated |
| **Manager's primary job** | **Doing tasks** | **Overseeing systems + handling exceptions** |

---

## What Automation Handles (Do NOT Do These Manually)

The following tasks are fully automated. You do not need to touch them unless the automation fails:

- Booking confirmation SMS/email to guest (triggered by FareHarbor → GHL webhook)
- Pre-tour message sequence: what to bring (2 days out), day-before reminder, post-tour review request
- Missed call text-back (instant SMS response to any missed call on company number)
- FAQ chatbot responses via website widget and SMS
- Night-before guide SMS with manifest + checklist
- Guide schedule confirmation (triggered when guide is assigned in FareHarbor)
- Monthly email campaigns (pre-scheduled in GHL)
- New group inquiry: auto-CRM entry, auto-quote, and initial follow-up sequence
- Post-tour review SMS with direct Google and TripAdvisor links
- Add-transport requests: chatbot captures guest name, date, headcount and flags for manager
- "Didn't get confirmation" requests: chatbot collects info and triggers resend workflow
- Day-of lost guest initial response: chatbot sends 740 N. Rampart address and escalation alert
- Weight/size FAQ questions: chatbot answers from FAQ (400 lb tandem limit)

**Your job with these automations is not to run them. Your job is to verify they ran and fix them when they don't.**

---

## Address Migration Watch

Monitor incoming texts for any guest referencing **"405 Frenchmen"**, **"Frenchman Street"**, or variations. These guests have outdated information — they need immediate correction before they show up at the wrong location.

The chatbot has an address correction branch trained on these keywords. But monitor the inbox manually as well, especially during high-volume days. If you see a guest referencing the old address and the chatbot hasn't responded yet — correct them directly and immediately.

Any references to the old address in GHL chat logs should be flagged: if it happens 3+ times in a week from different guests, there is a source (website, third-party listing, old confirmation email) still distributing the old address. Investigate and fix the source.

---

## New Daily Routine

**Target: 45–60 minutes of daily oversight, not all-day task execution.**

### Morning Check (Complete by 8:30 AM on tour days; 9:30 AM on non-tour days)

1. [ ] Open GHL — check the **Conversations inbox** first
   - Look for any conversations tagged or flagged as "Bot Escalation" or "Needs Human"
   - These are inquiries the chatbot could not resolve — respond to them now
   - Check for any replies from guests to automated sequences that need a real answer
   - Look for any guide replies to automated manifests that indicate a problem (unavailable, confused, wrong info)
   - **Look specifically for any day-of "can't find us" escalations** — these are urgent and time-sensitive

2. [ ] Open GHL — check **Workflow Activity / Failed Workflows**
   - Look for any red or failed workflow runs from the past 24 hours
   - Common failures: FareHarbor webhook didn't fire, phone number missing on a booking, guide phone not in system
   - For each failure: identify what didn't send, fix the underlying data issue, manually send if needed, log the failure

3. [ ] Open FareHarbor — review today's bookings (this part stays manual)
   - Confirm tour count, guide assignments, guest counts
   - **Verify third-party bookings (Viator, Expedia, TripAdvisor) still show shuttle on manifest** — automation does not catch missing shuttle flags
   - Confirm GHL sent the night-before guide SMS (check workflow log for yesterday's trigger) — if it failed, text the guide now
   - If any Honey Island tours are running: check gauge at wx.aerisweather.com/rivers/gauge/PERL1.html (this check is never automated — always do it manually)

4. [ ] Check the company phone (504-571-9975) for:
   - Any missed calls that the auto-text-back sent to — did any of those leads text back asking for a human?
   - Any voicemails from guests or guides that need a real response
   - Escalations from the chatbot that came in overnight

5. [ ] Check email inbox — automation handles most customer touchpoints, but some guests still email
   - Respond to anything that came in overnight
   - Group inquiry emails: move into GHL CRM if not already captured; trigger group inquiry workflow or handle manually

---

## GHL-Specific Manager Tasks

### Conversations Inbox Monitoring
- Check the inbox at least three times per day: morning, midday, afternoon
- When the chatbot escalates a conversation, it will tag it or assign it to you. Do not ignore these.
- After resolving a bot escalation, note what question stumped the bot — add it to the chatbot FAQ update list for weekly review
- Rule: if the same question escalates three times in a week, update the chatbot response for it

### Responding to Bot Escalations
1. When you pick up an escalated conversation: read the full thread first — the guest may have already gotten partial info from the bot
2. Don't repeat what the bot said — move the conversation forward
3. If it's a booking question: resolve it and provide the direct booking link or book for them in FareHarbor
4. If it's a complaint: follow the complaint protocol (see Escalation Matrix below)
5. After handling: mark conversation as resolved in GHL

### Workflow Failure Protocol
1. Navigate to GHL > Automation > Workflows > Activity Log
2. Filter for failures in the past 24–48 hours
3. For each failure, identify:
   - Which workflow failed?
   - At which step?
   - What data was missing or incorrect?
4. Fix the source data (usually in FareHarbor: missing phone, wrong guide assigned, webhook misfire)
5. Manually re-trigger the workflow or send the message manually if the window has passed
6. Log the failure and fix in your weekly system health note

### Chatbot Accuracy Review (Weekly Task — see Weekly section)

---

## Booking Oversight

The automation handles guest messaging. You own data integrity.

1. **Daily FareHarbor + GHL sync audit:**
   - Open GHL > Contacts or Pipeline — do new bookings from the past 24 hours appear as contacts?
   - If a booking is in FareHarbor but not in GHL, the webhook likely failed — add the contact manually and trigger the confirmation workflow
   - Confirm the pre-tour sequence is active for each new booking (check the contact's active workflows in GHL)

2. **Third-party booking verification (daily):**
   - Pull FareHarbor manifest for any Viator, Expedia, or TripAdvisor bookings
   - Confirm shuttle is listed — automation does not catch this; you must catch it manually
   - Alert the guide if shuttle logistics need to be confirmed

3. **Cancellation handling:**
   - FareHarbor processes the refund per policy
   - GHL should suppress remaining pre-tour messages when a booking is cancelled — verify this happened by checking the contact's active workflows
   - If messages were already sent and guest cancels: no action needed unless guest replies to a pre-tour message confused about their cancellation — handle those manually

---

## Minimum Participation Automation

The following workflow handles minimum participation cancellations for extended tours:

### How It Works
- GHL workflow runs a daily check at **4:00 PM** — flags any extended tour scheduled for tomorrow that has fewer than [MINIMUM — owner to set] confirmed bookings
- Manager receives an alert in GHL (and by SMS) at **4:30 PM** if minimum not met
- Manager makes the go/cancel decision and selects the appropriate action in GHL
- One-click sends the minimum participation outbound text to all affected guests
- System presents guests with 3 reply options (switch, reschedule, refund)
- Guest reply routes to:
  - Option 1 (switch): Workflow flags manager to update booking in FareHarbor; partial refund processed
  - Option 2 (reschedule): Workflow flags manager with guest preference; manager books new date
  - Option 3 (refund): Workflow flags manager to process full refund in FareHarbor

### Manager's Role in This Workflow
- Make the go/cancel decision by 5:00 PM
- Monitor guest reply inbox from 6:00 PM onward
- Process all FareHarbor actions (switches, refunds) by end of evening
- Call any guest who has not replied by 8:00 PM

**Owner must set the minimum participant threshold** for each tour type before this workflow can be fully configured. Until that number is set, the 4:30 PM alert will still fire — manager makes the judgment call manually.

---

## Guide Management

### Normal State (Automation Running)
- Guides receive auto-confirmation when assigned in FareHarbor
- Guides receive night-before SMS with manifest + checklist via GHL
- You do not need to manually text each guide for routine confirmation

Your job in normal state:
1. [ ] Verify in GHL workflow logs that night-before guide SMS fired for tomorrow's tours (check each evening around 7:00 PM)
2. [ ] Monitor for guide replies to automated messages — if a guide replies "I can't make it" or "wrong info," that's your escalation
3. [ ] Check GHL compliance dashboard weekly (not daily) — see Weekly Tasks

### Guide Exceptions (These Always Require Human Response)
- **Sick call / no-show:** Automation cannot fix this. Follow the same no-show protocol as the manual SOP — call backup guides, notify owner, contact guests if needed.
- **Last-minute swap:** You update the guide assignment in FareHarbor. GHL should send the new guide their manifest automatically — verify it fired.
- **New guide onboarding:** Run them through the manual compliance checklist (W-9, ICA via DocuSeal, CPR cert, DL). Add them to GHL with the correct tags so they receive guide workflows. Do not assign them to tours until compliance is complete.
- **Guide performance issue:** Document and escalate to owner. Automation does not handle performance management.

---

## Weather Protocol

Automation helps you notify guests, but the go/no-go decision is always yours.

1. **You make the weather decision by 6:30 AM** on any day tours are running.
2. Decision criteria: same as manual SOP (lightning, 25+ mph winds, Honey Island gauge out of range).
3. **If cancelling or rerouting:**
   - In GHL, go to the affected tour's contact list or tag group
   - Use the **Broadcast** or **Bulk SMS** function to send a cancellation message to all guests at once — one action instead of calling each person individually
   - Message template: *"NKST Update: Due to [weather/water conditions], today's [tour name] at [time] has been [cancelled / moved to Manchac Swamp]. We'll reschedule you or provide a full refund — reply here or call 504-571-9975."*
   - Send broadcast, then monitor replies — guests who reply are routed to your inbox
4. **Notify guides immediately after the guest broadcast** — text them directly (this is not automated).
5. Process refunds and reschedules in FareHarbor for guests who respond.
6. Document the cancellation event: date, tours affected, number of guests notified, time of broadcast.

---

## Hurricane / Named Storm Protocol

This protocol is distinct from regular weather cancellation. Named storm events require action on all upcoming bookings, not just same-day tours. Automation assists with notification volume, but all key decisions require human authorization.

**Monitor:** nhc.noaa.gov during hurricane season (June 1 – November 30).

### Activation Threshold
Activate when a named storm watch or warning is issued within 200 miles of the New Orleans metro area, OR when the NHC 72-hour forecast cone includes the region.

### Steps
1. **Notify owner immediately.** This is an owner-level decision.
2. In GHL, identify all contacts with upcoming bookings in the affected date range (next 72 hours minimum).
3. Use GHL **Broadcast / Bulk SMS** to send the hurricane cancellation message to all affected guests in one action:
   > Hi [NAME], this is [MANAGER NAME] from NolaKayak Tours. Due to [STORM NAME], we are proactively cancelling all tours [DATE RANGE] for the safety of our guests and guides. You will receive a full refund automatically — no action needed on your part. We'll be in touch to reschedule when we reopen. Please stay safe!
4. Process full refunds in FareHarbor for all affected bookings. Do not wait for guests to request them.
5. Block out dates in FareHarbor availability to prevent new bookings during the closure.
6. Update Google Business Profile status.
7. Post on social media that tours are suspended due to the named storm.
8. Document: dates cancelled, number of guests notified, total refunds processed, time of notifications.
9. **Reopen only with owner approval** after the storm passes and the launch site is inspected.

---

## Review Management

Automation sends the post-tour review request. Your job is to manage what comes back.

### Incoming Review Monitoring
1. Check Google Business, TripAdvisor, and Viator reviews at least 3x per week
2. Respond to every review within 48 hours:
   - **5-star:** Thank them warmly, personalize if you can (mention the tour), invite them back or to refer a friend
   - **4-star:** Same as 5-star; if they mentioned something specific that could be better, acknowledge it briefly
   - **3-star or below:** See below

### Responding to Negative Reviews
1. Do not respond emotionally or defensively — ever
2. Acknowledge their experience: *"We're sorry to hear this didn't meet your expectations."*
3. Offer to make it right: *"We'd love the opportunity to discuss this further — please reach out to us directly at 504-571-9975."*
4. Take the conversation offline — do not resolve complaints publicly in review threads
5. If the review describes a safety incident or makes a factual claim that could expose legal liability: do not respond until you've notified the owner and gotten guidance
6. After the offline conversation resolves the issue: if appropriate, politely follow up with the reviewer and ask if they'd be willing to update their review

---

## Group & Private Bookings

Group inquiries still require a human. Automation captures the lead — you convert it.

1. **Lead capture:** A group inquiry form on the website feeds directly into GHL CRM. You'll see a new contact appear in the "Group Leads" pipeline.
2. GHL sends an automated initial response and quote based on form inputs. This buys you time but does not close the booking.
3. **Your job:** Within 2 hours of a group lead appearing, call the contact.
   - Automation warmed them up — now you close
   - Confirm: group size, date, tour preference, shuttle, any occasion (birthday, bachelorette, corporate)
   - Provide custom quote if their group size or needs fall outside the automated response
   - If they want a private tour: escalate pricing discussion to owner
4. Once group confirms: create the booking in FareHarbor manually
5. GHL will pick up the booking via webhook and run the normal pre-tour sequence
6. Log the group in GHL pipeline — update their stage as the booking progresses

---

## Weekly Tasks

These are shorter now because automation handles the volume. Focus on system health and exceptions.

### Monday Morning System Check (30–45 minutes)
1. [ ] Review GHL workflow activity log for the past 7 days — note any failures
2. [ ] Review chatbot conversation logs — identify any questions the bot answered incorrectly or escalated unnecessarily
3. [ ] Check for any inbound references to "405 Frenchmen" or old address — investigate the source if multiple instances appear
4. [ ] Compile chatbot update list: questions to add, answers to revise
5. [ ] Update chatbot FAQ in GHL if you have 3+ items (if 1–2 items, batch them for the next week)

### Booking Audit (Mid-week)
1. [ ] Open FareHarbor — review all bookings for the next 14 days
2. [ ] Verify guide assignments and shuttle flags (especially third-party bookings)
3. [ ] Confirm GHL pre-tour sequences are active for all upcoming bookings
4. [ ] Check for any group or private bookings in the pipeline that need follow-up
5. [ ] **Check extended tour participant counts** for the next 7 days — flag any that are close to minimum threshold so you're not surprised at 4pm

### Review Responses
1. [ ] Check Google, TripAdvisor, Viator — respond to any reviews not yet addressed
2. [ ] Log review count and star rating trend for monthly owner summary

### Guide Compliance Dashboard
1. [ ] Open GHL compliance dashboard
2. [ ] Review expiry alerts: CPR certs, driver's licenses, Louisiana guiding permits
3. [ ] For any expiry within 60 days: contact guide directly and request updated documentation
4. [ ] Do not assign out-of-compliance guides to tours

### Payroll Prep
1. [ ] Tally tours by guide for the pay period (FareHarbor bookings CSV)
2. [ ] Prepare payment summary for owner
3. [ ] Owner approves — payments sent via PayPal on schedule

---

## Monthly Tasks

### System Health Review (First week of each month)
1. [ ] Pull GHL workflow success/failure report for the past 30 days
2. [ ] Calculate automation delivery rate: what % of pre-tour sequences completed without failure?
3. [ ] Identify the top 3 recurring failure types and address the root cause
4. [ ] Review chatbot performance: How many conversations handled by bot vs. escalated? What's the escalation rate? Target: under 20%
5. [ ] Test key workflows manually: book a test reservation (or use a sandbox) and verify the full sequence fires correctly
6. [ ] Report system health summary to owner

### GHL Contact List Audit (Monthly)
1. [ ] Check for duplicate contacts and merge them
2. [ ] Remove or archive contacts who are opted out or invalid
3. [ ] Confirm all active guides are tagged correctly and receiving the right automations
4. [ ] Confirm new leads from the past month are in the correct pipeline stages

### Monthly Email Campaign Review
1. [ ] Review the scheduled email campaign for next month in GHL — does it need any content updates?
2. [ ] Check open rate and click rate from the previous month's campaign
3. [ ] If open rate is below 20%: flag to owner; consider subject line or send-time adjustment
4. [ ] Forward performance data to owner in monthly summary

### Owner Monthly Summary
Send owner a brief report covering:
- Tours run, overall volume
- Automation health (delivery rate, failures fixed)
- Review trend (new reviews, rating average)
- Guide compliance status
- Any incidents or escalated complaints
- Items needing owner's decision

---

## Quarterly Tasks

### LDWF Eco-Tour Special Use Permit Report
1. [ ] Export FareHarbor bookings CSV for the quarter (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec)
2. [ ] Compile required reporting data: tour dates, types, guest counts, guide names, launch locations
3. [ ] Format per LDWF requirements
4. [ ] Submit to LDWF before the quarterly deadline
5. [ ] Save submitted report to the Legal folder
6. [ ] Notify owner of submission

### Seasonal Campaign Review (with Owner)
1. [ ] Review GHL scheduled campaigns for the upcoming season
2. [ ] Update content for seasonal relevance (spring, fall, holiday, local events)
3. [ ] Confirm automation trigger timing is appropriate for the tour schedule

### GHL Full Audit
1. [ ] Review all active workflows — are any outdated or no longer needed?
2. [ ] Confirm all FareHarbor → GHL webhooks are functioning correctly
3. [ ] Test guide compliance dashboard alerts
4. [ ] Review and update chatbot FAQ for any seasonal or product changes (pricing, new tours, hours)
5. [ ] Audit chatbot address references — confirm no references to old 405 Frenchmen St. remain

---

## Escalation Matrix

### Manager Handles Independently
- All chatbot escalations and FAQ questions
- Booking modifications, cancellations, reschedules (within policy)
- Negative reviews (follow-up protocol above)
- Guide no-shows and last-minute swaps (find replacement + execute)
- Weather go/no-go decision and broadcast
- Routine compliance tracking and guide reminders
- Equipment inventory and minor supply orders
- Workflow failures (fix and re-trigger)
- Group inquiry follow-up and conversion (non-custom pricing)
- Minimum participation decisions and guest notification
- Tour switch decisions (Manchac ↔ Honey Island due to water levels or participation)

### Escalate to Owner
- Any refund outside standard cancellation policy
- Guide termination or disciplinary action
- Any guest injury or on-water emergency
- Legal threat, chargeback dispute, or liability claim
- Pricing changes or new product creation
- Capital expenditures
- LDWF permit questions beyond routine reporting
- Custom group pricing (private tours, large groups)
- Negative reviews describing safety incidents or legal claims
- Any situation where automation has a systemic failure (entire workflow broken, not just one record)
- Media inquiries
- Hurricane / named storm protocol activation
- **Age policy exceptions** for children under 8 (pending owner's decision on formal policy)
- **Military discount requests** (pending owner's decision on formal policy)
- Any situation where the cost of a wrong decision is high and you're uncertain

**When escalating to owner:** State (1) what happened, (2) what you've already done, (3) what you need from them. Do not just say "there's a problem."

---

## Operating Mindset: You Are the Operator of a System

In the manual SOP world, a missed task meant a missed guest or a frustrated guide. In the automated world, a missed task usually means a broken loop that's silently failing at scale — pre-tour messages not sending, reviews not being requested, guide manifests going out with wrong info.

Your highest-value work now is:
1. **Watching the dashboard for what should have happened but didn't**
2. **Catching the 20% of inquiries the bot can't handle and converting them**
3. **Making the weather and safety decisions that no automation can make**
4. **Building relationships with guides that keep retention high**
5. **Being the human in the loop that guests talk to when they're confused, upset, or excited to book a large group**

The system runs the routine. You run the exceptions — and you improve the system over time.
