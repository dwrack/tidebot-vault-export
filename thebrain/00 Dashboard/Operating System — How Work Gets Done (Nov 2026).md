---
type: operating-standard
created: 2026-10-30
status: agreed with David 2026-10-30 (grill session), live Nov 1
review: Sunday weekly review; re-cut Jan 5
---

# Operating System — How Work Gets Done

Decided 2026-10-30 after the grill. The diagnosis, from David's own vault: 22 of 32 active projects stalled at "waiting on David's yes"; 1,604 staged drafts; the last thing that shipped end to end shipped because of an **outside deadline**. So the system is built on three facts: David's yes is the bottleneck, external clocks finish things, and Claude's output outruns decisions by about 50 to 1.

---

## 1. WIP limit: three projects in flight, portfolio-wide

Not per brand. Three. Starting a fourth means killing one in the Sunday review. Everything else is **Queued** (next up, with a trigger) or **Parked** (needs a season or an event).

### In flight now (through Nov 15)

| # | Project | Done when | Ship date | External clock (who is told the date) |
|---|---|---|---|---|
| 1 | **NOLA hire** — captain / assistant manager for NPB + NKST | offer accepted | Nov 20 | Posting live **Tue Nov 3**. Michael books 2 phone screens **Thu Nov 5**. Jeff told the job isn't replacing him before posting. |
| 2 | **DCKT off-season build** — Astro site swap + 2027 early-bird | doorcountykayaktours.com served from Cloudflare AND Dec 1 gift-card email scheduled with SES smoke test passed | cutover wk of **Nov 9**, email locked **Nov 24** | Dec 1 send date is fixed (gift season). Lea told the cutover week. GoDaddy + Cloudflare access is David's only hands-on step. |
| 3 | **Bike Bar sale** | deposit in hand, term sheet signed, Bob Draught has cleared the tax read | deposit by **Nov 15** | Michael gets the four questions **Mon Nov 2** (buyer name, 1 or 2 bars, what's included, who gets proceeds). Term sheet 48 h after his answers. |

Rule for all three: **missed ship date = kill-or-recommit at the next Sunday review.** No silent slide.

### Queued (next in, in order, when a slot opens)
1. NKST tracking fix + paid restart (ads dark since Oct 7)
2. NPB off-season: missed-call text-back live + site variant swap
3. Texas tracking (HPB GA4 purchase action, BBK server-side Meta event)
4. HBC Google Business Profile verified (was due Sept 30)

Everything else: see the Parked list in [[Project Portfolio — Priority & Season Map (Nov-Dec 2026)]].

---

## 2. Standing authorizations (Claude acts, tells David after)

Agreed 2026-10-30: **"Do it, but money stays with me."** Claude does the following without asking and reports it in one line in the daily digest. David vetoes after the fact; he does not pre-approve.

**Authorized, no yes needed**
- Reply to 5-star reviews (brand voice, no promises, no names).
- Answer OpenCX leads and handoffs from the published FAQ and prices; anything off-FAQ gets staged.
- Archive sessions with no "done when" or no activity in 14 days; archive superseded routine runs.
- Move a project file to Parked when it has had no dated movement in 60 days, with a one-line trigger (David said "not yet" to the 22-file batch on 10/30, so that batch waits for his word; the rule applies from Nov 1 forward).
- Prune the Project Kanban "This Week" list to 15 cards on Sunday, moving the rest into the brand's FDE report with a link back.
- Send the Monday Helm number and the standing weekly posts.
- Re-title sessions to the `[BRAND] Project — done when X` form.
- Fix broken tooling (token re-auth, API version bumps, scrape lockouts) and say what was stale until the fix.

**Still David's yes (money, people, name, irreversible)**
- Any ad spend change: pause, raise, lower, new campaign. Claude stages the exact change and the number; David taps.
- Refunds, credits, write-offs, loans, wires, checks.
- Hires, pay, schedules that change someone's hours.
- Anything outbound in David's name or to a partner (Michael, Jonah), a vendor, an attorney, a guest with a complaint.
- Deleting data, DNS changes, site cutovers (the go, not the prep).
- Anything that is the first of its kind.

---

## 3. One decision slot a day

Decisions arrive in **one morning tap, max 3**, through the existing decision system (one Slack DM + the DJL Morning Digest page, per the 10/17 rule). Each decision carries a **standing default** that fires if David skips it two mornings in a row. Decisions do not travel in Slack threads, session prose, or Kanban cards.

**Physical-world and money items go to the top of the tap** (keys, checks, notices, meters, insurance). Digital waits. The Piety water ran five days because the digital stack got read first.

### Queue for the next mornings
Live queue (wired 2026-10-31): `00 Dashboard/Daily Digest/Decisions Queue.md`. The 5:45am chief-of-staff run reads it with `decision-queue.py today --commit`; add a decision by appending a row (id, day, kind, options rec first, default). The table below is the seed copy.

| Day | Decision | Default if skipped twice |
|---|---|---|
| Sat Nov 1 | D1 Post the captain/assistant-manager role (Indeed, FB, Craigslist) | post Tue Nov 3 |
| Sat Nov 1 | D2 Send Michael the Bike Bar four questions | Claude drafts, David sends Mon |
| Sat Nov 1 | D3 DCKT Astro swap go / no-go | hold, recheck Nov 7 |
| Sun Nov 2 | D6 HPB June 6 refund ($927, policy backs it) | no default, money |
| Sun Nov 2 | D5 BBK Meta awareness pause + HPB Followers Reboost pause (~$990/mo, 0 purchases) | no default, money |
| Sun Nov 2 | D7 NKST lead guide, Stephanie vs Michelle | Stephanie (data: 8 tours, 5 review mentions) |
| Mon Nov 3 | D4 Better Loans $190k | no default, money |

---

## 4. Daily close: 10 minutes, phone, end of day

The only weekday "organizing" that happens. Three ticks:
1. What shipped today (Claude lists it; David reads).
2. Anything in flight with no movement in 7 days (Claude flags; David says kill or keep).
3. Tomorrow's 3 decisions previewed so he can sleep on them.

## 5. Sunday is the only maintenance window

The weekly review (already a skill) now ends with four mechanical steps:
- Archive every session without a "done when" or with 14 days of silence.
- Prune the Kanban to 15.
- Kill-or-recommit any in-flight project that missed its ship date.
- If a slot opened, promote the top Queued item and tell the person who owns its external clock.

Nothing gets reorganized Monday to Saturday.

---

## 6. Sidebar and titles (the small part)

- Sections stay by brand in season order (set 10/30). The **title is the system**: `[BRAND] Project — done when X`. David finds things by scrolling titles, and managers will mirror the convention.
- Hard cap: 3 live project sessions in the whole panel, matching the WIP limit, plus pinned HQ. Chats are fine but get archived Sunday.
- Routine runs never get their own row (the app nests them).

## 7. What David personally does

Only this: the morning tap, the daily close, two phone screens on Nov 5, the GoDaddy/Cloudflare login the week of Nov 9, and the Bike Bar text to Michael. Everything else on this page is Claude's or a captain's.

## 8. How we'll know it works (check Nov 15)

- At least 2 of the 3 in-flight projects hit "done when."
- Fewer than 20 live sessions in the panel.
- Kanban under 15 cards for two Sundays running.
- The Tier-0 decision list is at or under 3 items, not 7.

If none of those are true on Nov 15, the WIP limit drops to 2 and the authorization list grows. The problem will be the bottleneck, not the organization.
