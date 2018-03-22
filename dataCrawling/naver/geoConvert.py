import urllib.request
import json
import datetime

#Naver API-지도
def getRequestUrl(url):
    with open('id.json', 'r') as myID :
        jID = json.load(myID)
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", jID['Client_id'])
        req.add_header("X-Naver-Client-Secret", jID['Client_secret'])
    try :
        response = urllib.request.urlopen(req)
        
        if response.getcode() == 200:
            print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
        else:
            print(response.getcode())
    except Exception as err:
        print('error type :', err)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(), url))
    
def getGeoData(address):
    base = "https://openapi.naver.com/v1/map/geocode"
    node=""
    parameters="?query=%s"%urllib.parse.quote(address)
    url = base+node+parameters
    
    retData = getRequestUrl(url)
    
    if retData ==None:
        return None
    else:
        return json.loads(retData)

def main(address):
    jsonResult = getGeoData(address)
    
    if 'result' in jsonResult.keys():
        print('총 검색 결과 :', jsonResult['result']['total'])
        print('검색어 :',jsonResult['result']['userquery'])
        
        for item in jsonResult['result']['items']:
            print("="*20)
            print('주소 :', item['address'])
            print('위도 :', str(item['point']['y']))
            print('경도 :', str(item['point']['x']))

if __name__ == "__main__":
    address = '서울특별시 종로구 사직로 161 경복궁'
    main(address)