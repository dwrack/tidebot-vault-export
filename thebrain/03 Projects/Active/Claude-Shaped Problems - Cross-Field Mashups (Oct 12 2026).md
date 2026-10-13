# Claude-Shaped Problems: Cross-Field Mashups for DJL (Oct 12 2026)

Source: Science, Oct 2026, "Problems in 22 scientific fields had solutions hiding in plain sight. An AI has found them." Underlying post: Matthew Schwartz (Harvard physicist, visiting at Anthropic), "Claude-shaped science," Anthropic blog, Oct 1 2026. Tooling: BootLoops, open source, github.com/BootLoops-ai.

## What the article actually says (30 seconds)

- One physicist plus Claude produced 36 preprints across 18-22 fields in about 3 months, from ~400 candidate problems.
- The trick was not smarter math. It was noticing that the SAME equation shows up in unrelated fields. A collider-physics integral turned out to be the Bayesian evidence integral ecologists and geneticists had been stuck on for 20-30 years. Nobody had both skill sets in one head.
- Schwartz calls these "Claude-shaped problems": a problem in field A that a known technique from field B already solves, if anyone in A knew B existed.
- Setup: one Claude Code session per problem on cloud VMs, a master session handing out compute and validating, subagents writing intermediate results to markdown, and a separate adversarial "referee" session that tries to break every result.
- Results were "technically correct but boring" until a domain expert said what their field actually cares about. Humans supplied taste; Claude supplied breadth and grind.

## The lesson for you

You are the domain expert with 12 businesses' worth of taste. The barrier you keep hitting is not more marketing tactics (the growth play bank already has 22). It is that your problems are being solved with marketing tools when several of them are actually airline, hospital, call-center, or sports-analytics problems with mature solutions.

Your version of "the same equation in a different field":

| Your problem (field A) | Who already solved it (field B) | Technique | Data you already have |
|---|---|---|---|
| Slots that run half empty Tue-Thu, sell out Sat, same price | Airlines, hotels (revenue management) | Booking-curve / pickup forecasting + fences (lead-time, day-of-week, party size) | FareHarbor bookings: created date vs trip date, per slot, 3+ seasons |
| "Is this guide actually good or do they just get sunny Saturdays?" | Sports analytics (plus-minus, Elo) | Residual rating: review score minus what weather, group size, slot, and season predict | FH manifests + reviews + weather history |
| When to text a past guest so they rebook | Medicine, insurance (survival analysis) | Kaplan-Meier / hazard curve of time-to-second-booking; send at the hazard peak, not at 12 months | FH customer email history across years |
| Which ad set / brand gets tomorrow's dollars | Clinical trials (adaptive design), casinos | Thompson-sampling bandit across ad sets, auto-shifting budget to what is converting this week | Google Ads + Meta MCP data, already pulled daily |
| Where to aim ads, which hotels to pitch for concierge referrals | Retail site selection (Huff gravity model), epidemiology | Catchment map from guest zip codes weighted by drive time; rank hotels/neighborhoods by expected yield | FH customer zips, hotel lists |
| Guide schedules eat manager hours (Connor) | Hospitals (nurse rostering), airlines (crew pairing) | Constraint solver (Google OR-Tools, free) with availability, certs, max hours, fairness | Current schedules, TIPS cert tracker, availability texts |
| Weather cancels: refund vs credit, and what a "rain guarantee" should cost | Reinsurance, weather derivatives | Expected-loss pricing from historical cancel rate by month and brand | NOAA history + FH cancel log |
| NPB guest never hears about NKST, and vice versa | Amazon (collaborative filtering), grocery (market basket) | Cross-brand overlap + next-best-offer per guest | FH customer emails across all brands (same files that built the Meta custom audiences) |
| Dock check-in crush at the 2pm launch | Call centers, Disney (queueing theory) | Little's law: stagger start times or add one check-in lane for a 10-minute window | Check-in timestamps or a week of counting |
| Twelve brands forecast separately | Walmart/M5 competition (hierarchical forecasting) | Reconcile brand forecasts to a portfolio total so staffing and ad budget come from one number | Existing FH Forecast reports per vault |

## Ranked: where to break a barrier first

Ranking weighs: data already in hand, dollars, and whether it needs a new platform (none of the top 5 do).

| # | Mashup | Why first | Barrier it breaks | Effort |
|---|---|---|---|---|
| 1 | Booking-curve pricing (airline RM) | Biggest dollars. Every FH brand. FH supports custom pricing per availability. | Flat pricing on a perishable product | 1-2 wks |
| 2 | Guide plus-minus rating | Managers want it, fits the staff-comms goal, coaching gets objective | Reviews read as luck or vibes | 1 wk |
| 3 | Rebook hazard curve | Feeds the Guest Reactivation drips drafted today; replaces the guessed 12-month anniversary | Timing by calendar instead of by behavior | 3-4 days |
| 4 | Bandit ad allocation | The "apply" layer the /google-ads loop is missing | Weekly manual budget shuffling | 1-2 wks |
| 5 | Zip-code catchment map | Cheap, visual, instantly changes ad geo + hotel pitch list | Guessing where guests come from | 2-3 days |
| 6 | Guide scheduling solver | Hands Connor hours back | Spreadsheet scheduling | 1-2 wks |
| 7 | Weather actuarial | Makes growth play #1 (credit-over-refund) a priced policy | Policy set by gut | 3 days |
| 8 | Cross-brand recommender | NOLA and TX have 2+ brands each | Brands sold in silos | 1 wk |
| 9 | Hierarchical forecast | Upgrade of what exists | Twelve numbers nobody adds up | 1 wk |
| 10 | Check-in queueing | Ops, small | Dock crush | 2 days |

## How to run it (borrowed from BootLoops, sized for DJL)

- **One session per problem, one master.** Master allocates, tracks, and never does the math itself. Each problem gets its own folder under `03 Projects/Active/Mashups/<name>/` with `PLAN.md`, `RESULTS.md`, and the scripts.
- **Success criteria written before any code.** Example for #1: "a per-slot price table for NPB Nov-Dec with projected revenue change, backtested on 2025 bookings, no slot with under 60% projected fill at the new price." Vague wins ("good agreement," "done with one asterisk") get rejected.
- **Referee pass before David sees it.** A separate session gets the result cold and tries to break it: leakage, cherry-picked window, wrong join. Only what survives reaches David.
- **Show the plot.** Every result ships with one chart David can eyeball in 10 seconds. No chart, no result.
- **Reproduce something known first.** Before claiming a new finding, the pipeline must reproduce a number David already knows (e.g., last September's NPB revenue) from the same data.
- **Tools get kept.** Each problem leaves a reusable script (FH loader, weather joiner, review joiner). Later problems start faster. This is the compounding part and the real payoff.
- **David supplies taste.** Each result gets the "would an operator shrug at this?" test. If yes, reframe before polishing.

## What Claude should take from this (honest)

Schwartz's failure-mode list reads like David's feedback memory:

- "Declared victory early" = the purchase pixel being called broken for months after it was fixed. Fix: verify live, show the number, date it.
- "Grinds instead of building tools" = the quota-burn rig that made 1,604 unreviewable drafts. Fix: build the loader once, reuse it.
- "Loses context after compaction" = re-asking things David already settled. Fix: PLAN.md and RESULTS.md as the source of truth, consolidated every session.
- "Calls a 3-day task a 2-year campaign" = the recap habit. Fix: one line, done, path.
- "Conclusions can be wrong even when the calculation is right." Fix: the referee session, every time.

## Week 1 proposal

Day 1-2: build the shared FH loader (bookings + customers + cancels, all brands) and the weather joiner. Reproduce a known monthly revenue number per brand.
Day 3-5: Mashup #1 on NPB (longest booking history, year-round). Backtest, chart, referee, deliver.
Day 5: Mashup #5 (catchment map) as a quick second win from the same loader.
Week 2: #2 and #3, which share the review + customer joins.

Status: prep only. Nothing built yet. Waiting on David to pick the starting problem.

---

## Second input: "Below the Frontier" (Kevin Zhang, Eastwind, Oct 2026)

Source: eastwind.substack.com/p/below-the-frontier-the-battle-for

### What it says (30 seconds)

- **Bounded vs unbounded tasks.** Unbounded work (coding, research, trading) always benefits from a smarter model. Bounded work (extract this field, draft this reply, format this report) needs a fixed level of intelligence and no more. Frontier labs keep the unbounded revenue; the much larger bounded market will run on cheaper and local models.
- **2x2: where the model runs x where the data lives.** Cloud model + local data (today's desktop agents) is the transitional quadrant: destructive local edits with no rollback, erratic apps, prompt injection, "work stalls when the laptop lid closes." The durable quadrants are cloud+cloud (sandboxed VMs, versioning) and local+local once local models are good enough.
- **Intelligence sovereignty.** Proprietary models refuse some requests, so serious users route those workloads to models they control.
- **The "Switzerland layer."** Whoever owns the neutral layer that routes work between local and cloud models, and across devices, wins the knowledge-work market. Interface ownership has decided every prior platform shift (Microsoft with the GUI, cloud SaaS over desktop).

### How it reads against DJL

The fragility list is your incident log, item for item: the laptop sleeping through night-shift runs (Sept 19), the bind-mounted DocuSeal SQLite zeroed in a low-memory event (Sept 23), the migration bundle that silently dropped one 4KB file and blinded FareHarbor for a week (Aug 3), Michael's Claude writing his paths into a synced `.mcp.json` and breaking 5 servers for 19 days. You already answered half of it by moving the loops to the always-on Mac. The other half is versioning and routing.

The upside: you already own your Switzerland layer. The harness is Claude Code + the vault + ~27 MCPs + the skills folder, and Night Shift proved the same harness runs on Qwen by pointing `ANTHROPIC_BASE_URL` at Ollama. BootLoops makes the same point from the science side: the harness is model-agnostic, the model is a plug-in. Neither article thinks the moat is the model.

### The routing rule this gives us

Every loop and every skill gets a label. This replaces the "Haiku / Sonnet / Opus" guess in the model-routing section of CLAUDE.md with a criterion.

| Label | Test | Runs on | Examples in the fleet today |
|---|---|---|---|
| **Bounded** | A smarter model would not change the output | Local Qwen first, Haiku as fallback | review-watch reply drafts, GBP post drafts, caption batches, reddit draft gate, OpenCX handoff classification (new/money/angry), review mining into the VoC bank, vault audit, report formatting, alt text, FH report tabulation |
| **Bounded, outbound** | Same, but it touches a customer or a live system | Local drafts, human tick, then post | GBP replies, review SMS, win-back sends |
| **Unbounded** | More intelligence keeps finding more | Frontier (Opus/Fable), David in the loop | the 10 mashups above, pricing, ad strategy, anything in David's voice, legal/money/people, deciding what a result means |

Two consequences:
1. **The mashup track is frontier work by definition.** That is where the token spend belongs. The bounded fleet should cost close to nothing.
2. **Night Shift is on the wrong machine.** It runs on the laptop that sleeps. The 2015 Intel Mac cannot run a 27B model. The DCKT guide Mac is Apple Silicon (it already runs Qwen-Image via mflux) and never sleeps, so it is the natural home for the bounded fleet. RAM on that box needs checking before committing.

### Actions added to the plan

- **A1. Label the loops.** One pass over the ~59 launchd jobs on mbp-2 and the ~40 skills: bounded / bounded-outbound / unbounded. Output: a column in `00 Dashboard/Automation Roadmap.md`.
- **A2. Move bounded drafting to local.** Start with the ones already proven on Qwen (GBP replies, reddit drafts, review mining). Target host: DCKT Mac, pending a RAM check. Keep Haiku as the fallback when Ollama is down.
- **A3. Version the vaults.** Nightly git snapshot of each vault on mbp-2 (local repo, no remote, no secrets) so a bad edit by any session has a rollback. This is the "versioning" half of the durable quadrant.
- **A4. Sovereignty list.** Note which tasks have hit classifier refusals or quota walls (Schwartz hit this with biology; Night Shift exists partly for bulk/private work). Those route local by default.
- **A5. Keep skills model-agnostic.** No skill should assume a model name. Already mostly true; make it a rule in CLAUDE.md.

### One-line synthesis of both articles

Breadth and grind are cheap and getting cheaper. Taste, verification, and owning the harness are the parts that stay valuable. Spend frontier tokens only where a smarter answer changes the decision, and run everything else on metal you own.

---

## Third input: "Deno joins Cloudflare" (Cloudflare blog, Oct 9 2026)

Source: blog.cloudflare.com/deno-joins-cloudflare

### What it says (20 seconds)

- Ryan Dahl (Node, Deno) and Bert Belder join Cloudflare. Their job: make self-hosting the Workers runtime (`workerd`) a first-class path, by merging in Dahl's `celld`: one Rust binary, object storage as its only dependency, that runs the Workers + Durable Objects model anywhere.
- Durable Objects = a single-threaded object paired with its own SQLite database. The platform handles placement, routing, and storage. Dahl calls it "simple yet incredibly powerful." Cloudflare admits workerd's self-hosted Durable Objects were toy-grade until now.
- Varda's lock-in rebuttal: the open runtime is the same code as production, and customers have already left Cloudflare using it. Translation: this is a safe platform to build on because the exit exists.

### How it reads against DJL

This is an infrastructure signal, not a barrier-breaking idea. It matters because of where the first two inputs landed: run bounded work on something durable you control, version everything, and treat the model as a plug-in.

Today the bounded fleet is ~59 launchd jobs on a 2015 Intel Mac. The failure classes are all host problems, not logic problems: missing venvs after migration, iCloud TCC blocking Python, a laptop that sleeps, a watchdog that shared a venv with the thing it watched. Cron Triggers + Durable Objects is the architecture that deletes that whole class: each loop becomes an object with its own SQLite state, the platform wakes it, and "the machine was asleep" stops being a failure mode. You already run one thing this way (the IG story-reshare engine on Workers), and the domain migration to Cloudflare is booked for late November.

The honest limit: Workers cannot touch the iCloud vault, the Chrome bridge, iMessage, or Ollama. Anything that needs a Mac stays on a Mac. Zhang's line about labs wanting to own the data layer applies to you in miniature: the iCloud Obsidian vault is your data layer and your weakest link (sync conflicts, TCC, Michael's machine writing into it). A Worker writing to R2/KV with a Mac syncing results down is the clean split.

### Actions added

- **A6. Split the fleet by host need** during the A1 labeling pass: (a) API-only jobs that could run as Workers (review-watch, opencx-watch, seo-watch, ad report, meta-token-refresh, loop-watchdog, keyword monitors), (b) Mac-bound jobs (vault writers, Chrome bridge, FH scraper, iMessage, Night Shift on Ollama).
- **A7. Fold the decision into the November Cloudflare migration.** DNS move first as planned, then pilot ONE group-(a) loop as a Worker with a Durable Object (loop-watchdog is the right first candidate: it is the smoke detector and it should not live on the thing it monitors).
- **A8. Watch celld.** If Cloudflare egress or per-request costs ever matter, the self-host path lands the same code on mbp-2. No action now; recheck when the merged workerd ships "in the coming months."

### Synthesis across all three inputs

| Input | Lesson | DJL move |
|---|---|---|
| Claude-shaped science | Breadth + grind are cheap; taste + verification are the human job; the harness compounds | Mashup track with a referee pass, reusable loaders |
| Below the Frontier | Bounded work goes local/cheap, unbounded gets frontier; own the routing layer; versioning and always-on compute | Label the fleet, move bounded drafting local, nightly vault git snapshots |
| Deno joins Cloudflare | Durable, self-hostable state machines are becoming the default way to run small always-on logic | Pilot one loop as a Worker + Durable Object during the Nov migration |

---

## Fourth input, the clincher: "Fingerprints are the new cookies" (royfish.dev, Oct 2026)

Source: royfish.dev/fingerprints-are-the-new-cookies

### What it says (30 seconds)

- A browser can be identified without storing anything on it. Script reads GPU, CPU threads, memory, screen, audio rendering, fonts, time zone, language, and hashes them into one value. None of these need a permission prompt.
- Uniqueness comes from the intersection, not any one trait. Latest Chrome is common, French is common, an M4 Mac is common; the combination is rare. The goal is uniqueness "in your sample size," not on Earth. Zip + birth date + sex alone identifies over 60% of Americans.
- The sequence: cookies got bad PR (2019-20), Privacy Sandbox flopped, Google then allowed fingerprinting in its ad products (Feb 2025). The ad platforms you pay are already doing this to your customers. Only engine-level browser defenses (Brave, Tor) blunt it.
- Written as a warning to users. It has no marketer playbook, so the playbook below is ours.

### How it reads against DJL: your attribution hole is a record-linkage problem

The checkout happens on fareharbor.com in a lightframe, not on your domain. So the visitor who clicked your ad and the booking in FareHarbor have no shared key. That one fact explains most of the tracking pain of the last 18 months: GA4 last-click hides social (Onera saw under 2% social in GA vs 60% in guest surveys), DCKT overcounts 3x in Meta because CAPI-only with no browser event to dedup against, NKST has no pixel of its own, and FareHarbor owns the Conversions API config so every fix routes through a support ticket.

Joining two records that lack a shared key is a solved problem in another field: **probabilistic record linkage** (Fellegi and Sunter, 1969). Census bureaus and hospitals use it to match people across files with no ID: weigh each agreeing field by how rare the agreement is, sum the evidence, accept above a threshold. The article's entropy math is the same math. This is a Claude-shaped problem in the exact sense of input one.

The honest correction to the headline, for your situation: **hashed email is your new cookie, not the fingerprint.** You already hold every guest's email and phone in FareHarbor. Meta's Advanced Matching and Google's Enhanced Conversions and Offline Conversion Import are the platforms doing fingerprint-grade matching on your behalf, using hashed PII you send them. You don't need to fingerprint anyone to get most of the win. The fingerprint is a secondary signal for the one gap email can't close: linking the anonymous ad click on your site to the booking that happened ten minutes later on FareHarbor's domain.

### What we build: the Attribution Bridge (new mashup #1)

Three layers, in order of certainty.

| Layer | What it does | Identifier | Who matches | Confidence |
|---|---|---|---|---|
| 1. Offline conversions per brand | Nightly: FareHarbor bookings per brand -> hashed email + phone + value -> Meta offline event set per brand, Google Enhanced Conversions / Offline Conversion Import | Hashed email, phone | Meta, Google | High. Platform-sanctioned, fixes "NKST has no pixel" and per-brand ROAS without waiting on FareHarbor's pixel split |
| 2. Click-ID capture | A small first-party script (or Worker) on each site logs gclid / fbclid / ttclid / UTMs with a timestamp, coarse geo, and IP /24 to our own store. Try to pass the click ID into the FareHarbor booking (custom field or URL param; FH support needed to confirm) | Click ID | Us, deterministic when FH carries the ID | Medium until FH confirms passthrough |
| 3. Probabilistic join | When no click ID reaches the booking: Fellegi-Sunter match of site session (time, geo, device class, referrer) to booking (created_at, customer city, device if FH exposes it) within a window. Output a match probability, not a yes/no | Coarse device signals + time + geo | Us | Medium. Directional for channel mix, not for bidding |

Outputs: a per-brand "bookings by true source" table that replaces GA4 last-click, offline conversion feeds that let Smart Bidding and Meta value optimization see every booking including phone and dashboard ones (with event IDs so they dedup against FH's CAPI), and a monthly answer to "which Reel booked a boat."

What it replaces or feeds: growth play #3 ("How did you hear about us?" field) becomes the calibration set for layer 3 rather than the whole answer. Play #2 (dollar value on leads) and play #4 (video-viewer retargeting) get real conversion feedback. Mashup #4 (bandit ad allocation) needs this as its reward signal, and mashup #5 (catchment map) reads the same booking table.

### Rules that travel with it

- **First party only.** Data stays on our server or Cloudflare account. No third-party trackers added, nothing sold, nothing shared beyond the ad platforms that already receive hashed PII through CAPI today.
- **Disclose it.** One paragraph in each site's privacy policy covering first-party analytics, click-ID logging, and hashed-email conversion matching. Texas (TDPSA) and Oregon (OCPA) are the states that could apply; both likely exempt us by size, but the disclosure costs nothing and honors opt-outs.
- **Coarse, not creepy.** Layer 3 uses device class and time windows, not a canvas/audio hash. We are matching our own bookings to our own ad clicks, not following people around the web.
- **Dedup or it overcounts.** Every event we send carries an event_id and order_id so Meta and Google collapse it against FareHarbor's CAPI event. DCKT's 3x is what happens without this.
- **Verify against FareHarbor's own counts** monthly. If the bridge says 140 bookings and FH says 120, the bridge is wrong.

### Re-ranked top five

| # | Mashup | Why it moved |
|---|---|---|
| 1 | **Attribution Bridge** (record linkage) | Everything below it needs a trustworthy booking-by-source table. David called it the clincher. |
| 2 | Booking-curve pricing (airline RM) | Biggest dollars, FH data in hand |
| 3 | Bandit ad allocation | Now has a reward signal from #1 |
| 4 | Guide plus-minus rating | Managers want it |
| 5 | Rebook hazard curve | Feeds the reactivation drips |

### Week 1, revised

Day 1-2: FH loader (bookings + customers, all brands) and hashing. Reproduce last month's booking count per brand.
Day 2-3: Layer 1 live for one brand (NKST, since it has no pixel of its own): Meta offline event set + Google offline import, with event IDs. Confirm events land in Events Manager and Google Ads.
Day 3-4: Layer 2 click-ID logger on the NKST site. Ask FareHarbor (David Thompson) whether a custom field or URL param can carry gclid/fbclid into the booking.
Day 5: Layer 3 prototype on 60 days of history; chart matched vs unmatched bookings by channel. Referee pass.
Then roll Layer 1 to every FH brand in one go.

Status: prep. Nothing built, nothing sent to FareHarbor. Note: memory points to `_Staged for Approval/2026-10-10 Meta Purchase Pixel Fix.md` but that file is not in the folder as of today; the bridge supersedes it either way.
