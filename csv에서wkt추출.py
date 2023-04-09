import pandas as pd

# csv 파일 읽어오기
df = pd.read_csv("서울시 대로변 횡단보도 위치정보.csv", encoding='euc-kr', header=None)

# 첫번째 행 제거하기
df = df.iloc[1:]

# NODE 열에 NODE값이 포함된 행만 선택하기
node_df = df[df[0].str.contains("NODE")]

# WKT 형식에서 위도(latitude)와 경도(longitude) 추출하기
nodes = node_df.iloc[:, 1].str.replace(r"POINT\(", "").str.replace(r"\)", "")
new_df = pd.DataFrame({'latitude': nodes.str.split(" ").str[1].astype(float), 'longitude': nodes.str.split(" ").str[0].astype(float)})


# 새로운 CSV 파일로 저장
new_df.to_csv("대로변.csv", index=False)
