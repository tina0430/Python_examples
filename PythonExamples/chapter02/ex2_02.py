#type 함수 연습

print('변수 이름으로 키워드(예약어)를 써서는 안 된다.')
import keyword
print('키워드 목록 :',keyword.kwlist)

print('\n숫자 진법')
print(10, oct(10), hex(10), bin(10))
print(10,0o12, 0xa, 0b1010)

print('type(자료형) 확인')
print(7, type(7))
print(7.2, type(7.2))
print(3+4j, type(3+4j))
print(True, type(True))
print('a', type('a'))

myTuple=(1,)
myList=[1]
mySet={10}
myDict={'key':201}
print(myTuple, type(myTuple))
print(myList, type(myList))
print(mySet, type(mySet))
print(myDict, type(myDict))