# Workday Jobs Scraper - All myworkdayjobs.com Jobs

Collect every job from any myworkdayjobs.com careers site.

- Apify Store: [apify.com/tinyrex/workday-jobs-scraper](https://apify.com/tinyrex/workday-jobs-scraper)
- Guide: [scrape workday jobs myworkdayjobs](https://emirmrkaljevic.github.io/tinyrex-data-tools/scrape-workday-jobs-myworkdayjobs/)

## Input used in this example

```json
{
  "companies": [
    "https://workday.wd5.myworkdayjobs.com/Workday",
    "https://adobe.wd5.myworkdayjobs.com/external_experienced"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~workday-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/workday-jobs-scraper).
