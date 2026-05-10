# Austin Kayak Tours — SEO Action Plan & Blog Pipeline

Built from the 2026-05-09 audit. Anchored to real GSC data from the legacy `lonestarkayaktours.com` property (rebrand → austinkayaktours.com).

---

## Part 1 — 90-Day Action Plan

### Week 1: Foundation (must-do before anything else)

| # | Task | Owner | Effort | Why it matters |
|---|---|---|---|---|
| 1 | Verify austinkayaktours.com in Google Search Console (both URL property and sc-domain). Submit sitemap. | Dev/David | 15 min | Currently flying blind on the new domain |
| 2 | Generate and publish a clean robots.txt referencing the sitemap | Dev | 10 min | Currently empty |
| 3 | Confirm wp-sitemap.xml is generated and pinging | Dev | 15 min | Standard sitemap.xml didn't return content |
| 4 | Build per-page 301 map: lonestarkayaktours.com/X → austinkayaktours.com/X (not just root → root) | Dev | 2 hrs | Preserves equity from the legacy domain page-by-page |
| 5 | Update internal nav templates so links go to canonical URLs (not the nested `/austin-kayak-tours/X/` paths that 301) | Dev | 30 min | Saves a hop, consolidates internal link signal |
| 6 | Fix the `/kayak-paddleboard-rental/` 404 (real page is `/rental/`) — find inbound links and update or 301 | Dev | 30 min | Recovers any external link equity to the dead URL |

### Week 2: On-page CTR fixes (highest ROI of the whole plan)

The site already ranks top 3 for "austin kayak tour" / "kayak tours austin" / "austin kayak tours" but CTR is half of benchmark. These are the lowest-effort, highest-return changes.

| # | Page | Current title | Proposed title | Proposed meta description |
|---|---|---|---|---|
| 7 | / (home) | Austin Kayak Tours \| Kayak Tours & Rentals in Austin, TX | **Best Kayak Tours in Austin, TX — Lady Bird Lake from $50** | Guided kayak tours of Lady Bird Lake from $50. See the Austin skyline, the bat colony at sunset, or rent kayaks and paddle boards from $20. Book online. |
| 8 | /austin-skyline-tour/ | Austin Skyline Tour by Kayak \| Austin Kayak Tours | **Austin Skyline Kayak Tour — Guided Lady Bird Lake Tour** | 2-hour guided kayak tour of Lady Bird Lake with downtown Austin skyline views, history, and architecture. From $50. Daily at 10am, 1pm, 4pm. |
| 9 | /bat-bridge-kayak-tour/ | Sunset Bat Bridge Kayak Tour \| Austin Kayak Tours | **Sunset Bat Bridge Kayak Tour — Watch 1.5M Bats from the Water** | Paddle Lady Bird Lake at sunset and watch 1.5 million bats fly from the Congress Avenue Bridge. 2 hours, $50, daily Mar–Oct. |
| 10 | /rental/ | Kayak & Paddleboard Rental \| Austin Kayak Tours | **Kayak & Paddle Board Rentals on Lady Bird Lake — Austin, TX from $20** | Rent kayaks, paddle boards, and canoes on Lady Bird Lake in downtown Austin. Hourly rentals from $20. Walk-up or reserve online. |
| 11 | /paddleboard-tour/ | (verify current) | **Paddle Board Bat Tour — Sunset SUP on Lady Bird Lake** | Stand-up paddle board tour at sunset under the bat bridge. 2 hours, beginner-friendly, $50. |
| 12 | /corporate-events/ | (verify current) | **Corporate Kayak Events in Austin — Team Building on Lady Bird Lake** | Private corporate kayak tours and team-building events on Lady Bird Lake. Groups up to 60. Book direct. |

### Week 2-3: Schema markup (the FareHarbor/WP-VIP theme has a dedicated field for this — currently empty on every page)

Per the global CLAUDE.md notes: paste raw JSON only (no `<script>` wrapper) and never use escaped inner double quotes. The theme adds the wrapper automatically.

| # | Page | Schema type | Notes |
|---|---|---|---|
| 13 | / (home) | LocalBusiness + Organization | Address: 200 E Riverside Dr, Austin, TX 78704. Phone: 512-766-5640. Hours, geo, sameAs to social profiles |
| 14 | /austin-skyline-tour/ | Product + TouristTrip | Price $50, 2hr duration, aggregateRating from TripAdvisor |
| 15 | /bat-bridge-kayak-tour/ | Product + Event (seasonal) | Same pattern, note seasonal availability |
| 16 | /paddleboard-tour/ | Product | Same pattern |
| 17 | /rental/ | Product (with priceRange) | "$20-$50" style range |
| 18 | /faq/ | FAQPage | Mine top 5-10 Q&As, write as plain JSON-LD with single quotes inside string values |
| 19 | All tour pages | BreadcrumbList | Home > Tours > [Tour name] |

### Weeks 3-4: Two pillar pages (the strategic content investments)

| # | Page | Target keyword | Why |
|---|---|---|---|
| 20 | New: /best-places-to-kayak-in-austin/ | "best place to kayak in austin" | 2,799 imp at pos 13, **zero clicks**. Currently no Austin operator owns this SERP. Listicle format with Lady Bird Lake → recommends own tours; covers Lake Travis, Barton Creek, San Marcos for completeness |
| 21 | New: /kayaking-lady-bird-lake/ | "kayaking lady bird lake" + variants | Pillar hub: where to launch, rules, parking, dogs, best times, tour vs rental. Internal-link from every blog post |

### Month 2: Internal linking sweep + content production starts

| # | Task | Effort |
|---|---|---|
| 22 | Add Skyline tour CTA box mid-post in /blog/skyline/ (8,965 imp leaking) | 30 min |
| 23 | Add Bat tour CTA in /blog/some-reasons-to-check-out-the-south-congress-bat-colony/ | 15 min |
| 24 | Cross-link /blog/why-team-building-is-great-on-kayaks/ → /corporate-events/ | 15 min |
| 25 | Cross-link /blog/dog-friendly-activities-in-austin/ → /rental/ | 15 min |
| 26 | Cross-link /blog/five-great-ideas-for-an-austin-vacation/ → homepage with descriptive anchor | 15 min |
| 27 | Replace "Learn More" CTAs on homepage tour grid with descriptive anchors ("Skyline tour details", "Bat tour details", etc.) | 30 min |
| 28 | Publish first 4 new blog posts from the pipeline below (months 2-3 priority) | 8 hrs |
| 29 | Refresh /blog/skyline/ with 2026 dates and tighter CTA structure | 1 hr |

### Month 3: Sustained content + GBP integration

| # | Task |
|---|---|
| 30 | Publish next 4 blog posts |
| 31 | Add FAQ schema-driven sections to each tour page (mine from the FAQ page) |
| 32 | Cross-post blog content snippets to Google Business Profile (every new post = a GBP post) |
| 33 | Build out /paddle-board-lessons/ with internal links from /rental/ and /paddleboard-tour/ |
| 34 | Decide: build /canoe-rental/ or kill the canoe terms (GSC shows demand at pos 13-15 with low conversion) |

### Months 4-6: Scale + measure

| # | Task |
|---|---|
| 35 | Publish 4 posts/month, prioritizing Tier 1 from the pipeline |
| 36 | After 90 days, re-pull GSC data and identify which striking-distance keywords moved |
| 37 | Refresh top-traffic posts annually (skyline, breakfast, dog-friendly) |
| 38 | Build a link-building campaign targeting Austin tourism sites and "things to do in Austin" round-up posts |

---

## Part 2 — 50 SEO Blog Post Pipeline

Each post includes: target keyword, intent, money page to internal-link, priority tier, format.

**Priority tiers:**
- **Tier 1 (months 2-4)**: directly maps to high-impression GSC opportunity OR fills a critical content cluster gap
- **Tier 2 (months 5-7)**: supports a topic cluster, moderate demand
- **Tier 3 (months 8-12)**: long-tail, brand-building, seasonal

---

### Cluster A: Lady Bird Lake authority (6 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 1 | The Complete Guide to Kayaking on Lady Bird Lake (2026) | kayaking lady bird lake | /rental/ + tour pages | **1** |
| 2 | Where to Launch a Kayak on Lady Bird Lake: Every Public Access Point | kayak launch lady bird lake | /rental/ | **1** |
| 3 | Lady Bird Lake Kayak Rules, Permits & What's Allowed | lady bird lake kayak rules | /rental/ | 2 |
| 4 | What's the Best Time of Day to Kayak Lady Bird Lake? | best time kayak lady bird lake | /austin-skyline-tour/ | 2 |
| 5 | Lady Bird Lake vs. Lake Travis: Which Should You Kayak? | lady bird lake vs lake travis kayaking | / (home) | 2 |
| 6 | Parking Near Lady Bird Lake for Kayakers: A Honest Guide | parking lady bird lake kayak | /rental/ | 3 |

### Cluster B: Bat colony / sunset experience (5 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 7 | When Do the Bats Come Out at Congress Bridge? Monthly Schedule (2026) | when do bats come out congress bridge | /bat-bridge-kayak-tour/ | **1** |
| 8 | The Best Way to See the Austin Bats: From the Bridge vs. From the Water | best way to see austin bats | /bat-bridge-kayak-tour/ | **1** |
| 9 | Bat Bridge Kayak Tour: What to Expect, What to Wear, What to Bring | bat bridge kayak tour | /bat-bridge-kayak-tour/ | **1** |
| 10 | Sunset Kayaking in Austin: Why It's the Best Time to Paddle | sunset kayaking austin | /austin-skyline-tour/ (sunset) | 2 |
| 11 | The Mexican Free-Tailed Bats of Austin: Facts, Myths, and Why They Matter | austin bats facts | /bat-bridge-kayak-tour/ | 3 |

### Cluster C: Austin skyline / architecture (5 posts — they already own this)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 12 | The Austin Skyline From the Water: A Building-by-Building Guide | austin skyline from water | /austin-skyline-tour/ | **1** |
| 13 | The Tallest Buildings in Austin (and How to See Them on a Kayak Tour) | tallest buildings austin | /austin-skyline-tour/ | **1** (refresh of existing post) |
| 14 | Austin's Architectural History From a Kayak: A 2-Hour Tour | austin architecture tour | /austin-skyline-tour/ | 2 |
| 15 | The Story Behind Austin's Most Photographed Buildings | most photographed buildings austin | /austin-skyline-tour/ | 3 |
| 16 | How Austin's Skyline Has Changed in the Last 10 Years | austin skyline changes | /austin-skyline-tour/ | 3 |

### Cluster D: Beginner / first-timer guides (5 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 17 | Never Kayaked Before? An Honest Guide for First-Timers in Austin | beginner kayaking austin | /rental/ + /austin-skyline-tour/ | **1** |
| 18 | What to Wear Kayaking in Austin (Every Season) | what to wear kayaking austin | /rental/ | 2 |
| 19 | What to Bring on a Kayak Tour: The Real Checklist | what to bring kayak tour | /austin-skyline-tour/ | 2 |
| 20 | Are Kayak Tours Worth It? An Honest Take From a Tour Operator | are kayak tours worth it | /austin-skyline-tour/ | 2 |
| 21 | Solo Kayaking in Austin: What You Need to Know | solo kayaking austin | /rental/ | 3 |

### Cluster E: Seasonal / time-based (6 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 22 | Kayaking in Austin in Spring: Best Tours, What to Wear, What to Expect | kayaking austin spring | /rental/ | 2 |
| 23 | Summer Kayaking in Austin: How to Beat the Heat on Lady Bird Lake | summer kayaking austin | /austin-skyline-tour/ | 2 |
| 24 | Fall Kayaking in Austin: The Underrated Best Season | fall kayaking austin | /rental/ | 2 |
| 25 | Winter Kayaking in Austin: Yes, It's a Thing — Here's How | winter kayaking austin | /rental/ | 2 |
| 26 | Kayaking on the 4th of July in Austin: Fireworks From the Water | 4th of july kayak austin | /4th-of-july-fireworks-tour/ | **1** (seasonal) |
| 27 | New Year's Eve Kayak Tour in Austin: A Different Way to Ring In the Year | new years eve kayak austin | /new-years-eve-fireworks-tour/ | **1** (seasonal) |

### Cluster F: Group / event / occasion (6 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 28 | Bachelorette Party on Kayaks in Austin: A Different Take on the Weekend | austin bachelorette kayak | /corporate-events/ | **1** |
| 29 | Corporate Team Building on Lady Bird Lake: Why It Actually Works | austin corporate team building water | /corporate-events/ | **1** |
| 30 | Birthday Party on Kayaks in Austin: How to Plan One | austin birthday kayak | /corporate-events/ | 2 |
| 31 | Date Night Kayaking in Austin: An Honest Review of Every Tour | date night austin kayak | /austin-skyline-tour/ | 2 |
| 32 | Family Kayaking in Austin: Tour vs. Rental With Kids (Ages, Safety, Tips) | family kayaking austin | /rental/ | 2 |
| 33 | Hosting a Group of 20+ on Lady Bird Lake: How We Do It | group kayak austin | /corporate-events/ | 3 |

### Cluster G: Alternate Austin water locations (4 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 34 | Best Places to Kayak Near Austin (Outside of Lady Bird Lake) | best places to kayak near austin | / (home) | **1** |
| 35 | Kayaking on Lake Travis: A Local's Guide | kayaking lake travis | / (home) | 2 |
| 36 | Kayaking on Barton Creek: When and Where It's Possible | kayaking barton creek | / (home) | 2 |
| 37 | Kayaking the San Marcos River: A Day Trip From Austin | kayaking san marcos river | / (home) | 3 |

### Cluster H: Paddle board specific (4 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 38 | Stand-Up Paddle Boarding on Lady Bird Lake: Everything You Need to Know | paddle board lady bird lake | /paddleboard-tour/ + /rental/ | **1** |
| 39 | Kayak vs. Paddle Board: Which is Better for Lady Bird Lake? | kayak vs paddle board lady bird lake | /rental/ | 2 |
| 40 | Paddle Board Lessons in Austin: Where to Start and What to Expect | paddle board lessons austin | /paddle-board-lessons/ | 2 |
| 41 | The Sunset Paddle Board Bat Tour: A Different Way to See the Bats | paddle board bat tour | /paddleboard-tour/ | 2 |

### Cluster I: Comparison / decision content (5 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 42 | Sunrise vs. Sunset Kayak Tour in Austin: Which Should You Pick? | sunrise vs sunset kayak austin | /austin-skyline-tour/ | **1** |
| 43 | Renting vs. Joining a Tour on Lady Bird Lake: An Honest Comparison | kayak rental vs tour austin | /rental/ + /austin-skyline-tour/ | **1** |
| 44 | The Best Austin Kayak Tour for Tourists: A Real Recommendation | best kayak tour austin tourist | /austin-skyline-tour/ | 2 |
| 45 | Skyline Tour vs. Bat Tour: How to Choose | skyline vs bat kayak tour | /austin-skyline-tour/ + /bat-bridge-kayak-tour/ | 2 |
| 46 | The Best Cheap Things to Do in Austin Outdoors (Under $50) | cheap things to do austin outdoors | /rental/ | 3 |

### Cluster J: Austin tourism crossover (4 posts)

| # | Title | Target keyword | Money page | Tier |
|---|---|---|---|---|
| 47 | A Perfect Day in Downtown Austin: Kayak in the Morning, Eat on Rainey Street at Night | downtown austin day | /austin-skyline-tour/ | 2 |
| 48 | Where to Eat Before or After Your Kayak Tour in Austin | restaurants near lady bird lake | /austin-skyline-tour/ | 2 |
| 49 | Things to Do With Your Dog in Austin (Including Kayaking With a Pup) | dog friendly austin kayak | /rental/ | 2 |
| 50 | The Austin Tourist's One-Day Itinerary: Skyline, Bats, BBQ | austin one day itinerary | / (home) | 3 |

---

## Part 3 — Publishing Cadence

**Tier 1 first (16 posts):** posts #1, 2, 7, 8, 9, 12, 13, 17, 26, 27, 28, 29, 34, 38, 42, 43.
At 4 posts/month = months 2-5 covers all Tier 1.

**Tier 2 next (24 posts):** months 6-11 at 4 posts/month.

**Tier 3 (10 posts):** opportunistic, fold in seasonally.

**Internal linking discipline for every post:**
- Each post links to at least 2 money pages (with descriptive anchor text matching a target keyword)
- Each post links to at least 2 other blog posts in the same cluster (build the cluster's internal authority)
- Each post is linked FROM the relevant pillar page (post #1 or #34) within a week of publishing

---

## Part 4 — Tracking

After verifying austinkayaktours.com in GSC (Week 1, task #1), set up these monthly checks:

1. Striking-distance keyword movement (positions 5-20 → top 5)
2. Top-page click growth on the 4 money pages (home, skyline, bat, rental)
3. New keywords appearing in top 100 from new blog posts (lag time: 4-8 weeks per post)
4. Branded vs. non-branded click split

---

*Last updated: 2026-05-09. Source: SEO audit of austinkayaktours.com against GSC data from sister property lonestarkayaktours.com (last 90 days).*
