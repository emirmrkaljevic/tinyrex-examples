# NPI Registry Lookup - Bulk NPI Search & Healthcare Providers

Bulk NPI lookup and US healthcare provider lists from the official NPPES NPI Registry API.

- Apify Store: [apify.com/tinyrex/npi-registry-lookup](https://apify.com/tinyrex/npi-registry-lookup)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/npi-lookup-api-bulk-npi-validation-provider-list/)

## Input used in this example

```json
{
  "npis": [
    "1881018208",
    "1265131338"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~npi-registry-lookup/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/npi-registry-lookup).
