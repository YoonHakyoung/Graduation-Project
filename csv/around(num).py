import pandas as pd
from scipy.spatial import KDTree

# 데이터 프레임 A, B를 읽어옵니다.
A = pd.read_csv('csv/node.csv')
B = pd.read_csv('csv/대로변.csv')

# B의 좌표를 트리구조로 변환합니다.
B_tree = KDTree(B[['latitude', 'longitude']])

# 새로운 데이터프레임 생성을 위한 빈 리스트를 생성합니다.
result_list = []

# A의 좌표를 미리 튜플 형태로 저장합니다.
A_coords = list(zip(A['latitude'], A['longitude']))

# 데이터 프레임 A를 기준으로 주변 (distance)km 안에 B 값이 있는지 판별합니다.
for i, row_a in A.iterrows():
    lat_a, lon_a = row_a['latitude'], row_a['longitude']
    count_b = 0
    
    # B_tree에서 A 좌표를 기준으로 반경 50m 이내에 있는 좌표를 검색합니다.
    idx_list = B_tree.query_ball_point((lat_a, lon_a), r=0.0001)
    
    # 검색된 좌표의 개수를 세어 결과에 추가합니다.
    count_b = len(idx_list)
    
    # 결과 데이터프레임에 행을 추가합니다.
    result_list.append([str(int(row_a['node_key'])), count_b])

# 결과 데이터프레임을 생성합니다.
result_df = pd.DataFrame(result_list, columns=['node_key', 'Roadside'])

# 결과 데이터프레임을 csv 파일로 저장합니다.
result_df.to_csv('Roadside(num)_seoul.csv', index=False)

'''
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
result_df = pd.DataFrame(result_list, columns=['node_key', 'Children'])

# 결과 데이터프레임을 csv 파일로 저장합니다.
result_df.to_csv('Children(num)_seoul.csv', index=False)
'''