# Broken Link Checker - Find 404s, Dead Links & Redirects

Crawl a site and report 404s, dead links and redirect chains.

- Apify Store: [apify.com/tinyrex/broken-link-checker](https://apify.com/tinyrex/broken-link-checker)

## Input used in this example

```json
{
  "startUrls": [
    "https://quotes.toscrape.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~broken-link-checker/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/broken-link-checker).
