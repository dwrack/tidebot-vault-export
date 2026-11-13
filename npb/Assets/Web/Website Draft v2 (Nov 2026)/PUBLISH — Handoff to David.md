# Publishing the new NolaPartyBarges.com — handoff to David (2026-11-11)

This folder is the full build. Everything the page needs is here: `index.html`, `styles.css` and `img/`. There's nothing to install or compile. It's plain HTML and CSS, and the fonts load from Google Fonts.

## Permissions (updated 2026-11-13)
**David has full permissions on this project.** That means editing, restructuring, deleting, choosing the host and publishing, without asking Jeffrey first.
- This vault folder is now the **only** copy of the site. Jeffrey's Mac points at it too (`~/Projects/npb-site` is a link to this folder), so there's no private copy that can drift.
- Your Claude can work directly in this folder.
- Unused photos are in `img/unused/`. Delete them if you don't want them.
- Log big changes or the launch on the Who's On What board so Jeffrey and Michael can see what changed.

## Pick a route
**A. Keep WordPress (the current host).** Rebuild the page as a WordPress page or template using this HTML and CSS. Booking and blog links keep working, and you keep the WP admin. The work is putting the markup into the theme. A page builder's "Custom HTML" block plus the CSS in Additional CSS gets you there fastest.

**B. Static host (Netlify, Cloudflare Pages or similar).** Drag this folder onto the host and point the domain at it. It's the fastest and simplest option. The catch is the existing WP pages: blog, landing pages and corporate pages need redirects or a subdomain, or they go dark.

Before you switch DNS, check what else lives on the WP install. Old URLs that get traffic or ads should 301 to the new page, or keep running.

## Must do before it goes live
1. **Newsletter form.** The form near line 215 of `index.html` (`action="#"`, `data-todo="connect to GHL list"`) goes nowhere right now. Swap in the GHL form embed or webhook.
2. **Logo.** The header and footer wordmark is typed text in the logo colors. Swap in the real logo file if you'd rather. It's not in the vault yet.
3. **Favicon.** None is set yet.
4. **Prices to confirm:**
   - Pontoon $371 (worked out as $350 plus the 6% fee).
   - Eco Tour length and kids' pricing. The page says 1 hr 45 min, ages 13+. The old site said 2 hr and $30 per child.
5. **Domain consistency.** The canonical and og:url tags use `https://nolapartybarges.com/`, while the JSON-LD image uses `www.`. Match them to whichever host you serve from.
6. **Images.** The `img/` folder is about 2.8 MB. Run the photos through a compressor or convert them to WebP before launch.

## Don't change without checking
- **FareHarbor links.** Every booking link carries `ref=site-v2-...` so bookings can be credited to the new site. Keep the ref tags.
- **Prices.** They're shown with fees included and are never hidden behind an email. That's the house standard for every site.
- The Party Queen capacity is 26 here, which fixes the "22" on the live site.

Questions → Jeffrey.
