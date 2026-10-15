# Tech Stack Detector - Bulk Wappalyzer & BuiltWith Alternative

Detect CMS, e-commerce, analytics, CDN and payment tech on a list of domains (lead lists, competitor research).

- Apify Store: [apify.com/tinyrex/tech-stack-detector](https://apify.com/tinyrex/tech-stack-detector)
- Guide: [bulk tech stack lookup wappalyzer alternative](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-tech-stack-lookup-wappalyzer-alternative/)

## Input used in this example

```json
{
  "domains": [
    "wordpress.org",
    "shopify.com",
    "mozilla.org"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~tech-stack-detector/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/tech-stack-detector).
