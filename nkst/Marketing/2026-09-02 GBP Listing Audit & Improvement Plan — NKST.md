---
type: audit
scope: Google Business Profile
date: 2026-09-02
status: REPORT ONLY — nothing changed live
---

# GBP Listing Audit & Improvement Plan — NKST (2026-09-02)

> **REPORT ONLY.** Nothing in this document has touched the live GBP listing, the website, or any ad platform. Every recommendation needs David's sign-off before anything is changed.

## What's different about this pass

The last nine SEO passes (Aug 14–16) all recorded GBP as **"not checkable — blocked on MCP access."** That's still true for *writing* (see [Blocked](#whats-still-blocked)), but the listing is **publicly readable**, so this pass verified the live state directly on Google Maps today instead of carrying forward the Aug 11 snapshot. Every fact in the next section was read off the live listing on 2026-09-02.

Bottom line: **every GBP item from the Aug 11 audit is still open**, one of them is a standing suspension risk, and a competitor has moved ahead of NKST on the exact metric NKST used to win on.

---

## Live snapshot — verified today

| Field | Live value (2026-09-02) | Notes |
|---|---|---|
| Name | New Orleans Kayak Swamp Tours | Leads with "Kayak" — reinforces the narrow category |
| **Primary category** | **Canoe & kayak tour agency** | ⚠️ Aug 11 fix **not applied** |
| Rating / reviews | **4.9 · 1,401** | Was 1,416 on Aug 11 — **down 15** |
| Address | 740 N Rampart St, New Orleans, LA 70116 | Matches `Operations/Tour Pricing & Info` |
| Phone | **(504) 571-9975** | ✅ Resolves the "unconfirmed" field in `Entity Canon` / `entity.json` |
| Website | neworleanskayakswamptours.com | |
| Plus code | XW6J+FX New Orleans | |
| Last owner post | **Jul 7, 2026** | ~8 weeks stale |
| Last photo | 22 days ago | |
| Booking options | Bayou Kayak Rentals $37 · Manchac $69 · Extended Manchac $138 · "29 more options from $35" | ⚠️ Vault says $65/$130 — see [Price drift](#price-drift) |
| Review keywords | alligators (419) · swamp (473) · swamp tour (98) · kayak swamp tour (37) | Guests describe this as a **swamp tour**, not a kayak tour |

**Hours note:** the listing read "Closed · Opens 7 AM Thu" when checked. Every competitor checked showed the same next-day pattern, so this is most likely just an after-hours read rather than a Wednesday closure — but it is worth a 10-second confirm in the dashboard that the weekly hours are right, since wrong hours suppress local-pack eligibility outright.

---

## The competitive picture changed

The Aug 11 audit framed the problem as "you have double Tour Big Easy's reviews and still aren't in the pack — review volume is not the blocker." That framing needs updating:

| Business | Reviews | Rating | Primary category |
|---|---|---|---|
| **Wild Louisiana Kayak Swamp Tours** | **1,785** | **5.0** | Canoe & kayak tour agency |
| **New Orleans Kayak Swamp Tours** | 1,401 | 4.9 | Canoe & kayak tour agency |
| Bayou Swamp Tours New Orleans | 3,346 | 4.9 | Tour operator |
| Cajun Pride Swamp Tours | 4,431 | 4.7 | Boat tour agency |
| Cajun Encounters Tours | 12,352 | 4.9 | Boat tour agency |
| Swamp Tours New Orleans (Tour Big Easy) | 731 | 4.8 | Boat tour agency |

**Wild Louisiana is now ahead of NKST on both review count and rating, in the identical category.** They were logged as a content-gap competitor back in June (`Marketing/Competitor Content-Gap Analysis — Wild Louisiana`); they are now the direct head-to-head in the kayak-swamp category. NKST's review count went *down* 15 in three weeks while theirs is climbing. Review velocity is now a real blocker, not just category.

Also note **Bayou Swamp Tours is listed "Open 24 hours"** under "Tour operator" — that combination is a big part of why they hold the near-me pack.

---

## Fix list, in priority order

### 1. Kill or fix the fabricated-address listing (do this first)

**Still live today:** `Plantation & Swamp Tours New Orleans` — 4.8 (43) — Tour operator — address **"Swamp Tour Street"**.

"Swamp Tour Street" is not a real street. A fabricated address is a **listing-suspension trigger, and suspensions can cascade across every listing on the account** — including the 1,401-review primary. This has been flagged as open since Aug 11 and is the only item here with downside risk attached to *not* acting.

**Recommended fix: convert it to a service-area business.** In the GBP dashboard, remove the street address entirely and set it as a service-area business covering Greater New Orleans.

This is better than either obvious alternative:

- **Better than deleting it.** The listing carries **43 real reviews** (guests name guide Jacob by name). Deleting is permanent and throws away earned review equity to solve a field-level problem.
- **Better than entering a real address.** Pointing it at 740 N Rampart or Esplanade stacks another listing onto an address already in the 70116 cluster, making fix #3 worse. A service-area business has no street address to collide with.

It is also simply the correct structure: a tour operator that shuttles guests to a launch site 35 minutes away is, by Google's own definition, a service-area business rather than a storefront.

Do not leave it as-is.

**Also found today — a sixth listing not in the Aug 11 inventory:** `New Orleans Plantation & Swamp Tours` — 4.8 (36) — Tour agency — **no address**. A review on it names guide **Nick**, who is an NKST guide, so this is almost certainly a controlled listing. Confirm ownership and fold it into the consolidation decision below.

### 2. Change the primary category

**Canoe & kayak tour agency → Tour operator.** Keep "Canoe & kayak tour agency" as a secondary category, and add "Boat tour agency" and "Eco tour agency" as secondaries.

Why: Google matches *primary* category to query intent, and "swamp tour" resolves to boat/tour-operator intent. Every business in the near-me pack is "Tour operator" or "Boat tour agency"; every business *outside* it is "Canoe & kayak tour agency." NKST's own review keyword cloud says guests call this a **swamp tour** (473 mentions) far more than a **kayak swamp tour** (37). The category is describing the vessel; the market is searching for the destination.

This is a two-minute change and the single highest leverage item on the list.

### 3. Resolve the 70116 proximity cluster

Six controlled listings, five of them within a few blocks of each other:

| Listing | Address | Category |
|---|---|---|
| New Orleans Kayak Swamp Tours | 740 N Rampart St, 70116 | Canoe & kayak tour agency |
| Crescent City Kayak - Swamp Tours | 437 Esplanade Ave, 70116 | Canoe & kayak tour agency |
| Hidden Adventure Swamp & Plantation Tours | 435 Esplanade Ave, 70116 | Canoe & kayak tour agency |
| Admire New Orleans - Kayak Tours | (no address) | Tour operator |
| Plantation & Swamp Tours New Orleans | "Swamp Tour Street" | Tour operator |
| **New Orleans Plantation & Swamp Tours** *(new)* | (no address) | Tour agency |

Google shows one result per business cluster. Six near-identical listings on two blocks trip the diversity filter, and it may be resolving to none of them. Note 435 and 437 Esplanade are **adjacent doors** — that is the least defensible pair.

This is a business decision, not an SEO one, and it's been open since May. The `Entity Canon` position is that these are intentional funnel brands and should not be consolidated. That's a legitimate strategy, but it has a measurable cost in the local pack, and someone should decide knowingly rather than by default. **Minimum viable version:** give each surviving listing a genuinely distinct primary category and a distinct address, so they stop reading as duplicates of each other.

### 4. Restart posting — the calendar already exists

Last owner post was **Jul 7**. `Marketing/gbp-calendar.json` holds a fully written, `"approved": true` post calendar (account `109075056374613070632`, location `10129422728201342552`) that started 2026-05-09 and was evidently never carried past early July. The copy in it is good and already in brand voice.

Re-date the remaining entries and resume. Two posts a week is enough. Posts are a freshness and engagement signal, and this one is pure recovered work — the asset is written and sitting on disk.

### 5. Fix review velocity

Reviews went **1,416 → 1,401** while the nearest competitor climbed past NKST. A drop means reviews are being filtered or removed faster than new ones land.

The ask-for-review moment should be systematized rather than left to guide discretion — the strongest point is on the shuttle ride back, while the guide is still with the group and the experience is minutes old. Guides are named constantly and warmly in the existing reviews (Nick, Stephanie, Jacob), which is exactly the review profile that converts; that's an asset worth leaning on deliberately. Owner responses are in good shape and should continue.

### 6. Fill in the profile fields that are currently thin

Description, services, attributes, and Q&A are all either stale or unset. Copy-paste-ready assets are in the appendix below.

---

## Price drift

Google's booking module shows **$69 Manchac / $138 Extended / $37 Bayou rentals**, and "29 more options from $35."

The vault says **$65 / $130**, and that $65 figure is hard-coded into `Operations/Tour Pricing & Info`, `NKST — FAQ Complete`, the phone auto-text script, and the chatbot/SMS scripts. Either prices rose and the vault is stale, or Google is displaying a marked-up third-party rate.

Worth resolving, because guests read $69 on Google and then hear $65 from the phone script — and every AI answer engine scraping either source will quote a price that contradicts the other. Not a GBP fix per se, but it surfaced here.

---

## Two entity-record corrections while we're here

- **Phone is now confirmed:** `(504) 571-9975`. Update `Entity Canon.md` and `entity.json` (both currently say "unconfirmed — verify from GBP"), and check off the "Phone number confirmed and consistent" item on the Knowledge-Graph checklist.
- **Instagram mismatch:** `entity.json` lists `instagram.com/nolaswamptours` in `sameAs`, but `CLAUDE.md` names the two live accounts as **@neworleanskayakswamptours** and **@kayaknola**. The `sameAs` graph is only useful if the URLs resolve — verify and correct.

---

## Copy-paste assets

### Business description (706 / 750 chars)

```
Small-group kayak swamp tours 30 minutes from the French Quarter. Since 2013 we've paddled guests through Manchac, the second-largest bald cypress swamp in the country, in silent kayaks instead of airboats. No motors, no wake, no baited alligators. Just trained naturalist guides who know cypress regeneration, coastal land loss, and where the herons are.

Tours run 2 or 4 hours, 12 guests max. Alligators are common spring through fall (common, not guaranteed, we don't promise wildlife). Beginners do fine, the water has no current. Round-trip shuttle from 740 N Rampart, or meet us at the launch in LaPlace.

Also: Honey Island, the Whitney Plantation combo, and self-guided rentals on Bayou Bienvenue.
```

Note it leads with "swamp tours" and "cypress swamp," carries the airboat disambiguation from `Entity Canon`, and keeps the "common, not guaranteed" honesty line from `Brand Story & Values`.

### Services to add

Each of these is a searchable entry. Add with prices where they're stable:

- Manchac Swamp Wildlife Kayak Tour (2 hr)
- Extended Manchac Kayak Tour (4 hr)
- Honey Island Swamp Kayak Tour (2 hr, seasonal)
- Whitney Plantation + Swamp Combo (full day)
- Shell Bank Bayou Kayak Tour
- Bayou Sauvage Urban Refuge Kayak Tour
- Fishing / Crabbing / Shrimping Bayou Tour
- Bayou St. John Self-Guided Kayak Rental
- Bayou Bienvenue Self-Guided Kayak Rental
- Private & Group Kayak Tours (see `Operations/Private Tour Rate Card`)
- Round-Trip Shuttle from the French Quarter

### Attributes to set

Small-group tours · Guided tours · Family-friendly · Beginner-friendly · Wheelchair-accessible parking (verify) · Restroom (verify at launch) · LGBTQ+ friendly · Reservations required · Online booking available · Free parking at launch site

Only set what's actually true — false attributes are a redressal risk.

### Q&A to seed (post as owner, then answer)

Seeding these is legitimate and Google-supported, and it beats letting the top-voted answer come from a stranger.

1. **Is this an airboat tour?** — No. We use silent kayaks, not motorized airboats. No engine noise, no wake, and we never bait alligators. You paddle at water level in a group of 12 or fewer with a trained naturalist guide.
2. **Do I need kayaking experience?** — No. The water has no current, so you're not fighting anything. Guides run a full briefing before launch, and most of our guests have never been in a kayak.
3. **Will I see alligators?** — Common spring through fall at Manchac, especially on warm mornings. Common, not guaranteed — we don't promise wildlife. Alligators are genuinely rare at Honey Island; book Manchac if a sighting matters to you.
4. **How do I get there from the French Quarter?** — Either add the round-trip shuttle from 740 N Rampart (departs 1 hr 15 min before tour time) or drive yourself to the launch in the Maurepas Swamp WMA, about 35 minutes out. Please don't take an Uber to the launch — there's no return service.
5. **How long is the tour and what's the time on the water?** — The standard tour is about 2 hours with 2–2.5 hours on the water; the extended tour is 4 hours. Add 30–40 minutes each way if you're driving.
6. **Can you do private or large groups?** — Yes, private tours run from 1 guest up to 20+, with per-person rates dropping as the group grows. Groups over 20 get a manual quote.

### First four posts

Pull the rest from `Marketing/gbp-calendar.json` and re-date them.

1. **September gator weather** *(Book)* — September is one of the best alligator months at Manchac. Water's still warm, mornings are calm, and the summer crowds are gone. Book the 9:00 AM slot for the best odds.
2. **Airboat vs. kayak** *(Learn more)* — The most common question we get is why paddle instead of ride. Short answer: an airboat engine clears the wildlife out ahead of you. A kayak doesn't. Link to `/airboat-vs-kayak-swamp-tour-new-orleans/`.
3. **Fall booking notice** *(Book)* — September through November fills up, especially weekends. Book a week ahead for peak dates.
4. **The Two Swamps story** *(Learn more)* — Manchac shows you what's worth fighting for; Bayou Bienvenue shows you what happens when the fight is lost. Pull from `Brand Story & Values`.

---

## What's still blocked

The `gbp` MCP server (and `google-nkst`, `meta-organic`, `clarity`, `slack`, `opencx`, `playwright`) **failed to connect this session.** The cause is now identified rather than guessed:

**`node` is not installed anywhere on this machine.** Not in PATH, not in `/usr/local/bin`, `/opt/homebrew/bin`, `~/.nvm`, `~/.volta`, `~/.asdf`, or any Homebrew Cellar — Homebrew itself isn't present. Four of the seven MCP servers are `node`-launched scripts and cannot start. `slack` and `opencx` need `npx`, same dependency. This is the same root cause that blocked PSI on Aug 16, and it is **not** the "session MCP-approval gap" that passes 5–9 diagnosed. Re-approving servers will not fix it.

The fix is installing Node.js:

```bash
curl -fsSL https://nodejs.org/dist/v22.11.0/node-v22.11.0-darwin-arm64.tar.gz -o /tmp/node.tar.gz && sudo tar -xzf /tmp/node.tar.gz -C /usr/local --strip-components=1
```

That needs your password, so it's yours to run. Once `node` resolves, restart Claude Code and the `gbp` tools should register — which unblocks reading live categories/attributes/insights and writing changes programmatically, plus GSC, GA4, and PSI for every future audit.

### Dashboard access is also wrong (checked 2026-09-02)

Attempted the browser route as a fallback. The Google account currently signed into Chrome manages **two businesses, both in Milwaukee** — `Brew City Kayak | Milwaukee Kayak Rentals & Tours` and `Milwaukee Kayak Tours`. Neither NKST nor any of the six NOLA cluster listings appear in that account's Business Profile Manager.

The `gbp` MCP config points at a token file for **`dwrack81@gmail.com`**, so that is the likely owning account — inferred from the config filename, not confirmed against the live listing.

**Net: there is currently no working path to edit any NKST listing** — the API route is dead (no `node`) and the signed-in browser account has no access. The first unblocking step is signing into the owning Google account, not installing Node.

**Once access exists, every change in this document can be made by hand in the GBP dashboard.** None require API access.

---

## Verification notes

- Live listing state, competitor review counts, the "Swamp Tour Street" listing, and the sixth cluster listing were all read off Google Maps today, 2026-09-02.
- Aug 11 baseline figures are from `Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026).md`.
- Pricing, hours, and tour details are from `Operations/Tour Pricing & Info.md` and `NKST — FAQ Complete.md`; voice from `Brand Story & Values.md`; identity from `Entity Canon.md` / `entity.json`.
- No GBP settings were changed, no posts published, no listings edited, no site or ad platform touched in producing this report.

*Related: [[Entity Canon]] · [[Operations/Tour Pricing & Info]] · [[Brand Story & Values]] · [[Marketing/SEO-AEO-GEO Audit — Swamp Tour Money Keywords (Aug 2026)]]*
