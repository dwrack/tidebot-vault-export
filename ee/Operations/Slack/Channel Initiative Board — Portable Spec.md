# Channel Initiative Board — Portable Spec

Drop this file into any vault. It tells Claude how to build and maintain a Slack canvas initiative board for every channel in that workspace.

## The problem it fixes

Slack channels accumulate ideas, not commitments. Symptoms: no clear action items, no ownership, no deadlines, no assets attached, nowhere to discuss a thing that stays attached to the thing, and no visible link between initiatives that depend on each other.

Root cause: a channel is a stream and a canvas is a document. Neither has a per-item record. Fix the record and all six symptoms close.

## The rules

- One owner per row. Never two, never "the team."
- Next action is a verb someone does this week, not a goal.
- Discuss in the row's linked thread, not loose in channel.
- No owner and no date sends it to the Parking Lot. Don't hide it, drop it down.
- Walk the board top to bottom in a standing 15-minute meeting. Weekly.
- The board holds pointers, never the work itself.

## The format

One canvas per channel, pinned to the channel's canvas tab.

**Header**
```
Rules
- One owner per row. Never two.
- Next action = a verb, done this week.
- Discuss in the linked thread, not in channel.
- No owner + no date = Parking Lot.
- Walked top to bottom, <day>, 15 min.
```

**Active table**

| Initiative | Owner | Next action | Due | Assets | Thread |
|---|---|---|---|---|---|

- **Initiative** — 2-4 words. The thing, not the sentence about the thing.
- **Owner** — one first name. Append `?` if it's a proposal awaiting confirmation.
- **Next action** — under 8 words, starts with a verb.
- **Due** — a real date, or `Weekly` for standing work.
- **Assets** — link or short pointer to where the work lives. `—` if none exists yet, and that's usually a finding.
- **Thread** — permalink to one permanent Slack thread for that initiative.

**Parking Lot table**

| Item | Status |
|---|---|

Header line above it: `No owner, no date. Claim one or it stays here.`

## How Claude builds one

1. Pull the channel's last 60-100 messages plus any existing canvas.
2. Pull the vault for staged plans, trackers, and drafts that belong to that channel's domain. Anything written and never shipped is an initiative, not a document.
3. Extract every commitment, open question, and unshipped plan. Collapse duplicates.
4. Propose an owner from who has actually been doing that work in-channel. Mark every proposal with `?`. Never invent an owner silently.
5. Assign dates. Near-term work gets this week or next; anything vaguer than two weeks out belongs in the Parking Lot.
6. Sort Active by owner so each person sees their block.
7. Everything without both an owner and a date goes to the Parking Lot with a one-line status.
8. Report back: rows created, which owners are guesses, and any row whose owner is leaving or overloaded.

## Gotchas learned the hard way

- Thread links can't be generated in advance. Building the board means posting one stub message per initiative and pasting permalinks back, which floods the channel. Get approval before posting stubs.
- Count rows per owner before you finish. One person holding five rows is a single point of failure, and it's the thing the board exists to make visible.
- If an owner is leaving, say so next to their rows. Their rows are the ones that break silently.
- Cancelled tools and dead accounts get removed from the board and stamped dead in memory the same day. Otherwise the board and reality drift.
- Resist writing status prose into the board. If a row needs a paragraph, the paragraph goes in the thread.

## Cadence

- Monday, 15 minutes, walk it top to bottom.
- Owner says the next action and whether the date holds. Nothing else.
- Anything that needs discussion goes to its thread and the meeting moves on.
- Rebuild the board from scratch monthly. Boards rot faster than they get edited.
