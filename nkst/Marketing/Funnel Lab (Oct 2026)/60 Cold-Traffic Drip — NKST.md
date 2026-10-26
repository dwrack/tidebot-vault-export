# The trip-planning drip: cold traffic to NKST, no asks

*Drafted 2026-10-16 from David's brief: "We really need to have an amazing funnel and drip campaign to convert this cold traffic. Talk about the guides, other restaurants, get people hyped about the city, introduce them to the To-Go Cup newsletter style, show them more videos, only amazing photos, no asks for a sale, make it a really enjoyable part of their trip planning." DRAFT. Nothing built, nothing sent. Full funnel focus; cards 7 and 8 wait on this.*

## The funnel in one picture

```
Cold ad or post (Meta, IG, TikTok, the alligators-vs-crocodiles blog post)
        |
        v
The 30-second quiz  (Which swamp tour fits you? / What kind of swamp creature are you?)
   asks: ever kayaked, who's coming, live here or visiting, what you want to see, when, how'd you find us
   email unlocks the result (card c19 = B)
        |
        v
The trip-planning drip (this file): 8 emails over 2 to 3 weeks, timed to "when"
   the city, the guides, the swamp, the food, the videos. One quiet link per email. No sales ask until the end.
        |
        v
The To-Go Cup (biweekly city newsletter) picks them up after email 8
        |
        v
Booking, read in FareHarbor by ref tag (q-<lead id> on quiz links, tgc<NN> on newsletter links)
```

Two things the data already told us (Funnel Lab files 01 and 02): 65% of lead-form fills live in New Orleans and 33% have never kayaked, and the #1 question before booking is where we meet. So the drip has a local lane and a visitor lane, and "where we meet" shows up early and plainly, not as a pitch.

## Rules for every email

- **No ask until email 8.** Emails 1 to 7 have one quiet link each ("see the tour" or "watch this"), never a button that says Book, never a price in the subject.
- **One photo, full width, and it has to be great.** Real tour photos only (Assets/Carousel Picks has 20 picked already). No stock, no AI images.
- **One video where we have one.** The NKST YouTube channel (rebuilt June 2026) carries the swamp films; each email that has a natural video embeds a thumbnail that links to it.
- **Guides are people, not a roster.** Nick, Alex, Stephanie each get an email with their own photo and two real lines from reviews. Guide's OK first.
- **The city gets equal billing.** At least three of the eight emails are about New Orleans, not the swamp.
- **Honest wildlife.** Alligators are common spring through fall and go quiet below 65 F. Never "guaranteed." Never "completely safe."
- Signed "The crew at New Orleans Kayak Swamp Tours". Plain ASCII. Hosted one-click unsubscribe. Postal address in the footer (740 N Rampart St, New Orleans, LA 70116; David OK'd 2026-10-16).

## The eight emails

Pace comes from the quiz "when" answer, same as the engine already does: this weekend or this month = fast (days 0, 1, 2, 3, 5, 7, 9, 12); later or just looking = slow (days 0, 3, 7, 12, 18, 25, 32, 40). Local and visitor lanes swap the city email content, not the skeleton.

| # | Subject (working) | What it is | The one link | Photo / video |
|:-|:-|:-|:-|:-|
| 1 | Your result, and the one thing people ask first | Their quiz result, the tour that fits, and the answer to "where do we meet" in three plain lines (shuttle from 740 N Rampart, or drive 30 to 40 minutes). No price. | See the tour | Result photo (cypress channel) |
| 2 | Meet Nick | Nick, the guide named in more reviews than anyone. Two review lines, what he looks for on the water, the owls. | Watch 60 seconds with Nick [VERIFY a clip exists on the channel] | Nick in his kayak |
| 3 | Visitors: Three places we send our own families. Locals: The bayou you can paddle without leaving the city | Visitors: three restaurants, one line each, none of them on Bourbon (Parkway, Dong Phuong, Liuzza's by the Track [VERIFY hours]). Locals: Bayou St. John, the Magnolia Bridge, the rental 15 minutes from the Quarter. | The To-Go Cup, one line: "we write about the city every other week, here's the last one" | Bayou St. John at golden hour |
| 4 | Why the swamp is quiet | The two-minute version of the Manchac story: clear-cut in the 1900s, regrown, the second largest bald cypress swamp in the country, why a kayak is the only way to hear it. | Watch the Manchac film | Aerial of kayaks in the canopy |
| 5 | Never kayaked? Read this one | Their fear answered (the engine already branches on exp-never): stable sit-on-tops, life jacket on the whole time, guide in front, "Was definitely apprehensive... but PLEASE don't be!" | See first-timer photos | A first-timer group, smiling, dry |
| 6 | Meet Alex, then Stephanie | Two shorter guide intros: Alex (funny, the storyteller), Stephanie (patient, the one for the nervous friend). | Watch the guides answer four questions [VERIFY: Guide Video Clips Aug 2026 exist in vault Marketing] | Two portraits |
| 7 | Visitors: The two weeks you're here, sorted. Locals: What's on this month | A mini To-Go Cup: five dated events in their travel window (pulled from the current issue), one eat/drink, one locals' thing. This is the handoff to the newsletter. | Read the full To-Go Cup | Event photo |
| 8 | Open dates for your swamp day | The only ask. Real availability for their window from `/avail`, the price once, the shuttle once, one Book button with `ref=q-<id>`. | Book | Golden hour on the water |

Then: 24 hours after a Book tap with no booking, the existing "Still deciding?" email (signed by the crew, reply goes to info@). After email 8, the lead joins the To-Go Cup list.

## What changes in the quiz build

The quiz engine (`~/Projects/fh-lead-engine-quiz`, NKST files on branch `quiz-nkst`) already runs a 7-step drip with a fear branch, a guide email and a practical email. This plan keeps that machinery and changes the content and order:

| Engine step today | Becomes |
|:-|:-|
| q1 result + price + Book button | Email 1: result, where we meet, no price, no Book button |
| q2 fear answered | Email 5 (moves later, after the city and the guides) |
| q3 proof | Folded into emails 2 and 5 |
| q4 meet your guide | Emails 2 and 6 (three guides, with photos and video) |
| q5 where we meet, what to bring | "Where we meet" moves up to email 1; "what to bring" into email 8 |
| q6 open dates | Email 8, the one ask |
| q7 last note | Dropped; the To-Go Cup takes over |
| (none) | Emails 3, 4, 7: the city, the swamp story, the mini To-Go Cup |

Needs in code: an 8-step sequence (today max 7), a local/visitor lane on steps 3 and 7 (the engine already has `loc-local` / `loc-visitor` tags), image and video fields per step, and the To-Go Cup handoff (add the lead to the newsletter recipients after step 8). Copy lives in `engine/copy/nkst_quiz.json`; the lane logic is an engine change the hub session owns.

## Watching how the good ones do it

David's ask: subscribe to great newsletters and drips and watch them. Running now from info@neworleanskayakswamptours.com: Gambit, Eater New Orleans, Very Local, New Orleans & Co, Axios New Orleans, WWOZ, nola.com, The Infatuation, Atlas Obscura, Intrepid, Walks, Devour, Rick Steves, plus one OTA. Swipe-file rules: one folder label in Gmail (`swipe/newsletters`), Claude reads them weekly and keeps `Marketing/Newsletter Series 2026/90 — Swipe File.md` with what each does in the first 100 words, how often they ask, and one thing to steal.

[VERIFY with David: "Sign up for the batch" - which "Batch" did you mean? If it is a specific newsletter, name it and it goes on the list.]

## Measuring it (FareHarbor and the engine, not GA4)

| Stage | Number | Where |
|:-|:-|:-|
| Quiz starts, completions, emails | engine leads table (`source: quiz`) | DynamoDB `fh-leads` |
| Email taps per step | `book_taps` and `/t` go-link logs | engine |
| Bookings | Online Booking Reference contains `q-` | FareHarbor Advanced Bookings report |
| Unsubscribes per step | SES suppression list | SES us-west-2 |
| Newsletter handoff | leads added to To-Go Cup list after step 8 | recipients.json |

Read it monthly: bookings per 100 quiz starts, by lane (local vs visitor) and by quiz style (A vs B).

## What I need from David

1. Guide video: is there usable footage of Nick, Alex and Stephanie (the Aug 2026 "4 questions" clips, the YouTube channel), and are the three OK being featured?
2. Restaurants for the visitor lane: my three are Parkway, Dong Phuong, Liuzza's by the Track. Swap any?
3. Which "Batch" newsletter you meant.
4. OK for the hub session to change the engine (8 steps, lanes, image fields), or keep NKST copy-only inside the 7-step engine for now?
