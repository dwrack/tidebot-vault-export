# Member Night — Community Invite Send Record

**Sent 2026-07-28, immediately, in one pass.** 2,134 recipients.

This is the non-member expansion of the Aug 6 Members' Night, opened to the wider contact list after the members-only sends on Jul 17 (ActiveCampaign) and Jul 23 (SendGrid, 38 people).

## Send parameters

- **Category:** `member-night-community-aug2026`
- **Subject:** Join us next week for a dockside sauna party
- **Recipients:** 2,134
- **From:** Ebb & Ember <sauna@ebbandember.com>, reply-to same
- **Creative:** `community-invite-email.html` + `community-invite-email.txt` (this folder)
- **RSVP:** `https://ebbandember.activehosted.com/f/1` (ActiveCampaign, verified 200)
- Delivered in 10 back-to-back API calls of ~225 each. No scheduling, no throttling.

Early numbers at send time: 0 bounces, 0 blocks, 0 spam reports.

## A cancelled first attempt

An earlier version of this send was queued as a 50/50 A/B subject test scheduled for Wed Jul 29, 9 AM to 1 PM PDT. Davey called it off before delivery: no A/B, single subject, send immediately.

That batch (`YTljNWQyMDItOGFkOS0xMWYxLThlMjItNDJhNDQ1NGE3NzNlLTViNzhjMjQ2Mw`) was cancelled via `POST /v3/user/scheduled_sends` and confirmed `status: cancel` with **0 delivered** both before and after the real send went out. Nobody received two copies.

The lesson worth keeping: creating a batch id via `POST /v3/mail/batch` and attaching it to every personalization is what made that reversible. Scheduled mail without a batch id cannot be recalled. Always attach one.

## List derivation

Source: Google Sheet `Sauna Boat Opt in Form (Responses)` → `Master Contacts` tab, 2,301 rows.

| Step | Out | Left |
|---|---|---|
| Rows with non-blank Status (col F) | 24 | 2,277 |
| Live SendGrid suppression (unsubscribes, bounces, blocks, spam, invalid) | 118 | 2,159 |
| Already got the Jul 23 member send | 24 | 2,135 |
| Gmail-normalized duplicate | 1 | 2,134 |

Notes on the drops:

- **Suppression was fetched live, not read from the doc.** SendGrid held 150 suppressed addresses at send time; `Marketing/Do Not Contact List.md` still says 33. The doc is stale and should not be used as a source. Note `/v3/asm/suppressions/global` returns empty; the real opt-out list is `/v3/suppression/unsubscribes`. The count moved from 141 to 150 over the course of a single afternoon, so fetch it at send time, never earlier.
- **Only 24 of the 40 exclusions matched** because most members came from Periode and were never in Master Contacts. Verified zero members leaked through, including the comped crew (Kimberlynn, Jess, Grant, Hannah, Mack, Jordan) and Danesh.
- **Jennifer Wessler** (`yorefinnej@icloud.com`, cancelled 2026-06-21 over the jet noise) correctly held back by suppression.
- **`erik@periode.no`** added to the exclusion list by hand. Periode vendor support, same call as the July send.
- The duplicate was `camijustice@yahoo.com`, an exact repeat row in the sheet. Worth cleaning at the source.
- Deliberately kept in: `me@jonahmoses.com` (Jonah should see what went out) and `michael@saunaglo.com` (real waiver contact).

## Copy changes from the member version

Community-first paragraph order per Hannah's suggestion. The July 24 RSVP deadline became "we'll close it once we're full" (Davey's call, no fixed date). The "feel free to bring a guest" line dropped, staying silent on guests. Footer permission line changed from "you are a current or former member" to "you signed up for updates," since that claim is false for this audience. Second RSVP button added above the hero art so the CTA is visible on an iPhone without scrolling.

Same hero photo and logo as the member send, both verified live off the ActiveCampaign CDN.

## Pre-send verification

Two tests sent 2026-07-28, category `member-night-community-aug2026-test`, both delivered:

- `dwrack81@gmail.com` and `davey@ebbandember.com`

Confirmed on the received message:

- `List-Unsubscribe` in **https URL form, not mailto**, so Gmail's native button won't generate opt-out emails into the inbox
- `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058)
- `dkim=pass` and `spf=pass`, signed `d=ebbandember.com` via `s1`/`em3439`
- `[unsubscribe_url]` substitution resolved to a real hosted URL in both HTML and plain text

That last one matters: SendGrid's auto-appended footer silently failed on the July test, which would have shipped a CAN-SPAM gap. The footer is hardcoded and the tag passed explicitly in `tracking_settings.subscription_tracking`.

## Pull results

```
curl -H "Authorization: Bearer $SENDGRID_API_KEY" \
  'https://api.sendgrid.com/v3/categories/stats?start_date=2026-07-28&categories=member-night-community-aug2026'
```

Aggregate requests under this category will read high because the cancelled batch was counted as requested. **Delivered is the number to trust**, and it should top out around 2,134.

**Caveat on per-recipient data:** `/v3/messages` (the Email Activity feed) returned zero rows for every query on 2026-07-28, including the Jul 23 send that definitely happened. Address-level open/click data may not be retained despite the June note saying it was enabled. Check the Email Activity setting in the SendGrid UI before planning any "email the non-openers" follow-up.

## Open item

**No capacity cap is documented for the dock, and the ActiveCampaign RSVP form has no cutoff.** 2,134 invitations went out tonight against an unknown number of spots, and RSVPs will start landing within the hour. Watch the AC form and have a short "we filled up, next one soon" reply ready for overflow. A sent email can't be changed, so this is the only lever.

Sender: `~/.config/ee-sendgrid/send.py`.
