# NOLA Party Barge — Checklist Automation
*Google Forms + Apps Script | Setup once, runs forever*

---

## What This Does

- 5 mobile-friendly forms — one per shift phase
- All submissions log to a Google Sheet automatically
- You get **one daily summary email at 9 PM** with all completions
- Any USCG safety item flagged "No" → **you get an immediate email alert**
- End of day issues flagged → you get an immediate email alert
- You never look at the sheet unless something's wrong

---

## Setup — One Time Only (10 minutes)

**Step 1:** Go to [script.google.com](https://script.google.com) → click **New project**

**Step 2:** Delete all the code in the editor (select all, delete)

**Step 3:** Paste the entire script from the code block below

**Step 4:** On **line 9**, change `'YOUR_EMAIL_HERE'` to your email address

**Step 5:** Click the save icon (Ctrl+S or Cmd+S)

**Step 6:** In the function dropdown (top of page), select **`setupSystem`** → click **Run**

**Step 7:** Google will ask for permissions — click through and approve everything

**Step 8:** Check your email. You'll get a message with all 5 form links and the spreadsheet link.

**That's it.** Send each form link to the right crew members and have them add it to their phone home screen.

---

## The 5 Forms

| Form | Who Uses It | When |
|---|---|---|
| Arrival Checklist | All deckhands | Start of shift, before boat prep |
| Boat Prep & Safety | Captain + deckhand | After arrival, before guests |
| Pre-Departure | Deckhand | 5 min before each trip |
| Between Trips | Deckhand | Between each trip |
| End of Day Sign-Off | All crew | Before leaving |

---

## The Script

```javascript
/**
 * NOLA Party Barge — Operations Automation
 * Google Forms + Sheets + Apps Script
 *
 * SETUP: Run setupSystem() once. That's it.
 */

const CONFIG = {
  MANAGER_EMAIL: 'YOUR_EMAIL_HERE',        // ← UPDATE THIS (line 9)
  SPREADSHEET_NAME: 'NOLA Party Barge — Operations Log',
  DAILY_SUMMARY_HOUR: 21,                  // 9 PM — change if you want a different time
  BOATS: ['Freaky Tiki', 'Twerkin Tiki', 'Bayou Boogie', 'Party Queen'],
};

// ============================================================
// MAIN SETUP — RUN THIS ONCE
// ============================================================

function setupSystem() {
  const props = PropertiesService.getScriptProperties();

  // Create master spreadsheet
  const ss = SpreadsheetApp.create(CONFIG.SPREADSHEET_NAME);
  props.setProperty('SPREADSHEET_ID', ss.getId());

  // Create all 5 forms
  const forms = {
    'Arrival Checklist':    createArrivalForm(ss),
    'Boat Prep & Safety':   createBoatPrepForm(ss),
    'Pre-Departure':        createPreDepartureForm(ss),
    'Between Trips':        createBetweenTripsForm(ss),
    'End of Day Sign-Off':  createEndOfDayForm(ss),
  };

  // Store form URLs
  Object.entries(forms).forEach(([name, form]) => {
    props.setProperty('FORM_URL_' + name, form.getPublishedUrl());
  });

  // Set up daily 9 PM summary
  ScriptApp.newTrigger('sendDailySummary')
    .timeBased()
    .atHour(CONFIG.DAILY_SUMMARY_HOUR)
    .everyDays(1)
    .create();

  // Add a Links tab to the spreadsheet
  const linksSheet = ss.insertSheet('— Form Links —');
  linksSheet.getRange('A1:B1').setValues([['Form', 'Share This Link With Crew']]);
  linksSheet.getRange('A1:B1').setFontWeight('bold');
  Object.entries(forms).forEach(([name, form], i) => {
    linksSheet.getRange(i + 2, 1, 1, 2).setValues([[name, form.getPublishedUrl()]]);
  });
  linksSheet.autoResizeColumns(1, 2);

  // Email setup confirmation with all links
  const linkList = Object.entries(forms)
    .map(([name, form]) => `${name}:\n${form.getPublishedUrl()}`)
    .join('\n\n');

  MailApp.sendEmail(
    CONFIG.MANAGER_EMAIL,
    '✅ NOLA Party Barge — Checklist System Is Live',
    `Your operations system is set up and running.\n\n` +
    `Operations Log (Google Sheet):\n${ss.getUrl()}\n\n` +
    `FORM LINKS — Share with crew:\n\n${linkList}\n\n` +
    `You'll get a daily summary at 9 PM.\n` +
    `Any USCG safety flag or end-of-day issue will alert you immediately.`
  );

  Logger.log('Done. Check your email for links.');
}

// ============================================================
// FORM 1 — ARRIVAL CHECKLIST
// ============================================================

function createArrivalForm(ss) {
  const form = FormApp.create('NOLA Party Barge — Arrival Checklist');
  form.setDescription('Complete at the start of your shift, before boat prep.');
  form.setConfirmationMessage('Logged. Go get it done.');

  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addListItem().setTitle('Your boat').setChoiceValues(CONFIG.BOATS).setRequired(true);

  // Freaky Tiki
  form.addSectionHeaderItem()
    .setTitle('FREAKY TIKI')
    .setHelpText('Freaky Tiki crew only. All others skip to your boat.');
  form.addCheckboxItem()
    .setTitle('Freaky Tiki — mark all completed')
    .setChoiceValues([
      'Outdoor customer area set up (chairs, tables, cushions, shade sails)',
      'Customer restrooms inspected — clean and fully stocked',
    ]);

  // Twerkin Tiki
  form.addSectionHeaderItem().setTitle('TWERKIN TIKI');
  form.addCheckboxItem()
    .setTitle('Twerkin Tiki — mark all completed')
    .setChoiceValues([
      'Swept from roadside to property — all trash and debris cleared',
      'All trash cans emptied and relined',
      'Unsightly items removed and disposed in dumpster',
    ]);

  // Bayou Boogie
  form.addSectionHeaderItem().setTitle('BAYOU BOOGIE');
  form.addCheckboxItem()
    .setTitle('Bayou Boogie — mark all completed')
    .setChoiceValues([
      'Docks swept, cleaned, and scrubbed',
      'Assisted Freaky Tiki deckhand with customer area prep',
    ]);

  // Party Queen
  form.addSectionHeaderItem().setTitle('PARTY QUEEN');
  form.addCheckboxItem()
    .setTitle('Party Queen — mark all completed')
    .setChoiceValues([
      'Potted plants and trees inspected — dry ones watered',
      'Full property walk done — landscaping healthy and maintained',
      'Displaced materials raked and evened out',
    ]);

  // All crew
  form.addSectionHeaderItem().setTitle('ALL CREW');
  form.addMultipleChoiceItem()
    .setTitle('Customer area and restrooms — current status')
    .setChoiceValues(['All good ✓', 'Needs attention — see notes below'])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Notes or anything to flag');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  return form;
}

// ============================================================
// FORM 2 — BOAT PREP & SAFETY (alerts on USCG flags)
// ============================================================

function createBoatPrepForm(ss) {
  const form = FormApp.create('NOLA Party Barge — Boat Prep & Safety');
  form.setDescription('Complete after arrival duties. USCG items are required before every departure.');
  form.setConfirmationMessage('Logged. Any safety flags have been sent to the manager.');

  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addListItem().setTitle('Boat').setChoiceValues(CONFIG.BOATS).setRequired(true);

  // Boat prep items
  form.addSectionHeaderItem().setTitle('BOAT PREP');
  form.addCheckboxItem()
    .setTitle('Boat prep — check off everything completed')
    .setRequired(true)
    .setChoiceValues([
      '2 fully charged speakers loaded and tested',
      'Playlist ready and queued',
      'All surfaces wiped down thoroughly',
      'Spider webs cleared from railings, ceiling, seats',
      'Floors swept / turf raked',
      'Restroom cleaned (toilet, sink, floor)',
      'Toilet paper, soap, paper towels restocked',
      'Supplies loaded (garbage bags, spray, paper towels, water)',
      'Cooler drained and cleaned',
      'Inverter connected and operational',
    ]);

  // USCG Safety — captain required, any No triggers alert
  form.addSectionHeaderItem()
    .setTitle('USCG SAFETY CHECK')
    .setHelpText('Captain completes this section. Any "No" sends an immediate alert to the manager. Do not skip.');

  const safetyItems = [
    'Engine inspection complete (oil, fuel, bilge, battery)',
    'Navigation lights operational',
    'Life jackets counted — sufficient USCG Type I/II/III for max capacity',
    'Throwable PFD (Type IV) on deck and accessible',
    'Fire extinguisher charged and accessible',
    'Visual distress signals (flares) present and in-date',
    'Sound device (horn) functional',
    'First aid kit stocked',
    'VHF radio operational — tuned to Ch 16',
    'Vessel documentation / COI on board',
    "Captain's USCG license on person",
  ];

  safetyItems.forEach(title => {
    form.addMultipleChoiceItem()
      .setTitle(title)
      .setChoiceValues(['Yes ✓', 'No — flagging for manager'])
      .setRequired(true);
  });

  form.addParagraphTextItem()
    .setTitle('Safety notes — describe any flagged item here');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // Alert trigger
  ScriptApp.newTrigger('onBoatPrepSubmit')
    .forForm(form)
    .onFormSubmit()
    .create();

  return form;
}

// ============================================================
// FORM 3 — PRE-DEPARTURE
// ============================================================

function createPreDepartureForm(ss) {
  const form = FormApp.create('NOLA Party Barge — Pre-Departure');
  form.setDescription('Complete 5 minutes before each departure.');
  form.setConfirmationMessage('Logged. Have a great trip.');

  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addListItem().setTitle('Boat').setChoiceValues(CONFIG.BOATS).setRequired(true);
  form.addTextItem().setTitle('Scheduled departure time (e.g. 2:00 PM)').setRequired(true);

  form.addCheckboxItem()
    .setTitle('Pre-departure — confirm completed')
    .setRequired(true)
    .setChoiceValues([
      'Helped guests onboard with food and drinks (5 min before)',
      'Standing at boat entry to collect tickets (2 min before)',
      'Tickets counted and match FareHarbor manifest',
      'Tickets dropped in designated box for this boat',
    ]);

  form.addMultipleChoiceItem()
    .setTitle('Headcount matches manifest?')
    .setChoiceValues(['Yes ✓', 'No — discrepancy, noted below'])
    .setRequired(true);

  form.addTextItem().setTitle('Actual headcount on board');
  form.addParagraphTextItem().setTitle('Notes / issues');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  return form;
}

// ============================================================
// FORM 4 — BETWEEN TRIPS
// ============================================================

function createBetweenTripsForm(ss) {
  const form = FormApp.create('NOLA Party Barge — Between Trips');
  form.setDescription('Complete between each trip. Takes 2 minutes.');
  form.setConfirmationMessage('Logged.');

  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addListItem().setTitle('Boat').setChoiceValues(CONFIG.BOATS).setRequired(true);

  form.addCheckboxItem()
    .setTitle('Between trips — confirm completed')
    .setRequired(true)
    .setChoiceValues([
      'Trash run to dumpster',
      'Restroom checked and wiped down — paper cleared from bowl',
      'All surfaces wiped and cupholders cleared',
      'Next manifest checked on FareHarbor',
    ]);

  form.addMultipleChoiceItem()
    .setTitle('Restroom status')
    .setChoiceValues(['All good ✓', 'Needs attention — flagging'])
    .setRequired(true);

  form.addParagraphTextItem().setTitle('Notes');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  return form;
}

// ============================================================
// FORM 5 — END OF DAY SIGN-OFF (alerts on flags)
// ============================================================

function createEndOfDayForm(ss) {
  const form = FormApp.create('NOLA Party Barge — End of Day Sign-Off');
  form.setDescription('Complete before you leave. Every item required. This is your sign-off.');
  form.setConfirmationMessage('Signed off. See you tomorrow.');

  form.addTextItem().setTitle('Your name').setRequired(true);
  form.addListItem().setTitle('Boat').setChoiceValues(CONFIG.BOATS).setRequired(true);

  form.addCheckboxItem()
    .setTitle('End of day — check off EVERYTHING')
    .setRequired(true)
    .setChoiceValues([
      'All trash bagged and to dumpster',
      'Restroom clean — toilet clear, surfaces wiped, floor clean',
      'All surfaces wiped down and floor swept / vacuumed',
      'Seats removed and stowed neatly in restroom',
      'Cooler drained and wiped down',
      'Paper and cleaning products into weatherproof bin',
      'Inverter disconnected and stowed',
      'All non-essential items removed from boat',
      'Motors trimmed up and batteries turned off',
      'Dock lines double-checked',
      'Speakers to supply room and plugged in to charge',
      'Outdoor customer area and restrooms checked and clean',
    ]);

  form.addMultipleChoiceItem()
    .setTitle('Is the boat 100% ready for tomorrow?')
    .setChoiceValues(['Yes ✓', 'No — see notes below'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('How did today go?')
    .setChoiceValues([
      'Smooth — no issues',
      'Had some bumps but handled it',
      'Rough — manager needs to know',
    ]);

  form.addParagraphTextItem()
    .setTitle('Anything for the manager (incidents, maintenance, supply needs, guest issues, wins)');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  ScriptApp.newTrigger('onEndOfDaySubmit')
    .forForm(form)
    .onFormSubmit()
    .create();

  return form;
}

// ============================================================
// ALERT TRIGGERS
// ============================================================

function onBoatPrepSubmit(e) {
  const answers = e.response.getItemResponses();
  const flags = [];
  let crewName = '';
  let boat = '';

  answers.forEach(answer => {
    const title = answer.getItem().getTitle();
    const val = answer.getResponse();
    if (title === 'Your name') crewName = val;
    if (title === 'Boat') boat = val;
    if (typeof val === 'string' && val.includes('flagging')) {
      flags.push(`• ${title}`);
    }
  });

  if (flags.length > 0) {
    MailApp.sendEmail(
      CONFIG.MANAGER_EMAIL,
      `🚨 SAFETY FLAG — ${boat}`,
      `${crewName} flagged the following safety item(s) on ${boat}:\n\n${flags.join('\n')}\n\nTime: ${new Date().toLocaleString()}\n\nCheck the notes field in the operations log for details.`
    );
  }
}

function onEndOfDaySubmit(e) {
  const answers = e.response.getItemResponses();
  const flags = [];
  let crewName = '';
  let boat = '';

  answers.forEach(answer => {
    const title = answer.getItem().getTitle();
    const val = answer.getResponse();
    if (title === 'Your name') crewName = val;
    if (title === 'Boat') boat = val;
    if (typeof val === 'string' && (val.includes('No —') || val.includes('Rough'))) {
      flags.push(`• ${title}: ${val}`);
    }
    // If the notes field has content, include it
    if (title.includes('Anything for the manager') && typeof val === 'string' && val.trim().length > 0) {
      flags.push(`• Notes: ${val.trim()}`);
    }
  });

  if (flags.length > 0) {
    MailApp.sendEmail(
      CONFIG.MANAGER_EMAIL,
      `NOLA Party Barge — End of Day Flag (${boat})`,
      `${crewName} flagged something on ${boat} at end of day:\n\n${flags.join('\n')}\n\nTime: ${new Date().toLocaleString()}`
    );
  }
}

// ============================================================
// DAILY SUMMARY — runs at 9 PM
// ============================================================

function sendDailySummary() {
  const ssId = PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID');
  if (!ssId) return;

  const ss = SpreadsheetApp.openById(ssId);
  const today = new Date();
  const dateStr = Utilities.formatDate(today, Session.getScriptTimeZone(), 'yyyy-MM-dd');
  const displayDate = Utilities.formatDate(today, Session.getScriptTimeZone(), 'EEEE, MMMM d');

  let summary = `NOLA Party Barge — Daily Summary\n${displayDate}\n${'─'.repeat(40)}\n\n`;
  let totalSubmissions = 0;
  const boatCounts = {};

  ss.getSheets().forEach(sheet => {
    const name = sheet.getName();
    if (name.startsWith('—')) return; // skip links sheet

    const data = sheet.getDataRange().getValues();
    if (data.length <= 1) return;

    const headers = data[0];
    const boatCol = headers.findIndex(h => String(h).toLowerCase().includes('boat'));
    const nameCol = headers.findIndex(h => String(h).toLowerCase().includes('name'));

    const todayRows = data.slice(1).filter(row => {
      if (!row[0]) return false;
      const rowDate = Utilities.formatDate(new Date(row[0]), Session.getScriptTimeZone(), 'yyyy-MM-dd');
      return rowDate === dateStr;
    });

    if (todayRows.length > 0) {
      summary += `${name.replace(' (Form Responses 1)', '').replace(' (Form Responses)', '')}\n`;
      todayRows.forEach(row => {
        const who = nameCol >= 0 ? row[nameCol] : '?';
        const boat = boatCol >= 0 ? row[boatCol] : '?';
        summary += `  ✓ ${who} — ${boat}\n`;
        boatCounts[boat] = (boatCounts[boat] || 0) + 1;
      });
      summary += '\n';
      totalSubmissions += todayRows.length;
    }
  });

  if (totalSubmissions === 0) {
    summary += 'No checklist submissions recorded today.\n';
  }

  summary += `${'─'.repeat(40)}\nTotal submissions today: ${totalSubmissions}\n`;
  summary += `\nFull log: https://docs.google.com/spreadsheets/d/${ssId}`;

  MailApp.sendEmail(
    CONFIG.MANAGER_EMAIL,
    `NOLA Party Barge — ${displayDate} Summary`,
    summary
  );
}

// ============================================================
// UTILITY — re-send form links to yourself
// ============================================================

function resendFormLinks() {
  const props = PropertiesService.getScriptProperties().getProperties();
  const ssId = props['SPREADSHEET_ID'];
  const links = Object.entries(props)
    .filter(([k]) => k.startsWith('FORM_URL_'))
    .map(([k, v]) => `${k.replace('FORM_URL_', '')}:\n${v}`)
    .join('\n\n');

  MailApp.sendEmail(
    CONFIG.MANAGER_EMAIL,
    'NOLA Party Barge — Form Links',
    `Operations Log: https://docs.google.com/spreadsheets/d/${ssId}\n\n${links}`
  );
}
```

---

## After Setup — What to Tell Crew

Send each crew member their relevant form links. They should:
1. Open the link on their phone
2. Tap the share icon → **Add to Home Screen**
3. It acts like an app — one tap, done

**Which forms go to whom:**

| Role | Gets These Forms |
|---|---|
| All deckhands | Arrival, Pre-Departure, Between Trips, End of Day |
| Captain | Boat Prep & Safety (required), Pre-Departure, End of Day |

---

## Changing Anything Later

Tell me what you want changed and I'll update the script. To apply changes:
1. Open the script at [script.google.com](https://script.google.com)
2. Find your project
3. Paste the updated code
4. Run `setupSystem` again (it creates a fresh set of forms — old ones still exist)

Or for small changes (add/remove a checklist item), I can walk you through editing just the form directly in Google Forms — no code needed.

---

## If Something Breaks

Run `resendFormLinks()` from the script editor to get all your links re-emailed.

---

## Crew Onboarding Form (Add to Script)

Add this function to the same script. Then add `createCrewOnboardingForm(ss)` inside `setupSystem()` alongside the other 5 forms. It creates a 6th form — a one-time intake that every new crew member fills out before their first shift.

```javascript
// ============================================================
// FORM 6 — CREW ONBOARDING INTAKE (one-time per crew member)
// ============================================================

function createCrewOnboardingForm(ss) {
  const form = FormApp.create('NOLA Party Barge — Crew Onboarding');
  form.setDescription('Complete before your first shift. All fields are required. This information is kept confidential and used for scheduling, payments, and compliance only.');
  form.setConfirmationMessage('Submitted. Jeffrey will review and confirm your first shift once everything is verified.');

  // Identity
  form.addSectionHeaderItem().setTitle('PERSONAL INFORMATION');
  form.addTextItem().setTitle('Full legal name').setRequired(true);
  form.addListItem().setTitle('Role').setChoiceValues(['Captain / Operator', 'Deckhand']).setRequired(true);
  form.addTextItem().setTitle('Cell phone number').setRequired(true);
  form.addTextItem().setTitle('Email address').setRequired(true);
  form.addParagraphTextItem().setTitle('Home address (street, city, state, zip)').setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('What phone do you have?')
    .setChoiceValues(['iPhone', 'Android', 'Other'])
    .setRequired(true);

  // Emergency contact
  form.addSectionHeaderItem().setTitle('EMERGENCY CONTACT');
  form.addTextItem().setTitle('Emergency contact name').setRequired(true);
  form.addTextItem().setTitle('Emergency contact phone').setRequired(true);
  form.addTextItem().setTitle('Relationship to you').setRequired(true);

  // Payment
  form.addSectionHeaderItem().setTitle('PAYMENT INFORMATION');
  form.addMultipleChoiceItem()
    .setTitle('Preferred payment method')
    .setChoiceValues(['Venmo', 'Zelle', 'Cash App', 'Direct deposit (ACH)', 'Check'])
    .setRequired(true);
  form.addTextItem().setTitle('Payment handle / account (e.g. @yourvenmo or bank info for ACH)').setRequired(true);

  // Documents — Captain only
  form.addSectionHeaderItem()
    .setTitle('CAPTAIN / OPERATOR CREDENTIALS')
    .setHelpText('Captains only. Deckhands skip this section.');
  form.addTextItem().setTitle('USCG License number');
  form.addTextItem().setTitle('USCG License type (e.g. OUPV 6-pak, 25-ton, 50-ton, 100-ton)');
  form.addDateItem().setTitle('USCG License expiration date');
  form.addTextItem().setTitle('TWIC Card number');
  form.addDateItem().setTitle('TWIC Card expiration date');
  form.addTextItem().setTitle('Maritime Consortium enrollment / member number');
  form.addDateItem().setTitle('Most recent drug test date');
  form.addMultipleChoiceItem()
    .setTitle('Drug test result')
    .setChoiceValues(['Negative (pass)', 'Pending']);
  form.addDateItem().setTitle('CPR / First Aid certification expiration date');

  // Agreements
  form.addSectionHeaderItem().setTitle('ACKNOWLEDGMENTS');
  form.addMultipleChoiceItem()
    .setTitle('I have submitted or will submit my W-9 before my first shift')
    .setChoiceValues(['Yes', 'I need a W-9 form — please send me one'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('I understand I am an independent contractor, not an employee')
    .setChoiceValues(['Yes, I understand'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('I have read the Crew & Captain Performance Guide')
    .setChoiceValues(['Yes', 'No — I need it sent to me'])
    .setRequired(true);

  form.addParagraphTextItem().setTitle('Anything else Jeffrey should know before your first shift');

  // Alert Jeffrey on every submission
  ScriptApp.newTrigger('onCrewOnboardingSubmit')
    .forForm(form)
    .onFormSubmit()
    .create();

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  return form;
}

function onCrewOnboardingSubmit(e) {
  const answers = e.response.getItemResponses();
  let name = '', role = '', phone = '', email = '', notes = [];

  answers.forEach(answer => {
    const title = answer.getItem().getTitle();
    const val = answer.getResponse();
    if (title === 'Full legal name') name = val;
    if (title === 'Role') role = val;
    if (title === 'Cell phone number') phone = val;
    if (title === 'Email address') email = val;
    if (val && String(val).includes('need')) notes.push(`• ${title}: ${val}`);
  });

  MailApp.sendEmail(
    CONFIG.MANAGER_EMAIL,
    `New Crew Onboarding — ${name} (${role})`,
    `${name} just completed their onboarding intake.\n\n` +
    `Role: ${role}\nPhone: ${phone}\nEmail: ${email}\n\n` +
    (notes.length > 0 ? `Action needed:\n${notes.join('\n')}\n\n` : '') +
    `Review their full submission in the Operations Log and verify all documents before scheduling their first shift.`
  );
}
```
