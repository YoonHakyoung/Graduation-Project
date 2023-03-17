import json

file_path = "/Users/yoon/Downloads/서울시 자치구별 도보 네트워크 공간정보.json"

nodeDict = {"DESCRIPTION" : ['index[0] : 위도' , 'index[1] : 경도', 'index[2] : 노드 ID']}
linkDict = {"DESCRIPTION" : ['index[0] : 시작 노드 ID' , 'index[1] : 도착 노드 ID', 'index[2] : 경로 길이']}
nodeList = []
linkList = []
nodeList2 = {}


with open(file_path, 'r') as file:
    data = json.load(file)
    dataDATA = data["DATA"]

for i in dataDATA:
    if i['type'] == 'NODE':
        point = ((i['node_wkt'])[6:-1]).split(' ')
        nodeValue = [ [point[1], point[0]], str(i['node_id'])]
        nodeList.append(nodeValue)

        nodeList2[str(i['node_id'])] = [ float(point[1]), float(point[0]) ]

        
    else:
        linkValue = [ str(i['strt_node_id']), str(i['end_node_id']), i['link_len'] ]
        linkList.append(linkValue)


nodeDict['NODE'] = nodeList
linkDict['LINK'] = linkList

with open('node.json', 'w') as f : 
    json.dump(nodeDict, f, ensure_ascii=False, indent="\t")

print(nodeDict)
        
with open('link.json', 'w') as f :
    json.dump(linkDict, f, ensure_ascii=False, indent="\t")

with open('node2.json', 'w') as f :
    json.dump(nodeList2, f, ensure_ascii=False, indent="\t")