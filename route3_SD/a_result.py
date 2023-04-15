import json
import a_star_al
import nearest
from getGPS import start_lat,start_lon,end_lat,end_lon

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

'''
논현초
startID = nearest.find_nearest_node(37.504603 ,127.024747)
endID = nearest.find_nearest_node(37.507876, 127.026821)
'''
'''
강남
startID = nearest.find_nearest_node(37.498661 ,127.027775)
endID = nearest.find_nearest_node(37.501493, 127.029344)
'''
startID = nearest.find_nearest_node(37.484909 ,126.981060)
endID = nearest.find_nearest_node(37.481826, 126.978842)

print(startID,endID)

graph01 = a_star_al.Graph()
#result = graph01.a_star_algorithm('194041', '106906')
result = graph01.a_star_algorithm(startID, endID)


with open('route3_SD/path.json', 'w') as f :
    json.dump(result, f, ensure_ascii=False, indent="\t")