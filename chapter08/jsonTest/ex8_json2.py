import json
import codecs

def load_jsonfile(fname):
    try:
        with codecs.open(fname, 'rb', encoding='utf-8') as myfile:
            lines = myfile.read()   #string으로 반환
#             print(type(lines))
#             print(lines)
            jdata = json.loads(lines)
#             print(type(jdata))
            return jdata
    except ZeroDivisionError as err:
        print('error :', err)
    
filename = 'jtest.json'
mydata = load_jsonfile(filename)
print(mydata)   #사전 출력