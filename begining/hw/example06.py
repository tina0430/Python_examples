import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
 
table = pd.read_csv('./theater.csv', encoding='utf-8', header=None)
table.columns = ['id','theater', 'cnt']
table = table.set_index('theater')
table = table.groupby('theater').mean()
# print(table)

font_location = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

mytitle = 'showing count per theater'
table.plot(kind='bar', rot= 15, color='yellow', title=mytitle, alpha=0.7).grid(True)
plt.savefig('example06.png', dpi=400, bbox_inches='tight')
plt.show()