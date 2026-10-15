# Sitemap Scraper - All URLs from XML Sitemaps + Status Check

List every URL in a site's XML sitemaps, optionally with HTTP status checks.

- Apify Store: [apify.com/tinyrex/sitemap-scraper](https://apify.com/tinyrex/sitemap-scraper)
- Guide: [extract all urls from sitemap](https://emirmrkaljevic.github.io/tinyrex-data-tools/extract-all-urls-from-sitemap/)

## Input used in this example

```json
{
  "startUrls": [
    "https://apify.com"
  ],
  "maxUrlsPerSite": 500
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~sitemap-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/sitemap-scraper).
