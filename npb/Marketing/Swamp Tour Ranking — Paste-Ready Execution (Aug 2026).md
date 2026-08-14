# Swamp Tour Ranking — Paste-Ready Execution

**Date:** 2026-08-14
**Target keywords:** `new orleans swamp tour`, `swamp tour new orleans`, `swamp tours new orleans`
**Money page:** `https://nolapartybarges.com/` (the homepage IS the swamp page — do not build a second one)
**Source:** Executes the diagnosis in `SEO-AEO-GEO Audit — nolapartybarges.com (Aug 2026).md` and `SEO-AEO-GEO Deep Dive — nolapartybarges.com (Aug 2026).md`. Nothing here re-derives strategy. It's the copy and code those two docs called for.

---

## Where we actually stand (verified live 2026-08-14, corrected after a SERP check)

> **Correction, 2026-08-14.** An earlier version of this doc said "we rank #7.5." That's the number GSC reports, but it does not mean we hold a stable page-1 spot. David checked live and found us nowhere on page 1 or 2. Both are true, and the reconciliation is in "Why you don't see us" below. **The honest read is that we qualify for this SERP maybe 1 search in 10-30, mostly on mobile.** Read that section before the tables.

GSC, last 90 days, `sc-domain:nolapartybarges.com`:

| Query | Clicks | Impressions | CTR | Position |
|---|---|---|---|---|
| swamp tours new orleans | 21 | 738 | 2.85% | 7.5 |
| swamp tour new orleans | 12 | 875 | 1.37% | 7.5 |
| new orleans swamp tour | 13 | 470 | 2.77% | 7.4 |
| new orleans swamp tours | 4 | 161 | 2.48% | 5.8 |
| nola swamp tour | 4 | 113 | 3.54% | 4.5 |
| swamp tour (generic) | 3 | 346 | 0.87% | 18.7 |
| swamp tours (generic) | 3 | 331 | 0.91% | 28.3 |

All of it lands on `/`.

### Why you don't see us (the reconciliation)

GSC "position" is the average **only across searches where we appeared at all**. It says nothing about how often we appear. Those are two different numbers and the second one is the problem.

**Last 14 days, US, the four head-term variants combined:**

| Device | Impressions | Clicks | CTR | Avg position |
|---|---|---|---|---|
| Mobile | 234 | 11 | 4.70% | **8.4** |
| Desktop | 75 | 3 | 4.00% | **1.28** |
| Tablet | 3 | 0 | 0% | 7.3 |

Two things jump out.

**1. It's a mobile ranking.** 75% of impressions are mobile at position 8.4 — the bottom of page 1, below the local pack, the ads, and the tour-aggregator block. On a desktop SERP, that content is pushed further down or replaced entirely.

**2. The desktop "position 1.28" is almost certainly personalized, not competitive.** A generic head term does not average position 1.28 for a site that doesn't appear on page 1-2 of a clean search. Google heavily promotes sites you've previously visited. 75 impressions over 14 days at position ~1 is the signature of **us, our crew, and past customers** searching — not new demand. Don't count it.

**3. The appearance rate is the real number, and it's bad.** ~312 impressions over 14 days = **~22/day** across all four variants. Against the audit's corrected volume for those terms (roughly 7,000-19,000/mo combined, or 230-630/day), that's an appearance rate of **3-10%**. We show up in something like one search in ten to one in thirty.

So: a clean desktop search from an office in Houston or New Orleans will usually show nothing, exactly as observed. The two live SERP pulls in the first audit that found nothing in the top 20 were not wrong either.

**What is genuinely real:** 14 clicks in 14 days on those terms, and a 4.7% mobile CTR, which is *above* the normal curve for position 8 (typically 1.5-2.5%) — the review stars from the injected Product schema are doing work. Real people are finding and clicking us. There just aren't many of them.

### What this changes about the plan

Nothing in the fix list changes. The framing does:

- **The prize is the appearance rate, not the position.** Going from 5% appearance to 60% at the same position 8 is a 12x increase. Going from position 8 to position 5 at a 5% appearance rate is worth almost nothing. Fix qualification first.
- **This makes the entity problem the whole ballgame, not a nice-to-have.** We aren't being ranked 8th out of 10 relevant results. We're mostly not being considered a swamp tour operator at all, so we only surface when the query is unusually loose or the searcher is personalized toward us. That is precisely what a site titled "New Orleans Pedal Barge," with zero swamp-tour backlink anchors and 861 words on its money page, would look like.
- **Do not report this as "we rank #7.5" to anyone.** Report it as "we intermittently surface at the bottom of page 1 on mobile, in under 10% of searches."

### What's actually holding it at 7

Three things, in order of how much they cost us:

**1. Google still thinks this site is a pedal boat company.** Verified live today, three days after the audit flagged it as fix #1:

| Page | Live title tag |
|---|---|
| `/our-boats/` | Our Boats \| **New Orleans Pedal Barge** |
| `/the-freaky-tiki/` | The Freaky Tiki \| **New Orleans Pedal Barge** |
| `/new-orleans-booze-cruise/` | New Orleans Booze Cruise \| **New Orleans Pedal Barge** |
| `/swamp-tour-questions/` | Swamp Tour Questions \| **New Orleans Pedal Barge** |
| `/llms.txt` | "New Orleans **Pedal Barge** offers New Orleans **pedal** party boat booze cruises" |

The homepage title got fixed. Nothing else did. Half our backlink profile (62 of 124 referring domains) also says Pedal Barge, and **zero referring domains use an anchor containing "swamp tour" + "New Orleans."** Every entity signal Google reads points away from swamp tours. That is the ceiling.

**2. The homepage is 861 words with exactly one H2.** One. `All boats & swamp tours include`. Competitors ranking above us have dedicated swamp pages with 8-12 H2s. We're ranking on domain strength and GBP prominence alone.

**3. No FAQ, no FAQPage schema, no price in schema.** Which brings us to your question.

---

## Your question: should we have an FAQ on the homepage for AEO/GEO/SEO?

**Yes. And it's a bigger lever here than usual, for a reason that isn't obvious.**

Straight answer on each of the three:

- **SEO (classic blue links):** Marginal on its own. Google killed FAQ rich results for non-government/health sites back in Aug 2023, so no stars-and-accordions in the SERP. But the FAQ is the cheapest way to add the topical depth the homepage is missing, and it targets the four People Also Ask boxes that sit on the "swamp tours new orleans" SERP. That part is real.
- **AEO (People Also Ask, AI Overviews):** This is the actual win. The swamp SERP surfaces four AI-generated PAA boxes and we have a page for one of them. The highest-commercial-intent question on that SERP is **"How much does it cost to go on a swamp tour in New Orleans?"** and we have nothing answering it. We charge $63. That is a number nobody else on page 1 states plainly.
- **GEO (ChatGPT, Perplexity, Claude, Gemini):** Biggest structural gain. LLMs lift short, self-contained, question-headed passages close to verbatim. A 40-70 word answer under a literal question heading is the single most quotable format there is. We currently have 25 AI Overview citations and **21 of them are about December weather in New Orleans.** Zero on any commercial swamp query.

**The catch, and the reason to do this properly:** we already have the FAQ content. `/swamp-tour-questions/` is 1,623 words answering ten genuinely good questions, sitting at position 10.6 on 285 impressions with a 0.35% CTR. It is marked up as `Article` schema, not `FAQPage`. And its title says "New Orleans Pedal Barge." So we wrote the hard part two years ago and buried it.

So: FAQ block on the homepage (new, short, commercial), **and** fix the existing FAQ page's schema and title. Both below.

---

# THE FIXES

Ordered by clicks-per-minute-of-work.

---

## Fix 1 — WordPress Site Title (10 minutes, do this first)

This is fix #1 from the Aug 11 audit and it is still not done. It is the single highest-leverage field on the site.

**WP Admin → Settings → General → Site Title**

```
New Orleans Pedal Barge
```
change to
```
New Orleans Swamp Tours by Party Barge
```

> **Note on the wording.** The audit recommended "New Orleans Party Barge." I'd push it further. Every competitor that outranks us carries "New Orleans" + "Swamp Tour" as their dominant naming signal (tourbigeasy, jeanlafitte, louisianaswamp, cajunpride all do it). "Party Barge" alone keeps us positioned in a 590/mo category instead of the 3,000-10,000/mo one. **JEFF/DAVID: this is a brand call, not an SEO call — if it reads wrong to you, use "New Orleans Party Barge" and we lose maybe 20% of the lift.**

Then: **SEO plugin → Titles & Meta** → confirm the global title template ends in `%sitename%` and not a hardcoded string. If hardcoded, change it there too.

After saving, re-fetch `/our-boats/` and confirm the suffix changed. Pages with a hardcoded per-page SEO title won't be fixed by this and need their own edit.

---

## Fix 2 — llms.txt rewrite (10 minutes)

Currently the file AI engines read to understand us introduces us as a pedal boat company, and all 48 links in it are malformed (`[text] (url)` with a space, so nothing parses).

Replace the top of `/llms.txt` with:

```
# New Orleans Swamp Tours by Party Barge

> A BYOB swamp tour and party boat company in New Orleans, Louisiana. We run covered pontoon boats through Bayou Bienvenue to see alligators, herons, and cypress, departing from 2101 Paris Road, about 30 minutes from the French Quarter. Tours run 1 hour 45 minutes to 2 hours, start at $63 per person, include a captain and crew, a bathroom on board, and a Bluetooth sound system. Boats are heated in winter. Private charters available.

## Tours
- [Swamp Eco Tour: Gators and Bayou Birds](https://nolapartybarges.com/): 2-hour family-friendly swamp tour, from $50
- [The Freaky Tiki](https://nolapartybarges.com/the-freaky-tiki/): BYOB tiki boat swamp tour, up to 25 guests, from $63
- [The Twerkin Tiki](https://nolapartybarges.com/the-twerkin-tiki/): BYOB tiki boat swamp tour, up to 25 guests, from $63
- [The Bayou Boogie](https://nolapartybarges.com/the-bayou-boogie/): BYOB swamp tour boat, up to 18 guests, from $63
- [The Party Queen](https://nolapartybarges.com/the-party-queen/): BYOB swamp tour boat, up to 22 guests, from $63
- [Sunset Cocktail Cruise and Seafood Boil](https://nolapartybarges.com/): 2.5-hour sunset cruise with a Louisiana seafood boil, from $165

## Answers
- [Swamp Tour Questions](https://nolapartybarges.com/swamp-tour-questions/): what to wear, what to bring, how long it takes, tipping, weather
- [Which Swamp Tour Company Is Best](https://nolapartybarges.com/which-swamp-tour-company-is-the-best/): how New Orleans swamp tour operators compare
```

Note the link format: `[text](url)` with **no space**. That's the bug. Every one of the 48 existing links has it.

---

## Fix 3 — Homepage FAQ block (paste-ready copy)

Drop this **below the boat cards, above the footer**, on the homepage. Each answer is written to be liftable by an AI engine as a standalone unit: 40-70 words, self-contained, states the number.

The four starred questions are the literal People Also Ask boxes on the "swamp tours new orleans" SERP.

---

### New Orleans Swamp Tour Questions

**★ How much does a swamp tour in New Orleans cost?**

Most New Orleans swamp tours run $50 to $75 per person. Ours start at $63 for a 1 hour 45 minute BYOB cruise on a covered pontoon boat, and our 2-hour Swamp Eco Tour starts at $50. Private charters are available for groups. There's no fuel surcharge, no gratuity built into the ticket, and you bring your own drinks, so the price on the site is the price you pay.

**★ Is a swamp tour in New Orleans worth it?**

Yes, if you pick the right kind. The Louisiana wetlands are the thing people remember from a New Orleans trip more often than Bourbon Street. What makes a tour worth it is the boat and the guide, not the swamp. Ask whether there's a bathroom on board, whether the boat is covered, and how far you have to drive. Ours is 30 minutes from downtown, covered, heated in winter, and has a restroom.

**★ What's the best swamp tour in New Orleans?**

Depends what you want out of it. Airboats are loud and fast and cover more water. Kayaks get you closest to the wildlife but you're paddling. Covered pontoon boats like ours sit in the middle: you can hear the captain, bring a cooler, use a bathroom, and stay dry. If you're bringing a group, a birthday, or anyone who doesn't want to paddle, the pontoon is the one.

**★ What's the best time of year for a New Orleans swamp tour?**

March through October is peak alligator activity, since gators are cold-blooded and get sluggish below about 70 degrees. But the swamp doesn't close in winter. Our boats are heated, the birds are still there, the cypress is beautiful in the cold, and you'll have the bayou mostly to yourself. Summer mornings and evening cruises beat midday for both heat and wildlife.

**Where do New Orleans swamp tours actually leave from?**

Most leave from Slidell, Marrero, or Jean Lafitte, which means 45 to 60 minutes of driving each way. Ours departs 2101 Paris Road in New Orleans East, roughly 30 minutes from the French Quarter, on Bayou Bienvenue. That's the closest working swamp to downtown. No shuttle, no highway haul, no half-day gone before the boat starts.

**Will we actually see alligators?**

Almost always, March through October. Bayou Bienvenue is active water and our captains run it daily, so they know where the gators sit. You'll also see herons, egrets, turtles, and osprey year-round. We don't bait or feed them, so it's real wildlife on a real bayou rather than a staged show, which means we won't promise a number.

**Can you drink on a New Orleans swamp tour?**

On ours, yes. It's BYOB. Bring your own beer, wine, or cocktails and there's a bar setup on board to lay it out, plus a cooler, a Bluetooth sound system, and party lights. Most swamp tour operators in the area don't allow alcohol at all. Glass is fine, and there's a bathroom on board, which matters more than people expect.

**How long is a New Orleans swamp tour?**

Ours runs 1 hour 45 minutes on the water for the party boats and 2 hours for the Swamp Eco Tour. Add about 15 minutes for check-in and boarding. With a 30-minute drive from downtown each way, plan on roughly 3 hours door to door. Most other operators run 90 minutes to 2 hours plus a much longer drive.

**Are swamp tours in New Orleans family friendly?**

The Swamp Eco Tour is built for it: 2 hours, relaxed pace, captains who explain what you're looking at, restrooms on board, and no minimum age. The BYOB party boats work for families too, but they're geared toward adult groups. If you're bringing kids, book the Eco Tour.

**Do swamp tours run in the rain?**

Usually yes. Our boats are covered, so light rain is a non-issue and the wildlife is often more active. We cancel only for lightning or unsafe wind, and if we cancel you get a reschedule or a full refund. Louisiana rain tends to pass in twenty minutes, so we'd rather move you to a later slot than call off the day.

---

## Fix 4 — Homepage FAQPage schema

Paste into the **Schema Markup** ACF field (field key `field_seo__schema_markup`) on the homepage edit screen.

**Two rules that will silently break this if you miss them** (both learned the hard way on this theme):
1. **No `<script type="application/ld+json">` wrapper.** Raw JSON only. The field validates as JSON and rejects a script tag with `Please provide valid JSON. Error in object #1: Syntax error`. The theme adds the wrapper on render.
2. **No escaped inner double quotes (`\"`).** The storage layer strips the backslash and outputs a literal `"`, which breaks JSON parsing on the live page. Every question below is phrased to avoid inner quotes entirely.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does a swamp tour in New Orleans cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most New Orleans swamp tours run $50 to $75 per person. Ours start at $63 for a 1 hour 45 minute BYOB cruise on a covered pontoon boat, and our 2-hour Swamp Eco Tour starts at $50. Private charters are available for groups. There is no fuel surcharge and no gratuity built into the ticket."
      }
    },
    {
      "@type": "Question",
      "name": "Is a swamp tour in New Orleans worth it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, if you pick the right kind. What makes a tour worth it is the boat and the guide, not the swamp. Ask whether there is a bathroom on board, whether the boat is covered, and how far you have to drive. Ours departs 30 minutes from downtown New Orleans, is covered, is heated in winter, and has a restroom on board."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best swamp tour in New Orleans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends what you want. Airboats are loud and fast and cover more water. Kayaks get you closest to wildlife but you are paddling. Covered pontoon boats sit in the middle: you can hear the captain, bring a cooler, use a bathroom, and stay dry. For groups, birthdays, or anyone who does not want to paddle, the pontoon is the one."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best time of year for a New Orleans swamp tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "March through October is peak alligator activity, since alligators are cold-blooded and get sluggish below about 70 degrees. The swamp does not close in winter. Our boats are heated, the birds are still there, and the bayou is quiet. Summer mornings and evening cruises beat midday for both heat and wildlife."
      }
    },
    {
      "@type": "Question",
      "name": "Where do New Orleans swamp tours leave from?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most leave from Slidell, Marrero, or Jean Lafitte, which means 45 to 60 minutes of driving each way. Ours departs from 2101 Paris Road in New Orleans East, roughly 30 minutes from the French Quarter, on Bayou Bienvenue. That is the closest working swamp to downtown New Orleans."
      }
    },
    {
      "@type": "Question",
      "name": "Will we see alligators on a New Orleans swamp tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost always from March through October. Bayou Bienvenue is active water and our captains run it daily, so they know where the alligators sit. You will also see herons, egrets, turtles, and osprey year-round. We do not bait or feed the wildlife, so we will not promise a number."
      }
    },
    {
      "@type": "Question",
      "name": "Can you drink alcohol on a New Orleans swamp tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On ours, yes. It is BYOB. Bring your own beer, wine, or cocktails and there is a bar setup on board, plus a cooler, a Bluetooth sound system, and party lights. Most swamp tour operators in the New Orleans area do not allow alcohol at all. There is also a bathroom on board."
      }
    },
    {
      "@type": "Question",
      "name": "How long is a New Orleans swamp tour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ours runs 1 hour 45 minutes on the water for the party boats and 2 hours for the Swamp Eco Tour, plus about 15 minutes for check-in and boarding. With a 30-minute drive from downtown each way, plan on roughly 3 hours door to door."
      }
    },
    {
      "@type": "Question",
      "name": "Are New Orleans swamp tours family friendly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Swamp Eco Tour is built for families: 2 hours, a relaxed pace, captains who explain what you are looking at, restrooms on board, and no minimum age. The BYOB party boats work for families too but are geared toward adult groups. If you are bringing kids, book the Eco Tour."
      }
    },
    {
      "@type": "Question",
      "name": "Do New Orleans swamp tours run in the rain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually yes. Our boats are covered, so light rain is a non-issue and the wildlife is often more active. We cancel only for lightning or unsafe wind, and a cancellation means a reschedule or a full refund. Louisiana rain tends to pass in twenty minutes."
      }
    }
  ]
}
```

**Verify after saving.** The CMS accepts invalid output silently. Fetch the live page and run the embedded JSON-LD through `json.loads` before calling it done:

```bash
curl -sL https://nolapartybarges.com/ | python3 -c "
import sys,re,json
h=sys.stdin.read()
for m in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',h,re.S):
    try: print('OK', json.loads(m).get('@type'))
    except Exception as e: print('BROKEN:', e)
"
```

---

## Fix 5 — Add price to the existing Product schema

From the deep dive: `REVIEW_SNIPPET` is pulling **134,218 impressions and 1,358 clicks** at position 11.9. The Elfsight-injected Product schema carries a rating but no price, so a reseller (letsbatch.com, 7 reviews) gets "$63.00 to $1,200.00" in the SERP and we get a plain blue link.

Add an `offers` block to the Product schema:

```json
{
  "@type": "Offer",
  "priceCurrency": "USD",
  "lowPrice": "50",
  "highPrice": "1200",
  "availability": "https://schema.org/InStock",
  "url": "https://nolapartybarges.com/"
}
```

Leave the rest of the Elfsight block alone. It's working.

---

## Fix 6 — Rescue `/swamp-tour-questions/`

1,623 words, ten strong Q&As, position 10.6, **0.35% CTR**, and it's marked up as `Article`.

| Field | Now | Change to |
|---|---|---|
| Title | Swamp Tour Questions \| New Orleans **Pedal Barge** | `New Orleans Swamp Tour FAQ: Cost, What to Wear, Alligators` |
| Meta | auto-snippet, starts mid-sentence | `Everything to know before a New Orleans swamp tour: what it costs, what to wear, when alligators are active, how long it takes, and whether you can bring beer.` |
| H1 | Swamp Tour Questions | `New Orleans Swamp Tour Questions, Answered` |
| Schema | `Article` | **`FAQPage`** — mark up the ten existing H2s as Questions |

The ten H2s on that page are already perfectly formed questions. Converting `Article` to `FAQPage` is mechanical and it's the biggest AEO win on the site per unit of effort.

Then link it from the homepage FAQ block: after the last question, add
`Still deciding? Read the full [New Orleans swamp tour FAQ](/swamp-tour-questions/).`

---

## Fix 7 — Internal links (the anchor text problem)

Zero of our 124 referring domains use an anchor containing "swamp tour" + "New Orleans." We can't fix external anchors quickly, but internal ones we control today.

These are the highest-traffic pages on the site. Each gets one contextual link to `/` with a swamp anchor.

| Source page | 90d impressions | Anchor text to use | Where |
|---|---|---|---|
| `/how-much-do-you-need-to-budget-for-a-new-orleans-vacation-in-2024/` | 41,274 | `New Orleans swamp tour` | In the activities/entertainment cost section, next to the $63 figure |
| `/exploring-december-weather-...-what-to-wear/` | 40,346 | `heated New Orleans swamp tour` | In the "what to do in the cold" section |
| `/swamp-tour-questions/` | 3,715 | `book a New Orleans swamp tour` | End of the intro paragraph and after the final Q |
| `/which-swamp-tour-company-is-the-best/` | 24 | `New Orleans swamp tour` | In the comparison conclusion |
| `/new-orleans-swamp-tours-with-fishing-exploring-natures-bounty/` | 5,582 | `swamp tours in New Orleans` | First paragraph |
| `/a-winter-wonderland-on-the-swamp/` | 24 | `winter swamp tour in New Orleans` | Closing CTA |
| `/beyond-the-tourist-hotspots.../` | 5,428 | `New Orleans swamp tour` | In the off-the-beaten-path list |
| `/the-best-self-guided-walking-tour.../` | 5,372 | `swamp tour near New Orleans` | Closing "if you have another day" section |

**Anchor discipline:** vary the phrasing across these eight. Don't use the exact string `New Orleans swamp tour` more than four times sitewide. Never `click here` or `learn more`.

---

## Fix 8 — Homepage depth (the content project, do it last)

861 words and one H2 needs to become ~1,800 words with real structure. The FAQ block in Fix 3 adds roughly 800 of those words and six-plus headings on its own, which is why it's ordered first.

Remaining H2s to add between the boat cards and the FAQ:

- `What You'll See on Bayou Bienvenue` — alligators, herons, egrets, cypress, Spanish moss, the storm surge barrier, the levees
- `The Closest Swamp to the French Quarter` — 30 minutes, 2101 Paris Road, versus 45-60 to Slidell or Jean Lafitte
- `Airboat vs Kayak vs Covered Pontoon` — honest comparison table, this is the query behind half the PAA boxes
- `What's Included on Every Swamp Tour` — expand the existing single H2 into prose, not just the emoji list
- `Swamp Tours in Winter` — heated boats, the differentiator nobody else has

Keep the H1. `Most Swamp Tours in New Orleans Are Boring. Ours Aren't.` is doing its job.

---

## Execution order

| # | Fix | Time | Who |
|---|---|---|---|
| 1 | WordPress Site Title | 10 min | Whoever has WP admin |
| 2 | llms.txt rewrite | 10 min | Same |
| 3 | Homepage FAQ block (paste copy) | 20 min | Same |
| 4 | Homepage FAQPage schema + verify | 15 min | Same |
| 5 | Product schema price | 10 min | Same |
| 6 | `/swamp-tour-questions/` title, meta, H1, schema | 30 min | Same |
| 7 | Eight internal links | 45 min | Same |
| 8 | Homepage depth build | 3-4 hrs | Content |

Fixes 1-6 are about 95 minutes and cover the entity signal, the AEO gap, and the SERP snippet. Do those in one sitting.

**Re-check in GSC 21 days after Fix 1 lands.** Watch position on the three head terms and the appearance rate (impressions, not just position). If the entity fix works, impressions climb before position does.

---

## What NOT to do

- **Do not build a `/new-orleans-swamp-tour/` page.** The homepage already ranks #7.5 for these terms with the title and H1 pointed at swamp intent. A second page targeting the identical query with weaker authority makes Google choose, and that's the standard way to lose a position-7 ranking.
- **Do not spend money on a speed audit.** TTFB is 127ms, full HTML load 0.22s. The bottleneck is upstream of technical.
- **Do not chase `swamp tour near me`.** The 12,100/mo figure is a data artifact; raw clickstream shows 50.
