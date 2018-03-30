#카페 1879 - concat 연습

import pandas as pd

afile = 'a.csv'
bfile = 'b.csv'

atable = pd.read_csv(afile, encoding='utf=8', index_col=0, header=0)
btable = pd.read_csv(bfile, encoding='utf-8', index_col=0, header=0)

print(atable)
print('-'*50)
print(btable)
print('-'*50)

atable['pk'] = 'a'
btable['pk'] = 'b'

print(atable)
print('-'*50)
print(btable)
print('-'*50)

mylist = []
mylist.append(atable)
mylist.append(btable)
result = pd.concat(mylist, ignore_index=True)

print(result)
print('-'*50)

result.to_csv('result.csv', encoding='utf-8')
print('완료')