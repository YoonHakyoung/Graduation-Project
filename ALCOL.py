import csv

with open('/Users/yoon/Downloads/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    with open('유흥시설.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['latitude', 'longitude'])
        for row in reader:
            if len(row) > 6 and row[6].find('유흥') != -1:
                writer.writerow([row[38], row[37]])