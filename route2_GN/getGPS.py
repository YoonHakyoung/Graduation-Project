import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase Admin SDK 설정
cred = credentials.Certificate('/Users/yoon/Downloads/safe-navigation-app-6fc08-firebase-adminsdk-sy8t7-364b14f110.json')
firebase_admin.initialize_app(cred)

# Firestore 데이터베이스에서 데이터 가져오기
db = firestore.client()
doc_ref = db.collection('GPS').document('member1@gmail.com')
doc = doc_ref.get()
if doc.exists:
    data = doc.to_dict()
    wktdata = [data['lat'], data['lon']]
    print(wktdata)
else:
    print('No such document!')