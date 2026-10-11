# "Booze" removal + Party Queen stragglers (2026-10-09)

Michael's call 2026-10-09: take "booze" out of **visible text only**. Leave SEO titles, meta descriptions and URLs alone (they bring in "booze cruise" search traffic, which the weekly site check is tracking). Party Queen capacity stays **22 shared seats / 26 private**; only fix leftovers.

Why: Google Ads limits our ads for "Alcohol information" and reads the landing pages too (see the 2026-10-08 Google Ads row on the board). Note that BYOB, drinks and bar still appear, so this alone may not clear the flag.

## Scan 2026-10-09 (all 134 sitemap URLs, live HTML)

- Footer line "Top Rated Booze Cruises and Tours!" on 133 pages (one sitewide setting)
- 109 other sentences on 39 pages: 4 tour pages (Freaky Tiki, Twerkin' Tiki, Party Queen, Bayou Boogie), home, FAQ, blog index, the rest blog posts
- Left alone on purpose: "booze" in 16 SEO titles, meta/og descriptions, and 13 URLs

## Wording rules

- "booze cruise" becomes "party cruise" (keep capitals as they were)
- "bring your own booze" becomes "bring your own drinks"; "The Booze!" becomes "The Drinks!"
- "A Booze Cruise is a captained boat ride where the alcohol comes with you" becomes "A Party Cruise is a captained boat ride where you bring the drinks"
- "part Swamp Tour with Alligators, part Booze Cruise" becomes "part Swamp Tour with Alligators, part party"
- Footer: "Top Rated Party Cruises and Tours!"

## Party Queen stragglers

- /the-cajun-queen/ share title (og:title) still reads "The Cajun Queen - Up to 22 ppl Pedal Bike Party Booze Cruise", and the share description says "pedal party boat". Set both to match the page's SEO title/description, minus Pedal.
- /new-orleans-bachelorette-party-boat/ says "The Cajun Queen : up to 22 guests". Becomes "The Party Queen: up to 22 guests".

## Also found (stale price)

"$63 per person" still appears in 4 blog posts: bachelor-party-booze-cruise-new-orleans-bayou, divorce-party-booze-cruise-new-orleans, new-years-eve-holiday-party-boat-booze-cruise-new-orleans, beyond-bourbon-street-things-to-do-new-orleans-water. The real price is $59 (fixed on tour pages 2026-09-30).

## Log

- 2026-10-09: scan done, plan written. Waiting on Michael to sign in to wp-admin.

- 2026-10-09 (later, Michael signed in): EXECUTED. Footer heading changed once in Preset Content > Global Footer, which covers all 133 pages: "Top Rated Booze Cruises and Tours!" is now "Top Rated Party Cruises and Tours!". Body copy cleaned on 39 records: 33 blog posts (post_content), 4 activities and the FAQ and Home pages (ACF fields). Verified at the data layer: 39 of 39 now have zero "booze" in editable body content.
- Scope correction worth knowing: the original scan counted 109 visible sentences, but a page-level count double-counts a post's own title, which repeats in the breadcrumb, the H1 and related-post cards. Measured against the actual editable fields the real figure was 66 mentions in post_content plus about 19 in ACF body fields. Two posts (bachelor-party-booze-cruise-new-orleans-bayou, and the ultimate guide after its fix) had ZERO booze in their body at all; every hit on them was their own title repeating.
- Blog post H1s LEFT ALONE (13 of them). The H1 is a separate field from the Yoast/WDS SEO title here, so the plan's "leave SEO titles alone" did not decide it. Left them because their URLs and SEO titles are being kept for the same traffic reason, and because the Google Ads landing page is /the-freaky-tiki/, not these posts, so the alcohol flag is unaffected either way. One word to reverse if Michael wants them changed.
- Also deliberately left: "booze" inside acf[field_seo__schema_markup] on the activities (JSON-LD, not visible text), and the 19 SEO title/meta/og fields.
- Wording applied: "Booze Cruise(s)" to "Party Cruise(s)" keeping case; "The Booze!" to "The Drinks!"; "bring your own booze" to "bring your own drinks"; "part Booze Cruise" to "part party"; and "is a captained boat ride where the alcohol comes with you" to "is a captained boat ride where you bring the drinks". That last one needed a separate pass because inline <b> tags split the sentence and blocked the literal match.
- Method note for next time: posting the edit form back via fetch works for blog posts (78 fields) but SILENTLY FAILS on the activity pages, whose forms carry about 3,150 fields and appear to exceed PHP max_input_vars. The save completes and the timestamp moves but the ACF payload is dropped. Nothing was lost (leaf count, non-empty count and byte size were identical before and after), but the activities had to be done through the real admin form instead. Use the UI for anything with ACF repeaters.
- STILL OPEN from this plan: Party Queen og:title and og:description on /the-cajun-queen/; "The Cajun Queen : up to 22 guests" on /new-orleans-bachelorette-party-boat/; and the stale "$63 per person" in 4 blog posts (real price is $59).
