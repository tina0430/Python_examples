import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, style, font_manager, rc

def setTable(store):
    filepath='./storeinfo/'
    table = pd.read_csv(filepath+store+"Modify.csv", encoding='utf-8', index_col=0, header=0)
    a= table.apply(lambda r : r['sido']+''+r['gungu'], axis=1).value_counts()
    print (store)
    print(a)
    return a 

store_count=6
bbq = setTable('bbq')
pelicana = setTable('pelicana')
nene = setTable('nene')
kyochon = setTable('kyochon')
cheogajip = setTable('cheogajip')
goobne = setTable('goobne')
 
chiken_table = pd.DataFrame({'bbq':bbq,'pelicana':pelicana, 'cheogajip':cheogajip, 
                             'kyochon':kyochon, 'nene':nene, 'goobne':goobne}).fillna(0)
# print(chiken_table)

# plt.figure()
# chiken_table.sum(axis=0).iloc[:store_count].plot(kind='bar')
# plt.show()

data_draw_korea = pd.read_csv('./data_draw_korea.csv', index_col=0, encoding='utf-8', header=0)
data_draw_korea.index = data_draw_korea.apply(lambda r : r['광역시도']+''+r['행정구역'], axis=1)
# data_draw_korea.head()
chiken = pd.merge(data_draw_korea, chiken_table, how='outer', left_index=True, right_index=True)
print(chiken.shortName.unique())
chiken = chiken[~np.isnan(chiken['면적'])].fillna(0)
chiken['total'] = chiken_table.sum(axis=1)

font_name=font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

def showMap(blockedMap, targetData, strTitle, strColor, gamma):
    BORDER_LINES = [
        [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
        [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
        [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
        [(9, 12), (9, 10), (8, 10)], # 강원도
        [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
         (13, 4), (14, 4), (14, 2)], # 충청남도
        [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
         (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
        [(14, 4), (15, 4), (15, 6)], # 대전시
        [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도
        [(14, 8), (16, 8), (16, 10), (15, 10),
         (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
        [(15, 11), (16, 11), (16, 13)], # 울산시
        [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
        [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
        [(18, 5), (20, 5), (20, 6)], # 전라남도
        [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
    ]
    
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData]))*0.25
    whitelabelmin += min(blockedMap[targetData])
    
    datalabel = targetData
    
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])
    mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    cmapname = strColor
    
    plt.figure(figsize=(8,13))
    plt.title(strTitle)
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)
    
    for idx, row in blockedMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        dispname = row['shortName']
        
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 6.5, 1.5
            print(dispname)
        else:
            fontsize, linespacing = 11,1.2
            plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold', fontsize=fontsize, 
                         ha='center', va = 'center', color=annocolor, linespacing=linespacing)
            
    for path in BORDER_LINES:
        ys,xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=4)
        
    plt.gca().invert_yaxis()
    plt.axis('off')
    
    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(targetData)
    plt.tight_layout()
    
    plt.savefig(targetData+'.png')
    plt.show()
    
showMap(chiken, 'total', '6개 프랜차이즈 통닭집 분포', 'RdPu', 0.75)
showMap(chiken, 'bbq', 'BBQ 매장 분포', 'Reds', 0.75)
showMap(chiken, 'cheogajip', '처갓집 매장 분포', 'Greens', 0.75)
showMap(chiken, 'goobne', '굽네치킨 매장 분포', 'Oranges', 0.75)
showMap(chiken, 'kyochon', '교촌치킨 매장 분포', 'Greys', 0.75)
showMap(chiken, 'pelicana', '페리카나 매장 분포', 'Blues', 0.75)
showMap(chiken, 'nene', '네네치킨 매장 분포', 'Purples', 0.75)