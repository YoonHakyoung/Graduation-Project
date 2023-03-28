from geopy.distance import great_circle
import pandas as pd
import folium

class CountByWGS84:

    def __init__(self, df, lat, lon, dist=1):
        """
        df: 데이터 프레임
        lat: 중심 위도
        lon: 중심 경도
        dist: 기준 거리(km)
        """
        self.df = df
        self.lat = lat
        self.lon = lon
        self.dist = dist

    def filter_by_rectangle(self):
        """
        사각 범위 내 데이터 필터링
        """
        lat_min = self.lat - 0.001 * self.dist
        lat_max = self.lat + 0.001 * self.dist

        lon_min = self.lon - 0.0025 * self.dist
        lon_max = self.lon + 0.0025 * self.dist

        self.points = [[lat_min, lon_min], [lat_max, lon_max]]

        result = self.df.loc[
            (self.df['lat'] > lat_min) &
            (self.df['lat'] < lat_max) &
            (self.df['lon'] > lon_min) &
            (self.df['lon'] < lon_max)
        ]
        result.index = range(len(result))

        return result

    def plot_by_rectangle(self, df):
        """
        사각 범위 내 데이터 플로팅
        """

        m = folium.Map(location=[self.lat, self.lon], zoom_start=14)

        for idx, row in self.df.iterrows():

            lat_ = row['lat']
            lon_ = row['lon']

            folium.Marker(location=[lat_, lon_],
                          radius=15,
                          tooltip=row['ID']).add_to(m)
            folium.Marker(location=[37.5005, 127.021],icon=folium.Icon(color='red',icon='star')).add_to(m)
            

        folium.Rectangle(bounds=self.points,
                         color='#ff7800',
                         fill=True,
                         fill_color='#ffff00',
                         fill_opacity=0.2).add_to(m)
        
        

        return m
    
    def plot_by_radius(self, df):
        """
        반경 범위 내 데이터 플로팅
        """

        m = folium.Map(location=[self.lat, self.lon], zoom_start=14)

        for idx, row in df.iterrows():

            lat_ = row['lat']
            lon_ = row['lon']

            folium.Marker(location=[lat_, lon_],
                          radius=15,
                          tooltip=row['ID']).add_to(m)

        folium.Circle(radius=self.dist * 1000,
                      location=[self.lat, self.lon],
                      color="#ff7800",
                      fill_color='#ffff00',
                      fill_opacity=0.2
                      ).add_to(m)

        return m

df = pd.read_csv("/Users/yoon/python/houseWKT.csv", dtype= {'ID':object})

node1_lat = 37.500
node1_lon = 127.021
node2_lat = 37.503
node2_lon = 127.026

start = folium.Marker(location=[node1_lat, node2_lon], radius=15)

midnode_lat = (node2_lat + node1_lat) / 2
midnode_lon = (node2_lon + node1_lon) / 2
#print(midnode_lat-0.001, midnode_lon-0.0025)

test = CountByWGS84(df, midnode_lat, midnode_lon)
#print(test.filter_by_rectangle())

'''
result_rectangle = test.plot_by_rectangle(df)

pl_rad = test.plot_by_radius(df)

plot_1 = test.plot_by_rectangle(result_rectangle)
print(plot_1)
plot_1.save("plot_1.html")
pl_rad.save("radius.html")
'''

print(df.loc[0,'lat'])
