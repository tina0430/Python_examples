import pandas as pd

file_30s = './candle/candle_30s.csv'
table = pd.read_csv(file_30s, header=0, encoding='CP949')
len_30s = len(table) 
print(len_30s)

file_1m = './candle/candle_1m.csv'
table_1m = pd.read_csv(file_1m, header=0, encoding='CP949')
print(len(table_1m))
    
file_3m = './candle/candle_3m.csv'
table_3m = pd.read_csv(file_3m, header=0, encoding='CP949')
print(len(table_3m))

file_30m = './candle/candle_30m.csv'
table_30m = pd.read_csv(file_30m, header=0, encoding='CP949')
print(len(table_30m))

print('='*30)
for i in range(len_30s) :
    tmp = table_1m["time"][int(i/2)]
    table.set_value(i, 'val_1m', tmp)
    tmp = table_3m["time"][int(i/6)]
    table.set_value(i, 'val_3m', tmp)
    tmp = table_30m["time"][int(i/60)]
    table.set_value(i, 'val_30m', tmp)
