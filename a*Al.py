from collections import deque

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n): return 0

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
                    n = v;

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
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    

adjacency_list = {
    '107714': [('193994', 74)], 
    '107676': [('193733', 8), ('107714', 67)], 
    '107675': [('194041', 104), ('256', 12)], 
    '107290': [('194018', 30)], 
    '252': [('257', 16)], 
    '253': [('254', 12)], 
    '254': [('255', 19)], 
    '255': [('194034', 143), ('256', 41)], 
    '256': [('193734', 15)], 
    '257': [('193738', 19), ('254', 16)], 
    '107674': [('193992', 9), ('107460', 77)], 
    '258': [('259', 31)], 
    '259': [('262', 19)], 
    '107673': [('107674', 20)], 
    '262': [('253', 49)], 
    '107672': [('107673', 77)], 
    '194033': [('107176', 23), ('194039', 148)], 
    '107154': [('106861', 73), ('194035', 150), ('107155', 37)],    
    '107155': [('194033', 59)], 
    '107176': [('194030', 148), ('107177', 39)], 
    '107177': [('107178', 80)], 
    '107178': [('106859', 14)], 
    '107460': [('107672', 18)], 
    '107455': [('107456', 33)],                     
    '107456': [('107455', 33)],                     
    '106906': [('106907', 17)], 
    '106907': [('106939', 14), ('106906', 17)], 
    '107129': [('107154', 40)],                     
    '107076': [('107129', 16)],                     
    '107075': [('107076', 17)],                     
    '114849': [], 
    '102592': [('107178', 76)], 
    '106939': [('107075', 24)],                     
    '106859': [('106860', 91)], 
    '106860': [('106861', 41)], 
    '106861': [('106907', 41)], 
    '194044': [('107460', 59), ('107455', 67)], 
    '193725': [('114849', 96), ('193726', 31)], 
    '193726': [('130106', 27), ('193727', 17)], 
    '193727': [('193728', 29)], 
    '193728': [('193729', 23)], 
    '193729': [('130105', 19), ('193730', 11)], 
    '193730': [('193731', 12)], 
    '193731': [('107129', 22)], 
    '193733': [('193734', 13)], 
    '193734': [('252', 40)], 
    '193738': [('258', 13)], 
    '193992': [('193993', 19)], 
    '193993': [('193994', 21)], 
    '193994': [('193995', 23)], 
    '193995': [('107673', 8), ('193996', 136)], 
    '193996': [('107676', 16), ('107675', 8)], 
    '194018': [], 
    '194025': [('194027', 24)], 
    '194027': [('194028', 31)], 
    '194028': [('194031', 12), ('194029', 20)], 
    '194029': [('194037', 118), ('194030', 37)], 
    '194030': [('107290', 37)], 
    '194031': [('194036', 41)], 
    '194034': [('194035', 40), ('107155', 150)], 
    '194035': [('253', 144), ('193725', 43), ('107154', 150)], 
    '194036': [('194043', 64)], 
    '194037': [], 
    '194039': [('194041', 39), ('194040', 49), ('194034', 53)],
    '194040': [], 
    '194041': [('194039', 39)], 
    '194043': [('194044', 16), ('194037', 20)], 
    '130105': [('130144', 26)], 
    '71798': [], 
    '71797': [('71798', 60)], 
    '71796': [('71797', 38)], 
    '71795': [('130106', 19), ('71796', 35)], 
    '66722': [], 
    '71821': [('66722', 29)], 
    '71822': [('71823', 76), ('130148', 66)], 
    '71823': [], 
    '130106': [], 
    '130138': [('130139', 43)], 
    '130139': [('130140', 36)], 
    '130140': [('130144', 41)], 
    '130144': [('130145', 43)], 
    '130145': [('71795', 26)], 
    '130148': [('130145', 60), ('71823', 41)], 
    '71820': [('71822', 65), ('130138', 50), ('66722', 52)]
}

graph1 = Graph(adjacency_list)

graph1.a_star_algorithm('194041', '106906')