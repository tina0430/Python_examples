import pandas as pd
import json

fv_CFileName = '../publicData/중국(112)_해외방문객정보_2015_2017.json'
jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
print(china_table.head()) #default = 5
# print(china_table)

china_table.yyyymm = pd.to_datetime(china_table.yyyymm, format='%Y%m')
china_table['year'] = china_table.yyyymm.dt.year
china_table['month'] = china_table.yyyymm.dt.month
print(china_table.head())
# print(china_table)

china_table = china_table.set_index(['month', 'year'])['visit_cnt'].unstack(fill_value=0)
print(china_table)

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(china_table)
plt.show()