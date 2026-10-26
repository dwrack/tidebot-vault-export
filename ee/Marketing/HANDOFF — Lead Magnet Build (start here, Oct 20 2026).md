# Handoff: build the lead magnet (start a fresh session here)

**PRIZE UPDATE (Davey, 2026-10-20): "Win a weekday date night in our new private sauna."** Two people, one weekday evening (Mon, Wed or Thu), in one of the new private saunas. It ties straight into the date-night searches (Google "date ideas portland" 480/mo peaking in January, DataForSEO Oct 20; TikTok "date night spots portland oregon"). The privates are new inventory, so a prize night doesn't displace a paying Social guest. Open check: the privates aren't open yet. Confirm the opening date. Until then, early winners get the first date nights once they open ("be one of the first couples in"). The perk for every signup is still open; early access to book the privates fits this prize.


**Goal:** an email + SMS lead magnet live by the week of Nov 2, 2026, ahead of the holiday and January search peak. January is the year's biggest month: 7,583 Google search clicks, 3,527 Google profile website clicks and $51.1K revenue (verified Oct 20).

**Decisions (Davey, Oct 20):** see the top of `Lead Magnet — Build Package (DRAFT for review, Oct 2026).md`.
- A weekly draw for a weekday date night for two in a new private sauna (see the prize update above; it replaces the Private Party prize), plus a small perk for every signup. The perk is still open.
- Collect phone + text consent now; texts start only after Twilio approves a refiled registration (A2P).
- The draw popup ships now; the quiz popup comes later.
- Claude builds in test mode; L and Jess review. Nothing goes live without Davey's OK.

**Build order:**
1. **Davey picks the perk.** Then lock the copy in the package.
2. **ActiveCampaign:** form (first name, email, phone, SMS consent, hidden source field), tag `weekday-draw`, 6 emails from package section 4, hosted one-click unsubscribe. Test with our own addresses only. [VERIFY ActiveCampaign API access and key location, local only]
3. **/draw landing page + rules page:** draft in Squarespace as unpublished pages, or hand Jess the copy.
4. **Popup + banner:** prepared but not enabled; Jess or Davey flips it live.
5. **Weekly draw script on mbp-2:** picks a random entrant from the week's tag and DMs Davey. A person sends the winner notice and the Periode code.
6. **Twilio refile:** once the form is live, resubmit the registration using it as the opt-in proof. Draft the resubmission for Davey; don't submit it.
7. **Social:** launch Reel, carousel and TikTok scripts (package section 6) go to Kimberlynn in #marketing as a draft for Davey's OK.

**Related files (Marketing/):**
- the lead magnet concept doc and build package
- `Kimberlynn 1-1 Agenda (Oct 20 2026)`
- `Davey + Jonah Agenda — Marketing (Oct 2026)`
- `Seasonal Keyword Calendar — Rain + Every Month (Oct 2026)`
- `TikTok Keyword Content Plan (Oct 2026)`
- `Keyword & Content Opportunities (Oct 2026)`

**Dashboard:** https://claude.ai/artifact/BhshKhxmB5r1NQo4TY3cE4. It has 10 tabs, including Year. Revenue still stops at Oct 12 because Periode's Oct 1–18 export was stuck in their queue on Oct 19; re-run it from Reporting → CSV.

**Other open items:**
- **Instagram shares per post:** the meta-organic connector was patched (backup `index.js.bak-20261019`). Reconnect it with /mcp, then add shares to the Instagram tab.
- **Christmas Ships blog post:** publish by Oct 23.
- **Rainy-day pillar post:** publish by Oct 23.


## Website tie-in: new site + new pricing (Davey, 2026-10-20)

Davey wants the draw built into the new site with the new pricing, and wants a real countdown so we stay on people.

**The countdown is the weekly draw itself.** Entries close every Wednesday [PLACEHOLDER: close time, e.g. 9 AM PT] and the clock resets after each draw. It's a real deadline every week, not fake scarcity, and it gives every email and the banner a reason to say "closes in 2 days."

**Where it shows up on the new site (Design canvas https://claude.ai/artifact/YCeQxCTJbCNiASWciHcVeg, publish as the next R2.x label + version-log row):**
- **Banner, every page:** "Win a weekday date night in our new private sauna. Next draw in [2d 14h] →" Live countdown to the next Wednesday close; tap goes to /draw.
- **/draw page (new board, iPhone + desktop):** hero photo of a private sauna [PLACEHOLDER until V2 photos], what you win (2 people, one weekday evening Mon/Wed/Thu, Private Sauna 1 or 2), the big countdown, the ActiveCampaign form (first name, email, phone + SMS consent box, hidden src), rules link, and under the form the price ladder so entrants see what a normal visit costs.
- **Popup, once per visitor:** same offer + countdown. Suppressed on booking flows, on Google Ads clicks (gclid or utm_medium=cpc) and for members (package section 0).
- **Private Saunas page:** a "Win a date night in here" strip above the price line, linking to /draw.
- **Abandoned booking on our own form** (Astro Build Spec): if someone starts a booking and leaves with an email entered, they go into the same ActiveCampaign list with tag `abandoned-booking`, not the draw tag.

**Pricing in every price line and email = Jonah's 10/12 #pricing-revamp model, still placeholders until he confirms 11/1:**
- Weekday 1 hr $35 / 2 hr $50; weekend 1 hr 45 $60
- Private Sauna 1 + 2 (up to 4): $200 weekday / $250 weekend; Private Party (boat, up to 12): $500 / $600
- Memberships: Weekday $100, Anytime $150; punch passes 5 for $225, 10 for $400
- The prize line says "a $200 weekday private night" only once $200 is confirmed.

**Nurture emails pick up the new prices (package section 4):** the "still want to come?" email leads with the cheapest real first step, the $35 weekday hour, then the Weekday membership for people who come back. No invented discount; the draw is the hook and the regular price is the close.

**Launch order (because the new site won't be live by Nov 2):** ship the draw on Squarespace first using the same ActiveCampaign form embed and the same /draw copy, then move it onto the Astro site at cutover. Same form, same tags, so no list split.

**Still open:** Davey's perk for every signup (early access to book the privates fits), draw close day and time, privates opening date, Jonah's final 11/1 prices.
