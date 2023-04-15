from collections import deque
import math
import json
import nearest

class Graph:
    def __init__(self):
        self.adjacency_list = json.load(open('Project/graph.json'))
        self.wktlist = json.load(open('Project/node.json'))
        self.weights = {}
        with open('Project/weight_element_seoul.json', 'r') as f:
            weight_data = json.load(f)
            for row in weight_data:
                node_key = row['node_key']
                weights = row['weights']
                self.weights[node_key] = weights
        '''
        def w(weight):
            return 2.0 * (1 / (1 + 0.5 * weights['CCTV'] + 0.2 * weights['Children'] + 0.7 * weights['Roadside'] + 0.5 * weights['Bus'] )) - 1 * 0.5 * weights['Alcol']
        '''
        '''
        def w(weights):
            cctv_weight = weights.get("CCTV", 0) * 3
            roadside_weight = weights.get("Roadside", 0) * 3
            children_weight = weights.get("Children", 0) * 3
            bus_weight = weights.get("Bus", 0) * 2
            entertainment_weight = weights.get("Alcol", 0) * 5
            total_weight = cctv_weight + roadside_weight + children_weight + bus_weight + entertainment_weight
            print(total_weight , cctv_weight , roadside_weight , children_weight , bus_weight , entertainment_weight)
            if total_weight == 0:
                return 1
            # cctv, roadside, children, bus weight가 많을수록 반환값은 줄어들도록, 
            # entertainment weight가 많을수록 반환값은 증가하도록 합니다.
            safe_ele = cctv_weight + roadside_weight + children_weight + bus_weight
            score = (1 / (1 + safe_ele) * 1 + entertainment_weight * 1)
            if score <= 0:
                return 0.0001
            return score
        '''
        
        def w(weights):
            return weights['CCTV'] * 0.1 + weights['Roadside'] * 0.01 + weights['Children'] * 0.01 + weights['Bus'] * 00.1 + weights['Alcol'] * 1.2
        self.w = w
        
    def get_weighted_neighbors(self, v):
        neighbors = self.adjacency_list[v]
        weighted_neighbors = []
        for neighbor, distance in neighbors:
            if neighbor not in self.weights:
                weight = 1
            else: 
                weight = self.w(self.weights[neighbor])
                #weight = 1
                if weight == 0: weight = 1
                #print(neighbor, self.weights[neighbor], self.w(self.weights[neighbor]))
            weighted_neighbors.append((neighbor, distance * weight))
            #print(neighbor,'distance',distance,'weight',weight,'distance * weight', distance * weight)
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
                path_wkt = []
                path_len = 0
                result = {}
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                for i in range(len(reconst_path)-1):
                    current_node = reconst_path[i]
                    next_node = reconst_path[i+1]
                    for (neighbor, weight) in self.get_weighted_neighbors(current_node):
                        if neighbor == next_node:
                            for (neighbor_real, weight_real) in self.adjacency_list[current_node]:
                                if neighbor_real == neighbor:
                                    path_len += weight_real
                            break
                for pathnode in reconst_path:
                    print(pathnode, self.get_weighted_neighbors(pathnode))
                    if pathnode not in self.wktlist: pass
                    else: path_wkt.append(self.wktlist[pathnode])
                result["Path found"] = reconst_path
                result["Total distance"] = path_len
                result["lati,longi"] = path_wkt
                return result
            #print('n',n,'get_weighted_neighbors',self.get_weighted_neighbors(n))
            for (m, weight) in self.get_weighted_neighbors(n):
                #print('open_list', open_list,'\n','closed_list' ,closed_list)
                
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                
                else:
                   #print(g[m] , g[n]  ,weight)
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

#graph1 = Graph()
#nearest_node_id = nearest.find_nearest_node(37.499915, 127.024740, json.load(open('node.json')))
#print(graph1.a_star_algorithm('104257', '130475'))