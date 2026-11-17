# Gift Card Drip to Past Guests (Nov 17 to Dec 29, 2026)

**CURRENT STATUS (2026-11-15, verified today): built, tested, NOT sent.** Seven emails with A/B cells are built, one test of email 1 went to David, and nothing has gone to the list. The full-list send is blocked by the SES preflight (SES complaint rate 0.162% on Nov 16 against OUR gate of 0.05%, which is also over Amazon's 0.1% review line; bounce rate 2.75%, under both our 3% gate and Amazon's 5%; left over from the NKST send on Nov 6). Email 1 goes out the first weekday after David says go, earliest Tue Nov 17.

Preview: `preview/All 7 Emails.html` in this folder (self-contained, open it anywhere).
Style: the NKST "gift drip" look (Style Menu entry Designed Email): photo-led, calm serif, one button. Masthead is a text wordmark because the only logo on file is the Hot Spot award badge.

## The idea
Seven emails, about one a week, to past guests (4,632 mailable). No discount, no code, no price claims. The offer is the gift card itself. BBK's angle is Houston from the water: "there's nothing to do in Houston" is the most-wrong sentence in the city, so every email gives the buyer a way to prove it.

Because the guest list is mostly Houstonians and visitors who already paddled, the copy says "give someone what you did" and "nothing to ship," never "come back this weekend."

## Schedule
Calendar changed on Nov 15: today is Sunday, so email 1 slides to the first weekday after David's go. All seven still fit, no beat dropped.

| # | Send | Subject A | Subject B | Angle |
|---|---|---|---|---|
| 1 | Tue Nov 17 (earliest) | Give someone Houston from the water | A gift for someone who has enough stuff | Opener |
| 2 | Fri Nov 27 | We're not having a Black Friday sale | No doorbusters on the bayou | Deadpan no-sale |
| 3 | Thu Dec 3 | Know someone who says Houston has nothing to do? | For the person who's seen everything in Houston | Send a friend |
| 4 | Thu Dec 10 | For the person who's impossible to shop for | Three people on your list, one answer | Three people, one answer |
| 5 | Thu Dec 17 | No shipping deadline on this one | The gift that doesn't need a box | Nothing to ship, 3 steps |
| 6 | Tue Dec 22 | It's not too late | Forgot someone? Print this tonight | Last light, last minute |
| 7 | Tue Dec 29 | Unwrapped a bayou tour? | Winter is a good time to use it | Use it, or buy your own |

Email 7's main button goes to the Houston Skyline Kayak Tour page. Every other button goes straight to the FareHarbor gift card item.

## A/B test
Every email goes out in four groups of about 1,150: subject A or B crossed with hero photo A or B. Same copy and button in all four. Each address is hashed into a cell, reshuffled per email, one ledger so nobody gets two versions.

| # | Photo A | Photo B |
|---|---|---|
| 1 | Paddler toward the skyline, golden light | Skyline over a green bend, no people |
| 2 | Steps to the bayou, big clouds | Trees and clouds reflected, no people |
| 3 | Paddler on a board heading to the skyline | Kayaks on the bayou, evening |
| 4 | Concrete arch bridge and reflection | Dove mural along the bayou |
| 5 | Highway bridges and reflections | Allen's Landing dock and chains |
| 6 | Paddler silhouetted against a pink sunset | Kayaks under a soft evening sky |
| 7 | Skyline over a green bend | Paddler toward the skyline, golden light |

Only two subjects and two photos, not three, because this is the smallest list (about 4,600). With around 2,300 people per side and click rates near 1%, only a gap of about 40% or more between sides is a real result. Treat the first read as a lean, not a verdict.

## How to read results
- **Opens and clicks:** `cd ~/Projects/bbk-tools/newsletter-2026 && node ab-report.mjs em201-gift-houston-from-water` (reads CloudWatch, config set `bbk-campaign`). Opens run high because Apple Mail pre-loads images, so compare groups with each other only. Early clicks are mostly mail security scanners, so wait 3 days.
- **Sales:** FareHarbor, filter refs `gift_g01_aa` through `gift_g07_bb` (email number, then subject letter and photo letter). Subject winner = aa+ab against ba+bb. Photo winner = aa+ba against ab+bb. Gift sales per cell will be too few to judge alone.
- Carry the winning pattern (people vs no people, question vs statement) into later emails by swapping the A slot.

## What is wired (all verified 2026-11-15)
| Piece | Where |
|---|---|
| Sender | `Buffalo Bayou Kayak <info@buffalobayoukayak.com>`, domain verified and DKIM green in SES us-west-2. Replies go to BuffaloBayouKayak@gmail.com |
| Bounce and complaint notices | SNS topic `bbk-ses-events`, inbox feedback forwarding OFF (it was on) |
| Tracking | SES config set `bbk-campaign`, CloudWatch dimensions `campaign` and `cell` |
| Unsubscribe | Hosted one-click link, Lambda `bbk-unsubscribe` behind `https://ctbwza6y90.execute-api.us-west-2.amazonaws.com`. Tested GET, one-click POST and a bad token |
| Photos | S3 bucket `bbk-email-assets` (public read), 17 files, 8 to 170 KB each |
| Code | `~/Projects/bbk-tools/newsletter-2026/` (build.mjs, emails.mjs, send-ses.mjs, recipients.mjs, ab-report.mjs). Unsubscribe Lambda source in `~/Projects/bbk-tools/unsubscribe-lambda/` |
| Buy link | FareHarbor item 349459, the "Gift Card" item behind the Gift Cards link in the BBK site menu. `ref=gift_gNN_<cell>` and `full-items=yes` on every button |

### One deliberate difference from NKST: unsubscribes are BBK-only
The NKST and DCKT unsubscribe pages write to the account-wide SES suppression list, so a guest who opts out of one brand is silently blocked from every brand. For BBK, an unsubscribe writes to its own table (`bbk-unsubscribes`) and nothing else. `recipients.mjs` and `send-ses.mjs` both read it, and `send-ses.mjs` re-reads it right before a send. The flip side: people who already unsubscribed from NKST or another brand sit on the account-wide list and are skipped here too (3 BBK guests were affected).

## The list
Fresh FareHarbor pull on 2026-11-15, latest booking Nov 13.

| | Count |
|---|---|
| October 8 export (file on disk) | 4,172 |
| Fresh pull | 4,791 |
| GetYourGuide relay addresses dropped (cannot receive mail) | 156 |
| Unsubscribed or suppressed | 3 |
| **Mailable** | **4,632** |
| In the fresh list but not in the October file | 862 |
| In the October file but gone from FareHarbor's list | 315 |

The brief quoted 4,666 for October. The file on disk has 4,172 rows, so the comparison above uses the file.
FareHarbor has no "agreed to be emailed" field, so the list is every guest with an email minus opt-outs, same as past sends.

## Day-of runbook (when David says go)
1. `cd ~/Projects/bbk-tools/newsletter-2026 && node build.mjs && node recipients.mjs` (rebuilds the list and drops new opt-outs).
2. Dry run: `node send-ses.mjs --email em201-gift-houston-from-water --ab`. The preflight must say OK. It refuses if the SES account is unhealthy, bounce rate is 3% or more, complaint rate is 0.05% or more (our own gate, stricter than Amazon's), inbox feedback forwarding is on, or any relay address is on the list.
3. Send: `caffeinate -i node send-ses.mjs --email em201-gift-houston-from-water --ab --go`. One day, paced at 20 per second, retries on throttling. About 4 minutes for 4,632. The code lives on the laptop, so keep the lid open until it prints DONE.
4. Same day: sweep the BBK inbox (BuffaloBayouKayak@gmail.com) for bounces, out-of-office and replies, then run `ab-report.mjs` for sent, delivered and bounce counts.
5. Read results 3 days later.
For emails 2 to 7, change the key to the email's slug (`em202-gift-no-sale`, `em203-gift-nothing-to-do`, `em204-gift-three-people`, `em205-gift-no-shipping`, `em206-gift-last-light`, `em207-gift-your-seat`).

## Open items
- **Send is blocked by the SES preflight.** SES complaint rate 0.162% (Nov 16) against our gate of 0.05%. Amazon's own lines are: under review at complaint 0.1% or bounce 5%, may pause at 0.5% or 10% (checked against the AWS docs 2026-11-16). SES still reports the account HEALTHY even though the complaint figure is above 0.1%, so it is close to Amazon's line, not just ours. Bounce rate is 2.75%, fine. Both are left from the NKST Nov 6 send and fall slowly as newer mail dilutes them. Options: wait for the rate to fall, send in smaller waves of the most recent guests, or David says skip-preflight. Do not skip without his word.
- **Confirm three gift card facts.** BBK's site and FareHarbor page say nothing about expiry, delivery speed or which tours a card redeems on. The copy therefore says only "you choose the amount, they pick the day, good toward any tour we run" and "the gift card comes to your email." Once confirmed, add "never expires" and "right away" back (they are the strongest NKST lines).
- **Logo.** The only logo on the site and in the vault is the Hot Spot Winner award badge. The masthead is a text wordmark. Swap in a real logo if one exists.
- **Guests in two photos.** Email 3 photo B and email 6 photo B show guests far away on the water. Both photos already run on the BBK site and in carousels. Swap them for faceless shots if David prefers.
- **Season photos.** Most photos are summer shots (blue sky, green trees). The copy makes no seasonal claims beyond "cool air" in email 7.
- Houston Pedal Barge shares the Houston guest base. Its drip and this one can hit the same inbox in the same week.

## Not in this drip (on purpose)
- Discounts, codes, free add-ons, prices, countdowns.
- Safety or difficulty promises. The only audience statement is "all ages," taken from the tour page.
- SMS: separate opt-in list, separate approval.
