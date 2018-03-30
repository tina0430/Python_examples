#계층적 색인 연습

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# from pandas.indexes.multi import MuliIndex

myindex = [['강감찬', '강감찬', '강감찬', '김유신', '김유신', '김유신', '이순신', '이순신', '이순신'],
           ['갑', '을', '병', '갑', '을', '병', '갑', '을', '병']]
myseries = Series((np.arange(9)+1)*10, myindex)
print('-'*50)
print(myseries.index)
print('-'*50)
print(myseries)
print('-'*50)
print(myseries['강감찬'])
print('-'*50)
print(myseries[['강감찬', '이순신']])
print('-'*50)
print(myseries[:, '을'])
print('-'*50)
print(myseries.unstack())
print('-'*50)
print(myseries.unstack().stack())

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
font_location = "C:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
sns.heatmap(myseries.unstack())
plt.show()
