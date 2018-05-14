import pandas as pd


table = pd.read_csv('./theater.csv', encoding='utf-8', header=None)
table.columns = ['id','theater', 'cnt']

#극장별
theater_table = table.set_index('theater')
theater_table = theater_table.groupby('theater')
table1 = theater_table.sum()
table2 = theater_table.mean()
table3 = theater_table.count()
print(table3)
theater_table = pd.concat([table1, table2, table3['cnt']], axis=1)
print(theater_table)

print('-'*50)

#영화별
movie_table = table.set_index('id')
movie_table = movie_table.groupby('id')
table1 = movie_table.sum()
table2 = movie_table.mean()
table3 = movie_table.count()
table = pd.concat([table1, table2, table3['cnt']], axis=1)
print(table)