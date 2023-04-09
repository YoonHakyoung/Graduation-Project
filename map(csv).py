import folium
import pandas as pd

nodes = pd.read_csv('adList(wkt).csv')

# 지도의 중심을 설정합니다.
center = [37.4952, 127.0283]

# 지도를 만듭니다.
m = folium.Map(location=center, zoom_start=12)

# 노드 데이터를 순회하며 지도에 추가합니다.
for _, node in nodes.iterrows():
    # 노드의 위치를 저장합니다.
    location = [node['latitude'], node['longitude']]
    # 마커를 생성하고 지도에 추가합니다.
    marker = folium.Marker(location=location)
    marker.add_to(m)

# 지도를 출력합니다.
m.save('map.html')
