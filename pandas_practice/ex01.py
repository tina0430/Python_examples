from pandas import Series
import pandas as pd

mySeries = Series([10, 40, 30, 20])
print(mySeries)
print(mySeries.values)
print(mySeries.index)


mySeries = Series([10, 40, 30, 20], index=['강감찬', '이순신', '김유신', '광해군'])

mySeries.name = '호호호'
mySeries.index.name = '이름'
print(mySeries)

print(mySeries['김유신'])
mySeries['광해군'] = 100

print(mySeries[['김유신', '이순신']])

print(mySeries)

print(mySeries[mySeries < 50])
print()

print(mySeries * 2)

print('이순신' in mySeries)
print('을지문덕' in mySeries)

sdata = {'서울':2000, '부산':3000, '울산':4000, '광주':5000}
mySeries1 = Series(sdata)
print(mySeries1)

city = ['서울', '부산', '울산', '목포']
mySeries2 = Series(sdata, index=city)
print(mySeries2)
print('광주' in mySeries2)

print(mySeries1 + mySeries2)