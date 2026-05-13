# FareHarbor DNS Request Email — DMARC + SPF for doorcountykayaktours.com

Copy the body below into a fresh email. Send from `doorcountykayaking@gmail.com` (or `dwrack81@gmail.com`) to `support@fareharbor.com`.

---

**To:** support@fareharbor.com
**Subject:** DNS records needed — DMARC + SPF update for doorcountykayaktours.com

Hi FareHarbor support,

Could you add and update two DNS records on `doorcountykayaktours.com`? We're setting up marketing email through Amazon SES and need DMARC plus an SPF include so Gmail will stop sending our mail to spam.

**1. Add a new TXT record:**

```
Host:    _dmarc.doorcountykayaktours.com
Type:    TXT
Value:   v=DMARC1; p=none; rua=mailto:info@doorcountykayaktours.com; fo=1
TTL:     Auto / default
```

**2. Update the existing root SPF record.** The current TXT record on `@` (or `doorcountykayaktours.com`) reads:

```
v=spf1 ip4:184.173.239.120 a mx include:websitewelcome.com ~all
```

Please update it to:

```
v=spf1 ip4:184.173.239.120 a mx include:websitewelcome.com include:amazonses.com ~all
```

Just adding `include:amazonses.com` before `~all`. Keep everything else.

That's it — no other records need changing. The Amazon SES DKIM CNAMEs are already in place and verifying successfully.

Could you let me know once both are live? Should propagate in under a minute on Cloudflare.

Thanks,
David Rack
Door County Kayak Tours

---

## Notes (do not include in the email)

- DKIM is already done — three CNAMEs at `*._domainkey.doorcountykayaktours.com` pointing to `dkim.amazonses.com`. SES confirms they're valid.
- DMARC `p=none` is the safe starting policy. After 1-2 weeks of clean reports we move to `p=quarantine`, then `p=reject`.
- The SPF include adds Amazon's mail servers to the list of authorized senders for the domain.
- Once both records are live, the win-back drip will land in inbox instead of spam.
