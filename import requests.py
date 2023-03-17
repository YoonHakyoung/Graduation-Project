import requests
import json

listpolic = [{
                "addr_name" : "서울 중구 동호로 14길 18",
                "name" :"다산치안센터" 
            },
            {
            "addr_name" : "서울 중구 을지로 281",
            "name" :"DDP치안센터"
            },
            {
            "addr_name" : "서울 중구 충무로2길 39",
            "name" :"충4치안센터"
            }]

def get_coordinate(address): # 주소를 입력받음
    result = "" 
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address # 카카오 api 서버스를 이용하여 접근
    rest_api_key = '4af578c58356b165193c3c4b7eafc1f0' # 사용자 api key
    header = {'Authorization': 'KakaoAK ' + rest_api_key} 

    r = requests.get(url, headers=header) 
 
    if r.status_code == 200: # 정보를 오류없이 받아왔다면
        if len(r.json()['documents']) != 0: # 길이가 0이 아니라면
            try : 
                result_address = r.json()["documents"][0]["address"]
                result = (result_address["y"],result_address["x"])  # 좌표 정보에 접근
            except:  # 예외처리
                print("오류1")
                
            
        else: # 길이가 0인경우 na처리
            print("오류2")
            
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    return result # 좌표를 반환

for j in range(len(listpolic)):
    print(get_coordinate(listpolic[j]["addr_name"]))
