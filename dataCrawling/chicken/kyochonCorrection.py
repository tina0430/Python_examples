import pandas as pd

filepath = './storeinfo/'
store = 'kyochon'
filename = filepath+store
table = pd.read_csv(filename+'.csv', encoding='utf-8', index_col=0, header=0)

sido_file = open('sido_alias.txt', mode = 'r', encoding='utf-8')
sido_dict={}
linelists = sido_file.readlines()
for oneline in linelists:
    sido = oneline.replace('\n', '').split(':')
    sido_dict[sido[0]] = sido[1]
sido_file.close()

gungu_file = open('gungu_alias.txt', mode = 'r', encoding='utf-8')
gungu_dict={}
linelists = gungu_file.readlines()
for oneline in linelists:
    gungu = oneline.replace('\n', '').split(':')
    gungu_dict[gungu[0]] = gungu[1]
gungu_file.close()

district_table = pd.read_csv('district.csv', encoding='utf-8')

table.sido = table.sido.apply(lambda v : sido_dict.get(v, v))
table.gungu = table.gungu.apply(lambda v : gungu_dict.get(v, v))

m = pd.merge(table, district_table, on=['sido', 'gungu'], how='outer',
             suffixes=['', '_'], indicator=True)
m_result = m.query('_merge == "left_only"')
print(m_result)

table.to_csv(filepath+store+'Modify.csv')
