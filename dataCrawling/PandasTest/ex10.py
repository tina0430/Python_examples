import pandas as pd

filename = 'theater.csv'
colNames = ['id', 'theater', 'cnt']
df = pd.read_csv(filename, names=colNames, header=None)
df = df.rename(index=df.id)
df = df.reindex(columns=['theater', 'cnt'])
df.index.name = 'id'
print(df)

mygrouping = df.groupby('theater')['cnt']
print('-'*50)
print(mygrouping)
sumSeries = mygrouping.sum()
print('-'*50)
print(sumSeries)
meanSeries = mygrouping.mean()
print('-'*50)
print(meanSeries)
sizeSeries = mygrouping.size()  #개수
print('-'*50)
print(sizeSeries)   

newAggData = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
print(newAggData)