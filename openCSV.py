import csv

# CSV 파일 열기
with open('/Users/yoon/Downloads/전국어린이보호구역표준데이터.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    with open('어린이보호구역.csv', 'w', newline='') as newfile1:
        writer1 = csv.writer(newfile1)
        writer1.writerow(['latitude', 'longitude'])
        for row in reader:
            if '서울' in row[2]:
                writer1.writerow([row[4],row[5]])