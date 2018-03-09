print('환영합니다.')

'''
여러 줄 주석
'''

#한 줄 주석

var1='안녕 파이썬'
print(var1)
var1=5; print(var1)
var1='문자열 기억'

a=10    #참조 변수 - 객체의 주소를 기억
b=20.5  
c=b     #객체의 주소를 치환한다.
print(a, b, c)
print('주소 출력')
print('a:', id(a))     #id() 함수로 객체변수에 기억된 주소
print('b:', id(b))
print('c:', id(c))

print(a is b, a == b)   #주소 비교, 값 비교
print(b is c, b == c)

print('변수 선언 시 대소문자를 구분함')
A=1; a=2;
print('A+a=', A+a)
print('a:', id(A))
print('b:', id(b))