# Token Burn Sweep, 2026-10-31

13 read-only runs across 7 tour brands before the weekly token reset. Nothing was sent, posted, paused, or edited on any site, listing, or ad account. Ebb and Ember and Elevated Tides excluded. No Apify or Higgsfield.

## Decisions for David (money or human-judgment calls)

| # | Brand | Decision | Number |
|---|---|---|---|
| 1 | BBK | Pause Meta "Bat Bridge Kayak Tour - Traffic" (still active, bat season ended today) | $20/day, $140 last 7d, 0 purchases |
| 2 | AKT/LSKT | Pause Google Bat Search Nov 1; cut PMax $37.50 to $25/day | ~$625/30d saved; Michael touched this 10/29 |
| 3 | NPB | Pause 9 zero-conversion keywords, add PMax negatives, freeze National then tROAS 4.0 to 5.0 | ~$1,270/mo waste total incl. Messenger prospecting ($610/mo, OpenCX ghosts 57% of handoffs) |
| 4 | HPB | Every active Meta ad set targets Dublin, California 50mi, not Houston. Stop Followers Reboost ($296) and Initiate Checkout ($272) | $1,230 Oct spend, 0 tracked purchases |
| 5 | HPB | Dock address has 3 versions (GBP 2511, schema 2515, page 2513 NASA Rd). Which is real? | |
| 6 | BBK | Merge duplicate GBP "Space City Kayak Tours" (1005 Commerce, 1 review, our phone/URL) | |
| 7 | NKST | gravitytrails.com and admirenola.com outrank NKST for "new orleans kayak swamp tour"; NKST not top 20. Which domain owns the term? | |
| 7b | NPB | Decided 10/31: the sibling "New Orleans Party Boats" listing's website moves to neworleanspartyboat.com once that site is live. Not before. | |
| 8 | Fleet | `com.admirenola.medium-importer` runs on both Macs, both exit 1. Drop the laptop copy? | |

Michael hand-edited the Texas Google account (8497383499) on 10/8, 10/15, 10/20, 10/26, 10/29 and NPB National's budget 6 times in 24 days. Clear ads proposals with him before anything applies.

## Things Claude can just do (low risk, no money)

- Fix dead internal links: DCKT ~35 links to 10 dead URLs (worst `/cave-point-half-day-kayak-tour/`, 9 pages).
- Add contextual tour links from blogs: AKT 55/57 posts have none; NPB 72/91 posts have zero inbound; NKST top blogs (400+ clicks) don't link to tours; CPPP June 7 interlinking fixes still unshipped.
- Ship CPPP's staged May 6 title/meta rewrites (never went live).
- Replace placeholder metas: NKST 21 pages say "Have you seen the swamp?"; DCKT 18 utility pages on default; AKT/NPB auto-excerpt metas over 160 chars.
- Schema: add aggregateRating + sameAs to DCKT (1,010 reviews, 4.9), NKST (1,474, 4.9), AKT (143, 4.8, homepage says 4); Product/Offer schema on every tour page, FAQPage on AKT /faq/.
- NKST GBP has a junk "Tires" service type.
- BBK: publish the staged bat guide (21 drafts, nothing since Nov 2023; "houston bat colony" 6,600/mo). Retitle `/other-houston-experiences/` (ranks #1-2 for "kayak houston").
- NPB: build a "boat tours / boat rides" page (7 queries, 10.4k impressions, pos 8, 0.6% CTR). Retitle `/boat-rental/` (8.5k impr, 0.17% CTR) and `/things-to-do-in-new-orleans/` (duplicate title).
- HPB: point GBP and socials at the bare domain (www splits signals); link and retitle the boat-rides post (2,100 impr/qtr).
- Re-export Facebook cookies for `com.npb.fb-group-scan` (session expired 10/31). Fix hardcoded `/Users/wavey/` path in `com.admirenola.analytics` on mbp-2.
- Add buffalobayoukayak.com as a Search Console property (not on any connected account).
- Maps-rank `run.py` creds bug fixed this session (accepts username/password keys).

## Shared FareHarbor theme (fix once, all sites)

Measured on DCKT, CPPP, NPB, HPB, NKST, AKT, BBK. Mobile Lighthouse 27-46 everywhere, lab LCP 7-20s, pages 4.7-10 MB, 1.2-2.8 MB unused JS. Real-user CrUX passes where it exists, so this is P2 not P0. Causes in order: Elfsight reviews widget (~3 s main thread), OpenCX widget loaded unpinned from unpkg @latest (NPB loads it twice), FareHarbor embed (~1 MB), theme bundles. Also everywhere: http apex takes 2 redirect hops, redirecting/junk URLs in sitemap, default meta on utility pages, tour pages carry only breadcrumb schema, Best Practices stuck at 54. NPB-only: homepage desktop CLS 0.84, 3 GA4 tags.

## Map pack, one line per brand (checked 2026-10-31)

| Brand | At the pin | Away from the pin |
|---|---|---|
| DCKT | #1 "door county kayak tours", "kayak rental" | Not top 20 at Fish Creek, Sturgeon Bay; Sister Bay only "near me" #9 |
| CPPP | #1 cave point kayak tour, #2 kayaking/rental/bike rental | Not top 20 from any other town; DCKT listing (same address) outranks it |
| NPB | Main listing 0/25 at French Quarter on all 7 kws; tracker numbers were the sibling "New Orleans Party Boats" | Sibling top-3 on 8/25 for party boat terms; "swamp tour" 0/25 both |
| HPB | #1 at dock and Kemah for party boat/barge/bachelorette/boat rental | Nowhere in Houston proper, Galleria, Med Center; mobile Maps impressions fell Sep 19-20, cause unknown |
| NKST | #1 kayak tour, kayak new orleans, manchac | "swamp tour" #5-7; grid top-3 0% on swamp kws; absent at airport/Metairie |
| AKT | #2 austin kayak tour(s), sunset; #3 bat kayak tour | #12 rental; absent "austin bat tour"; LSKT sibling #1 on most; GBP pin 4 km north of lake |
| BBK | #1 on all 5 kws from dock and Discovery Green | 12% of grid top-3; absent Galleria and west Buffalo Bayou Park |

## Paid ads, per account

| Account | 30d | Verdict |
|---|---|---|
| NPB + NKST Google (4378232023) | NKST paused since 10/7 ($486, 0 conv). NPB National 4.2x to 0.94x last 7d, Meta main 2.96x to 1.63x same week | Check site + FH availability before touching bids. Decline all 12 Google recs |
| NOLA Meta act_87863118 | 4 identical Gator Collision ad sets ~$1,220 each at 2.6-3.2x; retargeting 7.1x on $605 is the best in the account | Merge the 4, grow creative 4 to 12+, feed retargeting. Pixel confirmed firing 10/30 |
| DCKT Google + Meta | $0 spend, campaigns ended 9/7 | Pre-stage April relaunch; demote Store visits etc from primary conversions (honest PMax ROAS 3.3x not 7x); archive 24 Meta campaigns, 6 sleepers would restart at $48/day |
| Texas Google (8497383499) AKT/HPB/BBK | AKT $1,713 at 3.25x, 1.22x last 7d (bat season). BBK PMax 7.3x on $15/day. HPB 3.2x vs 5.54 tROAS, 84% impr lost to rank | BBK PMax to $25/day, drop BBK Brand tROAS; pause HPB zero-conv ad groups; AKT Bat Search pause |
| Houston Meta act_1015419897308486 | $1,230 Oct, 0 purchases tracked. BBK pixel PageView only; HPB pixel last fired 2023-06-13 | Fix measurement before spending another dollar |
| Austin Meta act_638850950128825 | $179 Oct 1-7, 263 sessions, 0 purchases. No pixel on austinkayaktours.com, FH passes no fbc/fbp | Measurement first; collapse 34 stale ad sets |

## Fleet + tokens

System map: 2 high / 37 medium / 37 low across 3 Macs. Real failures: medium-importer double-active (both exit 1), npb fb-group-scan FB session expired, admirenola analytics ENOENT on laptop path. idea-radar "script missing" is a false positive.

Token diet (7d): 199 sessions, 6,769 calls, 1.96B cache-read tokens (~290k context re-read per call). Five heaviest sessions 3.3-4.0M each. Images 13.9% of input (over the 10% line), Artifact output 9.1%, Bash cat 7.1%. Long sessions are the cost, not any one tool.

## Dropped from the brief on purpose

Morning brief listed "confirm Oct 12-25 Homebase payroll." Homebase is autopay (David, 10/31 rule), not flagged.

## Files

- Brief: `TheBrain/00 Dashboard/Daily Briefings/2026-10-31.md`
- Tech SEO: `TheBrain/00 Dashboard/Tech SEO/2026-10-31 - {DCKT,CPPP,HPB,AKT,BBK,NKST}.md`, NPB in its own vault `00 Dashboard/Tech SEO/2026-10-31.md`
- Maps: `TheBrain/Marketing/Maps Rank/reports/<brand>/2026-10-31 - *.md`
- SEO audits: each vault's Marketing or SEO Content folder, dated 2026-10-31
- Ads audits: `<vault>/Ads/2026-10-31 *.md` for NPB, DCKT, AKT, HPB, BBK
- Fleet: `TheBrain/07 Reference/System Map/System Map.md`; tokens: `TheBrain/07 Reference/Token Diet 2026-10-31.md`
