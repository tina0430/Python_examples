#Naver API-데이터랩
#https://developers.naver.com/docs/datalab/search/#api-%EB%AA%85%EC%84%B8

import json
import urllib.request
import datetime
        
def getResult(startDate, endDate, timeUnit, device):
    url = "https://openapi.naver.com/v1/datalab/search"
    
    with open ('id.json', 'r') as myID : 
        jID = json.load(myID)
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", jID['Client_id'])
        req.add_header("X-Naver-Client-Secret", jID['Client_secret'])
        req.add_header("Content-Type","application/json")
        jsonBody = {"startDate":startDate,"endDate":endDate,"timeUnit":timeUnit,
                    "keywordGroups":[{"groupName":"한글","keywords":["한글","korean"]},
                                     {"groupName":"영어","keywords":["영어","english"]}],
                    "device":device,"ages":["1","2"],"gender":"f"}
        body = json.dumps(jsonBody)
#         print(body)
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
        
#     print(json.loads(retData))
    return json.loads(retData) if retData != None else None 
        
def main(startDate, endDate, timeUnit, device):
    jsonResult = getResult(startDate, endDate, timeUnit, device)
    with open('datalab.json', 'w', encoding='utf-8') as fs:
        retJson = json.dumps(jsonResult, indent=4)
        fs.write(retJson)

if __name__ =="__main__":
    startDate = "2016-01-01"
    endDate = "2017-03-22"
    timeUnit = "month" #date / week / month
    device = "pc" #pc / mo
    main(startDate, endDate, timeUnit, device)
    
    #TO DO LIST
    #gender : "m" #f - 이건 받거나 안받거나 설정 해야 함
    #ages : 1~11 #어떻게 받을지 고민해봐야 함
    #키워드/그룸 설정 