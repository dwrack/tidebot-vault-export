# Why NPB Leads Ghost — OpenCX Data

*Pulled live from the OpenCX API on 2026-08-28. 986 sessions, 2026-05-30 through 2026-08-28. Every number below is counted from actual transcripts, not estimated.*

---

## The shape of the problem

| Channel | Sessions | Ghosted (our message was last) |
|---|---|---|
| Messenger | 626 | 610 (97%) |
| Email | 199 | 145 (73%) |
| Instagram | 71 | 63 (89%) |
| Web chat | 90 | 59 (66%) |

**59% of all sessions are one message and gone.** 582 of 986 guests sent exactly one message, got an answer, and never spoke again. Not "went quiet after negotiating." One message.

**Only 24% of everyone who has ever contacted us is reachable off-platform.** Strip out the email channel (where an address comes free) and it collapses: of 787 Messenger, Instagram, and web sessions, 26 have a phone and 24 have any email. That's about 6%. Everyone else evaporates the second the Meta window closes.

---

## Five causes, in order of how much they cost us

### 1. The bot is a vending machine for a rate card

44% of first AI replies contain a dollar figure. Someone types "How much" and gets this back, cold:

> Public tour tickets are $63 per person. Private charters are flat-rate: Bayou Boogie $900 (up to 18), Party Queen $1,100 (up to 22), Freaky Tiki $1,250 (up to 25), Twerkin Tiki $1,250 (up to 25). For private charters, the deposit is $350 and the remaining balance is paid the day of the trip. What date are you looking at, and how many people?

Four boat names, five prices, a deposit policy, and a two-part question, before we've said one thing about what actually happens out there. $1,250 with no story attached is just a big number. 33% of the one-and-done guests asked about price, and this is what killed them.

### 2. Every reply ends in a chore

"What date and how many guests?" is a form. It gives the guest homework and gives them nothing back. That is the single most common closing line in the corpus and it is the last thing most of these people ever read from us.

### 3. We almost never ask for contact info, and asking demonstrably works

- Bot asked for a phone in **15%** of sessions. Asked for an email in **2%**.
- When it asked for a phone: **12%** capture. When it didn't: **2%**.

Six times better, and we do it one time in seven. Worse, when I read the sessions where we actually have a number, most of them are people who volunteered it unprompted off a Meta lead form. The bot didn't earn those. It just caught them.

### 4. The automated nudges are loud, fast, and one of them is a total zero

We send **3.21 automated messages per session**, and in 607 of 986 sessions the robot nudges outnumber the real conversation.

| Nudge | Sent | Replies |
|---|---|---|
| "Are you still there?" (3-min) | 781 | 68 (8.7%) |
| Session close-out messages | 632 | 16 (2.5%) |
| **5-step booking follow-up drip** | **1,703** | **0 (0.0%)** |

That drip has now sent seventeen hundred messages and generated **not one reply**. Zero. Here's why:

> "Hi! Just circling back on your party booking inquiry, did you get a chance to look at the details we sent?"
> "Wanted to check back in, anything holding you up on the booking?"
> "Popular dates tend to fill up fast, if you'd like me to hold something tentative while you decide..."

That's generic SaaS drip copy in a party boat DM. It smells like a robot from the first four words, so nobody reads past them.

And the timing is desperate: **94% of nudges fire within 10 minutes of the guest going quiet. Median is 3.3 minutes.** Someone reads a price, puts their phone down to talk to their friend, and 3 minutes later we're going "are you still there?"

### 5. Zero personality

There is not one funny line in 1,678 AI messages. Every response reads like a rate sheet PDF. We sell a BYOB party boat full of bachelorettes on a bayou with alligators in it, and the copy sounds like a dental office confirming an appointment.

The Nolan voice already exists in `Sales Agent Identity & Playbook.md`. **It is not what's running.** The live OpenCX prompt opens with "You are a customer support agent" and tells the bot to avoid emojis and stay professional. We wrote the good version and never shipped it.

---

## What that adds up to

We pay ~$2.83 to start a Messenger conversation. We then answer it like a price API, ask for homework, poke it three minutes later, and drip five corporate messages at it. Then the 24-hour Meta window shuts and the lead is legally unreachable forever, because we never got a phone, an email, or an opt-in.

The fix isn't a better closing line. It's a slower, funnier conversation that trades value before it asks for anything, and that always walks away with a way to reach the person again.

See: [[OpenCX Agent Prompt v2 — Nolan]] and [[OpenCX Nudge Sequence v2 — Slow Burn]]
