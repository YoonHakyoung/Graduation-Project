import numpy as np
from sklearn.neighbors import KDTree
import json

def find_nearest_node(wktlist):
    with open('Project/node.json', 'r') as f:
        nodes = json.load(f)
    node_positions = np.array(list(nodes.values()))
    tree = KDTree(node_positions, leaf_size=2)
    dist, ind = tree.query([wktlist], k=1)
    nearest_node_key = list(nodes.keys())[ind[0][0]]
    return nearest_node_key

#nearest_node_key = find_nearest_node([37.504603 ,127.024747])
#print(nearest_node_key)  # 출력 결과: 164469