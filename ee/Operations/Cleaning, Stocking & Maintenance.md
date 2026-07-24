# Cleaning, Stocking & Maintenance — Facilities Ops
*Started 2026-07-18. This is the working doc for the three offload areas Davey flagged: cleaner visibility/pay, supply stocking, and where maintenance items live.*

## Cleaning

- **Current cleaner:** Maria — contact saved as "Ebb and Ember Sauna Cleaning." Maria doesn't appear to text directly; messages get relayed through someone at +1 (503) 703-4735 who said "let me ask my mom," so that's likely her kid.
- **Group chat:** "Ebb & Ember Sauna Cleaning" (started 6/20/26, Jonah + that number).
- **Before Maria:** Chris cleaned through ~6/18/26 at a cadence described as "every 3 days(ish), before and after weekends." Before Chris: Addie (Mar–Apr).
- **Reference checklist:** [Ebb and Ember Cleaning reference](https://docs.google.com/document/d/1tmqE4k94FfGicOk0fKosD-jY1NXeEcamAnAtMnSzxRk) — Jonah shared this with Maria on 6/20. It already has a Date / Time In / Time Out / Signature tracking table and a required "Damage & Issue Reporting" section with a "Report to / Text # / Email" field.
- **The actual gap:** the tracking table and report-to fields have been blank since Addie left in April — Chris's rows never got filled in either. That's the real reason there's no visibility into which days anyone's actually gone. The system already exists, it's just not being used.
- **Payment gap:** Jonah sent a payment request to `mgmg150215@gmail.com` on 7/13; as of 7/15 he still hadn't been able to pay. Method/platform needs fixing, separate from the schedule problem.

## Stocking

- **Owner (per Davey, 7/18/26):** the cleaner should be the one refilling soap, paper towels, toilet paper, shampoo/conditioner during each visit — but someone still has to keep the *product* itself stocked so there's something to refill from.
- **Known incident:** ran out of soap on 6/20/26 even though a full 1-gallon bottle existed elsewhere on site. The gap wasn't the product, it was that supply *location* isn't documented anywhere.
- The reference checklist above already has "Supply Locations & Inventory Check" and "Supplies running low or missing" fields — also never filled in.
- **Open:** no par levels, no designated product buyer, no single documented storage location.

## Maintenance / Fix Log

New items from Davey (7/18/26), merged into `Operations/Todo.md` under Medium/Low Priority so they live in the one list already fed by Slack `#the-helm` / TideBot:

| Item | Bucket | Note |
|---|---|---|
| Ball at top of interior sauna door is broken | Medium | |
| Water line to sauna broken, needs hose | Medium | |
| Remove water thing in sauna | — | Already in Todo.md: "Remove water dispenser from sauna or label it clearly, replace with better solution in lounge" |
| Add spigot | Medium | Location TBD |
| Storage closet clean out | Medium | |
| Reconnect door to WiFi + solve battery draining issue | Medium | |
| Rearrange cameras for new sauna layouts | Medium | |
| Remove interior bathroom door | Low | |
| Better shower curtain | Low | |
| Automated lighting for everything | Low | Bigger project — scope/budget before starting |

⚠️ **Flag:** a lot of existing Medium-priority items in `Operations/Todo.md` are tagged owner **(Dustin)** — plunge pod costing, shower diagnosis, vanity switch, sauna light lock, sauna vents. Given Dustin resigned in March and is mid-buyout, he's probably not a live owner for hands-on fixes anymore. Worth reassigning before they sit forever.

## Next steps

- [ ] Confirm Maria's actual cadence and get the tracking table in the reference doc actually filled in going forward
- [ ] Fix the payment method (the 7/13 email request stalled)
- [ ] Fill in "Report to" contact + supply storage locations in the reference doc
- [ ] Decide who buys/restocks the physical product (Jonah? Davey?) — cleaner can only refill from what's on hand
- [ ] Reassign (Dustin)-tagged items in Todo.md to real current owners
- [ ] Mirror this into a Google Sheet for Jonah — couldn't auto-create a blank Sheet via the Drive API from here (400 error on `files.create` with the Sheets mimetype). Fastest fix: Jonah or Davey creates one blank Google Sheet and shares the ID, then it gets populated in full.
- [ ] Wire into Slack `#the-helm` once elevatedtidesebbember.slack.com is connected

---
*See also: `Operations/Todo.md` (master facilities list), `Operations/Jonah — Sauna Items March 30 2026.md`*
