import pandas as pd
import matplotlib.pyplot as plt
 
table = pd.read_csv('./theater.csv', encoding='utf-8', 
                    names=['id','theater'], header=None)

table = table.unstack('theater')
table.index.name = 'title'
table.columns = 'count'
# table.columns.name = 'count'

mytitle = 'showing count per theater'
print(table)
table.plot(kind='bar', rot=0, ylim=[0, 35], title=mytitle, grid=True, alpha=0.8)
plt.savefig('example07.png', dpi=400, bbox_inches='tight')
# plt.show()
