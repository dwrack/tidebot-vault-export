# Blog Automation — SERP Funnels for Austin Paddle Shack + Honey Island

*Created 2026-06-19. David: "more funnels for people to get into a kayak and more SERP real estate. super easy now that I have you to automate blog creation, posting, etc." Start with these two cloned brands; extensible to the rest.*

## Goal
Stand up automated, brand-voiced blog content on austinpaddle.com and honeyislandswampkayaktours.com to grab SERP real estate for local kayak intent and funnel readers into a booking. Same SERP-domination logic as the Door County cluster: own the results, push competitors off page 1.

## Why now / what changed
Both brands now have real Brand Story docs (written 2026-06-19), so the voice is defined and the `seo-blog-writer` skill can write on-brand instead of generic. That was the missing piece.

## Approach
1. **Keyword/topic map per site** (use `seo-audit` + GSC):
   - **Austin Paddle Shack:** Lady Bird Lake kayak rental, SUP rental Austin, paddleboard downtown Austin, "kayak behind Cidercade," bat-bridge paddle (rental angle — keep guided bat *tours* on the sibling Austin Kayak Tours). Don't blur the two brands.
   - **Honey Island Swamp Kayak Tour:** kayak swamp tour near Slidell / New Orleans, Honey Island Swamp wildlife/birding, kayak vs airboat, Honey Island Swamp Monster legend (its OWN folklore — keep Manchac/Julia Brown on NKST). Fix the Manchac/Maurepas FAQ leak on the live site first.
2. **Generate posts** with `seo-blog-writer`, loading each vault's Brand Story for voice. Every CMS field (H1, meta, FAQ schema, etc.) per the skill.
3. **Publish** to each WordPress site (FareHarbor/WP-VIP theme). Mind the theme's Schema Markup rules (raw JSON, no script wrapper, no escaped inner quotes).
4. **Internal links** from each post to the booking page — that's the funnel.
5. **Cadence:** start with a small batch per site, measure GSC impressions/positions, then scale.

## Guardrails
- Keep Austin Paddle Shack (rentals/SUP) and Austin Kayak Tours (guided bat tours) on **separate** keyword lanes. Same for Honey Island vs NKST/Manchac. Don't let the cloned brands cannibalize their siblings — differentiate intent.
- Staged for David's approval before anything publishes (per the approve-before-vault-writes / approve-before-posting rules).

## Sequence
Brand Story docs done → topic map → draft batch → David approves → publish → measure → scale to other brands.
