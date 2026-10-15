# Contact Details Extractor - Email, Phone & Social from Website

Pull emails, phone numbers and social profile links from a list of company websites.

- Apify Store: [apify.com/tinyrex/contact-details-extractor](https://apify.com/tinyrex/contact-details-extractor)

## Input used in this example

```json
{
  "domains": [
    "example.com",
    "apify.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~contact-details-extractor/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/contact-details-extractor).
