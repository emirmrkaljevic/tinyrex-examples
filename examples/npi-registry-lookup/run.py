"""Run tinyrex/npi-registry-lookup on Apify and save the results to JSON and CSV.

Store page: https://apify.com/tinyrex/npi-registry-lookup
Usage:  export APIFY_TOKEN=...   (https://console.apify.com/settings/integrations)
        python run.py            (edit input.json to change the input)
"""
import csv
import json
import os
from pathlib import Path

from apify_client import ApifyClient

HERE = Path(__file__).parent
run_input = json.loads((HERE / "input.json").read_text())

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tinyrex/npi-registry-lookup").call(run_input=run_input)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Run {run.id} finished with status {run.status}: {len(items)} items")

(HERE / "output.json").write_text(json.dumps(items, indent=2, ensure_ascii=False))
if items:
    fields = sorted({key for item in items for key in item})
    with open(HERE / "output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in items:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in item.items()})
    print("Saved output.json and output.csv")
