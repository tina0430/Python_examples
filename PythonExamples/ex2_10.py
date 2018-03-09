a={1,2,3,1}
print('set형 변수 a의 객체 값은',a)
print('a의 길이는', len(a))

print()
b={3,4}
print('함수를 이용한 합,차,교집합')
print('a와 b의 합집합:', a.union(b))
print('a와 b의 차집합:', a.difference(b))
print('a와 b의 교집합:', a.intersection(b))

print('?를 이용한 합,차,교집합')
print('a와 b의 합집합(a|b):', (a|b))
print('a와 b의 차집합(a-b):', (a-b))
print('a와 b의 교집합(a&b):', (a&b))

print('이러한 과정을 거쳐도 a는 그대로',a)

#print(b[0])        #에러 - 세트는 인덱싱이 불가하다
b.add(5)
print('숫자 5를 add 후 b는', b)
b.add((12,13))
print('튜플(12,13)을 add 후 b는', b)
#b.add([12,13])     #에러 - 리스트는 add로 추가가 불가하다
#b.add({12,13})     #에러 - 세트는 add로 추가가 불가하다
b.update({6,7})
print('세트 {6,7}을 update후 b는', b)
b.update([8,9])
print('리스트 [8,9]를 update후 b는', b)
b.update((10,11))
print('튜플(10,11)을 update후 b는', b)

b.remove(7)         #요소 삭제 : 값 7을 삭제 (없으면 오류)
b.discard(6)        #요소 삭제 : 값 6을 삭제 (없으면 통과)
print('요소 삭제 후 b는', b)

c=set()
print('c를 출력하면', c)
print('c의 type:', type(c))
c=b
print('b를 대입한 c를 출력하면', c)
c.clear()
print('clear 후 c:',c)
b.clear()
print('clear 후 b:',b)

print('\n자료형 사이의 형변환')
print('a는',a)
print('tuple(a)는',tuple(a))
print('list(a)는', list(a))
print('set(a)는', set(a))

print()
print('set type을 이용하여 list type의 중복 자료 제거하기')
myList=[1,3,2,3,2]
print('List type의 myList는', myList)

tmp=set(myList)
myList=list(tmp)
print('변환 후 myList:', myList)