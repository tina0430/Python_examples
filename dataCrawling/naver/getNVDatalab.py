#Naver API-데이터랩

import json
import urllib.request
import datetime

        
def getResult():
    url = "https://openapi.naver.com/v1/datalab/search"
    
    with open ('id.json', 'r') as myID : 
        jID = json.load(myID)
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", jID['Client_id'])
        req.add_header("X-Naver-Client-Secret", jID['Client_secret'])
        req.add_header("Content-Type","application/json")
        body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

    try:
        data=body.encode("utf-8")
        response = urllib.request.urlopen(req, data)
        rescode = response.getcode()
        
        if rescode ==200:
            print("[%s] URL Request Success : %s"%(datetime.datetime.now(), url))
            retData = response.read().decode('utf-8')
        else:
            print("Error Code:" + rescode)
            retData = None
            
    except Exception as err :
        print("error type :", err)
        
    print(json.loads(retData))
    return json.loads(retData) if retData != None else None 
        
def main():
    jsonResult = getResult()
    with open('datalab.json', 'w', encoding='utf-8') as fs:
        retJson = json.dumps(jsonResult, indent=4)
        fs.write(retJson)

if __name__ =="__main__":
    print("뀨")
    main()
    print("뀨2")