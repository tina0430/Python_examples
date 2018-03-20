import requests
from bs4 import BeautifulSoup

def goFunc():
    base_url = "https://www.naver.com/index.html"
    source_code = requests.get(base_url)
    #print(source_code)
    #print(type(source_code))
    plain_text = source_code.text
    with open('source_code.txt', 'w', encoding='utf-8') as myFile:
        myFile.write(plain_text)
    
    #print(plain_text)
    convert_data = BeautifulSoup(plain_text, 'lxml')
    with open('convert_data.txt', 'w', encoding='utf-8') as myFile:
        myFile.write(str(convert_data))
        
#     print(convert_data)
#     print(type(convert_data))
     
    #for atag in convert_data.findAll('a'):
    for atag in convert_data.findAll('a', {'target':'_blank'}):
        href = atag.get('href')
        title = atag.string
        print(title, '   ', href)
    
if __name__ == "__main__":
    goFunc()