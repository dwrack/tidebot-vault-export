# Captain Audio Log — Processing SOP

## Why This Exists

USCG Subchapter T requires a logbook covering safety drills, emergency equipment maintenance, and trip logs. Captain audio logs posted to Slack are the raw input. This SOP turns them into structured, timestamped records that satisfy that requirement.

## The Flow

1. **Captain finishes trip** and records a voice memo covering the trip
2. **Captain posts audio** to the designated Slack channel
3. **Audio is transcribed** and structured into a log entry in `Captain Logs/`
4. **Original audio is retained** in Slack (and backed up if needed) as the source record

## What Captains Should Cover in Their Audio Log

Tell them to just talk through the trip. Don't read a script. Hit these points naturally:

- Vessel name and trip time
- Passenger count
- Weather and water conditions
- Pre-departure safety check: anything flagged or out of order?
- All waivers signed?
- How the trip went: route, vibes, anything notable
- Any incidents, guest issues, equipment problems, or deviations
- Post-trip: equipment status, anything that needs maintenance or follow-up

A 60-90 second voice memo covers all of this. Doesn't need to be long.

## Processing Steps

When an audio log comes in on Slack:

1. Transcribe the audio (Whisper, built-in transcription, or manual)
2. Create a new file in `Captain Logs/` using this naming format:
   `YYYY-MM-DD — {{Vessel}} — {{Time}} — {{Captain}}.md`
   Example: `2026-04-21 — Boogie — 2pm — Ben.md`
3. Fill in the template fields from the transcription
4. Check off the safety items the captain confirmed
5. Flag anything that needs follow-up (maintenance, incidents, missing items)
6. If there's an incident, cross-reference with the Incident Report procedure in `SOP Coast Guard & Compliance.md`

## USCG Compliance Notes

- Logs must be retained and available for inspection
- The structured markdown log is the official record
- Original audio in Slack serves as backup/source material
- Any incident log should also trigger the full incident report process if it meets the threshold (injury, >$2k damage, vessel accident)
- Inspectors may ask for logbook going back 3 years, so don't delete old logs

## Slack Channel

Captains post audio logs to the NOLA Party Barge Slack channel connected via Rail/GitHub to this vault.

---

*See also: `Captain Logs/Captain Log Template.md` for the structured format.*
