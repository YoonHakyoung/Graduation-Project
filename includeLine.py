import folium
import csv

def make_rectangle(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    return (xmin, ymin, xmax, ymax)

# 두 노드의 좌표값으로 사각형을 만듦
n1 = (37.498, 127.023)
n2 = (37.502, 127.027)
rectangle = make_rectangle(n1, n2)

m = folium.Map(location=[37.5, 127.025], zoom_start=15)

# csv 파일을 읽어서 해당 사각형에 포함된 행을 출력
with open('/Users/yoon/python/houseWKT.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # 첫번째 라인은 제외
    for row in reader:
        lat, lon = float(row[1]), float(row[2])
        if rectangle[0] <= lat <= rectangle[2] and rectangle[1] <= lon <= rectangle[3]:
            folium.Marker(location=[lat, lon], tooltip=row[0]).add_to(m)
            print(row)



folium.Polygon(locations=[(rectangle[0], rectangle[1]), (rectangle[0], rectangle[3]), (rectangle[2], rectangle[3]), (rectangle[2], rectangle[1])], color='red', fill=False).add_to(m)

m.save('map.html')