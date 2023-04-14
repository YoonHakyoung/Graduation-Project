import json
import a_star_al
import nearest
from getGPS import wktdata

'''
#현재 사용자의 위도 경도 값
lati1 = wktdata[0]
longi1 = wktdata[1]
'''
lati1 = 37.484855
longi1 = 126.980657

#목적지 위도 경도 값
lati2 = 37.481915
longi2 = 126.979476


startID = nearest.find_nearest_node(lati1, longi1, json.load(open('Project/node.json')))
endID = nearest.find_nearest_node(lati2, longi2, json.load(open('Project/node.json')))


graph01 = a_star_al.Graph()
result = graph01.a_star_algorithm(startID,endID)

with open('route3_SD/path.json', 'w') as f :
    json.dump(result, f, ensure_ascii=False, indent="\t")