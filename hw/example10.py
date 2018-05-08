import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
table = pd.read_csv('./theater.csv', encoding='utf-8', header=None)
table.columns = ['id','theater', 'cnt']

table = table.unstack('theater')
mytitle = 'showing count per theater'
table.columns.name = 'count'
table.index.name = 'title'

table.plot(kind='bar', rot = 0, ylim = [0,35], title = mytitle, alpha=0.8).grid(True)
plt.savefig('example07.png', dpi=400, bbox_inches='tight')