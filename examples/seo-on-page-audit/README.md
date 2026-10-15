# SEO On-Page Audit - Title Meta H1 Canonical OG Schema

Audit title, meta description, H1, canonical, Open Graph and schema on a list of pages.

- Apify Store: [apify.com/tinyrex/seo-on-page-audit](https://apify.com/tinyrex/seo-on-page-audit)

## Input used in this example

```json
{
  "startUrls": [
    "https://example.com",
    "https://apify.com"
  ]
}
```

## Run it

Python 3.10+ (`pip install apify-client`):

```bash
export APIFY_TOKEN=your_token
python run.py
```

Node.js 18+ (`npm install apify-client`):

```bash
export APIFY_TOKEN=your_token
node run.mjs
```

No SDK, just HTTP (waits for the run and returns the dataset items):

```bash
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~seo-on-page-audit/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/seo-on-page-audit).
