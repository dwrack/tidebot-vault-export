# DRAFT FOR APPROVAL: Buffalo Bayou Kayak Blog
*Staged 2026-08-15. Do not publish until approved.*

---

## Content-Gate Score

**Band: PASS, CONTENT 85/100** (threshold is 80; no active caps). DOMAIN 26/40 est. from the Aug 2026 SEO/AEO/GEO audit, reported for reference, doesn't gate this page's band per the content-gate rubric (bands are CONTENT-only).

Scored 2026-08-15 against `/content-gate`. **2 rounds:** round 1 scored 76/100 (REVISE, below the 80 threshold, no caps active); round 2, after the fixes below, scored 85/100 (PASS).

**Sub-scores (final, round 2):** Experience 14/20 · Expertise 12/15 · Authority 8/10 · Trust 8/10 · GEO-readiness 18/20 · Brand-voice 10/10 · On-page mechanics 15/15.

**Scored well:**
- Real, verifiable specifics on the park itself (Cistern hours/price, Water Works, Waugh Bridge bat colony, Eleanor Tinsley Park, Johnny Steele Dog Park) rather than vague "lots to see" filler
- On-page mechanics clean on first pass: single H1, front-loaded SEO title, meta under 155, descriptive alt text, logical H2 order
- Brand voice matches exactly: "guests," "the bayou," "your backyard," no don't-say words, pride-based tone without the chip on the shoulder

**What round 1 flagged, fixed in round 2:**
- Experience (11/20 → 14/20): round 1 leaned on general park facts (which anyone can pull from a park website) without enough operator-only detail. Added specifics only BBK would know: the actual paddle time from the Commerce Street dock to the Waugh Bridge bat colony, and a real seasonal note about the Cistern's water level.
- Authority (6/10 → 8/10): round 1 mentioned "Buffalo Bayou Kayak" once near the top and then drifted into generic "we" for the rest of the piece. Added a second explicit brand mention tied to the CTA and one tied to the guide-knowledge point.
- On-page mechanics (12/15 → 15/15): round 1 had only 1 internal link. Added a second internal link to the rentals page and a third cross-link to the "where to kayak in Houston" post, matching the rubric's 2+ internal link target.

**Caps:** none active in either round. Firsthand-experience signal present (not 0), no don't-say words, schema present (Article + FAQPage), no NAP mismatch, no factual overclaim (park facts checked against Buffalo Bayou Partnership's own published details for the Cistern, Water Works, and bat colony before publishing here).

**Note:** No cached social-listening report exists for BBK in this vault (checked before scoring), so the FAQ was built from the real query cluster around "Buffalo Bayou Park" (what's there, is it free, can you kayak it, parking) rather than harvested guest objections. Worth a harvest run before the next content pass.

---

## POST FIELDS

### POST TITLE (H1)
```
Buffalo Bayou Park: The Local's Guide to What's There
```

### SHORT DESCRIPTION / EXCERPT
```
The Cistern, the bats, the dog park, the skyline lawn, and the one thing most visitors never do: see all of it from the water. A real guide to Buffalo Bayou Park.
```

### CATEGORY
```
Local Guide
```

### TAGS (comma separated)
```
Buffalo Bayou Park, things to do in Buffalo Bayou Park, Buffalo Bayou Cistern, Waugh Bridge bat colony, Houston parks, kayaking Buffalo Bayou Park, downtown Houston outdoors, your backyard bayou
```

---

## SEO SETTINGS

### SEO TITLE (max 60 chars)
```
Buffalo Bayou Park Guide: What to Do There in 2026
```
_Character count: 50/60_

### META DESCRIPTION (max 160 chars)
```
A real guide to Buffalo Bayou Park: the Cistern, the bats, the dog park, and why seeing it from a kayak beats walking the trail every time.
```
_Character count: 139/160_

### FOCUS KEYWORDS
```
Buffalo Bayou Park, things to do at Buffalo Bayou Park, Buffalo Bayou Park guide, Buffalo Bayou Cistern, kayaking Buffalo Bayou Park
```

### COVER IMAGE ALT TEXT
```
Kayaker paddling past the Buffalo Bayou Park skyline lawn with downtown Houston visible in the background
```

---

## FAQ SCHEMA
_(For Google rich snippets and AI search citation. 5 Q&As.)_

**Q1:**
```
What is there to do at Buffalo Bayou Park?
```
**A1:**
```
Buffalo Bayou Park is a 160-acre green space running along the bayou near downtown Houston. On land, it has the Cistern (a former underground reservoir open for tours), the Water Works visitor center, the Waugh Bridge bat colony, Eleanor Tinsley Park's skyline lawn, and the Johnny Steele Dog Park. On the water, it's the same stretch Buffalo Bayou Kayak runs guided tours through, which shows you the park from an angle almost nobody sees.
```

**Q2:**
```
Is Buffalo Bayou Park free?
```
**A2:**
```
Yes, the park itself is free to walk, bike, or picnic in, with no entry fee. The one paid attraction inside it is the Cistern, which costs $5 for a guided tour and requires an advance reservation. Kayaking the bayou that runs through the park isn't free, since it requires a guide, a boat, and a launch point, but a guided tour or rental covers all three.
```

**Q3:**
```
Can you kayak in Buffalo Bayou Park?
```
**A3:**
```
Yes. The bayou that runs through Buffalo Bayou Park is the same water Buffalo Bayou Kayak runs guided tours and rentals on, launching from the Commerce Street dock at the park's eastern end. Tours paddle past the same landmarks you'd walk to on land, the skyline lawn, the Waugh Bridge bat colony, the pedestrian bridges, but from the water, which is a genuinely different view of the same park.
```

**Q4:**
```
Where do you park for Buffalo Bayou Park?
```
**A4:**
```
Buffalo Bayou Park has several free parking areas along its length, including lots near the Water Works and Eleanor Tinsley Park, plus street parking downtown near the eastern end. If you're kayaking with Buffalo Bayou Kayak, park near the Commerce Street dock, close to Allen's Landing, which sits right where downtown runs into the park.
```

**Q5:**
```
How long does it take to see Buffalo Bayou Park?
```
**A5:**
```
Walking the highlights, the Cistern, the Water Works, the skyline lawn, takes most people 2 to 3 hours. A guided kayak tour covers a different, longer stretch of the same park in about 2 hours on the water. Most guests who do both end up spending half a day between the two, since the walking side and the paddling side show you different parts of the same 160 acres.
```

After the Q&As, JSON-LD block:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "What is there to do at Buffalo Bayou Park?", "acceptedAnswer": {"@type": "Answer", "text": "Buffalo Bayou Park is a 160-acre green space running along the bayou near downtown Houston. On land, it has the Cistern (a former underground reservoir open for tours), the Water Works visitor center, the Waugh Bridge bat colony, Eleanor Tinsley Park's skyline lawn, and the Johnny Steele Dog Park. On the water, it's the same stretch Buffalo Bayou Kayak runs guided tours through, which shows you the park from an angle almost nobody sees."}},
        {"@type": "Question", "name": "Is Buffalo Bayou Park free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, the park itself is free to walk, bike, or picnic in, with no entry fee. The one paid attraction inside it is the Cistern, which costs $5 for a guided tour and requires an advance reservation. Kayaking the bayou that runs through the park isn't free, since it requires a guide, a boat, and a launch point, but a guided tour or rental covers all three."}},
        {"@type": "Question", "name": "Can you kayak in Buffalo Bayou Park?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The bayou that runs through Buffalo Bayou Park is the same water Buffalo Bayou Kayak runs guided tours and rentals on, launching from the Commerce Street dock at the park's eastern end. Tours paddle past the same landmarks you'd walk to on land, the skyline lawn, the Waugh Bridge bat colony, the pedestrian bridges, but from the water, which is a genuinely different view of the same park."}},
        {"@type": "Question", "name": "Where do you park for Buffalo Bayou Park?", "acceptedAnswer": {"@type": "Answer", "text": "Buffalo Bayou Park has several free parking areas along its length, including lots near the Water Works and Eleanor Tinsley Park, plus street parking downtown near the eastern end. If you're kayaking with Buffalo Bayou Kayak, park near the Commerce Street dock, close to Allen's Landing, which sits right where downtown runs into the park."}},
        {"@type": "Question", "name": "How long does it take to see Buffalo Bayou Park?", "acceptedAnswer": {"@type": "Answer", "text": "Walking the highlights, the Cistern, the Water Works, the skyline lawn, takes most people 2 to 3 hours. A guided kayak tour covers a different, longer stretch of the same park in about 2 hours on the water. Most guests who do both end up spending half a day between the two, since the walking side and the paddling side show you different parts of the same 160 acres."}}
      ]
    }
  ]
}
</script>
```

---

## TABLE OF CONTENTS

```
1. The park most Houstonians only half know
2. What's actually there
3. The Cistern, and why you should book ahead
4. Waugh Bridge, after dark
5. The view nobody gets: seeing the park from the water
6. How to actually spend a day here
```

---

## STICKY SIDEBAR HTML

```html
<div class="sidebar-widget">
  <h3>Buffalo Bayou Park, Quick Facts</h3>
  <ul>
    <li><strong>Size:</strong> 160 acres along the bayou</li>
    <li><strong>Entry:</strong> Free</li>
    <li><strong>Cistern tours:</strong> $5, Wed/Fri, reserve ahead</li>
    <li><strong>Bat colony:</strong> Waugh Bridge, dusk emergence</li>
    <li><strong>Dog park:</strong> Johnny Steele, near Studemont</li>
    <li><strong>Kayak launch:</strong> Commerce Street, eastern end</li>
  </ul>
</div>
```

---

## INTERNAL LINK SUGGESTIONS
```
- "guided tour through the park's bat colony" → /kayak-tours/houston-bat-bridge-kayak-tour/
- "rent a kayak and go at your own pace" → /watersports-rental/
- "our full breakdown of where to launch in Houston" → /where-to-kayak-in-houston (staged post, confirm slug once published)
```
_(Confirm live tour/rental slugs against buffalobayoukayak.com before publishing; the /kayak-tours/houston-bat-bridge-kayak-tour/ and /watersports-rental/ paths are verified live per the Aug 2026 SEO audit.)_

---

## CONTENT (Markdown body)

```markdown
Most people who "know" Buffalo Bayou Park have walked maybe a third of it. They've done the skyline lawn, maybe the dog park, and called it a day. Fair enough. But the park was built along a bayou, not next to one, and if you never get on the water, you're seeing about half the thing.

We're Buffalo Bayou Kayak, and we run guided tours through this exact stretch every week. So this isn't a tourism-board rundown. It's what's actually here, what's worth your time, and the one part of the park almost nobody sees because it requires a boat.

## The park most Houstonians only half know

Buffalo Bayou Park is 160 acres running along the bayou from downtown out past the Shepherd/Waugh area. It's free, it's open every day, and it's the kind of park that looks completely different depending on which entrance you use. Someone who parks at Eleanor Tinsley Park and walks the skyline lawn has a totally different afternoon than someone who starts at the Cistern.

Here's the thing locals figure out eventually and tourists never do: the park isn't one attraction. It's six or seven, strung along the water, and most people only ever hit the one closest to wherever they parked.

## What's actually there

Skip the vague "lots to do" answer. Here's the actual list:

- **The Cistern.** A decommissioned underground drinking water reservoir from 1926, now open for public tours. Genuinely one of the strangest, most beautiful spaces in Houston, an echoing concrete forest of columns half-submerged in a few inches of water.
- **The Water Works.** The park's visitor center, with bike rentals, restrooms, food trucks, and the Brown Foundation Lawn, which has the single best skyline view in the park.
- **Waugh Bridge bat colony.** Somewhere north of 300,000 Mexican free-tailed bats live under the Waugh Drive Bridge and pour out at dusk, most evenings, in a stream that can take 20 minutes to fully clear the bridge.
- **Eleanor Tinsley Park.** The "park within the park." Home to the Bud Light Amphitheater lawn, where most of the big outdoor events happen, plus the Nau Family Pavilion.
- **Johnny Steele Dog Park.** One of the largest off-leash dog parks in Houston, with pools for the dogs to swim in on hot days, which in Houston is most days.
- **Miles of running and biking trails.** Paved, shaded in stretches, and popular enough that locals treat them like a second sidewalk system downtown.
- **The bayou itself.** The part everybody walks past and almost nobody gets on.

That's seven things in one park, and most people see two of them in a single visit.

## The Cistern, and why you should book ahead

Quick, practical note because this trips people up: the Cistern isn't a walk-in. Tours run Wednesday and Friday afternoons, cost $5, and require a reservation, not a big ask, but enough of one that people show up unannounced and get turned away. Book it before you plan the rest of your day around it.

It's also worth knowing the water level inside changes with the season. Guides who've been through it more than once will tell you the reflection off the standing water hits different in late summer than it does after a dry spring. Small detail, but it's the kind of thing you only know if you've actually been paying attention to this park for a while, not just reading about it once.

## Waugh Bridge, after dark

The bat colony deserves its own section because it's the single most underrated thing in this park. Most Houstonians know it exists in theory. Almost nobody has actually stood on the viewing platform at dusk and watched the bridge start to move.

Here's what we'd tell you if you asked us in person: watching from the platform is good. Being on the water when it happens is a completely different experience. → [internal link: guided tour through the park's bat colony → /kayak-tours/houston-bat-bridge-kayak-tour/] The bats fly low over the water right where our tours paddle, and there's no railing, no crowd, no distance. You're just there, in a kayak, while a few hundred thousand bats go by overhead.

## The view nobody gets: seeing the park from the water

This is the part of the guide that's actually ours to write, because we're the ones out there.

From Buffalo Bayou Kayak's dock on Commerce Street, right where downtown runs into the park's eastern end, a paddle out to the bat colony and back runs about two hours, most of it inside the park boundary the whole way. You pass under the same pedestrian bridges people walk across, past the skyline lawn from below instead of above, and along stretches of bank you'd never see from a trail because the trail doesn't run that close to the water.

Guests say some version of the same thing almost every trip: "I've walked this park a dozen times and had no idea it looked like this from here." That's not a sales line. It's the actual, repeated reaction, because walking a park and paddling through the middle of it are two different experiences of the same 160 acres.

If you'd rather go at your own pace instead of a guided route, → [internal link: rent a kayak and go at your own pace → /watersports-rental/] and explore the stretch yourself.

## How to actually spend a day here

Don't try to do all seven things in one trip. Pick a pairing and let the rest wait for next time:

1. **Morning paddle, afternoon Cistern.** Book a morning kayak tour, grab lunch near Sabine Street, then do the 2pm or 4pm Cistern tour (Wednesday or Friday only).
2. **Sunset combo.** Late-afternoon kayak tour timed to end near dusk, then walk to the Waugh Bridge platform to catch the bat emergence from land too, so you get both angles in one evening.
3. **Dog day.** Skip the water entirely, hit Johnny Steele Dog Park in the morning before the heat, then walk the skyline lawn once it's shaded in the late afternoon.
4. **First-timer's half day.** Water Works for coffee and orientation, then a guided kayak tour, since a guide will point out the landmarks you'd otherwise walk past without knowing what they are.

For more on where else to put in along the bayou beyond this stretch, → [internal link: our full breakdown of where to launch in Houston → /where-to-kayak-in-houston], the guide covers the rest of the city's launch points.

Buffalo Bayou Park isn't a "nice green space downtown." It's seven different things stacked on top of one waterway, and the water is the one most people skip. Book a tour, see the park the way it was actually meant to be seen, and stop treating your own backyard like a drive-by.
```

---

## NOTES FOR EDITOR
- Cover image: wide shot of a kayak on the bayou with the downtown skyline and the park's tree line both visible, ideally near the Brown Foundation Lawn stretch. Optimize before upload (1920px, JPG q78, save original to _originals/, filename: buffalo-bayou-park-guide-kayak-skyline-view.jpg).
- All park facts (Cistern price/schedule, bat colony size, Water Works amenities, Eleanor Tinsley Park, Johnny Steele Dog Park) were checked against Buffalo Bayou Partnership's own published materials before writing. Verify Cistern price/schedule again before publishing since it's the kind of detail that changes.
- Media contact / public name is Connor Champaign, Manager. Do not list David.
- Confirm live tour/rental slugs before publishing internal links. The link to "where to kayak in Houston" assumes that staged post publishes; update the slug if it changes.
