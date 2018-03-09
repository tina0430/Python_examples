def hap(x, y) :
    return x+y

print(hap(1,2))

#위코드를 람다로 표현
print(lambda x, y : x+y)

#람다식을 변수에 치환
a = lambda x, y : x+y
print(a(1,2))

#람다도 인수에 defailt 지정 가능
a = lambda x, y=10 : x*y
print(a(5))
print(a(5,6))

#람다도 가변 인수 지정 가능
a = lambda v, *tu, **dic : print(v, tu, dic)
a(1,3,4,2,m=4,n=5)

#다른 함수안에서 람다 사용 가능
result = list(filter(lambda a : a<5, range(10)))
print(result)

print(list(filter(lambda a : a%2, range(10))))
