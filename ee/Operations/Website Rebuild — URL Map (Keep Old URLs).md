# Website Rebuild: URL Map (keep every old URL)

Rule (Davey, 2026-11-02): every page on the new site keeps the exact URL of the old page it replaces. No renames. Anything retired gets a 301 to its closest new page. Checked live 2026-11-02 (sitemap, live crawl, GSC 16 months, GA4 12 months).

## Pages the new site must serve at the same URL

| URL | Google impressions (16 mo) | Visits (12 mo) | What it becomes |
|---|---|---|---|
| `/` | 26,823 | 12,781 | New homepage |
| `/faq` | 9,146 | 995 | FAQ page (keep FAQPage schema) |
| `/memberships` | 8,944 | 436 | Memberships page |
| `/wellness` | 8,098 | 153 | Wellness page |
| `/shop` | 7,863 | 70 | Gift cards (replaces Sauna Credit per new pricing) |
| `/joinus` | in sitemap | 29 | Keep as-is (join / signup) |
| `/best-saunas-portland` | in sitemap | n/a | Best saunas guide |
| `/privacy` | in sitemap | 1 | Privacy policy |
| `/terms-of-service` | in sitemap | n/a | Terms |

No trailing slash: `/faq`, not `/faq/`. On Cloudflare Pages build each as `faq.html` (served at `/faq`) or set Astro `trailingSlash: 'never'` + `build.format: 'file'`.

## 301 redirects (put in `_redirects` on Cloudflare Pages)

```
/home      /           301
/home/     /           301
/fitness   /wellness   301
/cart      /shop       301
```

`/fitness` already 301s to `/wellness` on Squarespace today; keep it.

## New pages (new URLs are fine, nothing old to protect)
- `/cold-plunge-portland` (top SEO gap)
- `/neighbors` (if neighbor discounts survive)
- Any new page: check this table first so it doesn't collide with an old URL.

## Launch checks
1. After DNS switch, curl every URL above: 200 for pages, 301 for redirects.
2. Remove noindex from the page AND `_headers`.
3. Resubmit the sitemap in Search Console; watch Coverage for 404s for 2 weeks.
4. `/photos.html` is a dev-only picker. Delete before launch.
