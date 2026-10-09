# Website Rebuild: Periode Live Availability (Oct 2026)

**Verdict: works.** Periode's slot data is publicly readable over the Firestore REST API with only the public web apiKey, no login. A Cloudflare Pages Function can fetch it with one POST and show "Next open: 5:00 PM today, 3 seats". Verified 2026-10-08 against the live booking page for Oct 9: all 7 Social Sauna slots matched exactly.

## Where the data lives

- Project `periode-prod`. Public web apiKey is in `https://minside.periode.no/env-config.js` (`window.firebaseConfig.apiKey`). It's the same key every visitor's browser gets, not a secret, but read it at runtime or keep it in an env var instead of hardcoding.
- **Slots:** `dateSlots/{orgId}/manifests/{productId}/slots/{YYYY-MM-DD}`
  - One doc per day. Doc ID = date, field `date` (string).
  - `slots` = array of `{ time, length, available, reserved, cancelled, deleted, booked, confirmed, onlyMembers, priceAdjustments, customMessage? }`
  - `time` = decimal hour in local time (17 = 5:00 PM, 17.5 = 5:30 PM). `length` in hours (1.75).
  - **Open seats = `available - reserved + cancelled + deleted`**. That's the exact formula in Periode's own bundle (`wf=e=>e.available-e.reserved+e.cancelled+e.deleted`).
- **Product config:** `bookingManifests/{productId}`: `name`, `timezone` (America/Los_Angeles), `capacity`, `closedDates`, `startDate`/`endDate`, `enabled`, `archived`, `generateDaysAhead` (45 for Social Sauna). Also public.
- No callable Cloud Function is involved. The booking page uses `onSnapshot` on the slots query (`where date >= X and date <= Y`).

| Product ID | Name | Capacity | Slots in Firestore? |
|---|---|---|---|
| w5FpVIGDc7DPhwYo5u3w | Social Sauna | 8 | yes, 7/day |
| ZnuD3bNp60NmHWN9qsXp | Sunrise Sauna | 8 | yes, 6:00 AM |
| HCzS2cNh0TNBxNvhj7nY | Moonlight Sauna | 8 | yes, 9:00 PM |
| Hy1DLi3fx7KiCgYCtAuT | Private Sauna | 1 | **none returned**: probably uses a parent product or the `availabilityBitmap` collection. Needs a separate look if privates go on the homepage |

Org ID: `wE4l5rKVuae2oCBE93gz`. Deep link: `https://minside.periode.no/booking/{org}/{product}/YYYY-MM-DD/HH:MM`

## Working example (Node 18+ / Workers `fetch`)

```js
const KEY = env.PERIODE_WEB_KEY; // public web apiKey from env-config.js
const ORG = 'wE4l5rKVuae2oCBE93gz', PRODUCT = 'w5FpVIGDc7DPhwYo5u3w';
const base = 'https://firestore.googleapis.com/v1/projects/periode-prod/databases/(default)/documents';
const ymd = d => d.toLocaleDateString('en-CA', { timeZone: 'America/Los_Angeles' });
const today = ymd(new Date()), tomorrow = ymd(new Date(Date.now() + 864e5));
const num = f => f.integerValue !== undefined ? Number(f.integerValue) : f.doubleValue ?? f.booleanValue ?? f.stringValue;

const res = await fetch(`${base}/dateSlots/${ORG}/manifests/${PRODUCT}:runQuery?key=${KEY}`, {
  method: 'POST', headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ structuredQuery: { from: [{ collectionId: 'slots' }], where: { compositeFilter: { op: 'AND', filters: [
    { fieldFilter: { field: { fieldPath: 'date' }, op: 'GREATER_THAN_OR_EQUAL', value: { stringValue: today } } },
    { fieldFilter: { field: { fieldPath: 'date' }, op: 'LESS_THAN_OR_EQUAL',    value: { stringValue: tomorrow } } } ] } } } })
});
const slots = (await res.json()).filter(r => r.document).flatMap(r => {
  const date = r.document.fields.date.stringValue;
  return (r.document.fields.slots?.arrayValue?.values || []).map(x => {
    const s = Object.fromEntries(Object.entries(x.mapValue.fields).map(([k, f]) => [k, num(f)]));
    const hh = Math.floor(s.time), mm = Math.round((s.time - hh) * 60);
    const hhmm = `${String(hh).padStart(2, '0')}:${String(mm).padStart(2, '0')}`;
    return { date, time: hhmm, open: s.available - s.reserved + s.cancelled + s.deleted, onlyMembers: s.onlyMembers,
      url: `https://minside.periode.no/booking/${ORG}/${PRODUCT}/${date}/${hhmm}` };
  });
});
// "Next open" = first slot with open > 0, !onlyMembers, start time later than now (PT)
```

Simpler single-day alternative: `GET {base}/dateSlots/{ORG}/manifests/{PRODUCT}/slots/2026-10-09?key=KEY`.

Output 2026-10-08 ~9:40 PM PT: Oct 8 slots 8/8/7/8/5/3/1 open; Oct 9 = 8, 5, 0, 5, 8, 5, 8 (matched the page exactly).

## Filtering the homepage function should do

- Drop slots whose start time is already past (the data still includes today's earlier slots).
- Skip `open <= 0`, `onlyMembers: true`, and dates in the product's `closedDates`.
- If a slot has `customMessage` and `available === 0`, Periode shows the message instead of seats. Treat it as not bookable.

## Risks

- **Unofficial.** It's Periode's internal schema, not an API they promise to keep. A field rename or a tightened Firestore security rule breaks it silently. Build it to fail soft: hide the widget, keep the plain "Book" button.
- **Key restrictions could change.** Today the key works from curl with no referrer. If Periode adds HTTP-referrer restrictions, server-side calls die first.
- **Load and courtesy.** Every read bills to Periode's Firebase project. Cache the result at the edge for 60 to 120 seconds (Workers Cache API or KV) so site traffic never maps 1:1 to Firestore reads. At that cache rate it's about 1 query a minute per product, which is trivial. No published rate limit, but don't poll per visitor.
- **Seat counts are a snapshot.** A 2-minute cache can show "1 seat" that just sold. The deep link lands on Periode's live page, which is the source of truth, so the worst case is a mild letdown, not a double booking.
- Worth a one-line ask to Erik at Periode (erik@periode.no) whether they're OK with it or have a supported endpoint coming. Not a blocker.
