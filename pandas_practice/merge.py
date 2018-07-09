#TODO
#1. csv 파일 읽어서 data.frame에 넣기
#2. 날짜별로 합치기
#3. csv로 저장 - 년도별로

import pandas as pd
# def merge_big_tables():
    
def merge_tables(start_date, end_date):
    print('start : ', start_date)
    for i in pd.date_range(start=start_date, end=end_date):
        i = i.strftime("%Y%m%d")
        filename = './news_'+i+'_result.csv'
        
        if i == start_date:
            table = pd.read_csv(filename, header=0, encoding='CP949')
            table = table.rename(columns={'word':'word','count':i})
        else:
            table_ = pd.read_csv(filename, header=0, encoding='CP949')
            table_ = table_.rename(columns={'word':'word','count':i})
            table = pd.merge(table, table_, on=['word'], how='outer')
            table = table.fillna(0)
    
#         print(i)
    print('end : ', end_date)
    filename = './result/news_' + start_date + '_' + end_date+'_result.csv'
    table.to_csv(filename, index = False, encoding='cp949')

if __name__ == '__main__':
#     merge_tables('20180318', '20180618')
#     merge_tables('20171218', '20180618')
#     merge_tables('20170918', '20180618')
#     merge_tables('20170618', '20180618')
    start_date = '20170618'
    end_date = '20180618'
    filename = './result/news_'+start_date+'_'+end_date+'_result.csv'
    table = pd.read_csv(filename, header=0, encoding='CP949')
    table['total'] = 0
    
    count = 0
    for i in pd.date_range(start=start_date, end=end_date):
        count += 1
        i = i.strftime("%Y%m%d")
        table['total'] = table['total'] + table[i]
    table = table[table.total > count]
    table['average'] = table['total']/count
    
    print(table)
    
    filename = './result/news_' + start_date + '_' + end_date+'_result_cut.csv'
    table.to_csv(filename, index = False, encoding='cp949')
    