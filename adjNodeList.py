import json

with open("/Users/yoon/python/link.json", 'r') as linkfile:
    linkJsonData = json.load(linkfile)
    linkData = linkJsonData["LINK"]
    nodeDic = {}

    for linkline in linkData:
        valueList = []
        endLeng = [linkline[1], linkline[2]]
        
        if linkline[0] in nodeDic:
            pass
            existList = nodeDic.get(linkline[0])
            existList.append(endLeng)
            nodeDic[linkline[0]] = existList
        else:
            valueList.append(endLeng)
            nodeDic[linkline[0]] = valueList

with open('adjNodeList1.json', 'w') as f : 
    json.dump(nodeDic, f, ensure_ascii=False)

            