file = open("/Users/yoon/python/cctv.txt", "r")

wktList = []

while True:
    line = file.readline()
    if not line:
        break
    latilong = (line.strip()).split(',')
    lati = float(latilong[0])
    longi = float(latilong[1])
    lati_PLUS_longi = [lati, longi]
    if lati_PLUS_longi in wktList:
        pass
    wktList.append(lati_PLUS_longi)

print(wktList)

bell_node_wkt = {}
num = 0
for i in wktList:
    
    num = num + 1
    bell_node_wkt[num] = i

print(bell_node_wkt)

#for key, value in bell_node_wkt.items():
    #print(key,':',value,',')

file.close()
import json
with open('cctv.json', 'w') as f :
    json.dump(bell_node_wkt, f, ensure_ascii=False, indent="\t")