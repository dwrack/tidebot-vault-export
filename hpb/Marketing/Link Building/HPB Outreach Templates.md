# Houston Party Barge - Link-Building Outreach

Companion to `HPB Backlink Prospects.csv` (110 prospects). This doc holds the SEO anchor map
and the actual email copy being sent. The sending machinery lives in
`.ses_campaign/outreach_emails.py` + `outreach_sender.py` + `outreach_recipients.json`.

## How it sends

- **Channel:** Amazon SES, us-west-2, from `info@houstonpedalbarge.com`, from-name
  "David at Houston Party Barge", reply-to `houstonpedalbarge@gmail.com` (the watched inbox).
- **Look:** plain personal note, no hero image or marketing button, so it reads as 1:1 B2B.
  Every email carries the HMAC one-click Unsubscribe + the Seabrook physical address (CAN-SPAM).
- **Pace:** batches, ~4 sends/sec. Batch 1 = 5 (sent 2026-06-07), then ~15 per batch.
- **Run it:**
  - `python3 outreach_sender.py preview --start 0 --count 5` (render, no send)
  - `python3 outreach_sender.py send --start 5 --count 15` (next batch)
  - logs land in `.ses_campaign/outreach_send_log_*.json`

## SEO anchor-text map

Lead with "party boat" language (June 2026 brand). Anchors are **mixed** across prospects so the
backlink profile looks natural, never the same exact-match phrase 56 times.

| Prospect type | Anchor text used | Target URL |
|---|---|---|
| DMO / chamber / city / marina | "Houston Party Barge", "Clear Lake party boat", "things to do in Seabrook" | homepage |
| Hotel concierge | "Kemah boat tours", "things to do near the Kemah Boardwalk" | homepage |
| Restaurant / bar (route) | "Houston Party Barge", "Clear Lake party boat" | homepage |
| Things-to-do blog / press | "BYOB party boat on Clear Lake", "things to do in Seabrook" | homepage |
| Bachelorette / wedding | "bachelorette party boat in Houston", "Houston bachelorette boat cruise", "private boat charter on Clear Lake" | /houston-party-barge-cruise/ |
| Corporate / team-building / DMC | "corporate team building on the water in Houston", "Houston group activities" | /corporate-group-event/ |
| Cross-promo vendor (limo/photo/DJ) | "private boat charter on Clear Lake", "things to do in Seabrook" | homepage or /houston-party-barge-cruise/ |

Target URLs (verified live 2026-06-07): homepage `https://houstonpedalbarge.com`,
`https://houstonpedalbarge.com/houston-party-barge-cruise/`,
`https://houstonpedalbarge.com/corporate-group-event/`.

## The 7 email templates (one per prospect type)

Each email = personalized opener (per prospect) + the body below + signature + footer.
Full copy is in `outreach_emails.py`; the shape of each:

- **local** (DMOs/chambers/cities/marinas): "we're a Coast Guard certified BYOB party boat out of
  Seabrook, add us to your local lineup, link to {url} ({anchor}), here's a comp sail."
- **hotel**: "on-the-water option a few minutes from your desk, add to your area guide, comp sail
  for your concierge crew."
- **restaurant**: "we launch on the same waterfront, our groups need somewhere to eat, trade links."
- **blog_press**: "story idea, photogenic summer-on-the-water angle, comp media sail + photos."
- **bachelorette**: "private 26-person charter ~$800-950, include us in your Houston content."
- **corporate**: "private charter = easy team-building day, add to your Houston group-activity list."
- **vendor**: "natural cross-referral, we send people your way, you mention us, link swap."

Subjects carry the prospect's name so no two are byte-identical (deliverability), e.g.
"Story idea for CultureMap: a BYOB party boat on Clear Lake".

## Status / next actions

- **Batch 1 sent** (2026-06-07): Visit Seabrook, Visit Bay Area Houston, Visit Houston,
  Clear Lake Area Chamber, BAHEP. 5/5, 0 failures.
- **51 emailable queued** (`Method = email`, `Status = QUEUED` in the CSV): send in batches of ~15
  once batch-1 deliverability looks clean.
- **10 VERIFY-first**: medium-confidence emails (Houstonia, Texas Monthly, Thrillist, chron.com,
  Wedding Chicks, The Bash, Meeting Tomorrow, Friendswood, Bach Babes, Free Fun in Houston). Confirm
  the address on the org's own page before adding to a send batch.
- **36 FORM-only**: real link targets with no emailable contact (most NASA-area hotels, several
  bachelorette/wedding/vendor sites). These need a manual form submission, not an email. David
  chose to skip auto-submitting directories, so these sit as a do-it-yourself follow-up list.
- **8 NONE**: no contact surfaced (mostly route bars reachable only by phone/FB). Worth a call given
  how close they are to the dock (Cabo Clear Lake is literally next door at 2513 E NASA Pkwy).

## Tracking replies

Replies hit `houstonpedalbarge@gmail.com`. As links get placed, update the prospect's `Status` in
the CSV to "LINKED" so we can measure the campaign.
