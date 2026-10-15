# UK Companies House Lookup - Company Profile, Officers & PSC

Fetch UK company profiles, officers and PSC data from the official Companies House API.

- Apify Store: [apify.com/tinyrex/uk-companies-house-lookup](https://apify.com/tinyrex/uk-companies-house-lookup)

## Input used in this example

```json
{
  "companyNumbers": [
    "00445790",
    "00000006"
  ],
  "companyNames": [
    "Tesco"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~uk-companies-house-lookup/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/uk-companies-house-lookup).
