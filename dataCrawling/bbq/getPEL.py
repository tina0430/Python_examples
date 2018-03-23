import pandas as pd
import urllib.request
import datetime
from bs4 import BeautifulSoup
from itertools import count

def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    try:
        responce = urllib.request.urlopen(req)
        code = responce.getcode()
        if code == 200:
            print('[%s] Url Reqest Success' % datetime.datetime.now())
            return responce.read().decode('utf-8', errors='ignore') #임시방편
        else:
            print('Code :', code)
            print('[%s] URL Error :%s' %(datetime.datetime.now(), url))
            
    except Exception as err:
        print('Error :', err)
        return None
        
def getPelicanaAddress():
    result = []
    for page_idx in count():
        url = "http://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=" % (page_idx+1)
        data = getRequestUrl(url)
        soup = BeautifulSoup(data, 'html.parser')
        tbl = soup.find('table', attrs={'class':'table mt20'})
        tb = tbl.find('tbody')
        print("-"*90)
        bEnd = True
        
        for tr in tb.findAll('tr'):
            bEnd = False
            mylist = list(tr.strings)
            store = mylist[1]
            address = mylist[3]
            address_ = address.split(' ')
            sido = address_[0]
            gungu = address_[1]
            
            sublist = []
            sublist.append(store)
            sublist.append(sido)
            sublist.append(gungu)
            sublist.append(address)
            result.append(sublist)
            
        if bEnd : 
            return result

def main():
    result = []
    myColumns = ('store', 'sido', 'gundu', 'address')
    myEncoding = 'utf-8'
    
    print('Pelicana 매장 크롤링 시작')
    result = getPelicanaAddress()
    print(result)
    data = pd.DataFrame(result, columns=myColumns)
    data.to_csv('pelicana.csv', mode='w', index=True, index_label='index', encoding=myEncoding)
    print('Pelicana 매장 크롤링 종료')


if __name__ == "__main__":
    main()