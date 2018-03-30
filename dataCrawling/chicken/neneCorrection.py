import pandas as pd

def setNewAddress(store):
    filepath = './storeinfo/'
    filename = filepath+store
    
    table = pd.read_csv(filename+'.csv', encoding='utf-8', index_col=0, header=0)
    
#     print('보정 전 데이터')
#     print(table.sido.unique())
    
    sido_file = open('sido_alias.txt', mode='r', encoding='utf-8')
    sido_dict={}
    linelists = sido_file.readlines()
    for oneline in linelists:
        sido=oneline.replace('\n', '').split(':')
        sido_dict[sido[0]] = sido[1]
    sido_file.close()
    
    table.sido = table.sido.apply(lambda v : sido_dict.get(v, v))
    sido_table = pd.read_csv('district.csv', encoding='utf-8')
    m = pd.merge(table, sido_table, on=['sido', 'gungu'], how='outer', 
                 suffixes=['','_'], indicator=True)
    m_result = m.query('_merge == "left_only"')
#     print(m_result[['sido', 'gungu']])
    
    print('\n보정 후 데이터')
    print(table.sido.unique())
    
    gungu_file = open ('gungu_alias.txt', mode='r', encoding='utf-8')
    gungu_dict={}
    linelists = gungu_file.readlines()
    for oneline in linelists:
        gungu = oneline.replace('\n', '').split(':')
        gungu_dict[gungu[0]]=gungu[1]
    gungu_file.close()
    print(gungu_dict)
    
    table.gungu = table.gungu.apply(lambda v :gungu_dict.get(v, v))
    m = pd.merge(table, sido_table, on=['sido', 'gungu'], how='outer', 
                 suffixes=['','_'], indicator=True)
    m_result = m.query('_merge == "left_only"')
#     print(m_result[['sido', 'gungu']])
    
    #특이한 데이터
    table.loc[((table.sido == '경상북도') & (table.gungu == '남구')), 'gungu'] = '포항시'
    
    
    table.to_csv(filename+'Modify.csv', encoding='utf-8')
    
    print('완료')
    
    m = pd.merge(table, sido_table, on=['sido', 'gungu'], how='outer', 
                 suffixes=['','_'], indicator=True)
    m_result = m.query('_merge == "left_only"')
    print(m_result[['sido', 'gungu']])
    
if __name__ == '__main__':
    setNewAddress('nene')