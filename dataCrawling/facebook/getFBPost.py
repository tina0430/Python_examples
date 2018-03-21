import json
import datetime
from dataCrawling.facebook import getFBNumericID as getN
from dataCrawling.facebook import getFBNewsFeed as getNF

def main(page_name):
    with open('id.json', 'r') as myID:
        jID = json.load(myID)
        app_id = jID['App_id']
        app_secret = jID['App_secret_code']
        access_token = app_id +'|' + app_secret
    
    go_next = True  #다음 post가 없으면 False가 된다.
    jsonResult = []
    
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
    
    print('[%s] %s Page id is %s'%(datetime.datetime.now(), page_name, page_id))
    
    jsonPost = getNF.getFacebookNewsFeed(page_id, access_token, from_date, to_date, num_statuses)
    print(jsonPost)
    if jsonPost == None:
        print("There are no datas")
        exit()
        
    while go_next:
        for post in jsonPost['data']:
            getPostData(post, access_token, jsonResult)
        if 'next' in jsonPost['paging'].keys() :
            jsonPost = json.loads(getN.getRequestUrl(jsonPost['paging']['next']))
        else :
            go_next = False
            
def getPostData(post, access_token, jsonResult):
    post_id = getPostItem(post, 'id')
    post_message = getPostItem(post, 'message')
    post_name = getPostItem(post, 'name')
    post_link = getPostItem(post, 'link')
    post_type = getPostItem(post, 'type')
    
    post_num_reactions = getPostTotalCount(post, 'reaction')
    post_num_comment = getPostTotalCount(post, 'comment')
    post_num_shares = 0 if 'shares' not in post.keys() else post['shares']['count']
    
    post_create_time = getPostItem(post, 'created_time')
    print(post_create_time)
    post_create_time = datetime.datetime.strptime(post_create_time, '%Y-%m-%dT%H:%M:%S+0000')
    print(post_create_time)
    post_create_time = post_create_time + datetime.timedelta(hours=+9)
    post_create_time = post_create_time.strftime('%Y-%m-%d %H:%M:%S')
    
    if post_create_time < '2016-02-24 00:00:00':
        reaction = getFacebookReaction(post_id, access_token)
    else:
        reaction = {}
    
    post_num_likes = getPostTotalCount(reaction, 'like')
    post_num_likes = post_num_reactions if post_create_time < '2016-02-24 00:00:00' else post_num_likes
    
    post_num_loves = getPostTotalCount(reaction, 'love')
    post_num_wows = getPostTotalCount(reaction, 'wow')
    post_num_hahas = getPostTotalCount(reaction, 'haha')
    post_num_sads = getPostTotalCount(reaction, 'sad')
    post_num_angrys = getPostTotalCount(reaction, 'angry')
    
    jsonResult.append({'post_id':post_id, 'message':post_message,
                       'name':post_name, 'link':post_link,
                       'create_time':post_create_time, 
                       'num_reactions':post_num_reactions,
                       'num_comments':post_num_comment,
                       'num_shares':post_num_shares,
                       'num_likes':post_num_likes, 'num_loves':post_num_loves,
                       'num_wows':post_num_wows, 'num_hahas':post_num_hahas,
                       'num_sads':post_num_sads, 'num_angrys':post_num_angrys})

def getFacebookReaction(post_id, access_token):
    base ="https://graph.facebook.com/v2.8"
    node = "/"+post_id
    reaction = "/?field=reaction.type(LIKE).limit(0).summary(total_count).as(like),"
    reaction += "reaction.type(LOVE).limit(0).summary(total_count).as(love),"
    reaction += "reaction.type(WOW).limit(0).summary(total_count).as(wow),"
    reaction += "reaction.type(HAHA).limit(0).summary(total_count).as(haha),"
    reaction += "reaction.type(SAD).limit(0).summary(total_count).as(sad),"
    reaction += "reaction.type(ANGRY).limit(0).summary(total_count).as(angry)"
    parameters = "&access_token=%s"%access_token
    url = base+node+reaction+parameters

    retData = getN.getRequestUrl(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def getFacebookPost (page_id, access_token, from_date, to_date, num_statuses):
    url = "https://graph.facebook.com/v2.8/"
    url += page_id +"/posts/" 
    url += "?fields=id,message,link,name,type,shares,reaction,"
    url += "created_time,comments.limit(0).summary(true).limit(0).summary(true)"
    url += "&since=%s&until=%s"%(from_date, to_date)
    url += "&limit=%s&access_token=%s"%(num_statuses, access_token)
    
    retData = getN.getRequestUrl(url)
    
    if(retData == None):
        return None
    else:
        return json.loads(retData)
    
def getPostItem(post, key):
    try:
        if key in post.keys():
            return post[key]
    except:
        return ''
    
def getPostTotalCount(post, key):
    try:
        if key in post.keys():
            return post[key]['summary']['total_count']
        else:
            return 0            
    except:
        return 0
    
if __name__ == '__main__':
    main('chosun')