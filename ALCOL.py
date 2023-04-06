import csv

with open('/Users/yoon/Downloads/소상공인시장진흥공단_상가(상권)정보_20221231 (1) 2/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    with open('ALCOL.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['latitude', 'longitude'])

        with open('서초.역삼.csv', 'w', newline='') as newfile1:
            writer1 = csv.writer(newfile1)

            for row in reader:
                if len(row) > 16 and ('서초' in row[16] or '역삼' in row[16]):
                    writer1.writerow(row)
                    if len(row) > 6 and row[6].find('유흥') != -1:
                        writer.writerow([row[38], row[37]])