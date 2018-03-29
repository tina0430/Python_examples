#데이터 추가 및 합치기 연습 (merge)

import pandas as pd

data1 = [{'name':"Eliot"},
         {'name':"Andy"},
         {'name':"Jenny"},
         {'name':"Justine"}]
df1 = pd.DataFrame(data1)
print(df1)

print('-'*50)
print('새로운 컬럼 추가하기')
df1['age']=[34,31,29, 34]
print(df1)

print('-'*50)

data2 = [{'sido':'서울'},{'sido':'경기'},{'sido':'인천'}]
df2 = pd.DataFrame(data2)
print(df2)

print('-'*50)
df3 =pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)

print('-'*50)
print('유일한 값만 추출')
print(df3.age.unique())

print('-'*50)
print('앞에서부터 2행만 조회')
print(df3.head(2))

print('-'*50)
print('특정 데이터를 기준으로 합치기 (특정 데이터이외의 데이터들이 중복되더라도 모두 표시됨)')
df3 = pd.DataFrame({"Year":[1991, 1994, 1993, 1995],
                    "Beer_Code":[11, 12, 13,14],
                    "Price":[100, 200, 300, 400]},
                    index=[1, 2, 3, 4])

df4 = pd.DataFrame({"Year":[1991, 1994, 1993, 1995],
                    "Beer_Code":[11, 12, 13,14],
                    "Price":[100, 200, 300, 400]},
                    index=[5, 6, 7, 8])

result = pd.merge(df3, df4)
print(result)

result = pd.merge(df3, df4, on = "Year")
print(result)

result = pd.merge(df3, df4, on = ["Year", "Beer_Code"])
print(result)