import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Firebase Admin SDK 설정
cred = credentials.Certificate('/Users/yoon/Downloads/safe-navigation-app-6fc08-firebase-adminsdk-sy8t7-364b14f110.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred)

# Firestore DB 객체 생성
db = firestore.client()

# JSON 파일에서 데이터 로드
with open('route3_SD/path.json', 'r') as f:
    data = json.load(f)

# 'lati,longi' 필드에서 위도, 경도 값 추출
lati_longi = data['lati,longi']
points = []
for lat, lng in lati_longi:
    points.append(firestore.GeoPoint(lat, lng))

# 'PATH' 컬렉션에 있는 'seocho@gmail.com' 도큐먼트에 'point' 필드 추가
doc_ref = db.collection('PATH').document('seocho@gmail.com')
doc_ref.set({'points': points})

# 'total distance' 필드에서 정수 값 추출
total_distance = int(data['Total distance'])

# 'PATH' 컬렉션에 있는 'seocho@gmail.com' 도큐먼트에 'total_distance' 필드 추가
doc_ref = db.collection('PATH').document('seocho@gmail.com')
doc_ref.set({'total_distance': total_distance}, merge=True)

print('업로드 완료')
