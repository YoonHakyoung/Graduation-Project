import pandas as pd
import geopy.distance

# 데이터 프레임 A, B를 읽어옵니다.
A = pd.read_csv('adList(wkt).csv')
B = pd.read_csv('어린이보호구역.csv')

# 새로운 데이터프레임 생성을 위한 빈 리스트를 생성합니다.
result_list = []

# 데이터 프레임 A를 기준으로 주변 안에 B 값이 있는지 판별합니다.
for i, row_a in A.iterrows():
    lat_a, lon_a = row_a['latitude'], row_a['longitude']
    near_b = False
    
    for j, row_b in B.iterrows():
        lat_b, lon_b = row_b['latitude'], row_b['longitude']
        distance = geopy.distance.distance((lat_a, lon_a), (lat_b, lon_b)).km
        
        if distance <= 0.001:    #km
            near_b = True
            break
    
    # 결과 데이터프레임에 행을 추가합니다.
    result_list.append([str(int(row_a['node_key'])), near_b])

# 결과 데이터프레임을 생성합니다.
result_df = pd.DataFrame(result_list, columns=['node_key', 'CHILDREN'])
result_df['CHILDREN'] = result_df['CHILDREN'].apply(lambda x: 'True' if x else 'False')

# 결과 데이터프레임을 csv 파일로 저장합니다.
result_df.to_csv('CHILD(TorF).csv', index=False)
