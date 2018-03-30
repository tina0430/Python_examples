#2018.03.26 기준

import re
import pandas as pd
import urllib.request
import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import count


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        responce = urllib.request.urlopen(req)
        if responce.getcode() == 200:
#             print('[%s] Url Reqest Success' % datetime.datetime.now())
            return responce.read().decode('utf-8', errors='ignore')

    except Exception as err:
        print('Error :', err)
        return None

def getKynochonAddress():
    result = []

    url = "https://www.goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome(r'C:\Python36\WebDriver\chromedriver.exe')
    wd.get(url)
    time.sleep(10)

    for page_idx in count():
        wd.execute_script('store.getList("%s")'% str(page_idx+1)) 
        print('PageIndex [%s] called' % str(page_idx+1))
        time.sleep(5)
        data = wd.page_source
        soup = BeautifulSoup(data,'html.parser')
#         print(soup)
        tbody = soup.find('tbody', attrs = {"id":"store_list"})
        for store_tr in tbody:
            trs = list(store_tr.strings)
#             print(trs)
            if trs[0] == '등록된 데이터가 없습니다.':
                return result
            store = trs[1]
            if trs[3] == ' ':
                address = trs[5]
            else:
                address = trs[6]
#                 address_ = address.split(' ')[:2]
            address_ = address.split( )
            sido = address_[0]
            gungu = address_[1]
            sublist = []
            sublist.append(store)
            sublist.append(sido)
            sublist.append(gungu)
            sublist.append(address)
            result.append(sublist)
            
        data = getRequestUrl(url)
    
        if data == None:
            break

    return result            
                
def main():
    result = []
    myColumns = ('store', 'sido', 'gungu', 'address')
    myEncoding = 'utf-8'
    
    print('[%s] 굽네 매장 크롤링 시작' % datetime.datetime.now())
    result = getKynochonAddress()
    data = pd.DataFrame(result, columns=myColumns)
    data.to_csv('goobne.csv', encoding=myEncoding, mode ='w', index=True, index_label='idx')
    print('[%s] 굽네 매장 크롤링 종료' % datetime.datetime.now())
    
if __name__ == "__main__":
    main()