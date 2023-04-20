import requests

url = 'http://127.0.0.1:5000/api'
headers = {'Content-Type': 'application/json'}

data = {'data':{'startID': [37.504603 ,127.024747],'endID':[37.507876, 127.026821]}}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('Error')



