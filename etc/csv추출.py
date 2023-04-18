import csv

# CSV 파일 열기
with open('경찰서1.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    next(reader)

    #새로운 파일
    with open('경찰서.csv', 'w', newline='') as newfile1:
        writer1 = csv.writer(newfile1)

        #열 이름 만들기
        writer1.writerow(['latitude', 'longitude'])
        for row in reader:
            writer1.writerow([row[0],row[1]])