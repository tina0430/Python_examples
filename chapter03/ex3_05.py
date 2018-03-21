#nonlocal, global 키워드 익히기

a = 10
b = 20
c = 30
d = 40
print('a id :', id(a))
print('b id :', id(b))
print('c id :', id(c))
print('d id :', id(d))

print('함수 수행 전  a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
print('=='*10)

def foo():
    a = 50
    b = 60
    d = 70
    print('a id (in foo) :', id(a)) #지역
    print('b id (in foo) :', id(b)) #지역
    print('c id (in foo) :', id(c)) #전역
    print('d id (in foo) :', id(d)) #지역
    print('=='*10)
    
    def bar():
        a=30  #전역 c에 이미 저장된 값이므로 전역c와 같은 값 참조
        nonlocal b  #부모의 지역변수인 b의 주소 참조
        global c    #전역변수 c의 주소 참조
        print('a id (in bar) :', id(a)) #지역
        print('b id (in bar) :', id(b)) #부모
        print('c id (in bar) :', id(c)) #전역
        print('d id (in bar) :', id(d)) #부모
        print('=='*10)
        
        c=70    #전역
        print('bar()에서 출력 1) a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
        b=80    #부모
        print('bar()에서 출력 2) a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
        b=90    #부모
        print('bar()에서 출력 3) a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
    bar()
    
    a=100   #지역
    print('foo()에서 출력 a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
    print('=='*10)
    
foo()

a=100
print('a id :', id(a))  #지역변수는 해당 함수가 종료되면 메모리에서도 지우기 떄문에 같은값 으로 변경해도 다른 주소참조
print('b id :', id(b))
print('c id :', id(c))
print('d id :', id(d))
print('함수 수행 후  a:{}, b:{}, c:{}, d{}'.format(a,b,c,d))
