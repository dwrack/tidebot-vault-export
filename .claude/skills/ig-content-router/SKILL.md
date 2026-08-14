---
name: ig-content-router
description: Turn exported saved Instagram posts (saved_posts.json) into Content Engine assets — a tagged swipe file plus per-business, ready-to-shoot content ideas. Use after the ig-saved-export skill has produced saved_posts.json, or whenever the user wants to process saved IG inspiration into their TideBot vault systems.
---

# Instagram Saved Posts — Content Router

Reads `saved_posts.json` (from the `ig-saved-export` skill) and files each saved
post into the vault's Content Engine as reusable content, not just a bookmark.

## Inputs

- `saved_posts.json` — array of posts. Look first at
  `thebrain/03 Projects/Active/Content Engine/saved_posts.json`, then the repo
  root, then ask the user for the path.
- Each record has: `url`, `type` (post/reel), `author`, `caption`, `thumbnail`,
  `savedFrom`, `scrapedAt`.

## The businesses (route ideas to these)

| Code | Business | Core hook |
|------|----------|-----------|
| dckt | Door County Kayak Tours | Scenic Great Lakes paddling |
| nkst | NOLA Swamp Kayak Tours | Silent bayou, wildlife, gators |
| npb  | NOLA Party Barge | Group party on the water |
| nbb  | NOLA Bike Bar | Pedal-pub crawl |
| hpb  | Houston Pedal Barge | Party pedal barge |
| bbk  | Buffalo Bayou Kayak | Urban Houston paddling |
| akt  | Austin Kayak Tours | City-lake / bat paddling |
| lskt | Lone Star Kayak Tours | Texas coast kayaking |
| ee   | Ebb and Ember | Sauna + cold plunge wellness |
| et   | Elevated Tides | Parent brand / cross-business |

When unsure which business a post fits, tag it `all` (a universal format) rather
than forcing a bad match.

## Content pillars / formats (classify each post into one)

Mirror the pillars already in `ee/Marketing/Social Media Strategy — Kimberlynn.md`
so this stays consistent with existing strategy:

1. **POV skit** — scripted relatable moment, soft close
2. **Multi-part arc** — one story across many posts (30-day, weekly series)
3. **Niche humor** — "types of people who…", "things only X understand"
4. **Edu-tainment** — fast value hook, faceless B-roll + text overlay
5. **Transformation** — before/after emotional arc, day-in-the-life
6. **UGC / repost** — creator content to reach out about and repost
7. **Hook / copy** — a caption, opening line, or on-screen text worth stealing
8. **Offer / promo** — deal framing, urgency, booking CTA mechanics
9. **Other** — worth keeping but doesn't fit above

## What to produce

For a first run, do **all** of the following. For re-runs, only process posts whose
`shortcode` isn't already in the master swipe file (it's the dedupe key).

### 1. Master swipe file
Write/append to
`thebrain/03 Projects/Active/Content Engine/IG Swipe File.md`.
One entry per saved post:

```markdown
### @{author} — {pillar}  ·  [{type}]({url})
- **Why it works:** {1-2 sentences on the actual mechanic — the hook, structure,
  or emotional beat that makes it perform. Not a description of the video.}
- **Steal this:** {the reusable pattern, stated so someone could execute it}
- **Fits:** {business codes, comma-separated, or `all`}
- **Effort:** {low / med / high to reproduce}
- `saved_from: {savedFrom}` · `shortcode: {shortcode}`
```

Group entries under `## {Pillar}` headings so the file reads as a playbook.

### 2. Per-business idea drops
For each business that got 3+ strong matches, append a dated section to that
business's `Marketing/Content Ideas — from IG Swipe.md` (create if absent):

```markdown
## {YYYY-MM-DD} — from saved IG posts
- **[{pillar}] {one-line idea adapted to THIS business}** — {how to shoot it,
  the specific local angle}. Source: [{author}]({url})
```

Adapt, don't copy: a "5 types of people in the sauna" post becomes "5 types of
people on a swamp tour" for nkst, with the specific characters named.

### 3. Update the Start Here list
Refresh the "Ready to shoot now" section in
`thebrain/03 Projects/Active/Content Engine/Saved IG Posts — Start Here.md` with the
5–10 lowest-effort / highest-fit ideas from this batch, so there's always a shot
list to pull from.

## Rules

- Judge the *mechanic*, not the surface. "Guy points at floating text" is useless;
  "open on the single most dramatic 1.5s, then rewind to how it started" is reusable.
- Be honest about fit. A wellness-brand transformation arc may not map to a party
  barge — say so and tag it `all` or the businesses it genuinely fits.
- Keep the original `url` on every entry so nothing becomes an orphaned idea.
- Don't invent captions the data doesn't contain; if a caption is empty, infer the
  format from `author` + `type` and note it's a low-confidence guess.
- This is inspiration/adaptation for the user's own brands — for the UGC/repost
  pillar, route through the existing `UGC Outreach & Repost Playbook` (get
  permission before reposting anyone's content).
