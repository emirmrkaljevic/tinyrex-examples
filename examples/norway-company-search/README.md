# Norway Company Search - Org Number Lookup & B2B Leads (Brreg)

Norwegian org number lookup and B2B lead lists from the official Brreg API.

- Apify Store: [apify.com/tinyrex/norway-company-search](https://apify.com/tinyrex/norway-company-search)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/norway-org-number-lookup-brreg-company-list/)

## Input used in this example

```json
{
  "companies": [
    "923609016",
    "Telenor"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~norway-company-search/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/norway-company-search).
