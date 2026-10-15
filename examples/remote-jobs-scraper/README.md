# Remote Jobs Scraper - Himalayas, Remote OK, We Work Remotely

Search remote jobs across Himalayas, Remote OK and We Work Remotely in one run.

- Apify Store: [apify.com/tinyrex/remote-jobs-scraper](https://apify.com/tinyrex/remote-jobs-scraper)
- Guide: [remote jobs api himalayas remoteok weworkremotely](https://emirmrkaljevic.github.io/tinyrex-data-tools/remote-jobs-api-himalayas-remoteok-weworkremotely/)

## Input used in this example

```json
{
  "keywords": [
    "python"
  ],
  "sources": [
    "himalayas",
    "remoteok"
  ],
  "maxResultsPerSearch": 50
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~remote-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/remote-jobs-scraper).
