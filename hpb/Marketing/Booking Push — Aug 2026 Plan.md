# HPB Booking Push — What Actually Moves the Needle (Aug 13, 2026)

## Short version
Email blast is the wrong first move. It's blocked, and the list is a liability.

---

## Why not the email blast (yet)

**1. Sending is literally broken.** Per `EMAIL DNS STATUS.md`, checked this morning:
- SES MAIL-FROM: not verified
- Daily test email to David: **failed**
- Still waiting on FareHarbor to add 3 Cloudflare records (`Email Deliverability Fix — DNS Records.md`)

Nothing goes out until that's fixed. Chasing FareHarbor on those 3 records is the single highest-leverage
30-minute task on this list, because it unlocks the winback sequence that's already built
(`Marketing/Winback Email Previews/` — 8 emails, done, sitting there).

**2. The list is 17k but consent is a mess.** From `Houston Pedal Barge Contacts — Clean Backup.csv`:
- 16,963 unique emails
- **575** marked `Subscribed`
- **4,883** marked `No` (explicit opt-out — do not mail, ever)
- **11,504** blank / unknown

That list goes back to 2014. Blasting 17k cold addresses on a freshly-repaired domain is how you burn
the domain in one send. Spam complaints from a decade-old list will tank the sender reputation before
the winback sequence ever gets a chance.

**The right email plan when DNS clears:**
- Send to the 575 `Subscribed` first. Warm the domain.
- Then a re-permission wave to the 11.5k unknowns in batches of ~1,000/day, ramping. One email:
  "still want to hear from us?" with a hosted one-click unsubscribe (RFC 8058, URL form, no mailto).
- Suppress the 4,883 `No` permanently.
- Never mail the full 17k in one shot.

---

## What to do instead, ranked

### 1. Chase the FareHarbor DNS records (today)
Unblocks email, winback sequence, and the Faith Group campaign. Everything downstream waits on this.

### 2. Run the giveaway on Facebook
FB page has ~37k fans and giveaways are the ONE format with a proven ceiling here
(`Marketing/HPB Organic Analytics Readout.md`):
- 2022-03-01 giveaway: **45,640 engagements, 14.2k shares**
- 2022-02-03 giveaway: 13,208 eng, 9.5k shares
- IG all-time #1 (129 eng) was also a giveaway

**CORRECTED 2026-08-13.** This section was written off the vault's giveaway doc, which turned out to be
stale. The giveaway already ran on 2026-06-21 and got **9 engagements, 0 shares**. A Nov 2025 one got 5.
The 2022 giveaway numbers were launch-era and don't repeat. The real blocker is that the page has no
organic reach left (baseline 1-10 per post), so no mechanic saves it without paid seeding.

See `Marketing/HPB Giveaway v2 — Whole Boat (Aug 2026).md` for the reworked version and what the page
data actually says works (specificity and location, not the giveaway mechanic).

### 3. Push charters and groups, not seats
It's mid-August in Houston. Daytime heat kills walk-up demand and Texas schools go back in ~2 weeks,
which flattens weekday retail bookings. Charters don't care:
- **Faith groups** — campaign is already built (`Marketing/Faith Group Campaign/`, incl. prospect CSV)
- Corporate end-of-summer team outings
- Birthdays / bachelorettes (evening cruises, when it's 85 instead of 98)

Sunset and after-dark slots are the product to sell in August. Lead with "on the water at night,"
not "summer fun."

### 4. Google Ads
This is where the buying intent lives ("party boat houston," "booze cruise kemah," "pedal barge
near me"). **Could not audit — the Google Ads MCP is returning `UNSUPPORTED_VERSION` (v21 deprecated),
so the connector needs a version bump before I can see spend, ROAS, or wasted terms.** Flagging as
a fix-it, not a finding.

### 5. SMS — careful
The CSV has phone numbers and Twilio is connected. But TCPA penalties are far worse than CAN-SPAM,
and 11.5k of those numbers have no recorded consent. Only text the 575 opted-in, or people who
booked recently. Do not bulk-text the file.

---

## Also worth noting
`houstonpedalbarge.com` is **not in the Google Search Console account** (21 other sites are).
That's free data being left on the table and probably a 10-minute verification fix.

---

## Sequence

| When | Move |
|---|---|
| Today | Chase FareHarbor on the 3 DNS records. Verify HPB in GSC. |
| This week | Launch the FB giveaway with an opt-in entry form. Start Faith Group outreach. |
| On DNS clear | Winback to the 575. Then ramp the re-permission wave. |
| Ongoing | Fix Ads MCP, then audit Google Ads spend. Sell night cruises + charters through Labor Day. |
