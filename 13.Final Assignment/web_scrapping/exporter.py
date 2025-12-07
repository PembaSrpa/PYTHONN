import csv
import json
from database import fetch_all

def export_csv(filename="products.csv"):
    data = fetch_all()
    if not data:
        print("No data found.")
        return

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV exported: {filename}")


def export_json(filename="products.json"):
    data = fetch_all()

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"JSON exported: {filename}")
