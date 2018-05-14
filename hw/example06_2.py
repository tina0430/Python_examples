import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
 
table = pd.read_csv('./theater.csv', encoding='utf-8', names = ['id','theater', 'cnt'], header=None)
table = table.groupby('theater').mean()
mySeries = table['cnt']
print(mySeries)

font_location = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

N = mySeries.size
ind = np.arange(N)
width = 0.35
men_std = (2, 3, 4)
ax = plt.subplot()
rects1 = ax.bar(ind, mySeries, width, color='blue', yerr=men_std)

ax.set_xlabel('Theater Name')
ax.set_ylabel('Showing Average Count')
ax.set_title('showing count per theater')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('CGV', 'Daehan', 'Mega'))

xleft = -0.5
xright = N + 0.5 ;
ax.set_xlim([xleft, xright])
ax.legend([rects1[0]], 'Count')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height), ha='center', va='bottom')

autolabel(rects1)
plt.show()
