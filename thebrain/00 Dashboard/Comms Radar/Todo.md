# Todo (Comms Radar)

Updated 2026-11-18 16:10. The radar re-reads this file every 2 hours and never un-ticks anything.

- Tick a box to close an item. Untick to reopen.
- Edit a title, a `#due:YYYY-MM-DD`, or the tags `#today` `#in-progress` `#waiting`. Your edits win.
- Comment: add a line under an item that starts with `  > ` and write your note. The radar answers on a `> Radar:` line.
- Add your own item anywhere as `- [ ] text #NPB`. It gets an id next run.
- Moving a line between sections does nothing; sections are re-sorted each run. To dismiss an item, tick it.

## Today and in progress

_nothing_


## Needs you

- [ ] Gravity Trails Autopayroll on hold, blocked before Nov 18 noon CST #due:2026-11-18 #id:T0211
  → David or the payroll admin open Homebase and resolve the issue holding Gravity Trails' Autopayroll before 12:00pm CST Nov 18. (David; Gmail dwrack81@; touched 2026-11-17)
- [ ] Elevated Tides umbrella policy: binder effective 11/6, payment link now sent #due:2026-12-13 #id:T0095
  → David and Jonah pay the invoice through Max's payment link and answer the carrier's questions via Max (expected revenue from the dock rental, whether it is rented with staff, supervision, what renters can access); Max is getting the no-watercraft-exclusion statement in writing, and the COI is due by Dec 13. (David; Gmail davey@; touched 2026-11-18)
  > David: this has nothign to do with jeff, so not sure why it says jeff should see this as an option below. fixt that. also i should have something that lets me know if jonah is working on it or if i am, can you pull his dashboard for ebb and ember and we can see whats involved with our lanes and items so that we aren’t doing double work.
  > Radar: Fixed the next move so it only names you, Jonah and Max, with no Jeff. I can't pull Jonah's Ebb & Ember dashboard from here, so I noted it as your next step to compare lanes before paying.
- [ ] Innovative Printing statement, pay by card over the phone #DCKT #id:T0015
  → David call Innovative Printing and pay the statement with a credit card. (David; Gmail doorcountykayaking@; touched 2026-10-30)
- [ ] TideBot written log processing down: Gemini credits depleted #NKST #id:T0104
  → David add prepay credits to the Google AI Studio project so TideBot's written trip log processing works again; the Nov 6 NKST log needs manual processing. (David; Slack #the-helm; touched 2026-11-06)
  > David: still? i thought we fixed this. i gave you 3 sets of apis to use as backup. help me help you to fix it if it really still needs fixing. but do it right this time;
  > Radar: I can't see this thread's details or run a live check from the ledger, so I can't say whether it is fixed. Someone needs to check the TideBot logs to see which API key the log processing is calling now and whether your three backup keys are wired in. Until that check is done, treat the status as unverified.
- [ ] Entergy bill overdue for 1407 Piety, $1,151.11 total, $647.20 past due #id:T0089
  → David check whether the $647.20 past due amount is covered; the Autopay notice forwarded by Gravity Trails says it is scheduled for 12/08/2026, so it will not clear anything overdue before then. (David; Gmail nolapedalbarge@; touched 2026-11-07)
  > David: it's my Piety address.
  > Radar: Got it, it's your Piety address, so I marked this as yours to pay: $647.20 is past due out of $1,151.11. Automating it sits in D0001.
- [ ] TideBot written log processing down, Gemini prepaid credits depleted #NKST #id:T0111
  → David top up the Gemini API prepay credits in AI Studio so TideBot can process written trip logs again; until then NKST logs need manual processing. (David; Slack #the-helm; touched 2026-11-08)
- [ ] Rick Carlson broker asks if NOLA Bike Bar sells standalone or with shared equipment and staff #NOLA-Bike-Bar #id:T0122
  → David decide whether to answer Rick Carlson on selling NOLA Bike Bar standalone versus including shared equipment, staff or booking infrastructure, or to drop the buyer inquiry. (David; Gmail nolakayaktours@; touched 2026-11-09)
- [ ] TideBot written log processing failing, Gemini prepaid credits depleted #NKST #id:T0124
  → David top up the Gemini API prepaid credits in AI Studio so TideBot can process written logs again; NKST manager process the Nov 9 log by hand. (David; Slack #the-helm, Slack #new-orleans-kayak-swamp-tours; touched 2026-11-09)
- [ ] TideBot written log processing failing, Gemini prepaid credits depleted #NKST #id:T0136
  → David top up the Gemini AI Studio prepay credits so TideBot can process written trip logs again; the Nov 9 Manchac log was left unprocessed. (David; Slack #the-helm; touched 2026-11-10)
- [ ] TideBot written log processing down, Gemini prepayment credits depleted #NKST #id:T0144
  → David or whoever runs TideBot on mbp-2 check which Gemini key and project it is calling and add prepay credits there, since the 402 says credits are depleted even after 3 keys were uploaded; then reprocess the Nov 12 logs by hand. (David; Slack #the-helm, Slack #new-orleans-kayak-swamp-tours; touched 2026-11-12)
  > David: fix it. i uploaded 3 total api keys to make sure we had enough keys and api credits to do this.
  > Radar: I can't touch TideBot or Gemini billing from here, so I logged this as your next move. The error is a 402 on gemini-2.5-flash-lite saying prepay credits are depleted, so the key TideBot is calling may not be one of the three you added, or they share one empty project. Two more NKST logs failed today and need manual processing.
- [ ] Apify rotated all API tokens after security incident #NPB #NKST #DCKT #id:T0155
  → David or Claude generate new Apify tokens for each brand account, update the local token files and user-scope Apify MCPs, then restart any scraper or job still using an old token. (David; Gmail davey@, Gmail nolakayaktours@, Gmail doorcountyzip@, Gmail nolapedalbarge@; touched 2026-11-12)
- [ ] Jonah asks if David is changing the existing website #id:T0177
  → David answer Jonah by text on whether he is making changes to the existing website. (David; Text with Jonah Moses; touched 2026-11-13)
- [ ] Jonah: odd 'V1 Pricing' on existing site and member booking issue #id:T0178
  → David look at the V1 Pricing showing on the existing site and the member booking issue Jonah reported, and reply to Jonah. (David; Text with Jonah Moses; touched 2026-11-13)
- [ ] Tile quote for two small sauna rooms in NE Portland, Sean Hyland walk-through #Ebb-Ember #id:T0182
  → David reply to Sean Hyland with a day this week for the walk-through; he is booking about three weeks out. (David; Gmail davey@; touched 2026-11-13)
- [ ] TideBot written log processing failing, Gemini prepaid credits depleted #NKST #id:T0188
  → David top up the Google AI Studio prepaid credits so TideBot can process guide logs again; until then logs like Michelle Healey's Nov 14 log need manual reading. (David; Slack #the-helm, Slack #new-orleans-kayak-swamp-tours; touched 2026-11-15)
- [ ] Loop health: 15 of 147 scheduled jobs failing, including Comms Radar Send and Command Center #id:T0200
  → David or Claude check the failing jobs on mbp-2, starting with Comms Radar Send (last ran Oct 30), Command Center (Oct 31), Cc V2, Google Ads Optimizer (exit 1) and Docuseal 8442 Watch (Oct 26). (David; Gmail dwrack81@ (DJL Daily); touched 2026-11-16)
- [ ] TideBot written log processing failing, Gemini prepay credits depleted #NKST #id:T0207
  → David top up the Gemini API prepaid credits in AI Studio so TideBot can process written logs again; until then logs like Stephanie's Nov 16 post need manual processing. (David; Slack #the-helm; touched 2026-11-16)
- [ ] AKT winter plan catch-up: NYE fireworks tour, sell vans, Viator return #AKT #id:T0210
  → David set a time to catch up with AKT on the winter plan: NYE fireworks tour (50-60 guests, about 3-4k profit), bring back Sunset Skyline, sell both vans for 1-2k, get back on Viator, and a membership of about $90 minimum. (David; Gmail dwrack81@; touched 2026-11-17)
- [ ] TideBot written log processing failing, Gemini prepayment credits depleted #NKST #id:T0221
  → David top up the Gemini prepaid credits in AI Studio billing so TideBot can process written logs again; until then logs like today's NKST post need manual processing. (David; Slack #the-helm; touched 2026-11-17)
- [ ] Proposed deal points, HD Clinton and Macadam note, Todd Key at JTK Law #id:T0229
  → David and Davey answer Todd Key's two questions: are you still good with the deal, and do you want to proceed with the Macadam filing; his lawyer's only remaining ask is 14 days between closing of the HD Clinton/member interest transaction and the Macadam note due date. (David; Gmail dwrack81@; touched 2026-11-18)

## Waiting on someone

- [ ] NPB content push #NPB #waiting #due:2026-10-31 #id:T0008
  → Kelly post content from today's trips; Davey asked again today. (Kelly; Slack #nola-party-barge; touched 2026-11-13)
- [ ] TideBot W-9 reminders overmessaging NKST crew, River b. complaint #NKST #waiting #due:2026-11-06 #id:T0055
  → Nothing for David. Davey already told TideBot to stop messaging signed guides and stay on Slack; Claude checks that W-9 nudges stay quiet (no overnight sends) until Fri Nov 6. (TideBot / Claude; Slack #the-helm, Slack #new-orleans-kayak-swamp-tours; touched 2026-11-03)
- [ ] Jonah presses Todd for deal-points update and summary judgment motions #waiting #due:2026-11-16 #id:T0167
  → Todd sends Jonah an update by Monday on Drew's response to the 11/4 structure and whether summary judgment motions are filed in both suits. (Todd; Gmail dwrack81@; touched 2026-11-12)
- [ ] Update address to 2105 Paris Road everywhere #waiting #due:2026-11-16 #id:T0059
  → Jeffrey Chitek update the address to 2105 Paris Road across listings and accounts this Monday, Nov 16, per Davey. (Jeffrey Chitek; Slack #nola-party-barge; touched 2026-11-14)
- [ ] NPB corporate holiday push: managers review pages and email before it goes to 105 companies #NPB #waiting #due:2026-11-17 #id:T0195
  → NPB managers walk through the holiday page, corporate page and test email, then reply in #helm-npb by noon Tuesday 11/17 with yes or no on the costume closet, trivia, karaoke and yard games, drinks and bartender with $10 corkage, the $59 pp 40-guest Mon-Thu package, the food, band and singer prices, and the quote builder. (NPB managers; Slack #helm-npb, Gmail nolapedalbarge@; touched 2026-11-16)
- [ ] NPB crew W-9 collection, signed form due Nov 20 #NPB #waiting #due:2026-11-20 #id:T0165
  → NPB crew sign the W-9 and reply done in Slack by Nov 20 so TideBot can check them off for 2026 1099s. (NPB crew; Slack #helm-npb; touched 2026-11-12)
- [ ] Elevated Tides permit extension, permit expires Nov 23 #waiting #due:2026-11-23 #id:T0222
  → Wait for the permit office to process Jonah's extension request on permit 26-035226-000-00-MT before it expires Mon Nov 23. (Jonah Moses; Gmail davey@; touched 2026-11-17)
- [ ] NKST rest-of-year guide schedule #NKST #waiting #id:T0005
  → Guides reply with days per week they can work and days they cannot, and claim open shifts like Abbie's Fri Nov 20 2pm; Davey then sets the schedule. (Davey; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-05)
- [ ] Deactivate JT Sides accounts (Slack, Gmail, FareHarbor and more) #NPB #waiting #id:T0074
  → Jeff confirm JT Sides is removed from FareHarbor and any other logins and, with admin access, sign him out of the NPB Gmail account. (Jeffrey Chitek; Text with Michael Fischer; touched 2026-11-06)
  > David: he is out. ask jeff if he is removed from fh, etc. and maybe logged out of the npb gmail account thru admin settings.
  > David: Approved a reply from the Command Center: Hey Jeff, JT Sides is out at NPB. Can you check that he's been removed from FareHarbor and anything else he had a login for? Also, if you have admin access, can you sign him out of the NPB Gmail accou
  > Radar: Noted that JT is out. The next move is Jeff confirming his FareHarbor removal and signing him out of the NPB Gmail through admin settings.
- [ ] WaterStrong Friday Sunrise sessions: additional insured and certificate #waiting #id:T0103
  → Max add WaterStrong as additional insured on the Capitol policy for Nov 1 to Dec 31, then Jonah sends Dena the certificate; Dena signs and returns the agreement. (Max McCuddy; Gmail davey@; touched 2026-11-06)
- [ ] Inkle bookkeeping refund, pre-Sept 8 payments ($5,229+) #DCKT #waiting #id:T0014
  → DCKT staff email Stretto to confirm the claim was received, since Chris Seablom says he cannot see the claims. (DCKT staff; Gmail doorcountykayaking@; touched 2026-11-09)
- [ ] Switch Verizon plans for new phones with Michael #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #waiting #id:T0127
  → Michael Fischer switch the Verizon plans so David can get the new phones. (Michael Fischer; Text with Michael Fischer; touched 2026-11-09)
- [ ] Michael asks to set up SMS text request for all New Orleans businesses, and OpenCX fix plan #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #waiting #id:T0038
  → Wait for Cody's reply to the SMS verification email, then David answers the OpenCX Fix Plan approve boxes and gives Michael the four safety facts. (Cody; Gmail dwrack81@; touched 2026-11-10)
  > David: sent cody email and waiting on his response.
  > Radar: Noted that you emailed Cody and are waiting on his reply. I moved this to waiting; the OpenCX boxes and the four safety facts for Michael are still open.
- [ ] NPB voucher reply to angry Halloween tiki guest, draft sent to Jeffrey for review #NPB #waiting #id:T0146
  → Jeffrey text David back OK or his changes to the draft reply; David then fills in the voucher amount or option before it goes out. (Jeffrey Chitek; Text with Jeffrey Chitek; touched 2026-11-10)
- [ ] Tile guy $1500 deposit check, needs Ebb & Ember checkbook #waiting #id:T0149
  → Jonah bring the Ebb & Ember checkbook or send a check with L so David can hand the tile guy the $1500 deposit. (Jonah Moses; Text with Jonah Moses; touched 2026-11-11)
- [ ] Elevated Tides Experience ACORD 126 DocuSign voided, to be updated and resent #waiting #id:T0150
  → Wait for Max McCuddy to send the updated ACORD 126 agreement for Elevated Tides Experience, then sign it. (Max McCuddy; Gmail davey@; touched 2026-11-11)
- [ ] Sergei gas line across the deck and tile work, no date or reply yet #waiting #id:T0174
  → Sergei reply with a start date on the gas line, now planned as one straight shot across the deck; Jonah asks Grant about the grout size, and David leans 1/16 inch. (Sergei; Text with Jonah Moses; touched 2026-11-13)
- [ ] Insurance premium audit portal access code not arriving, policy BR20250485 #waiting #id:T0176
  → Jonah request the access code and call the OSI audit hotline right away, since codes expire in 60 minutes; check spam and try an alternate email. (Jonah Moses; Gmail davey@; touched 2026-11-13)
- [ ] NKST W-9 collection for 1099 guides, 2 still open #NKST #waiting #id:T0066
  → Remaining 2 guides complete their W-9s so TideBot can file them; Bob Drought is out until Nov 23. (TideBot; Gmail nolakayaktours@, Slack #helm-nkst; touched 2026-11-15)
- [ ] Elevated Tides insurance premium audit, portal codes expire before arriving #waiting #id:T0194
  → Wait for the insurer to accept Jonah's emailed audit package (monthly sales 11/6/2025 to 10/31/2026, P&L by month, principals) for policy BR20250485, since portal codes arrive about two hours late and expire. (Jonah Moses; Gmail davey@; touched 2026-11-15)
- [ ] NKST crew asking about tour pay #NKST #waiting #id:T0053
  → Whoever approves TideBot payroll verify the unverified PayPal accounts for Emily Clarke and Michelle Healey, then react to release the Nov 1-15 payroll ($2,050 across 5 guides); it only produces a send list and does not move money. (NKST manager; Slack #helm-nkst; touched 2026-11-16)
- [ ] Kick off Cloudflare domain migration for all business domains #id:T0198
  → Someday item: run the Cloudflare migration when David has a free hour. Not urgent. (David; Gmail dwrack81@ (Google Calendar); touched 2026-11-16)
- [ ] Party invite headcount: staff, plus ones, and others #waiting #id:T0204
  → Jeffrey Chitek answer David on who is invited to the party: staff, a +1 each, and anyone else. (Jeffrey Chitek; Text with Jeffrey Chitek; touched 2026-11-16)
- [ ] Elevated Tides: Dustin's competing sauna building and deal timeline #waiting #id:T0212
  → Todd answers Jonah on the timeline for the notes, whether the HD Clinton and Macadam summary judgment motions are filed, and whether Dustin agreed to any of the 11/4 structure. (Todd; Gmail dwrack81@; touched 2026-11-17)
- [ ] Elevated Tides buyout term sheet, Miller/Seaworthy interests and HD Clinton note #waiting #id:T0216
  → Wait for Dustin's lawyer to confirm the 14 day buffer means the 14 day deadline to pay Macadam after initial closing, then execute the revised term sheet. (Dustin's lawyer; Gmail dwrack81@; touched 2026-11-17)
- [ ] Jonah deal terms with Todd: HD Clinton motion, term sheet amount, Macadam payment #waiting #id:T0218
  → Todd confirm whether Dustin's lawyer accepted $125,000 or $100,000, add the clawback line from 11/4, and give the exact date Dustin's 23 days run out on the motion. (Todd; Gmail dwrack81@; touched 2026-11-17)
- [ ] Contrast Therapy API access question, Gene Cripps #waiting #id:T0226
  → Davey answer Gene Cripps on what he wants to achieve with API access, since they have no open API. (Davey; Gmail davey@; touched 2026-11-18)

## Open

- [ ] Bike Bar text lead for two seats tonight #NOLA-Bike-Bar #due:2026-10-30 #id:T0012
  → Bike Bar team reply to the texter today with tonight's availability for two seats. (NOLA Bike Bar team; Gmail nolabikebars@ (Google Voice text); touched 2026-10-30)
- [ ] NKST Manchac tours missing trip logs and guide assignment #NKST #due:2026-10-30 #id:T0019
  → NKST guides post the written logs still missing for the Nov 14 11:30 AM and Nov 13 1:30 PM tours; today's Nov 17 11:30 log is posted but TideBot could not process it. (NKST guides; Slack #new-orleans-kayak-swamp-tours, Slack #the-helm; touched 2026-11-17)
- [ ] NPB guest asks to switch to the Twerkin Tiki boat #NPB #due:2026-10-31 #id:T0024
  → NPB team reply to Lexus Williams on whether they can move to the Twerkin Tiki boat, which departs at 1pm today with 13 passengers. (NPB team; Gmail nolapedalbarge@; touched 2026-10-31)
- [ ] AKT Hines family running late, asking how to reach guide #AKT #due:2026-10-31 #id:T0026
  → AKT staff text the Hines family back today to confirm the meet point at 200 East Riverside Drive, tell them how to reach the guide, and hold the tour for their 6:06 PM arrival if it fits. (AKT staff; Gmail austinkayaktours@ (Google Voice texts); touched 2026-10-31)
- [ ] GetYourGuide refund request, Austin Bat Bridge Oct 30 start time change #AKT #due:2026-11-02 #id:T0010
  → AKT staff reply to GetYourGuide with an explanation and any evidence of the 18:30 to 18:00 start change for booking GYG83W8G5773 (4 guests) within 72 hours, or the refund goes through in full. (AKT staff; Gmail austinkayaktours@; touched 2026-10-30)
- [ ] NKST guest cancels Nov 3 morning tour, booking 388637098, asks insurance refund #NKST #due:2026-11-03 #id:T0036
  → NKST staff cancel booking 388637098 for tomorrow morning and process the refund, since the guest added the insurance fee. (NKST manager; Gmail nolakayaktours@; touched 2026-11-02)
- [ ] TideBot weekend pacing push, Nov 6-8, all brands, reply due tonight #NPB #NKST #DCKT #HPB #BBK #AKT #LSKT #due:2026-11-04 #id:T0065
  → Each brand manager reply in their TideBot thread by tonight with the play for the softest weekend day: NPB (-45% guests), HPB (-80%), AKT (-50%), NKST (-20%) and DCKT (0 on the books); BBK has no baseline and needs a judgment call. (brand managers; Slack #helm-npb, Slack #helm-nkst, Slack #helm-dckt, Slack #helm-hpb, Slack #helm-bbk, Slack #helm-akt; touched 2026-11-04)
- [ ] NPB corporate party pricing draft, needs Barbo's and Beatty's costs before tomorrow's meeting #NPB #due:2026-11-06 #id:T0081
  → Jeffrey send Barbo's prices and Beatty's rate so TideBot can finalize the corporate party pricing before the Nov 6 meeting; Jeffrey says BBQ add-on is $20-30 per person ($20 for 2 proteins and sides, $30 for 3). (Jeffrey Chitek; Slack #helm-npb; touched 2026-11-05)
- [ ] NKST selling 2019 van, down to 3 vans, rear right tire needs replacing #NKST #due:2026-11-06 #id:T0100
  → Jeffrey check the 2019 van's rear right tire tonight and fix it before the sale. (Jeffrey Chitek; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-06)
- [ ] Stan Ventures AI visibility pitch to Houston Pedal Barge, call proposed Nov 10 #HPB #due:2026-11-10 #id:T0109
  → HPB manager decide whether to take the Tuesday Nov 10 10:15 AM Eastern call with Stan Ventures; someone replied 'Yes' to the cold pitch, so a response is expected. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-08)
- [ ] NKST 9am Nov 10 tour has only two guests, Emily asks to cancel #NKST #due:2026-11-10 #id:T0135
  → NKST manager tell Emily whether to cancel the 9am tour tomorrow with two guests and contact those guests; Emily offered to reach out. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-10)
- [ ] Connor + Michael meeting invite, Q4 pace and TX ad spend #AKT #LSKT #due:2026-11-10 #id:T0141
  → Send the Connor and Michael invite on Q4 pace and TX ad spend now without waiting for David's tick; owner is the Claude session that holds the calendar access. (Claude; Todo comment; touched 2026-11-10)
  > David: why didn’t you send the invite. i hate when i ask you to do something and then you take a long time and then come back and ask me , should i send it? Ive already walked away from my computer and then it doesn’t get done.wtf claude
  > Radar: I can't send invites from the ledger. I've changed the next move to send it now with no tick needed, and cleared the needs-you flag. Sorry about the wait.
- [ ] AWS SES DKIM disabled for neworleanskayakrental.com #NKST #due:2026-11-11 #id:T0106
  → Whoever manages the neworleanskayakrental.com DNS restore the SES DKIM records within 5 days, unless removing them was intentional. (David; Gmail doorcountyzip@; touched 2026-11-06)
- [ ] NPB guest booked for today, wants to move it to tomorrow #NPB #due:2026-11-11 #id:T0147
  → NPB team move K Iu's booking from today to tomorrow, same type, and confirm to the guest. (NPB team; Gmail nolapedalbarge@; touched 2026-11-11)
- [ ] AKT guest asks when to arrive for today's bat bridge tour #AKT #due:2026-11-12 #id:T0156
  → AKT staff reply to Leah Roberts before the tour with a recommended arrival time for the 5:00 pm Sunset Congress Avenue Bat Bridge Tour (sunset is 5:35 pm), booking 391033626, 3 guests. (AKT staff; Gmail austinkayaktours@; touched 2026-11-12)
- [ ] NKST guest asks if a dry bag is provided, tour this afternoon #NKST #due:2026-11-12 #id:T0164
  → NKST staff reply to Janet Walker today on whether a dry bag is provided before her afternoon tour. (NKST staff; Gmail nolakayaktours@; touched 2026-11-12)
- [ ] NKST waiver indemnification changes requested by Freddie Skarbek, Manchac tour Nov 12 #NKST #due:2026-11-12 #id:T0166
  → NKST manager reply to Freddie Skarbek on whether the email exchange counts as part of his waiver, and decide whether to accept his limit that he only indemnifies GT for his own acts, before his 2:00 pm tour today. (NKST manager; Gmail nolakayaktours@; touched 2026-11-12)
- [ ] NPB private party cruise inquiry, Nov 14, 12-15 people, 2pm #NPB #due:2026-11-14 #id:T0079
  → NPB team reply to Sam Boscoe before tomorrow's 2pm Party Queen cruise (Bayou Boogie is booked, $350 deposit) on whether NPB offers pickup and drop-off, or recommend a transport company. (Jeffrey Chitek; Gmail nolapedalbarge@; touched 2026-11-13)
- [ ] AKT guest asks if 7am sunrise tour Nov 15 is canceled for storms #AKT #due:2026-11-15 #id:T0187
  → AKT staff reply to Faith Eherts right away on whether the 7am sunrise tour runs given the rain and lightning forecast, and whether she can move to the next available tour. (AKT staff; Gmail austinkayaktours@; touched 2026-11-15)
- [ ] Airbnb Experiences insurance/license documents due Nov 16, NKST listings #NKST #due:2026-11-16 #id:T0027
  → NKST manager upload updated license and insurance documents to Airbnb's partner Evident for both listings (Plantation and Kayak Tour with Cajun food Stop, Paddle Through New Orleans' Beautiful Wetlands) before Nov 16, or the listings get paused and later bookings are cancelled. (NKST manager; Gmail nolakayaktours@; touched 2026-10-31)
- [ ] OpenAI ChatGPT Ads outreach to NKST, 30 min call on David's calendar Nov 16 #NKST #due:2026-11-16 #id:T0162
  → David confirm whether he or staff booked the Nov 16 9am PST Calendly call with Mehmet Guzel; cancel it if not, since the invite came from an unknown sender and mentions only New Orleans Kayak Swamp Tours. (David; Gmail nolakayaktours@, Gmail dwrack81@; touched 2026-11-12)
- [ ] GetYourGuide refund request, Houston Sunset Skyline Kayak Nov 11 flood cancellation, booking GYG2Q87263FV #AKT #LSKT #due:2026-11-16 #id:T0173
  → AKT/LSKT staff reply to GetYourGuide within 72 hours with the Nov 11 flooding cancellation explanation and any proof of the phone call or notice to the guest, or the full refund goes through. (AKT staff; Gmail austinkayaktours@; touched 2026-11-13)
- [ ] David's New Orleans trip: Tuesday HR sit-down with Jeffrey, Piety work Wednesday #NKST #due:2026-11-17 #id:T0202
  → David and Jeffrey Chitek hold an HR sit-down on the computer Tuesday evening Nov 17; David lands around midnight, does the Pool Spa Deck conference Tuesday and Piety work Wednesday morning before Michael Fischer arrives around noon. (David; Text with Jeffrey Chitek; touched 2026-11-16)
- [ ] GetYourGuide refund request, Houston Kayak and Paddleboard Rental Nov 15, guest says activity canceled #AKT #LSKT #due:2026-11-18 #id:T0192
  → AKT/LSKT staff reply to GetYourGuide with an explanation and any evidence for booking GYGVN2X9MHGF (2 guests, Nov 15 5:00 PM) within 72 hours, or the refund goes through in full. (AKT staff; Gmail austinkayaktours@; touched 2026-11-15)
- [ ] Hospice House asks NPB for silent auction items or food vendors, Nov 19 event #NPB #due:2026-11-19 #id:T0083
  → NPB manager decide whether to donate a gift card or item for the Nov 19 Wine and Dine with Hospice silent auction, or ignore. (NPB manager; Gmail nolapedalbarge@; touched 2026-11-05)
- [ ] Fairmont New Orleans Prestige Magazine meeting confirmation, Nov 19 8 AM #NPB #due:2026-11-19 #id:T0227
  → NPB manager check whether anyone actually booked this Nov 19 8 AM Fairmont meeting; it reads like a paid advertorial pitch, so skip it unless the team asked for it. (NPB manager; Gmail nolapedalbarge@; touched 2026-11-18)
- [ ] Texas Sales and Use tax return due Nov 20, AKT #AKT #due:2026-11-20 #id:T0085
  → AKT manager or whoever files taxes file the Texas Sales and Use return for the period ending 10/31/2026 electronically by Nov 20. (AKT manager; Gmail austinkayaktours@; touched 2026-11-05)
- [ ] NKST guide needed for Fri Nov 20 2pm tour, Alexis Hingle out #NKST #due:2026-11-20 #id:T0171
  → NKST manager find another guide for the Fri Nov 20 2pm tour and reassign it in FareHarbor. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-13)
- [ ] GetYourGuide guest asks how to add transportation, Manchac tour Nov 26 #NKST #due:2026-11-26 #id:T0220
  → NKST staff reply to Catherine Zhang via GetYourGuide to confirm whether transportation was selected on her Nov 26 11:30 am booking and how to add it. (NKST manager; Gmail nolakayaktours@; touched 2026-11-17)
- [ ] AKT Texas boat registration renewal, $110 due Nov 30 (Trident Pontoons 35ft) #AKT #due:2026-11-30 #id:T0075
  → AKT manager renew the Texas Parks and Wildlife registration for the 2021 Trident Pontoons (TX 8632KS) online, by mail or in person before Nov 30. (AKT manager; Gmail austinkayaktours@; touched 2026-11-04)
- [ ] Apres Assets GL and marina liability quotes, policy ends 12/27 #due:2026-12-01 #id:T0060
  → Michael or David complete the 11-page supplemental application for the boat slip rental coverage and return it to Shelley Zahn; compare incoming quotes against the first GL quote of $8,883.25 per year. (Michael Fischer; Gmail doorcountyzip@; touched 2026-11-18)
  > David: ask our old apres assets insurance for our loss runs via email and when it comes in forward it to the two agents were working with right now.
  > David: Approved a reply from the Command Center: Hi, Could you send over current loss runs for Apres Assets for the policy period(s) you covered us? We're getting a new general liability quote and the agents need them. If you need a policy number
  > Radar: Noted. I set it to waiting on the old insurer's loss runs, and your next step is forwarding them to the two agents when they arrive. I can't send the email myself.
- [ ] Seabrook Tree Lighting vendor applications, Dec 3, $10 fee #HPB #due:2026-12-03 #id:T0206
  → HPB manager decide whether to apply as a vendor for the Dec 3, 6-8pm Seabrook Tree Lighting ($10 fee), or ignore. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-16)
- [ ] NPB captain bench after newest captain scraped the Freaky Tiki #NPB #due:2026-12-14 #id:T0208
  → Jeffrey build a vetted backup captain list and sign up for the Dec 14 OUPV course; David wants an extra hire or cross-trained crew who can captain and alternate trips. (Jeffrey Chitek; Text with Jeffrey Chitek; touched 2026-11-16)
- [ ] Maritime Consortium drug-free vessel membership renewal, NPB and HPB, expires Dec 31 #NPB #HPB #due:2026-12-31 #id:T0040
  → NPB and HPB managers renew the Maritime Consortium memberships (accounts 23624 and 25143) before Dec 31 using the corrected company-specific renewal links in the Nov 2 emails, not the earlier link. (NPB and HPB managers; Gmail nolapedalbarge@, Gmail houstonpedalbarge@; touched 2026-11-02)
- [ ] Door County property tax due Dec 31, 8442 State Hwy 42 #DCKT #due:2026-12-31 #id:T0199
  → If no bill has arrived by Dec 20, assume it went to Truist and call the Town of Gibraltar; pay by Dec 31 to land on the 2026 return. (David; Gmail dwrack81@ (Google Calendar); touched 2026-11-16)
- [ ] AKT booking cancellation, Heather Bouse Oct 31 bat bridge tour #AKT #id:T0004
  → AKT staff cancel booking #381838130 (2 people, Oct 31 6:00pm Sunset Congress Avenue Bat Bridge Tour) and confirm to the guest. (AKT staff; Gmail austinkayaktours@; touched 2026-10-30)
- [ ] Cell tower lease at 2101 Paris Road marina #DCKT #id:T0006
  → David review the cell tower notes and 4-week plan and decide whether to pursue. (David; Gmail doorcountyzip@; touched 2026-10-30)
- [ ] NPB party boat inquiry, Nov 21 60th birthday, 10 guests #NPB #id:T0013
  → NPB team reply to Jessica Jackson on whether the 2 eighteen-year-olds mean she has to rent the whole boat, with Nov 21 availability and pricing for 10 guests. (NPB team; Gmail nolapedalbarge@; touched 2026-10-30)
- [ ] TripAdvisor bookings not passing transportation info, NKST #NKST #id:T0022
  → NKST manager check how TripAdvisor bookings are mapping transportation details into FareHarbor and fix the setup. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-10-31)
- [ ] HPB New Year's Eve boat party inquiry #HPB #id:T0029
  → HPB team reply to Jordan Henderson on Dec 31 availability, entertainment, party packages and activities. (HPB team; Gmail houstonpedalbarge@; touched 2026-11-01)
- [ ] Tourist directory offers to list Cave Point discount #Cave-Point #id:T0030
  → Cave Point staff decide whether to say yes to listing the up-to-30% discount on Tourist, then reply. (Cave Point staff; Gmail cavepointpp@; touched 2026-11-01)
- [ ] Bike Bar text lead, party of 8 on Twerkin Tiki Nov 27 #NOLA-Bike-Bar #NPB #id:T0032
  → NPB or Bike Bar team reply to the texter with Twerkin Tiki availability and pricing for 8 people on Friday Nov 27. (NPB team; Gmail nolabikebars@ (Google Voice text); touched 2026-11-01)
- [ ] NPB guest asks to move Jan 23 2027 booking from 2pm to 12pm #NPB #id:T0035
  → NPB team check 12pm availability on Jan 23, 2027 and move booking 389104488 for Sarah Burn, then confirm to her. (NPB team; Gmail nolapedalbarge@; touched 2026-11-01)
- [ ] Plaid corporate quote request, private Manchac airboat tour, 15 guests now Nov 18 morning #NPB #NKST #id:T0037
  → NKST manager reply to Antonin Guibal with Nov 18 morning availability, private tour pricing for 15 adults, pickup from The Roosevelt at 8:30 AM, deposit and weather terms; the request landed in the NPB inbox. (NKST manager; Gmail nolapedalbarge@; touched 2026-11-02)
- [ ] AKT Meta ad account dark 10+ days in peak bat season #AKT #LSKT #id:T0039
  → Check billing on the Meta ad account for AKT and get ads running again; AKT now runs as a front door into the Lone Star funnel. (AKT manager; Slack #helm-akt; touched 2026-11-02)
- [ ] Text lead: are the party barges still full in December #NOLA-Bike-Bar #NPB #id:T0044
  → NPB or Bike Bar team reply to the texter with December party barge availability. (NPB team; Gmail nolabikebars@ (Google Voice text); touched 2026-11-02)
- [ ] Review removal offer for Acacia Golson boat breakdown review, NPB #NPB #id:T0045
  → NPB team decide whether to engage this paid-looking review removal offer; reply to the Acacia Golson review publicly instead if it is not already answered. (NPB team; Gmail nolapedalbarge@; touched 2026-11-02)
- [ ] NKST booking 389092376, party shrinks from 10 to 9 on Nov 28, refund asked #NKST #id:T0046
  → NKST staff reduce booking 389092376 to 9 guests for Sat Nov 28 and refund one person if policy allows, then confirm to Axel Holm. (NKST staff; Gmail nolakayaktours@; touched 2026-11-02)
- [ ] NKST content creator collab, Sydney Lee (North Georgia, family in New Orleans) #NKST #id:T0048
  → NKST manager reply to Sydney Lee with what NKST has in mind for the collaboration and propose a call. (NKST manager; Gmail nolakayaktours@; touched 2026-11-02)
- [ ] NPB boat cruise inquiry Dec 4 surprise family outing, asks about fishing #NPB #id:T0051
  → NPB team reply to Lamar Steve Terri with Dec 4 availability and note that fishing is or is not offered. (NPB team; Gmail nolapedalbarge@; touched 2026-11-03)
- [ ] Boss Be Luxury Ride transport partnership pitch, NPB #NPB #id:T0052
  → NPB manager decide whether to reply to Boss Be Luxury Ride about group terms and a jointly sold offer, or ignore it. (NPB manager; Gmail nolapedalbarge@; touched 2026-11-03)
- [ ] Dash cam plan: Garmin 67W with Vault auto-upload #DCKT #id:T0054
  → David decide whether to buy a Garmin dash cam and check whether Vault clips can auto-download to iCloud daily, which is unverified. (David; Gmail doorcountyzip@; touched 2026-11-03)
- [ ] NKST black transit van wipers and washer fluid not working #NKST #id:T0061
  → NKST manager get the black transit's washer fluid dispenser fixed and the driver's side wiper blades replaced. (NKST manager; Slack #new-orleans-kayak-swamp-tours, Slack #the-helm; touched 2026-11-03)
- [ ] Boat Rentals Houston follow-up asking for an offer #HPB #id:T0064
  → HPB manager decide whether to answer Brendon Ford's request for a best offer on Boat Rentals Houston or ignore it. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-04)
- [ ] GetYourGuide 1-2 star review, Houston Sunset Skyline Kayak Tour #AKT #LSKT #id:T0067
  → AKT/LSKT staff log in to GetYourGuide, read the review and reply publicly. (AKT/LSKT staff; Gmail austinkayaktours@; touched 2026-11-04)
- [ ] Deckhand job description, training, and winter programming with Jeffrey #id:T0071
  → Jeffrey finishes the revised deckhand job description (entertainers and salespeople, commission and tips on upsells, camera-comfortable) and makes a promo video for the party pontune; David and Jeffrey keep tracking projects in the dashboard. (Jeffrey Chitek; Text with Jeffrey Chitek; touched 2026-11-04)
- [ ] Loyola University asks for updated COI, last one expired 6/7/22 #NKST #id:T0073
  → NKST manager request an updated certificate of insurance from the insurance agent and send it to David Young at Loyola Financial Affairs. (NKST manager; Gmail nolakayaktours@; touched 2026-11-04)
- [ ] Sasha Killion asks for transportation from Royal Sonesta for 17, Freaky Tiki Apr 16 2027 #NPB #id:T0080
  → NPB team reply to Sasha Killion with a transportation recommendation from the Royal Sonesta for 17 people for booking 366075171 on Apr 16, 2027. (NPB team; Gmail nolapedalbarge@; touched 2026-11-05)
- [ ] Apply for Elevated Tides trademark #id:T0084
  → David start the Elevated Tides trademark application, since Jonah agreed with a thumbs up. (David; Text with Jonah Moses; touched 2026-11-05)
- [ ] NKST group tour inquiry, Natalie Sklovskaya, ~20 people Jan 30 2027, $55 pp with custom pickup #NKST #id:T0086
  → NKST manager reply to Natalie Sklovskaya to confirm the $55 per person regular Manchac Kayak tour with custom pickup and drop-off at Frenchmen Street for about 20 people on Jan 30, 2027, and tell her how to book; she followed up Nov 5 after no answer since Oct 13. (NKST manager; Gmail nolakayaktours@; touched 2026-11-05)
- [ ] NKST van supplies: bug spray bottles requested, black van fuel #NKST #id:T0087
  → NKST manager buy bottles of bug spray to keep in the van like the sunscreen; Emily will fill up the black van tomorrow, it is just under 3/4 tank. (NKST manager; Slack #new-orleans-kayak-swamp-tours, Slack #the-helm; touched 2026-11-05)
- [ ] NOLA reunion group inquiry for party barge Nov 7 or 8 #NPB #NOLA-Bike-Bar #id:T0003
  → Reply to the texter with Nov 7/8 afternoon or evening availability and pricing for 12-14 people; NPB team to handle, as the lead landed in the Bike Bar inbox. (NPB team; touched 2026-11-06)
- [ ] AKT hosted kayak tour collab offer from travel creator Dylan Goodrich, Nov 24 #AKT #id:T0033
  → AKT staff reply to Sofie by email (she wants to keep it out of phone calls) with available times around Tue Nov 24 and what they need from Dylan and Alex for the free skyline tour for two. (AKT staff; Gmail austinkayaktours@; touched 2026-11-06)
- [ ] Cold funding offers (Arc Advances, Josh Rollins) to Cave Point and DCKT #Cave-Point #DCKT #id:T0091
  → Ignore both; same pattern as the other funding solicitations, send no financial documents. (David; Gmail cavepointpp@, Gmail doorcountykayaking@; touched 2026-11-06)
- [ ] Blink cameras offline: boat, workshop, gas station, palapas, floodlight #id:T0092
  → David or on-site staff check WiFi and power for the offline Blink cameras (Boat, Workshop, Gas station, Palapas, Wired Floodlight). (David; Gmail dwrack81@; touched 2026-11-06)
- [ ] NOLA Sales and Use tax not filed July through October #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #id:T0094
  → David and Michael get Louisiana Sales and Use filing automated through Michael's computer since he has the 2FA, and confirm whether July through October actually filed; David says it should have. (Michael Fischer; Text with Michael Fischer; touched 2026-11-06)
- [ ] NKST gift campaign email abuse reports via amazonses #NKST #id:T0097
  → NKST staff check the gift email send ('A gift for someone who has enough stuff' / 'Gift them the quiet') for spam complaints and make sure complainers are suppressed. (NKST manager; Gmail nolakayaktours@; touched 2026-11-06)
- [ ] Gift card email series with WINTERSWAMP discount code #NKST #id:T0098
  → David send the discount code in the gift card emails after the first few sends; Michael asked whether to include WINTERSWAMP in them. (David; Text with Michael Fischer; touched 2026-11-06)
- [ ] Spam complaints on 'Gift them the quiet' email sent via SES #NKST #id:T0099
  → David check that the Gift them the quiet send has a working hosted unsubscribe link and that complainers are suppressed. (David; Gmail nolakayaktours@; touched 2026-11-06)
- [ ] Elevated Tides boat grabbed by someone, see founders channel #id:T0101
  → David and Jonah sort out the lost boat in the founders channel; details are not in the texts. (David; Text with Jonah Moses; touched 2026-11-06)
- [ ] NKST guide needs XXXL PFDs; Manchac traffic tips #NKST #id:T0105
  → NKST manager check whether XXXL PFDs are available or buy some, and answer Abbie's question on avoiding traffic to Manchac. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-06)
- [ ] Email abuse report on a message sent via amazonses.com, 'Gift them the quiet' #NKST #id:T0107
  → NKST staff or David check which campaign sent 'Gift them the quiet' through Amazon SES and whether the recipient should be suppressed. (NKST staff; Gmail nolakayaktours@; touched 2026-11-06)
- [ ] NPB 40th birthday inquiry, 10-12 people, budget near $400 #NPB #id:T0108
  → NPB team reply to Alexandra Spector with what a party for 10-12 people costs and whether anything fits near $400. (NPB team; Gmail nolapedalbarge@; touched 2026-11-07)
- [ ] Piety St shipping container locked insecurely #NKST #id:T0016
  → NKST manager decide how the Piety container should be locked and tell the guides; guides use the trash can Stephanie placed on the table by the key box and empty it in the outdoor can. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-08)
- [ ] HPB SMS reply: 'Sorry, I can't talk right now' #HPB #id:T0110
  → HPB manager decide whether this reply needs a follow-up text from the HPB number, or just let it drop since the person said they can't talk. (HPB manager; Gmail dwrack81@ (HPB SMS alert); touched 2026-11-08)
- [ ] Buyer asks to purchase one pedal bike from the Bike Bar crew for sale #NOLA-Bike-Bar #id:T0112
  → Bike Bar team reply to Montrell Gooden on whether single bikes are for sale and at what price. (NOLA Bike Bar team; Gmail nolabikebars@; touched 2026-11-08)
- [ ] HPB SMS reply needs a human answer #HPB #id:T0113
  → HPB manager text back the number that replied 'Sorry, I can't talk right now' from the HPB line, or close it out if no follow-up is needed. (HPB manager; Gmail dwrack81@ (HPB SMS); touched 2026-11-08)
- [ ] NKST guide asks ETA on new seats #NKST #id:T0114
  → NKST manager answer Stephanie Lazensky on the ETA for the new seats. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-08)
- [ ] HPB SMS reply: contact says they can't talk right now #HPB #id:T0115
  → HPB manager text the contact back from the HPB number, offering a better time or a text-based answer. (HPB manager; Gmail dwrack81@ (HPB SMS alert); touched 2026-11-08)
- [ ] HPB SMS reply needs a human answer: 'Sorry, I can't talk right now' #HPB #id:T0116
  → HPB manager text the number back from the HPB SMS line to see if they want to reschedule the call or get their question answered by text. (HPB manager; Gmail dwrack81@ (HPB SMS); touched 2026-11-08)
- [ ] NKST Affiliate and Influencer Program signup form submission #NKST #id:T0056
  → NKST manager review the new affiliate/influencer signups and reply or approve. (NKST manager; Gmail nolakayaktours@; touched 2026-11-09)
- [ ] Admire NOLA GitHub Pages deploy failed #Admire-NOLA #id:T0093
  → Whoever maintains the Admire NOLA site check the failed deploy job in GitHub Actions and rerun it; it failed again on Nov 9 (build succeeded, deploy failed). (Admire NOLA site maintainer; Gmail admirenola@; touched 2026-11-09)
- [ ] HPB SMS reply 'Sorry, I can't talk right now' waiting on a human answer #HPB #id:T0117
  → HPB manager text back the number that replied from the HPB line; the same alert has repeated hourly since Nov 8 9pm. (HPB manager; Gmail dwrack81@ (HPB SMS alerts); touched 2026-11-09)
- [ ] Buffalo Bayou Kayak soft demand, $119 booked vs $299 7-day average #BBK #id:T0119
  → Reply do 1 in #the-helm if a BBK repost or quick offer draft is wanted; TideBot brings back any spend or post for a final go. (David; Slack #the-helm; touched 2026-11-09)
- [ ] 11 scheduled loops failing, including Command Center and Comms Radar Send #id:T0120
  → Claude check the failing launchd jobs on mbp-2 (Command Center, Comms Radar Send, NKST Payroll exit 1, Memory Freshness, Docuseal 8442 Watch and others) and restart them. (Claude; Gmail dwrack81@; touched 2026-11-09)
- [ ] Bob Drought: no W-9s on file for NPB contractors, lists 21 Gravity Trails payees over $600 #NPB #NKST #id:T0121
  → NPB manager collect W-9s for the 21 contractors Bob Drought listed as paid over $600 by Gravity Trails in 2026, and send them to him since he has none on file for the names he was asked about. (NPB manager; Gmail doorcountyzip@; touched 2026-11-09)
- [ ] Fake Meta page violation warning to NPB inbox, Google Form link #NPB #id:T0123
  → NPB staff do not click the Google Forms link; check the Facebook page's real status in Meta Business Suite and delete the email. (NPB manager; touched 2026-11-09)
- [ ] NPB inquiry: can a Maine Coon cat join the Swamp Eco Tour, Dec 9-13 #NPB #id:T0125
  → NPB team reply to Mira Bhattacharya on whether a harnessed cat is allowed on the public Swamp Eco Tour or a private boat, any pet fee, and December promotions for two adults. (NPB team; Gmail nolapedalbarge@; touched 2026-11-09)
- [ ] HPB SMS reply needs a human answer #HPB #id:T0126
  → HPB team text the number back from the HPB line and see whether the lead still wants to book. (HPB manager; Gmail dwrack81@; touched 2026-11-09)
- [ ] Ebb & Ember tile setter search, NW Tub & Shower declined #Ebb-Ember #id:T0128
  → Davey send the tile quote request to other Portland tile setters for the two sauna rooms, since NW Tub & Shower is booked full. (Davey; Gmail davey@; touched 2026-11-09)
- [ ] HPB SMS reply needs a human answer #HPB #id:T0129
  → HPB team text back the number that replied 'Sorry, I can't talk right now' from the HPB SMS line. (HPB manager; Gmail dwrack81@ (HPB SMS); touched 2026-11-09)
- [ ] Green Bay Glory soccer partnership pitch, DCKT #DCKT #id:T0130
  → DCKT staff decide whether to take a 15-20 minute meeting with Green Bay Glory about a sponsorship or partnership, or ignore it. (DCKT staff; Gmail doorcountykaking@; touched 2026-11-09)
- [ ] HPB SMS reply needing a human answer: 'Sorry, I can't talk right now' #HPB #id:T0132
  → HPB manager decide whether the 'can't talk right now' reply needs a follow-up text from the HPB SMS number or can be dropped. (HPB manager; Gmail dwrack81@; touched 2026-11-09)
- [ ] NPB booking inquiry, party of 9 on Nov 21, wants a call #NPB #id:T0133
  → NPB team call or reply to Wykeenia Russell about a party of 9 on Nov 21 and answer her questions. (NPB team; Gmail nolapedalbarge@; touched 2026-11-09)
- [ ] HPB SMS reply needs a human answer #HPB #id:T0134
  → HPB manager text back the number that replied 'Sorry, I can't talk right now' from the HPB line, or close it if no follow-up is needed. (HPB manager; Gmail dwrack81@ (HPB SMS); touched 2026-11-09)
- [ ] USPTO-styled notice about DOOR COUNTY KAYAK TOURS trademark application SN 99890274 #DCKT #id:T0062
  → DCKT staff or David verify this notice against the USPTO's own trademark records before replying, clicking anything or paying any fee; it has now arrived in two more inboxes. (David; Gmail doorcountykayaking@, Gmail dwrack81@; touched 2026-11-10)
- [ ] TideBot Gemini API prepayment credits depleted, written log processing failing #id:T0102
  → Switch TideBot to the saved backup Gemini keys so written log processing runs again, then confirm it in Slack; owner is the Claude session on mbp-2. (Claude on mbp-2; Todo comment; touched 2026-11-10)
  > David: i thought we made multipole backup keys for this and saved them. fix it
  > Radar: I can't see the backup keys from the ledger and can't switch anything myself. I've set the next move as swapping TideBot to the saved backup keys on mbp-2 and confirming it in Slack.
- [ ] Sankofa CDC asks what happened to the boat on Sunset Stroll #NKST #id:T0137
  → NKST manager reply to Rashida Ferdinand on the stuck boat and say what NKST will do for the group; the info admin replied that the trailer sank into the mud at the widened launch. (NKST manager; Gmail nolakayaktours@; touched 2026-11-10)
- [ ] Expedia asks AKT to restore rates on three products #AKT #id:T0138
  → AKT manager update rates in Expedia LXPC for City Skyline, Congress Bridge Bats and Sunset Skyline tours, or send Krish the retail price per person. (AKT manager; Gmail austinkayaktours@; touched 2026-11-10)
- [ ] Sankofa CDC asks whether NKST checked the launch before Sunset Stroll boat; trailer sank in mud #NKST #id:T0140
  → NKST manager reply to Rashida Ferdinand on whether anyone checked the graded launch Monday, now that Sankofa added crushed concrete and graded it with a bobcat, before the Sunset Stroll boat is finalized. (NKST manager; Gmail nolakayaktours@; touched 2026-11-10)
- [ ] NKST trailer handle missing after Nov 10 Manchac tour, replacement needed #NKST #id:T0143
  → NKST manager tell Stephanie Lazensky whether to buy the replacement trailer handle herself and be reimbursed or send the link, since Michelle's card is no longer in the key box. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-10)
- [ ] NKST kayak seats broken or missing, trailer handle missing #NKST #id:T0145
  → NKST manager buy or find replacement seats for the broken tandems, check the shipping storage container first as Davey says there should be spares, and fix the missing trailer handle; Davey will reimburse otherwise. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-10)
- [ ] BBK Meta purchase pixel not firing, HPB conversion tracking also reads $1.00 #BBK #HPB #id:T0020
  → Reply do 1 in #the-helm so TideBot tests the FareHarbor pixel on a live Buffalo Bayou booking page, then fix it and build a purchase-objective campaign for BBK and HPB. (David; Slack #the-helm; touched 2026-11-11)
- [ ] NKST company retreat inquiry, 9-10 people, kayak tour with transport, now Tue Dec 8 #NKST #id:T0078
  → NKST manager reply to Luke Johnson on availability and pricing for a group of 9-10 with transportation; he now offers Tuesday Dec 8, 1:00-5:30, instead of Dec 10. (NKST manager; Gmail nolakayaktours@; touched 2026-11-11)
- [ ] Glass Gala winner wants to schedule Maurepas Swamp guided kayak tour #NPB #NKST #id:T0151
  → NKST manager reply to Colleen Johnson with how to schedule her Glass Gala prize Guided Kayak Tour through Maurepas Swamp; the email landed in the NPB inbox. (NKST manager; Gmail nolapedalbarge@; touched 2026-11-11)
- [ ] Buffalo Bayou Kayak website enquiry form submission #BBK #id:T0152
  → BBK staff open the enquiry in the inbox and reply to the guest, since the notification shows no details. (BBK staff; Gmail buffalobayoukayak@; touched 2026-11-11)
- [ ] NKST Piety lot: white van keys missing, tire gauge needed #NKST #id:T0157
  → NKST manager find the missing white van keys at Piety, buy or place a tire gauge there, and check the black van's low back left tire; Michelle also suggested Jeff bring seats from the marina kayaks in the meantime. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-12)
- [ ] NKST Google Ads at 0.0x tracked ROAS on $72 spend, FareHarbor login expired #NKST #id:T0158
  → Reply do 1 in #the-helm so TideBot pulls NKST search terms and campaign numbers and proposes cuts; the FareHarbor scraper also needs to re-auth for blank bookings. (David; Slack #the-helm; touched 2026-11-12)
- [ ] AWS SES DKIM revoked for neworleanskayakrental.com in us-east-1 #NKST #id:T0159
  → Whoever manages DNS check whether the DKIM records for neworleanskayakrental.com were removed, and confirm the domain is verified in us-west-2, the production SES region, before any send. (David; Gmail doorcountyzip@; touched 2026-11-12)
- [ ] NKST white van rear tire losing air, key pulled from use #NKST #id:T0163
  → NKST manager get the white van's rear tire repaired or replaced; until then guides do not use any van with an air leak and check the tire sensor before driving the black van. (Michelle Healey; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-12)
- [ ] Katy Taylor High School Choir raffle, gift certificate donation pickup #AKT #id:T0168
  → AKT staff reply to Cara Lazenby and email or hand over the gift certificate (package deal agreed in June, about $120 value at each of Buffalo Bayou and Houston Party Barge) for the Madrigal Dinner raffle. (Connor; Gmail austinkayaktours@; touched 2026-11-12)
- [ ] Villalon Combat Sports pay-to-play Instagram shirt feature offer, AKT/LSKT #AKT #LSKT #id:T0169
  → AKT staff ignore or decline; it is a $10 plus branded T-shirt paid spotlight with no reach or booking guarantee. (AKT staff; Gmail austinkayaktours@; touched 2026-11-12)
- [ ] Boat insurance may not cover people on docks and gas station area #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #id:T0175
  → David call the insurance provider to get dock and gas station coverage added to the marine policy, and consider shopping other agents before the boat policy lapses. (David; Text with Michael Fischer; touched 2026-11-13)
- [ ] TideBot written-log processing down, Gemini API credits depleted #NKST #id:T0179
  → David or whoever owns the Gemini AI Studio project top up the prepaid credits so TideBot can process written trip logs again; logs posted meanwhile need manual processing. (David; Slack #the-helm; touched 2026-11-13)
- [ ] Fake Facebook page verification emails to HPB, Google Forms link #HPB #id:T0184
  → HPB staff do not click the Verification Center link; check the real page status inside Meta Business Suite and delete or report the emails. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-14)
- [ ] Text lead: is the tiki boat dog friendly #NOLA-Bike-Bar #NPB #id:T0186
  → NPB or Bike Bar team reply to the texter on whether the tiki boat is dog friendly. (NPB or Bike Bar team; Gmail nolabikebars@; touched 2026-11-14)
- [ ] TideBot Nov 14 daily: NPB return 4.3x under 5x floor, BBK booked $0 #NPB #BBK #LSKT #id:T0189
  → Reply do 1 in #the-helm so TideBot pulls NPB search terms and proposes cuts, and do 2 for a Buffalo Bayou repost or offer draft. (David; Slack #the-helm; touched 2026-11-15)
- [ ] Fake Meta violation warning to NPB page with Google Forms link #NPB #id:T0190
  → NPB manager do not click the Google Forms link or submit page details; check the page's real status in Meta Business Suite and delete the email. (NPB manager; Gmail nolapedalbarge@; touched 2026-11-15)
- [ ] Fake Meta 'page violation' warning to NKST inbox, likely phishing #NKST #id:T0191
  → NKST staff do not click the Google Forms link or enter any Facebook login; check the Facebook page's own Page Quality or Support Inbox in Meta Business Suite to confirm there is no real violation, then delete the email. (NKST manager; Gmail nolakayaktours@; touched 2026-11-15)
- [ ] NKST Manchac + Whitney Plantation inquiry, 3 people, Dec 29-31 #NKST #id:T0193
  → NKST manager reply to Christine Cipriani with availability on Dec 29, 30 or 31 for 3 people (3 singles, or 1 single and 1 tandem) and the morning NOLA pickup time. (NKST manager; Gmail nolakayaktours@; touched 2026-11-15)
- [ ] DCKT travel feature publication shortlist, Mujahid Khan now also pitching NKST swamp story #DCKT #NKST #id:T0018
  → Ignore or reply once for both brands; Mujahid Khan followed up again asking whether to narrow the Cave Point/shipwreck feature to two outlets and quote costs, which points to a paid placement pitch. (David; Gmail doorcountykayaking@; touched 2026-11-16)
- [ ] Admire NOLA and Hidden Adventure Tours Instagram and Threads engage bots logged out #Admire-NOLA #id:T0088
  → Log in to the Admire NOLA Instagram account on mbp-2 (Screen Sharing, admire Chrome profile); the engage bot is paused 24h. Hidden Adventure Threads login still needs checking too. (David; Slack #helm-admire; touched 2026-11-16)
- [ ] Bach Deluxe Travel Bike Bar private rental, party of 12 with a 17-year-old #NOLA-Bike-Bar #NPB #id:T0090
  → NPB or Bike Bar team reply to Tadasay Robinson: can a 17-year-old attend a full Bike Bar buyout for a 21st birthday, with availability and pricing. (NPB team; Gmail nolapedalbarge@; touched 2026-11-16)
- [ ] NPB Nov 15 bookings soft, return 0.7x under 5x floor #NPB #id:T0196
  → Reply do 1 in #the-helm so TideBot drafts a repost or quick offer for NPB; anything that spends or posts comes back for a final go. (David; Slack #the-helm; touched 2026-11-16)
- [ ] HPB random drug test authorization for Dustin Gause, Maritime Consortium #HPB #id:T0201
  → HPB manager pick a business-hours time, then notify Dustin Gause in writing to take the random test at Quest Diagnostics Fry Road in Katy with authorization Q25219822 and a photo ID; call the site first in case it needs an appointment. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-16)
- [ ] BBK corporate Christmas outing inquiry, 9 people, Dec 7 or 8 #BBK #id:T0203
  → BBK manager reply to Sierra Gerondale with private pontoon availability on Mon Dec 7 or Tue Dec 8, pricing, duration, food and drink policy, departure times and weather and cancellation terms for 9 people. (BBK manager; Gmail buffalobayoukayak@; touched 2026-11-16)
- [ ] Hibu rep offers demo for Lone Star Kayak Tours marketing #LSKT #AKT #id:T0205
  → AKT staff decide whether to take Jesse Reynolds' demo or webinar offer for Hibu marketing services, or ignore it, since he has no trial version. (AKT staff; Gmail austinkayaktours@; touched 2026-11-16)
- [ ] HPB cancellation policy shows 7 days on site, should be 72 hours #HPB #id:T0209
  → HPB manager read FareHarbor support's Nov 16 reply Michael forwarded and change the cancellation policy on the booking site from 7 days to 72 hours. (HPB manager; Gmail houstonpedalbarge@, Gmail dwrack81@; touched 2026-11-16)
- [ ] Clear Lake Marine Center invoice 20260937, balance now $5,503.50 #HPB #id:T0069
  → HPB manager confirm the invoice is legitimate and why the balance changed from $4,348.50 to $5,503.50 on a $12,593.00 total, then pay by ACH or check since a card adds 3%. (HPB manager; Gmail houstonpedalbarge@; touched 2026-11-17)
- [ ] AKT private group inquiry, now Wed March 3, 2027, up to 60 people #AKT #id:T0070
  → AKT staff reply to Nesi Junaid on whether a private afternoon outing on Wed March 3, 2027 works, which start times are open, and whether AKT can take up to 60 people; she is only checking availability for a 60-room hotel block. (Connor; Gmail austinkayaktours@; touched 2026-11-17)
- [ ] Michael deep dive on why AdWords and Meta aren't working, wants landing pages and lead magnets #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #id:T0082
  → David ask Claude to pull a report of which keywords are winning and who the competition is, and check what Michael's new ads are targeting. (David; Slack #helm-npb; touched 2026-11-17)
- [ ] NKST vehicle pre/post trip photos missing, accident damage found #NKST #id:T0213
  → NKST guides do a pre and post trip photo or video walk-around of every vehicle, and whoever had the van when the visible damage happened tells Davey so he can report it to insurance. (NKST manager; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-17)
- [ ] NPB alcohol sales manager applicant Amanda Halverson #NPB #id:T0214
  → NPB manager review Amanda's resume and screening answers (score 13/16, has ATC permit, 3+ years, wants $35 an hour, can start Nov 25, flagged for a thin work history answer) and decide on an interview. (NPB manager; Slack #helm-npb, Gmail nolapedalbarge@; touched 2026-11-17)
- [ ] Hiring captains, social media person and bar manager; replacing Sophia and crew #NPB #NOLA-Bike-Bar #id:T0215
  → David keeps running the captain and bar-manager ads, screens the first bar applicant, and settles with Michael whether a captain can also do check-ins and backup captain duty. (David; Text with Michael Fischer, Text with Jeffrey Chitek; touched 2026-11-17)
- [ ] Fake Meta page violation warning to NKST inbox (Google Form link) #NKST #id:T0217
  → NKST staff do not click the Google Forms link or submit anything; check the page's real status in Meta Business Suite, and treat the email as phishing. (NKST manager; Gmail nolakayaktours@; touched 2026-11-17)
- [ ] INNOVATX Events group inquiry, Houston conference Sept 2027, BBK #BBK #id:T0219
  → BBK manager reply to Allegra Zwaan with group size limits, per-person pricing and minimums, tour duration and inclusions for her preliminary proposal. (BBK manager; Gmail buffalobayoukayak@; touched 2026-11-17)
- [ ] Funding solicitations (GreenBridge, Better Loans, HeyLending) claiming approval, DCKT and Cave Point #DCKT #Cave-Point #id:T0011
  → Ignore these and send no bank statements, ID or voided check; Vincent Dorsey of BrightFunds Network is another cold pitch for a Friday call on a funding line, same pattern. (DCKT staff; Gmail doorcountykayaking@; touched 2026-11-18)
  > David: i need to remove my soft credit lock and allow them to push it forward with a credit pull to unlock this.
  > Radar: Noted: you want to lift the soft credit lock so the lender can pull credit. I put that as your next move, and I'd confirm the lender's identity first since the outreach is unsolicited.
- [ ] Apify usage limit hit and API tokens revoked (NPB and doorcountyzip accounts) #NPB #id:T0028
  → David or whoever runs the Apify jobs create new API tokens on both Apify accounts, update every integration that uses them, and renew the usage limit; all tokens were revoked Nov 11-12 after a security incident. (David; Gmail nolapedalbarge@, Gmail doorcountyzip@; touched 2026-11-18)
- [ ] NKST Piety St lot rubble and van whereabouts #NKST #id:T0034
  → Davey finish sorting the Piety parking and debris; trailer handles are already in the storage container at the back of Piety, so none need ordering; guides skip the white van (#3, leaking rear tire, no keys) and take photos or a video walk-around before and after every tour. (Davey; Slack #new-orleans-kayak-swamp-tours; touched 2026-11-18)
- [ ] Gas line install date and permit deadline for Elevated Tides privates #id:T0096
  → Wait for Jonah's update tonight on his BDS call; David still calls Mario for the gas line install date, and the $228 permit extension fee on DevHub is paid before calling in any inspection (permit 26-035226 expires 05/23/2027). (Jonah Moses; Text with Jonah Moses; touched 2026-11-18)
- [ ] Expedia wants rates to relist Austin Kayak tours #AKT #id:T0224
  → Connor send Krish the per-person retail rate and current timings for City Skyline, Congress Bridge Bats Evening and Sunset Skyline tours so he can set them up through the end of 2027. (Connor; Gmail austinkayaktours@; touched 2026-11-18)
- [ ] Shoreside liability coverage at Paris Road, Starnet P&I wording from Gallagher #NPB #id:T0225
  → David read the Starnet P&I clause (page 61 of the attached policy, covers passengers embarking and disembarking via docks and piers at the normal docking area) and check whether any contract for the Paris Road property requires general liability, since John says none is needed if Gravity Trails does not own the property. (David; Gmail nolapedalbarge@; touched 2026-11-18)
- [ ] Bike Bar text lead: does a full buyout require everyone 21+ #NOLA-Bike-Bar #id:T0228
  → Bike Bar team reply to the texter on whether a full buyout requires all guests to be 21+, with availability and pricing. (Bike Bar team; Gmail nolabikebars@ (Google Voice text); touched 2026-11-18)

## Backburner (LSKT)

- [ ] LSKT ad return 1.6x under 2x floor #LSKT #id:T0021
  → Reply do 1 in #the-helm for TideBot to test the FareHarbor pixel on a live Lone Star booking page, or do 2 to walk the funnel. (David; Slack #the-helm; touched 2026-11-17)

## Done (last 14 days)

- [x] GetYourGuide solo guest, Houston Sunset Skyline Oct 31, wants credit note #LSKT #AKT #due:2026-10-31 #done:2026-11-04 #id:T0025
- [x] AKT Riverside Lot parking permit statement $2,082.40 #AKT #due:2026-11-01 #done:2026-11-05 #id:T0002
- [x] Soward v. TripAdvisor hearing date, reply needed #AKT #due:2026-11-03 #done:2026-11-05 #id:T0001
- [x] NKST guest Freddie Skarbek objects to waiver indemnification wording, tour today 2pm #NKST #due:2026-11-12 #done:2026-11-12 #id:T0161
- [x] JTK Law proposed deal points, MSJ and declaration drafts #waiting #due:2026-11-16 #done:2026-11-13 #id:T0170
  > David: do i need to respond? i read it and it looks good. hoping for some closure on this
  > Radar: Nothing in the messages shows a reply is owed from you. Jonah already sent Todd the fixes for the declaration, and Todd says the revised version is headed to your inbox. Bill Drew has not answered the proposal yet, so closure is still waiting on him.
- [x] Progressive commercial auto policy renewal due Nov 16, NKST inbox #NKST #due:2026-11-16 #done:2026-11-17 #id:T0057
- [x] Michael Fischer NOLA trip Nov 16-20, days to tell Jaq #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #due:2026-11-17 #done:2026-11-18 #id:T0043
  > David: i need to use chase points to purchase that ticket
  > Radar: Noted, you'll book the ticket with Chase points. Michael still needs your three-day or two-day answer.
- [x] Alan Jalasjaa in NOLA Nov 15-20, free Thursday evening and Friday morning #NPB #NKST #due:2026-11-19 #done:2026-11-12 #id:T0148
  > David: Closed by the resolver: David replied to Alan inviting him to the Thursday marina party and asking which booth he is at.
  > Radar: Noted, closed. You invited Alan to the Thursday marina party and asked which booth he is at.
- [x] Marina party Thursday Nov 19, sauna vendor Alan invited, booth 2923 at spa conference #due:2026-11-19 #done:2026-11-14 #id:T0185
  > David: Closed by the resolver: David invited Alan to the Thursday marina party and asked his booth; Alan replied 11-14 with booth 2923.
  > Radar: Marked resolved. Alan is invited to the Thursday Nov 19 marina party and gave booth 2923 at the spa conference.
- [x] NKST payroll Oct 16-31 blocked on 3 questions, crew 'mj' needs rate #NKST #done:2026-11-05 #id:T0031
- [x] Marina insurance agent asks for vessel liability details #done:2026-11-13 #id:T0058
  > David: Closed by the resolver: Michael answered Shelley Zahn's boat and slip liability question 11/13 (GT occupies 4 slips, carries its own insurance) and sent loss runs; she said she can pro
  > Radar: Marked resolved. Michael answered the slip liability question and sent loss runs, and the quote work continues under the Apres Assets thread. The separate worry about dock and gas station coverage now has its own thread.
- [x] Certified Travel Media New Orleans brochure distribution offer #NPB #done:2026-11-04 #id:T0068
- [x] Pool Spa Patio Expo in NOLA, David going today #waiting #done:2026-11-04 #id:T0072
- [x] Viator refund processed, NKST Manchac Extended Oct 18, Daria Gerasimova #NKST #done:2026-11-04 #id:T0077
- [x] Jonah asks David to sign Maureen's DocuSign for 9, releases $10k earnest from WFG #done:2026-11-06 #id:T0047
  > David: ive done that awhile ago and i told you i did it. why are you asking again.
  > Radar: You're right, my mistake. I marked it resolved.
- [x] NKST bookings soft, $555 vs $996 7-day average #NKST #done:2026-11-06 #id:T0063
- [x] Automate paying Entergy for 1407 Piety #done:2026-11-13 #id:D0001
  > David: Closed by the resolver: Entergy notice forwarded 11-07 says Your Autopay is scheduled for 12/08/2026, so autopay is already set up.
  > Radar: Noted: the Entergy notice says Autopay is scheduled for 12/08/2026, so no new action here. The $647.20 past due amount is still tracked in T0089.
- [x] Homebase payroll for Oct 26 to Nov 8 due Nov 10 #done:2026-11-10 #id:T0118
  > David: no need to add this to our command center currently. i already mentioned this to you. dckt is seasonal and gt is autmatic. those emails can get auto archived.
  > Radar: Understood. Homebase payroll emails create no thread and I closed this one. They stay noise until W-2s in January. I can't auto-archive the emails from here, so that filter would need to be set in Gmail.
- [x] Jonah asks David to read his Slack message himself (without Claude) #done:2026-11-13 #id:T0131
- [x] NPB and NKST Google Ads show 0.0x tracked ROAS, FareHarbor login expired #NPB #NKST #done:2026-11-13 #id:T0139
  > David: Closed by the resolver: The 11-13 daily shows NPB booked 9 / $2.8k at 7.4x again, so FareHarbor data is flowing after the 0.0x reports of 11-09 to 11-11.
  > Radar: Closed. The 11-13 daily shows NPB booked 9 / $2.8k at 7.4x, so tracking is working again.
- [x] Sign marina approval for Elevated Tides (commercial use and plunge zone, slips 30, 61, 62) #done:2026-11-13 #id:T0142
  > David: Closed by the resolver: David emailed office@elevatedtides.com 'signed marina plan' with an attachment on 11/13 at 16:53, in answer to Jonah's request.
- [x] NPB family reunion inquiry, up to 34 people, late November #NPB #done:2026-11-11 #id:T0050
- [x] All Fuel quote for Warming Trends fire tables and pony wall, floating sauna #Cave-Point #done:2026-11-13 #id:T0153
  > David: Closed by the resolver: All Fuel emailed the estimate for the fire tables and pony wall on 11-11 after Davey said Please on 11-10.
  > Radar: Closed. All Fuel sent the fire tables and pony wall estimate on 11-11.
- [x] Move all domains to Cloudflare as they renew #NPB #NKST #NOLA-Bike-Bar #Admire-NOLA #done:2026-11-12 #id:T0154
  > David: Closed by the resolver: David told Michael 'Were moving all domains over to cloudflare as we renew'.
  > Radar: Noted, closed. Domains move to Cloudflare as each one renews.
- [x] Michael asks which seats to order on Amazon #done:2026-11-18 #id:T0160
  > David: Closed by the resolver: Claude said spare seats from Paris Road go in every van. Davey said he's getting seats from the marina and restocking the vans.
  > Radar: Marked resolved. Claude said spare seats from Paris Road go in every van, and Davey is getting seats from the marina and restocking the vans tomorrow.
- [x] Unsolicited GreenBridge Capital DocuSign funding application #Cave-Point #done:2026-11-15 #id:T0007
  > David: Closed by the resolver: The unsolicited GreenBridge envelope was voided as expired on 11-14; nothing was signed.
  > Radar: Closed. The GreenBridge envelope expired and was voided Nov 14 with nothing signed; I linked it to the related lender thread T0011.
- [x] Vacaxion Cvlt creator retreat, NPB airboat feature Nov 8-12, 10 comp tickets #NPB #done:2026-11-13 #id:T0041
- [x] Anti-slip dock steps options, get Alex's feedback #done:2026-11-13 #id:T0076
  > David: they look good, just need to finish installing them
  > Radar: Noted, the options are approved and the next move is now just finishing the install.
- [x] NKST ad return 0.4x under 5x floor, soft demand #NKST #done:2026-11-17 #id:T0172
  > David: Closed by the resolver: Daily reports show NKST recovered: 9.5x on 11-14 and 12.9x on 11-16 ($740 booked on $57 spend), so the 0.4x soft-demand flag no longer holds.
  > Radar: Marked resolved. The daily reports show NKST at 9.5x on 11-14 and 12.9x on 11-16, so the 0.4x flag no longer applies.
- [x] Roxanne Pauig follow-up on sauna float outlets quote, Hayden Island #done:2026-11-14 #id:T0180
  > David: Closed by the resolver: Davey replied to Roxanne at Smiley Electric on 11-14 with photos and the updated quote sheet.
  > Radar: Marked resolved. Davey answered Roxanne at Smiley Electric on Nov 14 with photos and the updated quote sheet. It reopens if she sends a new message.
- [x] Elevated Tides slip lease addendum for E&E, needs David's signature #Ebb-Ember #done:2026-11-14 #id:T0181
  > David: Closed by the resolver: David emailed the lease addendum back to office@elevatedtides.com signed for Elevated Tides Experiences LLC at 11-13 21:49, then again at 22:54.
  > Radar: Marked resolved. The signed addendum went back twice on Nov 13, so nothing is left on you unless the other side says they didn't get it.
- [x] NKST booked 0 on $56 spend Nov 13 #NKST #done:2026-11-17 #id:T0183
  > David: Closed by the resolver: The Nov 14 daily shows NKST green, booked 1 / $390 at 9.5x. The Nov 13 zero-booking day did not repeat.
  > Radar: Noted, closed. The Nov 16 daily also shows NKST at 12.9x on $57 spend and 4 bookings, so no repeat.
- [x] Possible buyer approach for Austin kayak operators (Rachel Foster) #AKT #done:2026-11-16 #id:T0197
  > David: Closed by the resolver: Austin Kayak Tours replied to Rachel Foster on 11-16 at 7:22 with 'Sure. 920-344-6641', agreeing to the call with the buyer.
  > Radar: Marked resolved. AKT replied to Rachel Foster agreeing to the call with the buyer, so nothing is open on this beyond the call itself.
- [x] NKST TripAdvisor refund processed, Nov 18 Manchac Extended tour (Alejandro Gallarzo) #NKST #done:2026-11-17 #id:T0223
