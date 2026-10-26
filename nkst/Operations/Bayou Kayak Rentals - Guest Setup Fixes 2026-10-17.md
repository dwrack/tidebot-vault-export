# Bayou Kayak Rentals: guest setup fixes (2026-10-17)

**CURRENT STATUS (verified 2026-10-17):** Section 1 feedback text LIVE (hold off). Section 3 booking notes LIVE in FareHarbor (only booking_notes changed; old copy saved as "Bayou Kayak Rentals - Booking Notes BEFORE 2026-10-17.txt"). Rentals also pulled from the summer catch-up review texts (27 pending skipped, 114 follow-ups cancelled). Section 4 not done.

## 1. Post-rental feedback text (replaces the Google review ask for rentals)

Sent ~90 min after the rental ends, from the NKST review number (+1 504-226-5402). Replies relay to the NKST staff phone (504-571-9975). One text only, no 2-day nudge.

> NOLA Kayak Swamp Tours: Hi {first}, hope the bayou treated you well! Self-guided rentals are brand new for us, so we want your honest take. What worked, what didn't? Just reply here. STOP to opt out

Go-live: set `"hold": false` on the `rental` entry in `item_overrides`, `~/Projects/fareharbor-brief/review-sms-nkst/config.json` on mbp-2.

Already sent before this change: Etienne Auriol (10/13 rental) got the review ask + nudge. Spencer Dohr (10/17) got the review ask; his 10/19 nudge is now cancelled.

## 2. What guests see before they arrive (problems found)

Sources: FH item "Bayou Kayak Rentals" (pk 225451) description + booking notes, and the linked Go Guide Map doc.

- **Expectation gap.** It sells under a swamp-tour brand, but Bienvenue is open marsh with utility poles and shipwrecks, not cypress swamp. Nothing says that. The upsell even tells them they'll "miss" wildlife on their own.
- **Wind isn't mentioned in the booking notes.** Open water plus a 15 mph breeze is the single fastest way to a bad rental. The Go Guide gives it half a line.
- **The essentials are buried in a Google Doc.** Lock code, help number, and route only live in the doc. The help number (504-571-9975) isn't in the confirmation at all.
- **Lock code is vague.** "You will receive a code... if not, they're unlocked." Who sends it and when isn't stated.
- **Conflicting place names.** Booking notes say "docks at Nola Party Barge, 2101 Paris Road." Transportation notes say "Eddie Pinto's Marina" with a $5 parking fee.
- **Time doesn't line up.** Listing says 3 hours, the route says 2 hours, and nothing tells them when to turn around.
- **Tone.** "We consider taking the kayak THEFT" in the Go Guide reads hostile to a paying guest.
- **Typos.** "Renals," "Tranportation."

## 3. Rewritten FH booking notes (paste-ready)

```
Thanks for booking a Bayou Kayak Rental! Self-guided rentals are new for us, so here's everything you need for a great paddle.

WHAT THIS IS
A self-guided paddle on Bayou Bienvenue, an open marsh 15 minutes from the French Quarter. No guide and no staff on the dock, so it's just you, the birds, and a lot of sky. You'll see herons, egrets and pelicans for sure. Gators show up sometimes, not always. If you're picturing a guided trip through cypress trees and Spanish moss, that's our Manchac Swamp Tour (link at the bottom), and we're happy to switch you.

BEFORE YOU COME (5 minutes)
1. Everyone in your group signs the waiver (link above). Forward this email to your group.
2. Read the Go Guide Map: https://docs.google.com/document/d/1s7_tNeHSpRaA3gtBrB2Sb38bHtyN9fhlUBW30IXHtfE/edit?usp=sharing
3. Save our number: 504-571-9975. Call or text it if anything is off, on land or on the water.

CHECK THE WIND
Open water + wind = hard work. If it's breezy, paddle INTO the wind first so the trip back is easy. If you see whitecaps, stay close to the marina and text us.

TIMING
You have up to 3 hours. The suggested loop takes about 2 hours at an easy pace. When you hit half your time, head back.

GETTING THERE
2101 Paris Rd, New Orleans, LA 70129. Look for the NOLA Party Barge sign. Parking is $5. There's construction on Paris Rd, so turn right onto the gravel road just past it.

BRING
Water, sunscreen, hat, sunglasses, shoes that can get wet, and a zip bag or dry bag for your phone. Life jackets are provided and required. No swimming.

WHEN YOU'RE DONE
Kayak back to the launch, paddle on the rack, life jacket in the bin, lock it up, and snap a photo of the returned kayak to the email in this confirmation.

After your paddle we'll text you to ask how it went. Honest answers help us make this better.

WANT THE FULL SWAMP?
Our guided Manchac Swamp Tour goes deep into cypress swamp with a local guide: https://neworleanskayakswamptours.com/tours/swamp-kayak-tours/manchac-mystic-kayak-tour/
```

## 4. Small fixes

- **FH description:** add one line: "Self-guided, open-marsh paddle. No guide. Best on calm mornings."
- **Transportation notes:** replace "Eddie Pinto's Marina" with "2101 Paris Rd (NOLA Party Barge sign)." Fix "Renals" in the cancellation notes.
- **Go Guide doc:** swap the THEFT line for "Please sign your waiver before you launch. It's in your confirmation email." Put the phone number at the top. Add the wind rule. State who sends the lock code and when.
- **Still needed: the 2 sub-par rental reviews.** Not found on the NKST or NPB Google listings as of 10/17. Need to know where they are (FH, TripAdvisor, Viator?) to confirm these fixes hit what they complained about.
