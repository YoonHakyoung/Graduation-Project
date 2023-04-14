import json
import csv
class Graph:
    def __init__(self):
        self.adjacency_list = json.load(open('graph(강남).json'))
        self.weights = {}
        with open('weight_element2.json', 'r') as f:
            weight_data = json.load(f)
            for row in weight_data:
                node_key = row['node_key']
                weights = row['weights']
                self.weights[node_key] = weights
        # w(n)
        def w(weights):
            return weights['CCTV'] * 0.01 + weights['Roadside'] * 0.01 + weights['Children'] * 0.01 + weights['Alcol'] * 0.9
        self.w = w

    def get_weighted_neighbors(self, v):
        neighbors = self.adjacency_list[v]
        weighted_neighbors = []
        for neighbor, distance in neighbors:
            # Call the weighting function w(n) to calculate the weight
            weight = self.w(self.weights[neighbor])
            weighted_neighbors.append((neighbor, distance * weight))
        return weighted_neighbors
    def h(self, n): return 1
    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                reconst_path = []
                path_len = 0
                while parents[n] != n: 
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                return reconst_path
            for (m, weight) in self.get_weighted_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

graph1 = Graph()
print(graph1.a_star_algorithm('71808', '104253'))