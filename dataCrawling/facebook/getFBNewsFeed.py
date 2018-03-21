import json
import datetime
from dataCrawling.facebook import getFBNumericID as getN

def main (page_name):
    with open('id.json', 'r') as myID:
        jID = json.load(myID)
        app_id = jID['App_id']
        app_secret = jID['App_secret_code']
        access_token = app_id +'|' + app_secret
    
    getN.getFacebookNumericID(page_name)
    with open('FacebookNIDs.json', 'r') as myID:
        jID = json.load(myID)
        page_id = jID[page_name]['id']
    
    if page_id == None:
        print('[%s] %s is invalid page name'%(datetime.datetime.now(), page_name))
        exit()
    
    from_date ="2018-03-18" #검색 시작일
    to_date ="2018-03-20" #검색 종료일
    num_statuses = "10" # 1회 조회시 가져올 post 갯수
    
    getFacebookNewsFeed(page_id, access_token, from_date, to_date, num_statuses)
    print('[%s] %s Newsfeeds are loaded'%(datetime.datetime.now(), num_statuses))
    
def getFacebookNewsFeed(page_id, access_token, from_date, to_date, num_statuses):
    base = "https://graph.facebook.com/v2.8"
    node = "/"+page_id +"/posts" 
    fields = "/?fields=id,message,link,name,type,shares,reaction,"
    fields += "created_time,comments.limit(0).summary(true).limit(0).summary(true)"
    duration = "&since=%s&until=%s"%(from_date, to_date)
    parameters = "&limit=%s&access_token=%s"%(num_statuses, access_token)
    url = base+node+fields+duration+parameters
    
    retData = getN.getRequestUrl(url)
    
    if(retData == None):
        return None
    else:
        return json.loads(retData)
    
if __name__ =="__main__" :
    main('jtbcnews')    #jtbcnews, chosun....
    