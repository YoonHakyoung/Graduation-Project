import json

file_path = "서울시 자치구별 도보 네트워크 공간정보.csv"

node_list = {}
link_list = {}

with open(file_path, 'r') as file:
    data = json.load(file)
    dataDATA = data["DATA"]

    for i in dataDATA:
        '''
        if i['type'] == 'NODE':
            point = ((i['node_wkt'])[6:-1]).split(' ')
            node_value = [float(point[1]), float(point[0])]
            node_dic = dict( { i['node_id']: node_value } )
            node_list.update(node_dic)
        '''
        #else:
        link_value = dict( {'start_node':str(i['strt_node_id']), 'end_node':str(i['end_node_id']), 'len':i['link_len']})
        link_dic = dict( { i['link_id']: link_value } )
        link_list.update(link_dic)

'''
with open('node.json', 'w') as f : 
    json.dump(node_list, f, ensure_ascii=False)
'''
with open('link.json', 'w') as f :
    json.dump(link_list, f, ensure_ascii=False)
