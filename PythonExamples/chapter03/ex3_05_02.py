a = 10
b = 20
c = 30

print('함수 수행 전 a:{}, b:{}, c:{}'.format(a,b,c))

def foo():
    a = 40
    b = 50
    print('foo()에서 출력 a:{}, b:{}, c:{}'.format(a,b,c))
    
    def bar():
        nonlocal b
        global c
        print('bar()에서 출력 a:{}, b:{}, c:{}'.format(a,b,c))
    bar()
    a = 100
    #c = 60 #오류
    print('foo()에서 출력 a:{}, b:{}, c:{}'.format(a,b,c))
foo()
print('함수 수행 후 a:{}, b:{}, c:{}'.format(a,b,c))