import csv

with open('cctv_강남.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    filtered_rows = []
    for row in reader:
        try:
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            if latitude >= 37.497184 and latitude <= 37.502585 and longitude >= 127.026490 and longitude <= 127.031035:
                filtered_rows.append(row)
        except (KeyError, ValueError):
            # latitude 또는 longitude가 없거나, 값이 잘못된 경우 해당 행을 건너뜁니다.
            continue

with open('cctv(강남역).csv', 'w', newline='') as csvfile:
    fieldnames = ['node_key', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in filtered_rows:
        writer.writerow(row)
