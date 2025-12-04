# CSV (Comma Separated Values) is a common format for storing tabular data.
# Each line in a CSV file is a data record, and each record consists of fields separated by commas.

import csv

# --- Reading from a CSV file using csv.reader ---
with open('example.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print("Row:", row)

# --- Writing to a CSV file using csv.writer ---
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London'],
    ['Charlie', '35', 'Sydney']
]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# --- Working with CSV files as dictionaries using DictReader and DictWriter ---
with open('example.csv', mode='r', newline='') as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print("Name:", row['Name'], "| Age:", row['Age'], "| City:", row['City'])

with open('dict_output.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'David', 'Age': '28', 'City': 'Toronto'})
    dict_writer.writerow({'Name': 'Eva', 'Age': '32', 'City': 'Berlin'})