# AI SEO — 90-Day Master Tracker

*Created 2026-05-10. Single source of truth for site updates, content, distribution, and measurement. Pairs with `Jess Astrella — Site Updates Spec.md` and `Content Plan — 20 Blog Posts (Silos).md`.*

## How to read this

Three lanes running in parallel:
- **Site Lane** — Jess Astrella (executor) + Davey (decisions, copy, schema review)
- **Content Lane** — Davey (writer) + Claude Code (drafts) + Hannah (review/edits)
- **Distribution Lane** — Davey + Mack (PR) + Hannah (GBP/reviews)

Weekly check-in: 30 min Sunday or Monday morning. Update this file as the canonical state.

Realism note: Davey has Dustin buyout active, dad's treatment, family load, and 12 other businesses. This plan assumes ~6-8 hours/week from Davey, not unlimited. Jess does 4-8 hours/week. Hannah does 2-3 hours/week.

---

## Phase 1: Foundation Sprint (May 11 to May 24, 2026)

Goal: ship the technical fixes and measurement infrastructure. Two weeks, 4-6 hours of Jess time, 4-5 hours of Davey time.

| Week | Lane | Owner | Task | Deliverable |
|---|---|---|---|---|
| W1 (May 11-17) | Site | Davey | Send Jess the kickoff email | Reply with calendar window |
| W1 | Site | Davey | Verify ebbandember.com in GSC (`sc-domain:ebbandember.com`) | DNS TXT verified |
| W1 | Site | Davey | Run baseline AI visibility check (manual ChatGPT, Perplexity, Google AI Overviews on 25 priority queries) | Baseline tracker filled |
| W1 | Distribution | Davey or Hannah | Reply to Aubrey's 3★ review with empathy + action | Reply published |
| W1 | Distribution | Davey | Pull remaining 36 GBP reviews (paginated continuation) | Complete review intel |
| W1 | Distribution | Hannah | Print Google review request cards (QR code) | 200 cards in lobby |
| W1 | Site | Davey | Run PageSpeed Insights on 3 key pages (home, /faq, /book) | Performance baseline |
| W2 (May 18-24) | Site | Jess + Davey | Kickoff sit-down (60-90 min) — walk Jess through spec + Claude Code demo | Spec accepted, dates locked |
| W2 | Site | Jess | Fix Squarespace Business Information panel (name, hours, phone, address) | LocalBusiness schema valid in Rich Results Test |
| W2 | Site | Jess | Add FAQPage JSON-LD via /faq Page Header Code Injection | FAQPage detected with 23 items in Rich Results Test |
| W2 | Site | Jess | Add definition sentence under H1 on homepage | Live |
| W2 | Site | Jess | Reconcile FAQ Q4 hours to "Daily 7am-9pm" | Live |
| W2 | Site | Davey | Audit and fix image alt text site-wide (highest-traffic pages first) | Alt text on every image |
| W2 | Distribution | Davey | Submit revised sitemap to GSC | Submitted |
| W2 | Distribution | Hannah | Set up Periode post-session email with review request | Email sending |

**Phase 1 success gate:** All schema validates. GSC verified. Aubrey replied. Baseline AI visibility logged. 5+ new reviews requested. Phase 2 starts only when these are green.

---

## Phase 2: Cornerstone Pages (May 25 to June 21, 2026)

Goal: ship five cornerstone pages that AI will cite for the next 12+ months. Four weeks.

| Week | Lane | Owner | Task | Deliverable |
|---|---|---|---|---|
| W3 (May 25-31) | Content | Davey + Claude | Draft /about copy ("the team" attribution) | 800-1,200 words |
| W3 | Content | Davey + Claude | Draft /floating-sauna-portland copy + FAQ block | 1,500-2,000 words |
| W3 | Site | Jess | Build /about in Squarespace (Hannah and David proof) | Page live |
| W3 | Distribution | Davey | First GBP post live (announce /about goes live, link to it) | Post published |
| W4 (June 1-7) | Site | Jess | Build /floating-sauna-portland with FAQPage schema | Page live, schema valid |
| W4 | Content | Davey + Claude | Research competitor pricing/capacity for /sauna-experiences-portland comparison guide | Research complete |
| W4 | Content | Davey + Claude | Draft /sauna-experiences-portland (the comparison guide) | 2,500-3,000 words, fair to all competitors |
| W4 | Distribution | Davey | Email Travel Portland content team — pitch inclusion in Wellness guide + offer comp session | Email sent |
| W4 | Distribution | Mack | Identify 1 podcast pitch target (Portland wellness or business) | Pitch sent |
| W5 (June 8-14) | Site | Jess | Build /sauna-experiences-portland with Article + ItemList schema | Page live, schema valid |
| W5 | Site | Davey | Internal linking pass (homepage, footer, nav rebuild) | Nav menu updated |
| W5 | Distribution | Davey | Build /press page aggregating coverage (KGW, Time Out, Portland Monthly x2, Travel Oregon, Yahoo) | Page live |
| W5 | Distribution | Hannah | GBP post #2 + #3 (river temp update, Banya Mondays) | 2 posts live |
| W6 (June 15-21) | Content | Davey + Claude | Draft /cold-plunge-portland (with NOAA river temp data) | 2,000-2,500 words |
| W6 | Content | Davey + Claude | Draft /private-sauna-rental-portland | 1,500-2,000 words |
| W6 | Site | Jess | Build both remaining cornerstones | Pages live |
| W6 | Distribution | Davey | Re-run 25-query AI visibility check, log movement | Dashboard updated |

**Phase 2 success gate:** 5 cornerstone pages live and indexed. /about appears for "Ebb and Ember founders" type queries. /floating-sauna-portland appears in AI answers for "Portland floating sauna" within 2-3 weeks of launch. At least 3 GBP posts live. Travel Portland response received.

---

## Phase 3: Blog Engine + Distribution Compound (June 22 to August 9, 2026)

Goal: ship first 7 of the 20 blog posts, build distribution flywheel. Seven weeks.

Blog setup (W7 only):

| Week | Lane | Owner | Task | Deliverable |
|---|---|---|---|---|
| W7 (June 22-28) | Site | Jess | Add /journal blog section to Squarespace | Section live |
| W7 | Site | Jess + Davey | Per-post template defined (SEO settings, image specs, byline) | Template documented |
| W7 | Content | Davey + Claude | Draft Post 1.5 "First Time at a Sauna" (~1,500-1,800 words) | Draft ready |
| W7 | Site | Jess | Publish Post 1.5 with optimized SEO settings | Live |
| W7 | Distribution | Hannah | Repurpose Post 1.5 → IG carousel + 1 email blast + 1 GBP post | 3 derivative pieces live |

Then a recurring weekly cadence W8 onward:

| Week | Post | Repurpose | Distribution touch |
|---|---|---|---|
| W8 (June 29-July 5) | 1.1 What to Wear to a Sauna | IG carousel + email + GBP | Reach out to one Portland wellness Reddit thread |
| W9 (July 6-12) | 1.2 How Long to Stay in a Sauna | IG reel + email + GBP | Pitch to Travel Oregon for inclusion |
| W10 (July 13-19) | 2.1 Cold Plunge Benefits (the science piece) | IG carousel + email + GBP | Submit to r/coldplunge as a resource |
| W11 (July 20-26) | 2.3 Contrast Therapy 101 | IG carousel + email + GBP | Backlink outreach to 3 wellness sites |
| W12 (July 27-Aug 2) | 1.3 Wet vs Dry vs Infrared | IG comparison reel + email + GBP | Pitch to Portland Monthly Health editor |
| W13 (Aug 3-9) | 1.4 Norwegian Sauna Tradition | IG carousel + email + GBP | Sauna Festival or West Coast Sauna Summit cross-promo |

Plus continuous:
- 2 GBP posts per week (Hannah)
- 1 review request batch per week (Hannah, post-session)
- Mack: 1 PR pitch per week
- Davey: 30-min Reddit/Quora authentic engagement weekly

**Phase 3 success gate:** 7 blog posts live and indexed. AI visibility check at W13 shows movement on at least 8 of the 25 priority queries vs Phase 1 baseline. Review count up by 15+. Travel Portland inclusion confirmed or in motion. First measurable AI referral traffic in GA4 (chat.openai.com, perplexity.ai, gemini.google.com).

---

## Open decisions before Phase 1 starts

| # | Decision | Owner | By |
|---|---|---|---|
| 1 | Sharing method for spec to Jess (Google Doc preferred) | Davey | Before email send |
| 2 | Email CC list (Hannah yes/no, plus media@ebbandember.com) | Davey | Before email send |
| 3 | Confirm 60-90 min calendar window May 19-30 for sit-down | Davey | This week |
| 4 | Aubrey reply tone and content (empathy + what's changed) | Davey | This week |
| 5 | Weekly check-in slot — Sunday eve or Monday morning | Davey | Phase 1 W1 |
| 6 | Cut Post 5.3 and replace with cultural piece on floating sauna trend | Davey | Phase 3 prep |
| 7 | Blog section URL slug (`/journal` vs `/notes`) | Davey | Phase 3 W7 |

---

## Risk register

What could derail this plan, with mitigations.

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Dustin negotiation escalates and consumes Davey bandwidth | Medium | High | Front-load Phase 1 deliverables that are Jess-owned, not Davey-owned, so progress continues |
| Jess capacity fills with V2 sauna build or signage work | Medium | Medium | Confirm Jess hours commitment in kickoff. If <4 hrs/week, defer Phase 3 site builds and lean on existing pages |
| Squarespace plan tier doesn't support Code Injection | Low | Medium | Verify in W1. If blocked, upgrade plan ($24/mo extra) |
| GSC verification fails at registrar | Low | Low | Davey owns DNS, can call registrar same-day |
| Aubrey doesn't respond well to reply or escalates | Low | Medium | Have Mack review reply before publishing if it gets touchy |
| AI visibility doesn't move by W13 despite execution | Medium | Medium | Re-evaluate at W13 gate. Likely cause: backlink shortage, not on-page. Pivot Phase 4 to outreach-heavy |
| Content production stalls (Davey bandwidth) | High | High | Claude Code drafts everything; Davey only edits and approves. Cut to 1 post/2 weeks if needed rather than skipping |

---

## Out of scope for this 90 days (revisit at Phase 4)

- Video production (the 3-5 min YouTube walkthrough I recommended originally)
- Wikipedia page push (need Mack to find an experienced editor first)
- Programmatic comparison pages (you-vs-Knot-Springs, you-vs-Löyly as standalone pages)
- Paid media layer (Google Ads, Meta Ads tied to high-converting cornerstone pages)
- Ebb and Ember branded gifting program (refer-a-friend mechanics)
- Press tour / Conde Nast / Travel + Leisure pitch (Mack-led, Phase 4)

These all matter. None are needed in the first 90 days.

---

## Weekly check-in template

Copy this into a new note each Sunday/Monday:

```
## Week of [date] — Check-In

### Phase: [1 / 2 / 3]
### Health: [Green / Yellow / Red] — one sentence why

### Done this week
- [task]
- [task]

### Slipped or blocked
- [task] — [reason] — [unblock by]

### Next week priorities (max 3)
1.
2.
3.

### Bandwidth check
- Davey: [hours available next week]
- Jess: [hours available next week]
- Hannah: [hours available next week]

### Open decisions
- [decision pending] — [decide by]
```

---

*Last updated: 2026-05-10 by Davey + Claude*
