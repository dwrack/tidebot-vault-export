# FareHarbor API — Capabilities & Integration Plan
*Researched March 29, 2026*

---

## Authentication
- API key auth (two headers: App key + User key)
- **Not self-service** — must contact FareHarbor to get credentials
- Company shortname: `doorcountykayaktours`
- Contact: support@fareharbor.com

---

## What We CAN Do

| Operation | Supported | Notes |
|---|---|---|
| Read real-time availability | YES | Pull in 7-day increments (date-range endpoint times out on larger windows) |
| Create a booking | YES | Full write access |
| Cancel a booking | YES | DELETE endpoint |
| Modify/update a booking | YES (partial) | Some fields only |
| Reschedule a booking | YES (effectively) | Cancel + rebook = two API calls |
| Receive webhook: booking created | YES | Instant |
| Receive webhook: booking cancelled | YES | Instant |
| Receive webhook: booking rebooked | YES | Fires with `status: "rebooked"` |
| Receive webhook: customer check-in | YES | |
| Receive webhook: payment data | YES (opt-in) | Not in default schema |
| Access customer contact data | YES | Name, email, phone in booking payload |

## What We CANNOT Do
- Push availability changes (dashboard-only)
- Push product/listing changes (dashboard-only)
- Self-register webhooks (must email support@fareharbor.com)
- Native CRM integration (doesn't exist yet)

---

## Best Integration Path: FareHarbor → CRM Direct

**No Zapier/Make needed.** The CRM supports an "Inbound Webhook" workflow trigger with a unique URL. Give that URL to FareHarbor support to register. Booking events fire instantly into the CRM.

### What triggers from FareHarbor → CRM:
- Booking created → create/update CRM contact, tag, fire welcome SMS sequence, set day-before + day-of + review triggers
- Booking cancelled → win-back SMS, tag `cancelled`
- Booking rebooked (rescheduled) → updated confirmation SMS
- Customer check-in → post-tour review request SMS (1-2hr delay)
- Payment data (opt-in) → payment follow-up if needed

### Writing back to FareHarbor from the CRM:
- Requires a CRM outbound webhook + custom FareHarbor API call
- Reschedule from the CRM = cancel via API + rebook via API
- Feasible with custom workflow — not out of the box

---

## Setup Steps
1. Get FareHarbor API credentials — email support@fareharbor.com (request Software Partner access)
2. Set up the CRM Inbound Webhook workflow trigger → copy the URL
3. Email support@fareharbor.com to register the CRM URL as webhook endpoint
4. Configure webhook to include payment data (opt-in)
5. Build CRM workflows for each event type
6. Test with a real booking

---

## Automation Flows to Build (Priority Order)

### Phase 1 — Fire and forget (webhooks → CRM → SMS)
1. Booking created → welcome SMS + day-before trigger set
2. Booking cancelled → win-back SMS
3. Booking rebooked → updated confirmation SMS
4. Check-in → post-tour review SMS (1-2hr delay)

### Phase 2 — Smart flows
5. Weather cancel trigger (manual in the CRM) → blast SMS to all today's bookings
6. Group booking 10+ → flag for personal call from David/Bella
7. Missed call → auto-SMS within 60 seconds

### Phase 3 — Write-back (custom code)
8. Reschedule from the CRM → cancel + rebook via FareHarbor API
9. Availability check before suggesting reschedule times
