import pandas as pd
import folium

# read the CSV files
rodside_df = pd.read_csv('Roadside(num)_seoul.csv')
adlist_df = pd.read_csv('그 외/node(서초).csv')

# filter the node keys with Roadside value not equal to 0
roadside_node_keys = rodside_df.loc[rodside_df['Roadside'] != 0, 'node_key'].tolist()

# filter the latitude and longitude for the roadside nodes
roadside_lat_long = adlist_df.loc[adlist_df['node_key'].isin(roadside_node_keys), ['latitude', 'longitude']]

# create a map centered at the mean latitude and longitude
map_center = [adlist_df['latitude'].mean(), adlist_df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=14)

# add markers for the roadside locations
for lat, long in roadside_lat_long.values:
    folium.Marker([lat, long]).add_to(m)

# display the map
m.save('map(Roadside).html')
