# Saved IG Posts → Content Engine — Start Here

*The pipeline that turns your Instagram **Saved** collection into shot-ready
content for every business. Two Claude Code skills do the work; this doc is the
map and the running action list.*

---

## The 3-step pipeline

```
[ Instagram Saved ]  --Playwright-->  saved_posts.json  --router-->  Swipe file + per-business ideas
   (your phone/PC)      (your PC)         (this vault)     (any session)     (Content Engine)
```

1. **Export** — run the `ig-saved-export` Playwright script **on your own
   computer** (Instagram blocks cloud/datacenter logins). It logs in as you, scrolls
   your saved grid, and writes `saved_posts.json`.
2. **Drop in** — copy `saved_posts.json` into this folder
   (`thebrain/03 Projects/Active/Content Engine/`).
3. **Route** — in a Claude session on this vault, run the `ig-content-router`
   skill. It fills the **IG Swipe File** and drops adapted ideas into each
   business's Marketing folder.

> Why not just do it here? This vault runs in a locked-down cloud session with no
> Instagram access, and a personal IG login from a datacenter IP gets checkpointed.
> The scrape has to run where you're already logged in. Everything after that runs here.

---

## What's useful to start doing (in order)

### This week — stand the pipeline up
- [ ] On your computer, in the `ig-saved-export` skill folder, run:
      `npm i playwright && npx playwright install chromium`
- [ ] Run `node export_saved.mjs YOUR_IG_USERNAME`, log in when the window opens,
      let it finish. Sanity-check `saved_posts.json` has your posts.
- [ ] Copy `saved_posts.json` into this folder and run the `ig-content-router`
      skill. You'll get an **IG Swipe File** and per-business idea drops.

### Every week — keep it fed (15 min)
- [ ] Keep saving posts you like on Instagram during the week (that IS the input).
- [ ] Re-run the export (login is cached now — fast) and re-run the router. It only
      processes posts it hasn't seen, so it stays quick.
- [ ] Skim the new swipe entries; star 1–2 to actually shoot.

### Every month — turn inspiration into output
- [ ] Pick the top 3 "low effort / high fit" ideas from the swipe file and schedule
      a single filming session to knock them out (batch B-roll + faceless formats).
- [ ] Route any UGC/creator posts through the **UGC Outreach & Repost Playbook** —
      DM for permission before reposting anyone else's content.
- [ ] Move winners into each business's posting queue (e.g. Ebb & Ember's
      `Last Minute Posts`).

---

## Ready to shoot now
*(The router refreshes this with the best low-effort ideas from your latest batch.
Until you've run it, it's empty — that's expected.)*

- _Run `ig-saved-export` → `ig-content-router` to populate this list._

---

## How posts get categorized

Every saved post is sorted into one of these formats (same pillars as the existing
social strategy), tagged with which businesses it fits, and reduced to a **reusable
mechanic** — the hook or structure you can copy — not just a description:

`POV skit · Multi-part arc · Niche humor · Edu-tainment · Transformation · UGC/repost · Hook/copy · Offer/promo · Other`

Businesses ideas route to: **dckt, nkst, npb, nbb, hpb, bbk, akt, lskt, ee, et** —
or `all` for a universal format.

---

## Files this pipeline touches
- `.claude/skills/ig-saved-export/` — the Playwright exporter (run locally)
- `.claude/skills/ig-content-router/` — the vault-side processor
- `thebrain/03 Projects/Active/Content Engine/saved_posts.json` — your export (git-ignored; it's data)
- `thebrain/03 Projects/Active/Content Engine/IG Swipe File.md` — the master swipe file
- `{business}/Marketing/Content Ideas — from IG Swipe.md` — adapted per-business ideas

*Maintained via the Content Engine. First created 2026-08-14.*
