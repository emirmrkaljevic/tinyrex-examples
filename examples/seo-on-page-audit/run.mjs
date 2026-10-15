// Run tinyrex/seo-on-page-audit on Apify and save the results to output.json.
// Store page: https://apify.com/tinyrex/seo-on-page-audit
// Usage: export APIFY_TOKEN=... && node run.mjs   (edit input.json to change the input)
import { readFileSync, writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const here = new URL('.', import.meta.url);
const input = JSON.parse(readFileSync(new URL('input.json', here), 'utf8'));

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('tinyrex/seo-on-page-audit').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Run ${run.id} finished with status ${run.status}: ${items.length} items`);

writeFileSync(new URL('output.json', here), JSON.stringify(items, null, 2));
console.log('Saved output.json');
