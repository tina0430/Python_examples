import json
import datetime
import urllib.request

#Naver API-검색
def getRequestUrl(url):
    with open ('id.json', 'r') as myID : 
        jID = json.load(myID)
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", jID['Client_id'])
        req.add_header("X-Naver-Client-Secret", jID['Client_secret'])
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success : %s"%(datetime.datetime.now(), url))
            return response.read().decode('utf-8')
#         else:
#             print(response.getcode())
        
    except Exception as err :
        print("error type :", err)
        print("[%s] Error for URL : %s"%(datetime.datetime.now(), url))

def getNaverSearchResult(sNode, search_text, start_page, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/"+sNode+".json"
    parameters = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(search_text), start_page, display)
    url = base+node+parameters
#     print(url)
    
    reData = getRequestUrl(url)
    
    if reData == None:
        return None
    else:
        return json.loads(reData)

def getPostData(post, jsonResult):
    title = post['title']
    description = post['description']
    org_link = ['orginallink']
    link = ['link']
    
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    
    jsonResult.append({'title':title,
                       'description':description,
                       'org_link':org_link,
                       'link':link,
                       'pDate':pDate})
    return

def main(sNode):
    jsonResult = []     #최종 결과물을 담을 리스트
    search_text = '미투'  #검색할 키워드
    display_count = 100 #1회 검색시 100개 가져오겠다.
    
    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
    
    while ((jsonSearch != None) and (jsonSearch['display'] != 0)) :
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)
        nStart = jsonSearch['start']+jsonSearch['display']
        print('nStart :', nStart) #1000건 이상은 유료
        if nStart >= 1000 :
            break
        jsonSearch=getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open('%s_naver_%s.json'%(search_text, sNode), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4 , sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
 
        print('%s_naver_%s.json SAVED'%(search_text, sNode))

if __name__ == "__main__":
    #"news", "blog", "cafearticle"
    main("news")