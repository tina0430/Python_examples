import pandas as pd

files = ['./candle/30초.csv', './candle/1분.csv', './candle/3분.csv', './candle/30분.csv']

# table_30s = pd.read_csv(files[0], header=0, encoding='CP949')
# len_30s = len(table_30s) 

table_1m = pd.read_csv(files[1], header=0, encoding='CP949')

table_3m = pd.read_csv(files[2], header=0, encoding='CP949')
table_3m = table_3m.filter(['시간', 'OBV+Slow%K'], axis=1)

table_30m = pd.read_csv(files[3], header=0, encoding='CP949')
table_30m = table_30m.filter(['시간', 'OBV+Slow%K'], axis=1)

len_1m = len(table_1m) 
len_3m = len(table_3m) 
len_30m = len(table_30m) 

print(len_1m)
print(len_3m)

table = table_1m.filter(['일자','시간', 'OBV+Slow%K'], axis=1)
table = table.rename(columns={'시간':' 시간_1분', 'OBV+Slow%K':'OBV+Slow%K_1분'})
print(table.head(5))
i_3m = i_30m = 0


for i in range(len_1m) :
    tmp = table_3m["시간"][i_3m]
    table.set_value(i, '시간_3분', tmp)
    
    tmp = table_3m["OBV+Slow%K"][i_3m]
    table.set_value(i, 'OBV+Slow%K_3분', tmp)
     
    tmp = table_30m["시간"][i_30m]
    table.set_value(i, '시간_30분', tmp)

    tmp = table_30m["OBV+Slow%K"][i_30m]
    table.set_value(i, 'OBV+Slow%K_30분', tmp)
      
    if i%3 == 0 and i_3m < len_3m-1:
        i_3m = i_3m+1
         
    if i%30 == 0 and i_30m < len_30m-1:
        i_30m = i_30m+1
        
#     30초 기준
#     tmp = table_1m["OBV+Slow%K_1분"][int(i/2)]
#     table.set_value(i, 'OBV+Slow%K_1분', tmp)
#     tmp = table_1m["시간"][int(i/2)]
#     table.set_value(i, '시간_1분', tmp)
#     tmp = table_3m["OBV+Slow%K"][int(i/6)]
#     table.set_value(i, 'OBV+Slow%K_3분', tmp)
#     tmp = table_3m["시간"][int(i/6)]
#     table.set_value(i, '시간_3분', tmp)
#     
#     tmp = table_30m["OBV+Slow%K"][int(i/60)]
#     table.set_value(i, 'OBV+Slow%K_30분', tmp)
#     tmp = table_30m["시간"][int(i/60)]
#     table.set_value(i, '시간_30분', tmp)

print(table.fillna('0.00%'))
filename = './candle/merge_candles.csv'
table.to_csv(filename, index = False, encoding='cp949')