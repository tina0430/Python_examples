#Series 연습

import pandas as pd

mydata = {'a':0., 'b':1.,'c':2.} #1. = 1.0
d = pd.Series(mydata)
print(d)

print()
mydata = pd.Series(mydata, index=['a','b','B','c'])
print(d) #NaN : Not A Number (존재하지 않는 값)