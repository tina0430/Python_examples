#2018.03.24 기준

import pandas as pd
import urllib.request
import datetime
from itertools import count
import xml.etree.ElementTree as et


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
    
def getNeneStore():
    result = []
    for page_index in count():
        print(page_index)
        url = "http://nenechicken.com/subpage/where_list.asp"
        url += '?target_step2=%s' %(urllib.parse.quote('전체'))
        url += '&proc_type=step1'
        url += '&target_step1=%s' %(urllib.parse.quote('전체'))
        
        data = getRequestUrl(url)
        root = et.fromstring(data)
        for element in root.findall('item'):
            sublist = []
            sublist.append(element.findtext('aname1'))
            sublist.append(element.findtext('aname2'))
            sublist.append(element.findtext('aname3'))
            sublist.append(element.findtext('aname5'))
            result.append(sublist)
            
    return result

def main():
    result = []
    myColumns = ('store', 'sido', 'gungu', 'address')
    myEncoding = 'utf-8'
    
    print('NeNe 매장 크롤링 시작')
    result = getNeneStore()
    data = pd.DataFrame(result, columns=myColumns)
    data.csv('nene.csv', mode='w', idx=True, index_label='index', encoding=myEncoding)
    print('NeNe 매장 크롤링 종료')

if __name__ == "__main__":
    main()