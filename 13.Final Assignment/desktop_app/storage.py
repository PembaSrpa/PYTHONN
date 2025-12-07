import json
import csv
import os

DATA_FILE = "data.json"

def load_json():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

def save_json(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def export_csv(filename="data.csv"):
    data = load_json()
    if not data:
        print("No data to export.")
        return
    keys = data[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data exported to {filename}")

def import_csv(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            save_json(data)
            print("CSV imported successfully!")
    except FileNotFoundError:
        print("File not found.")