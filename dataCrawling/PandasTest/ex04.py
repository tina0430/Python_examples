import pandas as pd
import numpy as np

myindex = ['a','b','c','d','e']
d = pd.Series(7, index = myindex)
print(d)

print('-'*50)

s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print('s[0]\n', s[0], sep = '')
print('\ns[:3]\n', s[:3], sep = '')
print('\ns[[4, 1]]\n', s[[4, 1]], sep = '') 

print('-'*50)
print('요소명 함수 연산 가능')
print(np.power(s, 2))
print(np.power(s, 3))
print(np.sum(np.power(s, 2)))