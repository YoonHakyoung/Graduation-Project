import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase Admin SDK 설정
cred = credentials.Certificate('/Users/yoon/Downloads/safe-navigation-app-6fc08-firebase-adminsdk-sy8t7-364b14f110.json')
firebase_admin.initialize_app(cred)

# Firestore 데이터베이스에서 데이터 가져오기
db = firestore.client()
doc_ref = db.collection('GPS').document('seocho@gmail.com')

# Hnode 필드의 위도(latitude)와 경도(longitude) 값을 가져와 startGPS에 저장
start_lat = doc_ref.get().to_dict()['Hnode']['latitude']
start_lon = doc_ref.get().to_dict()['Hnode']['longitude']
startGPS = [start_lat, start_lon]

# destination 필드의 위도(latitude)와 경도(longitude) 값을 가져와 endGPS에 저장
end_lat = doc_ref.get().to_dict()['destination']['latitude']
end_lon = doc_ref.get().to_dict()['destination']['longitude']
endGPS = [end_lat, end_lon]