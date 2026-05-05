# Crew Intake Form — Google Forms Setup
*Built 2026-05-05 to fill all credential gaps in one pass instead of chasing per field*

> **What this is:** A single intake form Jeffrey sends to all 14 crew members at once. Each person fills it out themselves, attachments included. Replaces ~150 separate texts with one link.

---

## How to Set This Up (10 minutes)

1. Go to forms.google.com and click "Blank form"
2. Title: **NPB Crew Onboarding Intake**
3. Description: *"This is the one form we need from everyone on the crew. Takes about 10 minutes. Once it's in, you're set, no more texts asking for stuff. Captains have a few extra fields at the end. Questions, ping Jeffrey."*
4. Settings tab: turn on "Collect email addresses," "Limit to 1 response," "Require sign-in"
5. Linked Sheet: connect to a Google Sheet called **NPB Crew Intake Responses**
6. Paste the questions below (in order, with the indicated field types)
7. After build, test with your own email, then send to crew via the message at the bottom

---

## Form Questions (Paste Into Google Forms)

### Section 1: Basics

**1. Full legal name (as it appears on your ID)** — Short answer, required
**2. Preferred name / what we should call you** — Short answer, required
**3. Date of birth** — Date, required
**4. Phone number** — Short answer, required
**5. Email** — Short answer, required (auto-filled if you require sign-in)
**6. Mailing address (street, city, state, ZIP)** — Paragraph, required
**7. iPhone or Android?** — Multiple choice (iPhone / Android), required
*Used for setting up Slack, Tidebot, and form shortcuts on your phone.*

### Section 2: Emergency Contact

**8. Emergency contact full name** — Short answer, required
**9. Emergency contact phone** — Short answer, required
**10. Emergency contact relationship** — Short answer (spouse, parent, friend, etc.), required

### Section 3: Payment

**11. Preferred payment method** — Multiple choice (Venmo / Zelle / Cash App / Direct deposit/ACH), required
**12. Payment handle or account info**
- For Venmo/Zelle/Cash App: your handle or phone/email
- For ACH: bank name, routing #, account #
— Short answer, required

### Section 4: Identification & Background

**13. Photo ID upload (driver's license or passport, both sides if DL)** — File upload, required
**14. I authorize NOLA Party Barge to run a background check as part of onboarding** — Multiple choice (Yes / No), required
*Required for all crew. We use [provider name TBD] and the check runs once. You'll get a copy of the result.*

### Section 5: Role

**15. Your role at NPB** — Multiple choice, required
- Captain (full time)
- Captain (part time)
- Deckhand (full time)
- Deckhand (part time)
- Reception / Check-ins
- Hybrid (deckhand + reception)
- Operations / Project Manager
**16. Your typical availability** — Checkboxes (Mon, Tue, Wed, Thu, Fri, Sat, Sun, Varies week to week), required
**17. Anything we should know about your schedule?** (vacations, second job, school, etc.) — Paragraph, optional

### Section 6: Captain-Only (Show only if Q15 = Captain FT or Captain PT)

**18. USCG Captain's License number** — Short answer, required
**19. License grade** — Multiple choice (OUPV / 6-pak, 25-Ton Master, 50-Ton Master, 100-Ton Master, Other), required
**20. License expiration date** — Date, required
**21. Upload USCG License (front and back)** — File upload, required
**22. TWIC Card number** — Short answer, required
**23. TWIC expiration date** — Date, required
**24. Upload TWIC Card** — File upload, required
**25. CPR / First Aid certification expiration date** — Date, required
**26. Upload CPR / First Aid cert** — File upload, required
**27. Maritime Consortium enrollment** — Multiple choice (Currently enrolled / Not enrolled / Not sure), required
**28. If enrolled, upload your enrollment confirmation** — File upload, optional
**29. Date of your most recent USCG-compliant drug test** — Date, required
**30. Drug test result** — Multiple choice (Negative / Other), required

### Section 7: Acknowledgements

**31. I have received the Independent Contractor Agreement (ICA) link separately and will sign it via DocuSeal** — Checkbox, required
**32. I have read or will read the Crew & Captain Performance Guide before my next shift** — Checkbox, required
**33. I understand that I'm classified as a 1099 independent contractor and am responsible for my own taxes** — Checkbox, required
**34. Anything else we should know?** — Paragraph, optional

---

## Jeffrey's Send Message (Text + Email)

> **Subject (email):** Quick crew intake form, 10 min, please knock out by Sunday

> Hey, doing some long-overdue cleanup on our crew records. We're missing addresses, emergency contacts, W-9s, and signed ICAs for most of you. Instead of chasing everyone for individual stuff, I built one form. Takes about 10 minutes, you upload your ID and any captain credentials right inside it.
>
> Link: [paste Google Form link]
>
> Please get this in by **Sunday May 11**. Anyone who doesn't have it in by then comes off the schedule the following week, until it's done. This is so we're all clean with USCG and the IRS, not me being a hardass.
>
> One more thing: a separate DocuSeal email is going out for the Independent Contractor Agreement. Sign that too.
>
> Questions, hit me up.
>
> Thanks,
> Jeffrey

---

## After Responses Come In

The Google Sheet auto-populates. Workflow per response:

1. Open the sheet, find the new row
2. Update `Crew Roster & Credentials Tracker.md` for that person:
   - Flip ❌ to ✅ for each field that's now filled
   - Save uploaded files to Drive folder `NPB Crew Records / [Last Name First Name] /`
3. If captain: log USCG license expiration, TWIC expiration, CPR expiration, drug test date in the Expiration Alerts table
4. Send DocuSeal ICA link if not already sent
5. Order background check via [provider]
6. Once W-9 + ICA + background = ✅, mark Status = "Cleared to schedule" in the master roster

> **Tip:** Add a calendar reminder to review the sheet every Monday morning. Anyone still incomplete gets one nudge that week.
