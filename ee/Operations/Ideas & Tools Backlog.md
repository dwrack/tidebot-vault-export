# Ideas & Tools Backlog

*A running list of things to explore when looking for what to work on next.*

---

## AI & Automation Tools to Explore

### n8n — visual workflow automation
- `github.com/n8n-io/n8n`
- Self-hosted, 400+ integrations (Gmail, Google Drive, webhooks, Claude API)
- **Best use cases for E&E:**
  - Donation requests → auto-generate gift card + draft reply
  - Illness/cancellation emails → auto-issue gift card + draft reply
  - New Google review → notify + draft response
  - Classify incoming emails → route to correct SOP

### Inbox Zero — AI email assistant
- `github.com/elie222/inbox-zero`
- Gmail-native, AI triage, auto-draft, categorization
- Most directly applicable to reducing email management time
- Has a hosted version (no self-hosting required)

### AnythingLLM — chat with your docs/vault
- `github.com/Mintplex-Labs/anything-llm`
- Self-hosted, connects Obsidian vault to an LLM
- Could use SOP & FAQ doc as live knowledge base when drafting replies
- Claude would "know" your policies without re-explaining each session

### Activepieces — lightweight n8n alternative
- `github.com/activepieces/activepieces`
- Easier to self-host, good Gmail connector
- Worth comparing to n8n before committing to one

### MCP Servers (add-ons for Claude Code)
- `github.com/modelcontextprotocol/servers`
- **Puppeteer** — browser automation (e.g., scrape Periode.no dashboard)
- **SQLite** — lightweight local DB for tracking customer interactions/history
- **Slack** — route notifications to Slack if needed

---

## Email Automation Ideas (Fully Automatable)

- **Donation requests** — detect pattern, generate gift card link, send reply, done
- **Illness/same-day cancellations** — auto-issue gift card + templated reply
- **New Google Business reviews** — alert + draft a response for approval
- **Booking reminders** — door code / waiver reminder if waivers unsigned 24hr before session

## Email Workflows (Assisted, Not Automated)
These still need Davey/Jonah judgment — just assisted with drafts:
- Partnership proposals (Willie McBride, Danesh Oleshko type)
- Design/vendor proposals (Jess Astrella type)
- Aspiring operator inquiries

---

## Future Sauna Builds

- **Ducks vs. Beavers rivalry saunas** — build two themed floating saunas playing off the Oregon Ducks vs. Oregon State Beavers football rivalry. One sauna styled to look like a duck, one like a beaver. Strong Oregon identity angle, viral potential, and a natural draw for game weekends and rivalry week.
  - Share on a future call with Jordan and Mack (PR)
  - Share via email with Jess and Hannah when they are onboarded

---

## Other Ideas

- **World Sauna Day (Apr 25–27)** — promo code WORLDSAUNA (20% off) already set up; think about social/marketing push
- **Danesh "Banya Mondays"** — still an open informal arrangement; worth formalizing if Mondays keep growing
- **Periode.no bookkeeping report** — Erik is building a monthly downloadable report; follow up once available to simplify bookkeeper workflow
- **Door code UX** — asked Periode to show door code on waiver page too, not just booking page; follow up if not resolved
- **Gift card → membership payment** — system limitation, in progress with Periode; follow up

---

*Last updated: March 2026*
