# Website Rebuild — Static Site Plan

**Status:** Approved direction, parked until Davey returns from vacation (~Sept 9, 2026)
**Decided:** Aug 26, 2026

## The decision
Rebuild ebbandember.com as a static site. No Squarespace, no Webflow, no CMS.

- **Stack:** Astro (static HTML) + GitHub repo + Cloudflare Pages
- **Cost:** $0/month hosting (vs ~$23/mo Squarespace). Domain renewal only.
- **Why:** fastest possible (edge-served static), most secure (no server/plugins/admin to hack), highest design ceiling (custom code = Bathhouse/Sky Lagoon tier, not template tier). Claude maintains it directly via Git; content edits are markdown.
- **Tradeoff accepted:** no browser editor for Jess/Hannah. Site changes route through Davey → Claude.

## First action when back
Claude builds a **prototype homepage** — dark, photo-led, Bathhouse NYC / Sky Lagoon register, using real photos from `Assets/Photos/` (respect PRIVACY-HOLD tags). Davey judges the visual ceiling before committing further.

## Design references
- bathhouse.com — closest vibe: dark, moody, booking-first
- othership.us — ritual language, session flow
- skylagoon.com — cinematic full-bleed video
- loylyhelsinki.fi — Nordic waterfront minimalism
- Fonts: BASAL display only, Inter everywhere else

## Launch checklist (cutover, not build)
Target cutover: **October shoulder season**, not during the summer revenue run.

1. **DNS first:** confirm where domain is registered (if Squarespace, transfer out). Move DNS to Cloudflare. Preserve Google Workspace MX, ActiveCampaign domain auth, SES records — email breaks silently if botched.
2. **301 redirects** for every current URL, incl. the queued /wellness→/experiences rename.
3. **Port the Periode tracking bridge** (footer script: fbclid/gclid/client_id forwarding) day one, or ad attribution goes dark again.
4. **Re-point every inbound link:** Google Ads final URLs, Meta ads, GBP website field, IG bio, lodging partner links, printed QR codes.
5. **Carry over:** FAQPage schema (25 Q live), GA4 + Meta CAPI, AI-crawler-open robots.txt.
6. **Build the never-shipped pages while in there:** /journal blog, /cold-plunge-portland, /private-sauna-rental-portland (per 90-day AI SEO plan).
7. **Email capture** wired to ActiveCampaign (replace old opt-in form/sheet flow).
8. **Rules still in force:** About page = "the team" only (no founder names until Dustin resolves); PRIVACY-HOLD photos need member OK.
9. Heads-up to Jonah before killing the Squarespace bill.

## Open questions for Davey
1. Green-light the prototype homepage build?
2. Where is the domain registered? (determines DNS transfer step)
3. Tell Jess/Hannah about the no-browser-editor tradeoff now or after prototype?
