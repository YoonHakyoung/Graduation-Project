import json
import a_star_al
import nearest
from getGPS_1 import wktdata

#현재 사용자의 위도 경도 값
lati1 = wktdata[0]
longi1 = wktdata[1]


#목적지 위도 경도 값
lati2 = 37.499815
longi2 = 127.029714


#startID = nearest.find_nearest_node(lati1, longi1, json.load(open('node.json')))
endID = nearest.find_nearest_node(lati2, longi2, json.load(open('node.json')))

print( endID)

graph01 = a_star_al.Graph()
result = graph01.a_star_algorithm('104660', '130477')

with open('path2.json', 'w') as f :
    json.dump(result, f, ensure_ascii=False, indent="\t")