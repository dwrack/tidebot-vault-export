# LinkedIn Corporate Outreach: Playbook

Started 2026-10-12. Sender: Davey's personal LinkedIn. Engine: `~/Projects/linkedin-outreach` on the always-on Mac (davids-mbp-2), brand config `brands/ee.json`. Runs 7am Pacific, Mon-Fri. Apify bills to the Ebb & Ember account only.

This file is the brain. The daily job reads it before it writes anything, so edit here to change how the drafts sound.

## The one rule

Every message has to be useful to the reader even if they never book. If a draft only makes sense as a sales pitch, it doesn't go out.

## How it runs

1. **Find:** 5 new people a weekday, alternating days between the Portland metro and Vancouver/Clark County WA, rotating through the segments below. Duplicates, out-of-market people and anyone on the Do Not Contact list get dropped.
2. **Draft:** Claude reads each profile, picks a segment and a give sized to their company, and writes a connection note (200 characters max, no pitch, no link) plus a follow-up for after they accept.
3. **Deliver:** the batch lands in `Daily/YYYY-MM-DD.md` in this folder. No Slack.
4. **Send:** Davey sends from his phone and ticks the boxes under each person in that day's note:
   - `[x] sent` = connection request sent
   - `[x] accepted` = they accepted. The follow-up shows up in the daily note 2 days later.
   - `[x] follow-up sent` = the follow-up went out
   - `[x] replied` = they replied. The engine stops nudging and the conversation is yours.
   - `[x] booked` = it turned into a booking
   - `[x] skip` = never show this person again
   Tick boxes in any old daily note. The next morning's run picks them up.
5. **Track:** `Tracker.csv` here mirrors the engine's tracker after every run. Don't edit it, it gets overwritten. Change status by ticking boxes.
6. **Report:** Friday's note opens with a scorecard: sent, accepted, replied, booked, for the week and all time.

Nothing ever sends automatically. LinkedIn restricts accounts that automate sending, and a bot voice is exactly what we're avoiding.

## Hard limits

- 5 new requests a day, 25 a week. LinkedIn starts flagging around 100 a week.
- 2 messages max without a reply: the connection note, then one follow-up. Then stop. No "just bumping this."
- No links in the connection note. In the follow-up, one link at most, and only to something useful (ebbandember.com).
- Never name past guests or say who booked. "A few people from your industry come out on weekday mornings" is fine. Names are not.
- Brand name is always "Ebb & Ember," with the ampersand.
- Never say the sauna is wood-fired. Don't mention fuel at all.
- Never call it "a float" or "the float." It's the sauna, or the session.
- No health claims. No "reduces cortisol," no "boosts immunity," no "heals." We don't promise feelings. "People usually leave quieter than they came in" is about as far as it goes.
- No wellness buzzwords: transformative, healing journey, unlock, optimize, biohack, self-care.
- Don't quote the draft corporate package prices ($749 team block, $150 host, etc.). They aren't approved yet. Use list prices below or say "I'll send numbers."

## Facts the drafts can use

- Portland's floating sauna, on the Columbia River at the Elevated Tides marina in North Portland (173 NE Bridgeton Rd). Opened January 1, 2026.
- For Vancouver, WA people: we're directly across the river, about 10-15 minutes from downtown Vancouver over the I-5 or I-205 bridge, free parking. There's no floating sauna or river plunge on the Washington side. Say "Vancouver, WA" so nobody thinks BC.
- The cold plunge is the river itself. Around 42 degrees in winter, 60-65 in summer. It's always optional; you can sit on the ladder or skip it.
- Sessions are 1 hour 45 minutes: heat, cold, rest. Open 7am-9pm daily.
- Private session, the whole sauna is yours, up to 10 guests: $449 off-peak (Mon-Thu, Fri before 5pm), $539 peak. That's about $45 a person off-peak.
- Social session, shared, up to 8 guests: $49 a person off-peak, $59 peak.
- Sunrise session at 6am and Moonlight session (9-10pm) are $39.
- Memberships run $99 to $299 a month (3-month minimum).
- Groups bigger than 10 rotate through back-to-back private sessions.
- No alcohol on the sauna dock.
- Weekday mornings and early afternoons are wide open. Evenings and weekends book up.

## Segments and what we give each one

Company size decides the give. A 6-person design studio and a 2,000-person hospital system want completely different things.

### 1. HR, benefits and people-ops leads (any size)
They're buried in burnout surveys and wellness stipends nobody uses.
- **Give:** a free intro session for their wellness committee or benefits team. Four to six of them come out on a weekday morning, see it, decide if it fits. No proposal attached.
- **Bigger give:** a one-page "recovery perk" sheet they can drop into a benefits deck: what a session is, what it costs per head, how a team block works.
- **Ideas to offer:** quarterly team recovery mornings, a corporate membership pool (a handful of passes the whole team shares), a burnout-prevention offsite that isn't a conference room.
- **Angle:** "Most wellness perks are an app nobody opens. This is two hours where nobody can check Slack."

### 2. Small teams, 2-15 people (fits one private session)
Founders, office managers, studio leads, small law and design firms, agencies.
- **Give:** the math. A private session off-peak is $449 for up to 10, about $45 a head. Less than a round of drinks and an appetizer, and nobody's hungover Friday.
- **Ideas to offer:** after-work reset instead of happy hour, closing a project, a new-hire welcome, a client thank-you.
- **Timing hook (Oct-Dec):** the holiday party that isn't another restaurant back room.

### 3. Mid-size companies, 50-500 people
People ops, office managers, ERG leads, internal comms.
- **Give:** a ready-made monthly "wellness day" rotation: one weekday morning a month, teams take turns, 10 at a time. HR gets a recurring perk without planning anything.
- **Ideas to offer:** employee perk passes (discounted social seats for staff), a benefits-fair pop-up table with a session raffle, department rotations through back-to-back privates.
- **Angle:** one invoice, a schedule they can forward, and a perk people actually use.

### 4. Connectors: referral partners
Hotel concierges and front desk managers, corporate retreat and offsite planners, gyms and climbing gyms, physical therapists, chiropractors, athletic trainers, massage studios, running clubs.
They send people somewhere every week. One good relationship beats 20 cold leads.
- **Give:** make their recommendation easy and good. A one-pager with what to tell clients, how to book, what to bring. For PTs, trainers and gyms: a free session for their staff so they can speak to it firsthand.
- **Bigger give:** a partner code for their clients or guests (Davey approves rates and codes).
- **Angle for PTs and trainers:** "Your clients ask where to do contrast therapy outside a clinic. This is the river version." Keep it about the experience, never a medical claim.
- **Angle for concierges and planners:** "When a guest asks what's actually Portland, this is an easy yes."

### 5. Physical-work and safety cultures
Construction, trades, healthcare (nurses, ER, OR teams), first responders (fire, police, EMS), warehouse and logistics.
They work hard on their feet and get thanked with pizza.
- **Give:** a crew recovery morning. A private session on a weekday, timed after a night shift or a big pour.
- **Ideas to offer:** shift-end sessions (Sunrise at 6am fits night shift), a station or unit appreciation day, Moonlight sessions for swing shift.
- **Lead with safety:** trained host on every session, river entry is optional and supervised, "when in doubt, don't go out" is a real rule. Safety managers care about this first.

### 6. Sales and high-stress teams
Sales leaders, account execs, BD, agency partners, finance.
- **Give:** a client-entertainment alternative to dinner and drinks. A private session for them and a client, then coffee. It's the meeting the client remembers.
- **Ideas to offer:** quarter-close reset for the team, a client morning instead of a steakhouse night, a deal-signing session.
- **Angle:** "Two hours with a client and no phones beats a three-hour dinner where everyone's checking email."

## Personalization signals, best first

1. **Something they actually posted** in the last 30 days.
2. **New role** in the last 90 days ("congrats on the move to X").
3. **Company news:** an expansion, a new office, an award, a wellness initiative.
4. **Their headline or about section.** Use one specific detail and never flatter.
5. **Shared Portland detail:** their neighborhood, a local org they're part of.

If there's no real hook, the note stays short and plain. A fake compliment is worse than none.

## Voice

The drafts should sound like Davey texting someone he respects:
- Short, contractions, a little imperfect. One idea per line.
- No "I hope this finds you well," no "I'd love to pick your brain," no "synergy," no em dashes, no double dashes, no exclamation marks.
- One specific detail about them and one small ask: "worth a look?", "want the one-pager?", "want me to hold a morning for your committee?"
- Open with their name, end when done. No sign-off flourish.

Connection note example (shape, not a script):
> Hi Sam, saw the Hillsboro office expansion. I run Ebb & Ember, the floating sauna on the Columbia. Would be good to be connected.

Follow-up example:
> Thanks for connecting. A lot of people-ops folks I talk to say the wellness stipend mostly goes unused. If it's useful, I'll host your wellness committee for a free weekday morning session, 4 to 6 people, no pitch. Want me to hold one in November?

## Open decisions (Davey)

- Partner codes for concierges, PTs and gyms: what discount, and is there a referral payout? Drafts say "partner rate" until this is set.
- Free intro sessions for wellness committees: how many a month, and which mornings?
- Corporate membership pool: do we offer it at all, and at what price? Drafts only float it as an idea until this is set.
