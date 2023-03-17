import json
with open("/Users/yoon/python/node2.json", 'r') as nodefile:
    nodeData = json.load(nodefile)
with open("/Users/yoon/python/adjNodeList1.json", 'r') as adjNodefile:
    wktdic = json.load(adjNodefile)

for i in wktdic:
    if i in nodeData:
        wktdic[i] = nodeData[i]

with open('node(linked).json', 'w') as f : 
    json.dump(wktdic, f, ensure_ascii=False)