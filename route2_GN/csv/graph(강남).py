import json
import csv

# Read the CSV file and extract node keys
node_keys = set()
with open('node(강남역).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        node_keys.add(row['node_key'])

# Read the JSON file and extract relevant nodes
graph = {}
with open('graph.json') as jsonfile:
    data = json.load(jsonfile)
    for key, values in data.items():
        if key in node_keys:
            graph[key] = values
        else:
            for value in values:
                if value[0] in node_keys:
                    if key not in graph:
                        graph[key] = []
                    graph[key].append(value)

# Write the output to a new JSON file
with open('graph(강남).json', 'w') as outfile:
    json.dump(graph, outfile, indent="\t")
