# FareHarbor Capability Map

Built 2026-10-13 from all 654 articles in `md/` (help center pulled 2026-10-13). Paths are relative to `~/Projects/fareharbor-help/`. "Support" means the article says FareHarbor Support, your Account Manager or a request form must enable or configure it. "Opt-in" means a self-serve toggle. Several articles contradict each other; those are flagged in section 6. Help articles describe what was true when written, so confirm in each live dashboard before acting.

## 1. One-page summary: 25 capabilities most operators leave unused

Revenue
1. Dynamic Pricing 2.0: AI demand-based pricing within price levels you approve; Support enables it. `md/54312757536027-introduction-to-dynamic-pricing-2-0.md`
2. Price schedules with dynamic rules: capacity rules ("Increase price by 20% when there are 3 spots remaining") and time rules (25% off a week ahead); Support builds them. `md/40897564606875-using-price-schedules-with-dynamic-rules.md`
3. Combos and Packaged combos: upsell page after the first booking, with seasonal discounts; one report shows results. `md/42957728899611-setting-up-combos.md`, `md/42957744220443-packaged-combos.md`
4. Cross-Sell Combos: sell a neighbor's item inside your checkout; no commission engine, you price it in. `md/42957735775643-cross-sell-combos.md`
5. Suggested items on cart and confirmation page/email. `md/40897852857755-suggested-items.md`
6. Abandoned cart email, one email 2 hours after drop-off, needs the online cart. `md/40897602138523-abandoned-cart-recovery.md`
7. Waitlist with automatic "seat opened" email on cancellation. `md/42957506762395-waitlist.md`
8. Deposits and payment links: take a deposit online, let customers pay the balance from the confirmation email. `md/40898010428315-deposits.md`, `md/42957750164379-using-payment-links-for-underpaid-bookings.md`
9. Memberships with punchcard benefits and auto-renew. `md/40897569988507-creating-memberships.md`, `md/42957494045595-purchasing-using-and-renewing-memberships.md`
10. Gift cards with custom designs, plus issuing a gift card instead of a refund. `md/40897463368859-creating-gift-card-designs.md`, `md/40897504237851-giving-credit-using-gift-cards.md`
11. Private Events: contracts, payment schedules, proposals, for charters and buyouts (North America only). `md/40897283393307-introduction-to-private-events.md`
12. Seat maps sold online, so customers pick (and you can upsell) premium seats. `md/40897668719003-introduction-to-seating-assignment.md`

Distribution
13. FHDN (FareHarbor Distribution Network): one contract, many resellers; 20% referral or 25% API commission. `md/42957709413403-fareharbor-distribution-network-fhdn-overview.md`
14. Google Things to Do: commission-free Google bookings. `md/40898232783003-google-things-to-do-integration.md`
15. FareHarbor in ChatGPT: FHDN inventory bookable inside ChatGPT. `md/47076472962459-fareharbor-in-chatgpt.md`
16. Affiliate toolkit: promo codes, QR codes, widgets, blocks, rules, settings groups. `md/42957577429019-affiliate-booking-methods.md`
17. Airbnb Experiences and Viator special offers. `md/40898086122395-working-with-airbnb-experiences.md`, `md/51495663149083-viator-special-offers.md`

Automation and communication
18. Per-item automatic reminder emails, follow-up emails (with Google review link or your survey URL) and reminder texts. `md/40897385230363-automatic-reminders-and-follow-ups.md`, `md/40897349493531-social-media-and-survey-urls.md`
19. FareHarbor Agent: 24/7 AI chat/SMS/WhatsApp/phone/email agent on your FH data. `md/48858951282075-introduction-to-fareharbor-agent.md`
20. Webhooks (booking and item events) plus Zapier. `md/40898279460763-configuring-webhooks.md`, `md/40898281485339-introduction-to-the-zapier-integration.md`
21. Free FareHarbor Waivers and standalone waiver links/QR. `md/40897871757339-fareharbor-waivers.md`, `md/54050261537563-waiver-links.md`
22. Native GA4 and Meta Conversions API purchase events. `md/42957815081883-setting-up-google-analytics-4-ga4-to-work-with-fareharbor.md`, `md/42957825564827-tracking-conversions-with-the-meta-facebook-pixel.md`

Control and insight
23. Pace report (booking pace vs same point last year) and Item occupancy report. `md/48197997852443-introduction-to-the-pace-report.md`, `md/51274856853659-item-occupancy-report.md`
24. Online rebooking and online cancellation by the customer, driven by cancellation policies. `md/40897213805723-online-rebooking.md`, `md/42957504194715-canceling-bookings.md`
25. Booking restrictions toolkit: custom sold-out text, unlisted availabilities, "Open" override, negative cutoffs (book after start), reservation timer, online queuing. `md/42957724449051-booking-restrictions.md`, `md/40897924991771-how-do-i-change-online-booking-cutoff-times.md`, `md/40897508706715-reservation-timer.md`

## 2. Area-by-area map

### 2.1 Items and availability

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Create/duplicate item | Build new or duplicate; duplicate copies pricing, notes, notifications, schedules, not availabilities (always created Private) | Item Setup Checklist green/orange/red | Builds Team on request | `md/40897518310427-creating-an-item.md` |
| Item listing | Name, SKU, headline, description, photos (1800px+, up to 10) | First photo is main | No | `md/40897518866843-managing-an-item-s-listing.md` |
| Content Builder | Structured listing (highlight box, overview, FAQs, cancellations) with AI format button | Short description 150 chars; FAQ answer 1,000; required for Booking.com | Tab may need Support | `md/40897489868315-content-builder.md` |
| Archive/delete/private/unlisted | Archive blocked with future bookings; delete blocked with any bookings | Unlisted = direct link only | No | `md/40897505139611-archiving-an-item.md`, `md/40897506401819-deleting-an-item.md`, `md/40897479531931-updating-an-item-s-online-booking-settings.md` |
| Retail items | "Buy now" items for merch, gifts, memberships; turns off most customer notifications except abandoned cart | Settings do not revert when toggled off | No | `md/39062128436251-set-up-a-retail-item.md`, `md/45944867557915-reverting-retail-item-settings.md` |
| Item tags | Predefined tags for affiliate search (about 5 per item) | | Yes | `md/40897509473691-tagging-items.md` |
| Item colors | 12 preset colors across calendars/manifest | Not shown to customers | No | `md/40897505667355-working-with-item-colors.md` |
| Creating availabilities | Creator view or saved Availability Schedules; repeat up to 2 years out | 25,000 at once; scheduler locks after 5 min idle | Permissions may need Support | `md/40897157383579-creating-availabilities.md` |
| Duplicate availabilities | Copy a year of availabilities to next year | Copies are not bookable online by default | No | `md/40897157383579-creating-availabilities.md` |
| Availability updater | Bulk change status, capacity, headline, start time, length, customer types, whole-booking fields, resource requirements, pickup route, crew, blocks, notes | 20,000 at once; does not touch dates (duplicate and rebook instead) | No | `md/40897171773979-update-availabilities.md`, `md/40897163348635-changing-the-date-of-an-availability.md` |
| Online booking status | Auto close, Open (ignores cutoffs), Closed and Call to book, Closed and hidden, Cancelled, Unlisted | Cancelling does not cancel bookings or notify customers | No | `md/40897163756955-changing-online-booking-status.md`, `md/40897123112859-canceling-availabilities.md` |
| Booking restrictions | Min/max party size, auto-close timing, call-to-book text, Waitlist; separate rules for empty vs booked availabilities | Online only; staff can still book | No | `md/42957724449051-booking-restrictions.md`, `md/40897202052635-changing-an-availability-s-booking-restrictions.md` |
| Cutoff times | Hours before start or before midnight; negative hours allow booking after start | Three levels: dashboard, item, availability | No | `md/40897924991771-how-do-i-change-online-booking-cutoff-times.md` |
| Custom sold-out message | Replace "call to book" with e.g. Sold Out | Per item | No | `md/40897941513755-how-do-i-change-the-message-displayed-for-sold-out-availabilities.md` |
| Waitlist | Customers join on full availabilities; staff email or auto-email when seats open | Auto email 1 per customer, cannot be customized, 5 min spacing; not for retail or memberships | Opt-in toggles | `md/42957506762395-waitlist.md` |
| Reservation timer | Holds selected capacity 10 minutes with visible timer | Per item | Yes | `md/40897508706715-reservation-timer.md` |
| Online queuing | Virtual line when demand spikes; 15 min per cart item | FareHarbor sets limit, not adjustable | Automatic | `md/40897520707099-managing-high-volumes-with-online-queuing.md` |
| Capacity and customer type capacity | Total capacity, per-type capacity, per-booking min/max | Most restrictive wins | No | `md/40897166960923-availabilities-and-capacity.md`, `md/40897443464603-customer-types-overview.md` |
| Resources | Boats, kayaks, guides with max uses, overrides, requirements, timeline | Changes to resources: Support strongly recommended; resources removed from online calendar when exhausted, no Sold Out message | Yes (recommended) | `md/40897623777947-resources-overview.md`, `md/40897599314843-resource-faqs.md`, `md/42957498439067-manage-resource-overrides.md`, `md/40897653002139-using-the-resources-timeline.md` |
| Resource requirements | Per customer or whole booking, prep/cleanup timing, split parties, hidden per price sheet | Reapply resources after edits | Settings > Resource Requirements may need Support | `md/40897652546331-setting-up-resource-requirements.md`, `md/40897583177883-reapplying-resource-requirements.md` |
| Auto-archive resources | Archives unused resources after 365 days by default | Opt-out in Advanced company settings > Performance | No | `md/42957497827227-archiving-resources.md` |
| Seat maps and seating | Map builder, zones, groups, auto-assign, online seat selection, exclusive groups, buyout fill-all | Needs "Manage seat maps"; maps over 400 split | Yes | `md/40897708072987-using-the-seat-map-builder.md`, `md/40897662663963-managing-seating-settings-for-an-item.md`, `md/40897643117339-auto-assigning-seats-to-customers.md`, `md/40897646461851-using-exclusive-seating-groups.md`, `md/40897656251931-using-seating-with-buyouts.md`, `md/40897671433115-blocking-and-unblocking-seats.md`, `md/40897674508315-managing-seat-assignments.md`, `md/40897616738331-assigning-seats-while-booking.md` |
| Transportation | Lodging, pickup locations, routes, pickup manifest, dispatch schedule | One base rate on the field; lodging list cannot be limited | Yes | `md/40897708407963-transportation-basics.md`, `md/47573562952347-route-planning.md`, `md/40897708820763-transportation-faqs.md`, `md/40897666959771-updating-transportation-settings.md`, `md/40897710461851-using-the-manifest-to-view-pickup-routes.md` |
| Headlines | Public headline (with photo and confirmation notes) and private headline per availability | Private not translatable | No | `md/40897164314267-managing-availability-headlines.md` |
| Availability notes | Staff-only Markdown notes on manifest | | No | `md/40897175691291-working-with-availability-notes.md` |
| Availability pricing | Per-availability price override | Not recommended; conflicts with schedules/affiliate sheets | Contact Support first | `md/40897144641435-working-with-availability-prices.md` |
| Booking flows | Group items into pages, also drive suggested items | Custom flows do not auto-add new items; default flow change affects FH profile and site | Directors only by default; Support assists | `md/40897872308251-introduction-to-booking-flows.md`, `md/40897873586971-managing-booking-flows.md` |
| Combos, Packaged combos, Cross-Sell Combos | See 2.5 | | | |
| Bookings calendar views | Month, Grid, Day, Agenda, Timeline, Multiday timeline; custom calendars per user | New items not in filtered custom calendars until edited | No | `md/40897254646043-customizing-your-bookings-calendar.md`, `md/40897225844123-saving-custom-calendars.md` |
| Calendar subscription (ICS) | Bookings to Google/Outlook/Apple calendar | 7 days back, 42 ahead; Google can lag 12 hours | Build section may need permission | `md/40897927395227-how-do-i-add-my-fareharbor-calendar-to-my-mobile-device-or-computer.md` |
| Online price previews | Prices on grid, calendar, availabilities | Items with more than 30 availabilities per day show none; cached up to 60 min | Taxes/fees inclusion needs Support | `md/42957817873179-price-previews-for-online-booking.md`, `md/47317945396251-price-preview-locations-and-display-logic.md` |
| Total price display | Include fees and taxes in all prices | Default on in EU/UK, AU/NZ, ZA, Canada, price-transparency US states | Else Support | `md/55230875441563-total-price-display-for-online-booking.md` |
| Search by date | Pick a date, see all bookable activities | | Permission/Support | `md/40898519444891-using-search-by-date-for-online-booking.md` |
| Google ratings on book form | Shows rating from Place ID | 100+ reviews and 4.2+ stars | Yes | `md/40897237339035-google-ratings.md` |
| Locations | Directions, map links, Place IDs, headings used in emails, Google Calendar, Tripadvisor | Transportation details replace locations when present | Hiding while keeping association: Support | `md/40897375707931-locations.md` |

### 2.2 Pricing, customer types, custom fields

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Customer types | Person/child/etc.; exclusive types for charters; family and group types; ticket color for QR | Item-level capacity changes do not update existing availabilities | No | `md/40897433004571-setting-up-customer-types.md`, `md/40897442777627-exclusive-customer-types.md`, `md/40897443464603-customer-types-overview.md` |
| Customer type admin | Reorder, archive, remove, delete, visibility per price sheet | Re-adding a deleted name creates a new type; API-connected: Support removes types | API case yes | `md/40897432300187-reordering-customer-types.md`, `md/40897414300315-archiving-customer-types.md`, `md/40897459688475-removing-and-deleting-customer-types.md`, `md/40897500740123-updating-customer-type-visibility.md` |
| Price sheets | Base, Online, Direct, affiliate sheets with inheritance; Overview tab edits all items; Adjustment column for percent change | Auto-archive after 730 days default | Adjustment column may need Support | `md/40897574874907-introduction-to-price-sheets.md`, `md/40897594780699-using-price-sheets.md`, `md/42957526035483-archiving-price-sheets.md`, `md/42957526845211-updating-customer-type-prices.md` |
| Price schedules | Rule-based sheets by booking date/day or availability date/day/time | Must set as company default to take effect | Seasonal setup: Support offered | `md/40897588033691-introduction-to-price-schedules.md`, `md/40897586490523-archiving-price-schedules.md` |
| Price Planner | Calendar tool to build price schedules | Early access; customer-type pricing only; schedule names cannot be edited | Yes | `md/49693334756251-introduction-to-price-planner.md` |
| Dynamic pricing | See summary items 1 and 2 | Time rules not supported on GetYourGuide/Viator; supported affiliates need percentage commission | Yes | `md/54312757536027-introduction-to-dynamic-pricing-2-0.md`, `md/40897564606875-using-price-schedules-with-dynamic-rules.md` |
| Custom fields | Text, checkbox, dropdown, quantity, transportation, code, code generator, waiver, label, date, email, gift card | Priceable: checkbox, dropdown, transportation, code | No | `md/40897381123611-custom-field-basics.md`, `md/40897451668251-setting-up-custom-fields.md` |
| Whole-booking field groups | One group per availability; duplicable | Only one group at a time | No | `md/40897421411611-custom-field-groups.md`, `md/40897409092251-archiving-custom-field-groups.md` |
| Conditional fields | Show/hide on other answers | No conditions on label, transportation, waiver, multi-text fields | No | `md/40897381615515-conditional-custom-fields.md` |
| Required/visibility/private | Per price sheet; Require an answer, Hide on receipts, Hide when booking | Label and Waiver fields cannot be required | No | `md/40897422636315-how-do-i-make-a-custom-field-required.md`, `md/40897424450203-how-do-i-change-a-custom-field-s-visibility.md` |
| Default values | Field-level and item-level; item wins | Text, checkbox, dropdown, quantity, code generator | No | `md/40897439429275-setting-a-default-value-for-a-custom-field.md` |
| Adjustable pricing | Staff-entered price on a field (comps, damage, discounts) | Needs "Adjust custom field prices on bookings" | Opt-in | `md/40897408900379-using-custom-fields-with-adjustable-pricing.md` |
| Add fields to existing bookings | Post-booking add-ons | Cannot remove original fields | No | `md/40897408545307-adding-custom-fields-to-existing-bookings.md`, `md/40897221525403-adding-an-expense-or-discount-to-a-booking.md` |
| Archive/remove/delete fields | Archive preferred | Cannot delete if attached | No | `md/40897396875931-archiving-custom-fields.md`, `md/40897423198107-removing-and-deleting-custom-fields.md` |
| Custom field group library at company level | Optional | | Yes | `md/40897409092251-archiving-custom-field-groups.md` |
| Tax types and Multi-tax | Percentage or flat taxes in-line; per-component taxes | Multi-tax: no custom Final Price; not in invoices/API; negative fields miscalculate | Multi-tax and aggregate to in-line: Support | `md/40897895708827-tax-types.md`, `md/40897859797659-multi-tax.md`, `md/40897890578459-legacy-aggregate-tax-settings.md` |
| Item descriptions/notes/Markdown | Markdown in notes, descriptions, messages | No text colors/alignment | No | `md/40897899863195-using-markdown-in-fareharbor.md`, `md/40897506530843-tips-for-writing-item-descriptions.md` |
| Translations | Translate content, emails, canned messages; 22 UI languages; bulk CSV | Waivers not translatable; no in-house translation | Opt-in or Support | `md/40897347733659-translating-your-fareharbor-content-into-other-languages.md`, `md/51485877769883-update-translations-in-bulk.md` |
| SKUs/internal names | Staff-only labels in reports | | No | `md/40897769598747-skus-and-internal-names.md` |

### 2.3 Bookings and manifests

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Create booking | Contact optional; save card; partial payment; confirmation email | Walk-ups: skip name/email/phone (permission plus company setting) | Text opt-in checkbox may need Support | `md/40897195083163-creating-a-booking.md`, `md/40897223488027-creating-bookings-without-a-contact-name.md`, `md/40897286610331-creating-bookings-that-require-phone-or-email.md` |
| Booking actions | Add/remove customers, rebook, cancel, set check-in, add payment, hold card, refund, print | Add/remove creates a new booking; payment not auto-adjusted | No | `md/40897221207067-editing-bookings.md`, `md/40897232976923-adding-or-removing-customers-from-a-booking.md` |
| Rebooking | Single and bulk rebook | Bulk rebooking is opt-in; fails without capacity; no bulk cancel | Opt-in | `md/40897261404187-rebooking-a-customer.md` |
| Cancel booking | Refund and/or gift card, email | Online customer cancel needs Support | Online: yes | `md/42957504194715-canceling-bookings.md` |
| Online rebooking | Customer moves own booking | Not for affiliates, deposits, retail, promo/gift card payments | Yes | `md/40897213805723-online-rebooking.md` |
| Cancellation policies | Rules by timeframe and refund percent; affiliate policy overrides item policy | Creating policies disabled by default; 5-minute grace after booking | Yes | `md/40897768261019-cancellation-policies.md` |
| Orders and online cart | Multiple bookings, one payment; cart for customers | Same contact only | Yes | `md/40897554987419-creating-an-order.md`, `md/40897546559515-online-orders-and-shopping-cart.md`, `md/40897545554331-order-faqs.md`, `md/42957489681947-order-actions.md`, `md/40897556352027-managing-orders.md` |
| Expense/discount line items | Retroactive discounts, tips, retail, fix balance due | Needs "View/Create and edit line items" | Permissions via Support | `md/40897221525403-adding-an-expense-or-discount-to-a-booking.md`, `md/40897914302363-why-do-cancelled-or-refunded-bookings-show-a-balance-due.md` |
| Booking notes/comments | Internal; searchable | Never shown to customers | No | `md/40897194025755-booking-notes-and-comments.md` |
| Split customers/payments | Procedures | | No | `md/40897272980891-splitting-customers-on-a-booking.md`, `md/40897979338651-splitting-payment-on-a-booking.md` |
| Find booking | Name, ID, email, phone, item, last 4 of card | | No | `md/40897227291035-finding-a-booking.md` |
| Overbooking | Staff may overbook; online customers never | Guides cannot by default | No | `md/40897252927003-overbooking.md` |
| Manifest | Columns, filters, grouping, views (availability, item, bookings, transportation, resource), CSV, print; custom manifests as user defaults | Cannot resize columns | No | `md/40897541945115-manifest-overview.md`, `md/40897482570395-saving-custom-manifests.md` |
| Check-in | Checked in / No-show statuses, custom statuses, auto no-show | Feature must be enabled; no-shows get no follow-ups | Yes | `md/40897334261915-checking-in-customers.md`, `md/40897308837275-no-shows-and-follow-ups.md` |
| Multi-scan | Repeated scans per ticket (multi-ride) | Beta; no membership link, no reports | Yes (Account Mgmt) | `md/40897295075483-multi-scan.md` |
| Private events | See summary item 11 | Stripe only; no automated payments | Yes | `md/40897258328091-configuring-private-events.md`, `md/40897271923227-scheduling-a-private-event.md`, `md/40897268694043-private-events-best-practices.md`, `md/40897270589467-reporting-on-private-events.md`, `md/40897300430619-setting-up-a-private-event.md` |
| Crew | Assign users with roles, crew notifications, visibility limits | Updater adds do not trigger crew notifications | Permission edits via Support | `md/40897187422235-adding-and-removing-crew.md`, `md/40897407029147-adding-assigning-and-removing-roles.md`, `md/40897393741083-crew-notifications.md`, `md/40897416956187-editing-crew-visibility.md` |
| Assistant (AI in Dashboard) | Plain-language questions, creates bookings/gift cards, changes status, asks to confirm | Limited to the user's permissions | No | `md/53765984682651-introduction-to-assistant.md` |
| Keyboard shortcuts | Shift+? lists them | | No | `md/40897718767259-keyboard-shortcuts.md` |
| Files on bookings | Not allowed; PII uploads blocked from 2026-09-30 | Existing PII files deleted after June 2027 | n/a | `md/40897899237915-can-files-be-uploaded-to-customer-bookings.md`, `md/54407505162139-uploading-files-containing-personal-identifiable-information-pii.md` |

### 2.4 Customers and CRM-style features

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Customer directory | Profiles, booking/membership/waiver history, lifetime value, tags, auto "Returning" tag, notes | Once enabled; no CSV export, merges or booking from profile yet | Rollout-gated | `md/42957456905883-customer-directory.md` |
| Booking-form autofill | Suggests directory profiles | Default on; Advanced company settings > Bookings | Opt-out | `md/42957456905883-customer-directory.md` |
| Contacts report | Names, emails, phones, opt-in flag, zip, language | Anti-spam rules apply | No | `md/40898088413595-contacts-report.md` |
| Customers report | Customer types plus check-in data (from 2021-02-10) | | No | `md/40898088723227-customers-report.md` |
| Subscribe to email list | Checkbox on booking creates opt-in for the Contacts report | | No | `md/40897195083163-creating-a-booking.md` |
| Integrations for CRM/email | HubSpot, Mailchimp, Podium, Yonder, TourAdvantage (Drip) | See 2.12 | Mostly | `md/43687134994715-hubspot-integration.md`, `md/43770566859035-integrating-mailchimp.md` |
| Email workaround across dates | FH cannot email across date ranges; export contacts to your email tool | | n/a | `md/40897386906395-emailing-customers.md` |

### 2.5 Campaigns, promo codes, gift cards, memberships, combos

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Discount Codes (new) | Percent or fixed, item or customer-type level, redemption window, limits, affiliate options | See section 3 | Yes | `md/50078996211483-introduction-to-discount-codes.md`, `md/50079733016859-create-manage-discount-codes.md`, `md/50118840777883-reference-discount-code-settings.md` |
| Campaigns (classic) | Imported or random codes through a Campaign code custom field; supports vouchers, gift certificates | See section 3 | Yes | `md/40897288495515-creating-campaigns-and-promo-codes.md` |
| OTA discounts | Percent discounts auto-synced to Viator | Viator only | Yes | `md/45501481631899-how-to-create-an-ota-discount.md`, `md/45535305591451-how-to-create-an-ota-discount.md`, `md/51495663149083-viator-special-offers.md` |
| Groupon/Travelzoo vouchers | Voucher codes as a campaign | | Yes | `md/40897305203355-using-groupon-travelzoo-or-livingsocial-with-fareharbor.md` |
| Campaign reporting | Campaigns report, Custom Field Answers, Expenses and Discounts | Deleted campaigns still in reports | No | `md/40897317690779-tracking-and-analyzing-campaigns.md`, `md/40898061587995-campaigns-report.md` |
| Gift cards | Sold online and in Dashboard, expiration by type, designs, bulk import, resend | 10,000 local currency online cap; cannot restrict to certain items | Setup form | `md/40897462601755-gift-card-faqs.md`, `md/40897463478555-gift-card-overview.md`, `md/40897458166683-managing-gift-cards.md`, `md/40897476361499-redeeming-a-gift-card.md` |
| Gift card as credit | Cancel with gift card; issue from booking; rebook to gift-card item | Gift card shortfall removes the booking fee | Gift-card item: Support | `md/40897504237851-giving-credit-using-gift-cards.md` |
| Memberships | Duration or date-range, benefits, punchcards, overlapping, sub-members (25 max), auto-renew, import/export | Members must use same email; customers cannot self-cancel | Yes (each add-on separately) | `md/40897569765275-introductions-to-memberships.md`, `md/40897569988507-creating-memberships.md`, `md/40897543220635-overlapping-memberships.md`, `md/50957273883163-manage-sub-members-on-memberships.md`, `md/40897543047835-managing-and-viewing-members.md`, `md/42957494045595-purchasing-using-and-renewing-memberships.md` |
| Combos | Two items only, opener plus upsell, discounts, seasonal rates | Online only; not carried over on rebooking; no affiliates/ASN | Opt-in | `md/42957728899611-setting-up-combos.md`, `md/42957726827675-combo-discounts.md`, `md/40897840776731-introduction-to-combos.md` |
| Packaged combos | Shown at start of flow with streamlined checkout | Same-day rules and embedded-calendar display unavailable | Opt-in | `md/42957744220443-packaged-combos.md` |
| Cross-Sell Combos | Partner items in upsell; supplier-set discount | Stripe both sides; online only; not in Dock; no mediation | Yes | `md/42957735775643-cross-sell-combos.md` |
| Suggested items | Upsell in cart/confirmation | First three flow items in the email | Yes | `md/40897852857755-suggested-items.md` |
| Dynamic pricing / Price Planner | See 2.2 | | | |

### 2.6 Email, SMS, notifications, waivers

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Confirmation/cancellation notes | Company, item, headline levels | Item notes above company notes | No | `md/40897393367963-updating-confirmation-notes.md`, `md/40897348918171-updating-your-cancellation-notes.md` |
| Canned messages | Reusable email/text content | Text 130 chars | No | `md/40897372816795-canned-messages.md` |
| Automatic reminders/follow-ups | Per item, email and text | Section 4 | Texting needs enabling | `md/40897385230363-automatic-reminders-and-follow-ups.md` |
| Texting | Single or bulk from availability; opted-in only; send-only | 130 characters | Yes | `md/40897348692763-texting-customers.md` |
| Email customers | Single or bulk; Markdown; status columns | No range-of-dates blasts | No | `md/40897386906395-emailing-customers.md`, `md/40897392303515-previewing-customer-emails.md` |
| Default email checkboxes | Send confirmation/rebooked/cancellation by default | | Opt-in | `md/40897362574619-updating-default-email-settings.md` |
| Health and safety policy | Company and item level | | No | `md/40897346962331-managing-health-safety-policies.md` |
| Social/survey URLs | Google review link, survey button with booking parameters | | No | `md/40897349493531-social-media-and-survey-urls.md` |
| Staff notifications | Email/push for bookings, cancellations, manifests, crew, disputes, bounces, bank changes | No SMS to staff | No | `md/42957499257627-subscribing-to-user-notifications.md`, `md/40897725265307-unsubscribing-from-user-email-notifications.md` |
| FareHarbor Waivers | See section 4 | 300 signers/booking | Opt-in | `md/40897871757339-fareharbor-waivers.md`, `md/54050261537563-waiver-links.md` |
| Smartwaiver / Wherewolf | Third-party waivers | Cannot run with FH Waivers | Yes | `md/40898257549211-smartwaiver-integration.md`, `md/40898258345883-wherewolf-integration.md` |
| FareHarbor Agent | AI agent across web chat, Lightframe, FB/IG, WhatsApp, SMS, phone, email | Selected clients only; powered by OpenCX | Yes | `md/48858951282075-introduction-to-fareharbor-agent.md`, `md/48859367837083-fareharbor-agent-frequently-asked-questions.md`, `md/48859121544731-how-to-set-up-fareharbor-agent.md`, `md/54008273297307-fareharbor-agent-how-to-connect-communication-channels.md`, `md/54013483763611-fareharbor-agent-how-to-configure-handoff-settings.md`, `md/48859348921115-how-to-work-with-bookings-in-fareharbor-agent.md`, `md/48859223037467-how-to-manage-guest-conversations-in-fareharbor-agent.md`, `md/54015610972827-fareharbor-agent-tips-tricks-on-how-to-get-bookings.md`, `md/48858992768155-how-to-access-the-fareharbor-agent-workspace.md` |
| Tripadvisor Review Express | Follow-up review requests; cancelled and all-no-show bookings excluded | | Support | `md/40897375707931-locations.md`, `md/42957504194715-canceling-bookings.md` |
| Receipts/tickets | Footer text, tip line, Boca tickets, receipt printers | Party under 10 listed individually by default | Boca and receipt printing: Support | `md/40897618955547-customizing-receipts.md`, `md/40897618602651-customizing-boca-tickets.md`, `md/42957496986139-setting-up-your-boca-ticket-printer.md`, `md/40897607766043-printing-receipts.md`, `md/40897578529179-printing-receipts-and-tickets.md`, `md/40897591879451-setting-up-your-receipt-printer.md`, `md/40897566157979-ticket-faqs-and-troubleshooting.md`, `md/40897596060955-bluetooth-receipt-printing-with-the-fareharbor-app.md` |

### 2.7 Payments, deposits, invoices, Stripe, Affirm

Affirm is not mentioned anywhere in the 654 articles. Buy-now-pay-later in the help center is Afterpay only.

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Payment Setup Checklist | Required before cards or payouts; 2SV and "Manage bank accounts" needed | 7-day wait before first payout eligibility on new bank | No | `md/40897891290907-introduction-to-the-payment-setup-checklist.md`, `md/40897866719003-payment-setup-checklist-for-us-bank-accounts.md`, `md/40897894382747-updating-the-payment-setup-checklist.md` |
| Processors | Stripe default; PayPal; dLocal (TH, ZA, CR) | Do not click "Save for Later" in reverification | PayPal: Support | `md/40897875964827-payment-setup-checklist-for-paypal.md`, `md/42957746512155-payment-setup-checklist-for-dlocal.md` |
| Booking fee | 6% on direct bookings for businesses under $35,000 online direct volume | Applies to Dashboard, Dock, payment links; reviewed each Oct 1 | n/a | `md/40897900687771-october-2024-booking-fee-adjustment.md` |
| Processing rate | Tiered by annual online volume | Past payments keep old rate | n/a | `md/40897934927131-processing-rate-adjustments.md` |
| Deposits | Per booking or per participant | Not for private items; gift cards cannot apply to deposit items | Yes | `md/40898010428315-deposits.md` |
| Partial payments / splitting | Dashboard only | FH advises against online partial | Support for online | `md/40897977378971-collecting-partial-payments.md` |
| Payment links | Balance payment from confirmation page | Full balance only from 2026-09-10; expires 7 days after the activity | Yes | `md/42957750164379-using-payment-links-for-underpaid-bookings.md` |
| Authorization holds | Hold up to 7 days (Visa 5) | Cannot be disputed until captured | No | `md/40897980634523-credit-card-authorization-holds.md` |
| Saved cards | Dashboard users only; cannot be removed | | No | `md/40898022765979-saving-a-card-to-charge-later.md` |
| Wallets/local methods | Apple Pay, Google Pay, Link (instant bank US), Afterpay, Alipay, WeChat Pay, Bancontact, Bizum, iDEAL, MB WAY, Satispay, Vipps | Afterpay $1 to about $2,000; Stripe only | Most need Support | `md/42957748495131-using-apple-pay-and-google-pay-for-online-payments.md`, `md/40897959062171-link-by-stripe.md`, `md/42957731295387-afterpay.md`, `md/42957739195931-alipay.md`, `md/42957764771739-wechat-pay.md`, `md/40897958631835-bancontact.md`, `md/54101810137243-bizum.md`, `md/40897963921691-ideal.md`, `md/44019004669979-mb-way.md`, `md/40897975056027-satispay.md`, `md/42957716870427-vipps.md` |
| Security | 3DS, AVS, Radar, enhanced controls | AVS lifts conversion with cart, hurts without | Enhanced protections: Support | `md/40897979448091-3d-secure-authentication.md`, `md/43436153392667-address-verification-system-avs.md`, `md/57089084352667-fraud-prevention-payment-security-best-practices.md` |
| Disputes | Accept or fight; evidence packet 16 pages | Auto-fights if no reply | No | `md/40898039424411-dispute-faqs.md`, `md/40898039858843-dispute-reasons-and-what-to-do.md`, `md/40898034083611-refunding-a-disputed-charge.md`, `md/40898023469083-tips-for-preventing-disputes.md`, `md/40898039491867-paypal-disputes-overview.md` |
| Refunds | Full free; partial keeps booking fee; reserve first | Cannot refund outside-FH payments | No | `md/40898026879387-refunding-a-customer.md`, `md/40898002492443-credit-card-refund-faqs.md`, `md/40898026206363-custom-refunds.md`, `md/40898002050971-checking-the-status-of-a-credit-card-refund.md` |
| Refund Reserve | Recurring transfer option | Non-US banks keep it funded | Opt-in | `md/40898037215259-managing-your-refund-reserve.md` |
| Payouts | Daily/weekly/monthly; rolling window | Payout-after-availability-ends | Window/accrual: Support | `md/40898001686043-payouts.md` |
| Ledgers | Different banks per item/availability | Cannot be disabled; no per-ledger 1099-K | Yes | `md/40898000845851-ledgers.md` |
| Bank accounts and debits | Reorder, primary; ACH debits for shortfalls | Debits US only; Wise/Payoneer fail | No | `md/42957769732635-adding-or-changing-a-bank-account.md`, `md/40898018334491-bank-debits.md`, `md/40898018537371-wise-fareharbor.md` |
| Stripe Capital | Financing offers | Invitation only, US | No | `md/56930177957659-getting-financing-with-stripe-capital.md` |
| Payment types, tax IDs, statement text | Custom payment types; statement 18 chars | Tax ID cannot be edited in Dashboard | Statement text: Support | `md/40897877617563-setting-up-payment-types.md`, `md/40897979411483-tax-ids.md`, `md/40897980786843-what-is-my-card-statement-text.md`, `md/45255013469595-updating-your-business-information.md`, `md/40898031697563-customer-bank-statements-faqs.md`, `md/40898021403675-charging-credit-cards.md`, `md/40898039255707-what-credit-cards-does-fareharbor-accept.md` |
| 1099-K | Will not match FH reports | API bookings not on it | n/a | `md/42957746733083-frequently-asked-questions-about-the-1099-k-form.md` |
| Affiliate invoices/DACH invoices | Operator-generated | DACH: past, fully paid direct bookings without booking fee | Support for enablement | `md/42957548712347-getting-started-with-invoicing.md`, `md/42957740853787-generating-invoices-for-dach-customers.md` |
| Company cards | Share a saved card with partners | Stored at Stripe | No | `md/42957745568923-company-cards.md` |

### 2.8 Affiliates, Distribution Hub, OTAs, Google, ChatGPT

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| New affiliate setup | Adds affiliates, pricing, commission | 3 to 5 business days | Yes | `md/40898119322395-new-affiliate-request.md`, `md/42957513918363-affiliate-dashboard.md`, `md/42957515150747-affiliate-tagging.md` |
| Booking methods | Widgets, promo code, QR, API, affiliate dashboard | No tiered commissions; commissions not auto-paid | Widgets/promo/QR: yes | `md/42957577429019-affiliate-booking-methods.md`, `md/40898084853403-affiliate-book-buttons-qr-codes.md`, `md/42957562974747-affiliate-promo-codes.md` |
| Payment relationships | Billing, Referral, Referral deposit, Net rate, Skip payment | Some Dashboard-only | n/a | `md/45526491915163-deciding-how-your-affiliates-get-paid.md`, `md/42957573653019-payment-options-for-affiliates.md` |
| Affiliate rules | Limit items/times/capacity for affiliates and OTAs | Applies to whole item; no rule reporting | No | `md/40898100610715-affiliate-rules.md` |
| Affiliate blocks | Reserve seats for one affiliate with auto-release | Not with resources | No | `md/46302229002779-affiliate-blocks.md` |
| Settings groups, categories | Reusable bundles; labels for reports | FHDN/major OTA configs central | Partly | `md/56018604663195-affiliate-settings-groups.md`, `md/56014078344091-affiliate-categories.md` |
| Rates check | Verify price sheets | | Updates via channel support | `md/42957547822875-checking-your-affiliate-rates.md` |
| Invoicing and payouts | Create, email, mark paid, settle by card or US bank debit | Invoices cannot be edited after creation | No | `md/42957548712347-getting-started-with-invoicing.md`, `md/51217770218395-managing-affiliate-invoice-payments.md` |
| Agents and desks | Concierge tracking | | No | `md/40898140534299-managing-affiliate-agents.md` |
| FHDN | Network resale | Needs Stripe; 20%/25%; 30 days notice to leave; 5th/10th business day commission | Opt-in via form; leaving: Support | `md/42957709413403-fareharbor-distribution-network-fhdn-overview.md`, `md/45613243359643-distribution-partnership-types.md`, `md/45613007969947-working-with-affiliates.md`, `md/42957693991963-fhdn-reports-accounting.md`, `md/42957682382619-fareharbor-distribution-network-fhdn-opt-out-request.md` |
| FHDN API payouts | New payout account due end of Sept 2026 | Otherwise payouts stay Pending | No | `md/54515340128923-setting-up-fhdn-api-payouts.md` |
| Marketplace quality score | Photos, description, 30+ future availabilities, reviews | Max 3 tags | Ratings: Support | `md/40898234979995-how-to-improve-your-fareharbor-marketplace-item-quality-score.md`, `md/42957706861851-fareharbor-marketplace-for-affiliates.md` |
| Guide to partnering | Cross-sell, FHDN, direct | | Yes | `md/42957682208283-guide-to-partnering-and-reselling-with-other-fareharbor-clients.md` |
| OTA connectivity | Viator, Airbnb, Booking.com, Expedia, Google, GetYourGuide, many more | Customer type changes break connections; API fee 2% | Connectivity form | `md/53778629402651-working-with-external-apis.md`, `md/46620607425819-working-with-viator.md`, `md/40898086122395-working-with-airbnb-experiences.md`, `md/42957706509595-working-with-booking-com.md`, `md/42957656201627-api-partner-directory.md`, `md/42957604700827-api-fee-invoice-process.md` |
| Google Things to Do | See summary item 14 | 10 activities per Business Profile | Yes | `md/40898232783003-google-things-to-do-integration.md`, `md/40898233093275-optimizing-for-google-my-business.md` |
| FareHarbor in ChatGPT | FHDN items in ChatGPT; ref=openai-widget | Retail and gift cards ineligible; no ranking control | Opt-out = opt out of FHDN | `md/47076472962459-fareharbor-in-chatgpt.md` |
| Affiliate-side tools | Affiliate dashboard, reports, notifications | | | `md/42957617442459-affiliate-dashboard-faq.md`, `md/42957579351579-affiliate-dashboard-tools.md`, `md/42957581849499-reports-for-affiliates.md`, `md/48866544114971-affiliate-booking-notifications.md`, `md/42957572556443-getting-started-as-an-affiliate.md`, `md/42957556694811-fareharbor-distribution-network-fhdn-for-affiliates.md`, `md/43387026547355-fareharbor-marketplace-for-affiliates.md`, `md/51226757445531-invoice-payments-and-payouts-for-affiliates.md`, `md/42957621111067-invoicing-for-affiliates.md`, `md/42957573653019-payment-options-for-affiliates.md` |
| Hub overview | | | | `md/43685777785115-what-is-the-distribution-hub.md` |
| GetMyBoat | Connection paused | | | `md/42957656201627-api-partner-directory.md` |
| Other listings | TourConnect, Dazhboards, Sojern, Tomis, web chat partners | | Partner-specific | `md/40898245848091-tourconnect-integration.md`, `md/54893080554779-dazhboards-integration.md`, `md/40898259138331-sojern-digital-marketing-partnership.md`, `md/40898259804315-tomis-partnership.md`, `md/40898229581979-web-chat-best-practices-and-recommendations.md`, `md/40898256647835-mypasstracker.md` |

### 2.9 Website, book buttons, embeds, Lightframe, SEO

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Embed generator | Book button/link, embedded calendar, grid, enclosed checkout; Online ref tag | Online ref strongly recommended; calendar stylesheet not customizable | No | `md/40898512663451-adding-fareharbor-links-and-embeds-to-your-website.md` |
| Lightframe | Overlay checkout; auto-lightframe script before `</body>` | Not on Google Sites/Canva; Wix and GoDaddy embeds cannot lightframe | Free install on request | `md/40898469746075-lightframe-overview.md`, `md/40898501624731-advanced-lightframe-api-usage.md`, `md/40898498425115-website-cheatsheet.md` |
| Lightframe cosmetics | Dark mode, background image, brand colors, cancellation badges | Brand colors and background image are beta; badges via Support | Partly | `md/40898456312475-configuring-dark-mode-for-online-booking.md`, `md/40898519837979-adding-a-background-image-for-the-lightframe.md`, `md/40898514584091-brand-appearance.md` |
| Buttons stylesheet | Styled and fixed floating buttons | | No | `md/40898487556763-fareharbor-buttons-stylesheet.md`, `md/40898489020571-using-the-fareharbor-buttons-stylesheet-with-wordpress.md` |
| WordPress plugin | Shortcodes, auto-lightframe, hooks | Plugin v3.1+ for auto lightframe | No | `md/42957853992987-wordpress-plugin.md`, `md/40898473465883-wordpress-plugin-hooks.md` |
| Custom embed generator | Multi-dashboard panel grid | | No | `md/40898520358939-fareharbor-custom-embed-generator.md` |
| Instagram book link, Facebook CTA | Link-type URL for ads; Facebook disabled custom Book Now links | Use Learn More, Shop Now, etc. | Link on request | `md/40898451866011-adding-book-banners-to-instagram-posts.md`, `md/40898439737627-connecting-your-facebook-page-with-fareharbor.md` |
| Kiosk legacy | Locked tablet booking URL | Replaced by Dock | Yes | `md/40898504527003-kiosk-mode-legacy-feature.md` |
| FareHarbor Sites | Managed WordPress VIP site; pages, activities, rows/blocks, forms, cards, blog, Complianz | About 4 week build; 30 days notice to leave; template not transferable | Yes | `md/41245673579035-fareharbor-sites.md`, `md/42957824488091-fareharbor-site-onboarding-timeline.md`, `md/41240383426971-fareharbor-sites-faqs.md`, `md/41245664325787-leaving-your-fareharbor-site.md`, `md/41243260002587-rows-and-blocks.md`, `md/41244291720859-activity-settings.md`, `md/41244259013403-company-settings.md`, `md/41245580245915-what-is-wordpress-vip.md`, `md/41245516819739-ensuring-security-on-wordpress-vip.md` |
| Sites activity management | Add, remove, price, event, timed activities | Do not Publish early; remove = Call to Book/Draft/Trash | Support for imports | `md/41243394141211-how-do-i-add-a-tour-or-activity-to-my-fareharbor-site.md`, `md/41243448784283-how-do-i-remove-an-activity-from-my-fareharbor-website.md`, `md/41243467538075-how-do-i-set-up-an-activity-that-is-an-event.md`, `md/41243927775771-timed-activities.md`, `md/41243509485467-how-do-i-update-a-price-for-an-activity-page-or-item.md`, `md/41243649504539-how-do-i-update-an-activity-page-description.md`, `md/41243819703835-how-do-i-update-the-tags-for-an-activity-block.md`, `md/41243967426971-what-is-an-activity-page.md`, `md/41243978300187-cards.md` |
| Price Sync | Daily one-way sync of Dashboard prices to site | No strikethrough, multi-item, dynamic pricing | Admin toggle | `md/42957794771995-price-sync.md`, `md/41243341791387-fareharbor-sites-activity-pricing-overview.md` |
| Sites content tools | Banner, logo, menu, footer, media, sidebar, testimonials, forms, Instagram feed, redirects, permalinks | Media 10MB; videos YouTube/Vimeo only | No | `md/41245042923035-how-do-i-change-add-a-promotional-banner.md`, `md/41245371728923-how-do-i-update-my-logo-site-icon.md`, `md/41240598410139-how-do-i-update-my-menu-bar-tabs.md`, `md/41240557317531-how-do-i-update-my-fareharbor-website-footer.md`, `md/41244079904027-media.md`, `md/41243894587035-sidebar.md`, `md/41244009935003-testimonials.md`, `md/41244135414299-forms.md`, `md/41244936403739-how-do-i-add-an-instagram-feed-to-my-fareharbor-site.md`, `md/41244765492891-setting-up-redirects-on-your-fareharbor-site.md`, `md/41244726737691-permalinks.md`, `md/41243978300187-cards.md`, `md/41244313757979-blog-settings.md` |
| Sites admin | Users, 2FA, login, mobile and device content, general settings | 2FA mandatory | Access issues: Support | `md/41245391981723-how-do-i-invite-a-new-user.md`, `md/41245460938907-wordpress-user-permissions-for-updating-fareharbor-sites.md`, `md/55660566997147-using-your-client-user-account-on-fareharbor-sites.md`, `md/41244664684955-set-up-two-factor-authentication-2fa-in-wordpress.md`, `md/41240536619035-how-do-i-login-to-my-website.md`, `md/41240279984667-device-specific-content.md`, `md/41244400952091-mobile-settings.md`, `md/41244139584667-general-settings.md`, `md/41243150326939-adding-and-editing-pages.md`, `md/43525323077403-auto-generated-pages.md`, `md/41240497422875-how-do-i-change-a-picture-update-my-media.md`, `md/41240632689179-website-training-videos.md`, `md/43487481174811-sending-site-contributor-invites-to-fareharbor.md` |
| Sites SEO and domains | SEO FAQ, Tech Audit, go-live | Sitemap regenerates up to 1 month; linking straight to flows hurts SEO | Pre-sweep via Support | `md/52856871265051-seo-faqs.md`, `md/52966871885851-tech-audit-101.md`, `md/41240033843355-finding-your-domain-registrar.md`, `md/41240097377435-going-live-what-to-expect.md`, `md/41240205135515-what-is-a-domain-registrar-url-cms.md`, `md/42957776003355-complianz-activation-and-configuration.md` |
| Affiliate activity on Sites | Resell other operators' items | | Support | `md/41240460210971-how-do-i-add-an-affiliate-activity-to-my-fareharbor-website.md` |
| Best practice | Book button on every page, mobile fixed button | | No | `md/42957863615131-best-practice-for-website-integration.md` |
| Cookie consent | Supported CMPs only | OneTrust, Complianz, Cookiebot, iubenda, Consent Mode v2 | No | `md/42957738437659-cookies-under-privacy-laws.md` |
| Accessibility | WCAG 2.1 AA target | | Ticket for FH sites | `md/40897739668763-accessibility.md` |

### 2.10 Reporting, analytics, exports

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Reports structure | Performance, Operations, Customers and marketing, Accounting | Per-group permissions | No | `md/40898104978587-introduction-to-reporting.md`, `md/40898092549403-report-types-overview.md` |
| Advanced report engine | Date types, filters, groupings, saved reports, share links | Standardized CSV format coming | No | `md/40898075231131-advanced-reports-overview.md`, `md/40898077265179-advanced-report-settings.md`, `md/40898044848283-general-report-options.md`, `md/40898075692187-saving-a-report.md`, `md/40898057430939-important-terms.md`, `md/49511039883931-glossary-of-report-columns.md` |
| Sales and revenue | Daily/monthly sales, Revenue by Type, Payouts and refunds, Reconciliation | Revenue by Type "collected" is the click date, not deposit date | No | `md/40898080768155-sales-reports.md`, `md/48194277955995-daily-and-monthly-sales-reports.md`, `md/40898095662875-revenue-by-type-report.md`, `md/40898080138139-payouts-and-refunds-report.md`, `md/40898029021979-using-reports-to-answer-common-questions.md` |
| Booking reports | Bookings, daily/monthly, Booking source, Booking details | Report on availability vs booking date | No | `md/40898072248987-bookings-reports.md`, `md/51862042421019-daily-monthly-bookings-report.md`, `md/40898028173851-booking-source-report.md` |
| Pace report | Pace vs last year | Not forecast; excludes cancelled | Advanced Reports permission | `md/48197997852443-introduction-to-the-pace-report.md` |
| Item occupancy | Occupancy per availability | No CSV; tracking began April 2026 | No | `md/51274856853659-item-occupancy-report.md` |
| Insights and opportunities | Recommendations (add photos, availability) | Not predictive | View reports | `md/44922963169819-insights-opportunities.md` |
| Affiliate reports | Affiliate bookings, categories | | No | `md/56293946497051-affiliate-bookings-report.md` |
| Custom Field Answers, Campaigns, Gift cards, Benefit uses, Resource uses, Expenses and discounts, Disputes | Specialty reports | Custom Field Answers needs at least one field filter | No | `md/40898062225947-custom-field-answers-report.md`, `md/40898061587995-campaigns-report.md`, `md/40898062343835-gift-cards-report.md`, `md/40898050743323-benefit-uses-report.md`, `md/40898052038683-resource-uses-report.md`, `md/40898113325595-expenses-and-discounts-report.md`, `md/40898067199259-credit-card-disputes-report.md` |
| Monthly tax breakdown | Tax by type CSV | From 2026-04-01 only | No | `md/42957770551707-monthly-tax-breakdown.md` |
| FareHarbor Invoices | Combined FH fee invoices | Pre-2026-06-30 data not migrated | No | `md/52047290432155-fareharbor-invoices-report.md`, `md/42957785927835-payment-processing-documents-report.md` |
| Multi-dashboard reports | Run across companies | Owner/Director on each | Setup via Support | `md/40898057916955-running-reports-across-multiple-dashboards.md` |
| Contacts and Customers reports | See 2.4 | | | `md/40898088413595-contacts-report.md` |
| Legacy reports | Pre-2017 | Use advanced instead | No | `md/40898077874459-introduction-to-legacy-reports.md`, `md/40898111199771-custom-field-use-report.md`, `md/40898093280027-detailed-bookings-report.md` |
| GA4 | Native events and funnels | See 2.12 | Setup via Support | `md/49913901254555-google-analytics-integration-setup-guide.md`, `md/49913718416027-analyze-user-behavior-with-fareharbor-conversion-funnels.md`, `md/49913713874459-setting-up-a-conversion-funnel-by-item-or-flow-id.md`, `md/42957829280923-how-to-gain-visibility-inside-the-lightframe-with-a-conversion-funnel.md`, `md/44277654773403-build-your-audience-using-fareharbor-ga4-events.md`, `md/40898463183771-introduction-to-google-analytics-4-ga4-reports.md`, `md/40898491759003-why-don-t-my-google-analytics-and-fareharbor-reports-match.md` |
| Downloads | CSV, print | Slow downloads: alt-click, Chrome | No | `md/40897898334619-how-do-i-download-a-manifest-or-report.md` |

### 2.11 Users, permissions, multi-company

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Users | Add, edit, deactivate, delete; email login mandatory since 2026-05-18 | Email must be verified | No | `md/40897695502363-adding-and-editing-users.md`, `md/40897736568091-deactivating-users.md`, `md/40897712400923-deleting-users.md`, `md/47912505950619-introduction-to-email-login-in-fareharbor.md`, `md/40897740097691-logging-into-your-dashboard.md`, `md/40897700687643-logging-out-of-your-dashboard.md` |
| Permission groups | Directors, Managers, Payments Setup, Reservationists, Guides; custom groups | Create/edit disabled for everyone by default | Yes | `md/40897699291803-permission-groups.md`, `md/40897729012507-managing-permission-groups.md` |
| Outside users | Staff from another Dashboard | Director outside users cannot do checklist tasks | Yes | `md/40897730655899-outside-users.md` |
| 2-step verification | Required each login; no authenticator apps | Session 14 days | Opt-out via Support | `md/40897681313563-2-step-verification.md` |
| Passwords | 8+ chars; force logout | | No | `md/40897722167451-changing-or-resetting-passwords.md` |
| Notifications | See 2.6 | | | `md/42957499257627-subscribing-to-user-notifications.md` |
| Webhook/API users | Integration user with plus-address | | | `md/40897695502363-adding-and-editing-users.md` |
| Help Center login, status page | Shortname login; status.fareharbor.com | | No | `md/43227119961755-viewing-fareharbor-help-center-pages.md`, `md/40897954897691-subscribing-to-fareharbor-status-updates.md` |

### 2.12 Integrations, Zapier, External API, webhooks

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Webhooks | Real-time POST on booking create/update/cancel; item changes | HTTPS only; 3 retries 60s apart; no gift card or promo visibility | Tab may need Support | `md/40898249392539-introduction-to-webhooks.md`, `md/40898279460763-configuring-webhooks.md`, `md/40898294427291-using-webhooks.md` |
| Zapier | One-way FH to Zapier, 3 triggers | Key from Your Account > API Keys | No | `md/40898281485339-introduction-to-the-zapier-integration.md`, `md/40898298749211-creating-paid-orders-in-square-from-fareharbor-retail-item-bookings.md`, `md/40898312964251-managing-inventory-in-square-for-fareharbor-retail-items.md` |
| External API for OTAs | Partner builds against FH | Section 5 | Yes | `md/53778629402651-working-with-external-apis.md` |
| GA4 integration | Events view_item_grid to purchase | Multi-site checkbox; multi-dashboard needs custom dimension | Add GA user via Support | `md/42957815081883-setting-up-google-analytics-4-ga4-to-work-with-fareharbor.md`, `md/49910563968539-configuring-your-ga4-property-for-multiple-fareharbor-dashboards.md`, `md/49910540745883-google-analytics-4-ga4-frequently-asked-questions.md`, `md/42957836698779-how-to-create-a-new-google-analytics-ga4-property.md`, `md/42957830296475-tracking-conversions-in-google-ads-using-ga4.md`, `md/40898437368603-analytics-integrations-overview.md` |
| Meta Conversions API | Server-side Purchase event | One pixel per Dashboard | EU: Support | `md/42957825564827-tracking-conversions-with-the-meta-facebook-pixel.md` |
| Custom pixels | TikTok, Ads, others | Admin-only, via Support; no thank-you page | Yes | `md/40898437450523-custom-conversion-pixel-tracking-capabilities.md` |
| Accounting | QuickBooks Online (US), Xero, Kapta | No tax values, customer type or discounts sync | Opt-in | `md/42957793242395-quickbooks-online-integration.md`, `md/42957823210779-integrating-xero.md`, `md/46743985096347-kapta-automated-invoicing.md` |
| CRM/marketing | HubSpot, Mailchimp, Podium, Yonder, TourAdvantage | New bookings only | Opt-in/Support | `md/43687134994715-hubspot-integration.md`, `md/43770566859035-integrating-mailchimp.md`, `md/40898230385947-podium-integration.md`, `md/40898247304859-yonder-integration.md`, `md/40898276178971-touradvantage-integration.md` |
| POS and retail | Square, Lightspeed, Factor4 gift cards | Square: no promo, memberships, combos, gift cards | Opt-in | `md/40898264452123-creating-a-square-integration.md`, `md/44233609322523-integrating-lightspeed.md`, `md/55342056679835-factor4-integration.md` |
| Photos | Fotaflo, PicThrive | | Yes | `md/40898227720091-fotaflo-integration.md`, `md/40898188389787-picthrive-integration.md` |
| Insurance/protection | Buoy (FL boat rental), vQuip (US), TourClaim | | Yes | `md/40898261087387-integrating-buoy.md`, `md/40898187685659-vquip-integration.md`, `md/47787190349723-tourclaim-integration.md` |
| Passes and scheduling | CityPASS, Go City, Papershift, Buzzshot | | Yes | `md/42957773599899-integrating-citypass.md`, `md/42957822059547-integrating-go-city.md`, `md/40898260715675-papershift-integration.md`, `md/40898244499483-buzzshot-escape-room-software-integration.md` |
| Marketing intro, partner categories | Stubs | | | `md/40898244581915-introduction-to-marketing-communications.md` |

### 2.13 Mobile app, check-in, POS (Dock)

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| FareHarbor app | iOS 13+/Android 8+, biometrics, push | Biometrics not for shared devices | No | `md/40897805141659-using-the-fareharbor-app-on-ios-devices.md`, `md/40897761048603-using-the-fareharbor-app-on-android-devices.md` |
| QR ticket scanning | Per-item enable; per-device check-in status; customer-type limits (iOS); offline mode | Customer-type scanning iOS only; status mode needs offline off; Android scan needs internet | Opt-in; wallet passes beta | `md/40897298271899-introduction-to-setting-up-and-scanning-qr-codes.md`, `md/40897298891547-scanning-qr-codes-for-default-check-in-status.md`, `md/40897352809115-scanning-qr-codes-for-specific-customer-types.md`, `md/40897343183259-scanning-qr-codes-with-the-fareharbor-android-app.md`, `md/40897344149659-scanning-qr-codes-with-the-fareharbor-ios-app.md`, `md/40897319874843-scanning-qr-codes-offline-using-the-fareharbor-android-app.md`, `md/40897336553499-scanning-qr-codes-offline-using-the-fareharbor-ios-app.md`, `md/40897340595867-using-handheld-qr-code-scanners-with-the-fareharbor-app.md`, `md/40897310315675-scanning-qr-codes-for-check-in-on-your-mobile-device.md` |
| Dock (POS) | Staff and Kiosk modes, retail view, tips, Tap to Pay, QR payments, seat assignment | Fee per transaction; no memberships, combos, booking flows, Smartwaiver | Yes (Account Mgmt) | `md/42957713960987-introduction-to-fareharbor-dock.md`, `md/42957683348507-setting-up-the-fareharbor-dock-application.md`, `md/42957745935003-configuring-fareharbor-dock.md`, `md/40897751168539-fareharbor-dock-staff-mode.md`, `md/40897774194459-fareharbor-dock-kiosk-mode.md`, `md/40897762779675-using-fareharbor-dock.md`, `md/47330976167451-fareharbor-dock-hardware-requirements.md`, `md/44281516364699-booking-management-in-dock-staff-mode.md`, `md/51823653511195-collecting-tips-on-fareharbor-dock.md`, `md/49746368068635-dock-staff-mode-partial-payment-and-mark-unpaid.md`, `md/40897806799771-qr-code-payments-with-fareharbor-dock.md`, `md/53050152853915-seat-assignment-in-dock.md` |
| Card readers | M2, WisePad 3, S700; Tap to Pay | Must buy from FareHarbor; contactless caps | Bluetooth enable: Support | `md/42957784953627-card-readers-at-a-glance.md`, `md/43739255445019-using-an-s700-card-reader.md`, `md/40897816885275-using-a-wisepad-3-bluetooth-card-reader-ios-fareharbor-app.md`, `md/40897814921627-using-a-wisepad-3-bluetooth-card-reader-with-the-fareharbor-android-app.md`, `md/40897796457371-using-an-m2-chipper-2x-bluetooth-card-reader-android-fareharbor-app.md`, `md/40897812267163-using-an-m2-chipper-2x-bluetooth-card-reader-ios-fareharbor-app.md`, `md/40897913362331-accepting-payments-with-tap-to-pay-on-android.md`, `md/40897920277659-accepting-payments-with-tap-to-pay-on-iphone.md`, `md/40897844588443-firewall-and-network-settings.md`, `md/40897814103323-legacy-using-a-verifone-p400-wi-fi-ethernet-card-reader.md`, `md/40897837807003-legacy-using-a-wisepos-e-wi-fi-card-reader.md`, `md/40897997796251-legacy-cardflight-ios-card-swipers.md` |
| Hardware guidance | Browsers, printers, scanners | Handheld scanners: Nadamoo, ScanAvenger | Boca: Support | `md/40897766646811-recommended-hardware-and-software.md` |

### 2.14 Settings and company-level toggles

| Feature | What it does | Key settings/limits | Needs Support? | Article(s) |
|---|---|---|---|---|
| Advanced company settings (gear) | Combos, Packages, FareHarbor Waivers, abandoned cart, bulk rebooking, API fee, dark mode, price previews, auto-archive, party size for summarized receipts, skip contact name | Needs "Edit Dashboard features, company contact info, and FareHarbor profile" | Some hidden | `md/42957728899611-setting-up-combos.md`, `md/40897871757339-fareharbor-waivers.md`, `md/40897602138523-abandoned-cart-recovery.md`, `md/40897261404187-rebooking-a-customer.md`, `md/42957604700827-api-fee-invoice-process.md` |
| Auto-archive | Campaigns, price sheets (730 days), resources (365 days) | Disable in Performance section | No | `md/40897303606683-archive-a-campaign.md`, `md/42957526035483-archiving-price-sheets.md`, `md/42957497827227-archiving-resources.md` |
| Demo mode | `?preview=` login; test card 4242 4242 4242 4242 | Cannot return to demo after go-live | Support gives URL | `md/40897745394587-using-fareharbor-in-demo-mode.md` |
| Request forms | Add availabilities, gift cards, promo codes, connectivity, affiliates, FHDN opt-in, 1:1 training | | Yes | `md/42957708079899-request-forms.md`, `md/42957471291419-new-item-request.md`, `md/51722294445467-complete-your-onboarding-worksheet.md` |
| Learning | Compass, Spark conference, webinars | Spark 2026 Austin Oct 27-29 | No | `md/40897920983067-fareharbor-compass.md`, `md/40897881393563-fareharbor-spark-conference.md`, `md/40897881467035-webinars-and-training-sign-up.md` |
| Recommended images | Logo 250px+, item photos 700px+ | | No | `md/40897918751003-recommended-image-sizes.md` |
| Privacy | CCPA requests via privacy policy | | n/a | `md/40897931324571-ccpa-and-data-privacy.md` |
| Getting started and glossary | Basics | | | `md/42957683138459-fareharbor-glossary.md`, `md/40897739713051-dashboard-fundamentals.md`, `md/40897741234331-navigating-the-dashboard.md`, `md/40897500869787-essential-dashboard-skills.md`, `md/40897766646811-recommended-hardware-and-software.md` |
| Troubleshooting | Errors, speed, calendar bookmarking, previewing embeds | LH-50 error = balance under $0.50 | No | `md/40897883820827-troubleshooting-error-messages.md`, `md/40897942850715-troubleshooting-speed.md`, `md/40897882231963-why-does-my-bookings-calendar-show-the-wrong-month-or-day.md`, `md/40897934838811-why-can-t-i-preview-calendar-embeds-on-my-website.md`, `md/40897882142875-how-do-i-block-off-a-day-on-my-calendar.md` |
| Maintenance notice | Feb 2026 downtime | Past | n/a | `md/44898770557339-february-2026-planned-system-maintenance.md` |
| Webinar library (109 pages, mostly stubs) | Hints at features: duplicate calendars, availability schedules, trip protection add-on, custom manifests | Not detailed | | `md/47784437781659` (Build 2026 calendar), `md/47784370822683` (manifest and check-in), `md/47784424412955` (updating availabilities) |

## 3. Promo codes and campaigns deep dive

FareHarbor has three redemption mechanisms that can coexist "without conflict" (`md/44475456979483-redemption-types-summary-use-cases.md`): Discount codes (a discount), Campaign codes (pre-paid value such as certificates and third-party vouchers) and Gift cards (a payment method). Affiliate promo codes are a fourth, tracking-first variant. None of the campaign or discount articles describe a URL parameter or auto-apply link. The only link-based mechanisms are affiliate book buttons/QR codes that carry a price sheet and `ASN ref` (`md/40898084853403-affiliate-book-buttons-qr-codes.md`), and the Lightframe `sheet-uuid` and `schedule-uuid` parameters used for affiliate links (`md/41240460210971-how-do-i-add-an-affiliate-activity-to-my-fareharbor-website.md`). A QR can "auto-apply discounted prices and/or include a promo code field" (`md/42957577429019-affiliate-booking-methods.md`), which is the closest thing to an auto-apply link.

### 3.1 Discount Codes (newer feature, Settings > Discount Codes)

Enablement: "The Discount Codes feature must first be enabled for your account"; submit a request to Support. Staff need the "Manage campaigns and discount codes" permission (`md/50079733016859-create-manage-discount-codes.md`).

| Setting | Detail | Source |
|---|---|---|
| Discount type | Percentage or fixed monetary. "Negative values are not supported. Decimal values are supported only for fixed-value discounts." | `md/50118840777883-reference-discount-code-settings.md` |
| Code format | "Codes can contain up to 20 characters. Spaces are not supported." Allowed specials: - _ $ # %. "Codes must be unique across discount and gift card codes." Manually typed only: "Discount codes currently support manually configured code values only." | same; `md/50118886356763-discount-codes-frequently-asked-questions.md` |
| Level | Applies at item or customer type level, "reduce the eligible booking subtotal before taxes and fees are calculated." "Applied once per" eligible item or customer type | `md/50079733016859-create-manage-discount-codes.md` |
| Items and customer types | Pick eligible items; limit to customer types | `md/50078996211483-introduction-to-discount-codes.md` |
| Minimum booking amount | Subtotal minimum, none by default | reference page |
| Maximum uses | "Unlimited redemptions are allowed by default. Any successful redemption counts toward the maximum usage limit, including multiple eligible items redeemed within the same transaction." | reference page |
| Redemption period | Required start date, optional end. "If no end date is configured, the code remains redeemable indefinitely." Statuses Active, Scheduled, Expired | reference page |
| Valid and blackout activity dates | Date ranges, weekdays or both. "Blackout dates always override valid activity date settings." | reference page; `md/50118924267035-discount-codes-best-practices.md` |
| Priced custom fields | Toggle applies the discount to all or none of the priced custom fields on eligible items | reference page |
| Restrict to Dashboard users | Customers cannot redeem online | reference page |
| Affiliate options | "Tag affiliate" auto-assigns an affiliate; "Block this discount when booked by an affiliate or through an affiliate link". Only shown when an affiliate exists | reference page |
| Zero-value codes | Percent or fixed 0, used for attribution without discounting; needed for combos | `md/50118863154331-guidelines-for-using-discount-codes-with-other-features.md` |

Per-customer limit: no per-customer or per-email redemption limit is documented for Discount Codes or Campaigns. Usage limits are total only (max uses per code).

Stacking and interactions:
- "Only one discount code can currently be redeemed per booking or transaction" (one code can hit several items in the cart). `md/50118924267035-discount-codes-best-practices.md`
- "Maximum usage limits apply to individual qualifying item redemptions, not just completed bookings or transactions." If few uses remain, "discounts will continue applying until the remaining usages are exhausted based on item order within the transaction." `md/50118886356763-discount-codes-frequently-asked-questions.md`
- Memberships: "Discount codes apply after membership pricing is applied, so customers can stack eligible discount codes with membership discounts." same FAQ.
- Combos: "Discount codes cannot currently be redeemed for bookings purchased with combos or packaged combos unless the discount is configured with a 0 value." "Combo pricing takes precedence over standard discount code pricing." Existing codes "may be removed automatically once combo pricing becomes applicable."
- "Discount codes cannot be used when a customer rebooks online." "This feature is not designed to be used in conjunction with third-party platforms, such as Groupon."
- A discount larger than the subtotal reduces it to zero; "Negative subtotals or booking credits are not created."
- Staff can apply by hand: booking > "+ Add expense or discount" > Discount code; "You can apply only one discount code per booking." `md/50118825905307-apply-a-discount-code-to-a-booking.md`
- Report: Expenses and Discounts report (`md/40898113325595-expenses-and-discounts-report.md`).

### 3.2 Campaigns (classic, Settings > Campaigns)

Needs enabling: "Please reach out to FareHarbor Support to enable the Campaigns feature." Support will also build campaigns from the Promo Code Request Form (`md/44475456979483-redemption-types-summary-use-cases.md`, `md/40897288863899-campaign-and-promo-code-faqs.md`, `md/40897264802587-new-promo-code-request.md`).

| Setting | Detail | Source |
|---|---|---|
| Codes | Typed one per line or "Generate random codes" with optional prefix. "Codes are not case sensitive." Allowed: letters, numbers, - _ # $ %. Tip: do not include the campaign name in the code | `md/40897288495515-creating-campaigns-and-promo-codes.md` |
| Max uses per code | Set per code; blank = unlimited | same |
| Pricing | Price column on the Campaign code custom field: Change > "Adjust total by" percent or dollar. "discounts should always be entered as negative numbers"; without the minus sign "the code will add the amount or percentage instead of subtracting it." | same |
| Whole booking vs per customer | Checkbox "If priced, change price of all customers on booking" (works only on whole-booking fields) | same; FAQ |
| Item scope | Field is attached to an item (Whole-booking fields tab) or to specific customer types | same |
| Valid/blackout dates | Five bases: availabilities on, booking on, days before midnight on day of availability (early bird), days after code generation by booking date, days after code generation by availability start. Weekday options. "These rules apply to online customers only. Logged-in Dashboard users with booking permissions can override valid and blackout dates, if needed." "When no valid or blackout dates are added, codes will always be valid." "If there are overlapping valid and blackout dates, the blackout dates will override the valid dates." | `md/40897273365915-adding-valid-or-blackout-dates.md` |
| Affiliate promo | Edit code > Advanced > "ASN Affiliate" tags the affiliate to each online booking | `md/40897288495515-creating-campaigns-and-promo-codes.md` |
| Customer errors | "Cannot be used today", "Not valid for this availability", or max uses reached | `md/40897288863899-campaign-and-promo-code-faqs.md` |
| Field display | Promo field is hidden behind "Add promo or discount code" link by default; uncheck "Hide code input behind a link" to show it | same |
| Archive | Auto-archive after "2 years (730 days)" of inactivity by default; codes with max use under 50 only archive "once all uses are exhausted" | `md/40897303606683-archive-a-campaign.md` |
| Delete | Deleted codes still show in reports; cannot delete while attached to a custom field | `md/40897292795035-removing-and-deleting-campaigns.md` |
| Conversion | Campaigns acting as discount codes can be moved to Discount Codes by Support | `md/44475456979483-redemption-types-summary-use-cases.md` |
| Tracking | Campaigns report (bookings and net revenue per campaign); Custom Field Answers per code; Total column is what the campaign cost you | `md/40897317690779-tracking-and-analyzing-campaigns.md` |

### 3.3 Affiliate promo codes, vouchers, OTA discounts, gift cards, stacking

- Affiliate promo codes: Support-built; code on your site tags the affiliate with or without a discount; commission per customer, booking total or product; "We recommend only having one of these features enabled" (promo codes or discount codes). Promo codes cannot be used on items covered by a matching affiliate rule ("Some options you selected are no longer available"). `md/42957562974747-affiliate-promo-codes.md`, `md/40898100610715-affiliate-rules.md`
- Voucher codes (Groupon style): one-time codes, 100% off one person, net rate owed can be fixed even at $0. `md/42957562974747-affiliate-promo-codes.md`, `md/40897305203355-using-groupon-travelzoo-or-livingsocial-with-fareharbor.md`
- OTA discounts: "Currently, OTA discounts are only available for Viator." Percentage only, one discount per booking, applied automatically on the OTA, no effect on direct bookings, "Not currently compatible with Dynamic Pricing". `md/45501481631899-how-to-create-an-ota-discount.md`, `md/51495663149083-viator-special-offers.md`
- Gift cards: "Gift cards cannot be made redeemable for certain items only." Case and character sensitive. "A customer cannot use a gift card to purchase another gift card." "Gift cards cannot be applied when an item requires a deposit." `md/40897462601755-gift-card-faqs.md`, `md/40898010428315-deposits.md`
- Combo discounts cannot stack with discount codes but can with campaign codes if the combo's Campaigns setting is checked. `md/42957726827675-combo-discounts.md`
- Custom fields with adjustable pricing allow staff-entered one-off discounts. `md/40897408900379-using-custom-fields-with-adjustable-pricing.md`
- Price sheet Adjustment column discounts a whole sheet by percent. `md/40897594780699-using-price-sheets.md`
- Dynamic Pricing: "Not for exact-condition rules (e.g. 60 days in advance early bird): use price schedules". `md/54312757536027-introduction-to-dynamic-pricing-2-0.md`

## 4. Communication and automation deep dive

### 4.1 Automatic customer messages

| Message | Trigger and timing | Customization | Not customizable | Source |
|---|---|---|---|---|
| Confirmation email | On booking; Dashboard bookings use "Send confirmation email by default" checkbox | Company, item and headline confirmation notes (item above company); canned messages; locations with headings; health and safety policy; cancellation notes; translations; Markdown | Layout | `md/40897393367963-updating-confirmation-notes.md`, `md/40897362574619-updating-default-email-settings.md`, `md/40897375707931-locations.md` |
| Rebooked / cancellation email | On staff action if default boxes are checked | Cancellation notes are included in all emails except follow-ups | | `md/40897348918171-updating-your-cancellation-notes.md` |
| Reminder email | Per item, hours before start, up to 2880 hours (120 days). Sent at top of the hour, fractions round up. Optional "reminder cutoff" to skip late bookings | Canned message or custom; multiple recipients | | `md/40897385230363-automatic-reminders-and-follow-ups.md` |
| Follow-up email | Hours after availability start or end; thank-you, review, share. With FH Waivers, goes to every digital signer | Google review URL, survey URL (button "Tell us about your experience" with booking, start-at and item parameters), social links | | same; `md/40897349493531-social-media-and-survey-urls.md` |
| Reminder text | Same scheduler as reminder email; "Text messages can only be sent as reminders" | "limited to a maximum of 130 characters. All texts will automatically include a direct link to the booking details." | No follow-up texts | same; `md/40897348692763-texting-customers.md` |
| Waitlist signup email | "always sent and cannot be disabled" | | | `md/42957506762395-waitlist.md` |
| Waitlist seat-opened email | Optional automatic on cancellation/rebooking, grace period in minutes; once per customer | "You cannot customize automatic notification emails" | | same |
| Abandoned cart email | One email 2 hours after drop-off, after an email entered at checkout; cart item starts 8+ hours later | "Cannot be customized, resent or triggered manually" | Count of sends not reportable | `md/40897602138523-abandoned-cart-recovery.md` |
| Payment reminders / payment links | "Make a payment" button on confirmation page, emails, reminders | Payment reminder as a canned Message | No automatic payment plans or deadlines | `md/42957750164379-using-payment-links-for-underpaid-bookings.md` |
| Private event payment reminders | 24 hours before a payment is due | | | `md/40897258328091-configuring-private-events.md` |
| Waiver requests | On confirmation screen, confirmation, reminder emails, reminder SMS | Text, sections, fields, minors; no translations | Submit button text | `md/40897871757339-fareharbor-waivers.md` |
| Gift card emails | Recipient email with code; purchaser can resend | Design, message, recipient notes | Cannot change a purchased card's design | `md/40897463368859-creating-gift-card-designs.md` |
| Membership emails | Purchase email with QR; reminder one week before expiry; auto-renew reminder with cancel link | Reminder message limited to "Newly expired membership message" type | | `md/40897543220635-overlapping-memberships.md`, `md/42957494045595-purchasing-using-and-renewing-memberships.md` |
| Proposal email (private events) | Manual | Proposal message max 100 chars | | `md/40897300430619-setting-up-a-private-event.md` |
| Airbnb messages | Delivered in Airbnb inbox, outbound only; links, phones, emails stripped | Toggle | | `md/40898086122395-working-with-airbnb-experiences.md` |
| API/OTA bookings | Follow-ups sent; reminders contradictory (see section 6) | Per affiliate settings | | `md/53778629402651-working-with-external-apis.md` |
| Staff alerts | New/cancelled bookings, manifests, crew, disputes, failed customer emails, bank changes | Email and app push per user or per item | No SMS to staff | `md/42957499257627-subscribing-to-user-notifications.md` |

### 4.2 Controls

- Per-item switches live at Items > item > Settings > Notifications > Customer Notifications and must be repeated per item (`md/40897385230363-automatic-reminders-and-follow-ups.md`).
- Disable for one booking (gear beside Send email or text), one availability (weather cancellations), or many via the availability updater.
- A manual send before the scheduled time "will prevent the scheduled message from being sent."
- No-shows: if every customer is a no-show, automatic follow-ups (including Tripadvisor Review Express) are off by default (`md/40897308837275-no-shows-and-follow-ups.md`).
- Cancelled availabilities disable reminders; reopening requires re-enabling them (`md/40897123112859-canceling-availabilities.md`).
- Texting: only to verified numbers, only opted-in customers appear in bulk sends, send-only (replies get an auto-response), international numbers allowed, delivery status logged and visible as a manifest column (`md/40897348692763-texting-customers.md`). Carriers flag links, all caps and words such as "Free".
- Email status columns on the manifest show sent/opened times. Bounce alerts are a staff notification.
- Bulk email works per availability only; across date ranges "it is not possible" (`md/40897386906395-emailing-customers.md`).
- Translations send emails in the contact's language; per-booking language change (`md/40897347733659-translating-your-fareharbor-content-into-other-languages.md`).
- Unsubscribing via the footer link kills all FareHarbor emails, including invoices and disputes; only Support can resubscribe (`md/40897725265307-unsubscribing-from-user-email-notifications.md`).
- Receipt customization: footer, tip line, party-size summary threshold (`md/40897618955547-customizing-receipts.md`).
- Retail items switch off every automatic notification except abandoned cart (`md/45944867557915-reverting-retail-item-settings.md`).

### 4.3 What FareHarbor does not do natively

No marketing campaigns or newsletters, no SMS follow-ups, no two-way SMS, no cross-date bulk email, no custom abandoned cart sequence. Partners fill the gap: Podium, Mailchimp, HubSpot, TourAdvantage (Drip), Yonder, Dazhboards, the FareHarbor Agent (`md/40898230385947-podium-integration.md`, `md/43770566859035-integrating-mailchimp.md`, `md/54893080554779-dazhboards-integration.md`).

## 5. API and integration deep dive

External API (`developer.fareharbor.com/api/external/v1/`, cited in `md/42957577429019-affiliate-booking-methods.md`)
- The help center does not list per-endpoint scopes. It describes the External API as a partner channel for OTAs/resellers: availability, pricing, booking create/cancel and item data keyed by company shortname and item ID (`md/53778629402651-working-with-external-apis.md`). The article does not say customer lists are readable.
- Operator-side data reads are via webhooks, Zapier and reports, not a self-serve REST key. Zapier keys come from Your Account > API Keys, and data is limited to the user's permission group.
- Affiliate API access needs: payment gateway, developer team, "$50,000 total transaction value trailing 12 months", "Connection fee and annual maintenance fees: 1,000 EUR each", and signed agreements. FHDN API needs $250,000 trailing and an FHDN contract (`md/42957577429019-affiliate-booking-methods.md`).
- Setup for a connected OTA: request via the Connectivity Support Form; affiliate with price sheet and invoice sheet; "Default - API cancellation policy"; permission "Affiliate - API External"; default payment "Affiliate taking payment"; deselect "Require a voucher number on bookings".
- Changes that break the connection: adding/removing customer types, deleting or replacing the item, modifying API resources, changing pricing. "Call-to-book, cancelled, closed, or hidden availabilities are considered unavailable via API." Unlisted availabilities are read as "Open" by the reseller API (`md/40897205605659-making-an-availability-unlisted.md`).
- Fees: "A 2% API Fee applies to all eligible API-generated bookings, except for our clients in Guam and French Polynesia" on "Total Paid to Affiliate". Opt in with "Allow API Bookings to be charged an API Fee". Exempt: direct bookings, FHDN, Google Things to Do, affiliate book buttons, portal bookings, promo codes. Invoiced by the 5th, charged on the 6th, retried the 13th (`md/42957604700827-api-fee-invoice-process.md`).
- FHDN commission: referral links 20%; API 25% (operator nets 75%); operator as affiliate earns 15%. "The commission rates are non-negotiable." API OTA pays net month after activity (`md/42957709413403-fareharbor-distribution-network-fhdn-overview.md`). Booking.com standard is 25% via the FHDN API (`md/42957706509595-working-with-booking-com.md`). Pricing sync is controlled by Viator (enable in Viator), and adult/group tickets under $5 do not sync (`md/46620607425819-working-with-viator.md`).
- Rate limits: none stated for the External API. Only documented throttle: 3,000 waiver signatures per day per company, 250 per minute across dashboards (`md/54050261537563-waiver-links.md`), and a Meta limit of one pixel per Dashboard.

Webhooks (`md/40898249392539-introduction-to-webhooks.md`, `md/40898279460763-configuring-webhooks.md`, `md/40898294427291-using-webhooks.md`)
- One-way POST JSON in real time. Added per user (Users & Permissions > user > Webhooks tab).
- Schemas: Bookings only, Bookings only (Optimized), Bookings + payments, Bookings + payments (Optimized), custom booking schema (cannot be updated; create a new one), Items.
- Triggers: New, Updated (includes cancellations), Canceled. Item webhooks fire on listing, bookability, Info & Policies and notification saves. "Adding or updating images does not trigger API calls."
- "New" does not fire for refunds, payments, hold card, check-in, discounts, reprice. "Updated" does fire for check-in, refunds, waiver signatures, contact edits.
- HTTPS required; failures retry "three times, with a 60-second delay between retries".
- Limits: "Visibility into gift cards, promo codes, or discount codes is not available." "Webhooks cannot be used for generating invoices." Activity log of deliveries on request.

Zapier (`md/40898281485339-introduction-to-the-zapier-integration.md`)
- FH to Zapier only; three FareHarbor triggers; 2,000+ apps. Square paid-order and inventory Zaps documented. Free/Starter plans need one Zap per retail item.

Fees and approvals summary
- API fee 2%, FHDN 20/25%, Booking fee 6% (direct, small volume), processing tiered, Dock transaction fee (ask Account Manager), PicThrive/TourClaim/vQuip paid by partner contract.
- Partner relationship required: External API, FHDN API, Google Things to Do (connectivity form), GetYourGuide ("may take several weeks"), Booking.com (very limited new connections), Expedia (via Local Expert), MyPassTracker (no new integrations), Wherewolf (webhook-based).

## 6. Gotchas and hidden limits

Money
- Refund keeps the booking fee on partial refunds: "FareHarbor has a policy of retaining a booking fee on bookings with partial refunds." Full refunds are free. `md/40898002492443-credit-card-refund-faqs.md`
- Processing fees paid on earlier transactions are "non-refundable" when rates change. `md/40897934927131-processing-rate-adjustments.md`
- You "cannot issue a refund in FareHarbor once a charge has already been marked as disputed" (except Pending inquiries). `md/40898039858843-dispute-reasons-and-what-to-do.md`
- Fraud disputes: "Even if the charge was made using a stolen credit card, unfortunately you will need to accept the dispute."
- 1099-K will not match reports; API bookings are not on it. `md/42957746733083-frequently-asked-questions-about-the-1099-k-form.md`
- Gift cards online capped at 10,000 local currency; higher "can result in Stripe punitively disabling payments". `md/40897462601755-gift-card-faqs.md`
- Afterpay "is not a suitable solution for bookings over $2000." `md/42957731295387-afterpay.md`
- Card readers bought elsewhere will not work. `md/42957784953627-card-readers-at-a-glance.md`
- Tap to Pay: no PIN; $100 Visa/MC and $250 Amex caps; not iPad. `md/40897913362331-accepting-payments-with-tap-to-pay-on-android.md`
- Payment links: from 2026-09-10 full remaining balance only. Confirmation pages expire "seven days after the availability ends".
- Ledgers cannot be turned off once enabled. `md/40898000845851-ledgers.md`
- Payouts missing: savings accounts unsupported, Payoneer/Wise cannot do bank debits, checklist incomplete.

Availability and booking
- Cancelling an availability does not cancel bookings or notify customers.
- Bulk delete converts availabilities with bookings to Closed & Hidden.
- Changing an availability's capacity "will not automatically adjust its available resources"; changing time of a resourced availability does not shift resource use.
- Duplicate availabilities default to not bookable online.
- Customer type capacity edits at item level only affect new availabilities.
- Exclusive customer types ignore item min/max party size.
- Bulk rebooking has no undo; "bulk cancellation and rebooking" does not exist.
- Items with future bookings cannot be archived; items with any bookings cannot be deleted.
- Customized booking flows do not auto-add new items.
- "Combos consist of two items only" (one article describes a three-item package; the FAQ says two). Combos do not carry over on rebooking, only work online, and "will not work with affiliates and ASN links."
- Waitlist does not work with conditional customer types.
- Resources exhausted = availability disappears online, no Sold Out message.
- Online rebooking excludes affiliate bookings, cash, gift card or promo payments, deposits.
- Orders and online cart are off by default.

Communication
- Texts max 130 characters and cannot be follow-ups.
- No SMS for logged-in users.
- Footer unsubscribe kills invoices and dispute emails.
- Waivers: one waiver per item, 300 signers per booking, no translations, in-person waivers cannot be attached to a booking, cannot run beside Smartwaiver or Wherewolf, retained 7 years.
- Files on bookings are not allowed; PII uploads blocked.

Distribution
- "Cross-Sell Combos do not support commissions or affiliate tracking."
- Affiliate commissions: "we cannot accommodate commission structures based on number of seats sold" and "Commissions are not paid out automatically."
- Affiliate rules and blocks cannot be reported on; blocks do not work with resources.
- Opting out of FHDN: 30 days notice; "affiliates will not be alerted" of API cancellations.
- Booking.com is "not currently able to process new requests."
- Google Things to Do limit: 10 activities per business page.
- Cancelling an API booking in FareHarbor does not cancel it for the customer.

Websites and tracking
- GA4 and FareHarbor "will never match".
- Facebook removed custom Book Now links; GTM-only setups often fail; conversion pixels cannot read names or phones.
- Wix and GoDaddy GoCentral embeds cannot open in Lightframe.
- Linking straight to booking flows can hurt SEO.
- Price previews missing on items with more than 30 availabilities per day.
- FareHarbor Sites: template stays with FareHarbor; no extra plugins.

Account
- 2SV required; no authenticator apps; no admin-assisted setup.
- Permission group editing is disabled for everyone by default.
- Creating cancellation policies is "disabled by default".
- Many features listed as "must be enabled by FareHarbor": Discount Codes, Campaigns, Memberships (plus flexible, overlapping and sub-members each), Check-in, Orders, Online cart, Suggested items, Multi-tax, Tagging, Seating, Transportation, Dock, Private events, Ledgers, deposits, payment links, online rebooking, Boca tickets, receipt printing, Google ratings, texting, waiver links.

Source contradictions to confirm live
- Customer directory lifetime value: net of refunds vs "not deducted".
- Affiliate invoice by card: FAQ says no, invoicing pages say yes.
- Viator reservation hold: 5 vs 15 minutes.
- External API reminder emails: setting says send, text says "not provided".
- Item occupancy and resources: older page says unsupported, newer says supported.
- Xero tax values; Combo report (reporting available vs not); Multi-tax price adjustments.
- Android QR scanning needs internet; Android offline mode exists from app 1.14 (`md/40897319874843-scanning-qr-codes-offline-using-the-fareharbor-android-app.md`).
- Gift card tax: overview says full amount applies to price and tax; FAQ example leaves tax due.

## 7. Audit checklist (answer yes/no per company dashboard)

Items and availability
1. Is every item's Item Setup Checklist green? (`md/40897518310427-creating-an-item.md`)
2. Do all public items have a Content Builder description and 5+ photos at 1800px wide? (`md/40897489868315-content-builder.md`)
3. Are retail items (merch, gift cards, memberships) set to "Display as a retail item"? (`md/39062128436251-set-up-a-retail-item.md`)
4. Are availabilities created from Availability Schedules, and did you duplicate next year's calendar? (`md/40897157383579-creating-availabilities.md`)
5. Are cutoffs set per item, with different rules for empty vs booked availabilities? (`md/42957724449051-booking-restrictions.md`)
6. Do you use negative cutoff hours or the Open override for walk-up friendly items? (`md/40897924991771-how-do-i-change-online-booking-cutoff-times.md`)
7. Is a custom sold-out message set instead of "call to book"? (`md/40897941513755-how-do-i-change-the-message-displayed-for-sold-out-availabilities.md`)
8. Is the waitlist enabled on full-prone items, with automatic seat-opened email? (`md/42957506762395-waitlist.md`)
9. Is the reservation timer enabled on high-demand items? (`md/40897508706715-reservation-timer.md`)
10. Are boats, kayaks, bikes and captains modeled as resources with overrides? (`md/40897623777947-resources-overview.md`)
11. Do boat items use seat maps with online seat selection or exclusive groups? (`md/40897668719003-introduction-to-seating-assignment.md`)
12. Is capacity per customer type set where bikes or kid seats are limited? (`md/40897443464603-customer-types-overview.md`)
13. Are private charter customer types marked exclusive? (`md/40897442777627-exclusive-customer-types.md`)
14. Do you use public headlines with photos for special departures? (`md/40897164314267-managing-availability-headlines.md`)
15. Is the booking flow structured so new items are added to custom flows? (`md/40897873586971-managing-booking-flows.md`)

Pricing and fields
16. Are Online, Direct and affiliate price sheets deliberate (not left at defaults)? (`md/40897574874907-introduction-to-price-sheets.md`)
17. Do you use price schedules for seasonal or weekend pricing and set it as company default? (`md/40897588033691-introduction-to-price-schedules.md`)
18. Have you asked your Account Manager about Dynamic Pricing 2.0 or dynamic rules? (`md/54312757536027-introduction-to-dynamic-pricing-2-0.md`)
19. Are price previews on and including fees and taxes? (`md/42957817873179-price-previews-for-online-booking.md`)
20. Are add-ons (photo package, trip protection, gear, food, tip) sold as priced custom fields? (`md/40897451668251-setting-up-custom-fields.md`)
21. Are conditional custom fields used to shorten the book form? (`md/40897381615515-conditional-custom-fields.md`)
22. Is adjustable pricing available to staff for comps and damage fees? (`md/40897408900379-using-custom-fields-with-adjustable-pricing.md`)
23. Are tax types correct and is Multi-tax avoided unless required? (`md/40897859797659-multi-tax.md`)

Bookings, check-in and operations
24. Is Check-in enabled with custom statuses and auto no-show? (`md/40897334261915-checking-in-customers.md`)
25. Is QR ticket scanning enabled on each item, with devices configured? (`md/40897298271899-introduction-to-setting-up-and-scanning-qr-codes.md`)
26. Are custom manifests saved and assigned as user defaults? (`md/40897482570395-saving-custom-manifests.md`)
27. Are custom calendars saved per role (captains, front desk)? (`md/40897225844123-saving-custom-calendars.md`)
28. Are crew assigned in the Dashboard with crew reminders and manifest links? (`md/40897393741083-crew-notifications.md`)
29. Is the ICS calendar subscription set up for captains? (`md/40897927395227-how-do-i-add-my-fareharbor-calendar-to-my-mobile-device-or-computer.md`)
30. Are orders and the online cart enabled? (`md/40897546559515-online-orders-and-shopping-cart.md`)
31. Is the abandoned cart email enabled? (`md/40897602138523-abandoned-cart-recovery.md`)
32. Is online rebooking or online cancellation enabled with cancellation policies per item? (`md/40897213805723-online-rebooking.md`, `md/40897768261019-cancellation-policies.md`)
33. Is bulk rebooking enabled for weather cancellations? (`md/40897261404187-rebooking-a-customer.md`)
34. Is Private Events configured for charters or buyouts (if in North America)? (`md/40897258328091-configuring-private-events.md`)
35. Are walk-up bookings allowed without name or email, with permissions limited? (`md/40897223488027-creating-bookings-without-a-contact-name.md`)

Customers and CRM
36. Is the Customer directory enabled, with tags used? (`md/42957456905883-customer-directory.md`)
37. Is "Subscribe to email list" captured, and is Contacts exported to an email tool? (`md/40898088413595-contacts-report.md`)
38. Is a CRM/email integration (HubSpot, Mailchimp, Podium) connected? (`md/43770566859035-integrating-mailchimp.md`)

Campaigns, gift cards, memberships, upsell
39. Are Discount Codes and Campaigns both enabled where needed? (`md/50079733016859-create-manage-discount-codes.md`)
40. Do promo codes use valid/blackout dates and max uses? (`md/40897273365915-adding-valid-or-blackout-dates.md`)
41. Is every promo code tracked on the Campaigns report monthly? (`md/40898061587995-campaigns-report.md`)
42. Is promo field visible (not hidden behind a link) on key items? (`md/40897288863899-campaign-and-promo-code-faqs.md`)
43. Are gift cards sold online with designs and a "Buy now" button on the website? (`md/40897462601755-gift-card-faqs.md`)
44. Do cancellations offer gift card credit instead of refunds? (`md/40897504237851-giving-credit-using-gift-cards.md`)
45. Are memberships, punchcards or season passes offered? (`md/40897569988507-creating-memberships.md`)
46. Are combos or packaged combos built, with seasonal discounts? (`md/42957728899611-setting-up-combos.md`)
47. Are Cross-Sell Combos running with neighboring operators? (`md/42957735775643-cross-sell-combos.md`)
48. Are suggested items active in cart and confirmation email? (`md/40897852857755-suggested-items.md`)

Communication and waivers
49. Are automatic reminder emails on for every item? (`md/40897385230363-automatic-reminders-and-follow-ups.md`)
50. Are reminder texts on, and is texting enabled with opt-in captured online? (`md/40897348692763-texting-customers.md`)
51. Are follow-up emails on, with Google review URL and survey URL filled? (`md/40897349493531-social-media-and-survey-urls.md`)
52. Do confirmation notes include arrival, parking, what to bring, and weather policy? (`md/40897393367963-updating-confirmation-notes.md`)
53. Are Locations with Google Place IDs set for every item? (`md/40897375707931-locations.md`)
54. Are canned messages ready for weather delays? (`md/40897372816795-canned-messages.md`)
55. Are FareHarbor Waivers enabled (and not conflicting with Smartwaiver)? (`md/40897871757339-fareharbor-waivers.md`)
56. Are standalone waiver links enabled for events? (`md/54050261537563-waiver-links.md`)
57. Are staff subscribed to new booking, cancellation and dispute notifications? (`md/42957499257627-subscribing-to-user-notifications.md`)
58. Is FareHarbor Agent available on this account? (`md/48858951282075-introduction-to-fareharbor-agent.md`)
59. Are translations enabled where guests are international? (`md/40897347733659-translating-your-fareharbor-content-into-other-languages.md`)

Payments
60. Is the Payment Setup Checklist fully green and reverification current? (`md/40897894382747-updating-the-payment-setup-checklist.md`)
61. Is the 6% booking fee applicable, and is the billing method on file? (`md/40897900687771-october-2024-booking-fee-adjustment.md`)
62. Are deposits enabled for high-value or private items? (`md/40898010428315-deposits.md`)
63. Are payment links enabled for balances? (`md/42957750164379-using-payment-links-for-underpaid-bookings.md`)
64. Is Afterpay, Apple Pay, Google Pay and Link live online? (`md/42957731295387-afterpay.md`)
65. Is AVS requested on items with fraud history? (`md/43436153392667-address-verification-system-avs.md`)
66. Is Refund Reserve funded with a recurring transfer? (`md/40898037215259-managing-your-refund-reserve.md`)
67. Is card statement text clear (18 characters)? (`md/40897980786843-what-is-my-card-statement-text.md`)
68. Are dispute notifications on and are check-in records used as evidence? (`md/40898023469083-tips-for-preventing-disputes.md`)
69. Are ledgers needed for separate bank accounts? (`md/40898000845851-ledgers.md`)
70. Are card readers purchased from FareHarbor, with Tap to Pay enabled? (`md/42957784953627-card-readers-at-a-glance.md`)
71. Is Dock activated for walk-up sales with tipping and printers? (`md/42957713960987-introduction-to-fareharbor-dock.md`)

Distribution
72. Are you in FHDN (as provider) and what commission is accepted? (`md/42957709413403-fareharbor-distribution-network-fhdn-overview.md`)
73. Has the FHDN API payout account been set up by end of September 2026? (`md/54515340128923-setting-up-fhdn-api-payouts.md`)
74. Is the Marketplace item quality score maximized (photos, 30+ future availabilities, reviews)? (`md/40898234979995-how-to-improve-your-fareharbor-marketplace-item-quality-score.md`)
75. Is Google Things to Do connected? (`md/40898232783003-google-things-to-do-integration.md`)
76. Are you eligible and listed in ChatGPT? (`md/47076472962459-fareharbor-in-chatgpt.md`)
77. Are Viator, Airbnb, GetYourGuide, Booking.com connections reviewed for API fee and rate parity? (`md/53778629402651-working-with-external-apis.md`)
78. Do hotels and concierges use affiliate QR/promo codes with tracked commissions? (`md/42957577429019-affiliate-booking-methods.md`)
79. Are affiliate rules limiting OTA capacity during peak? (`md/40898100610715-affiliate-rules.md`)
80. Are affiliate blocks used for partners who need guaranteed seats? (`md/46302229002779-affiliate-blocks.md`)
81. Are affiliate categories set for reporting? (`md/56014078344091-affiliate-categories.md`)

Website and tracking
82. Is the Lightframe auto-lightframe script on every page of the site? (`md/40898469746075-lightframe-overview.md`)
83. Does every embed/button carry an Online ref tag? (`md/40898512663451-adding-fareharbor-links-and-embeds-to-your-website.md`)
84. Is GA4 connected through Settings > Analytics & Tracking with referral exclusions? (`md/42957815081883-setting-up-google-analytics-4-ga4-to-work-with-fareharbor.md`)
85. For multiple Dashboards on one site, is the company_shortname dimension created? (`md/49910563968539-configuring-your-ga4-property-for-multiple-fareharbor-dashboards.md`)
86. Is Meta Conversions API configured with one pixel? (`md/42957825564827-tracking-conversions-with-the-meta-facebook-pixel.md`)
87. Is GA4 purchase imported to Google Ads as the only primary conversion? (`md/42957830296475-tracking-conversions-in-google-ads-using-ga4.md`)
88. Is a supported cookie consent tool installed? (`md/42957738437659-cookies-under-privacy-laws.md`)
89. If on FareHarbor Sites, is Price Sync enabled? (`md/42957794771995-price-sync.md`)
90. Are Facebook and Instagram links using the Link code type? (`md/40898451866011-adding-book-banners-to-instagram-posts.md`)

Reporting and admin
91. Is the Pace report reviewed weekly? (`md/48197997852443-introduction-to-the-pace-report.md`)
92. Is Item occupancy reviewed for under 50% availabilities? (`md/51274856853659-item-occupancy-report.md`)
93. Are Booking source and Affiliate bookings reports saved? (`md/40898028173851-booking-source-report.md`)
94. Is Insights and opportunities reviewed? (`md/44922963169819-insights-opportunities.md`)
95. Are webhooks or Zapier sending bookings to Sheets, Slack or CRM? (`md/40898249392539-introduction-to-webhooks.md`)
96. Is QuickBooks/Xero connected for accounting? (`md/42957793242395-quickbooks-online-integration.md`)
97. Do all users have verified emails, 2SV and least-privilege permission groups? (`md/40897681313563-2-step-verification.md`, `md/40897699291803-permission-groups.md`)
98. Is multi-dashboard reporting configured for the 12 companies? (`md/40898057916955-running-reports-across-multiple-dashboards.md`)
99. Are auto-archive settings reviewed (campaigns, price sheets, resources)? (`md/40897303606683-archive-a-campaign.md`)
100. Are Google ratings enabled on the book form (100+ reviews, 4.2+)? (`md/40897237339035-google-ratings.md`)
