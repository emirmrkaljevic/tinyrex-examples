# SAM.gov & UK Contracts Finder Tenders Scraper

Search US SAM.gov and UK Contracts Finder opportunities in one dataset.

- Apify Store: [apify.com/tinyrex/us-uk-tenders-scraper](https://apify.com/tinyrex/us-uk-tenders-scraper)

## Input used in this example

```json
{
  "sources": [
    "contracts-finder"
  ],
  "keywords": [
    "software"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~us-uk-tenders-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/us-uk-tenders-scraper).
