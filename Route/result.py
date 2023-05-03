import json
import a_star_al
import nearest

#논현초
startID = nearest.find_nearest_node([37.504603 ,127.024747])
endID = nearest.find_nearest_node([37.499189, 127.023197])

#강남
#startID = nearest.find_nearest_node([37.498661 ,127.027775])
#endID = nearest.find_nearest_node([37.501318, 127.029222])

graph01 = a_star_al.Graph()
result = graph01.a_star_algorithm(startID, endID)
#result = graph01.a_star_algorithm('107672', '106906')
#result = graph01.a_star_algorithm('194041', '106906')

with open('Route/path.json', 'w') as f :
    json.dump(result, f, ensure_ascii=False, indent="\t")