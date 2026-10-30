# Bulk Email Validator - MX, Disposable, Role & Typo Check

Validate email lists: syntax, MX records, disposable and role addresses, typo hints.

- Apify Store: [apify.com/tinyrex/bulk-email-validator](https://apify.com/tinyrex/bulk-email-validator)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-email-validation-mx-disposable-check/)

## Input used in this example

```json
{
  "emails": [
    "hello@apify.com",
    "jane@gmial.com",
    "test@mailinator.com",
    "nobody@example.com"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~bulk-email-validator/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/bulk-email-validator).
