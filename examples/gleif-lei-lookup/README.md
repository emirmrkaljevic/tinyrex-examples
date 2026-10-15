# LEI Lookup - Bulk GLEIF LEI Search, Validation & Parents

Look up, validate and enrich Legal Entity Identifiers (LEI) via the official GLEIF API.

- Apify Store: [apify.com/tinyrex/gleif-lei-lookup](https://apify.com/tinyrex/gleif-lei-lookup)

## Input used in this example

```json
{
  "leis": [
    "HWUPKR0MPOU8FGXBT394",
    "7LTWFZYICNSX8D621K86"
  ],
  "companyNames": [
    "Siemens AG"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~gleif-lei-lookup/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/gleif-lei-lookup).
