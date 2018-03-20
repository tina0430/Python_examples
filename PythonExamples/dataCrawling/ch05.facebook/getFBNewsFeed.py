import urllib.request
import json
from getFBNumericID import getFacebookNumericID

def getFacebookNewsFeed(page_name):
    
    with open('id.json', 'r') as myID:
        jID = json.load(myID)
    app_id = jID['App_id']
    app_secret = jID['App_secret_code']
    
    with open(page_name+'FacebookNID.json', 'r') as myID:
        jID = json.load(myID)
    page_id = jID['id']
    
    #[code 1]
    from_date ="2018-03-18" #검색 시작일
    to_date ="2018-03-20" #검색 종료일
    
    num_statuses = "10" # 1회 조회시 가져올 post 갯수
    
    access_token = app_id +'|' + app_secret
    
    #[code 2]
    url = "https://graph.facebook.com/v2.8/"
    url += page_id +"/posts/" 
    url += "?fields=id,message,link,name,type,shares,reaction,"
    url += "created_time,comments.limit(0).summary(true).limit(0).summary(true)"
    url += "&since=%s&until=%s"%(from_date, to_date)
    url += "&limit=%s&access_token=%s"%(num_statuses, access_token)
    
    #Request의 기본 method는 GET
    req = urllib.request.Request(url)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = response.read()
            data = data.decode('utf-8')
            data = json.loads(data)
            print(data)
        
    except ZeroDivisionError as err:
        print(err)
    finally:
        print('완료') 
    

if __name__ =="__main__" :
    page_name = 'jtbcnews'
    #page_name = "chosun"
    getFacebookNumericID(page_name)
    getFacebookNewsFeed(page_name)
    