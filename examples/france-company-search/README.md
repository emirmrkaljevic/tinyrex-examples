# France Company Search - SIREN, SIRET & B2B Lists (Sirene)

SIREN/SIRET lookup and French B2B company lists from the official Sirene API.

- Apify Store: [apify.com/tinyrex/france-company-search](https://apify.com/tinyrex/france-company-search)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/siren-siret-lookup-french-company-list-api/)

## Input used in this example

```json
{
  "companies": [
    "552032534",
    "Michelin"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~france-company-search/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/france-company-search).
