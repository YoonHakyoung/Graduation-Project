import json

with open("/Users/yoon/python/adList_len50.json", 'r') as listfile:
    adList = json.load(listfile)

dict = {}

safepath = ['194041', 
        '107675', '256', '255', '254', '253', '262', 
        '114849', '193725', '193726', '193727', '193728', 
        '193729', '193730', '193731', '107129', '107076', 
        '107075', '106939', '106907']

shortpath = ['194039', '194034', '107155', '107154']

for node in adList:
    if node in safepath or shortpath:
        dict[node] = adList[node]

for node in dict.values():
    for partner in node:
        if partner[0] in safepath:
            partner[1] = 0
        if partner[0] in shortpath:
            partner[1] = 100

with open('adList(path).json', 'w') as f :
    json.dump(dict, f, ensure_ascii=False, indent="\t")
