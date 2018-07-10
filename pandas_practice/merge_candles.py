import pandas as pd

#start 0 : 30초봉 기준 / 1 : 1분봉 기준
def merge_tables(files, start, index):
    if start == 0 :
        table_30s = pd.read_csv(files[0], header=0, encoding='CP949')
        table = table_30s.filter(['일자','시간', index], axis=1)
        table = table.rename(columns={'시간':' 시간_30초', index:index+'_30초'})
    
    elif start == 1 :
        table_1m = pd.read_csv(files[1], header=0, encoding='CP949')

    table_3m = pd.read_csv(files[2], header=0, encoding='CP949')
    
    table_30m = pd.read_csv(files[3], header=0, encoding='CP949')
    
    len_1m = len(table_1m) 
    len_3m = len(table_3m) 
    len_30m = len(table_30m) 

    table = table_1m.filter(['일자','시간', index], axis=1)
    table = table.rename(columns={'시간':' 시간_1분', index:index+'_1분'})
    i_3m = i_30m = 0

    for i in range(len_1m) :
        tmp = table_3m["시간"][i_3m]
        table.set_value(i, '시간_3분', tmp)
        
        tmp = table_3m[index][i_3m]
        table.set_value(i, index+'_3분', tmp)
        
        tmp = table_30m["시간"][i_30m]
        table.set_value(i, '시간_30분', tmp)
    
        tmp = table_30m[index][i_30m]
        table.set_value(i, index+'_30분', tmp)
          
        if i%3 == 0 and i_3m < len_3m-1:
            i_3m = i_3m+1
             
        if i%30 == 0 and i_30m < len_30m-1:
            i_30m = i_30m+1
    
    print(table.fillna('0.00%'))
    filename = './candle/result/merge_candles_'+index+'.csv'
    table.to_csv(filename, index = False, encoding='cp949')

if __name__ == '__main__' :
    files = ['./candle/선물_30초.csv', './candle/선물_1분.csv', 
             './candle/선물_3분.csv', './candle/선물_30분.csv']
    merge_tables(files, 1, 'RSI')
    merge_tables(files, 1, 'BB_중심선')
    merge_tables(files, 1, 'RSI+MACD')
    merge_tables(files, 1, 'OBV+Slow%K')