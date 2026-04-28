# NKST Guide Comprehension Quiz — Answer Key & Grading Reference
*Last updated: 2026-04-28 | Owner: Manager + Owner | Confidential, do not share with guides*

This is the canonical answer key and grading rules for the NKST Guide Comprehension Quiz. The Google Form auto-grades using these answers. The manager uses this doc to grade paper retakes, run coaching conversations, and update the Form when policies change.

> **Sync rule:** This doc, the quiz markdown (`Guides/NKST — Guide Comprehension Quiz (Expanded).md`), and the Apps Script (`Operations/google-forms-setup.gs`) all carry the same answer key. If you change one, change all three. Update this doc first; it's the source of truth.

---

## Pass Rate Logic

**Threshold: 80% (24 of 30 correct).**

| Score | Outcome |
|-------|---------|
| 28-30 / 30 | Excellent. Solo sign-off cleared. |
| 24-27 / 30 | Pass. Solo sign-off cleared. Manager reviews missed questions in next coaching session. |
| 21-23 / 30 | Below pass. Coaching session before retake. Retake within 7 days. |
| Under 21 / 30 | Significant gaps. Retraining required (re-read flagged docs, re-quiz after manager approval). |

**Annual renewal:** Same threshold. Failure to pass after retake = paused from scheduling until completed.

**Coaching after fail:** Manager reviews each missed question with the guide and confirms understanding before retake. Document the conversation briefly in `Guides/[Name]/coaching_notes_[YYYY].md`.

---

## Master Answer Key

| # | Section | Correct | Topic |
|---|---------|---------|-------|
| 1 | Safety | B | Honey Island gauge under 5 ft = move to Manchac |
| 2 | Safety | B | PFD reframe (immersion + disorientation) |
| 3 | Safety | C | Audible thunder = off the water now |
| 4 | Safety | B | Capsize: reassure, signal, paddle to assist |
| 5 | Safety | B | Bad-smelling PFD: set aside, flag manager |
| 6 | Safety | B | Anaphylaxis: 911 with GPS, monitor |
| 7 | Safety | B | Booking-specific waiver only, no paper, no generic QR |
| 8 | Safety | B | Flat tire: pull off, guests safe, manager + AAA, stay with guests |
| 9 | Safety | C | Distress signal = three whistle blasts |
| 10 | Safety | C | PFD short: don't launch, call manager |
| 11 | Safety | B | Possible spinal: stabilize in water, don't move, 911 |
| 12 | Vehicle | **D** | Tire pressure: door sticker on that specific van |
| 13 | Vehicle | B | Brake light out: don't roll, text manager |
| 14 | Vehicle | B | Rear-ended: full accident protocol, no fault admission |
| 15 | Vehicle | B | Guest can't drive the van. Ever. |
| 16 | Vehicle | B | Top fuel to 1/2 before parking |
| 17 | Vehicle | C | New noise: log in Post-Tour Damage Report |
| 18 | Conduct | B | Harassment: boundary, redirect, document, report |
| 19 | Conduct | B | Witnessed misconduct is reportable |
| 20 | Conduct | C | No romantic pursuit of guests; immediate termination |
| 21 | Conduct | B | If manager is the issue, contact owner directly |
| 22 | Conduct | B | Slur: redirect, end early if continues, document, report |
| 23 | Incident | B | 24 hours for any guest injury |
| 24 | Incident | C | Yes, near-misses are reportable |
| 25 | Incident | B | Full report: timeline, photos, witnesses, weather, last meal/sleep |
| 26 | Incident | B | Equipment back in service only after manager + shop sign-off |
| 27 | IC Status | B | Guide controls how, NKST controls outcome |
| 28 | IC Status | C | Own taxes, 1099, own GL insurance |
| 29 | IC Status | B | Yes, can decline tours per ICA cancellation notice |
| 30 | IC Status | B | $1M / $2M GL insurance required |

**Bold rows** = answers that have shifted from earlier versions. Q12 in particular: was 60/75 hardcoded, now door-sticker. Vehicle Handbook (Section 3.1) and Vehicle Maintenance Log updated 2026-04-28 to match. All three sources are now in sync.

---

## Coaching Notes (use during manager review)

These are the questions where guides most often miss the point and where the coaching conversation matters most. Manager should be ready to explain the **why**, not just confirm the answer.

**Q2 (PFD lifeguard).** The reframe is the lesson. Guides who answer "it's policy" are technically correct but lose the guest. Reframe = guest cooperates.

**Q3 (distant thunder).** Audible = within 10 miles. The miss is "wait and see." We don't wait.

**Q7 (waiver).** Why this matters: a generic or paper waiver gives a plaintiff's attorney a documentation gap. Booking-specific = defensible.

**Q11 (neck pain).** Spinal injury protocol: PFD is doing the flotation. Moving them risks paralysis. The miss is acting on instinct (get them out of the water) when the right move is to wait.

**Q12 (tire pressure).** Critical. Vans can have very different specs. 60/75 was a legacy spec for one of our vans; not universal. Door sticker is the only correct source. Wrong pressure is a leading cause of passenger-van rollover.

**Q14 (rear-ended).** The miss is "no big deal, exchange info, drive on." Even minor accidents need the full protocol because injuries can surface days later.

**Q20 (romantic pursuit).** Hard line. Guides may not see why post-tour pursuit is different. Answer: power dynamic + brand risk + immediate termination per ICA.

**Q23 (24h reporting).** Any injury, no matter how small. The miss is "it was just a scrape, didn't bother." Document everything.

**Q27 (outcome control).** This is the IC classification protection. Guides need to understand they choose the method; NKST defines the result. If a guide thinks NKST scripts every word, our IC defense gets weaker.

---

## How to Update When Policies Change

When a policy changes (Handbook revision, new SOP, regulatory update), the quiz needs to follow.

1. **Update this doc first.** Change the answer in the master table. Add a coaching note if the change is non-obvious.
2. **Update the quiz markdown** at `Guides/NKST — Guide Comprehension Quiz (Expanded).md` to match.
3. **Update the Apps Script** at `Operations/google-forms-setup.gs` to match.
4. **Decide whether to re-issue.** Material changes (safety, vehicle, conduct) trigger a mid-cycle re-quiz for active guides. Cosmetic changes wait until annual renewal.
5. **Archive the prior version.** Drop a copy of the old quiz markdown in `Archive/Quiz Versions/[YYYY-MM-DD]/` so we can prove what was on the quiz at any point in time. Plaintiff's lawyers ask this.

---

## Audit Trail Requirements

For each guide, each year, retain:
- The Google Form response receipt (PDF or Sheet row + screenshot)
- Score
- Date of completion
- Date of any retake
- Manager coaching notes if a retake was required

Folder: `Guides/[Name]/quiz_pass_[YYYY-MM-DD].pdf`. Retain 7 years.

If the guide takes the quiz on paper (no internet, off-site), the manager grades against this doc, signs and dates the paper, scans to the same folder.

---

## Cross-References

- Quiz (guide-facing version): `Guides/NKST — Guide Comprehension Quiz (Expanded).md`
- Form builder script: `Operations/google-forms-setup.gs`
- Annual signing flow: `Guides/NKST — Annual Guide Acknowledgement Form.md`
- Annual cycle wrapper: `Guides/Annual Retraining Cycle.md`
- Vehicle Handbook (governs Q12-Q17): `Operations/NKST — Vehicle Handbook.md`
- Conduct Policy (governs Q18-Q22): `Guides/Guide Conduct & Anti-Harassment Policy.md`
- Investigation SOP (governs Q23-Q26): `SOPs/SOP — Incident Investigation & Corrective Action.md`
- ICA + Classification Rationale (governs Q27-Q30): `Legal/Independent Contractor Agreement — Template & Legal Analysis.md` and `Legal/Guide Role — Outcome-Based Classification Rationale.md`
