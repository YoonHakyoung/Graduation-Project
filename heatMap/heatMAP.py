import csv
import json

# Load weight data from weight_element.json file
with open('weight_element.json') as f:
    weights_data = json.load(f)

weights = {}
for data in weights_data:
    node_key = data['node_key']
    weights[node_key] = data['weights']

# Load adList data from adList(wkt).json file
with open('adList(wkt).json') as f:
    adlist_data = json.load(f)

# Calculate safety grades and write to adList(wkt).csv file
with open('heatMap.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['latitude', 'longitude', 'safety grade'])

    for node_key, coords in adlist_data.items():
        latitude, longitude = coords
        cctv = weights[node_key]['CCTV']
        roadside = weights[node_key]['Roadside']
        children = weights[node_key]['Children']
        alcol = weights[node_key]['Alcol']
        bus = weights[node_key]['Bus']
        safety_grade = 0.01 * cctv + 0.1 * children + 0.3 * roadside + 0.3 * bus + 1.5 * alcol
        safety_grade = round(safety_grade, 2)
        writer.writerow([latitude, longitude, safety_grade])
