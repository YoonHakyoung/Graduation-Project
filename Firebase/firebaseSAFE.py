import pandas as pd
from math import sin, cos, sqrt, atan2, radians
from firebase_admin import credentials, firestore, initialize_app

# Firebase Admin SDK 설정
cred = credentials.Certificate('/Users/yoon/Downloads/safe-navigation-app-6fc08-firebase-adminsdk-sy8t7-364b14f110.json')
initialize_app(cred)

# Firestore 데이터베이스에서 현재 위치 가져오기
db = firestore.client()
query = db.collection(u'GPS').where(u'email', u'==', u'safe@gmail.com')
docs = query.get()

if len(docs) > 0:
    doc = docs[0]
    # 현재 위치의 위도와 경도 가져오기
    latitude = doc.to_dict()['Hnode']['latitude']
    longitude = doc.to_dict()['Hnode']['longitude']

    # 안전 장소 데이터 프레임 로드 및 거리 계산 함수 정의
    df = pd.read_csv('merged_safe.csv')

    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # 지구 반경 (km)
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c
        return d

    distances = []
    for _, row in df.iterrows():
        distance = haversine(row['latitude'], row['longitude'], latitude, longitude)
        distances.append(distance)

    # 데이터프레임에 거리 정보 추가하고, 가장 가까운 3개 선택하기
    df['distance'] = distances
    closest_rows = df.sort_values('distance').head(3)

    # 결과 딕셔너리 생성하여 Firestore에 업로드하기
    result_dict = {}
    for i, row in enumerate(closest_rows.itertuples()):
        result_dict[str(i+1)] = {row.type: [row.latitude, row.longitude]}

    nearby_ref = db.collection(u'Nearby Safe').document(u'safe@gmail.com')
    nearby_ref.set(result_dict)

    print('Data uploaded to Firestore!')
else:
    print('문서가 존재하지 않습니다.')
