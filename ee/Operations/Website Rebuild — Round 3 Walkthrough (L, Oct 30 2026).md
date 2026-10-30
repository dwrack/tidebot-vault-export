# Website Rebuild: Round 3 Walkthrough with L (Oct 30 2026)

Source: voice transcript of L + Davey walking the review-copy canvas (claude.ai/artifact/JhyUH6WM6FNK3bidgaZ6w3), pasted by Davey 2026-10-30. Builds on [[Website Rebuild — Round 1 Feedback (Jonah, Oct 13 2026)]]. Working canvas: claude.ai/artifact/YCeQxCTJbCNiASWciHcVeg.

## Direction
- **Ship an MVP, then add.** Get the new homepage live (iPhone first, desktop right behind), minimal content. Deeper booking features come after launch.
- **Mobile is the priority.** Only ~10% of visitors are on desktop. Mobile's job is booking; PR, press and marketing content live in the hamburger menu.
- **Sunday brunch (Nov 1):** L + Davey pick the hero (mobile + desktop): which video, which photo, final layout. That session gives Claude what it needs to build.

## MVP homepage changes (build now)
1. **Hero:** shorter, landscape video, about half the current height. Use a wide sauna shot (there are plenty of good ones). Final pick at Sunday brunch.
2. **H1 smaller.** Keep "THE COLUMBIA, WARMED." but at a smaller size.
3. **Keep the intro copy** (cedar sauna on the Columbia River, heat up inside, climb down the ladder into the river, do it again), but clean it up so it reads more presentational.
4. **Floating header with a Book button,** always visible. That frees the old Book block below the hero to become "Today's socials."
5. **"Today's socials" right under the hero, front and center.** It skips the Periode booking page and drops people straight onto the session. MVP version: the next 3 social sessions from right now, plus "see more."
6. **Rename "Pick your heat."** It sounds like a temperature setting. Ideas from the call: "Pick your vibe," "Experiences."
7. **Collapse the session types on mobile** (Social, Private Party, Private Sauna 1/2). Stacked full-size they're too much. Use toggles or small modals that open and close.
8. **Remove the sections L flagged as extra** below the hero (exact blocks to confirm against the canvas on Sunday).
9. **Soft opt-in on each page** for people not ready to book, e.g. "not ready yet, email me" (like the "email me when it's pouring" idea). Each page gets its own call to action.

## Events page (can start now)
- Put the two events that are live at the top, then upcoming or potential events.
- Email signup per event ("we'll tell you when it's on").
- "Got an idea for an event night?" and "Book the whole space" asks.
- **Events get their own mailing list**, separate from the main list.

## Later (after MVP)
- Today's sessions as a live list with times, and an expand toggle.
- "Book a social" modal with a real calendar on our site, so people never see the Periode calendar.
- The same for privates: "See available times" pops up Private Sauna 1 and 2.
- Booking that stays fully on our site. **Blocker:** nobody knows how Periode expects payment to work off their page, since it runs through Adyen. Ask Periode.
- Any-hour booking (the "book it any hour" change Jonah worked out) feeds "what's available in the next 1-2 hours."

## Data L asked for: how far ahead do people book? (pulled 2026-10-30)
Periode API, Jul 31 to Oct 29 2026, cancelled bookings excluded, 1,152 bookings.

| Session | Bookings | Same day | Within 3 hrs | Within 24 hrs | Median lead |
|---|---|---|---|---|---|
| All | 1,152 | 33% | 16% | 46% | 29 hrs |
| Social Sauna | 935 | 32% | 18% | 46% | 28 hrs |
| Moonlight Sauna | 37 | 78% | 38% | 78% | 5 hrs |
| Banya | 63 | 37% | 5% | 40% | 54 hrs |
| Private Sauna | 53 | 4% | 2% | 13% | 15 days |
| Members only | 259 | 39% | 19% | 54% | 20 hrs |

Read: about a third of socials book same day and nearly half within 24 hours, so "Today's socials" earns the top spot. It should also show tomorrow, because the other half books further out. Privates book about two weeks ahead, so their module should open on a calendar, not "today."

## Open decisions
1. Hero video or photo (Sunday brunch).
2. New name for "Pick your heat."
3. Today's socials window: today only, or today plus tomorrow.
4. Who asks Periode about payment on our own site (Adyen).
5. Events mailing list: which tool (ActiveCampaign list or a separate one).

### Still open from the canvas "Open Questions" note (Round 2)
6. Private Saunas 1 + 2 opening date (needed for the homepage block).
7. Is Friday daytime priced as a weekday?
8. Live seats: the unofficial Periode read works today. Does L push Periode for an official endpoint? This gates the MVP "next 3 socials" list.
9. Events page (starting now): Wed + Thu times, Aufguss host + insurance, sound bath practitioner, which Thursdays get which.
10. Corporate: confirm whole-dock and weekday-team prices from the Sept 23 buyout draft, plus invoicing, COI and provisions vendor.
11. Ad landing pages: drive times, parking, Banya times, Monday social access, borrow hats?

## Status
- 2026-10-30: walkthrough filed and lead-time data pulled. Waiting on the Sunday brunch picks before building round 3.
