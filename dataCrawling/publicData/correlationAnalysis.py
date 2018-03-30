#서울시 주요 관광지 외국인 입장객과 국내 방문 국가 별 외국인 상관관계 분석

import json
import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import pandas as pd
# from dataCrawling.publicData import tourPointVisitor
# from dataCrawling.publicData import getvisitorCount

def correlation(x, y):
    n = len(x)
    vals = range(n)
    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0
    
    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i])*float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)
        
        try:
            r = ((n*mul_xy_sum)-(x_sum*y_sum))
            r /= math.sqrt( ((n*x_sum_pow)-pow(x_sum, 2)) * ((n*y_sum_pow)-pow(y_sum, 2)) )
        except Exception as err:
            print('Error :', err)
            r = 0.0
            
    return r

def setScatterGraph(tour_table, visit_table, tourpoint):
    #그래프에 한글 입력하려고 함
    font_location = "C:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)
    
    #tour_table의 reNm이랑 tourpoint가 같아야만 해당 데이터 프레임 반환 - where과 비슷한 개념 
    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour, visit_table, left_index=True, right_index=True)
    print(merge_table)
    
    fig = plt.figure()
    fig.suptitle(tourpoint+'상관관계 분석')
    
    plt.subplot(1,3,1)
    plt.xlabel('중국인 입국수')
    plt.ylabel('외국인 입장객수')
    r = correlation(list(merge_table['china']), list(merge_table['ForNum']))
    plt.title('r={:.5f}'.format(r))
    plt.scatter(list(merge_table['china']), list(merge_table['ForNum']), 
                edgecolor='none', alpha=0.75, s = 6, c='black')
    
    plt.subplot(1,3,2)
    plt.xlabel('일본인 입국수')
    plt.ylabel('외국인 입장객수')
    r = correlation(list(merge_table['japan']), list(merge_table['ForNum']))
    plt.title('r={:.5f}'.format(r))
    plt.scatter(list(merge_table['japan']), list(merge_table['ForNum']), 
                edgecolor='none', alpha=0.75, s = 6, c='black')
    
    plt.subplot(1,3,3)
    plt.xlabel('미국인 입국수')
    plt.ylabel('외국인 입장객수')
    r = correlation(list(merge_table['usa']), list(merge_table['ForNum']))
    plt.title('r={:.5f}'.format(r))
    plt.scatter(list(merge_table['usa']), list(merge_table['ForNum']), 
                edgecolor='none', alpha=0.75, s = 6, c='black')
    
    plt.tight_layout()
    
    plt.show()
    
def main():
    #파일 읽어와서 데이터 프레임으로 만들기
    tpFileName = './서울특별시_관광지입장정보_2015_2017.json'
    jsonTP = json.loads(open(tpFileName, 'r', encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum'))
    tour_table = tour_table.set_index('yyyymm')

    #관광지 이름 저장
    resNm = tour_table.resNm.unique()
    
#     getvisitorCount.main('중국', 2015, 2017)
    fv_CFileName = './중국(112)_해외방문객정보_2015_2017.json'
    jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
    print(jsonFV)
    china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    
#     getvisitorCount.main('일본', 2015, 2017)
    fv_JFileName = './일본(130)_해외방문객정보_2015_2017.json'
    jsonFV = json.loads(open(fv_JFileName, 'r', encoding='utf-8').read())
    print(jsonFV)
    japan_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    
#     getvisitorCount.main('미국', 2015, 2017)
    fv_AFileName = './미국(275)_해외방문객정보_2015_2017.json'
    jsonFV = json.loads(open(fv_AFileName, 'r', encoding='utf-8').read())
    print(jsonFV)
    usa_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    
    fv_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    fv_table = pd.merge(fv_table, usa_table, left_index=True, right_index=True)
    
    for tourpoint in resNm:
        setScatterGraph(tour_table, fv_table, tourpoint)
        
if __name__ == "__main__":
    main()