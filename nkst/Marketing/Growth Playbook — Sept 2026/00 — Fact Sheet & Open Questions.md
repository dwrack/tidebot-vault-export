# 00 — Fact Sheet & Open Questions

*Growth Playbook, September 2026. Every other file in this folder draws its facts from this sheet. If a number changes, change it here first, then search the folder for the old value.*

**Status: DRAFT.** Nothing here is live. Anything that touches the website, FareHarbor, GHL, GBP or ad accounts needs David's sign-off first.

---

## Verified facts (source in brackets)

**Brand**
- Name: New Orleans Kayak Swamp Tours (NKST). Operating since **2013**. [Brand Story & Values]
- Phone: **(504) 571-9975**. [GBP, verified 2026-09-02]
- Site: neworleanskayakswamptours.com. Booking runs through FareHarbor.
- Outward contact persona: **Ray Fontaine**. Never "correct" this name, and never list David as the contact. [Entity Canon]
- AI chat agent: Magnolia (OpenCX).

**Proof**
- Google: **4.9★ from 1,401 reviews** (2026-09-02). Guests name guides warmly (Nick, Stephanie, Jacob).
- TripAdvisor Travelers' Choice. Climate Culture "See the Vision" award.
- Silent kayaks, not airboats. Trained naturalist guides. **12 guests max** on public tours.
- Safety: USCG Type III life jackets, CPR-certified guides, a safety briefing on every tour.

**Flagship: Manchac Swamp Wildlife Tour**
- **2 hours.** 2–2.5 hours on the water.
- **From $65/person** *(see open question 1)*.
- Where: Maurepas Swamp WMA (Manchac), the second-largest bald cypress swamp in the US. Launch at Old US Hwy 51, LaPlace (Plus Code 5H64+W3), about 35 minutes from the French Quarter.
- Times: 9:00 AM, 11:30 AM, 2:00 PM and 4:30 PM.
- **Pickup:** round-trip shuttle from **740 N Rampart St** (edge of the French Quarter), **+$25/person**. The van leaves 1 hr 15 min before tour time. Guests who drive can meet at the launch. Don't use Uber to get there, because there's no ride back.

**Other tours**
| Tour | Price | Notes |
|---|---|---|
| Extended Manchac (4 hr) | $130/pp | 11:00 AM. Best for photographers and serious wildlife watchers. |
| Whitney Plantation + Swamp Combo (~8 hr) | $195/pp | 9:00 AM. Whitney admission and transport included. |
| Honey Island (2 hr) | $65/pp | **Summer only.** Alligators are **rare** here, and water levels make it less consistent. Book Manchac if seeing gators matters to you. |
| Bayou Bienvenue self-guided rental | ~$37 (per GBP) | 2102 Paris Rd, Lower 9th Ward. Code unlock. The "Two Swamps" restoration story. |
| Private tours | See [[Operations/Private Tour Rate Card]] | Standard 2 hr: 1 guest $250 · 2 guests $350 · 3 guests $450 · 4–6 $120/pp · 7–12 $110/pp · 13–20 $105/pp. More than 20 guests: call David. |

**Guest rules**
- Minimum age **8**. Anyone under 16 paddles tandem with an adult.
- Tandem sit-on-top kayaks (Wilderness Systems) hold 400 lbs combined. Solo paddlers are most comfortable under 250 lbs.
- No experience needed. The water has no current.
- Tours run in light rain and cancel only for lightning or severe weather. When we cancel, the guest gets a full refund.
- Wildlife: "**common, not guaranteed.**" Alligators are common at Manchac from spring through fall. Below 65°F reptiles go quiet, but winter brings migratory birds.
- Seasons: fall is the best season and books up fast. Winter runs year-round in the 40s–60s°F. Summer is hot, so the early tours are best.

**Existing programs to build on**
- Referral: "Give $10 / Get $10" code, specced but not built. [Customer Journey Map, Stage 6]
- Affiliates: about 100 dormant GHL signups. The pitch is 10% commission or $50–100 per day of referrals, **not yet confirmed**. [Affiliate & Partner Program]
- Partner prospects: Destination Kitchen Food Tours (food partner), Bach to Basic and JETSET Bachelorette (concierges), plus ghost-tour guides. [NKST + NPB Cross-Promo]
- Sibling brand for party groups: **NOLA Party Barge**.
- Restoration partner: Sankofa CDC. Bayou Bienvenue is the restoration site.
- 45 SEO blog drafts are already staged in `Marketing/Blog Drafts - Staged/`. The new pages should link to them rather than duplicate them.

## Voice rules (from Brand Story & Values)
- Sound like a local who loves the job. Short sentences, active voice, contractions, real numbers.
- **Say:** guests, book, tour expert, common, frequent, eco-tour, trained naturalists.
- **Never say:** customers, purchase, guaranteed, extreme, "adventure of a lifetime," human agent.
- Keep exclamation marks to a minimum. Never name or bash a competitor. Always say "silent kayaks, not airboats" in positive terms.
- Honesty over hype. Don't promise alligators, and don't oversell Honey Island.

---

## Open questions (resolve before anything goes live)

1. **Price drift. $65 or $69?** Google's booking module shows Manchac at $69 and Extended at $138. The vault says $65 and $130. Every file here uses **$65 / $130** and says "from." If the live FareHarbor price is $69, search and replace across the folder.
2. **Cancellation policy conflict.** The FAQ says cancelling 48+ hrs out gets a full refund and anything later gets nothing. The SMS playbook says 50% inside 48 hrs. The copy here says only "Free cancellation up to 48 hours before your tour," which holds under both. Pick one and fix both source docs.
3. **Affiliate commission.** The partner kit and referral program assume **10% commission** for trade partners and **$10/$10** for guests. David needs to confirm both.
4. **New products that don't exist in FareHarbor yet.** The photo package, cypress planting add-on, conservation donation, bundles and gift-card designs all need FareHarbor items (or add-ons) built before any page promotes them. Kevin Schmitt (FareHarbor) is the contact.
5. **Photographer partner.** The "Private swamp adventure + professional photos" bundle needs a contracted photographer and a rate. The price in 03 is a proposal.
6. **Food partner.** The "Kayak + French Quarter food" bundle assumes Destination Kitchen Food Tours, or another operator, agrees to a joint ticket or a cross-referral. Nobody has contacted them yet.
7. **Cypress planting logistics.** Confirm with Sankofa CDC, or whichever restoration partner we use, the cost per tree, planting season, and whether guests get a certificate or GPS pin.
8. **Instagram handle for sameAs/schema.** entity.json says @nolaswamptours, but the live accounts are @neworleanskayakswamptours and @kayaknola.
9. **Don't create duplicate URLs.** Manchac already has a live booking page, `/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/`, with 7,839 impressions and 194 clicks. Put the new Manchac copy on that URL, or 301 the old one the same day. Honey Island already has two URLs (a category archive and a tour page). Merge them into one before adding anything new. Every new slug in this folder is a *proposal*. Check it against the live site first.
10. **Tour name.** The vault uses "Manchac Swamp Wildlife Tour" and the live site uses "Manchac Mystic Kayak Tour." Pick one and use it everywhere.
11. **Staged blog drafts that contradict this sheet.** Fix these before publishing:
    - `honey-island-vs-manchac-swamp-tour` and `honey-island-swamp-visitor-guide` say alligators are "common" at Honey Island. This sheet says they're rare there, and Honey Island is summer only.
    - The first of those drafts also has a line about operators who "throw marshmallows" at gators. That's competitor-bashing and should come out.
    - Two drafts say Manchac runs "five times a day." This sheet lists four start times.
12. **Drive time.** The docs give 30, 35, 30–40 and 45 minutes. This folder uses **35 minutes**.
13. **Honey Island gaps.** Start times, season dates, launch address, and whether the Rampart shuttle serves it are all unconfirmed.
14. **Bayou St. John.** One draft sells a guided Bayou St. John tour, and the GBP plan lists a rental there. Neither is confirmed as a live product.
15. **Blog URL format.** Some sources say posts live under `/blog/` and others say at the root. Check the live site before building internal links.
16. **Uber policy conflict.** The fact sheet and Tour Pricing both say "don't Uber to the launch." The FAQ says guests can Uber out and take the return shuttle back. Pick one.
17. **Stale stats in Brand Story & Values.** It still says "384+ five-star reviews" (Google now shows 1,401) and "400+ tours, zero injuries," which looks low for a company running since 2013. Update both, or drop them.
18. **Old pickup addresses** (437 Esplanade, 405 Frenchmen) and a **Jean Lafitte** mention are still on the live swamp-tours page. No Jean Lafitte product exists in the vault. Remove it, or confirm it's real.
19. **Public group cap.** Sources say both "10–12" and "12." Separately, the 4-guest minimum for public departures isn't disclosed anywhere a guest would see it.
20. **Return times** on the best-for pages are estimates. Ops needs to confirm them.
