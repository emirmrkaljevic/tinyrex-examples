# TED EU Tenders Scraper - Public Procurement & Awards

Search EU public tenders and contract awards on TED by keyword, CPV code and country.

- Apify Store: [apify.com/tinyrex/ted-tenders-scraper](https://apify.com/tinyrex/ted-tenders-scraper)
- Guide: [ted tenders api export](https://emirmrkaljevic.github.io/tinyrex-data-tools/ted-tenders-api-export/)

## Input used in this example

```json
{
  "keywords": [
    "software"
  ],
  "cpvCodes": [
    "72000000"
  ],
  "countries": [
    "DE",
    "AT"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~ted-tenders-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/ted-tenders-scraper).
