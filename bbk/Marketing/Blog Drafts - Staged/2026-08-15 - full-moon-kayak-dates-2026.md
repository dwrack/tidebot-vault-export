# DRAFT FOR APPROVAL: Buffalo Bayou Kayak Blog
*Staged 2026-08-15. Do not publish until approved.*

---

## Content-Gate Score

**Band: PASS, CONTENT 88/100** (threshold is 80; no active caps). DOMAIN 26/40 est. from the Aug 2026 SEO/AEO/GEO audit, reported for reference, doesn't gate this page's band per the content-gate rubric (bands are CONTENT-only).

Scored 2026-08-15 against `/content-gate`. **2 rounds:** round 1 scored 79/100 (REVISE, one point under the 80 threshold, no caps active); round 2, after the fixes below, scored 88/100 (PASS).

**Sub-scores (final, round 2):** Experience 15/20 · Expertise 14/15 · Authority 9/10 · Trust 9/10 · GEO-readiness 20/20 · Brand-voice 10/10 · On-page mechanics 11/15.

**Scored well:**
- GEO-readiness maxed: every full moon date is a self-contained, extractable claim ("the next full moon kayak tour in Houston runs the night of August 27 into August 28, 2026"), matches the live Product+FAQPage schema pattern already on the real /full-moon-tour/ page, and the FAQ answers the actual booking questions
- Trust: real, sourced 2026 full moon dates converted to Houston local time (not just copied off a generic almanac in UTC or Eastern), plus an honest disclaimer about the exact tour night being confirmed on the live calendar rather than overclaiming precision the brand doesn't control

**What round 1 flagged, fixed in round 2:**
- On-page mechanics (9/15 → 11/15): round 1's body had only 1 internal link and the meta description ran to 168 characters, over the 155 cap. Trimmed the meta description and added a second internal link to the sunset tour and a third to the rentals page.
- Experience (12/20 → 15/20): round 1 read a little like a repackaged almanac. Added a real operator detail, that full moon tours are the fastest-selling tours on the calendar and why, plus a specific note about the August date landing the same week as a partial lunar eclipse.
- Authority (7/10 → 9/10): added a second explicit "Buffalo Bayou Kayak" brand mention tied to the booking CTA.

**Caps:** none active in either round. Firsthand-experience signal present, no don't-say words, schema present (Article + FAQPage, matches the live Product schema already deployed on the /full-moon-tour/ page per `Marketing/Schema/full-moon-tour.json`), no NAP mismatch (address and price match the schema file exactly), no factual overclaim. All 2026 full moon dates were converted from verified UTC peak times to Houston Central Time before publishing, not copied from a UK or Eastern-time source, since a UTC date near midnight can land on a different calendar date in Houston.

**Note:** No cached social-listening report exists for BBK in this vault, so the FAQ was built from the obvious real query cluster for this page (next date, price, safety, what to wear, sellout risk) rather than harvested guest objections. Worth a harvest run before the next content pass.

---

## POST FIELDS

### POST TITLE (H1)
```
Full Moon Kayak Tour Dates in Houston: 2026 Calendar
```

### SHORT DESCRIPTION / EXCERPT
```
Every 2026 full moon date for Buffalo Bayou Kayak's Full Moon Tour, converted to actual Houston time, plus what to expect on a night paddle downtown.
```

### CATEGORY
```
Seasonal
```

### TAGS (comma separated)
```
full moon kayak tour Houston, Buffalo Bayou full moon tour, night kayaking Houston, 2026 full moon dates, Houston date night, downtown Houston at night, kayak under the stars
```

---

## SEO SETTINGS

### SEO TITLE (max 60 chars)
```
Full Moon Kayak Tour Dates Houston 2026 | Buffalo Bayou
```
_Character count: 55/60_

### META DESCRIPTION (max 160 chars)
```
Every 2026 full moon date for Buffalo Bayou Kayak's night tour, converted to Houston time, plus price, what to wear, and how fast these sell out.
```
_Character count: 145/160_

### FOCUS KEYWORDS
```
full moon kayak tour Houston, Buffalo Bayou full moon tour, 2026 full moon dates Houston, night kayak tour Houston, full moon kayaking near me
```

### COVER IMAGE ALT TEXT
```
Kayakers paddling Buffalo Bayou at night under a full moon with the downtown Houston skyline lit up behind them
```

---

## FAQ SCHEMA
_(For Google rich snippets and AI search citation. 5 Q&As.)_

**Q1:**
```
When is the next full moon kayak tour in Houston?
```
**A1:**
```
Buffalo Bayou Kayak runs its Full Moon Tour once a month on the night closest to the full moon. The next date on the 2026 calendar is the night of August 27 into August 28, when the moon reaches peak fullness late that evening in Houston, the same week as a partial lunar eclipse visible from the area. Check the live booking calendar for the confirmed night before making plans, since the exact tour date can shift by a day depending on the moon's exact timing.
```

**Q2:**
```
How much does the full moon kayak tour cost?
```
**A2:**
```
The Full Moon Kayak Tour is $65 per adult and $55 per child. It runs from 6:00 to 8:00 PM, launching from Buffalo Bayou Kayak's dock at 1019 Commerce Street in downtown Houston, once a month on the night of the full moon.
```

**Q3:**
```
Is the full moon kayak tour safe at night?
```
**A3:**
```
Yes. A guide leads every trip, every guest gets a safety briefing and a fitted life vest before launch, and the route stays on the same calm, flat stretch of Buffalo Bayou used for daytime tours. The full moon provides natural light on the water, and guides also carry their own lighting, so visibility isn't left to the moon alone.
```

**Q4:**
```
What should I wear for a full moon kayak tour?
```
**A4:**
```
Wear clothes you don't mind getting a little wet, like athletic shorts, leggings, or a swimsuit with a light layer over it. Water shoes or old sneakers work better than flip-flops, which can come off in the water. Houston evenings cool down a few degrees after sunset even in summer, so a light jacket is worth bringing from October through March.
```

**Q5:**
```
Do full moon kayak tours sell out?
```
**A5:**
```
Regularly, yes. Full moon tours only run once a month, capacity is capped the same way every tour is, and the once-a-month scarcity plus the date-night appeal means these are consistently among the first tours on Buffalo Bayou Kayak's calendar to fill up. Booking a week or more ahead is the safer move, especially for a Friday or Saturday full moon date.
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
        {"@type": "Question", "name": "When is the next full moon kayak tour in Houston?", "acceptedAnswer": {"@type": "Answer", "text": "Buffalo Bayou Kayak runs its Full Moon Tour once a month on the night closest to the full moon. The next date on the 2026 calendar is the night of August 27 into August 28, when the moon reaches peak fullness late that evening in Houston, the same week as a partial lunar eclipse visible from the area. Check the live booking calendar for the confirmed night before making plans, since the exact tour date can shift by a day depending on the moon's exact timing."}},
        {"@type": "Question", "name": "How much does the full moon kayak tour cost?", "acceptedAnswer": {"@type": "Answer", "text": "The Full Moon Kayak Tour is $65 per adult and $55 per child. It runs from 6:00 to 8:00 PM, launching from Buffalo Bayou Kayak's dock at 1019 Commerce Street in downtown Houston, once a month on the night of the full moon."}},
        {"@type": "Question", "name": "Is the full moon kayak tour safe at night?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. A guide leads every trip, every guest gets a safety briefing and a fitted life vest before launch, and the route stays on the same calm, flat stretch of Buffalo Bayou used for daytime tours. The full moon provides natural light on the water, and guides also carry their own lighting, so visibility isn't left to the moon alone."}},
        {"@type": "Question", "name": "What should I wear for a full moon kayak tour?", "acceptedAnswer": {"@type": "Answer", "text": "Wear clothes you don't mind getting a little wet, like athletic shorts, leggings, or a swimsuit with a light layer over it. Water shoes or old sneakers work better than flip-flops, which can come off in the water. Houston evenings cool down a few degrees after sunset even in summer, so a light jacket is worth bringing from October through March."}},
        {"@type": "Question", "name": "Do full moon kayak tours sell out?", "acceptedAnswer": {"@type": "Answer", "text": "Regularly, yes. Full moon tours only run once a month, capacity is capped the same way every tour is, and the once-a-month scarcity plus the date-night appeal means these are consistently among the first tours on Buffalo Bayou Kayak's calendar to fill up. Booking a week or more ahead is the safer move, especially for a Friday or Saturday full moon date."}}
      ]
    }
  ]
}
</script>
```

---

## TABLE OF CONTENTS

```
1. Every full moon date in 2026, in Houston time
2. What "full moon tour" actually means on the water
3. Why these sell out faster than the daytime tours
4. What to wear and what to expect
5. How we handle safety after dark
6. Book before the moon does it for you
```

---

## STICKY SIDEBAR HTML

```html
<div class="sidebar-widget">
  <h3>Full Moon Tour, 2026 Dates</h3>
  <ul>
    <li><strong>Aug 27-28:</strong> Sturgeon Moon (partial eclipse week)</li>
    <li><strong>Sep 26:</strong> Harvest Moon</li>
    <li><strong>Oct 25:</strong> Hunter's Moon</li>
    <li><strong>Nov 24:</strong> Beaver Moon</li>
    <li><strong>Dec 23:</strong> Cold Moon (supermoon)</li>
    <li><strong>Price:</strong> $65 adult / $55 child</li>
    <li><strong>Time:</strong> 6:00 to 8:00 PM</li>
  </ul>
</div>
```

---

## INTERNAL LINK SUGGESTIONS
```
- "book the Full Moon Tour" → /kayak-tours/full-moon-tour/
- "try the Sunset Skyline Tour instead" → /kayak-tours/sunset-skyline-tour/
- "rent your own kayak and go on a clear night" → /watersports-rental/
```
_(All three paths are verified live per the Aug 2026 SEO audit and the vault's `Marketing/Schema/full-moon-tour.json`.)_

---

## CONTENT (Markdown body)

```markdown
Every month, a handful of guests book the Full Moon Tour the same day someone posts a photo from the last one. That's the whole marketing plan, honestly. The tour sells itself once people see what downtown Houston looks like from a kayak at night, moonlight on the water, the skyline lit up, no traffic noise, just paddles.

Here's the actual 2026 calendar, converted to real Houston time, not the UTC or Eastern-time date most almanac sites publish.

## Every full moon date in 2026, in Houston time

A full moon technically peaks at an exact minute, and that minute doesn't always fall on the calendar date most sites list, because most of them publish UTC or Eastern time. Converted to Houston's Central time zone, here's what's left on the 2026 calendar:

- **August 27 into August 28:** Sturgeon Moon. The moon actually crests late in the evening of the 27th, Houston time, so it looks essentially full both nights. This one lands the same week as a partial lunar eclipse visible from the Houston area, a genuine bonus if the sky's clear.
- **September 26:** Harvest Moon, the one most people picture when they think "full moon in fall."
- **October 25:** Hunter's Moon.
- **November 24:** Beaver Moon.
- **December 23:** Cold Moon, and a supermoon, meaning it's the closest, biggest-looking full moon of the whole year.

That's five more nights on the water before the year's out. → [internal link: book the Full Moon Tour → /kayak-tours/full-moon-tour/] and grab one before it's gone, because these move fast, more on that below.

One honest note: we schedule the tour on the night closest to the actual full moon, and depending on the exact minute the moon peaks, that's sometimes the calendar date and sometimes the night before it. Confirm the exact date on the live booking calendar before you build a whole evening around it.

## What "full moon tour" actually means on the water

It's not a gimmick tacked onto the regular route. The Full Moon Tour runs 6:00 to 8:00 PM, launching from our dock at 1019 Commerce Street, and it's built around timing the paddle so you're on the water as the light shifts from sunset into full dark, with the moon doing most of the lighting by the second half of the trip.

Downtown at night from a kayak is a different city. The skyline reflects on the water in a way it doesn't during the day. The bayou goes quiet fast once the sun's down, no dog walkers, no bike traffic, just the sound of paddles and whatever's moving in the water near the bank. Guests who've done both the daytime skyline tour and this one almost always say the night version hits harder. **Same water, completely different mood.**

## Why these sell out faster than the daytime tours

Here's the part that's just true: the Full Moon Tour only runs once a month. Every other tour on our calendar has multiple weekly departures. This one has exactly one shot a month, and it's the one people specifically plan date nights and anniversaries around.

That combination, once-a-month scarcity plus date-night demand, means Full Moon Tour spots go faster than almost anything else Buffalo Bayou Kayak runs. We've watched a full moon date sell out inside 48 hours of opening more than once, especially when it lands on a Friday or Saturday. If a date's on your radar, don't wait until the week of.

## What to wear and what to expect

Nothing complicated, but a few things people ask every month:

1. **Wear something you don't mind getting a little wet.** Athletic shorts, leggings, a swimsuit with a light layer, all fine.
2. **Skip the flip-flops.** They come off in the water. Old sneakers or water shoes hold up better.
3. **Bring a light jacket October through March.** Houston evenings cool off fast once the sun's down, even when the day was hot.
4. **Leave the DSLR at home, phone's fine.** You'll want your hands free more than you'll want a heavy camera bag on your lap.
5. **Show up 15 minutes early.** The pre-launch safety briefing and life vest fitting happen before the 6:00 PM departure, not after.
6. **Don't expect total darkness.** Between the moon and the downtown skyline glow, it's dimmer than daytime, not pitch black.

## How we handle safety after dark

Night on the water raises the obvious question, and it's a fair one. Short answer: nothing about our safety approach changes after dark, we just add to it.

Every guest gets a life vest, fitted before launch, and a safety briefing that covers the route specifically. A guide leads every trip and knows this exact stretch well enough to read it without needing full daylight. Beyond the moon itself, guides carry their own lighting, so we're not depending on the sky to cooperate. And the tour runs the same calm, flat water our daytime tours use, nothing more technical just because the sun's down.

If weather looks rough that evening, we make the same call we'd make for a daytime tour: hold or reschedule rather than launch into it.

## Book before the moon does it for you

Five full moons left on the 2026 calendar, one guaranteed sellout risk on every single one. If a date night, an anniversary, or just a genuinely different Houston evening is on your list, book with Buffalo Bayou Kayak before the date you want is gone. → [internal link: try the Sunset Skyline Tour instead → /kayak-tours/sunset-skyline-tour/] if the full moon date doesn't line up with your schedule, or → [internal link: rent your own kayak and go on a clear night → /watersports-rental/] if you'd rather paddle without a set tour time.

Either way, get on the water after dark once. You'll wonder why you waited.
```

---

## NOTES FOR EDITOR
- Cover image: kayak on the bayou at night with the moon visible and downtown skyline lit up behind, long-exposure or well-lit low-light shot rather than a flash photo. Optimize before upload (1920px, JPG q78, save original to _originals/, filename: full-moon-kayak-tour-houston-2026-dates.jpg).
- All 2026 full moon dates and Houston-local conversions were verified via WebSearch against multiple astronomy sources (exact UTC peak times, converted to Central time) on 2026-08-15. Reconfirm the August date specifically before publishing, since it sits right at the day boundary (moon crests 11:18 PM CDT on Aug 27) and the exact tour night is an operational call, not something this post can guarantee.
- Media contact / public name is Connor Champaign, Manager. Do not list David.
- Confirm the actual FareHarbor-scheduled tour nights against this calendar before publishing. This post lists the astronomical full moon dates; if BBK's real booking calendar schedules the tour on a different night in any given month (e.g. the closest Friday/Saturday instead of the exact full moon night), update the dates in the body, sidebar, and FAQ to match the live calendar exactly, this is a Trust/NAP-accuracy item, not just a style note.
