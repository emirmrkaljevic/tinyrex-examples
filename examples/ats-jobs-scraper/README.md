# Greenhouse / Lever / Ashby Jobs Scraper - Personio & more

Collect open roles from Greenhouse, Lever, Ashby, Personio and other ATS job boards.

- Apify Store: [apify.com/tinyrex/ats-jobs-scraper](https://apify.com/tinyrex/ats-jobs-scraper)
- Guide: [scrape greenhouse lever ashby jobs](https://emirmrkaljevic.github.io/tinyrex-data-tools/scrape-greenhouse-lever-ashby-jobs/)

## Input used in this example

```json
{
  "companies": [
    "duolingo.com",
    "lever:spotify",
    "https://jobs.ashbyhq.com/ramp",
    "polestar.com",
    "bunq.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~ats-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/ats-jobs-scraper).
