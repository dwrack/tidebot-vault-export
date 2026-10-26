# Michael: LinkedIn corporate outreach (handoff, 2026-10-22)

From David's Claude. David wants more corporate group bookings (team outings, client nights, holiday parties, convention groups) and wants it run from your LinkedIn with your Claude. Nothing sends by itself. Your Claude finds people and drafts, you tap send.

## Do these first

1. **Review the deck:** https://claude.ai/artifact/D4t2Y8kaek7w11rgsus47W (shared by link). Check the private boat rates ($800 to $1,200 by boat), the 100-guest party room (David's number, not yet checked against the occupancy permit), the 6 palapas, and that the closing slide's contact line is right. The whole-marina price and the phone number are still blank. Tell David OK or send edits.
2. **Read `Playbook.md` in this folder.** It has the segments, what we give each one, the limits and the voice.
3. **Check your Claude has `apify-npb` at user scope on your Mac** (NPB's Apify account, billed to the business). If it's missing, ask David. Don't copy his key.

## Paste this to your Claude each weekday

```
Run the LinkedIn 5 for Nola Party Barge. Read Marketing/LinkedIn Corporate Outreach/Playbook.md and Tracker.csv first. Find 5 new New Orleans people (DMC owners, hotel group sales, convention and meeting planners, office managers or HR at companies of 2 to 100 people) with the Apify actor harvestapi/linkedin-profile-search through apify-npb, skipping anyone already in Tracker.csv. For each person, read their profile, pick the segment and one real hook, and draft a connection note (200 characters max, no pitch, no link) in my own voice, plus a follow-up for after they accept. Show all 5 in chat, ready to copy. Do not send anything. Add them to Tracker.csv. Also draft follow-ups for anyone who accepted 2 or more days ago.
```

A test search of 10 profiles cost about 15 cents, so a month of this should run a few dollars.

## Rules

- You send every message by hand from your own LinkedIn. No automation tools or browser extensions, because LinkedIn restricts accounts that automate.
- 5 new requests a day, 25 a week. No more than 2 messages without a reply.
- Write Nola Party Barge in full, never NPB. Never mention pedaling. Never name past guests.
- David's name stays off all of it.
- Hold the deck link until they reply.

## Tracker

Create `Tracker.csv` in this folder with the columns: date, name, title, company, segment, hook, note_sent, accepted, replied, outcome. Your Claude keeps it current. On Fridays it gives David a one-line scorecard: sent, accepted, replied, booked.

## Still open (David decides)

- Commission or net rate for DMCs and hotels. Until it's set, drafts say "partner rates" and nothing more.
- How many free fam trips a month, and which boat and slot.
- Whether we donate rides to fundraisers.
