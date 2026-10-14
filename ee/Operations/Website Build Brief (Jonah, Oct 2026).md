# Website Build Brief (Jonah, Oct 2026)

Jonah wrote this (shared with Davey 2026-10-13). Load it at the start of any website or landing-page build for E&E, Elevated Tides, or Ohana, alongside Jess's style guide, and check the work against both before showing Davey or Jonah. Deliberately NOT in CLAUDE.md so it only costs context when a site is being built. Round-1 feedback that triggered this: [[Website Rebuild — Round 1 Feedback (Jonah, Oct 13 2026)]]. Build spec: [[Website Rebuild — Astro Build Spec (Oct 2026)]].

The idea (Adam Hayes): a model reasons better from principles plus checkable numbers than from a style guide. Four parts, used in order: decide what the page is for, follow the principles, hold the numbers, run the pre-launch checklist.

Sources: The UX Laws in My CLAUDE.md, The Visual Rules in My CLAUDE.md, Build product like the top 1%, Quoc Ly's "20 things to have Claude do before launching your website" reel. Condensed and reworded; read the originals for full text.

## 1. Before you design (product audit)
- **Time to value.** How long, how many clicks, from landing to the moment the visitor feels the point of the place? Under a minute and under five clicks. For E&E: landing to a confirmed booking.
- **Steal deliberately.** Keep a swipe file of flows and details from sites you admire; say which one a page is modeled on.
- **One world.** Site, emails, booking pages and confirmations feel like the same business. Test: cover the logo; would someone still know whose page it is?
- **Cut.** For every element: kill it, defer it, or pre-fill it.
- **Hold an opinion.** A page with a clear point of view beats a neutral one. Know what the business will not do.

## 2. Principles (the UX laws)
- **Hick's Law** (more choices, slower decisions): one job per screen; drop low-priority options; split hard choices into steps; recommend an option when choosing is hard.
- **Fitts's Law, size**: generous buttons and tap areas, spaced apart; no tiny icon as the only way to do something.
- **Jakob's Law**: standard placement for navigation, search, account, booking; invent a new pattern only for a real gain.
- **Proximity**: labels, controls and their information together; separate unrelated groups with space before borders.
- **Miller's Law**: chunk long content and forms; clear headings; never make people remember something from a previous screen.
- **Doherty threshold** (~400 ms): acknowledge every click at once; loading, processing, success states; never leave someone unsure it worked.
- **Von Restorff**: one dominant call to action per section; secondary actions visibly quieter.
- **Fitts's Law, distance**: actions beside what they affect; submit next to the last field.
- **Serial position**: most important first, closing action last.
- **Peak-end rule**: finish every flow on a clear confirmation of what happened and what comes next.
- **Zeigarnik**: show completed and remaining steps; save progress; easy to resume.
- **Pragnanz**: simple structure, little decoration, obvious hierarchy.
- **Sensible defaults**: preselect the common, safe option; never a default that commits someone unexpectedly; every default easy to change.
- **Postel's Law, prevention**: accept common formats; state requirements before submit; disable what is unavailable; warn before anything destructive.
- **Postel's Law, recovery**: keep the user's work after an error; plain-words error + exact fix; undo or retry.
- **Similarity**: same-purpose components look and behave the same; never style different actions the same way; reuse before making new.
- **Uniform connectedness**: containers and shared backgrounds tie controls to their content, on purpose.
- **Parkinson's Law**: fewest steps; cut needless confirmations; prefill what is known; shortcuts for repeat visitors.
- **Tesler's Law**: essentials first, advanced options when relevant, system carries the complexity.
- **Goal gradient**: show progress through multi-step flows; milestones; make what is left feel small and specific.

**Build order:** name the visitor's main goal; design the shortest clear path to it; make the next action obvious; remove distractions; respond to every action; prevent errors; keep work safe on failure; confirm clearly at the end. When principles conflict: clarity, accessibility, user control, getting the task done. Judgment, not a checklist.

## 3. Visual rules (checkable numbers)

| Element | Rule |
|---|---|
| Spacing scale | 4, 8, 16, 24, 32, 48, 64, 96 (8px grid; 4px only inside compact components) |
| Type scale | 14, 16, 20, 25, 31, 39 (ratio at least 1.25); body 16px or more; smallest labels 12px; H1 at least twice body |
| Line height | body 1.5 or more; headings 1.1 to 1.25 |
| Layout | 12 columns; breakpoints 640, 768, 1024, 1280; max width 720px reading, 1280px app-style pages |
| Buttons | 40px tall default, 32px compact, 48px touch-first; every tap target at least 44 x 44 |
| Inputs and tables | 40px inputs; 48px table rows (40px compact) |
| Icons | 16px inline, 20px in buttons and inputs, 24px standalone |
| Motion | 100 to 200ms feedback, 200 to 300ms layout changes, never over 400ms |
| Corners | one radius for components, one larger for containers and dialogs |
| Color | one accent; a neutral scale (background, surface, border, two text colors); status colors only for status |

**Ebb & Ember palette** (Brand Identity Packet, Jonah's vault `05 Ebb & Ember/Marketing/EE Brand Identity Packet .pdf`): mist #C8DACC, sage #798D7F, cream #EAD3B7, copper #BF7E45, charcoal #212121. Copy follows the E&E brand voice (this vault: [[Brand Story & Values]] + the reel/caption conventions).

## 4. Pre-launch checklist
- [ ] Privacy policy page
- [ ] Terms and conditions page
- [ ] No secrets or API keys in front-end code
- [ ] HTTPS forced everywhere
- [ ] Cookie consent banner (only if the site sets tracking/analytics cookies)
- [ ] Meta title and description on every page
- [ ] Social preview image
- [ ] Favicon
- [ ] sitemap.xml and robots.txt
- [ ] Alt text on every image
- [ ] Images compressed
- [ ] Page load speed checked (mobile too)
- [ ] Color contrast passes
- [ ] Works well on mobile
- [ ] Custom 404 page
- [ ] No broken links
- [ ] Form validation with plain-language errors
- [ ] Spam protection on every form
- [ ] Analytics installed
- [ ] One clear call to action per page
