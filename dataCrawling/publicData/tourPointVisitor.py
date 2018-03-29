import urllib.request
import datetime
import json
import math

def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    try:
        response = urllib.request.urlopen(req)
        
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as err:
        print("Error message :", err)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
def getTourPointVisitor(access_key, yyyymm, sido, gungu, nPagenum, nItems):
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    parameters ="?_type=json&serviceKey="+access_key
    parameters += "&YM="+yyyymm
    parameters += "&SIDO="+urllib.parse.quote(sido)
    parameters += "&GUNGU="+urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNo="+str(nPagenum)
    parameters += "&numOfRows="+str(nItems)
    
    url = end_point + parameters
    print(url)
    retData = getRequestUrl(url)
    if retData == None:
        return None
    else:
        return json.loads(retData)
    
def getTourPointData(item, yyyymm, jsonResult):
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = '' if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    
    jsonResult.append({'yyyymm':yyyymm, 'addrDc':addrCd,
                       'gungu':gungu, 'sido':sido, 'resNm':resNm,
                       'rnum':rnum, 'ForNum':ForNum, 'NatNum':NatNum})
    return

def main(sido, nStartYear, nEndYear):
    with open('id.json', 'r', encoding='utf-8') as myID :
        jID = json.load(myID)
        access_key = jID['key']
        
    jsonResult=[]
    gungu =''
    nPagenum = 1
    nTotal = 0
    nItems = 100
    
    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = "{}{:0>2}".format(str(year), str(month))
            nPagenum = 1
            while True:
                jsonData = getTourPointVisitor(access_key, yyyymm, sido, gungu, nPagenum, nItems)
#                 print(jsonData)
#                 if not jsonData:
#                     print('데이터 없다!')
#                     break
                if jsonData['response']['header']['resultMsg'] == 'OK':
                    nTotal = jsonData['response']['body']['totalCount']
                     
                    if nTotal == 0:
                        break
                     
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)
                    nPage = math.ceil(nTotal/100)
                    if nPagenum == nPage :
                        break
                     
                    nPagenum += 1
                    
                else:
                    break
        with open('%s_관광지입장정보_%d_%d.json'%(sido, nStartYear, nEndYear), 'w', encoding='utf-8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
            
        print('%s_관광지입장정보_%d_%d.json SAVED'%(sido, nStartYear, nEndYear))
if __name__ == "__main__":
    main('서울특별시', 2015, 2017)