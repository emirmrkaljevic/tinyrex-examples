# Bulk Website Screenshot - Full Page PNG/JPEG from URL List

Full-page or viewport screenshots of a list of URLs as PNG/JPEG.

- Apify Store: [apify.com/tinyrex/bulk-website-screenshot](https://apify.com/tinyrex/bulk-website-screenshot)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-website-screenshots-to-csv-google-drive/)

## Input used in this example

```json
{
  "urls": [
    "https://example.com",
    "https://apify.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~bulk-website-screenshot/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/bulk-website-screenshot).
