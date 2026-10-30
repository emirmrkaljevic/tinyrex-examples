# Bulk Lighthouse Audit - Core Web Vitals, SEO, Accessibility

Run Google Lighthouse on many URLs: performance, SEO, accessibility scores and Core Web Vitals.

- Apify Store: [apify.com/tinyrex/lighthouse-audit](https://apify.com/tinyrex/lighthouse-audit)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-lighthouse-audit-core-web-vitals/)

## Input used in this example

```json
{
  "urls": [
    "https://example.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~lighthouse-audit/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/lighthouse-audit).
