#2018.03.26 기준

import re
import pandas as pd
import urllib.request
import datetime
from bs4 import BeautifulSoup 

def getRequestUrl(url):
    req = urllib.request.Request(url) 
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
#             print('[%s] Url Reqest Success' % datetime.datetime.now())
            return res.read().decode('utf-8')
    except Exception as err:
        print('Error :', err)
        return None
        
def getCheogajipAddress():
    result = []
    url = "http://www.cheogajip.co.kr/bbs/board.php?bo_table=store"
    data = getRequestUrl(url)
    soup = BeautifulSoup(data,'html.parser')
    page_end = soup.find('a', attrs={"class":"pg_page pg_end"}).get('href')
    page_end = re.findall(r'[0-9]+', page_end)[0]
    page_end = int(page_end)
    page_idx = 1
    
    for page_idx in range(1, page_end+1):
        print(page_idx)
        url = "http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s"%page_idx
        data = getRequestUrl(url)
        
        if data == None: 
            break
        
        soup = BeautifulSoup(data,'html.parser')
        trs = soup.find('tbody').findAll('tr')
        for tr in trs:
            store = tr.td.find_next_sibling().text
            address = tr.find('td', attrs = {"class":"td_subject"}).text
            address_ = address.split(' ')
            sido = address_[0]
            gungu = address_[1]        
        
            sublist = []
            sublist.append(store)
            sublist.append(sido)
            sublist.append(gungu)
            sublist.append(address)
            result.append(sublist)
            
    return result

def main():
    result = []
    myColums = ('store', 'sido', 'gungu', 'address')
    myEncoding = 'utf-8'
    
    print('[%s] 처가집 매장 크롤링 시작' % datetime.datetime.now())
    result = getCheogajipAddress()
    data = pd.DataFrame(result, columns=myColums)
    data.to_csv('choegajip.csv',encoding=myEncoding, mode='w', index=True, index_label='idx')
    print('[%s] 처가집 매장 크롤링 종료' % datetime.datetime.now())

if __name__ == "__main__":
    main()