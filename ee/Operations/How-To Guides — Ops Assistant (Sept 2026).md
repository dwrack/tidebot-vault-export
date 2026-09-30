# How-To Guides: Ops Assistant (Sept 2026)

Status: DRAFT for Davey + Jonah. Built 2026-09-30. Pairs with [[Master Action List (Sept 2026)]] (item numbers H2-H60). Updated 2026-09-30 with Davey's answers.

How this file works: **Part A** is 17 reusable SOPs. **Part B** is one card per task: which SOP, who to contact, what done looks like, when to escalate. Where an SOP already exists in the vault, the guide points to it instead of rewriting it.

## Ground rules (read first)

1. **Nothing goes out without an OK.** Every email, text, Slack post, review reply, or vendor order gets drafted first and approved by Davey or Jonah (SOP-3). No exceptions in the first 90 days.
2. **Access is staged.** Day 1 you get sauna@ebbandember.com. Other tools (Periode, ActiveCampaign, Meta, Google Ads, Slack channels) get added as tasks need them and trust builds. Ask for access, don't borrow someone's login.
3. **Month 1: ask before you buy anything.** Every purchase gets an owner OK first. After month 1, routine buys go on auto up to a limit the owners set.
4. **Logins live in 1Password.** Never paste a password, code, or API key into Slack, email, a doc, or this vault. If you see one posted somewhere, tell Davey.
5. **Sign as the business.** "Ebb & Ember" (or "Elevated Tides" for marina stuff). No founder names on anything public.
6. **Brand words.** Always "Ebb & Ember" with the ampersand. It's a sauna session, never "a float." Don't mention the fuel type. Location is Portland, Oregon, on the Columbia River.
7. **Write it down.** If a task is waiting on someone, it goes in `Open Loops.md` the same day.
8. **Not your lane:** Dustin exit, owner pay, legal, pricing, strategy, The Rose / Holman Dock, Slip 7, anything that speaks for Davey or Jonah on money or people. If a task drifts into one of these, stop and flag it.

---

## Part A: Reusable SOPs

### SOP-1: Periode support request
Tool: Periode admin (login in 1Password). Contact: Erik Kvanli, erik@periode.no (support backup: kontakt@periode.no).
1. Check `Operations/Ideas & Tools Backlog.md` and `Operations/Email SOP & FAQ.md` for what's already been asked. Don't re-ask cold.
2. Reproduce the problem yourself in Periode. Screenshot it.
3. Draft one email per issue: what happens, what should happen, a screenshot, a real example (booking ID, no guest personal info beyond what's needed).
4. Get the OK (SOP-3), then send from sauna@.
5. Log it in `Open Loops.md`: item, "Periode / Erik", date sent.
6. No reply in 7 days: one polite bump. No reply in 14: escalate to Davey.
7. **Done** = Periode confirms a fix (or says it can't be done) and you've tested it. Update the Master Action List row.

### SOP-2: ActiveCampaign email send (newsletter, member, segment)
Tool: ActiveCampaign (1Password). Lists: Master Contacts sheet (tab "Master Contacts"), Periode member export.
1. Write the draft in the vault first (`Marketing/`). Short, skimmable, sentence-case subject, CTA button above the fold on an iPhone, button before any big image.
2. Build the audience. **Scrub it** against `Marketing/Do Not Contact List.md` and `Marketing/Ebb and Ember - Email Unsubscribes 2026-07-20.xlsx`. Dedupe with Gmail normalization (lowercase, drop dots and +tags on gmail.com).
3. Unsubscribe must be ActiveCampaign's hosted one-click link. Never "reply to unsubscribe," never a mailto link.
4. Give the campaign a unique name (e.g. `newsletter-2026-10-07`) so opens/clicks are traceable per recipient.
5. Send a test to yourself + Davey. Check it on a phone.
6. Get the OK on the test (SOP-3). For anything over ~50 people, Davey approves one sample before the batch.
7. Don't cc media@ on outbound (Davey, 2026-06-23; older trackers that say "cc media@" are out of date).
8. Schedule or send. Afterward, add any new unsubscribes or "take me off" replies to the Do Not Contact list the same day.
9. **Done** = sent, stats noted in the vault file (sent / opens / clicks / unsubs) 48 hrs later.
Escalate: bounce rate over ~5%, spam complaints, or anyone angry.

### SOP-3: Draft for approval (anything outbound)
1. Write the draft where the owner can see it: the vault file for the task, or a Slack DM to Davey/Jonah.
2. Top line: who it goes to, channel (email/text/Slack), and one-line gist.
3. Then the exact text, as it will send.
4. Wait for a clear "yes, send." A thumbs-up on a different message doesn't count.
5. Send, then note "sent [date]" on the draft.
Guest and vendor replies that follow an existing template in `Operations/Email SOP & FAQ.md` can be pre-approved as a category later. Until Davey says so, everything goes through this.

### SOP-4: Vendor / contractor chase (quotes, parts, photos, deliverables)
Tools: Slack (Grant, Jess, Hannah, Kimberlynn are in Slack), sauna@ email for vendors outside Slack, text for people who aren't in Slack (draft first).
1. Find the ask in its source (Master Action List, punch sheet, Slack thread). Write down exactly what's needed and by when.
2. Team/contractor asks go in the right Slack channel (build stuff in #private-saunas-build), not email.
3. One message, one ask, a date. Example: "Can you send the photo of the inside-wall rough-in by Friday?"
4. Log it in `Open Loops.md`.
5. Bump once after 3 business days. Second bump after a week, and tag Davey or Jonah.
6. When it arrives, file it (quote PDF → `Operations/` next to the project; photo → `Assets/Photos/<date>/`), and update the row.
7. **Done** = the thing is in hand and filed, and the owner knows.
Escalate: any quote over the spend limit, any vendor asking for payment or a signature, anything safety-related that's slipping.

### SOP-5: Weekly Open Loops review (Mondays)
File: `Open Loops.md` (plus the Davey <> Jonah note for proposed edits).
1. Open the file. For each row: is it still waiting? On whom? Since when?
2. Waiting 7+ days: send a nudge (SOP-4) and fill "Last nudge."
3. Waiting 14+ days: move it to a short "Needs owner call" list and post that list to Davey + Jonah.
4. Unblocked items: move to `Active Projects.md` or mark done.
5. Scan Slack for new stuck asks since last Monday and add them.
6. For the Davey <> Jonah note: send the owners a short list of suggested edits (items done, items missing names, items with no date). Don't edit the note yourself.
7. **Done** = every row has a date, an owner, and a last-nudge date from this week.

### SOP-6: Punch List sheet + pinned Slack update
Sheet: "Punch List Items" (Google Sheets, link in 1Password/bookmarks). Channel: confirm with Davey (likely #sauna-improvements).
1. One row per task. Every row has Owner, Priority (High / Medium / Low only), Complete (x or blank), and a Notes date.
2. New item from Slack or a meeting: add a row the same day.
3. Done item: mark x, add who confirmed it and the date.
4. Once a day (work days): **edit the one pinned Slack post in place.** Never post a new one. Format: Done this week / In progress (owner) / Blocked (on whom).
5. The old Grant fix lists (ET + E&E, now facilities-hire work) live in the same sheet on their own tab.
6. **Done** = sheet and pinned post match, no row without an owner.

### SOP-7: Member night / themed event logistics
Template: `Marketing/Members Night Sept 15 — *` files and `Marketing/Member Night Aug 2026/` (send plan, send list, send record). Programming SOP: `SOPs/Ebb and Ember — SOP Programming Activations.md` (use its insurance + agreement stages for any outside partner).
1. T-4 weeks: owners confirm date, time, capacity, partner/vendors. Write it at the top of a new vault file.
2. T-3 weeks: build the invite list from Periode (active members, paused members flagged separately). RSVP form via ActiveCampaign.
3. Draft invite email (SOP-2) and SMS copy. SMS goes from Google Voice on the sauna@ number: vary the wording between waves, send in small spaced batches (26 identical MMS tripped the limit in Sept). Scrub against Do Not Contact by hand, SMS has no auto-scrub.
4. T-1 week: confirm vendors, headcount, any partner insurance cert (SOP-16).
5. T-1 day: one reminder round.
6. Day-of checklist: iPad charged with the guest waiver open (SOP-8), guest list, towels, signage, content plan with Kimberlynn (who's OK being filmed).
7. After: send record, headcount, what broke, photos filed (SOP-11).
8. **Done** = recap file in the vault within 3 days.

### SOP-8: Waivers
Tool: Periode waiver settings + the entrance iPad.
**Changing waiver text (H2):**
1. Pull the current waiver text into a vault file.
2. Draft the new lines (e.g. pregnancy, heart conditions, medications) as tracked additions.
3. Owners approve the language (and their attorney, if they say so). You don't write legal terms on your own.
4. Update in Periode, sign a test waiver yourself, screenshot.
5. **Done** = live text matches the approved draft.
**Collecting at events and walk-ins (H3):**
1. Every guest signs before they go on the dock. Members' guests too.
2. iPad at the entrance, waiver open, charged.
3. Check names against the RSVP/booking list.
4. Anyone who won't sign doesn't go on the dock. Get Davey or Jonah if it gets awkward.

### SOP-9: Customer service inbox (sauna@)
**Use the existing SOP:** `Operations/Email SOP & FAQ.md` (cancellations, door codes, donations, operator inquiries, partnerships, memberships, promo codes) and `SOPs/Cancellation & Refund Policy.md`.
1. Check twice a day on work days. Weekends too once W-2 (nobody owns weekends right now).
2. Reply with the matching template. Gift cards are issued in Periode.
3. Donation requests: the Monday auto-responder already sends $50 gift cards. Check it ran, handle the odd ones.
4. Guest-pass questions: Ember 1 = 4 guest passes, Ember 2 = 8, and the member must be present.
5. Anything not in the SOP (complaints, injuries, press, partnership asks, refunds outside policy): draft and send to Davey (SOP-3).
6. Public phone for guests is (503) 308-1293. Never give out any other number.

### SOP-10: Outreach batch (lodging, brands, creators, merch, corporate)
Trackers: `Marketing/Lodging Outreach — Tracker (Jun 2026).md` + `— Templates & Sample`, `Event Partner Target List (Aug 2026).md` + `Event Brand Partnership Framework.md`, `Creator Outreach Playbook.md`, `UGC Outreach & Repost Playbook.md`, `Merch — Vendor Sample Outreach (Sept 2026).md`, `Corporate & Buyout Package — Draft (Sept 2026).md`, `Partner Outreach Drafts (Pending).md`.
1. Pick 10-20 targets from the top of the tracker.
2. Scrub against the Do Not Contact list.
3. Personalize one sample using the tracker's template. Davey approves the sample (SOP-3).
4. Send 1:1 from the address Davey names (not a bulk tool). Space them out.
5. Log every touch in the tracker (status, date).
6. Follow up once at ~7 days, again at ~14. Then mark `dead` or move on.
7. Replies that want a deal, a price, or a meeting go straight to Davey/Jonah.
8. **Done** = every target in the batch has a status and a date.

### SOP-11: Video + content capture
References: `Marketing/V2 Build Diary — Content Playbook (Aug 2026).md`, `Marketing/B-Roll Shot List — Photographer Brief (Aug 2026).md`, `Marketing/Social Media Strategy — Kimberlynn.md`.
1. Kimberlynn directs and edits. You host on camera or collect clips.
2. Guests on camera: verbal OK at minimum, written release for anything featured. No release = tag the file PRIVACY-HOLD.
3. File everything in `Assets/Photos/<YYYY-MM-DD>/` with `_originals/` and a `CATALOG.md` line per clip (who, what, release yes/no).
4. Best clips to Kimberlynn in Slack with the path.
5. **Done** = filed, cataloged, handed off.

### SOP-12: Research and recommend (one-pager)
Use for: temp display, Harvia battery, door ball, lock bridge, mats, gas techs, furniture, Dock Galley, welcome kit, summaries.
1. Write the question in one line at the top of a new vault file.
2. Find 3 options max. For each: what it is, cost, link, lead time, who installs.
3. Pick one and say why in two lines.
4. List what you couldn't confirm. Don't guess specs; write "unknown, need X."
5. Post the file path to the owner. **Done** = they say yes/no.

### SOP-13: Meeting write-up
1. Listen once through, take timestamps.
2. Write: decisions, action items (who + by when), open questions, one-paragraph summary.
3. Action items go onto the Master Action List / punch sheet.
4. Save in the vault next to the recording reference. Owners review before anything is shared further.

### SOP-14: Buying supplies, parts, and subscriptions
1. Month 1: everything needs an owner OK. After that, check the auto-buy limit (not set yet, see Master Action List Q6).
2. Link + price + quantity + who installs, posted to Davey or Jonah.
3. Buy with the method they name. Never enter card numbers yourself unless they set you up with a company card.
4. Receipt to the bookkeeping folder the owners name. Log the delivery date.
5. Recurring items (trash bags, TP, cleaning supplies): keep a simple reorder list with par levels. Reference: `Operations/Cleaning, Stocking & Maintenance.md`.
6. Subscriptions (water filter, TP, paper towels): check the exact product on site first (filter model, dispenser size), count how fast it runs out, pick a delivery interval, compare 2 suppliers. Owner approves, then set it up to ship to the address they name.
7. Log every subscription (item, supplier, interval, cost, account email) in one table in `Operations/` so it can be paused or cancelled later.

### SOP-15: "Did it actually ship?" check
Needs read-only Ads access, which comes after trust is built. Until then Davey or Claude runs it.
1. Find the approved change (e.g. `Operations/Google Ads Keyword Plan & Budget Decisions (2026-07-18).md`).
2. Look at the live system (read-only access, or ask Claude to check).
3. Table: approved vs live, one row per setting.
4. Mismatches go to Davey. Don't change ad settings yourself.

### SOP-16: Vendor insurance certs
Folder: `Operations/Vendor Insurance Certs/` + its README (Linnea is the worked example).
1. List every vendor/instructor/contractor who works on site.
2. Ask each for a certificate naming Elevated Tides LLC and Elevated Tides Experiences LLC (173 NE Bridgeton Rd, Portland, OR 97211) as additional insured. Limits: owners set the minimum (Linnea's is $2M/$3M).
3. File the PDF, add a README entry (insurer, policy #, limits, expiry).
4. Calendar reminder 30 days before expiry on the sauna@ calendar.
5. Anyone without a cert: flag before their next on-site day.

### SOP-18: Cleaners (code + oversight)
**Cleaners code (H27):**
1. The sauna lock auto-locks. The code change needs Bluetooth, so do it on site with the lock app (login in 1Password).
2. Create a separate cleaners code. Never reuse the guest code.
3. Give it to the cleaners in person or by a message the owner approves. Never post it in Slack, email threads, or the vault.
4. Test it on the door. Put "cleaners code set [date]" on the punch sheet (no digits).
5. If the guest code changes, check the cleaners code still works.
**Oversight (H59):**
1. Get the cleaners' schedule (which days, what time). Put it on the sauna@ calendar.
2. Write a one-page checklist from `Operations/Cleaning, Stocking & Maintenance.md`: sauna benches, floors, bathroom, shower, lounge reset, trash, restock.
3. After each visit (or the next day you're on site), walk it with the checklist. Photos of anything missed.
4. Log each visit: date, done/missed items. Jonah uses the log to pay them.
5. Restock soap, shampoo/conditioner, paper towels, TP when under par.
6. Two misses in a month: send the log to Jonah. You don't give the cleaners feedback on pay or their contract.

### SOP-17: Weekend sauna hosting (W-2 only)
Not written yet. The vault's `SOPs/... Pre-Tour Preparation` and `... Guest Communication Templates` were copied from the kayak business and don't fit a sauna. Use these for now: `SOPs/How We Run Things — Ebb and Ember.md`, `SOPs/Culture Quiz — Ebb and Ember.md`, `Operations/Cleaning, Stocking & Maintenance.md`, `SOPs/Ebb and Ember — SOP Coast Guard & Compliance.md` (incident report). The hire's first weekends are shadow shifts; they write the hosting SOP from those.

---

## Part B: Task cards

| # | Task | SOP | Contact / tool | Done looks like | Escalate if |
|---|---|---|---|---|---|
| H2 | Waiver medical language | 8 | Periode waiver settings | Approved text live, test waiver signed | Owners haven't approved in 7 days |
| H3 | Event waivers on iPad | 8 | Entrance iPad | 100% of guests signed before the dock | Someone refuses |
| H4 | Mario parts + stove schedule | 4 | Mario (Hannah has the thread) | Parts list, order confirmation, monthly schedule on the calendar | Stove fails again before parts arrive |
| H5 | Emergency gas tech list | 12 | Web search, calls | 3-5 names with phone, hours, rate in `Operations/` | None answer after-hours calls |
| H6 | CO alarm | 14 | Owner OK to buy; Facilities hire installs | Alarm installed + tested, one per V2 stove on the V2 list | Any alarm sounds: guests off the boat, call Davey/Jonah |
| H7-H10 | Periode asks | 1 | Erik Kvanli | Fix confirmed and tested | 14 days no reply |
| H11 | Signage to print | 4 | Jess (Slack), sign printer | Signs printed and handed to the facilities hire for install. 10 river-safety signs = 1 per ramp, 1 per life ring (7), 1 at the sauna walk-up | Jess blocked on an owner decision |
| H12 | Boater discount email | 2 | Owners set %, Dockwa list via Jonah | Sent to slip holders + houseboat list | Pricing not decided |
| H13 | Weekly newsletter template | 2 | ActiveCampaign | Reusable template + 1 approved send | Unsub spike |
| H14 | Referral announcement | 2 | Periode (25% referral live), ActiveCampaign | Sent to members | Referral terms unclear |
| H15 | Dockwa follow-ups | 3 | `../Elevated Tides/Dockwa Contacts.md`, Jonah | 5 drafts approved by Jonah. Drafts only for now; Jonah decides on direct texting after you start | Hurt's 12-month clause and Fitzpatrick's $925 are Jonah's call |
| H16 | Lodging outreach | 10 | Lodging tracker | First 7 sent, logged | Any "what's the commission?" reply |
| H17 | Safety + welcome videos | 11 | Kimberlynn | Videos cut and approved | Script questions on safety claims: owners approve wording |
| H18 | Reviews + monthly summary | 12, 3 | Google Business Profile, email surveys, `Marketing/_reviews_export` | Reply drafts approved and posted; summary to owners by the 5th | Any review mentions injury or safety |
| H19 | Google Ads check | 15 | Read-only Ads access or Claude | Approved vs live table | Any mismatch |
| H20 | Twilio A2P status | 5 | Ask Claude "check the Twilio campaign status" | VERIFIED noted, or FAILED sent to Davey | FAILED |
| H21 | Current alarm instructions | 4 | Manufacturer support | Install instructions PDF to Facilities | No reply in 14 days |
| H22 | Punch sheet cleanup | 6 | Punch sheet | Every row: owner, High/Med/Low, date. Zach rows reassigned | Nobody to assign a row to |
| H23 | Old Grant lists sorted | 6 | The "Tasks for @Grant" Apple Note (owners share it) | One tab, ramp wheels on top, statuses | Ramp wheels not scheduled |
| H24 | Open Loops current | 5 | `Open Loops.md` | Every row dated, June items resolved or re-dated | |
| H25 | Next member night | 7 | Sept 15 files | Recap filed | No date from owners by T-4 weeks |
| H26 | Sauna insurance renewal | 4, 12 | Davey + Jonah, current carrier/broker | Current policy summarized (carrier, limits, renewal date), changes listed (V2 saunas, events, capacity), renewal quote in front of owners before the renewal date | Anything needing a signature, payment, or a coverage decision |
| H27 | Cleaners code | 18 | Lock app on site (Bluetooth) | Code works on the door, cleaners have it | Never write the code down anywhere shared |
| H28 | Anti-slip mats | 12, 14 | Facilities hire installs | Mats quoted, bought, screwed down | |
| H29 | Parking package | 4, 12 | Jess designs, Facilities hire installs | Sign copy + quotes approved | Towing language needs owner/legal OK |
| H30 | Insurance certs | 16 | Each vendor | Cert on file for every on-site vendor | Vendor has no insurance |
| H31 | Figure out merch | 10, 12 | Merch tracker + `Merch — Vendor Sample Outreach (Sept 2026).md`; Jordan (Early Bird PR) for Pals | Samples requested, then a one-pager: what to sell, vendor, unit cost, minimums | Minimums or pricing need a decision |
| H32 | Event brand partners | 10 | Target list + framework | Tier A pitches out, logged | Any brand wants to talk money |
| H33 | Creator + UGC outreach | 10, 11 | Playbooks, Kimberlynn | Weekly invites out, reposts logged with permission | |
| H34 | V2 build diary clips | 11 | Grant (Slack) | Daily clips filed + cataloged | Grant stops sending |
| H35 | Videographer quotes | 4 | Shot list brief | 3 quotes to owners | |
| H36 | Partner newsletter features | 10 | Alder Creek, Island Sailing | Contact names found, drafts approved | |
| H37 | Corporate target list | 10 | Corporate package draft | 25 targets in a tracker | Pricing questions |
| H38 | Slip-holder welcome kit | 12 | Jonah | Draft kit approved | |
| H39-H42, H44 | Research one-pagers | 12 | Web | One-pager with a pick | |
| H43 | Phone charger sign | 4 | Print shop, Facilities installs | 3 taglines → approved → printed → installed | |
| H45 | FAQ additions | 3 | Jess posts on the site | Live on /faq | Alcohol answer not decided |
| H46 | World Sauna Day plan | 7 | WORLDSAUNA code in Periode | Plan to owners by Jan 15 | Confirm dates in writing before touching the code |
| H47 | Silent night + yoga concepts | 7, 12 | Programming Activations SOP | Proposal with partner, slot, price idea | Partner needs a contract |
| H48 | Spigot photo | 4 | Mario | Photo delivered to Mario | |
| H49 | Lounge fan | 4 | Manufacturer | Answer on app/smart switch | |
| H50 | Prospectus clip consent | 11 | Crew member (Davey names them) | Written OK filed, or clip swapped | |
| H51 | sauna@ inbox | 9 | Gmail sauna@ | Inbox under a day behind | See SOP-9 |
| H52 | Pinned Slack update | 6 | Slack | Pinned post edited daily | |
| H53 | Weekend hosting | 17 | On site | Shadow shifts done, hosting SOP drafted | Any injury: Coast Guard SOP incident steps |
| H54 | Davey <> Jonah note edits | 5 | Owners | Weekly suggested-edit list sent | |
| H55 | Trash bags + supplies | 14 | Reorder list | Par levels never hit zero | |
| H56-H58 | Water filter, TP, paper towel subscriptions | 14 | Check product on site first | Each subscription approved, running, logged in the table | Cost jumps or item discontinued |
| H59 | Cleaner oversight | 18 | Cleaners, Jonah | Weekly visit log + checklist results | Two misses in a month |
| H60 | Rain garden water flow | 12 | Owners (details TBD) | One-pager: water source, flow path, plant list, cost, who builds, any marina/city permit question | Anything touching the river or needing a permit |

---

## Before the hire starts (owner homework)

- Answer the 7 remaining questions at the bottom of the Master Action List.
- Rotate the passwords that were posted in Slack (O4) and put everything in 1Password.
- Decide which H items are the 3-4 contract projects (hiring doc lists 6 candidates; H7-H10, H15, H17, H25 map to them. The member meeting write-up is off the list).
- Confirm the Slack channel for the pinned punch-list post.
