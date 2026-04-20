# DCKT — System Access Setup Guide
*Exact steps to connect each system. Do these in order.*

---

## Status Summary

| System | Status | Who Does It | Est. Time |
|---|---|---|---|
| Gmail (dwrack81) | ✅ Done | — | — |
| GHL — DCKT location | ❌ Need location ID + PIT | David | 5 min |
| Google Drive API | ❌ Need to enable | David | 2 min |
| DCKT Gmail (Info@) | ❌ Need to add account | David | 5 min |
| FareHarbor API | ❌ Need API key | David | 10 min |
| n8n workflow export | ❌ Need JSON | David | 3 min |
| Homebase API | ❌ Need API key | Bella | 5 min |

---

## Step 1 — GHL: Get DCKT Location ID + PIT Token
**Priority: Highest. Unlocks the entire automation stack.**

GHL MCP is already set up for other businesses. DCKT just needs its own key added.

### Get Location ID
1. Log into GHL → switch to DCKT sub-account
2. Go to **Settings → Business Profile**
3. Copy the **Location ID** (looks like: `xxxxxxxxxxxxxxxxxxx`)

### Create PIT Token
1. In DCKT sub-account → **Settings → Private Integrations**
2. Click **+ Create New Integration**
3. Name it: `Claude Code`
4. Select all scopes (or at minimum: Contacts, Conversations, Workflows, Calendars, Opportunities)
5. Copy the token

### Add to Claude
Run this in terminal (replace with real values):
```bash
# Open ~/.claude.json and add under mcpServers.ghl.env:
# "GHL_LOCATION_ID": "YOUR_DCKT_LOCATION_ID",
# "GHL_KEY_YOUR_DCKT_LOCATION_ID": "YOUR_DCKT_PIT_TOKEN"
```
Or just share the Location ID and PIT token here and I'll add them.

---

## Step 2 — Google Drive API: Enable for dwrack81@gmail.com
**Unlocks: All Google Docs, Sheets, and Drive files**

1. Open this URL in Chrome while logged in as dwrack81@gmail.com:
   `https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=140506566057`
2. Click **Enable**
3. Done — I can immediately read all your Drive files

---

## Step 3 — DCKT Gmail: Connect Info@DoorCountyKayakTours.com
**Unlocks: Reading/sending from your business email**

The Gmail MCP currently only has dwrack81@gmail.com. To add the DCKT business email:

1. In Claude Code → **Settings → MCP Servers → gmail**
2. Add a second Google account using Info@DoorCountyKayakTours.com credentials
3. Re-authorize

*Alternative:* Set up a Gmail forward from Info@ → dwrack81 so all DCKT emails land in one inbox I can already read.

---

## Step 4 — FareHarbor API Key
**Unlocks: Booking data → GHL sync, automated triggers on tour completion**

1. Log into FareHarbor dashboard
2. Go to **Settings → Integrations** (or contact FareHarbor support)
3. Request API credentials — note your **API Key** and **User Key**
4. Share here and I'll connect it to GHL via webhook

*FareHarbor support:* support@fareharbor.com — mention you need API access for GHL integration

---

## Step 5 — n8n Workflow Export (NOLA Party Barge template)
**Unlocks: Customer chatbot for doorcountykayaktours.com**

1. Log into n8n (nolapartybarge.app.n8n.cloud or wherever it lives)
2. Open the NOLA Party Barge chatbot workflow
3. Click **⋮ → Export → Download as JSON**
4. Share the JSON file here — I'll adapt it for DCKT:
   - Rename "Nolan" → DCKT bot name
   - Swap NOLA FAQ content → DCKT FAQ (already written in the SOP)
   - Point webhook → new DCKT n8n instance
   - Update colors/branding

---

## Step 6 — Homebase API (Bella's task)
**Unlocks: Guide schedules → GHL sync, payroll data visibility**

1. Log into Homebase → **Settings → Integrations → API**
2. Generate an API key
3. Add to GHL or share here

---

## After All Steps Are Done

Once everything is connected:

| Integration | What it enables |
|---|---|
| GHL + FareHarbor | Booking → auto-trigger all customer workflows |
| GHL + Homebase | Guide schedule → shift notification workflows |
| GHL + n8n chatbot | Website chatbot answers 24/7, escalates to GHL |
| Drive | I can read all your DCKT docs, SOPs, spreadsheets |
| DCKT Gmail | I can monitor + draft from Info@ directly |

---

## For Bella — Her Setup Checklist

Before the Friday call, David should send Bella invites to:
- [ ] GHL — DCKT sub-account (Manager role)
- [ ] Homebase — Manager access
- [ ] FareHarbor — Staff access
- [ ] Info@DoorCountyKayakTours.com — Gmail access or alias

After Friday, Bella builds:
- [ ] Guide-facing GHL workflows (G1–G4) — using the Automation Spec
- [ ] HR/onboarding system (Gusto or WorkBright) — using the HR Comparison note
- [ ] Chatbot FAQ review — using the SMS Bot SOP

---

*Related: [[DCKT — Systems Integration Hub]]*
*Related: [[DCKT — GHL Automation Workflows Spec]]*
