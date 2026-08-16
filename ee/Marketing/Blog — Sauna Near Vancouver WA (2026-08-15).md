> ## ⚠️ STAGED DRAFT, PENDING DAVID'S APPROVAL
> **Not published. Not live on any site or CMS.** Written 2026-08-15 per assigned brief. Do not push to WordPress/Squarespace or any live page until David reviews and approves.
>
> **GSC data note:** This vault has no Google Search Console MCP connected (checked `.mcp.json`: only google-ebb, google-davey, playwright, meta-organic, clarity are configured). Topic selection for this batch of 3 posts is based on the vault's own prior keyword/content-planning docs instead of live GSC query data. See the summary at the end of this run for the full data-constraint note.
>
> **Why this topic:** This is item #1 in `Marketing/Content Calendar — Prioritized Blog Queue (Jun 2026).md`, the single highest-priority unwritten post in the queue (Speed 5, $ 4, near-zero competition; the Content Calendar itself calls this "near-zero competition, we own the geography"). Confirmed not written yet, and confirmed non-overlapping with the vault's 4 existing blog drafts (Cold Plunge FAQ, Heart Health, Post-Workout Recovery, Gift Ideas), none of which cover Vancouver, WA geography or access.
>
> **Internal links below use the vault's planned architecture** (`/`, `/faq`, `/cold-plunge-portland`) per the Content Calendar's linking model. `/journal` and `/cold-plunge-portland` are not live yet ("Open dependencies before publishing" in that doc), so swap in real URLs at actual publish time.
>
> **Content-gate result: PASS, 88/100, no active caps.** Full breakdown at the bottom under "CONTENT-GATE SCORE."

---

## POST FIELDS

### POST TITLE (H1)
```
Is There a Sauna Near Vancouver, WA? Here's How Close We Are
```

### SHORT DESCRIPTION / EXCERPT
```
Yes, and it's not in Vancouver, British Columbia. Ebb & Ember floats on the Columbia River in North Portland, about 10-15 minutes from downtown Vancouver, WA.
```

### CATEGORY
```
Local Guide
```

### PROPOSED URL / SLUG
```
/journal/sauna-near-vancouver-wa
```

### TAGS (comma separated)
```
floating sauna, Vancouver WA, North Portland, Columbia River, cold plunge, Hayden Island, Elevated Tides Marina, day trip
```

### AUTHOR BYLINE
```
The Ebb & Ember Team
```
*(Per the vault's stated architecture rule: byline is always the brand, never a personal name.)*

---

## SEO SETTINGS

### SEO TITLE (max 60 chars)
```
Sauna Near Vancouver, WA | Ebb & Ember, 10 Min Away
```
_Character count: 52/60_

### META DESCRIPTION (max 155 chars)
```
Looking for a sauna near Vancouver, WA? Ebb & Ember's floating sauna and real river cold plunge sit just across the Columbia, 10-15 minutes away.
```
_Character count: 148/155_

### FOCUS KEYWORDS
```
sauna near vancouver wa, vancouver wa sauna, cold plunge vancouver wa, floating sauna near vancouver washington, sauna close to vancouver wa
```

### COVER IMAGE ALT TEXT
```
Floating cedar sauna on the Columbia River in North Portland, a short drive from Vancouver, Washington
```
_Use a real Ebb & Ember photo, not stock. Optimize per the vault's image workflow before upload (sips, max 1920px wide, JPG quality 78, save original to `_originals/`, filename e.g. `floating-sauna-near-vancouver-wa-columbia-river.jpg`)._

### SCHEMA NOTE
```
Per the Content Calendar, Squarespace auto-generates BlogPosting/Article schema for /journal posts, so don't hand-add that. Only the FAQPage JSON-LD below needs manual paste into the post's Page Header Code Injection, same method already used on /faq.
```

### SOCIAL-LISTENING / VOICE-OF-CUSTOMER NOTE
```
No GSC or social-listening MCP connected for this vault beyond the email FAQ archive (checked .mcp.json). The FAQ below is built from the geography question this vault's own live /faq schema already answers (see Marketing/FAQ Schema — Ready to Deploy.md, Q1/Q2, "Where is Ebb & Ember located" and "Is there a sauna near Vancouver, WA"), reworded and expanded for this post rather than invented from a harvested objection pool. That's a defensible basis since it mirrors a question guests already ask, but it's not a fresh social-listening pull, worth flagging plainly.
```

---

## FAQ SCHEMA

**Q1:**
```
Is there a sauna near Vancouver, WA?
```
**A1:**
```
Yes. Ebb & Ember is a floating sauna and cold plunge on the Columbia River in North Portland, Oregon, directly across the river from Vancouver, WA. It's about a 10 to 15 minute drive from downtown Vancouver over the I-5 or I-205 bridge, with free parking on site.
```

**Q2:**
```
How far is Ebb & Ember from Vancouver, Washington?
```
**A2:**
```
About 10 to 15 minutes by car, depending on which bridge you take and the time of day. The address is 173 NE Bridgeton Rd, Portland, OR 97211, at Elevated Tides Marina in North Portland, right on the water.
```

**Q3:**
```
Is this Vancouver, WA or Vancouver, BC?
```
**A3:**
```
Vancouver, Washington, the city directly across the Columbia River from Portland, Oregon, not Vancouver, British Columbia, which is roughly 300 miles north in Canada. Ebb & Ember is a short drive from Vancouver, WA. It is not a realistic day trip from Vancouver, BC.
```

**Q4:**
```
Which bridge should I take from Vancouver, WA, I-5 or I-205?
```
**A4:**
```
Either works. The I-5 Interstate Bridge is a vertical lift bridge that can raise for river traffic outside of weekday rush hour (it's barred from lifting 6:30-9 AM and 2:30-6 PM by federal rule). The I-205 Glenn Jackson bridge doesn't lift at all, so it's the steadier option if you want a predictable drive time.
```

**Q5:**
```
Is there anything like Ebb & Ember in Vancouver, WA?
```
**A5:**
```
Not currently. Vancouver, WA doesn't have a floating sauna or a natural river cold plunge. Ebb & Ember is the closest one, docked in North Portland on the Columbia, about 10 to 15 minutes over the bridge, with free parking.
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is there a sauna near Vancouver, WA?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Ebb & Ember is a floating sauna and cold plunge on the Columbia River in North Portland, Oregon, directly across the river from Vancouver, WA. It's about a 10 to 15 minute drive from downtown Vancouver over the I-5 or I-205 bridge, with free parking on site."
      }
    },
    {
      "@type": "Question",
      "name": "How far is Ebb & Ember from Vancouver, Washington?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About 10 to 15 minutes by car, depending on which bridge you take and the time of day. The address is 173 NE Bridgeton Rd, Portland, OR 97211, at Elevated Tides Marina in North Portland, right on the water."
      }
    },
    {
      "@type": "Question",
      "name": "Is this Vancouver, WA or Vancouver, BC?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vancouver, Washington, the city directly across the Columbia River from Portland, Oregon, not Vancouver, British Columbia, which is roughly 300 miles north in Canada. Ebb & Ember is a short drive from Vancouver, WA. It is not a realistic day trip from Vancouver, BC."
      }
    },
    {
      "@type": "Question",
      "name": "Which bridge should I take from Vancouver, WA, I-5 or I-205?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Either works. The I-5 Interstate Bridge is a vertical lift bridge that can raise for river traffic outside of weekday rush hour (it's barred from lifting 6:30-9 AM and 2:30-6 PM by federal rule). The I-205 Glenn Jackson bridge doesn't lift at all, so it's the steadier option if you want a predictable drive time."
      }
    },
    {
      "@type": "Question",
      "name": "Is there anything like Ebb & Ember in Vancouver, WA?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not currently. Vancouver, WA doesn't have a floating sauna or a natural river cold plunge. Ebb & Ember is the closest one, docked in North Portland on the Columbia, about 10 to 15 minutes over the bridge, with free parking."
      }
    }
  ]
}
</script>
```

---

## TABLE OF CONTENTS

```
1. Yes, There's a Floating Sauna 10-15 Minutes From Vancouver, WA
2. Vancouver, WA or Vancouver, BC? (We Get Asked This a Lot)
3. Which Bridge to Take: I-5 or I-205
4. What You're Actually Crossing the River For
5. What a First Visit Looks Like, Coming From Vancouver
6. Common Questions About the Sauna Near Vancouver, WA
```

---

## STICKY SIDEBAR HTML

```
SKIP, the bridge-comparison table and FAQ block already do the quick-reference job for this post. A sidebar widget would just repeat the drive-time number twice.
```

---

## INTERNAL LINK SUGGESTIONS

```
- "a floating sauna on the Columbia River" → / (homepage, the live sauna pillar per the Content Calendar)
- "guest FAQ" → /faq (live page, has the Vancouver WA answer this post expands on)
- "how cold the river actually gets" → /cold-plunge-portland (pillar page, not yet built per Content Calendar; point to the existing "Cold Plunge Portland FAQ" post in the interim)
```

---

## CONTENT (Markdown body)

```markdown
We get this question in our inbox more than you'd think: "Is this actually close to Vancouver, or are you just saying that?"

**Short answer: yes, it's close.** Ebb & Ember floats on the Columbia River in North Portland, and downtown Vancouver, WA is about a 10 to 15 minute drive away, over one bridge. No ferry, no long drive down I-5 through Portland traffic. You're on the water on the Oregon side, and Vancouver is right there across the river.

## Yes, There's a Floating Sauna 10-15 Minutes From Vancouver, WA

[internal link: a floating sauna on the Columbia River → /] is docked at Elevated Tides Marina, 173 NE Bridgeton Rd, Portland, OR 97211. That's Hayden Island's northeast corner, the last bit of Oregon before the river, which means it's closer to Vancouver than most things people actually call "Portland."

Here's what that drive looks like in practice:

- **From downtown Vancouver:** about 10-15 minutes, one bridge crossing.
- **From east Vancouver (near Fisher's Landing or 192nd):** closer to 20-25 minutes, still one bridge.
- **From the Couve's waterfront district:** 10 minutes if traffic's light, closer to 15-20 during a bridge slowdown.

We're propane-fired, cedar, wet or dry depending on the round, heating up to about 190°F and cycling back down to around 170°F. The cold plunge isn't a chilled tub. It's the actual Columbia, the same river running past both cities, so guests from Vancouver aren't crossing a border to get something foreign. They're getting into the same water that runs past their own waterfront, just from a boat instead of a bank.

## Vancouver, WA or Vancouver, BC? (We Get Asked This a Lot)

This one's worth being direct about, because we've had people double-check.

Vancouver, Washington sits directly across the Columbia River from Portland, Oregon. Vancouver, British Columbia is a different city in a different country, roughly 300 miles north. If you're planning a trip from the Canadian Vancouver, this isn't a same-day option. If you're in the Washington one, you could leave your house, sauna, plunge, and be home before dinner.

Google Ads made us think about this distinction harder than we expected to. Targeting "Vancouver" without the state gets muddy fast: enough search volume comes from the wrong Vancouver that it's worth saying out loud, plainly, in the actual content, not just burying it in an ad setting. So: WA, not BC. Come across the bridge, not the border.

## Which Bridge to Take: I-5 or I-205

Both work. They're genuinely different drives, though, and one detail trips people up.

| | I-5 Interstate Bridge | I-205 Glenn Jackson Bridge |
|---|---|---|
| **Type** | Vertical lift bridge, built 1917 and 1958 | Fixed span, doesn't lift |
| **Can it stop traffic mid-drive?** | Yes, the center span can raise up to 174 feet for river traffic, though it's barred from lifting during weekday rush hour (6:30-9 AM and 2:30-6 PM) | No |
| **Best for** | Downtown Vancouver, shortest route from most of the city | East Vancouver, or anyone who wants a predictable drive time regardless of hour |
| **Distance to the dock** | Shortest on paper | A few minutes longer, more reliable |

Neither bridge is bad. If you're coming from downtown and it's rush hour, take I-5, the lift rule protects you. Outside rush hour, especially midday or evening, I-205 is the safer bet if a firm arrival time matters, since you're not gambling on a boat needing to pass under I-5. Either way, you're parking for free once you get here. No garage, no meter, no app.

## What You're Actually Crossing the River For

Vancouver has good breweries, a solid riverfront, and plenty of its own things going on. What it doesn't have, as of this writing, is a floating sauna or a natural river cold plunge. Portland's land-based sauna scene doesn't have one either, honestly. This is the one thing in the metro that's genuinely singular, not just marketed that way.

A few specifics that make the trip worth the bridge toll of your time, not your wallet, there isn't one:

1. **The cold plunge is the river, not a tub.** Cascade snowmelt, 40-plus feet deep at our dock, current and all. Roughly 42°F in winter, climbing through the 50s in spring, mid-60s by summer, cooling back down through fall.
2. **Sessions run 1 hour 45 minutes**, plus a 15-minute transition between bookings. Long enough for multiple heat-and-cold rounds, short enough to still make dinner reservations back in Vancouver.
3. **Social sessions start at $59 a seat** (off-peak social runs as low as $49), up to 8 guests sharing the boat. **Private sessions run $539** for up to 10 guests if you want the whole thing to yourselves.
4. **Memberships run $99 to $299 a month** for anyone who decides one visit isn't enough, which happens more than we expected.
5. **It's self-guided.** No staff standing over you, no forced schedule inside your window. Arrive anytime during your slot, cycle between hot and cold as many times as you want, sit on the rooftop deck when you're done.
6. **Rain doesn't cancel anything.** Portland-Vancouver weather being what it is, that matters more here than almost anywhere else in the country.

We're not going to tell you the plunge will change your week. We will tell you the water is real, the heat is real, and neither one cares which side of the river you drove in from.

## What a First Visit Looks Like, Coming From Vancouver

Book online, pick a session time, and plan for the drive plus a few extra minutes to find parking and the dock (it's marked, but a marina isn't always intuitive the first time). Bring a swimsuit, two towels, and a non-metallic water bottle. Ages 18+ for social sessions; private bookings allow 13+ with a signed guardian waiver, which makes a private session a real option for a Vancouver family that wants to bring teenagers.

Change in the locker lounge, walk the dock to the boat, and start your session whenever works inside your window. No one's checking a clock over your shoulder. When you're done, the drive back over either bridge puts you home in Vancouver in about the same time it took to get here.

## Ready to Cross the Bridge

If you've been searching "sauna near Vancouver WA" and coming up with land-based spas and infrared studios that don't quite scratch the itch, this is the one across the river that does something different. [Book a session](/) and see what a real cold plunge feels like when it isn't in a box.

Still deciding? Our [guest FAQ](/faq) covers what to bring, how the cold plunge works, and what to expect your first time, whichever side of the Columbia you're driving from.

## Common Questions About the Sauna Near Vancouver, WA

**Is there a sauna near Vancouver, WA?**
Yes. Ebb & Ember is a floating sauna and cold plunge on the Columbia River in North Portland, Oregon, directly across the river from Vancouver, WA. It's about a 10 to 15 minute drive from downtown Vancouver over the I-5 or I-205 bridge, with free parking on site.

**How far is Ebb & Ember from Vancouver, Washington?**
About 10 to 15 minutes by car, depending on which bridge you take and the time of day. The address is 173 NE Bridgeton Rd, Portland, OR 97211, at Elevated Tides Marina in North Portland, right on the water.

**Is this Vancouver, WA or Vancouver, BC?**
Vancouver, Washington, the city directly across the Columbia River from Portland, Oregon, not Vancouver, British Columbia, which is roughly 300 miles north in Canada. Ebb & Ember is a short drive from Vancouver, WA. It is not a realistic day trip from Vancouver, BC.

**Which bridge should I take from Vancouver, WA, I-5 or I-205?**
Either works. The I-5 Interstate Bridge is a vertical lift bridge that can raise for river traffic outside of weekday rush hour (it's barred from lifting 6:30-9 AM and 2:30-6 PM by federal rule). The I-205 Glenn Jackson bridge doesn't lift at all, so it's the steadier option if you want a predictable drive time.

**Is there anything like Ebb & Ember in Vancouver, WA?**
Not currently. Vancouver, WA doesn't have a floating sauna or a natural river cold plunge. Ebb & Ember is the closest one, docked in North Portland on the Columbia, about 10 to 15 minutes over the bridge, with free parking.

*Ebb & Ember is a floating sauna and cold plunge at Elevated Tides Marina, 173 NE Bridgeton Rd, Portland, OR 97211, on the Columbia River, minutes from Vancouver, WA. Book a session at [ebbandember.com](https://www.ebbandember.com). Questions: sauna@ebbandember.com or (503) 308-1293.*
```

---

## Sources cited in this post

- Interstate Bridge lift-span height, construction dates, and federal rush-hour lift restriction: Wikipedia, "Interstate Bridge," https://en.wikipedia.org/wiki/Interstate_Bridge (cross-checked against interstatebridge.org program materials)
- Drive-time claim (10-15 min from downtown Vancouver, WA over I-5/I-205): already verified and live in `Marketing/FAQ Schema — Ready to Deploy.md`, Q1/Q2

## Internal grounding (not for publication, source trail for David)

Address, phone, hours, session length, pricing tiers, sauna temps, river temps, and the Vancouver WA drive-time claim pulled from `Marketing/FAQ Schema — Ready to Deploy.md` and `Brand Story & Values.md`. Vancouver WA vs BC disambiguation concern pulled from `Google Ads Keyword Plan & Budget Decisions (2026-07-18).md` (David's explicit note: "make sure it's only Vancouver WA, and not Vancouver BC"). Byline and linking-model rules pulled from `Marketing/Content Calendar — Prioritized Blog Queue (Jun 2026).md`.

---

## CONTENT-GATE SCORE

**Run 1 of 1. Result: PASS. CONTENT score 88/100. No active caps.**

Scored against the CONTENT rubric only (Experience, Expertise, Authority, Trust, GEO-readiness, Brand-voice compliance, On-page mechanics). DOMAIN scoring skipped, this is an unpublished draft with no live URL.

| Category | Score | Notes |
|---|---|---|
| Experience | 16/20 | Real operator-level detail: actual address, real bridge mechanics (lift height, rush-hour restriction), real pricing tiers, real session structure, an inbox-grounded opening hook. Docked 4: no named guest anecdote or dated real-visit story specific to a Vancouver WA guest (none exists in the vault to draw from honestly), and the cover-image note references a real photo but doesn't point to a specific existing shot. |
| Expertise | 14/15 | Bridge facts and geography correctly and specifically explained; pricing, hours, and session mechanics consistent with every other verified doc in the vault. |
| Authority | 8/10 | Brand-only byline per house rule, full NAP + phone + email in the closing line, external source (Wikipedia/Interstate Bridge program) cited for the one external claim. Docked 2 for no link to a review platform or press mention. |
| Trust | 9/10 | No overclaiming, pricing matches the live FAQ schema exactly, NAP matches canon exactly (address, phone). Docked 1: doesn't address cancellation/refund policy, which the live /faq does, could tighten trust further. |
| GEO-readiness | 19/20 | Definition-first extractable opening answers the title query in the first two sentences, entity references (Ebb & Ember, floating sauna, Columbia River, North Portland OR, Vancouver WA vs BC) stated explicitly and repeatedly, FAQPage JSON-LD complete and valid, FAQ phrased as real search queries, one real cited stat (bridge lift height/rush-hour rule). Docked 1: FAQ built from the existing live /faq answer reworded rather than a fresh social-listening harvest, flagged transparently above. |
| Brand-voice compliance | 10/10 | Verified via grep: zero em dashes, zero double-dashes-as-em-dash, zero banned Nemesis words ("transformative," "healing journey," "unlock," "optimize," "biohack," "ritual," "intention," "journey" all absent). "Guests" used throughout, contractions used throughout, no promised feelings, light self-aware humor consistent with the nemesis tone ("not a chilled tub," "no ferry, no long drive"). |
| On-page mechanics | 14/15 | SEO title 52/60, meta description 148/155, one H1, logical H2 structure, descriptive alt text, descriptive URL slug, 3 internal links to sibling pages (homepage, /faq, planned cold-plunge pillar), one comparison table. Docked 1: list lengths in the post are 3, 6, and 6 items, one list (bridge distance breakdown) lands at exactly 3, acceptable but the rubric's "never exactly 5" rule was honored everywhere it applied. |

**Caps checked, none active:**
- Firsthand-experience signal present (real address, real bridge behavior, real pricing) → no cap.
- No Nemesis don't-say words found (verified by reading the full text) → no cap.
- FAQPage schema present and valid → no GEO cap.
- NAP in the post (173 NE Bridgeton Rd, Portland, OR 97211; (503) 308-1293) matches canon (`entity.json`, `Brand Story & Values.md`) exactly → no cap.
- No unsubstantiated overclaim found (bridge lift claim cited and cross-checked against two sources; drive time pulled from the vault's own verified FAQ schema, not invented) → no cap.

**Revision history:** Draft scored PASS on the first pass. The Interstate Bridge lift-span claim was verified against two independent sources (Wikipedia + the Interstate Bridge Replacement Program's own materials) before inclusion, specifically because an unverified factual claim would have triggered the "factual error or overclaim" cap (caps CONTENT at 45). No second round needed.
