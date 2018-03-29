#Data Frame 연습

import pandas as pd

data1 = {
    'one' : pd.Series([1., 2., 3.], index = ['a', 'd', 'b']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
    }

print(type(data1))
print(data1)

df1 = pd.DataFrame(data1)
print(type(df1))
print(df1)

print('-'*50)
data2 = {
    'one':pd.Series([1., 2., 3.]),
    'two':pd.Series([1., 2., 3., 4.])}
df2 = pd.DataFrame(data2)
print(df2)

data3 = [{'a':1, 'b':2}, {'a':5, 'b':10, 'c':20}]
df3 = pd.DataFrame(data3)
print(df3)

print('-'*50)
print('색인을 넣는 경우')
df4 = pd.DataFrame(data3, index=['first','second'])
print(df4)

print('-'*50)
print('특정한 컬럼만 조회')
df5 = pd.DataFrame(data3, columns = ['a','b'])
print(df5)

print('-'*50)
print('컬럼 이름 변경')
df6 = pd.DataFrame(data3)
df6 = df6.rename(columns={'a':'Col1'})
print(df6)

print('-'*50)
print('특정 컬럼을 색인으로 이동하기')
df7 = df6.set_index('b')
print(df7)