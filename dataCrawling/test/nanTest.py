import pandas as pd

filename = 'mynan.csv'

table = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)

print('원본 파일 내용')
print(table)

print('\n요소별 null체크 - notnull')
print(table.notnull())
print('\n요소별 null체크 - isnull')
print(table.isnull())

print('\ndropna 함수')
print(table.dropna(subset=['kor']))

print('\nfillna 함수')
print(table.fillna(10))