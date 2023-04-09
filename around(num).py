import pandas as pd
import geopy.distance

# 데이터 프레임 A, B를 읽어옵니다.
A = pd.read_csv('adList(wkt).csv')
B = pd.read_csv('버스정류장.csv')

# 새로운 데이터프레임 생성을 위한 빈 리스트를 생성합니다.
result_list = []

# 데이터 프레임 A를 기준으로 주변 (distance)km 안에 B 값이 있는지 판별합니다.
for i, row_a in A.iterrows():
    lat_a, lon_a = row_a['latitude'], row_a['longitude']
    count_b = 0
    
    for j, row_b in B.iterrows():
        lat_b, lon_b = row_b['latitude'], row_b['longitude']
        distance = geopy.distance.distance((lat_a, lon_a), (lat_b, lon_b)).km
        
        if distance <= 0.05:    #km
            count_b += 1
    
    # 결과 데이터프레임에 행을 추가합니다.
    result_list.append([str(int(row_a['node_key'])), count_b])

# 결과 데이터프레임을 생성합니다.
result_df = pd.DataFrame(result_list, columns=['node_key', 'Bus'])

# 결과 데이터프레임을 csv 파일로 저장합니다.
result_df.to_csv('Bus(num).csv', index=False)
