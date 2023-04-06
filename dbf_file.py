import pandas as pd
from simpledbf import Dbf5

# dbf 파일 경로와 파일 이름을 지정합니다.
dbf_file = "/Users/yoon/Downloads/LSMD_CONT_LDREG_2097_경기_화성시/LSMD_CONT_LDREG_2097_41590.dbf"

# dbf 파일을 pandas 데이터프레임으로 로드합니다.
dbf = Dbf5(dbf_file, codec='euc-kr')
df = dbf.to_dataframe()

# 데이터프레임을 csv 파일로 저장합니다.
df.to_csv('/Users/yoon/Downloads/화성시.csv', index=False)
