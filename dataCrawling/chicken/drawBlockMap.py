import pandas as pd

def setTable(store):
    filepath='./storeinfo/'
    table = pd.read_csv(filepath+store+"Modify.csv", encoding='utf-8', index_col=0, header=0)
    aaa= table.apply(lambda r : r['sido']+''+r['gungu'], axis=1).value_counts()
    print(aaa)
    
# bbq = setTable('bbq')
pelicana = setTable('pelicana')
# nene = setTable('nene')
# kyochon = setTable('kyochon')
# cheogajip = setTable('cheogajip')
# goobne = setTable('goobne')
# 
# chiken_table = pd.DataFrame({'bbq':bbq,'pelicana':pelicana, 'cheogajip':cheogajip, 
#                              'kyochon':kyochon, 'nene':nene, 'goobne':goobne}).fillna(0)
# print(chiken_table)