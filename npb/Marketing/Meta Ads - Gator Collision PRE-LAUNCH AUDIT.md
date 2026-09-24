# Gator Collision: pre-launch audit

Run 2026-09-22, after publishing paused and before turning delivery on.

## Verified good

**Campaign** `52578687844700`
- Objective Sales. Campaign budget **off**. "Share some of your budget with other ad sets"
  **unchecked**, so no bleed between ad sets.
- Campaign toggle **off**. All four ad sets read "Campaign off". Spending nothing.

**Ad sets**, all four identical except name
- Daily budget $40.00 each. $160/day total.
- Conversion location Website. Performance goal **Maximize number of conversions**.
  Bid strategy Highest volume. Delivery Standard. Runs ongoing.
- Locations: New Orleans, Louisiana, US, 50 mile. Minimum age 24. Gender All.
- Detailed targeting: Interests, Nightlife (bars, clubs & nightlife).

**Ads**, all four
- Facebook Page: New Orleans Party Barge. Instagram: nolapartybarge.
- Website URL: `https://nolapartybarges.com/the-freaky-tiki/`
- Meta Pixel: GT Pixel- NPB, Kayak `701301873334767`
- Format Single video, Creative source Manual upload, Multi-advertiser ads **Off**.
- AI off: text improvements, video touch-ups, translation (0 languages), no AI images.

**The thing that decides whether this test can work:** the pixel's **Purchase event is
Active**, delivered through the Conversions API, currently in use by two live ad sets. The
optimization target is real, not theoretical.

**Landing page** loads and matches the ad copy: $63, $1,250, 1 hr 45 min.

**Alcohol policy:** minimum age 24 clears Meta's 21+ floor for alcohol-related ads.

---

## Flags, none of them blockers

1. **Targeting expansion is on.** Meta can reach beyond the Nightlife interest. It applies
   equally to all four ad sets so the comparison still holds, but treat "Nightlife" as a
   hint rather than a hard constraint.
2. **Facebook right column will not deliver.** A 9:16 video does not fit that placement,
   which wants a static image. Low-value placement for a mobile-first audience. Ignore it.
3. **Event match quality 6.2/10, "Update recommended."** Events Manager also flags "$146 ad
   spend affected by low data quality" on this pixel. Not blocking, but it makes
   optimization less precise than it could be. Worth a separate cleanup pass.
4. **The landing page title still says "New Orleans Pedal Barge."** The page body has zero
   "pedal" mentions, but the SEO title does, and that shows in the browser tab and in
   search results. Breaks the no-pedal rule outside the ad itself. Worth fixing on the site.
5. **Advertiser and Payer transparency fields are blank.** Ads Manager shows "Please add"
   in review, but the field is labeled **optional**. Not a blocker.
6. **The kayak draft is still queued.** "New Orleans Kayak Swamp - Video views", change
   "Updated: Ad status", still erroring. Left unpublished on purpose. Unrelated to this
   campaign.

---

## Verdict

Nothing found that should stop launch. The structure, targeting, creative, tracking, and
destination all check out, and the one thing that could have made the test worthless (no
Purchase signal) is confirmed working.

Turn it on at: Campaigns > NPB | Purchase | Gator Collision | Sept 2026 > Off/On toggle.
That starts $160/day.
