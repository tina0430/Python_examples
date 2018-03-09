t=('a','b','c','a')
#t='a','b','c','a'    #괄호를 적지 않아도 튜블이 되나 권장하지 않음
print('t는',t)
print('t * 2는', t*2)
print('t가 가지고 있는 원소의 개수는 %d개'%(len(t)))
print('t가 가지고 있는 \'a\'의 개수는 %d개'%(t.count('a')))
print('t가 가지고 있는 첫 번째 \'a\'의 인덱스는 ', t.index('a'))

print()
p=(1,2,3)
#p[1]=10        #에러 - 튜플은 수정이 안된다.
q=list(p)
print('리스트 q는', q)
q[1]=10
p=tuple(q)
print('튜플 p는', p)

print('\n튜플도 슬라이싱이 가능')
print('p[1:]의 결과는', p[1:])

print('\n값 교환하기')
t1=(10, 20, 30)
print('t1은', t1)
a, b, c=t1
print('a:', a, 'b:', b, 'c:', c)
c, b, a = a, b, c
t2=a, b, c
print('t2는',t2)