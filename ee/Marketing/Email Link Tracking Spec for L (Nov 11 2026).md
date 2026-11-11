# Email Link Tracking Spec for L (Nov 11 2026)

Sent to L via Slack DM (Claude app) on 2026-11-11 pending Davey's OK. Open item on the dashboard until she confirms after her first send.

## Why this works
- GA4 G-YF8FPEWW4S runs on ebbandember.com (Squarespace footer today, `a/track.js` on the Astro rebuild, verified 2026-11-11 on both hosts).
- Periode checkout lives on minside.periode.no and fires purchases server-side (GA4 Measurement Protocol + Meta CAPI).
- The site script staples the GA4 client_id/session_id (plus gclid/fbclid) onto every minside.periode.no link, so a booking stitches back to the email session ONLY if the click lands on ebbandember.com first.
- A link straight to minside.periode.no skips the site, so the booking lands as Unassigned / (not set).

## Rules for L
1. Every link points at an ebbandember.com page. Never link straight to minside.periode.no.
2. Every link carries UTMs, lowercase, hyphens, no spaces:
   - utm_source=email
   - utm_medium=newsletter | drip | members | draw | transactional
   - utm_campaign=YYYY-MM-DD-short-name (e.g. 2026-11-18-new-pricing)
   - utm_content=hero-button | text-link | photo | footer (which link in the email)
3. Unsubscribe and preference links get no UTMs.
4. If the email tool has an "add Google Analytics / UTM to links" toggle, turn it on but set the values to this pattern (it will default to its own names otherwise).
5. Keep the tool's own click tracking on. We read both: tool = opens/clicks per link, GA4 = pages visited and bookings.
6. Send Davey the utm_campaign name before each send so the GA4 report is ready.

## What we see afterwards
GA4 Traffic acquisition filtered to source=email: sessions, pages, begin_checkout (Periode click) and purchase by campaign and by utm_content. Realistic ceiling: ~50-60% of bookings stitch to a session (repeat guests who book from a saved Periode link never touch the site).
