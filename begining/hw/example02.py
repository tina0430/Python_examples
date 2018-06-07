import pandas as pd

def getMovieTable():
    myColumns = ['id','theater', 'cnt']
    table = pd.read_csv('./theater.csv', encoding='utf-8', header=None)
    table.columns = myColumns
    table = table.set_index('id')
    return table
    
if __name__ == '__main__':
    print(getMovieTable())