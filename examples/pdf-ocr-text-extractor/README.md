# PDF Text Extractor & OCR - Bulk PDF and Image to Text

Extract text from PDFs and images in bulk, with OCR only on scanned pages.

- Apify Store: [apify.com/tinyrex/pdf-ocr-text-extractor](https://apify.com/tinyrex/pdf-ocr-text-extractor)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-pdf-to-text-ocr-scanned-pdf-api/)

## Input used in this example

```json
{
  "fileUrls": [
    "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
    "https://raw.githubusercontent.com/ocrmypdf/OCRmyPDF/v16.0.0/tests/resources/ccitt.pdf"
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
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~pdf-ocr-text-extractor/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/pdf-ocr-text-extractor).
