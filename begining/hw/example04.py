from hw.example01 import getMovieTable

table = getMovieTable()
table = table.groupby('genre')['genre'].count()
print(table)