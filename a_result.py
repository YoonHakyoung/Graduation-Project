import json
import a_star_al
import nearest
from getGPS import wktdata

#현재 사용자의 위도 경도 값
lati1 = wktdata[0]
longi1 = wktdata[1]

#목적지 위도 경도 값
lati2 = 37.502568
longi2 = 127.025193

startID = nearest.find_nearest_node(lati1, longi1, json.load(open('adList(wkt).json')))
endID = nearest.find_nearest_node(lati2, longi2, json.load(open('adList(wkt).json')))

print(startID, endID)

graph01 = a_star_al.Graph()
result = graph01.a_star_algorithm(startID, endID)

with open('path.json', 'w') as f :
    json.dump(result, f, ensure_ascii=False, indent="\t")