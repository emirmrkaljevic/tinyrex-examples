# Finland Company Search - Y-tunnus Lookup & B2B Leads (YTJ/PRH)

Y-tunnus lookup and Finnish B2B lead lists from the official PRH/YTJ API.

- Apify Store: [apify.com/tinyrex/finland-company-search](https://apify.com/tinyrex/finland-company-search)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/y-tunnus-lookup-finnish-company-list-ytj-api/)

## Input used in this example

```json
{
  "companies": [
    "0112038-9",
    "Supercell"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~finland-company-search/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/finland-company-search).
