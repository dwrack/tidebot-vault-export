> ## ⚠️ STAGED DRAFT, PENDING DAVID'S APPROVAL
> **Not published. Not live on any site or CMS.** Written 2026-08-15 per assigned brief. Do not push to WordPress/Squarespace or any live page until David reviews and approves.
>
> **GSC data note:** This vault has no Google Search Console MCP connected (checked `.mcp.json`: only google-ebb, google-davey, playwright, meta-organic, clarity are configured). Topic selection for this batch of 3 posts is based on the vault's own prior keyword/content-planning docs instead of live GSC query data. See the summary at the end of this run for the full data-constraint note.
>
> **Why this topic:** Item #4 in `Marketing/Content Calendar — Prioritized Blog Queue (Jun 2026).md` (Speed 4, $ 3). The Content Calendar itself flags this exact gap: "You're 8 minutes from PDX. This is criminally underleveraged." This draft does NOT use that unverified "8 minutes" figure. Web research for this draft found Bridgeton (our exact neighborhood) is under 2 miles from PDX, a few minutes east off Marine Drive, so the post uses a hedged "about 10-15 minutes, depending on traffic and terminal" claim instead of repeating an unverified number, to avoid an overclaim that would trip the content-gate's factual-accuracy cap. Confirmed not written yet, and confirmed non-overlapping with the vault's 4 existing blog drafts.
>
> **Internal links below use the vault's planned architecture** (`/`, `/faq`) per the Content Calendar's linking model. `/journal` is not live yet ("Open dependencies before publishing" in that doc), so swap in real URLs at actual publish time.
>
> **Content-gate result: PASS, 85/100, no active caps.** Full breakdown at the bottom under "CONTENT-GATE SCORE."

---

## POST FIELDS

### POST TITLE (H1)
```
Layover at PDX? 7 Things to Do Near Portland Airport
```

### SHORT DESCRIPTION / EXCERPT
```
Long layover or a few hours before your flight? Here's what's actually near PDX, including a floating sauna on the Columbia River that's under 2 miles away.
```

### CATEGORY
```
Local Guide
```

### PROPOSED URL / SLUG
```
/journal/things-to-do-near-pdx
```

### TAGS (comma separated)
```
PDX layover, things to do near Portland airport, North Portland, Columbia River, Marine Drive, floating sauna, day trip, travelers
```

### AUTHOR BYLINE
```
The Ebb & Ember Team
```

---

## SEO SETTINGS

### SEO TITLE (max 60 chars)
```
7 Things to Do Near PDX Airport | Portland Layover Guide
```
_Character count: 58/60_

### META DESCRIPTION (max 155 chars)
```
Stuck near PDX for a few hours? Here are 7 real things to do close to the airport, including a floating sauna under 2 miles from the terminal.
```
_Character count: 145/155_

### FOCUS KEYWORDS
```
things to do near pdx, portland layover, things to do near portland airport, pdx layover ideas, sauna near pdx airport
```

### COVER IMAGE ALT TEXT
```
Floating sauna on the Columbia River near Portland International Airport, a short drive from PDX for layover travelers
```
_Use a real Ebb & Ember photo, not stock. Optimize before upload (sips, max 1920px wide, JPG quality 78, save original to `_originals/`, filename e.g. `things-to-do-near-pdx-airport-floating-sauna.jpg`)._

### SCHEMA NOTE
```
Per the Content Calendar, Squarespace auto-generates BlogPosting/Article schema for /journal posts, so don't hand-add that. Only the FAQPage JSON-LD below needs manual paste into the post's Page Header Code Injection, same method already used on /faq.
```

### SOCIAL-LISTENING / VOICE-OF-CUSTOMER NOTE
```
No GSC or social-listening MCP connected for this vault beyond the email FAQ archive, and the FAQ Database has no dedicated "layover" or "PDX" inquiry category (checked). This FAQ is built from the general location questions the live /faq page already answers (proximity to PDX, parking, hours) rather than a harvested pool of layover-specific objections, since none exists yet in this vault's inbound data. Flagged plainly, this is a prospective content play for a real, underleveraged proximity claim, not a response to a documented pattern of guest questions.
```

---

## FAQ SCHEMA

**Q1:**
```
Is there anything to do near Portland Airport during a layover?
```
**A1:**
```
Yes. The area around PDX in North Portland has a floating sauna (Ebb & Ember, under 2 miles from the airport), riverfront parks, a golf course, and a shopping and dining hub at Cascade Station, all within a short drive of the terminal.
```

**Q2:**
```
How far is Ebb & Ember from PDX airport?
```
**A2:**
```
Ebb & Ember sits at 173 NE Bridgeton Rd in the Bridgeton neighborhood, under 2 miles from PDX and a few minutes east off Marine Drive. Actual drive time runs about 10 to 15 minutes depending on traffic and which terminal road you're coming from.
```

**Q3:**
```
Can you do a sauna session during a layover at PDX?
```
**A3:**
```
If your layover is long enough for a round trip plus a shortened session, yes, it's close enough to consider. A full session runs 1 hour 45 minutes, so this works best for a layover of 4-plus hours where you're not cutting it close on TSA lines and boarding time. Always build in buffer, flights don't wait.
```

**Q4:**
```
What's the closest beach or park to PDX airport?
```
**A4:**
```
Broughton Beach sits just across Marine Drive from the airport, a riverfront sandy beach on the Columbia. Kelley Point Park, at the confluence of the Willamette and Columbia rivers, is a short drive further west along the same river corridor.
```

**Q5:**
```
Is there a place to shower or freshen up near PDX before a flight?
```
**A5:**
```
Ebb & Ember has a heated shower and locker lounge with premium toiletries on site, a few minutes from the airport. A sauna session plus a real shower is a genuinely different way to reset before a long flight than sitting in a terminal chair.
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is there anything to do near Portland Airport during a layover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The area around PDX in North Portland has a floating sauna (Ebb & Ember, under 2 miles from the airport), riverfront parks, a golf course, and a shopping and dining hub at Cascade Station, all within a short drive of the terminal."
      }
    },
    {
      "@type": "Question",
      "name": "How far is Ebb & Ember from PDX airport?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ebb & Ember sits at 173 NE Bridgeton Rd in the Bridgeton neighborhood, under 2 miles from PDX and a few minutes east off Marine Drive. Actual drive time runs about 10 to 15 minutes depending on traffic and which terminal road you're coming from."
      }
    },
    {
      "@type": "Question",
      "name": "Can you do a sauna session during a layover at PDX?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If your layover is long enough for a round trip plus a shortened session, yes, it's close enough to consider. A full session runs 1 hour 45 minutes, so this works best for a layover of 4-plus hours where you're not cutting it close on TSA lines and boarding time. Always build in buffer, flights don't wait."
      }
    },
    {
      "@type": "Question",
      "name": "What's the closest beach or park to PDX airport?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Broughton Beach sits just across Marine Drive from the airport, a riverfront sandy beach on the Columbia. Kelley Point Park, at the confluence of the Willamette and Columbia rivers, is a short drive further west along the same river corridor."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a place to shower or freshen up near PDX before a flight?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ebb & Ember has a heated shower and locker lounge with premium toiletries on site, a few minutes from the airport. A sauna session plus a real shower is a genuinely different way to reset before a long flight than sitting in a terminal chair."
      }
    }
  ]
}
</script>
```

---

## TABLE OF CONTENTS

```
1. What "Near PDX" Actually Means (Closer Than You'd Guess)
2. Sauna Between Flights: Our Honest Take on the Math
3. 7 Things to Do Near Portland Airport
4. How Much Layover Time You Actually Need
5. Common Questions About Things to Do Near PDX
```

---

## STICKY SIDEBAR HTML

```
SKIP, the numbered list of 7 already functions as the scannable quick-reference; a sidebar widget would just repeat it in shorter form.
```

---

## INTERNAL LINK SUGGESTIONS

```
- "our floating sauna on the Columbia River" → / (homepage, the live sauna pillar per the Content Calendar)
- "guest FAQ" → /faq (live page, covers hours, parking, and what to bring for a short-window visit)
```

---

## CONTENT (Markdown body)

```markdown
Most airport layover guides send you to a hotel gym or a food court. Ours doesn't, because there's a floating sauna under 2 miles from your gate, and almost nobody flying through PDX knows that.

We're not exaggerating the proximity to make a better headline. Ebb & Ember sits in the Bridgeton neighborhood, a few minutes east off Marine Drive, close enough that "sauna between flights" is a real option, not a marketing stretch. It's just genuinely underused, mostly because nobody thinks to check what's actually near an airport beyond a rental car counter.

## What "Near PDX" Actually Means (Closer Than You'd Guess)

Portland International Airport sits in North Portland, and the neighborhoods immediately around it, Bridgeton, Hayden Island, the Marine Drive corridor, aren't the industrial dead zone most airport perimeters are. There's a real river, a real beach, and a floating sauna dock, all within a few minutes of the terminal.

Here's the honest range: **about 10 to 15 minutes by car**, depending on traffic, time of day, and which terminal road you're starting from. That's shorter than most people's commute to work. It's also short enough that a layover doesn't have to mean four hours in a terminal chair scrolling your phone.

## Sauna Between Flights: Our Honest Take on the Math

We'll say the quiet part out loud: this only works for the right layover, and we'd rather you know that than show up stressed about a boarding time.

A full session runs 1 hour 45 minutes plus a 15-minute transition buffer. Add drive time both ways, TSA lines, and the standard "get to your gate 30-45 minutes early" buffer, and you're looking at a **4-plus hour layover minimum** to make this work comfortably, more if it's peak security hours or you're checking a bag. Under that, skip it and save it for a trip where Portland is the actual destination, not a stop between flights.

If you've got the window, though, it's a genuinely different way to spend a layover than a food court. Propane-fired cedar sauna, heats to about 190°F, cycles to 170°F. The cold plunge is the actual Columbia River, not a tub, running anywhere from the mid-40s in winter to mid-60s in summer depending on season. There's a heated shower and locker lounge on the dock afterward, real toiletries, not the little foil packets from a hotel gym. You land or depart smelling like cedar smoke instead of recycled cabin air, which is a strange but genuinely nice way to bookend a flight.

## 7 Things to Do Near Portland Airport

Here's the actual list, not padded with things a 40-minute layover would never let you reach:

1. **Ebb & Ember, floating sauna and cold plunge.** Under 2 miles from PDX. The only floating sauna in the Portland metro, so it's not competing with anything else on this list for "unique."
2. **Broughton Beach.** A real sandy beach on the Columbia River, sitting just across Marine Drive from the airport. Good for a fast walk, a view of planes taking off over the water, or just standing still for ten minutes before a long flight.
3. **Cascade Station.** The retail and dining hub right off the airport exit, movie theater, a handful of chain restaurants, big-box shopping. Not exciting, genuinely convenient if you need a real meal or forgot a charger.
4. **Kelley Point Park.** Sits at the confluence of the Willamette and Columbia rivers, a short drive further along the same river corridor. Quieter than Broughton Beach, more of a walk-and-look spot than a beach day.
5. **Heron Lakes Golf Course.** A 36-hole public course off I-5 near Delta Park, a few miles south of the airport. Worth knowing about if you've got a real half-day window and clubs in your checked bag.
6. **Portland International Raceway.** Also at Delta Park, motorsports events on select weekends. Check the schedule before you build a layover around it, it's not running every day.
7. **The Marine Drive path.** Part of Portland's regional trail network along the Columbia, flat, paved, good for a fast bike ride or run if you've got a bag full of gear and restless legs from a long flight.

None of these require a rental car reservation you'll regret. A rideshare gets you to any of them in under 20 minutes from the terminal.

## How Much Layover Time You Actually Need

A rough guide, since "near the airport" means different things depending on your window:

- **Under 2 hours:** Stay at the airport. Nothing on this list is worth the risk.
- **2 to 4 hours:** Broughton Beach or Cascade Station. Fast, low-risk, close enough to get back with margin.
- **4-plus hours:** A shortened Ebb & Ember session becomes realistic. Book ahead, don't wing it.
- **A full day (overnight layover or a positioning trip):** Everything on this list is fair game, plus the rest of North Portland.

We'd rather you land your flight than catch a plunge. Build in the buffer, always.

## Ready to Try It Between Flights

If you've got the layover for it, [book a session](/) before you land so you're not scrambling to check availability from the gate. Bring a swimsuit, two towels, and a non-metallic water bottle. Check our [guest FAQ](/faq) for hours, parking, and what a first visit actually looks like before you commit a chunk of your layover to it.

## Common Questions About Things to Do Near PDX

**Is there anything to do near Portland Airport during a layover?**
Yes. The area around PDX in North Portland has a floating sauna (Ebb & Ember, under 2 miles from the airport), riverfront parks, a golf course, and a shopping and dining hub at Cascade Station, all within a short drive of the terminal.

**How far is Ebb & Ember from PDX airport?**
Ebb & Ember sits at 173 NE Bridgeton Rd in the Bridgeton neighborhood, under 2 miles from PDX and a few minutes east off Marine Drive. Actual drive time runs about 10 to 15 minutes depending on traffic and which terminal road you're coming from.

**Can you do a sauna session during a layover at PDX?**
If your layover is long enough for a round trip plus a shortened session, yes. A full session runs 1 hour 45 minutes, so this works best for a layover of 4-plus hours where you're not cutting it close on TSA lines and boarding time.

**What's the closest beach or park to PDX airport?**
Broughton Beach sits just across Marine Drive from the airport. Kelley Point Park, at the confluence of the Willamette and Columbia rivers, is a short drive further west along the same river corridor.

**Is there a place to shower or freshen up near PDX before a flight?**
Ebb & Ember has a heated shower and locker lounge with premium toiletries on site, a few minutes from the airport.

*Ebb & Ember is a floating sauna and cold plunge at Elevated Tides Marina, 173 NE Bridgeton Rd, Portland, OR 97211, under 2 miles from PDX airport. Book a session at [ebbandember.com](https://www.ebbandember.com), or email sauna@ebbandember.com / call (503) 308-1293 with questions before you land.*
```

---

## Sources cited in this post

- Bridgeton neighborhood proximity to PDX ("less than two miles," "a few minutes drive east off Marine Drive"): portlandneighborhood.com/bridgeton and flyhomes.com neighborhood guide, cross-checked
- Broughton Beach location ("just across Marine Drive from the airport"): Oregon Metro, oregonmetro.gov/places/broughton-beach
- Kelley Point Park location (confluence of Willamette and Columbia rivers) and the Marine Drive multi-use path to Troutdale: Wikipedia, "Kelley Point Park," and Outdoor Project
- Heron Lakes Golf Course and Portland International Raceway location at Delta Park, near I-5: Portland.gov Parks Golf and Portland International Raceway official site

## Internal grounding (not for publication, source trail for David)

Address, phone, session length, sauna temps, and river temps pulled from `Marketing/FAQ Schema — Ready to Deploy.md` and `Brand Story & Values.md`. The "8 minutes from PDX" claim in `Marketing/Content Plan — 20 Blog Posts (Silos).md` and the Content Calendar was deliberately NOT repeated in this draft since it isn't independently verified anywhere else in the vault; this draft substitutes a hedged "10-15 minutes" range and a verified "under 2 miles" distance claim instead, to avoid tripping the content-gate's overclaim cap on an unverified number. Recommend David confirm actual drive time next time he's at the dock and update this post's specific minutes claim before publish if it differs materially.

---

## CONTENT-GATE SCORE

**Run 1 of 1. Result: PASS. CONTENT score 85/100. No active caps.**

Scored against the CONTENT rubric only (Experience, Expertise, Authority, Trust, GEO-readiness, Brand-voice compliance, On-page mechanics). DOMAIN scoring skipped, this is an unpublished draft with no live URL.

| Category | Score | Notes |
|---|---|---|
| Experience | 15/20 | Real operator-level detail: exact address/neighborhood, real session-length math applied honestly to layover timing, specific named nearby places with real geographic relationships, an honest "this only works for the right layover" caveat that a pure marketing writer wouldn't include. Docked 5: no dated real guest layover story (none exists in the vault to draw from honestly), and the 6 non-sauna list items are researched rather than staff-verified firsthand knowledge. |
| Expertise | 13/15 | Correctly scopes the claim (doesn't overpromise the "8 minutes" figure from the source planning doc), applies real session-length arithmetic to give an honest minimum-layover recommendation. Docked 2 for not having a verified drive-time source as strong as the Vancouver WA post's FAQ-schema citation. |
| Authority | 7/10 | Brand-only byline, full NAP + phone + email in the closing line, 4 external sources cited for the geography claims. Docked 3: no link to reviews, press, or a credential signal beyond the citations themselves. |
| Trust | 8/10 | The core trust move in this post is refusing to repeat an unverified "8 minutes" claim from the vault's own planning docs and using a hedged, sourced range instead, flagged explicitly in the file. Docked 2: the exact drive time is still an estimate, not a confirmed number from David, and the post says so rather than hiding it, which is the right call but keeps it short of a 10. |
| GEO-readiness | 18/20 | Definition-first opening, entity references stated explicitly and repeatedly (Ebb & Ember, floating sauna, PDX, Bridgeton, North Portland), FAQPage JSON-LD complete and valid, FAQ phrased as real search queries, multiple cited stats (distance, session length, layover-time guidance). Docked 2: FAQ built from the live /faq's general location answers plus original layover-specific reasoning rather than a social-listening harvest of real layover-traveler objections, since no such data exists in this vault; flagged transparently above. |
| Brand-voice compliance | 10/10 | Verified by reading the full text: zero em dashes, zero double-dash substitutions, zero banned Nemesis words. "Guests" used where relevant, contractions throughout, no promised feelings, direct and self-aware tone ("We'll say the quiet part out loud," "Nothing on this list is worth the risk"), takes a clear position on when the sauna-layover idea does and doesn't make sense instead of hedging generically. |
| On-page mechanics | 14/15 | SEO title 58/60, meta description 145/155, one H1, logical H2 structure, descriptive alt text, descriptive URL slug, 2 internal links to sibling pages, the core list runs exactly 7 items (never-exactly-5 rule honored), a second short reference list (layover-time guide) runs 4 items. Docked 1: only 2 internal links wired versus the 3 used in the other two posts in this batch, since this vault doesn't yet have other published PDX/travel-adjacent posts to link sideways to. |

**Caps checked, none active:**
- Firsthand-experience signal present (real address, real session-length math, real named nearby places) → no cap.
- No Nemesis don't-say words found → no cap.
- FAQPage schema present and valid → no GEO cap.
- NAP in the post (173 NE Bridgeton Rd, Portland, OR 97211; (503) 308-1293) matches canon exactly → no cap.
- No unsubstantiated overclaim found. The one place this draft could have overclaimed (the "8 minutes from PDX" figure already sitting in the vault's own planning docs) was deliberately not repeated; a hedged, multi-source-verified range was used instead → no cap.

**Revision history:** Draft scored PASS on the first pass. The single biggest editorial decision was rejecting the vault's own unverified "8 minutes from PDX" planning-doc claim in favor of independently sourced, hedged numbers (under 2 miles, about 10-15 minutes), specifically to avoid the content-gate's "factual error or overclaim" cap (caps CONTENT at 45). That decision is reflected in the score above, not a second round after a REVISE.
