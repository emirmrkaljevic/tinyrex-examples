# TinyRex examples

Copy-paste Python, Node.js and curl examples for the [TinyRex actors on the Apify Store](https://apify.com/tinyrex). Each folder has a ready `input.json`, a `run.py`, a `run.mjs` and a short README with the HTTP call.

All actors use official APIs or public pages, need no login, and are pay-per-result, so failed or empty lookups are not charged. Tutorials live on the [TinyRex data tools guide site](https://emirmrkaljevic.github.io/tinyrex-data-tools/).

## Quick start

```bash
git clone https://github.com/emirmrkaljevic/tinyrex-examples
cd tinyrex-examples
pip install -r requirements.txt        # or: npm install
export APIFY_TOKEN=your_token          # https://console.apify.com/settings/integrations
python examples/rss-feed-scraper/run.py
```

Each script writes `output.json` (and `output.csv` in Python) next to itself. Change `input.json` to run your own domains, keywords or feeds.

## Actors

### Lead generation & company data

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [contact-details-extractor](https://apify.com/tinyrex/contact-details-extractor) | Pull emails, phone numbers and social profile links from a list of company websites. | [examples/contact-details-extractor](examples/contact-details-extractor) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/extract-emails-socials-from-domain-list/) |
| [tech-stack-detector](https://apify.com/tinyrex/tech-stack-detector) | Detect CMS, e-commerce, analytics, CDN and payment tech on a list of domains (lead lists, competitor research). | [examples/tech-stack-detector](examples/tech-stack-detector) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-tech-stack-lookup-wappalyzer-alternative/) |
| [gleif-lei-lookup](https://apify.com/tinyrex/gleif-lei-lookup) | Look up, validate and enrich Legal Entity Identifiers (LEI) via the official GLEIF API. | [examples/gleif-lei-lookup](examples/gleif-lei-lookup) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-lei-lookup-gleif-api-validation/) |
| [uk-companies-house-lookup](https://apify.com/tinyrex/uk-companies-house-lookup) | Fetch UK company profiles, officers and PSC data from the official Companies House API. | [examples/uk-companies-house-lookup](examples/uk-companies-house-lookup) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/companies-house-api-bulk-uk-company-lookup/) |
| [npi-registry-lookup](https://apify.com/tinyrex/npi-registry-lookup) | Bulk NPI lookup and US healthcare provider lists from the official NPPES NPI Registry API. | [examples/npi-registry-lookup](examples/npi-registry-lookup) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/npi-lookup-api-bulk-npi-validation-provider-list/) |
| [sec-edgar-filings-scraper](https://apify.com/tinyrex/sec-edgar-filings-scraper) | 10-K, 10-Q, 8-K and Form 4 filings by ticker or CIK from the official SEC EDGAR APIs. | [examples/sec-edgar-filings-scraper](examples/sec-edgar-filings-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/sec-edgar-api-download-10-k-8-k-filings-csv/) |
| [france-company-search](https://apify.com/tinyrex/france-company-search) | SIREN/SIRET lookup and French B2B company lists from the official Sirene API. | [examples/france-company-search](examples/france-company-search) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/siren-siret-lookup-french-company-list-api/) |
| [norway-company-search](https://apify.com/tinyrex/norway-company-search) | Norwegian org number lookup and B2B lead lists from the official Brreg API. | [examples/norway-company-search](examples/norway-company-search) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/norway-org-number-lookup-brreg-company-list/) |
| [finland-company-search](https://apify.com/tinyrex/finland-company-search) | Y-tunnus lookup and Finnish B2B lead lists from the official PRH/YTJ API. | [examples/finland-company-search](examples/finland-company-search) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/y-tunnus-lookup-finnish-company-list-ytj-api/) |

### Jobs

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [ats-jobs-scraper](https://apify.com/tinyrex/ats-jobs-scraper) | Collect open roles from Greenhouse, Lever, Ashby, Personio and other ATS job boards. | [examples/ats-jobs-scraper](examples/ats-jobs-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/scrape-greenhouse-lever-ashby-jobs/) |
| [workday-jobs-scraper](https://apify.com/tinyrex/workday-jobs-scraper) | Collect every job from any myworkdayjobs.com careers site. | [examples/workday-jobs-scraper](examples/workday-jobs-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/scrape-workday-jobs-myworkdayjobs/) |
| [remote-jobs-scraper](https://apify.com/tinyrex/remote-jobs-scraper) | Search remote jobs across Himalayas, Remote OK and We Work Remotely in one run. | [examples/remote-jobs-scraper](examples/remote-jobs-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/remote-jobs-api-himalayas-remoteok-weworkremotely/) |

### Public tenders & grants

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [ted-tenders-scraper](https://apify.com/tinyrex/ted-tenders-scraper) | Search EU public tenders and contract awards on TED by keyword, CPV code and country. | [examples/ted-tenders-scraper](examples/ted-tenders-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/ted-tenders-api-export/) |
| [us-uk-tenders-scraper](https://apify.com/tinyrex/us-uk-tenders-scraper) | Search US SAM.gov and UK Contracts Finder opportunities in one dataset. | [examples/us-uk-tenders-scraper](examples/us-uk-tenders-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/sam-gov-contracts-finder-tenders-api/) |
| [tenderned-tenders-scraper](https://apify.com/tinyrex/tenderned-tenders-scraper) | Search Dutch public tenders on TenderNed. | [examples/tenderned-tenders-scraper](examples/tenderned-tenders-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/tenderned-api-dutch-public-tenders-export/) |
| [eu-grants-scraper](https://apify.com/tinyrex/eu-grants-scraper) | Find open EU funding calls (Horizon Europe, Digital Europe and more) by keyword. | [examples/eu-grants-scraper](examples/eu-grants-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/eu-funding-calls-horizon-europe-api/) |

### E-commerce

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [shopify-products-scraper](https://apify.com/tinyrex/shopify-products-scraper) | Export a Shopify store catalog with prices, variants and stock to JSON/CSV. | [examples/shopify-products-scraper](examples/shopify-products-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/export-shopify-store-products-to-csv/) |
| [woocommerce-products-scraper](https://apify.com/tinyrex/woocommerce-products-scraper) | Export a WooCommerce store catalog with prices, variations and stock. | [examples/woocommerce-products-scraper](examples/woocommerce-products-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/export-woocommerce-store-products-to-csv/) |

### SEO & web

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [sitemap-scraper](https://apify.com/tinyrex/sitemap-scraper) | List every URL in a site's XML sitemaps, optionally with HTTP status checks. | [examples/sitemap-scraper](examples/sitemap-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/extract-all-urls-from-sitemap/) |
| [broken-link-checker](https://apify.com/tinyrex/broken-link-checker) | Crawl a site and report 404s, dead links and redirect chains. | [examples/broken-link-checker](examples/broken-link-checker) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/find-broken-links-404-redirects-website/) |
| [seo-on-page-audit](https://apify.com/tinyrex/seo-on-page-audit) | Audit title, meta description, H1, canonical, Open Graph and schema on a list of pages. | [examples/seo-on-page-audit](examples/seo-on-page-audit) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-on-page-seo-checker-title-meta-h1/) |
| [rss-feed-scraper](https://apify.com/tinyrex/rss-feed-scraper) | Turn RSS, Atom or JSON Feed URLs (or plain websites) into clean JSON/CSV. | [examples/rss-feed-scraper](examples/rss-feed-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/rss-feed-to-json-csv-api/) |
| [lighthouse-audit](https://apify.com/tinyrex/lighthouse-audit) | Run Google Lighthouse on many URLs: performance, SEO, accessibility scores and Core Web Vitals. | [examples/lighthouse-audit](examples/lighthouse-audit) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-lighthouse-audit-core-web-vitals/) |

### Documents, media & data quality

| Actor | What it does | Example | Guide |
|---|---|---|---|
| [bulk-website-screenshot](https://apify.com/tinyrex/bulk-website-screenshot) | Full-page or viewport screenshots of a list of URLs as PNG/JPEG. | [examples/bulk-website-screenshot](examples/bulk-website-screenshot) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-website-screenshots-to-csv-google-drive/) |
| [bulk-email-validator](https://apify.com/tinyrex/bulk-email-validator) | Validate email lists: syntax, MX records, disposable and role addresses, typo hints. | [examples/bulk-email-validator](examples/bulk-email-validator) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-email-validation-mx-disposable-check/) |
| [pdf-ocr-text-extractor](https://apify.com/tinyrex/pdf-ocr-text-extractor) | Extract text from PDFs and images in bulk, with OCR only on scanned pages. | [examples/pdf-ocr-text-extractor](examples/pdf-ocr-text-extractor) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-pdf-to-text-ocr-scanned-pdf-api/) |
| [audio-video-transcriber](https://apify.com/tinyrex/audio-video-transcriber) | Transcribe audio and video URLs to text, SRT and VTT with Whisper. | [examples/audio-video-transcriber](examples/audio-video-transcriber) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/transcribe-audio-video-to-text-srt-whisper-api/) |

## Other ways to run them

- No code: open the Store page, paste your input and download CSV, Excel or JSON.
- Schedules and webhooks: run any actor on a schedule in the Apify Console and get the results by webhook, or plug them into Make, Zapier or n8n through the Apify integrations.
- AI agents: every actor is also callable as a tool through the [Apify MCP server](https://mcp.apify.com/).

## About

Written by the author of the TinyRex actors. Issues and requests for new examples are welcome. MIT licensed.
