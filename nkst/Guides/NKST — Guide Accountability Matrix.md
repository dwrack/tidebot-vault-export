# NKST — Guide Accountability Matrix
*Created: July 2026*

> One page that answers: what does every guide owe us, how do we know it happened, who checks, and what happens when it doesn't. The audio tour logs and the GHL 3-question text already exist. What's new here is the **photo proof layer** for van cleaning and PFD care, and a single consequence ladder so enforcement isn't ad hoc.

The design principle, for classification reasons: we verify **results** (clean van, hung PFDs, gas in tank), never methods. A photo of the outcome is the cleanest possible proof of a result. See [[Legal/Guide Role — Outcome-Based Classification Rationale]].

---

## The Photo/Video Proof System (New)

Two short videos and two photos, dropped in the same Slack thread as the post-tour audio log. Takes about 90 seconds with a phone. Slack timestamps and archives everything automatically, so there's no separate log to maintain.

**Post-tour proof set (every tour):**

| # | Proof | What it proves |
|---|---|---|
| 1 | Video (10-15 sec): pan of van interior from the rear or side door, floors and seats visible | Van cleaned, no trash, no guest items left |
| 2 | Photo: PFDs hung on the rack, MiraZyme bottle somewhere in frame | PFDs hung to dry and sprayed |
| 3 | Video (5-10 sec): dashboard showing fuel gauge and no warning lights on; guide reads odometer aloud | Gas level documented, no warning lights, mileage recorded |
| 4 | Photo: locked gate/container at Piety St | Base secured |

Video for 1 and 3 because a still can't prove the full interior is clean or that the dash is clear of warning lights; a quick pan can.

**Pre-tour protection footage (conditional):** If you arrive and the van or gear is NOT in the condition the last guide's proof claimed, film it and flag it in Slack before you touch anything. That clears you and puts it on the right person. If you don't flag it at pickup, the condition is on you at drop-off. This is the same rule every rental car company uses, and it's what makes the whole system self-enforcing.

**Why this and not just the audio log:** the audio log says "van's clean, PFDs hung." The footage shows it. Insurance, guest-damage disputes, and guide-to-guide handoffs all get resolved by the picture, not by memory.

---

## Per-Tour Accountability

| # | Obligation | Standard (the result we require) | Proof | Where it lives | Reviewed by |
|---|---|---|---|---|---|
| 1 | Night-before guest contact | Every guest texted with meet time, location, guide phone # | Audio log 1 mention; guest complaints are the failure signal | Slack | Ops manager, weekly |
| 2 | Pre-tour vehicle + gear check | Tires, lights, trailer unlocked, 15 PFDs, first aid, tow rope | Audio log 1 (pre-tour) | Slack | Ops manager, weekly |
| 3 | Waivers confirmed before launch | 100% signed, zero exceptions | FareHarbor manifest | FareHarbor | Ops manager, spot check |
| 4 | Tour delivered to standard | Safety briefing, PFDs on all guests on water, group together | Guest reviews, audio log, incident record | Google/FareHarbor reviews | Ops manager, monthly |
| 5 | Van cleaned | Interior trash-free, floors clear, nothing left behind | **Video 1** (interior pan) | Slack thread | Ops manager, weekly |
| 6 | PFDs cleaned + hung | All PFDs on rack, MiraZyme sprayed, none left in van or trailer | **Photo 2** (PFD rack) | Slack thread | Ops manager, weekly |
| 7 | Gas + mileage | Topped off at Shell (code 6006) or flagged why not; odometer captured | **Video 3** (dash: gas, no warning lights, odometer read aloud) + audio log 3 | Slack thread | Ops manager, weekly |
| 8 | Base secured | Van, container, gate locked | **Photo 4** (locked gate) | Slack thread | Ops manager, weekly |
| 9 | Post-tour audio log | Recording 3 submitted before leaving Piety St | Slack timestamp | Slack | Ops manager, weekly |
| 10 | Damage/incident reporting | Verbal report immediately, written within 24 hours | [[Operations/Post-Tour Vehicle & Equipment Damage Report]] | Slack + vault | Ops manager, same day |

**Payment link:** per ICA Section 2.3, the tour log is due within 48 hours to trigger payment. The proof set (2 videos + 2 photos) is part of the tour log (see [[Legal/ICA Exhibit B — Equipment Care & Photo Documentation]]). No log + proof set, payment for that tour holds until they're in. Not a fine, not a penalty, just the documentation that releases the invoice.

---

## Recurring Accountability (Beyond Per-Tour)

| Cadence | Obligation | Proof | Owner |
|---|---|---|---|
| Weekly | Respond to rotating check-in question (relationship, not compliance) | GHL reply | Ops manager |
| Weekly | Ops manager reviews all photo threads + audio logs, clears or flags each tour | Weekly summary table | Ops manager |
| Monthly | Deep-clean rotation: assigned guide does full van vacuum/hose-out + PFD inspection for wear (buckles, straps, fading) | Photo set + note in Slack | Ops manager assigns |
| Quarterly | Gear count audit: PFDs, paddles, first aid restock, merch box | Inventory count vs. [[Operations/Vehicle Checklists]] | Ops manager |
| Annual | CPR cert current, DL clean, ICA + acknowledgement re-signed, insurance cert | [[Guides/Guide Roster & Compliance Tracker 2026]] | Ops manager |
| Annual | Retraining day completed | [[Guides/Annual Retraining Cycle]] attendance | Owner + ops manager |

---

## Weekly Review (Ops Manager, Monday)

Scan every tour thread from the week. Each tour gets a ✅ or a flag. The whole review should take 15 minutes, because the proof is sitting in the thread.

| Item | This week |
|---|---|
| Tours run | |
| Tours with complete proof set (4/4) | / |
| Tours with post-tour audio log | / |
| Gas confirmed topped | / |
| Flags raised (dirty handoff, damage, missing gear) | |
| Guides with an open miss | |

Claude can generate this from the Slack channel weekly. Anything flagged twice by different guides (same van issue, same gear problem) goes to the Open Issues Log in [[Operations/Vehicle Accountability Log]].

---

## Consequence Ladder

Kept simple on purpose. The tone with guides stays casual, the ladder itself does not bend.

| Step | Trigger | What happens |
|---|---|---|
| 1. Nudge | First missed proof set or log | TideBot/manager text same day: "Hey, missing your post-tour videos/photos from today, can you confirm the van and PFDs got done?" |
| 2. Conversation | Second miss within 30 days | Ops manager calls. Not a write-up, a conversation. Find out what's in the way. |
| 3. Payment hold | Log/photos not in within 48 hours | That tour's payment holds until documentation is in (ICA 2.3). Automatic, no drama. |
| 4. Scheduling hold | Third miss in 30 days, or an unflagged dirty handoff caught on the next guide's photos | Guide can't claim new tours until current. Manager tells them directly. |
| 5. Termination | Pattern continues, or any safety-critical miss (waivers skipped, PFDs not worn, DUI-class event) | ICA Section 17.2, immediate for cause |

Safety-critical items (waivers, PFDs on guests, impaired operation) skip straight to step 5 territory. Cleaning and documentation misses walk the ladder.

---

## Who Owns What

| Role | Owns |
|---|---|
| Guide | Doing the work, proving it happened (photos + audio), flagging problems at pickup instead of inheriting them |
| Ops manager | Weekly review, nudges, conversations, scheduling holds, deep-clean rotation assignments |
| Owner (David) | Ladder steps 4-5, ICA changes, hearing appeals if a guide thinks a flag is wrong |
| TideBot | Reminders before/after tours, confirming logs received, first-miss nudge |
| Claude | Weekly summary from Slack, pattern flags across guides/vans |

---

*Related: [[Operations/Guide Tour Log]] · [[Operations/Vehicle Accountability Log]] · [[Legal/ICA Exhibit B — Equipment Care & Photo Documentation]] · [[Guides/NKST — Guide Onboarding Matrix]]*
