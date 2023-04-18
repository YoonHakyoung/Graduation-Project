import pandas as pd
import geopy.distance

A = pd.read_csv('csv/대로변_sort.csv')

for i, row_a in A.iterrows():
    print(row_a['latitude'], row_a['longitude'])