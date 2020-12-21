import csv
import json

with open('data_final.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('data_final.json', 'w') as f:
    json.dump(rows, f)
