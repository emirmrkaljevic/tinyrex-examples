# RSS Feed Scraper - RSS, Atom & JSON Feed Reader to JSON/CSV

Turn RSS, Atom or JSON Feed URLs (or plain websites) into clean JSON/CSV.

- Apify Store: [apify.com/tinyrex/rss-feed-scraper](https://apify.com/tinyrex/rss-feed-scraper)
- Guide: [rss feed to json csv api](https://emirmrkaljevic.github.io/tinyrex-data-tools/rss-feed-to-json-csv-api/)

## Input used in this example

```json
{
  "feeds": [
    "https://www.nasa.gov/feed/",
    "https://blog.cloudflare.com/rss/",
    "https://github.com/apify/crawlee/releases.atom"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~rss-feed-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/rss-feed-scraper).
