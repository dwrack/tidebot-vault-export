**Recommendation: build the new site on C. Second Line.** All three judges picked it, and it scored highest on every lens (7.7 of 10). It's the only first phone screen that feels like a party, and its crew builder gets a group to a real FareHarbor time in about 4 taps.

As of 2026-10-08. Scores are from the judges' pass, before each direction's fix round. All 8 prototype pages re-checked today: PASS, 0 fails.

| Direction | Score | Best at | Biggest weakness |
|---|---|---|---|
| **C. Second Line** (pick) | 7.7 | Party-poster first screen with "$59 a seat" on the Check dates button. Crew builder books an exact time, and the group-chat link reopens the same plan | Parade-poster look says "New Orleans" more than "our boats." Builder figures are hand-drawn stand-ins |
| A. Painted Hull | 6.7 | Most ours: real Freaky Tiki hull lettering, the boats' awning stripe, a price board that flips from seat to whole boat | Only one boat has real lettering. Heavy headings on a long page |
| D. Lights On | 6.3 | Flips from day to the real night photo of the pink-lit tiki. Both prices on every card | Day mode, which ad traffic sees, is the plainest. Night runs on one photo |
| B. Big Sky | 5.8 | Real sky and tonight's sunset time from the actual sun over the marina. Best type | Reads calm, closer to the eco tour than a party. Longest page |

## How to view

- On the Mac: open `~/Projects/npb-site/design/index.html` (double-click it in Finder). Tap a screenshot to open that homepage. Each card also links its Freaky Tiki page.
- Quick look: `~/Projects/npb-site/design/compare-mobile.png` shows all four first phone screens side by side.
- These are prototypes. Booking buttons open the real FareHarbor checkout, so don't finish a booking. Text sign-ups never send.

## 6 calls before the build starts

If you don't answer, the default ships (except #1).

| # | Decision | Recommended default |
|---|---|---|
| 1 | DNS: who logs into Squarespace Domains, which Cloudflare account takes the zone, and will FareHarbor (Kevin Schmitt) send the full DNS export and the WP VIP origin hostname, and keep the old site and zone up for 30 days? | No default. This is the hard blocker. Ask FareHarbor this week and turn on domain auto-renew now (it expires 2027-02-07) |
| 2 | Guest faces in the hero (the tiki-pass and bead-toss loops have no release on file)? | Drone loops only until you say yes. A yes is the easiest way to get a party into the first screen |
| 3 | Primary logo: palm sunset or tiki wordmark, and where's the vector? | Palm sunset mark. It's the only one with files, and it matches Google and the socials |
| 4 | Text sign-up: launch the opt-in before a sender number is approved? | Yes. Buy the new toll-free number first so the disclosure can name it. Box starts unchecked, sign-ups get collected, nothing sends until it's verified. Seat alerts stay hidden until then |
| 5 | Drinks wording (ATC permit): can the site mention drinks with the seafood boil, "first drink included" or champagne packages? | No. "Sunset Cruise & Seafood Boil," food and cruise only, packages hidden |
| 6 | Legal name and address on the Privacy, Terms and SMS Terms pages (the old page says Milwaukee, Twilio says Wauwatosa)? | "Gravity Trails LLC, doing business as NOLA Party Barge," with the address on the approved Twilio brand. No owner name |

## What happens next

1. You reply "go with Second Line" (or pick another one) and answer what you can above.
2. Ask FareHarbor about DNS this week. The DNS move (step A) doesn't wait on the new site, and nothing visible changes.
3. Build on the pick in Astro, about 3 to 4 weeks. It folds in the best parts of the others (Painted Hull's seat chips that follow the price toggle, the builder fixes for 6-person groups and multi-day times) and self-hosts the fonts.
4. Shoot list: straight-on hull shots of every boat (for lettering), the blue building and three flags for Getting Here, and the LED rail lights at night.
5. Cutover in two steps (DNS first, then the site). Not Oct 24 to Nov 1, and not the week before Thanksgiving.
