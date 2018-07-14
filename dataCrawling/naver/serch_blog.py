import json
import math
from datetime import datetime
import requests
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

#https://developers.naver.com/docs/search/blog/


naver_client_id = "XdCShjcZWRgW7JnRyCFO"
naver_client_secret = "F9RMDFMjUo"

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", naver_client_id)
    req.add_header("X-Naver-Client-Secret", naver_client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success : %s"%(datetime.now(), url))
            return response.read().decode('utf-8')

    except Exception as err :
        print("error type :", err)
        print("[%s] Error for URL : %s"%(datetime.now(), url))

def get_blog_search_result_pagination_count(search_blog_keyword, display_count):
    encode_search_keyword = urllib.parse.quote(search_blog_keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encode_search_keyword
    
    response_body_dict = json.loads(getRequestUrl(url))
    
    if response_body_dict['total'] == 0:
        blog_pagination_count = 0
        
    else:
        blog_pagination_total_count = math.ceil(response_body_dict['total'] / int(display_count))

        if blog_pagination_total_count >= 1000:
            blog_pagination_count = 1000
            
        else:
            blog_pagination_count = blog_pagination_total_count

        print("Count of post that include keyword " + search_blog_keyword + " : " + str(response_body_dict['total']))
#         print("keyword " + search_blog_keyword + "에 해당하는 블로그 실제 페이징 수 : " + str(blog_pagination_total_count))
#         print("keyword " + search_blog_keyword + "에 해당하는 블로그 처리할 수 있는 페이징 수 : " + str(blog_pagination_count))

    return blog_pagination_count


def get_blog_post(file_route, search_blog_keyword, display_count, search_result_blog_page_count, sort_type):
    encode_search_blog_keyword = urllib.parse.quote(search_blog_keyword) #urlencode

    for i in range(1, search_result_blog_page_count + 1):
        url = "https://openapi.naver.com/v1/search/blog?query=" + encode_search_blog_keyword + "&display=" + str(
            display_count) + "&start=" + str(i) + "&sort=" + sort_type
        
        response_body_dict = json.loads(getRequestUrl(url))
        
        file = open(file_route, 'w', encoding='utf-8')
        result = []
                
        for j in range(0, len(response_body_dict['items'])):
            try:
                blog_post_url = response_body_dict['items'][j]['link'].replace("amp;", "")

                get_blog_post_content_code = requests.get(blog_post_url)
                get_blog_post_content_text = get_blog_post_content_code.text

                get_blog_post_content_soup = BeautifulSoup(get_blog_post_content_text, 'lxml')

                for link in get_blog_post_content_soup.select('frame#mainFrame'):
                    real_blog_post_url = "http://blog.naver.com" + link.get('src')

                    get_real_blog_post_content_code = requests.get(real_blog_post_url)
                    get_real_blog_post_content_text = get_real_blog_post_content_code.text

                    get_real_blog_post_content_soup = BeautifulSoup(get_real_blog_post_content_text, 'lxml')
                    for blog_post_content in get_real_blog_post_content_soup.select('div#title_1'):
                        blog_post_title = blog_post_content.find('span').get_text()
                        
                    for blog_post_content in get_real_blog_post_content_soup.select('div#postViewArea'):
                        blog_post_content_text = blog_post_content.get_text()

#                         remove_html_tag = re.compile('<.*?>')
#                         blog_post_title = re.sub(remove_html_tag, '', response_body_dict['items'][j]['title'])

#                         blog_post_description = re.sub(remove_html_tag, '', response_body_dict['items'][j]['description'])
#                         blog_post_postdate = datetime.strptime(response_body_dict['items'][j]['postdate'], "%Y%m%d").strftime("%y.%m.%d")
#                         blog_post_blogger_name = response_body_dict['items'][j]['bloggername']
                        blog_post_full_contents = str(blog_post_content_text)
                        blog_post_full_contents = " ".join(blog_post_full_contents.split())
#                         remove = re.findall(r'[ .ㄱ-ㅎㅏ-ㅣ가-힣\w]+')
#                         blog_post_full_contents = " ".join(blog_post_full_contents.split())
                        print("\ntitle :" + blog_post_title)
                        print("\ncontents :" + blog_post_full_contents)
                        if len(blog_post_full_contents) > 1000 :
                            print('==================over 1000==================')
                            result.append(['title : ' + blog_post_title, 'contents : ' + blog_post_full_contents])
                        
#                         print("포스팅 URL : " + blog_post_url)
#                         print("포스팅 제목 : " + blog_post_title)
#                         print("포스팅 설명 : " + blog_post_description)
#                         print("포스팅 날짜 : " + blog_post_postdate)
#                         print("블로거 이름 : " + blog_post_blogger_name)
#                         print("포스팅 내용 : " + blog_post_full_contents)
                            
            except:
                j += 1
#         print(result)
        for i in range(len(result)):
            file.write(result[i][0]+'\n')
            file.write(result[i][1]+'\n')
        print('file saved')
        file.close()
            
def naver_blog_crawling(file_route, search_blog_keyword, display_count, sort_type):
    search_result_blog_page_count = get_blog_search_result_pagination_count(search_blog_keyword, display_count)
    get_blog_post(file_route, search_blog_keyword, display_count, search_result_blog_page_count, sort_type)
    
if __name__ == '__main__':
    keyword = "호이짜짜"
    now = datetime.today().strftime("%Y%m%d")
    route = './naver_blog_' + now + '_' + keyword + '.txt'
    naver_blog_crawling(route, keyword, 10, "sim") #sim : 유사도순 / date : 날짜순
