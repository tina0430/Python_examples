#2018.03.24 기준

import pandas as pd
import urllib.request
import datetime
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

    for sido_idx in range(1,18):
        for gungu_idx in count():
            print(sido_idx, gungu_idx)
            url = "http://www.kyochon.com/shop/domestic.asp"
            url += "?sido1=%s&sido2=%s"%(sido_idx, gungu_idx+1)
            data = getRequestUrl(url)
            
            if data == None:
                break
            
            soup = BeautifulSoup(data,'html.parser')
            ulTag = soup.find('ul', attrs={"class":"list"})
            liTags = ulTag.findAll('li')
            for li in liTags:
                address = li.a.get('href')
                
                if not address:
                    break
                
                address_ = address.split("'")
                store = address_[3]
                address = address_[1]
                address_ = address.split(" ")
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
    myColumns = ('store', 'sido', 'gungu', 'address')
    myEncoding = 'utf-8'
    
    print('[%s] 교촌 매장 크롤링 시작' % datetime.datetime.now())
    result = getKynochonAddress()
    data = pd.DataFrame(result, columns=myColumns)
    data.to_csv('kyochon.csv', encoding=myEncoding, mode ='w', index=True, index_label='idx')
    print('[%s] 교촌 매장 크롤링 종료' % datetime.datetime.now())
    
if __name__ == "__main__":
    main()