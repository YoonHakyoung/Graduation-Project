import json
import pandas as pd

# JSON 파일을 읽어들입니다.
with open('adList(wkt).json', 'r') as f:
    node_data = json.load(f)

# DataFrame을 생성합니다.
df = pd.DataFrame.from_dict(node_data, orient='index', columns=['latitude', 'longitude'])

# CSV 파일로 저장합니다.
df.to_csv('node_info.csv', index_label='node_key')
