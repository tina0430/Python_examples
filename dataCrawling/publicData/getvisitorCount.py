#국가별 출입국 인원 수집 / 시각화

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import urllib.request
import datetime
import json

def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    try:
        responce = urllib.request.urlopen(req)
        if responce.getcode() == 200:
            print('[%s] Url Reqest Success' % datetime.datetime.now())
            return responce.read().decode('utf-8')
        
    except Exception as err:
        print('Error :', err)
        print('[%s] URL Error :'%(datetime.datetime.now(), url))
        return None
    
def getNatVisitor(access_key, yyyymm, nat_cd, ed_cd):
    
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters ="?_type=json&serviceKey="+access_key
    parameters += "&YM="+yyyymm
    parameters += "&NAT_CD="+str(nat_cd)
    parameters += "&ED_CD="+str(ed_cd)
    
    url = end_point +parameters
    retData = getRequestUrl(url)
    if retData == None:
        return None
    else:
        return json.loads(retData)

def drawGraph(index, visitYM, cnVisit):
    font_lacation = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_lacation).get_name()
    matplotlib,rc('font', family=font_name)
    
    plt.xticks(index, visitYM)
    plt.plot(index, cnVisit)
    plt.xlabel('방문월')
    plt.ylabel('방문객수')
    plt.grid(True)
    plt.show()
    
def main(nation, nStartYear, nEndYear):
    jsonResult = []
    national_codes = {'한국':100,'중국':112, '일본':130, '미국':275, '영국':316} 
    national_code = national_codes[nation]
    ed_cd="E" if national_code != 100 else "D"
    
    with open('id.json', 'r', encoding='utf-8') as myID :
        jID = json.load(myID)
        access_key = jID['key']
        
    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = "{}{:0>2}".format(str(year), str(month))
            
            jsonData = getNatVisitor(access_key, yyyymm, national_code, ed_cd)
            if jsonData['response']['header']['resultMsg'] == "OK":
                krName = jsonData['response']['body']['items']['item']['natKorNm']
                krName = krName.replace(' ','')
                iTotalVisit=jsonData['response']['body']['items']['item']['num']
                print('%s_%s : %s' % (krName, yyyymm, iTotalVisit))
                jsonResult.append({'nat_name':krName, 'nat_cd':national_code, 
                                   'yyyymm':yyyymm, 'visit_cnt':iTotalVisit})
    
    cnVisit = []
    visitYM = []
    index = []
    i = 0
    for item in jsonResult:
        index.append(i)
        cnVisit.append(item['visit_cnt'])
        visitYM.append(item['yyyymm'])
        i = i+1
    
    with open('%s(%s)_해외방문객정보_%d_%d.json'%(krName, national_code, nStartYear, nEndYear-1), 
              'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    drawGraph(index, visitYM, cnVisit)
    
if __name__ =="__main__" :
    main('중국', 2015, 2017)