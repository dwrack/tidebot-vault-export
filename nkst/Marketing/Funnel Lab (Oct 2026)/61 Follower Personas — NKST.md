*Drafted 2026-10-20 for the Funnel Lab. Status: PARTIAL. The Instagram follow-graph pull did not run (blocked, see below). Sections 2 to 4 are built from data we already have (168 Messenger lead-form fills, 1,303 reviews with text, 58 organic chats, all from file 01). Anything the IG graph would add is marked [VERIFY after graph]. Nothing posted, sent, or changed on Instagram.*

# Follower Personas: NKST

## Bottom line

- The IG graph is blocked twice over: the NKST Apify account (swirled_inscription, FREE) has **$1.29 of $5 left** until Nov 13 (checked 2026-10-20), and the default run costs **~$7.80**. On top of that, the actor's free-plan gate caps us at 5 runs and 1,000 rows a day. Spent this session: **$0.00**.
- The free seed source is down as well. The IG Graph API returned 400 for @kayaknola media/tags and "no permission" (code 10/100) for both accounts through meta-organic, so we have no commenter or tagger list to seed from. (Checked 2026-10-20.)
- What we already know is enough to fix the quiz now: it asks local vs visiting, skill, and party size, but never **where they're staying or living, how they get to the swamp, or what else they do in the city**. Those three are exactly what the To-Go Cup and the drip need.

## To unblock the graph (David's call)

| Step | Cost | What it gets |
|:-|:-|:-|
| Apify Starter on the NKST account for one month | $29/mo, cancel after | Removes the free gate; default 60 seeds x 150 = ~$6.43 at Starter pricing |
| Re-auth the IG token for @kayaknola (`IG_TOKEN_KAYAKNOLA`) and give the meta-organic app `instagram_manage_comments` on both accounts | free | Commenters and taggers as seeds, which are closer to real customers than random followers |
| `brands.json` only lists @kayaknola | free | Add @neworleanskayakswamptours as a second seed source once the token works |

Waiting for the Nov 13 reset doesn't fix it: $5 still won't cover $7.80, and the 5-runs-a-day gate stays. With $1.29 we could pull about 4 seeds, and 4 people tell you nothing. I didn't spend it.

## 1. Accounts NKST followers also follow

**Not run.** The table below is the structure the graph fills in. These are hypotheses for what to check, not findings.

| Group | What we'd look for | Status |
|:-|:-|:-|
| NOLA food | city food pages, neighborhood restaurants | [VERIFY after graph] |
| Music and festivals | Jazz Fest, Frenchmen St venues, WWOZ, Voodoo, French Quarter Fest | [VERIFY after graph] |
| Travel | travel inspo, "things to do in NOLA" creators | [VERIFY after graph] |
| Outdoors | paddling, Louisiana wildlife, birding, Jean Lafitte NHP | [VERIFY after graph] |
| Local news | WWL, Fox 8, NOLA.com, The Gambit | [VERIFY after graph] |
| Hometown (feeder) | sports teams and city pages outside NOLA (feeds ad geo) | [VERIFY after graph] |

## 2. Personas (real counts, from the lead form and reviews)

Base: 168 Messenger lead-form fills (Apr 20 to Oct 6, 2026). Every fill answered two questions: do you live in New Orleans, have you kayaked.

| Persona | Count | Share | Supporting evidence |
|:-|:-|:-|:-|
| **Local, has kayaked** (wants a new spot close to home) | 68 | 40% | Locals 110 of 168 (65%). Reviews barely show them: local language in 2.2% (29) of reviews |
| **Local first-timer** (wants to try it, needs it easy) | 42 | 25% | First-timers 56 of 168 (33%). "Easy or stable" in 10% of reviews, "nervous or scared" in only 3.1% |
| **Visitor, has kayaked** (wants the not-Bourbon day) | 44 | 26% | Visitor language in 13.7% (179) of reviews. "Highlight of our weekend" and "best experience in New Orleans" phrasing |
| **Visitor first-timer** (group or couple on a trip) | 14 | 8% | Friends 6.6% (86), couples 5.6% (73), family 4.7% (61) of reviews |

What cuts across all four:
- Getting there is the #1 worry: meet spot, pickup, or parking comes up in 43% (25 of 58) of organic chats and is the first question in 29%.
- Price shows up in 28% of chats (16). Military and veteran discounts get asked about by name.
- The guide is the product. 55% of reviews name one.
- 72% of lead-form chats (121 of 168) ended after the AI's single reply. The quiz has to do the follow-up the form never did.

Note: the lead form skews local because the Meta lead campaign targeted the metro (paused since Jul 15). Past-guest email is 95% visitors. So these are two different audiences, and the quiz should sort them on the first screen.

## 3. What the quiz doesn't ask that these personas would answer

Current quiz (`engine/quiz/nkst.json`, branch quiz-nkst) asks: ever kayaked, who's coming, live here or visiting, what you want (gators, birds, quiet, history), when, how'd you find us. The personality quiz adds Saturday morning, photo style, and paddle length.

| New question | Answer options | Who it's for | Why (evidence) |
|:-|:-|:-|:-|
| How are you getting to the swamp? | I'll drive / Need a ride from the Quarter / Rideshare / Not sure yet | All | Getting there is 43% of chats and #1 first question. It routes to the pickup upsell or a "where to park" email |
| Where are you staying? (visitors) | French Quarter / Marigny-Bywater / CBD-Warehouse / Garden District-Uptown / Mid-City / Outside the city | Visitors (34%) | Drives which restaurants and bars go in drip email 3. [VERIFY after graph: add neighborhoods the graph shows] |
| What part of town are you in? (locals) | Uptown / Mid-City / Bywater-Marigny / Gentilly / Metairie-Kenner / Northshore / Westbank | Locals (65%) | Sets To-Go Cup content and the Bayou St. John rental pitch. Northshore is close to Honey Island |
| How many nights are you in town? (visitors) | 1-2 / 3-4 / 5+ | Visitors | Sets drip timing. A 2-night trip needs every email before arrival |
| What else is on the list? (multi-select) | Food / Live music / Festivals / History and cemeteries / Bars / Plantations / Just the swamp | All | Picks the newsletter lane. [VERIFY after graph: the options should mirror the top also-follow groups] |
| What's the occasion? | Just because / Birthday / Date / Showing visitors around / Bachelorette / Work group | Locals mostly | "Showing visitors around" is the repeat-local job nobody tracks. Birthday and bachelorette show up in reviews (0.4%, 0.5%) |
| Anything you're nervous about? | Tipping over / Gators or snakes / Bugs and heat / Bathrooms / Nothing | First-timers (33%) | Gets the fear out in the open and routes to the right reassurance email. Low in reviews (3.1%), unknown in leads |
| Kids' ages? (only if "Family with kids") | Under 6 / 6-11 / 12+ | Families | Kids came up in 7% of chats. Age decides tandem vs solo |
| Any discount we should know? | Military or veteran / Local resident / Student / None | All | Military and veteran discounts are named in the price chats (28% mention price) |

Skip: income, age, gender. Nobody will answer them truthfully, and they don't change what we send.

Keep the quiz around 30 seconds: add at most 3 to the main path (getting there, where staying or living, what else is on the list). The rest go as branches or as a one-tap question in drip email 2.

## 4. Names for the To-Go Cup and the drip

**Not from the graph.** The ones below are already in the drip draft (file 60) and the Customer Truth data. The graph would replace or confirm them with what our followers actually follow.

| Type | Names | Source |
|:-|:-|:-|
| Restaurants | Parkway Bakery, Dong Phuong, Liuzza's by the Track | File 60, email 3 [VERIFY hours] |
| Neighborhood and outdoor spots | Bayou St. John, Magnolia Bridge | File 60, email 3 (locals) |
| Swamp locations | Honey Island Swamp, Manchac | NKST tour pages |
| Events | none confirmed | [VERIFY after graph: Jazz Fest, French Quarter Fest, Voodoo, Bayou Boogaloo, and second lines are the obvious checks] |

## Next run

When the Apify plan and the IG token are fixed: `seeds nkst --seeds 60` then `following nkst --per 150 --max-usd 8`, then `analyze` and `segment`. After that, refill sections 1 and 4 and swap the [VERIFY after graph] answer options for real ones. Cache stays in `~/Projects/follower-personas/cache/nkst/` (local, not iCloud).
