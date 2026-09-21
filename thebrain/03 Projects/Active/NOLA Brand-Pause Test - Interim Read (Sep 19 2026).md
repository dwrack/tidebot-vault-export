# NOLA Brand-Pause Test: Interim Read (Sep 19, 2026)

**Bottom line: the test is leaking, so it can't answer the question yet.** We paused the brand campaign and 38 brand keywords, but never added brand negatives. Google re-routed the same brand searches to the generic phrase keywords still running. Paid brand spend only fell about 13%, not 100%.

Full analytics page: https://claude.ai/artifact/3Tx8nUhLCeRUfCF4cGtGHh (local copy: `NOLA Brand-Pause Test - Analytics (Sep 19 2026).html` in this folder). David's call 9/19: keep the test running, he's reviewing the analytics before deciding on the negatives.

Parent spec: [[NOLA Brand-Pause Test — Sep 2026]]. Data through Sep 18 (11 test days). Nothing in the account was changed today.

## The leak

Search terms matching tiki / freaky / twerk / boogie / pedal / nola party barge, across NPB National + Local + Brand:

| Window | Brand-term spend | Per day | Clicks | Conv | Conv value |
|---|---|---|---|---|---|
| Pre (Aug 25 - Sep 7, 14d) | $727 | $52 | 558 | 29.5 | $5,338 |
| Test (Sep 8 - 18, 11d) | $498 | $45 | 276 | 22.2 | $5,795 |

The Brand campaign itself did stop ($122 to $2). The spend moved next door. During the test, these ENABLED generic keywords caught the brand searches:

| Keyword (phrase/exact) | Brand-query spend | Clicks |
|---|---|---|
| party barge new orleans | $102 | 84 |
| booze cruise new orleans | $87 | 32 |
| new orleans party boat | $62 | 26 |
| party boat ride new orleans | $49 | 22 |
| barge new orleans | $40 | 23 |
| booze cruise nola | $34 | 22 |

Top leaked searches: "freaky tiki new orleans" ($116, 47 clicks, 6 conv), "nola party barge" ($112, 106 clicks, 8.8 conv). Those two alone are about half the leak.

Worse, the clicks got pricier. Pure brand-name searches cost $1.28 a click pre-test and $1.76 during it. "freaky tiki new orleans" now runs $2.46 a click because it's matching to generic keywords like "booze cruise new orleans".

PMax (Sales-Performance Max-12) also went from 1 conversion pre to 19.7 in the test window on $617 spend. Its search categories include "twerkin tiki" and "tiki boat new orleans". Most of its volume is hidden in the uncategorized bucket, but that jump smells like brand traffic landing there too.

Confirmed: the only brand-ish negative on National, Local, or PMax is the "nola pedal barge reviews" exact we added Sep 8.

## What the other checks say (for the record)

| Check | Pre | Test | Read |
|---|---|---|---|
| FH bookings created, NPB (per day) | 20.9 bk / $4,229 | 22.5 bk / $4,969 | Held. But paid brand never really stopped, so this proves nothing. |
| GSC brand clicks, nolapartybarges.com (per day) | 7.4 | 7.9 | Flat. No paid clicks were freed up for organic to absorb. |
| Account spend (per day) | $284 | $304 | Up slightly. Kayak + PMax soaked up budget. |
| Competitor ads on brand terms | none (Sep 8) | see SERP section | |

Gap worth knowing: nolaboozecruise.com and neworleanstikiboats.com are not in Search Console under dwrack81, so organic absorption can only be measured on nolapartybarges.com. They rank #1 for the tiki terms, so that's a real blind spot.

## Recommended fix

Add these as campaign-level negatives on NPB National (23480870878), NPB Local (23480870632), and PMax (24184656153), then restart a clean 14-day clock:

- Phrase: `freaky tiki`, `twerkin tiki`, `twerking tiki`, `bayou boogie`, `nola party barge`, `nola pedal barge`, `pedal barge`
- Exact: `nolapedalbarge`, `nolapartybarge`, `nolapartybarges`

Deliberately NOT negated: "tiki boat new orleans" and "pedal pub new orleans". Those are category searches a competitor could win, not our brand names.

If added Sep 19 or 20, the clean window runs to Oct 3 or 4. That still lands before the Halloween push.

Revert is easy: remove the 10 negatives, un-pause the campaign and 38 keywords.

## SERP check (Sep 19)

Live Google SERPs, New Orleans, desktop + mobile, 5 brand terms (freaky tiki new orleans, nola party barge, twerkin tiki new orleans, bayou boogie party boat new orleans, nola pedal barge). 10 snapshots.

- **Competitor ads: zero.** Nobody moved in on the vacated terms.
- Our ads didn't show in any snapshot either. The leak is intermittent, not every search, but the search terms report shows it's still $45 a day.
- Organic #1 on every term is ours (nolapartybarges.com or nolaboozecruise.com). Usually #2 and #3 as well.
- Only outside seller in any top 3: letsbatch.com, a reseller listing of the Freaky Tiki at organic #3 on desktop.
- Side note: paddlebooking.com ranks #8 for "bayou boogie" with the old 6301 Paris Road Chalmette address. Stale listing, worth a fix request sometime.

So the original hunch still looks right. No competition, organic owns the page. We just haven't run the clean test that proves it.

## What to tell Michael on Sep 22

The honest version: "First two weeks were contaminated. Brand searches kept triggering ads through our generic keywords. Bookings held, but that's not evidence yet. We plugged the hole on [date] and will have a real answer on [date + 14]."
