#카페 1878

import pandas as pd

filename = 'pivotFile.cvs'
data = pd.read_csv(filename, encoding='utf-8', header=0)
print('-'*50)
print(data)

pivotData = data.pivot(index='name', columns='item', values='value')
print('-'*50)
print(pivotData)
