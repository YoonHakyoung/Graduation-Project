import csv
import json

data = []

with open('weight_element_seoul.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        weights = {
            'CCTV': int(row['cctv']),
            'Roadside': int(row['Roadside']),
            'Children': int(row['Children']),
            'Alcol': int(row['Alcol']),
            'Bus': int(row['Bus'])
        }
        data.append({
            'node_key': row['node_key'],
            'weights': weights
        })

with open('weight_element_seoul.json', 'w') as f:
    json.dump(data, f, indent="\t")
