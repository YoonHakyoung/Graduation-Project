import pandas as pd
import json

with open("/Users/yoon/python/nodeinHouse_wkt.json", 'r') as file:
    data = json.load(file)

df = pd.json_normalize(data["DATA"])

df.to_csv("houseWKT.csv")