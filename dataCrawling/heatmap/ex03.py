#계층적 색인 - 두측 모두
from pandas import DataFrame
from pandas import Series
import numpy as np

myindex = [['강', '강', '이', '이'],
           ['갑', '을', '갑', '을']]
mycolumns = [['서울', '부산', '서울'],
           ['Green', 'Red', 'Green']]
myframe = DataFrame((np.arange(12).reshape(4,3)), myindex, mycolumns)
myframe.index.names = ['key1', 'key2']
myframe.columns.names = ['city', 'color']

print(myframe)
print('-'*50)
print(myframe['서울'])
