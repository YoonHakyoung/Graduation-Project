import json
with open("/Users/yoon/python/adList.json", 'r') as adListfile:
    adjacency_list = json.load(adListfile)

for i in adjacency_list:
    print("i, ",i)
    valueList = []
    for j in adjacency_list[i]:
        valueList.append(j[0])