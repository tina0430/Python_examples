a='Hello'   #변수 a는 'Hello'객체의 주소를 기억한다.
print(a)    #변수 a는 'Hello'객체 주소가 아닌 '안녕'겍체 주소를 기억한다.
a='안녕'
print(a)

b='Python'
print(b[1])
#b[0]='p'   #에러     #string은 immutable
b='python'  #'python'이라는 객체를 가리키게 됨.
print(b)

korea='대한민국만세'
print('1.', korea[0])
print('2.', korea[-1])
print('3.', korea[0:-1])
print('4.', korea[0:3])
print('5.', korea[1:])
print('6.', korea[:2])
print('7.', korea[-3:-1])
print('8.', korea[0:5:2])
print('9.', korea[:])