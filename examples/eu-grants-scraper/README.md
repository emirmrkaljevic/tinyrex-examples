# EU Grants Scraper - Horizon Europe & EU Funding Calls

Find open EU funding calls (Horizon Europe, Digital Europe and more) by keyword.

- Apify Store: [apify.com/tinyrex/eu-grants-scraper](https://apify.com/tinyrex/eu-grants-scraper)
- Guide: [eu funding calls horizon europe api](https://emirmrkaljevic.github.io/tinyrex-data-tools/eu-funding-calls-horizon-europe-api/)

## Input used in this example

```json
{
  "keywords": [
    "artificial intelligence"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~eu-grants-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/eu-grants-scraper).
