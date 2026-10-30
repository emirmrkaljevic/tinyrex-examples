# SEC EDGAR Filings Scraper - 10-K, 10-Q, 8-K by Ticker

10-K, 10-Q, 8-K and Form 4 filings by ticker or CIK from the official SEC EDGAR APIs.

- Apify Store: [apify.com/tinyrex/sec-edgar-filings-scraper](https://apify.com/tinyrex/sec-edgar-filings-scraper)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/sec-edgar-api-download-10-k-8-k-filings-csv/)

## Input used in this example

```json
{
  "companies": [
    "AAPL",
    "TSLA"
  ],
  "formTypes": [
    "10-K",
    "8-K"
  ],
  "maxFilingsPerCompany": 5
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~sec-edgar-filings-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/sec-edgar-filings-scraper).
