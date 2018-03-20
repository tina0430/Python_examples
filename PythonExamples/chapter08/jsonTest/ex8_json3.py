import json
import requests

def goFunc():
    base_url="http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5"
    source_code = requests.get(base_url)
    
    plain_text = source_code.text
    print(plain_text)
    
    print()
    json_data = json.loads(plain_text)
    print(json_data)
    
    print()
    print(json_data['SeoulLibraryTime']['RESULT']['CODE'])
    
    print()
    print(json_data['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])
    print(json_data['SeoulLibraryTime']['row'][0]['ADRES'])
    print(json_data['SeoulLibraryTime']['row'][0]['TEL_NO'])
    
    
    print()
    print(json_data['SeoulLibraryTime']['row'][1]['LBRRY_NAME'])
    print(json_data['SeoulLibraryTime']['row'][1]['ADRES'])
    print(json_data['SeoulLibraryTime']['row'][1]['TEL_NO'])
    
    print()
    for i in range(len(json_data['SeoulLibraryTime']['row'])):
        print(json_data['SeoulLibraryTime']['row'][i]['LBRRY_NAME'])
    
if __name__ =="__main__":
    goFunc()