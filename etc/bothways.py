import json

with open('adjNodeList.json', 'r') as f:
    graph = json.load(f)

# graph 딕셔너리를 복사합니다.
graph_copy = graph.copy()

# 복사본을 이용하여 양방향 그래프를 생성합니다.
for node, edges in graph_copy.items():
    for (neighbor, weight) in edges:
        if neighbor not in graph:
            graph[neighbor] = [(node, weight)]
        if node not in [n[0] for n in graph[neighbor]]:
            graph[neighbor].append((node, weight))

with open('graph.json', 'w') as f :
    json.dump(graph, f, ensure_ascii=False)