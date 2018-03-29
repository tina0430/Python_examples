import pandas as pd

result = [] #목록을 저장할 리스트
myColumns = ('번호', '이름', '나이')
myEncoding = 'utf-8'

for idx in range(1, 3):
    sublist = []
    sublist.append(100*idx)
    sublist.append('김철수'+str(idx))
    sublist.append(999)
    result.append(sublist)

#data : 데이터 프레임
data = pd.DataFrame(result, columns=myColumns)

data.to_csv('mypandas.csv', encoding=myEncoding, mode ='w', index=True, index_label=' ')
