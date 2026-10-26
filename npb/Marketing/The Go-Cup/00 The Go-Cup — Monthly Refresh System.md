# The Go-Cup: Monthly Refresh System

**UPDATE 2026-10-16:** the newsletter is now quiz-first, and every tap saves to the reader's profile inside the email (AMP for Gmail/Yahoo, 85% of the list by provider). There are four editions: Just Visiting / In Town / Another Round / Yeah You Right. Spec: [[01 In-Email Answers — Spec]]. Click-through preview: `preview-quiz.html`. Where sections 3-5 below disagree, the spec wins.

*Drafted 2026-10-15 by David's Claude. Plan only. Nothing is built, scheduled or sent. Builds on [[NOLA Instagram Pulse — Oct 2026]] and the survey contest funnel (Lead Funnels Oct 2026, doc 02).*

**The idea in one line:** a City Cast-style city newsletter for New Orleans, written by the NOLA Party Barge crew. There are two editions, one for people visiting and one for people who live here. It gets refreshed once a month for the season. Every issue ends with a boat as the easy next plan.

## 1. The name

"The Bayou Report" was too small. The newsletter covers the whole city, and the bayou is only where *we* happen to be. The name should feel like New Orleans, work for visitors and locals, sound good read aloud (for audio later), and fit a party brand.

| Name | Why it works | Why it might not | Verdict |
|:-|:-|:-|:-|
| **The Go-Cup** | Only-in-NOLA (you walk out of the bar with your drink). It means "take it with you", which is exactly what a weekly cheat sheet is. Short, fun, sounds like us. "This is the Go-Cup" works as an audio open | A little drink-forward for the family crowd. The family edition can still use it, since it's culture, not a bar crawl | **Pick this** |
| Lagniappe | Means "a little something extra". Locals love it | Used by a hundred businesses, and visitors can't spell it or search for it | Use as a **block name** inside the email |
| Yeah You Right | Pure local slang, instant insider feel | Visitors won't get it | Good **name for the locals edition**, maybe |
| Throw Me Something | The Mardi Gras ask, full of energy | Feels seasonal (February only) | Use as a **subject line** in Carnival season |
| Pass a Good Time | Warm, Cajun, an invitation | Long, and soft on a phone | Tagline material |
| Neutral Ground | Clever local word | A coffee house and plenty of others already use it | Skip |
| Where Y'at | Perfect, but... | Where Y'at Magazine owns it (it showed up in the Instagram scrape) | Skip |

**Recommendation:** **The Go-Cup**, with the tagline "What's worth doing in New Orleans this week. Poured by the crew at NOLA Party Barge."

- Visitor edition: **The Go-Cup: Just Visiting**
- Locals edition: **The Go-Cup: Yeah You Right** (or simply "Locals")

Checked 2026-10-15: a quick web search found no newsletter called The Go-Cup in New Orleans, only Instagram posts using the word. That was not a trademark search. Do one before printing anything.

## 2. How it feels like City Cast (without a podcast studio)

City Cast is a daily local podcast plus newsletter in 13 cities (there's no New Orleans one, checked 2026-10-15). What makes it work, and our version of each:

| City Cast does | We do |
|:-|:-|
| A named host with a face and a voice | One crew host signs every issue, with a photo up top. A real crew member who says yes, never David. Nolan (the chat agent) could be the "voice" if we want one character across chat and email. David's call |
| A short, chatty opener about the city today | 2-3 lines from the host about what the city feels like this week ("It finally dropped below 80. Everyone's on a porch.") |
| The same sections in the same order | Fixed blocks (below), so readers learn where to look |
| Asks readers things | Every issue has a 1-tap poll. The answers feed the quiz tags |
| Daily | **Weekly, Thursday morning** (weekend planning). Daily isn't realistic with our staffing |
| The podcast | Phase 2: a 2-minute "voice memo" from the host recorded on a phone, linked at the top. Optional |
| A web archive | Each issue gets posted on the new site (`/go-cup/2026-10-22`). Free SEO for "things to do in New Orleans this weekend" |

## 3. Two editions, one engine

**How we know who's who:**
1. The first question of any quiz or signup: **"Live here or visiting?"**
2. The FareHarbor booking zip code (anything outside the metro counts as a visitor)
3. Visitors with a trip date switch to the locals rules for 30 days after the trip. They become past guests, and that's the "come back / send your friends" lane.

| | Just Visiting | Yeah You Right (locals) |
|:-|:-|:-|
| Time frame | **Their trip dates.** "The week you're here", keyed to `trip_month`, with a countdown when we know the date | **This weekend** |
| The 3 Things | Big, iconic and seasonal, plus one off-the-map pick to feel like an insider | New openings, neighborhood stuff, free and cheap stuff |
| Food | The po'boy argument, where to go after the parade | What's new, what's coming soon, who's doing a pop-up |
| Boat slot | "The one thing to book before you land" | Weeknight openings, first dibs on open boats, "bring the out-of-town friends" |
| Tone | Your friend who lives here | Your neighbor who knows everybody |
| Poll example | "Parade or bayou first?" | "Casamento's or Acme? Settle it." |

## 4. The blocks (same order every week, all in bar-talk)

*Locked 2026-10-15: David approved the name, the logo and the copy voice.*

| Block | Subhead under it | What's in it |
|:-|:-|:-|
| **The Toast** | (host name), pouring this week | 2-3 line host opener about the city right now |
| **First Round** | Three things worth leaving the house for. | Date, time, place, one line of opinion each |
| **Fresh Pour** | Just opened, or about to. | One spot, what to order |
| **Pour Decisions** | This week's bar argument. Tap your side. | Hot take + 1-tap poll (feeds the quiz tags) |
| **Lagniappe** | A little something extra. | One weird history fact or local word |
| **This Round's On...** | A local spot we'd send you to anyway. | Sponsor slot, one per issue, clearly labeled (section 10) |
| **Last Call** | Visitors: The one thing to book before you land. Locals: Locals' pour, first dibs on open boats. | The only boat block. Real photo from that week + the link |
| **Next Round** | (none) | One-line teaser for next Thursday, the open loop |

**Footer, in voice:** "Change my order" (switch edition) · "What're you drinking?" (pick topics) · "Cut me off" (one-click hosted unsubscribe, never by email).

**More names in the same vein (for later blocks, quizzes and subject lines):**
- Monthly quiz: **Bartender's Choice** ("Which Krewe are you?")
- Issue number: **Round 01, Round 02...**
- Reader replies or mailbag: **Tab's Open**
- Best-of or year-end issue: **Top Shelf**
- Rainy-day picks: **Under the Awning**
- Late-night picks: **One More**
- Locals' deals and first dibs: **Locals' Pour**
- Referral ask: **Buy Your Friend a Round** (forward to a friend)
- Welcome email: **Your First Pour**
- Subject line format: `Go-Cup: Skeletons on Magazine St`

## 4b. The signup: "Get the Go-Cup."

One name everywhere: site footers, the popup, quiz result pages, Nolan in chat, QR on the boat.

- **Headline:** Get the Go-Cup.
- **Body:** New Orleans, poured weekly. The 3 things worth doing, what just opened, and whatever locals are arguing about. Free, every Thursday.
- **Fork:** I'm visiting / I live here (visitors also get "When's the trip?")
- **Button:** Pour me one
- **Fine print:** One email a week. Cut me off anytime, one click.
- On the boat: a QR card that says "Get the Go-Cup. Your crew's cheat sheet for the rest of the trip."

It's a lead magnet that doesn't feel like one: no PDF, no "free guide", just the thing itself.

## 5. Quizzes and polls that sharpen it

Every tap writes a tag. Interest tags: `food`, `music`, `outdoors` (gators/bayou), `nightlife`, `parades_fests`, `family`, `weird_history`. The engine fills The 3 Things, weighted to the reader's top two tags, and keeps one wildcard so it never gets stale.

- **Weekly:** the Hot Take poll (no entry, pure fun, one tag per tap)
- **Monthly:** one seasonal quiz, 4-5 taps, with a shareable result. "Which Krewe are you?" (Feb), "What's your Jazz Fest personality?" (Apr), "What kind of Halloween New Orleanian are you?" (Oct). The result page tags them and offers the matching boat. The quiz branch already exists (`quiz-npb`, not deployed)
- **Signup:** live here or visiting, plus "What do you want more of?" (pick 2)
- **Decay:** a tag nobody has clicked in 8 weeks loses weight, so the mix follows what they actually open now

## 6. The monthly refresh (the part that keeps it timely)

Runs around the **20th of each month** for the next month. It's one review file for David or Michael, one approval, then it loads.

| Step | Who / what | Output |
|:-|:-|:-|
| 1. Season spine | The 12-month calendar below plus that year's real dates | What the month is "about" |
| 2. Instagram pulse | Apify scrape of 12+ hashtags plus a list of local curator accounts (weekly, about $0.65 each, NPB account) | What's new, hot, coming soon |
| 3. Draft the Month Pack | Claude | 4 weekly issues x 2 editions; refreshed funnel blocks (LIKE-PICKS, `trip_month` answer pages, SC-03, SC-18); the month's quiz; 12 subject lines; 1 boat angle for the month |
| 4. Fact check | Claude | Every date and venue re-checked against its source the week of each send (V17 in the funnel doc) |
| 5. Approve | David or Michael, one file | Edits inline, then "ship it" |
| 6. Load | SES runner on mbp-2 (already schedule-file driven) | Sends on schedule. Weekly pulse swaps in fresh items Thursday morning |

Where it would run: a launchd job on mbp-2, writing to `Marketing/The Go-Cup/Month Packs/YYYY-MM.md`. A one-line ping when the pack is ready, by email, not Slack (Slack was paused 10/13 for notification fatigue).

## 7. The season spine (verify dates every year)

| Month | What the city is about | Boat angle |
|:-|:-|:-|
| Jan | Carnival season starts Jan 6 (Twelfth Night), king cake everywhere | "Escape the parade crowds" group days |
| Feb | **Mardi Gras** (2027: Tue Feb 9), parades, krewes | Parade-break boat, bachelor/ette peak |
| Mar | St. Joseph's altars, Super Sunday (Mardi Gras Indians), St. Patrick's | Crawfish season starts, spring break groups |
| Apr | French Quarter Fest, Jazz Fest starts | Day-off-from-the-fest boat |
| May | Jazz Fest, crawfish peak, Mother's Day | Mother's Day, graduations |
| Jun | Pride, Juneteenth, the heat starts | Sunset slots, beat-the-heat timing |
| Jul | Essence Fest, July 4, Tales of the Cocktail | Big-group weekends |
| Aug | Satchmo SummerFest, Red Dress Run, White Linen Night | Weeknight locals push (the slow month) |
| Sep | Southern Decadence, Saints season starts | Game-day tailgate boats |
| Oct | Halloween season, Krewe of Boo, fall fests | Costume-friendly sailings (Creole Queen owns the river, the bayou is open) |
| Nov | Fair Grounds opening day, Po-Boy Fest, Bayou Classic, Thanksgiving | Holiday parties start |
| Dec | Celebration in the Oaks, Réveillon dinners, bonfires on the levee, NYE | Office parties, family in town |

## 8. Keeping the name in their heads (without being an ad)

- Our name is in the masthead, the tagline and the host's sign-off, and that's it. The value is the city, the boat is the punchline.
- **From the Boat** uses a real photo from that week, never stock, so it feels live.
- **Locals perk:** first dibs on open boats, posted only in the locals edition. That's a reason to stay subscribed. No new discount needed (matches V12).
- **Forward-to-a-friend line** in the visitor edition: "Coming with a crew? Send them this so they stop asking you what to do."
- **Same voice everywhere:** chat (Nolan), funnel emails and The Go-Cup all sound like one crew.

## 9. What to measure

Open rate by edition, taps per issue (the tag engine's fuel), the click rate on From the Boat, bookings within 14 days of an issue, unsubscribes by edition, and forwards. Read it monthly in the same review file.

## 10. The Go-Cup as a media property (David, 2026-10-15)

David: "each of our websites can push emails into it" and "we can probably sell advertising on it with our web studio company." That makes The Go-Cup bigger than a NOLA Party Barge newsletter. It becomes the portfolio's New Orleans audience.

**Every New Orleans site feeds one list.** NOLA Party Barge, New Orleans Kayak Swamp Tours, Crescent City Kayak, Honey Island Swamp Kayak Tour, NOLA Bike Bar, NOLA Booze Cruise, New Orleans Tiki Boats and Admire NOLA each carry the same "Get the Go-Cup" block. Each signup is tagged with `source_site`, so we know who brought whom in and the Last Call slot can rotate brands to match interests (gators and outdoors go to the kayak tour, nightlife goes to the booze cruise).

**Selling ads.** City Cast pays for itself with local sponsors read in the host's voice. Ours is the "This Round's On..." slot:
- 1 sponsor per issue, written in our voice, labeled as sponsored
- Sold by the web studio as an add-on for its New Orleans clients ("website + a Go-Cup feature")
- Price it once the list is real. A rough benchmark is $25 to $50 per 1,000 subscribers per send for local newsletters (my estimate, not verified). Sell nothing until the list passes about 2,000 and opens are known
- Never sell Last Call. Never take a competitor (other boats, swamp tours, cruises)

**Decision this creates:** the masthead says "by NOLA Party Barge" right now. If five brands feed it and outside sponsors buy in, a neutral "by the crew" byline may read better, with the brands showing up in Last Call. The logo works either way; only the tagline line changes.

**Web studio notes found 2026-10-15:** TheBrain vault, `03 Projects/NOLA Web Studio/Automation Spec (Oct 12 2026).md` and `03 Projects/Active/NOLA Website Outreach/Round 2 Prospects.md`. Those prospects are the first list of people to pitch the sponsor slot to.

## Open calls for David

1. ~~Name~~ LOCKED 2026-10-15: The Go-Cup, locals edition "Yeah You Right". Logo files in `Logo/` (SVG + PNG, sheet at `Logo/logo-sheet.html`)
1b. Masthead: keep "by NOLA Party Barge" or go neutral "by the crew" now that every NOLA site feeds it?
2. Host: which crew member is the face? Or Nolan as the voice?
3. Weekly Thursday send + monthly pack on the 20th, running on mbp-2: go?
4. Phase 2 audio voice memo: yes later, or skip?

## 11. Standing rules for every issue (David, 2026-10-16)

"I want people to talk about this." Every Round must have:
- **Creatives spotlight (The Dress Code, or a seasonal swap):** 2-4 local artists, makeup/SFX, designers, makers, with their IG handle. Use their photo only with their OK (DM them first). Feature people, not chains.
- **After Dark:** at least one underground or creative party (St. Claude, warehouse, drag, burlesque, secret-location raves), tagged 18+/21+ and marked CONFIRM if single-source.
- **Photos:** real boat photos plus creator or organizer photos with permission. No stock, ever. Every event card gets an image or an "ask for photo" slot.
- **Add to calendar** (Google + Apple .ics) on every event worth leaving the house for.
- **Pour Decisions has a "Hard disagree" option** that opens "Fair enough. What would you do instead?" A few favorite responses run next week, first names only, with permission.
- **Every tap visibly confirms:** button flips to a check, "Saved to your tab" pops up, and the Your Tab block at the bottom lists everything tapped.
- **Locals only + tourist teaser (David, 2026-10-16):** 1-3 items per issue (small venues, secret parties, Locals' Pour boat perks) show in full only to `audience=local`. Everyone else gets a blurred teaser card with a reason it stays small, plus "Visiting? send me the visitor-friendly version". It makes locals feel let in and gives tourists a reason to open next week.
- **Reader tip box:** "Know someone better?" feeds next week's spotlight.
Preview of the standard: `preview-v3.html`. Research for Round 01: `Research - Creatives + Underground Oct 22-Nov 8 2026.md`.

## 12. Seasonal themes (David, 2026-10-16)

Same layout, fonts and section order every issue. A theme swaps only the palette, the masthead colors and the band title under the logo. Built as CSS variables (`body data-theme=...` in the preview). In the real email they're inlined, and the masthead is a pre-rendered PNG per theme, because Gmail strips SVG.

| Theme | Runs | Masthead / band | Accent (under 10%) | Band title |
|:-|:-|:-|:-|:-|
| Base | Any week with no holiday | Teal #2a7d7b | Gold | (none) |
| Halloween | Oct 1 to Nov 2 | Night #16131a | Pumpkin #e8762b | The Halloween Round |
| Friendsgiving + Bayou Classic | Nov 3 to 30 | Pecan brown #4a2f22 | Cranberry #9c2b3a | The Second Helping |
| Holidays + Reveillon | Dec 1 to 26 | Evergreen #1f3b2e | Candle gold #d4a84b | The Bonfire Round |
| New Year's | Dec 27 to Jan 5 | Midnight #121826 | Champagne #e3c98a | The Last Round of the Year |
| Carnival | Jan 6 (Twelfth Night) to Mardi Gras (Feb 9, 2027) | Deep purple #3b1f5c | Gold #d4a84b, green #2e7d4f only in small rules | The Carnival Round |
| Lent + St. Joseph's + Super Sunday | Mardi Gras to Mar 31 | Indigo #24305e | Sky #8fb8de | (no title) |
| Fest season | Apr to May | Brass #7a5a1d | Coral | The Fest Round |
| Summer | Jun to Aug | Coral #ff4447 | Ink | The Heat Index |
| Saints season | Sep | Black #17171a | Old gold #b8a46a | The Game Day Round |

**Rules:** one theme per issue. No gradients, drop shadows or clip-art. Photos stay real. The theme lives in color and one line of type, nothing more. The Halloween masthead is at `Logo/themes/header-halloween-1200x300.png`. Make each new theme by swapping colors in `gocup-email-header.svg` and rendering with headless Chrome plus the web fonts. The monthly pack (section 6) picks the theme from this table by send date.

## 13. Voice note (David, 2026-10-16)

Keep the bar-talk commentary and the teasing. Just no gendered or odd address at the reader ("smart guy" was too weird). Hard-disagree prompt reads: "Fair enough. What would you do instead?"
