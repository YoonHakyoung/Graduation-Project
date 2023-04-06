import json
with open("/Users/yoon/python/adList.json", 'r') as adListfile:
    adjacency_list = json.load(adListfile)

print(adjacency_list)

for node, edges in adjacency_list.items():
    for i in range(len(edges)):
        edges[i][1] = 50

print(adjacency_list)

with open('adList_len50.json', 'w') as f :
    json.dump(adjacency_list, f, ensure_ascii=False, indent="\t")