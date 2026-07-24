# Member Night — SendGrid Send Plan

Built 2026-07-22. Event: **Thursday, Aug 6, 6-9 PM**, Ebb & Ember, 173 NE Bridgeton Rd.

## Status: tested, ready to send. Waiting on Davey's call on 3 things (bottom).

---

## What the source email was

The `.eml` in Downloads was a Gmail forward of the **ActiveCampaign send that already went out Fri Jul 17, 3:19 PM**. It had everything needed (art, copy, RSVP link), but it was wrapped in AC tracking and a Gmail forward header. All of that is stripped now.

## What got rebuilt for SendGrid

| Original (ActiveCampaign) | Now |
|---|---|
| Gmail "Forwarded message" header block | removed |
| RSVP button to `emlnk9.com/lt.php?x=...` (per-contact tracking) | direct to `https://ebbandember.activehosted.com/f/1` (the AC RSVP form, verified 200) |
| FB / IG / TikTok icons wrapped in AC tracking | direct to the real profile URLs |
| AC open-tracking pixel | removed (SendGrid adds its own) |
| AC unsubscribe (`proc.php?act=unsub`) | removed, replaced with SendGrid |
| AC address footer | replaced with our own address block |

Images still load from the AC CDN. All 3 verified public and returning 200, so they render fine from a SendGrid send. Not worth rehosting for a 35-person list.

**RSVP still lands in ActiveCampaign.** The form at `/f/1` collects first name, last name, email itself, so stripping the per-contact params costs nothing.

Artifact: `member-night-email.html` (this folder).

## Unsubscribe wiring — the actual finding

SendGrid account-level subscription tracking is on, but on the first test it **silently failed to append the visible footer**. Headers were fine; the body had no unsubscribe link and no physical address. That is a CAN-SPAM gap and it would have shipped unnoticed.

Fix: stop relying on the auto-append. The footer is now written into the HTML and the plain text directly, with `[unsubscribe_url]` as an explicit `substitution_tag` passed in `tracking_settings.subscription_tracking`. SendGrid swaps in the hosted URL at send time.

Verified on the received message (TEST 2):

- `List-Unsubscribe: <https://u108593827.ct.sendgrid.net/lu/unsubscribe?...>` — **URL form, not mailto**, so the native Gmail/Apple button does not generate an unsubscribe email to the inbox
- `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058)
- Visible hosted unsubscribe link in the HTML body, plus the URL in plain text
- Physical address in the body
- `dkim=pass` + `spf=pass`, signed `d=ebbandember.com` via `em3439`
- Clicked the link end to end: returned "Unsubscribe successful", the address landed in SendGrid global suppression, then the test address was removed again (suppression list back to 118)

## Audience

**38 recipients: 27 current, 11 past.** Built from the Periode merchant API, cross-checked against the `betalinger.csv` payments export, then deduped and scrubbed. Full reconciliation in `Send List.md`.

The payments export added no actual members (its 3 extras are all failed signups). It did confirm 33 of them, and the exercise surfaced that 3 comped crew memberships were never created in Periode. Those 3 were added by hand.

## Decisions (Davey, 2026-07-22)

1. **RSVP deadline stays July 24.** No art changes. Two-day window is fine on a 35-person list; late RSVPs get handled by hand.
2. **Send to all 35**, including anyone who already got the Jul 17 AC blast. Reads as a member-specific nudge, no exclusion pass needed.

## To send

`send_lib.py` in the session scratchpad, or replicate: SendGrid v3 `mail/send`, from `sauna@ebbandember.com`, category `member-night-aug-2026`, one personalization per recipient, `subscription_tracking.substitution_tag = [unsubscribe_url]`.

Per-recipient open/click tracking is on, so results can be pulled by category after the send.
