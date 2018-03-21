import urllib.request
import json
import datetime #카페 177

def getFacebookNumericID(page_name):
    #기본적인 설정 값 변수 할당
    with open('id.json', 'r') as myID : jID = json.load(myID)
    
    app_id = jID['App_id']
    app_secret = jID['App_secret_code']
    access_token = app_id +'|' + app_secret
    
    #접근 url 생성
    url = "https://graph.facebook.com/v2.8/"    #base
    url += page_name                            #node
    url += "/?access_token=%s"%(access_token)   #token
    print("url : ", url)
    
    data = getRequestUrl(url)
    with open(page_name+'FacebookNID.json', 'w') as idFile : idFile.write(data)
        
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('==[%s] url request success=='%(datetime.datetime.now()))
            return response.read().decode('utf-8')  #함수(메소드) 체이닝
        
    except Exception as err :
        print('error :', err)  
        print('==[%s] Error for URL : %s=='%(datetime.datetime.now(), url))  
        return None  
      
if __name__ == "__main__":
    #page_name = 'jtbcnews'
    #page_name = "chosun"
    getFacebookNumericID('jtbcnews')