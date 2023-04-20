import pandas as pd
from math import sin, cos, sqrt, atan2, radians

df = pd.read_csv('Flask/__pycache__/merged_safe.csv')

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    return d

#현재위치
lat = 37.496412
lon = 127.070421

distances = []
for _, row in df.iterrows():
    distance = haversine(row['latitude'], row['longitude'], lat, lon)
    distances.append(distance)

# add the distances to the DataFrame
df['distance'] = distances

# sort the DataFrame by distance and select the 5 closest rows
closest_rows = df.sort_values('distance').head(3)
result = {}
for i, row in enumerate(closest_rows.itertuples()):
    result[i+1] = {row.type: [row.latitude, row.longitude]}
print(result)