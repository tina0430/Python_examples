import urllib.request
import json
import datetime

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] url request success'%(datetime.datetime.now()))
            return response.read().decode('utf-8')  #함수(메소드) 체이닝
        
    except Exception as err : 
        print('[%s] Error for URL : %s'%(datetime.datetime.now(), url))  
        print('Error :', err) 
        return None  
      
def getFacebookNumericID(page_name):
    with open('id.json', 'r') as myID : 
        jID = json.load(myID)
        app_id = jID['App_id']
        app_secret = jID['App_secret_code']
        access_token = app_id +'|' + app_secret
    
    base = "https://graph.facebook.com/v2.8"    
    node = "/"+page_name                       
    token = "/?access_token=%s"%(access_token)  
    url = base+node+token   #접근 url
    
    retData = getRequestUrl(url)
    if(retData == None):
        return None
    else:
        with open('facebookNIDs.json', 'r+') as idFile :
            ids=json.load(idFile)
            keyList = ids.keys()
            if page_name in keyList:
                return
            if ids == {}:
                idFile.seek(0)
                idFile.write('{\n\t"%s":%s\n}'%(page_name, retData))
            else:
                off = idFile.tell()
                idFile.seek(off-3)
                idFile.write(',\n\t"%s":%s\n}'%(page_name, retData))
        
if __name__ == "__main__":
    getFacebookNumericID('jtbcnews')    #jtbcnews, chosun....