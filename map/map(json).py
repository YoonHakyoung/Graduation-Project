import folium
import json

# JSON 데이터 로드
with open('node.json', 'r') as f:
    data = json.load(f)

# 지도 중심 좌표 설정
center = [37.573050, 126.979189]

# 지도 생성
map = folium.Map(location=center, zoom_start=13)

# 마커 추가
for key in data.keys():
    lat, lon = data[key]
    folium.Marker(location=[lat, lon], tooltip=key).add_to(map)

# 지도 저장
map.save('map(json).html')
