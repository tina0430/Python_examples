import urllib.request
import datetime
import pandas as pd
from bs4 import BeautifulSoup 
import re

#TODO LIST
#1. url가지고 html가져오기
#2. html문서에서 내가 얻고자하는 정보 뽑아오기 
#3. 뉴스의 줄임말 혹은 이하 ** 이런 단어들 전처리
#4. 맞춤법 검사 -> 명사 추출 및 비속어 학습
 
#1. url가지고 html 가져오기
def getRequestUrl(url):
    req = urllib.request.Request(url) 
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
#             print('[%s] Url Reqest Success' % datetime.datetime.now())
            return res.read().decode('utf-8', errors='ignore') #임시방편-특수 문자 나올떄마다 저장해서 치환해야 함
    except Exception as err:
        print('Error :', err)
        return None

#2. html문서에서 내가 얻고자하는 정보 뽑아오기 
#2-1. 총 몇페이지 있는지 뽑기(for문 돌릴껴)
#2-2. 기사 하나하나 내용 저장
def getNaverFinanceNews():
    result = []
    url = "http://finance.naver.com/news/news_list.nhn?mode=LSS2OD&section_id=101"
#     url += "section_id2=258" #뭔지 모르겠고 더 알아봐야 함
    url += "&date=20180502"
    url += "&office_id=014" #언론사 id
    
    print(url)

    url += "&page=1" #맨뒤 버튼에 걸려있는 링크로 총 몇페이지인지 구해서 반복문 돌리기
    data = getRequestUrl(url)
#     print(data)
    soup = BeautifulSoup(data,'html.parser')
    page_end = soup.find('td', attrs={"class":"pgRR"}).a.get('href')
    page_end = re.findall('[0-9]{1,}$', page_end)[0]
    for i in range(1,int(page_end)+1):
        new_url = url + 'page=' + str(i)
        print(new_url)
    return result
#http://finance.naver.com/news/news_list.nhn?mode=LSS2OD&section_id=101&office_id=001&page=1
#office_id 001~597까지 있으나 네이버 금융 뉴스 홈에 노출되는건 38개의 언론사
#다른 뉴스도 검색하면 검색가능 ex) 뉴스홈에서 '삼성' 검색시 4페이지에 프레시안 기사 찾을 수 있음(5/1 오후 12:04 기준)

#3. main 작성
def main():
    result = []
    myColums = ('store', 'sido', 'gungu', 'address')
    myEncoding = 'utf-8'
    
    print('[%s] 네이버 증권 크롤링 시작' % datetime.datetime.now())
    result = getNaverFinanceNews()
#     data = pd.DataFrame(result, columns=myColums)
#     data.to_csv('NaFiNews.csv', encoding=myEncoding, mode='w', index=True, index_label='idx')
    print('[%s] 네이버 증권 크롤링 종료' % datetime.datetime.now())
    
#     print('[%s] 네이버 증권 크롤링 시작' % datetime.datetime.now())
#     result = getNaverFinanceNews()
#     data = pd.DataFrame(result, columns=myColums)
#     data.to_csv('NaFiNews.csv', encoding=myEncoding, mode='w', index=True, index_label='idx')
#     print('[%s] 네이버 증권 크롤링 종료' % datetime.datetime.now())
#     
#     print('[%s] 네이버 증권 크롤링 시작' % datetime.datetime.now())
#     result = getNaverFinanceNews()
#     data = pd.DataFrame(result, columns=myColums)
#     data.to_csv('NaFiNews.csv', encoding=myEncoding, mode='w', index=True, index_label='idx')
#     print('[%s] 네이버 증권 크롤링 종료' % datetime.datetime.now())
#     
#4. main 시작
if __name__ == "__main__":
    main()