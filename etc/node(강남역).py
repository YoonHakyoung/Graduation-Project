import csv

with open('cctv_강남.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    filtered_rows = []
    for row in reader:
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        if latitude >= 37.497184 and latitude <= 37.502585 and longitude >= 127.026490 and longitude <= 127.031035:
            filtered_rows.append(row)

with open('cctv(강남역).csv', 'w', newline='') as csvfile:
    fieldnames = ['latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in filtered_rows:
        writer.writerow(row)
