#카페 45 / 46 / 1377 / 1878 / 1879 / 162

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

data = [[10.0, np.nan], [20.0, 30.0], [np.nan, np.nan], [40.0, 50.0]]
myFrame = DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['one','two'])

print(myFrame)
print('-'*50)
print(myFrame.sum())
print('-'*50)
print(myFrame.sum(axis = 0))    #default
print('-'*50)
print(myFrame.sum(axis = 1))
print('-'*50)
print(myFrame.cumsum()) #누산메소드 - 누적합을 구해줌
print('-'*50)
print(myFrame.mean(axis = 0))
print('-'*50)
print(myFrame.mean(axis = 1))
print('-'*50)
print(myFrame.mean(axis = 1, skipna = False))
print('-'*50)
print(myFrame.describe()) #간단한 통계치 정보/%:4분위 데이터/std:표준편차
print('-'*50)
print(myFrame.idxmax())
print('-'*50)
mySeries = Series(['a', 'a', 'b', 'c', 'd'] * 2) 
#unique:중복되지 않는 데이터/top:빈도수가 가장 많은거/freq:top의 횟수
print(mySeries.describe())
print('-'*50)
print(mySeries)
myUnique = mySeries.unique()
print(myUnique)
print('-'*50)
print(mySeries.value_counts())
print('-'*50)
print(pd.value_counts(mySeries.values, sort=False))
print('-'*50)
mask = mySeries.isin(['b','c'])
print(mask)
print(mySeries[mask])
