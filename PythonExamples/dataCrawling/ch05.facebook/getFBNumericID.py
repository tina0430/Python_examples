import urllib.request
import json

def getFacebookNumericID(page_name):
    #[code 1] 기본적인 설정 값 변수 할당
    with open('id.json', 'r') as myID:
        jID = json.load(myID)
    
    app_id = jID['App_id']
    app_secret = jID['App_secret_code']
    
    access_token = app_id +'|' + app_secret
    
    #[code 2] 접근 url 생성
    url = "https://graph.facebook.com/v2.8/"    #base
    url += page_name                            #node
    url += "/?access_token=%s"%(access_token)   #token
    print("url : ", url)
    
    #[code 3] 
    req = urllib.request.Request(url)
    
    #[code 4]
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = response.read()
            data = data.decode('utf-8')
            with open(page_name+'FacebookNID.json', 'w') as idFile:
                idFile.write(data)
            data = json.loads(data)
            page_id = data['id']
            print(page_name + " Facebook Numeric id : " + page_id)
            
    except Exception as err:
        print("error :", err)
    finally:
        print('완료')
        
if __name__ == "__main__":
    #page_name = 'jtbcnews'
    #page_name = "chosun"
    getFacebookNumericID('jtbcnews')