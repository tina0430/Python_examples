# 다음 코드들을 이용하여 엑셀 파일을 작성하시오.
# abc.csv 파일의 내용
# 이름,나이
# 김철수,10
# 박영희,20

import pandas as pd

data = [{'이름':'김철수'},{'이름':'박영희'}]
data2 = {'이름':['김철수','박영희']}
df = pd.DataFrame(data2)

df['나이'] =[10, 20]
print(df)
df.to_csv('abc.csv')

print('-'*50)

s1 = pd.Series(['김철수', '박영희'])
s2 = pd.Series([10, 20])

df1 = pd.DataFrame({'이름':s1})
df2 = pd.DataFrame({'나이':s2})

df3 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)

print('-'*50)

#사전은 순서가 없어서 꼭 이름-나이 순으로 저장되지만은 않는다
df4 = pd.DataFrame({'이름':s1, '나이':s2})
print(df4)