---
type: build-plan
business: New Orleans Kayak Swamp Tours
status: PLAN, nothing changed on the live job yet. Double-checked + worst-case pass 2026-10-19.
created: 2026-10-19
builds_on: Operations/24-Hour Under-Minimum Check — Build Spec (2026-10-13).md
code: davids-mbp-2 ~/Projects/fareharbor-brief/thin-check/
---

# Thin-Departure Ladder v2

## Where it stands today (verified live 2026-10-19 on mbp-2)
- `thin.mjs` (finds thin departures, 9:45am + 3pm) and `send.mjs` (upsell ladder +$65 → +$30 → free, reply classifier) run daily in dry mode. **Zero texts ever sent.**
- **The Google Voice send path has never worked on that Mac.** The DCKT missed-call bot it was copied from ran for 4 minutes on Oct 13, Google signed it out, and it has been unloaded since. 0 texts sent. The kayak profile (`profile-nkst`, account info@neworleanskayakswamptours.com, line 504-571-9975) was never created.
- FareHarbor rebooking is manual. Weather isn't built. Jeff still owes the cutoffs.
- FH dashboard cookie (Oct 9) still reads fine. Its auto-refresh job log has been silent for 58 days.

## Worst cases found (from the code, the last 7 days of real plans, and 13 years of GV history)

### Would have hurt a real guest or the business
| # | Scenario | Evidence | Fix |
|---|---|---|---|
| 1 | **Cross-swap.** Two thin departures each get offered the other one. Both say yes, they trade places, and both departures are still thin | Oct 18 plan: Toni (combo, 2) offered the Extended; Daria (Extended, 1) offered the combo | Plan the whole day as one problem: pick ONE target departure, everyone moves toward it, never in both directions |
| 2 | **Downgrade sold as upgrade** + blank price ("It's $ more") | Toni, Oct 18 | Target must be longer AND pricier; refuse to send any text with an empty price |
| 3 | **Texting a stranger.** A UK/foreign number stored without its country code gets a "1" added and is treated as a US number | Code only checks digit count, ignores the booking's country field. 2 GB/ES guests in the last week | Only text when country = US AND the number is a valid US mobile |
| 4 | **Morning-of texts land after the boat leaves.** The schedule runs on the Mac's Pacific clock | "7am day-of" tick fires 9am CT, after the 8am/9am tours | Fix the schedule to CT |
| 5 | **Leaving one guest stranded.** Party A (2) takes the upgrade, Party B (1) already got "you're all set as booked." Now B is solo, under minimum | Ladder treats each guest alone and promises "keep it as booked" | Re-score the departure after every move; never promise "as booked" unless the departure is confirmed to run |
| 6 | **"Spot held for you" that isn't** | `move` r3 template says it; nothing holds capacity | Check live capacity before every offer and again before every rebook; drop the "held" wording |
| 7 | **Shuttle guests moved to a time with no van** | Shuttle ($25) is a common add-on; Jeff's 9am "no transportation" setup | Never auto-move a booking with the shuttle add-on; Jeff only |
| 8 | **OTA bookings (Viator/TripAdvisor, GetYourGuide)** | Daria was a Viator booking. Their money is collected by the OTA, phone may be a relay | No upsell charges and no auto-rebook on OTA bookings; free moves go to Jeff with the OTA rebook steps |
| 9 | **Misreading replies** turns into a wrong FareHarbor action | Classifier: "Sure, cancel the 2pm and put us on the 9:30" reads as REFUND; "we fly out Monday" reads as RESCHEDULE; "I can't wait!" reads as NO and triggers a cheaper offer | Auto-rebook only on a clean, short yes to the exact offer. Everything else goes to a human |
| 10 | **No opt-out handling** | "STOP" currently classifies as unclear and the ladder continues | STOP / unsubscribe / wrong number = stop forever, no further texts |
| 11 | **Free upgrade given to someone who never answered** | Rung 3 goes out on silence | Fine as an offer, but no FH change until they reply yes |

### Would break the system
| # | Scenario | Evidence | Fix |
|---|---|---|---|
| 12 | **Google signs the bot out** (the most likely failure) | Happened to the DCKT bot within 3 minutes. JT loop on the NPB line hits passkey re-auth regularly | Run GV inside the real signed-in Chrome bridge (like the JT loop) instead of a separate bot profile. Check sign-in at 9:30am every day and Slack if dead, before the 10am texts are due |
| 13 | **Losing the main business number.** Google Voice terms don't allow automated messaging; the 571-9975 line has 13 years of guest history | Policy risk, no incident yet | Hard cap of ~10 automated texts/day, human-like pacing. If Google ever warns, move automated sends to the Twilio number (already registered for the review texter) and keep GV for humans |
| 14 | **Two runs at once** crash on the shared browser profile | DCKT log: "ProcessSingleton" crash Oct 13 | Lock file: a tick that finds another running exits quietly |
| 15 | **Reply parser never tuned.** Detecting "this message came from the guest" in GV's page was never tested (`--dump` exists, never run) | Code comment admits it | Tune on our own test threads in the lab before any guest |
| 16 | **Jeff texts the guest himself from his cell** and the bot texts too | Bot only sees the GV thread | Slack ✋ reaction on a guest = bot stops for that booking |
| 17 | **Overnight gap.** Guest replies at 10pm about an 8am tour; next tick is morning, too late | Ladder last tick 9pm | Add a 6am CT reply check; anything unresolved for a tour before 10am pings Jeff by 6:15am |

### Lessons from 13 years of GV threads (Voice Data Analysis doc)
- **The damaging weather failure is silence, not cancelling.** Guests who showed up or called after a cancelled tour with no notice. Weather-cancel notices must go to every channel (text + email) and confirm delivery.
- **Most rain cancels are unnecessary.** Guests see rain and cancel; we paddle in light rain. Weather texts should reassure by default and only offer a move above Jeff's cutoffs.
- **Reschedule/modify is the #1 inbound reason, forever.** Expect replies like "can we add a person" or "move to Saturday." Those go to a human, not the classifier.
- **Address confusion lasted years** (405 Frenchmen vs 740 N Rampart). Confirmation texts pull the meeting point from one config field, never hardcoded.
- **Staff already did this by hand** ("not enough participation for our 4 hour extended tour tomorrow, Monday morning extended or a 2 hour tomorrow morning?"). Brian's 2025 wording is a good template source along with Jeff's.
- **Wrong-brand callers exist** (NPB/other-tour confusion on this line). Unclear replies go to a human.

## What v2 adds (unchanged from the first draft, now with the fixes above baked in)
1. **GV texting** through the signed-in Chrome bridge, daily sign-in check, ~10/day cap.
2. **FareHarbor auto-rebook** via the dashboard's internal API (Public API has no writes). Endpoint captured once on a test booking. Verify-after-write. Auto only for: free move, clean yes, direct booking, no shuttle, capacity confirmed. Everything else goes to Jeff in Slack with the link.
3. **Weather if-this-then-that** from the free NWS forecast for Manchac. Slack-only until Jeff gives cutoffs. Cancel notices go out on every channel.
4. **Alarms**: GV signed out, FH cookie dead, plan file missing by 4pm, rebook failed. Each one posts to Slack. Caps: 10 texts, 10 rebooks a day. `config.send` kill switch.

## Rollout
- **Phase 0, lab (no guests):** fixes #1-#17, test allowlist of our phones, one test booking in FH. Full loop: thin found → text → reply → rebook → confirm → verify. Also scripted replies through the classifier (the 30 nastiest real-world replies) before it touches a guest.
- **Phase 1, shadow:** real guests, every text and rebook staged in Slack, Jeff ✅. 1-2 weeks.
- **Phase 2:** auto free moves for direct bookings. Daily digest.
- **Phase 3:** paid upgrades, only after a test booking proves how FH charges the difference.

## Needs from David / Jeff
- Sign in the kayak GV (info@neworleanskayakswamptours.com) in a Chrome bridge profile on mbp-2, Screen Sharing, ~2 min.
- Jeff: weather cutoffs, plus his reschedule texts (Brian's 2025 text is a fallback).
- OK to use the Twilio review-texter number as the fallback sender if GV is down?
- Test allowlist phone numbers.
