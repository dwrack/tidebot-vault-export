# 07 — Vendors & Tech Stack
*Part of [[DCKT Playbook — Master Index]]*

---

## Core Operations Stack

| Vendor | Role | Account / Contact | Notes |
|---|---|---|---|
| **FareHarbor** | Bookings, website host, job applications | info@doorcountykayaktours.com | WordPress site hosted by FH. Submit requests at fareharbor.com/help/submit/ |
| **Homebase** | Scheduling, payroll, time tracking | Active | Free plan covers up to 20 employees / 1 location. Payroll add-on ~$39/mo |
| **GHL (Go High Level)** | CRM, customer/guide comms, marketing automation | DCKT sub-account in agency dashboard | Set up but underutilized — Bella to build guide automation sequences |
| **Google Workspace** | Email, Drive, docs | doorcountykayaking@gmail.com + info@doorcountykayaktours.com | Forwarded to dwrack81@gmail.com |
| **GroupMe** | Guide team chat | Active | Primary internal comms for guides on-water and on-shift |

---

## Bookings & Distribution

| Vendor | Role | Notes |
|---|---|---|
| **FareHarbor** | Primary booking platform | All tours, rentals, e-bikes, job applications, accountability forms |
| **GetYourGuide** | OTA distribution | Connected via FareHarbor API. Set +20% markup via FareHarbor |
| **Viator** | OTA distribution | Connected via FareHarbor API. Viator business profile must be kept current |
| **Airbnb Experiences** | Additional distribution | Added 2025 — confirm still active for 2026 |

**Important FareHarbor note:** Always include the specific site URL when submitting install requests. Your email is the primary contact for multiple sites. Wrong site installs have happened (see State of Play doc — Conner Quarles / NOLA chatbot incident).

---

## Media & Photography

| Vendor | Role | Credentials |
|---|---|---|
| **SmugMug** | Photo hosting + customer sales | Upload within 24 hrs of every tour. Password: kayak |
| **dcphotofun.com** | Customer-facing photo download portal | Password for gallery access: **kayak** |

**Photo price:** $20 for all photos (before or at booking)
**Watermark protection:** Go to gallery settings → Photo Protection → ON → password: kayak

---

## Print & Marketing

| Vendor | Role | Account Info |
|---|---|---|
| **GotPrint** | Brochure printing | Account: info@gravitytrails.com / password: Cool6006 |
| **Canva** | Ad design + social media creative | Used for sauna ads, House of Clouds, Detours branding |
| **Google Ads** | Paid search advertising | Active |
| **Meta / Facebook** | Paid ads + catalog | Active |

**Brochure distribution:** Door County rack cards throughout county. Restock regularly through the season.

---

## Waivers & Legal

| Vendor | Role | Notes |
|---|---|---|
| **iWaivers** | Digital waivers via QR code | Guides display QR at launch — all guests sign before getting in boats |
| **DocuSeal** | Employment contracts, e-signatures | Open source — replacing DocuSign/DocHub. Self-host or docuseal.co. Get Bella sender access once deployed. |

---

## Insurance & Finance

| Vendor | Role | Contact |
|---|---|---|
| **Zodiac Insurance** | GL insurance carrier | Mike Carlin — mcarlin@zodiacinsurance.com |
| **Imperial PFS (IPFS)** | Premium financing | Tom Keegan — notifications@ipfs.com |

---

## AI & Automation

| Vendor | Role | Contact | Notes |
|---|---|---|---|
| **Rawgrowth.ai** | AI/chatbot installations, n8n | Conner Quarles — connerquarles13@gmail.com | Chris West is agency lead |
| **n8n** | Automation workflows | Active on NOLA Party Barge | DCKT chatbot not yet built |

**Pending for DCKT:**
- AI chatbot for doorcountykayaktours.com (port from NOLA Party Barge "Nolan" template)
- GHL guide comms automation sequences (Bella's project)
- FareHarbor → GHL booking confirmation/reminder automation

---

## Staffing / HR Tech

| Vendor | Role | Notes |
|---|---|---|
| **Homebase** | Scheduling, clock-in/out, time tracking, team messaging | Current — keep for shift management |
| **BambooHR** (proposed) | Onboarding docs, employee records, e-signatures | Strong REST API. Fills gap Homebase can't |
| **Rippling** (proposed) | Full HR + IT + payroll | Most powerful but most complex/expensive |
| **WorkBright** (optional) | Seasonal worker onboarding | Designed for seasonal/summer staff — worth evaluating |

---

## Accounts to Maintain

Bella should have access to (or be trained on) all of the following:

| System | Access Level Needed |
|---|---|
| FareHarbor | Manager — booking dashboard, availability, job application forms |
| Homebase | Manager — scheduling, payroll, employee records |
| GHL (DCKT sub-account) | Admin — workflow builder, contacts, comms |
| doorcountykayaking@gmail.com | Manager access or forward/alias |
| Google Drive (DCKT folder) | Editor |
| SmugMug | Uploader / Organizer |
| DocHub or DocuSign | Sender |
| GotPrint | Account access for brochure reorders |

---

## New Experiences / DBAs — Tech Notes

| Experience | Brand | Social / Booking |
|---|---|---|
| **Lykke Sauna** | Lykke Sauna Co. | Listed on FareHarbor, social media, iWaivers for sauna sessions |
| **E-bike Tours** | Cave Point Paddle & Pedal / DoCo Kayak & Bike | On FareHarbor, GetYourGuide, Viator |
| **House of Clouds & Curiosity** | DCKT / potential standalone | FareHarbor listing in progress (2025) |
| **Door County Detours** | Detours | Separate brand: @doorcountydetours IG/TikTok/FB, doorcountydetours@gmail.com |
