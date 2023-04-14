import json

weights = {}
with open('weight_element.json', 'r') as f:
            weight_data = json.load(f)
            for row in weight_data:
                node_key = row['node_key']
                weights = row['weights']
                weights[node_key] = weights
                print(weights)
                print(0.1 * weights['CCTV'] , \
                      0.3 * weights['Roadside'] , \
                      0.1 * weights['Children'] , \
                      1.5 * weights['Alcol'] ,\
                      0.3 * weights['Bus'])
