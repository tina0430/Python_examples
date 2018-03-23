import re
import pandas as pd
import urllib.request
import datetime
from bs4 import BeautifulSoup
from itertools import count

def getRequestUrl(url):
    req = urllib.request.Request(url)
    code = 0
    try:
        responce = urllib.request.urlopen(req)
        if responce.getcode() == 200:
            print('[%s] Url Reqest Success' % datetime.datetime.now())
            return responce.read().decode('utf-8', errors='ignore')

    except Exception as err:
        print('Error :', err)
        return None

def getKynochonAddress():
    result = []

    for sido in range(1,18):
        for gungu in count():
            url = "http://www.kyochon.com/shop/domestic.asp"
            url += "?sido1=%s&sido2=%s"%(sido, gungu+1)
            print(url)
            data = getRequestUrl(url)
            
            if data == None:
                break
            
            soup = BeautifulSoup(data,'html.parser')
            ulTag = soup.findAll('ul', attrs={"class":"list"})
            for ul in ulTag:
                dlTag = ul.find('dl')
                store = dlTag.find('dt').text
                address = dlTag.find('dd').text
                address_ = address.split(' ')
                print(address_)
                sido = "1"
                gungu = "2"
                sublist = []
                sublist.append(store)
                sublist.append(sido)
                sublist.append(gungu)
                sublist.append(address)
                result.append(sublist)
    
    return result            
                
def main():
    result = []
    myColumns = ('store', 'sido', 'gundu', 'address')
    myEncoding = 'utf-8'
    
    print('Kyochon 매장 크롤링 시작')
    result = getKynochonAddress()
    data = pd.DataFrame(result, columns=myColumns)
    data.to_csv('kyochon.csv', encoding=myEncoding, mode ='w', index=True, index_label='index')
    print('Kyochon 매장 크롤링 종료')
    
if __name__ == "__main__":
    main()