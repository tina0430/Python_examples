from pydoc import doc
def docFunc1():
    print('DocFuunc1 호출')
    
def docFunc2(name):
    print(name, '안녕')
    return None #생략하도 None 반환

def docFucn3(arg1, arg2):
    res = arg1 + arg2
    return res

docFunc1()
print('딴짓을 하다가~~')
docFunc1()
print('함수명은 주소 :', docFunc1)    #객체의 주소 기억    
otherFucn = docFunc1             #함수 주소를 치환
otherFucn()

print('현재 파일의 객체 목록 :', globals())

print()
print(docFunc2('지희'))           #리턴값이 None이면 해당 키워드 출력
#docFunc2()                #에러 - 인수의 개수 부족
#docFunc2('만복', '행복')     #에러 - 인수의 개수 넘침
docFunc2(10)

print()
print(docFucn3(10, 20))          #동적 처리 - 숫자 전달
print(docFucn3('만복', "행복"))     #동적 자료 - 문자 전달

print()
def area_tri(a, b):
    c = a*b/2
    area_print(c)

def area_print(area):
    print('면적은', area)

area_tri(30, 20)