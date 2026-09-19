# Merch — Outreach Send Instructions (Mac)

*Handoff for the always-on Mac session, which has the davey@ebbandember.com mailbox connected. The cloud session could only reach dwrack81@gmail.com, so it prepared everything and stopped short of sending.*

---

## What to send

- 60 plain-text emails, one per vendor, in `merch-outreach-drafts.json` in this folder. Each record has `to`, `subject`, and the full `body`.
- Send FROM davey@ebbandember.com only. If that identity is not available, do not send from another address. Write the 60 emails to `~/Desktop/EE merch outreach/` as .txt files instead and stop.
- Subject for every email: Sample request from Ebb & Ember, Portland's floating sauna
- No attachments, no HTML, no tracking. A few seconds between sends.
- One email per address. Nobody outside the JSON.

## How to find the mailbox

Check in order: a Gmail MCP connector authenticated as davey@ebbandember.com; Apple Mail with the davey account (AppleScript); the mail setup in `~/Projects/tidebot`.

## Log

Append a section `## Send Log (Mac, <date>)` to `Merch — Sample Outreach Tracker.md` with a table: company | email | sent or failed | timestamp. If the vault is not on the machine, write the log to `~/Desktop/EE merch outreach/send-log.md`.

## Report

Five lines at the top of the final message: mail connection used, sent count, failed count and why, log location, anything that needs Davey.

## Prompt to paste into the Mac session

> Send the Ebb & Ember merch sample outreach from davey@ebbandember.com. Instructions and the 60 email bodies are in the tidebot-vault-export repo, branch claude/ebb-ember-merch-curation-v7wfn0, folder ee/Marketing: read "Merch — Outreach Send Instructions (Mac).md" and follow it.

---

*Prepared September 19, 2026.*
