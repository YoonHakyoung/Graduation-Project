import json
from collections import deque
from haversine import haversine

class Graph:

    def __init__(self, adjacency_list, wktData):
        self.adjacency_list = adjacency_list
        self.wktData = wktData

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def printWKT(self, wktList):
        testList = {}
        for pathnodeID in wktList:
            testList[pathnodeID] = wktData[pathnodeID]
        return testList
    
    def h(self, n, stop_node):
        hStart = self.wktData[n]
        hStop = self.wktData[stop_node]
        
        midnode_lati = (abs(hStart[0] + hStop[0]))/2
        midnode_longi = (abs(hStart[1] + hStart[1]))/2
        midnode = [midnode_lati, midnode_longi]

        len1 = int( haversine(hStart, midnode, unit = 'm') )
        len2 = int( haversine(midnode, hStop, unit = 'm') )
        return (len1 + len2)

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
                if n == None or g[v] + self.h(v, stop_node) < g[n] + self.h(n, stop_node):
                    n = v
                    
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return self.printWKT(reconst_path)

            for (m, weight) in self.get_neighbors(n):
                
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

with open("/Users/yoon/python/graph.json", 'r') as adListfile:
    adjacency_list = json.load(adListfile)

with open("/Users/yoon/python/node.json", 'r') as wktfile:
    wktData = json.load(wktfile)

graph1 = Graph(adjacency_list, wktData)

start_node = '106906'
stop_node = '194041'

print(graph1.a_star_algorithm(start_node, stop_node))