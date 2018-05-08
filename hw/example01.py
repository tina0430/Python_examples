import pandas as pd

def getMovieTable():
    return pd.read_csv('./movie.csv', encoding='utf-8', index_col=0, header=0)
    
if __name__ == '__mai__':
    print(getMovieTable())