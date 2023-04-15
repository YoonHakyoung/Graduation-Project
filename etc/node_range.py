import csv

with open('csv/유흥시설.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    filtered_rows = []
    for row in reader:
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        if latitude >= 37.481775 and latitude <= 37.485271 and longitude >= 126.978041 and longitude <= 126.982110:
            filtered_rows.append(row)

with open('csv/유흥시설(사당).csv', 'w', newline='') as csvfile:
    fieldnames = ['node_key', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in filtered_rows:
        writer.writerow(row)

