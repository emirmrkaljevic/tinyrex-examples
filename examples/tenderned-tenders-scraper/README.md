# TenderNed Netherlands Tenders Scraper

Search Dutch public tenders on TenderNed.

- Apify Store: [apify.com/tinyrex/tenderned-tenders-scraper](https://apify.com/tinyrex/tenderned-tenders-scraper)

## Input used in this example

```json
{
  "keywords": [
    "software"
  ],
  "maxResults": 10
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~tenderned-tenders-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/tenderned-tenders-scraper).
