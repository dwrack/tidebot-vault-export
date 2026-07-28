# Contract Review — Team Packet
*How Jeff, JT and Michael review the Captain + Deckhand contracts using their own Claude Desktop.*

---

## The Rule

**Nobody edits the files.** David holds the master.

- Two people writing to the same Obsidian file in iCloud silently clobbers one of them. It's happened before.
- Reviewers read, answer their scoped questions, send the answers back.
- David merges. One version, always current, nobody guessing which copy is real.

---

## What Each Person Owns

| Person | Owns | Deliverable back |
|---|---|---|
| **Jeff** | Rates + logistics | Priced rate card, claim-gate decision, open `JEFF:` callouts answered |
| **JT** | Marina reality check | Does the line-item list match what crew actually do at the dock |
| **Michael Fischer** | Classification | 1099 posture, Jones Act / LHWCA, the unpaid-training flag |

---

## How They Open the File (send this to Jeff and JT)

1. Open **Finder** → the shared **NOLA Party Barge** folder
2. Go into the **SOPs** folder
3. Find the file for your review (named below)
4. Open **Claude Desktop**, start a new chat
5. **Drag the file straight into the chat window**
6. Paste your prompt from below and hit send

That's it. No setup, no plugins, no account changes. Claude reads the file you dropped in.

> If dragging doesn't work: click the **paperclip** in Claude Desktop and pick the file that way.

---

# JEFF — Rates + Logistics

**Files to drag in (both):**
- `Exhibit A — Captain Pay Schedule.md`
- `Exhibit A — Deckhand Pay Schedule.md`

**Prompt to paste:**

```
I'm the ops manager for NOLA Party Barge, a party boat tour company in New Orleans. We run 4 boats out of a marina in Jean Lafitte with about 14 crew, captains and deckhands, all 1099 contractors.

I've attached two pay schedules we're about to put in front of crew. Every dollar amount is blank. My job is to price them.

Interview me one question at a time. Don't dump all the questions at once, and don't move on until I've actually given you a number.

For each line item, ask me:
1. What we pay today for that work, if anything
2. What I think it should be worth
3. Whether the unit is right (per tour, per day, per occurrence, per weekend)

Push back if a number seems off relative to the others. A turnaround clean shouldn't be worth more than running a trip. Flag it if I do something inconsistent.

At the end, give me:
- A clean filled-in rate card table, both roles, ready to paste back
- A "cost per boat per Saturday" estimate so I can see what a 3-trip day actually costs us
- Any line item I priced in a way that'll cause an argument with crew

Two other things I need to decide, ask me about these last:
1. Claim gate: should deep cleans, boat moves and fuel runs be PRE-authorized in writing before the work happens, or should crew log it and I approve at the pay run? Give me the tradeoff, then let me pick.
2. Whether there should be a weekend lead premium at all, or if that line comes out.
```

**Also send Jeff back:** the open `JEFF:` callouts still sitting in both ICAs (Culture Quiz, who can sign off a captain besides him, Tidebot live status, backup coverage when a boat-assigned deckhand calls out, the Routes SOP question).

---

# JT — Marina Reality Check

**Files to drag in (both):**
- `Exhibit A — Captain Pay Schedule.md`
- `Exhibit A — Deckhand Pay Schedule.md`

**Prompt to paste:**

```
I run daily operations at the marina for NOLA Party Barge, a party boat company in Jean Lafitte, Louisiana. I'm the guy on the ground every day. I know what crew actually do because I watch them do it.

I've attached two pay schedules. We just split crew pay into separate line items instead of one flat rate. I need to check it against reality before it goes to crew.

Interview me one question at a time. You're trying to find work that falls between the cracks.

Walk me through a real day at the marina in order, and at each step ask:
- Does this work have a line item on the schedule?
- If yes, is it in the right bucket, and is the trigger written the way it actually happens?
- If no, what is it and roughly how long does it take?

Specific things I want you to press me on:
- Opening prep vs turnaround vs closing. Are those the right three boundaries, or is there work that doesn't fit any of them?
- What happens on a day with two boats going out and one crew covering both?
- Rain delays, late groups, a group that shows up 40 minutes late. Who's getting paid for that waiting time under this schedule?
- Trailering, launching, hauling out. Is that happening, and is it covered?
- Anything crew already complain about not getting paid for.

At the end give me a short list, in plain language, of:
1. Work that has NO line item and needs one
2. Line items where the trigger is written wrong compared to how it really goes
3. The one thing most likely to cause a fight on payday

Keep it short. I'm not writing a report, I'm sending this to the owner.
```

---

# MICHAEL FISCHER — Classification

**Files to send:** both ICAs and both Exhibits.

Michael isn't doing a Claude interview, he's giving a legal read. Send him the docs with this note:

> Michael, before we put these in front of crew I need your read on classification. Four flags I already know about, plus whatever I'm missing:
>
> 1. **Unpaid mandatory training.** Orientation, shadow trips and ride-along coaching are all written as unpaid. I know that's the weakest point under an economic-realities review. It's marked `MF:` in both docs. Tell me if it has to change.
> 2. **Jones Act.** Captains likely qualify as seamen under the Chandris test no matter what the ICA calls them. Does the itemized per-deliverable structure move that at all, or is it irrelevant to the analysis?
> 3. **LHWCA.** Deckhands working shore-side on and near vessels in navigable waters. What's our real exposure and what insurance closes it?
> 4. **Direction and control.** We moved deckhands off a flat shift fee to per-trip plus per-day line items specifically to strengthen the 1099 posture. Does that actually help, or is the level of operational direction in the SOPs the thing that decides it regardless of how we pay?
>
> Hold-harmless, IP and indemnification are still placeholders marked `LEGAL:`. Those need the maritime attorney, not you, but flag anything you see.

---

## After the Reviews Come Back

1. David merges everything into the vault master
2. Rates go into both Exhibit A files
3. Michael's changes go into the ICA bodies
4. Maritime attorney does the final pass on the `LEGAL:` placeholders
5. Then, and only then, DocuSeal

---

## Messages to Send

**To Jeff (text or Slack):**

> Hey, need you on the crew contracts this week. I split the pay into separate line items so people get paid for what they actually do instead of one flat number that covers everything. Every dollar amount is blank and pricing them is your call.
>
> Two files in the shared NOLA Party Barge folder, SOPs subfolder: Exhibit A Captain Pay Schedule and Exhibit A Deckhand Pay Schedule.
>
> Easiest way: open Claude Desktop, drag both files into a new chat, paste the prompt I'm sending you next. It'll walk you through pricing one line at a time and spit out a filled-in table.
>
> Don't edit the files themselves, just send me the numbers back. Can you get me that by Friday?

**To JT (text):**

> Hey, quick one. We rewrote how crew get paid: instead of one flat rate for the day, every piece of work is its own line item. Opening prep, turnaround, closing, boat moves, all separate.
>
> You're the one who actually sees what crew do all day, so I need you to tell me what we missed. Two files in the shared NOLA Party Barge folder under SOPs, both start with Exhibit A.
>
> Open Claude Desktop, drag them in, paste the prompt I'm sending. It'll walk you through a normal day and find the gaps. Takes 15 minutes.
>
> Don't edit the files, just send me the list back. Mainly looking for work that doesn't have a line item yet.
