#네이버 실시간 인기 검색어 읽기

import urllib.request
from bs4 import BeautifulSoup

class findKeyword():
    def start(self):
        try:
            url = "http://www.naver.com"
            page = urllib.request.urlopen(url)
            
            soup = BeautifulSoup(page.read(), "lxml")
            #print(soup)
            titleList = soup.ol.find_all('li')
            #print(titleList)
            print('<Naver 실시간 검색어>')
            
            for i in range(0, 10) :
                print(str(i+1) + ") "+ titleList[i].text)
        except ZeroDivisionError as err:
            print('error :', err)
        finally:
            print('크롤링 완료')

findKeyword().start()