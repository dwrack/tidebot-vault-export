# Homepage FAQ + AI Visibility Plan (Nov 2026)

**CURRENT STATUS (2026-11-02, late):** Built in the local site copy (`~/dev/ee-site-preview`, not deployed). The homepage FAQ now uses 8 questions picked by search volume: floating sauna (1,600/mo US), where in Portland, how cold is the Columbia (390/mo US) with a link to the new /columbia-river page, how long to stay in a sauna (5,400/mo US, written as listen-to-your-body), what to wear (3,600/mo US), sauna or plunge first (390 + 880), private sauna, rain/winter. FAQPage schema is on the homepage for those 8; /faq marks up only its 14 extra questions, so no question is marked up twice. Open blanks: parking line, social capacity [8], sauna temp range, cancellation policy. The draft below is history.

Built 2026-11-02 from Search Console (90 days, 724 queries), the Oct 2026 People Also Ask pull, ads search terms and the live /faq. Draft copy: verify the bracketed facts before it ships. No prices until new pricing goes live 11/23.

## What people search (non-brand, 90 days)

| Search | Impressions | Our position |
|---|---|---|
| sauna portland | 1,180 | 7.3 |
| portland sauna | 504 | 7.9 |
| floating sauna portland | 384 | 2.6 |
| sauna portland oregon | 304 | 7.1 |
| cold plunge portland | 245 | 9.6 |
| floating sauna | 193 | 5.0 |
| sauna near me (+ cold plunge near me variants) | ~420 combined | 6 to 8 |
| sauna cold plunge portland (+ variants) | ~410 combined | ~3 |
| private sauna portland | 95 | 8.7 |
| portland cold plunges / cold plunges portland | 172 | 13 to 14 |

Takeaway: we win "floating sauna" (2 to 5) and "sauna + cold plunge" (~3). We're page 1 bottom for plain "sauna portland" (the biggest term) and weak on "cold plunge portland" and "private sauna portland".

## Confirmed facts (Davey, 2026-11-02)
- Hours: daily 6am to 10pm.
- Sessions: 1 hr booking = 45 min in use + 15 min changeover; 2 hr booking = 1 hr 45 min in use + 15 min changeover.
- Swimsuits: required in the social sauna and for private parties on the sauna boat; optional in Private Saunas 1 and 2.
- Stoves: natural gas fired.
- Sauna boat private parties: up to 12 (Davey 11/2, 'I believe', confirm).
- Drive: ~16 min / 8.8 mi from downtown (OSRM, no traffic).
- Live strip on the dev homepage (11/2): river now (USGS Dodson), air now (NWS KPDX), and the 41°F winter to 72°F August range.
- Inside-sauna temp: Inkbird ITC-308-WIFI is a Tuya device. Watchdog code on mbp-2 is ready but tuya.env was never created, so it has never read the temp.
- Private Saunas 1 and 2: slated to open by Thanksgiving.
- Live temps: river = USGS 453630122021400, Columbia River near Dodson OR (below Bonneville, closest Columbia gauge with temperature; 14.0°C / 57°F on 11/2). Air = NWS KPDX (Portland airport, a few miles from the dock). Swap in the dock's own Ecowitt thermometer once it's installed.
- River range, last 12 months (daily means): 41°F Jan to Feb, 47 to 54°F Apr, 65 to 72°F Jul to Sep, 58 to 66°F Oct.

## Homepage FAQ (8 questions, short answers, same text in FAQPage schema)

Rule for every answer: first sentence answers the question and names Ebb & Ember, Portland and the Columbia River where it fits. 40 to 60 words. One hard fact (a number, an address, a time). AI engines lift that first sentence.

1. **What is a floating sauna?**
   A floating sauna is a sauna built on a float and docked on the water. Ebb & Ember is Portland's floating sauna, a cedar sauna docked on the Columbia River in North Portland. You heat up inside, take the ladder straight into the river for your cold plunge, and repeat.

2. **Where is the floating sauna in Portland?**
   Ebb & Ember is docked at Elevated Tides Marina, 173 NE Bridgeton Rd, Portland, OR 97211, on the Columbia River in North Portland, about 15 minutes north of downtown by car (8.8 miles via I-5, longer at rush hour). [Parking: one line.]

3. **Can you cold plunge in the Columbia River?**
   Yes. At Ebb & Ember your cold plunge is the Columbia River itself: climb down the ladder from the sauna deck into the river. The river runs about 41°F in January and February, mid 50s in spring and fall, and up to about 72°F in August. We show today's river and air temperature live on the site. No lifeguard on duty, plunge at your own risk.

4. **How hot is the sauna?**
   The Ebb & Ember sauna is natural gas fired and runs about 170 to 190°F, with cedar benches and room for [8] in a social session. Add water to the rocks for steam.

5. **How does a sauna and cold plunge session work?**
   A 1 hour booking gives you 45 minutes on the sauna, 2 hours gives you 1 hour 45 minutes. Heat up in the cedar sauna for 10 to 15 minutes, take the ladder into the Columbia for a short cold plunge, then rest on the deck. Most guests do 3 to 4 rounds. Go at your own pace, there's no right number. (No health claims.)

6. **Do I need a swimsuit? What should I bring?**
   A swimsuit, two towels (one to sit on, one to dry off), a non-metal water bottle and sandals or bare feet. Swimsuits are required in the social sauna and for private parties on the sauna boat. In Private Saunas 1 and 2, swimsuits are optional. Towels and robes aren't provided.

7. **Can I book a private sauna in Portland?**
   Yes. Book the whole Ebb & Ember sauna boat for a private party of up to 12, or book Private Saunas 1 and 2 for smaller groups, opening by Thanksgiving. [Price line after 11/23.]

8. **Is the sauna open in the rain and in winter?**
   Yes, year-round, rain or shine. Ebb & Ember is open daily 6am to 10pm, and sessions aren't cancelled for weather. Rain on the roof is half the point.

Keep the full FAQ (pricing detail, kids, pets, refunds, booking changes) on /faq. Fix on the live /faq while there: change "propane fired" to natural gas fired; hours to 6am to 10pm; session length to two options: 1 hour (45 minutes of use + 15 to change over) or 2 hours (1 hr 45 min of use + 15 to change over).

## How we show up in AI answers (ChatGPT, Gemini, Google AI Overviews, Perplexity)

1. **Same facts everywhere.** Address, hours, sauna temp, river plunge, "Portland's floating sauna" worded the same on the homepage, /faq, GBP description + Q&A, Yelp, TripAdvisor. AI trusts facts that agree across sources.
2. **Schema.** FAQPage for these 8, plus LocalBusiness (type HealthAndBeautyBusiness / DaySpa) with "floating sauna" in the description, geo, hours, priceRange, and sameAs links to IG, GBP, press. The dev site has none yet.
3. **Answer-first copy.** Every section's first line should be quotable on its own.
4. **Build /cold-plunge-portland.** The homepage alone won't beat Knot Springs and Koti for "cold plunge portland". Draft exists: `Marketing/Blog — Cold Plunge Portland FAQ.md`.
5. **Get on the lists AI reads.** AI answers to "best sauna Portland" pull from Portland Monthly, Time Out, Reddit, Yelp and roundup posts. Keep /best-saunas-portland, push for inclusion in roundups, answer Reddit threads honestly as the business.
6. **Track it.** Add E&E's keywords to the daily ai-citation loop (sauna portland, cold plunge portland, floating sauna portland, private sauna portland) to see who gets cited each day.
