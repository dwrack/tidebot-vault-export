# Website Rebuild: Handoff Brief (Nov 2 2026, night)

One working session for the website from here on: **Social Ember website**. This brief folds in everything from the "meeting notes / FAQ / SEO" session.

## Unshipped changes in `~/dev/ee-site-preview` (not deployed)
- `index.html`: live conditions box under the hero CTAs: River now (USGS 453630122021400, Columbia near Dodson, CORS ok), Air now (NWS KPDX), "River by season 41°F winter · 72°F August". Shows n/a if a feed fails. Tested on mobile locally (57°F / 48°F on 11/2). Backup of the prior page: scratchpad `index.before-temps.html` of the old session.
- `_redirects`: /home, /home/ -> /, /fitness -> /wellness, /cart -> /shop (301).
- Deploy failed from that session: the project moved to the sauna@ Cloudflare account. Deploy from here with the new account's credentials.

## Decisions (Davey, 11/2)
- New prices live Mon 11/23 (announce 11/15). Site launches on them; nothing priced goes public before.
- Hours 6am to 10pm. Sessions: 1 hr booking = 45 min use + 15 changeover; 2 hr = 1 hr 45 min + 15.
- Swimsuits required in the social sauna and sauna-boat private parties; optional in Private Saunas 1 + 2 (open by Thanksgiving).
- Stoves are natural gas fired (OK to say; never wood, never propane).
- Sauna-boat private parties up to 12 (Davey "I believe").
- Keep every old URL exactly: /, /faq, /memberships, /wellness, /shop, /joinus, /best-saunas-portland, /privacy, /terms-of-service.
- Mobile header hides on scroll, shows on stop; desktop fixed. Flame-only logo on small phones.
- L owns ActiveCampaign lists for all signups.

## Build list (also the "Website rebuild" row on the in-flight dashboard)
1. Move "On the dock every week" right after Find your ritual.
2. Add a Reviews section (CSS exists, no section).
3. Rename to "Ways to wellness".
4. Swap Sauna Credit for gift card (Jonah's 11/1 plan).
5. Trim repeat "Columbia" in hero copy.
6. Restore the earlier How it goes formatting.
7. Confirm small-phone flame logo; test with phone zoom on.
8. Private sauna names once settled.
9. Hero photo from Jonah's camera when shot.
10. Launch with new prices 11/23.
11. Keep old URLs (map file below).
12. SEO: title + H1 "Portland Floating Sauna + Columbia River Cold Plunge"; add LocalBusiness + FAQPage schema, OG tags, canonical; keyword H2s under the brand kickers; remove noindex from page AND `_headers` at launch.
13. Add the 8-question homepage FAQ (draft below; open blanks: parking line, social capacity 8?).
14. Later: live inside-sauna temp once Tuya is set up (Inkbird ITC-308 is Tuya; watchdog code on mbp-2 needs `~/.config/ee-stove-watchdog/tuya.env`; Davey makes the Tuya IoT account and moves the thermostat to Smart Life).

## Files
- Meeting notes: `Meeting Notes/Website Working Session + Dock Ops (2026-11-02).md`
- Site plan: `Operations/Website Rebuild — Pricing Funnel + Site Plan (Nov 2026).md`
- URL map: `Operations/Website Rebuild — URL Map (Keep Old URLs).md`
- FAQ + AI plan: `Marketing/Homepage FAQ + AI Visibility Plan (Nov 2026).md`

## Still open
- Wednesday 11/4 working session with L: calendar event needs L's email + a time.
- Neighbor discounts (scratch?), "apply to join" membership, private sauna names.
- In-flight dashboard auto-refresh (laptop `com.ebbember.inflight-dash`) failed 11/2: headless Claude couldn't load Artifact tools. Manually refreshed.
