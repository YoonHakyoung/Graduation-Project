import csv

# CSV 파일 열기
with open('어린이보호구역 위치도.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)

    next(reader)

    #새로운 파일
    with open('어린이보호구역.csv', 'w', newline='') as newfile1:
        writer1 = csv.writer(newfile1)

        #열 이름 만들기
        writer1.writerow(['latitude', 'longitude'])
        for row in reader:
            writer1.writerow([row[10],row[9]])