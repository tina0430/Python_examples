import folium
import pandas as pd
import urllib.request
import datetime
import json
import webbrowser

def getRequestUrl(url):
    with open ('../naver/id.json', 'r') as myID : 
        jID = json.load(myID)
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", jID['Client_id'])
        req.add_header("X-Naver-Client-Secret", jID['Client_secret'])
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
#             print("[%s] URL Request Success : %s"%(datetime.datetime.now(), url))
            return response.read().decode('utf-8')        
    except Exception as err :
        print("error type :", err)
        print("[%s] Error for URL : %s"%(datetime.datetime.now(), url))


def getGeoData(address):
    base = 'https://openapi.naver.com/v1/map/geocode'
    
    try:
        parameters = '?query='+urllib.parse.quote(address)
    except Exception as err:
        print (err)
        return None
        
    url=base+parameters
    
    retData = getRequestUrl(url)
    
    if retData == None:
        return None
    
    jsonAddress = json.loads(retData)
#     print(jsonAddress)
    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else:
        return None
    
    return [latitude, longitude]
        
def main():
    latitude = 37.5666512
    longitude = 126.9696842
    
    mymap = folium.Map(location=[latitude, longitude], zoom_start=1)
    store_list = ['bbq', 'pelicana','nene','kyochon', 'goobne','cheogajip']
    colors={'bbq':'red', 'pelicana':'black', 'nene':'purple', 
            'kyochon':'green', 'goobne':'blue', 'cheogajip':'orange'}
    
    for store in store_list:
        print('-'*50)
        print(store)
        print('-'*50)
        filepath = '../test/storeinfo/'
        position = '강동구'
        geoData = []
        filename = filepath+store+'Modify.csv'
        df = pd.read_csv(filename, encoding='utf-8', index_col = 0, header = 0)
        
        df = df[df.gungu == position]
        for idx , row in df.iterrows():
            print(colors[store])
            address = row['address']
            geoData = getGeoData(address)
#             print(idx, '\n', row)        
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color=colors[store])).add_to(mymap)
    
    filename = filepath+'chicken.html'
    mymap.save(filename)
#     webbrowser.open(filename)
if __name__ == "__main__":
    main()