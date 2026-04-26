# Google Ads Cleanup — FareHarbor Tracker

**Started:** 2026-04-25
**Owner:** Davey
**Vendor:** FareHarbor (Kevin Schmitt + Jasantha Mari)
**Cadence:** Weekly status check (Fridays)

---

## Baseline (last 30 days, pre-fixes)

| Account | Spend | Conv | ROAS | All-conv ROAS |
|---|---|---|---|---|
| Gravity Trails NOLA | $3,439 | 197 | 15.09 | 38.4 |
| Lone Star Austin | $1,163 | 25 | 4.13 | 10.3 |
| Door County | $366 | 3 | 1.64 | 1.64 |
| Houston Party Barge | $0 | 0 | n/a | n/a |

Re-pull these monthly to track impact.

---

## P0 — Quick Wins (target: this Friday)

- [ ] **Negative kw — NOLA**: add "booze cruise" to NPB campaigns
- [ ] **Negative kw — Lone Star**: add "private party boat rental"
- [ ] **Door County brand search debug**: investigate why "door county kayak tours" got 11 clicks $20 spend / 0 conv. Likely tracking gap on dcdetours.com or FareHarbor checkout pixel.
- [ ] **Mobile bid modifiers (NOLA)**:
  - [ ] NPB Brand: +25%
  - [ ] NPB National: +15%
  - [ ] NPB Local: +15%
  - [ ] NKST National: leave
  - [ ] NKST Local: -15%
  - [ ] All campaigns tablet: -50% or exclude

## P1 — Landing Page Fixes (scope by next Friday, ship within 2 weeks)

### Bat tour LP (lonestarkayaktours.com/kayak/sunset-bat-bridge-kayak-tour/)

Current: $678 spend / 1.9% CVR / 1.62 ROAS / Quality Score 4-5 / LP grade B

- [ ] Replace building hero image with sunset bat emergence photo
- [ ] Embed FareHarbor calendar widget above the fold (not redirect)
- [ ] Add aggregated star rating + review count above the fold
- [ ] Add live scarcity ("X spots left tonight")
- [ ] Sticky mobile booking widget
- [ ] Named guide bio with photo (Boats and Bats does this well)

Target: 4%+ CVR, ROAS 4+, Quality Score to 7+

### Swamp tour LP (neworleanskayakswamptours.com homepage)

Current: $1,101 spend / 10.3% CVR / 9.12 ROAS / "swamp tour" QS:3 / LP grade B

- [ ] Aggregated star rating + review count above the fold (mirror Wild Louisiana's "Over 600 Five-Star Reviews")
- [ ] Pull tour cards with "From $X" pricing higher
- [ ] Embedded FareHarbor calendar above the fold
- [ ] H1 rewrite to match search intent ("Small-group kayak swamp tours in New Orleans, from $65")
- [ ] Move "frequently sells out" out of FAQ to booking area
- [ ] Build dedicated /swamp-tour-new-orleans/ page for keyword relevance

Target: 12%+ CVR, ROAS 12+, Quality Score 7+

## P2 — Conversion Tracking (target: end of month)

- [ ] Audit + archive duplicate/inactive purchase trackers on NOLA (7+ legacy ones)
- [ ] Enable `view_book_form` as a SECONDARY conversion signal (not primary)
- [ ] Verify pixel firing on FareHarbor checkout for Door County

## P3 — Account Restructure (target: end of June)

- [ ] Move Houston Pedal Barge campaigns off Lone Star Austin account onto own dedicated account + pixel
- [ ] Get a roadmap for separating each brand into its own ad account, all linked under one MCC
- [ ] Decision: lonestarkayaktours.com vs austinkayaktours.com for "bat tour austin" — consolidate or separate?

---

## Weekly check-in log

Update each Friday:

### Week of 2026-04-27
- Email sent: [date]
- FareHarbor reply received: [date]
- Items completed:
- Items in progress:
- Blockers:

### Week of 2026-05-04
-

### Week of 2026-05-11
-

---

## Reference

- Audit data: ran 2026-04-25 via `~/.claude/mcp-servers/google-ads/` MCP
- Accessible accounts: 4378232023 (NOLA), 8497383499 (Lone Star Austin), 8672151991 (Door County), 2986009791 (HPB, no spend)
- Davey MCC: 4064677082 (empty, FareHarbor accounts not linked yet)
