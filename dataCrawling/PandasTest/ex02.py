#Series 연습

import numpy as np
import pandas as pd

mydata = np.random.randn(5)
print(mydata)
d = pd.Series(mydata)
print(type(d))
print(d)

print('-'*50)
mydata = np.random.randn(5)
myindex = ['A', 'B', 'C', 'D', 'E']
d = pd.Series(mydata, myindex)
print(d)