#2018.03.24 기준

import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

#TODO LIST
#1 전처리 - 서울, 서울틀별시 -> 서울특별시로 통일
#2 정규표현식으로 데이터 뽑기 (split 말고)
    
def getBbqAddress():
    result = []
    url = "http://www.bbq.co.kr/page/order/shop_ajax.asp"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.findAll('div', attrs={'class':'storeNearyByItem-description'})
#     print(len(tags))
    for tag in tags:
        name = tag.div.span.text
        address = tag.find('div', attrs={'class':'storeNearyByItem-address'}).text
        addressList = address.split(' ')
        sido = addressList[0]
        gungu = addressList[1]
        
        sublist = []
        sublist.append(name)
        sublist.append(sido)
        sublist.append(gungu)
        sublist.append(address)
        result.append(sublist)
        
    return result

def main():
    result = []
    myColumns = ('store', 'sido', 'gundu', 'address')
    myEncoding = 'utf-8'
    
    print('bbq 매장 크롤링 시작')
    result = getBbqAddress()
    data = pd.DataFrame(result, columns=myColumns)
    data.to_csv('bbq.csv', encoding=myEncoding, mode ='w', index=True, index_label='index')
    print('bbq 매장 크롤링 종료')
    
if __name__ == "__main__":
    main()