from hw.example01 import getMovieTable

table = getMovieTable()

#장르가 코미디인 항목만 조회
table1 = table[table['genre'] == '코미디']
print(table1)
print()

#감독 이름이 존재하는 항목만 조회
table2 = table[table['director'].notnull()]
print(table2)
print()

#배우 이름이 존재하는 항목의 제목과 배우 이름만 조회
table3 = table[table['actor'].notnull()]
table3 = table3.reindex(columns=['title', 'actor'])
print(table3)