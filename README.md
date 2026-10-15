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
| [contact-details-extractor](https://apify.com/tinyrex/contact-details-extractor) | Pull emails, phone numbers and social profile links from a list of company websites. | [examples/contact-details-extractor](examples/contact-details-extractor) |  |
| [tech-stack-detector](https://apify.com/tinyrex/tech-stack-detector) | Detect CMS, e-commerce, analytics, CDN and payment tech on a list of domains (lead lists, competitor research). | [examples/tech-stack-detector](examples/tech-stack-detector) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/bulk-tech-stack-lookup-wappalyzer-alternative/) |
| [gleif-lei-lookup](https://apify.com/tinyrex/gleif-lei-lookup) | Look up, validate and enrich Legal Entity Identifiers (LEI) via the official GLEIF API. | [examples/gleif-lei-lookup](examples/gleif-lei-lookup) |  |
| [uk-companies-house-lookup](https://apify.com/tinyrex/uk-companies-house-lookup) | Fetch UK company profiles, officers and PSC data from the official Companies House API. | [examples/uk-companies-house-lookup](examples/uk-companies-house-lookup) |  |

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
| [us-uk-tenders-scraper](https://apify.com/tinyrex/us-uk-tenders-scraper) | Search US SAM.gov and UK Contracts Finder opportunities in one dataset. | [examples/us-uk-tenders-scraper](examples/us-uk-tenders-scraper) |  |
| [tenderned-tenders-scraper](https://apify.com/tinyrex/tenderned-tenders-scraper) | Search Dutch public tenders on TenderNed. | [examples/tenderned-tenders-scraper](examples/tenderned-tenders-scraper) |  |
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
| [broken-link-checker](https://apify.com/tinyrex/broken-link-checker) | Crawl a site and report 404s, dead links and redirect chains. | [examples/broken-link-checker](examples/broken-link-checker) |  |
| [seo-on-page-audit](https://apify.com/tinyrex/seo-on-page-audit) | Audit title, meta description, H1, canonical, Open Graph and schema on a list of pages. | [examples/seo-on-page-audit](examples/seo-on-page-audit) |  |
| [rss-feed-scraper](https://apify.com/tinyrex/rss-feed-scraper) | Turn RSS, Atom or JSON Feed URLs (or plain websites) into clean JSON/CSV. | [examples/rss-feed-scraper](examples/rss-feed-scraper) | [guide](https://emirmrkaljevic.github.io/tinyrex-data-tools/rss-feed-to-json-csv-api/) |

## Other ways to run them

- No code: open the Store page, paste your input and download CSV, Excel or JSON.
- Schedules and webhooks: run any actor on a schedule in the Apify Console and get the results by webhook, or plug them into Make, Zapier or n8n through the Apify integrations.
- AI agents: every actor is also callable as a tool through the [Apify MCP server](https://mcp.apify.com/).

## About

Written by the author of the TinyRex actors. Issues and requests for new examples are welcome. MIT licensed.
