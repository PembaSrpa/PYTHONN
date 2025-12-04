# --- JSON (JavaScript Object Notation) in Python ---

# JSON is a lightweight data-interchange format that's easy for humans to read and write,
# and easy for machines to parse and generate.
# JSON data consists of key-value pairs and supports data types like objects (dict), arrays (list), strings, numbers, booleans, and null.

import json

# --- Writing Python data to a JSON file ---
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {"city": "New York", "zip": "10001"}
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # Write data as formatted JSON

# --- Reading JSON data from a file ---
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded from file:", loaded_data)

# --- Parsing JSON strings ---
json_str = '{"greeting": "Hello", "count": 5}'
parsed = json.loads(json_str)
print("Parsed from string:", parsed)

# --- Converting Python objects to JSON strings ---
py_dict = {"status": "success", "result": [1, 2, 3]}
json_text = json.dumps(py_dict)
print("As JSON string:", json_text)