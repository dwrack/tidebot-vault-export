*Split from TheBrain/03 Projects/Active/Funnel Lab (Oct 2026) on 2026-10-15. The TheBrain copy is the cross-brand hub; this folder is the working copy for DCKT.*

# How Did You Hear About Us: DCKT (full file 11, all brands)

Board card c05 (04 card 5): Board: pick = none yet (waiting) / note = (none)

*Added to this folder beyond the nine files in the split brief: file 11 is written for all brands and card 5 points to it.*

# Play 3: "How did you hear about us?" (two versions)

*Drafted 2026-10-14 overnight by David's Claude. DRAFT. Nothing changed in FareHarbor or Periode.*

This one isn't a conversion play. It's the measuring stick for every A/B test in the Funnel Lab. GA4 last-click hides social (the Onera example: under 2% social in GA, 60%+ in guest surveys). Without self-reported source, we'll keep funding whatever GA happens to credit.

## Version A: Question at checkout (FareHarbor custom field)

One dropdown on every FH item's checkout. **Optional, not required.** A required field on a phone checkout is one more reason to bail; optional fields on FH typically still get answered by most guests because it sits next to fields they're already filling.

Options (same list everywhere so brands compare):
- Instagram
- TikTok
- Facebook
- Google search
- Google Maps
- TripAdvisor
- Viator / Expedia / GetYourGuide
- A friend or family member
- Hotel, Airbnb host or concierge
- I've been before
- Other: [short text]

Pros: catches every direct booking, zero follow-up needed. Cons: one more field at the moment of paying.

## Version B: Question after they've paid (confirmation email + day-after text)

No checkout change at all. The confirmation email gets one line with tap links, each link is a tracked URL that records the answer and shows "Thanks, see you on the water."

> Quick one so we know what's working: how'd you find us?
> [Instagram] [TikTok] [Google] [A friend] [Been before] [Other]

Pros: zero checkout friction, works on Periode (E&E) where we can't add fields easily. Cons: maybe 20-35% answer, skewed toward engaged guests. Needs a tiny tap-link endpoint (the fh-lead-engine already serves confirm pages, so it can host this).

## My pick

**A on FareHarbor brands, B on E&E.** If David is nervous about checkout friction, run A on NKST only for 30 days and compare its booking conversion rate to the prior 30 days and to BBK (no change) before rolling out. That's the test.

## Monthly read

Claude pulls the custom-field answers from the FH bookings report on the 1st, tallies per brand, and lays it next to GA4's channel split. The gap between the two is the story.

## Open questions for David

1. Optional (my pick) or required?
2. Roll to all FH brands at once, or NKST-only for 30 days first?
3. Who flips the setting in each FH dashboard? It's one custom field per item (the DCKT analysis counted 39 items on DCKT alone), so bulk-apply if FH allows it.
