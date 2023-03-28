import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class Ploy:
    def __init__(self, df, wkt1, wkt2):
        self.df = df
        self.wkt1 = wkt1
        self.wkt2 = wkt2
        self.square = self.ploy()

    def ploy(self):
        node4wkt = [
            (self.wkt1[0], self.wkt1[1]),
            (self.wkt1[0], self.wkt2[1]),
            (self.wkt2[0], self.wkt2[1]),
            (self.wkt2[0], self.wkt1[1])
        ]
        square = Polygon(node4wkt)
        return square
    
    def InOut(self):
        points = [Point(xy) for xy in zip(self.df['lon'], self.df['lat'])]
        result = self.df.loc[[point.within(self.square) for point in points], :]
        result.reset_index(drop=True, inplace=True)
        return result

df = pd.read_csv("/Users/yoon/python/houseWKT.csv", dtype= {'ID':object})
test = Ploy(df, (37.500, 127.021), (37.504, 127.026))
inout = test.InOut()
print(inout)

import folium
from folium.plugins import Draw

# 지도 생성
m = folium.Map(location=[37.5, 127.02], zoom_start=13)

# 사각형 좌표
sw = (37.498, 127.021)
ne = (37.504, 127.026)

# 사각형 그리기
folium.Rectangle(
    bounds=[sw, ne],
    color='red',
    fill=True,
    fill_color='red',
    fill_opacity=0.2
).add_to(m)

# 지도에 그림 추가
Draw(export=True).add_to(m)

for index, row in df.iterrows():
    lat = row['lat']
    lon = row['lon']
    marker = folium.Marker(location=[lat, lon])
    marker.add_to(m)

    poly_coords = [(37.500, 127.021), (37.504, 127.021), (37.504, 127.026), (37.500, 127.026)]

# 사각형을 지도 위에 추가
folium.Polygon(locations=poly_coords, color='blue', fill_opacity=0.1).add_to(m)

# 사각형 좌표를 지도 위에 마커로 추가
for coord in poly_coords:
    folium.Marker(location=coord, icon=folium.Icon(color='red')).add_to(m)

# 지도 출력
m.save('map.html')
