#인수 키워드로 매핑하기

def showPlus(start, end=5):
    print('start:%d | end:%d | sum:%d'%(start, end, start+end))
    
showPlus(2, 3)
showPlus(3)
showPlus(start=2, end=3)
showPlus(end=4, start=3)
showPlus(2, end=3)

#아래의 경우 에러
#showPlus(start=2, 3)    #두 번쨰 인자가 상수이면 안된다
#showPlus(end=2, 3)      #non-keyword atg

print('\n가변 인수 처리')
def func1(*ar):
    print(ar, type(ar))
    for i in ar :
        print('음식:' + i)
        
func1('비빕밥', '김밥', '볶음밥')

print()
def func2(a, *ar):
    print(a)
    print(ar)
    for i in ar :
        print('배고플 떄:' + i)
func2('비빔밥', '김밥', '볶음밥')
print()
func2('짜장', '짬뽕')