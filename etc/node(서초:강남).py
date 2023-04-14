import pandas as pd
import csv

# CSV 파일 읽기
df = pd.read_csv("/Users/yoon/Downloads/서초_도보.csv", encoding='euc-kr', header=None)

# Write to CSV file
with open('node(서초).csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['node_key','latitude', 'longitude'])
    for index, row in df.iterrows():
        if row[0] == 'NODE':
            if '서초구' in row[11]:
                coordinates_str = row[1].replace("POINT(", "").replace(")", "")
                coordinates = coordinates_str.split(" ")
                result = [row[2], float(coordinates[1]), float(coordinates[0])]
                writer.writerow(result)

    f.close()
