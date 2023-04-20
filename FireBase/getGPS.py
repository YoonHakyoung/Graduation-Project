from firebase_admin import credentials, firestore, initialize_app
from time import sleep

# Firebase Admin SDK 설정
cred = credentials.Certificate('/Users/yoon/Downloads/safe-navigation-app-6fc08-firebase-adminsdk-sy8t7-364b14f110.json')
initialize_app(cred)

# Firestore 데이터베이스에서 데이터 가져오기
db = firestore.client()

# 위치 값 가져오는 함수
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        if changes and 'destination' in changes[0].document.to_dict():
            # Hnode 필드의 위도(latitude)와 경도(longitude) 값을 가져와 startGPS에 저장
            start_lat = doc.to_dict()['Hnode']['latitude']
            start_lon = doc.to_dict()['Hnode']['longitude']
            startGPS = [start_lat, start_lon]

            # destination 필드의 위도(latitude)와 경도(longitude) 값을 가져와 endGPS에 저장
            end_lat = doc.to_dict()['destination']['latitude']
            end_lon = doc.to_dict()['destination']['longitude']
            endGPS = [end_lat, end_lon]
            
            print("Start GPS:", startGPS)
            print("End GPS:", endGPS)


# 이벤트 리스너 등록
doc_ref = db.collection('GPS').document('seocho@gmail.com')
doc_watch = doc_ref.on_snapshot(on_snapshot)

# 무한 루프 생성
while True:
    sleep(1)
