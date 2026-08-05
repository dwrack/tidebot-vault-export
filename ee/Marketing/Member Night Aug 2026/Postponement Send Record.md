# Member Night Postponement — Send Record

**Date sent:** 2026-08-05 (event was Thursday 2026-08-06, 6–9 PM)
**Reason:** Postponed due to smoke / air quality in Portland. Copy says "heat and air quality concerns" per Davey's wording.
**New date:** TBD — follow-up email owed to this same list.

## The send

| | |
|---|---|
| Channel | SendGrid (`~/.config/ee-sendgrid/send.py`) |
| From / reply-to | sauna@ebbandember.com, "Ebb & Ember" |
| Subject | Member Night is postponed (single subject, no A/B) |
| Category | `member-night-postpone-aug2026` |
| Batch ID (cancel lever) | `NWRmZjNhNmUtOTEwNy0xMWYxLTgxNDAtMjZmMzA3ZmEwM2VjLTY3M2Y3OGMzMA` |
| In list | 34 RSVPs |
| Delivered | 33, zero bounces |
| Held back | 1 (Serhan Ceran) |

Assets: `postponement-email.html`, `postponement-email.txt`, `postponement-recipients.json`

## Exceptions

- **Serhan Ceran <serhanceran@pm.me>** — unsubscribed 2026-06-05, so SendGrid refused him. He RSVP'd for 2 anyway. Sent him a 1:1 note from sauna@ via Gmail instead (thread `19fd3e519bcf6665`) with the postponement plus a direct question asking whether he still wants to stay unsubscribed. **His suppression record was left intact** — do not resubscribe him unless he replies asking for it.
- **dwrack81@gmail.com** was removed from global suppression during testing so Davey could see a preview. He is now back on all future Ebb sends. Re-add if that wasn't intended.
- **jonah@ebbandember.com is suppressed** and will silently miss every Ebb blast until cleared.

## Gotcha that cost time

The shell `SENDGRID_API_KEY` env var is set to the **Gravity Trails / doorcountyzip** SendGrid account (userid 25475776), not Ebb (108593827). `send.py` prefers the env var, so it grabbed the wrong key and 403'd on "from address does not match a verified Sender Identity." Worse, the first dry run scrubbed against the *wrong account's* 1,333-address suppression list and falsely reported all 34 sendable.

Workaround used: `export SENDGRID_API_KEY=$(grep -oE 'SG\.[A-Za-z0-9_\-]{20,30}\.[A-Za-z0-9_\-]{40,50}' <vault memory key file> | head -1)` before every invocation.

Also: `--test` mode skips the suppression scrub entirely, so a suppressed test address returns a clean HTTP 202 and is then silently dropped. Always confirm with `/v3/messages?query=to_email="..."` rather than trusting the 202.
