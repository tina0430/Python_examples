# 다음과 같은 list가 있다.
# pandas의 Series와 numpy를 이용하여 절대 값으로 변경한 후, 
# 각 요소들의 제곱의 합을 구하는 프로그램을 작성하세요. 
from pandas import Series
import numpy as np 

data = [-1, 2, 4, -3, -2]

s = Series(data)

total = np.sum(np.power(np.abs(s), 2))
print(total)

#약간의 응용
total_odd = np.sum(np.power(np.abs(s[::2]), 2))
print(total_odd)

total_even = np.sum(np.power(np.abs(s[1::2]), 2))
print(total_even)
