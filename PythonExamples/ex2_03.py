v1=3            #치환1
print("v1:%d, address:%d"%(v1, id(v1)))

v1=v2=v3=5      #복수의 기억장소를 선언하면서 초기화
print(v1, v2, v3)
print(id(v1), id(v2), id(v3))
print('출력1', end=',')
print('출력2')

v1, v2=10, 20
print(v1, v2)
v2, v1=v1, v2   #두 개의 기억장소 참조값 교환 처리
print(v1, v2)

print('값 힐딩 packing 연산')
v1, *v2=[1,2,3,4,5]
print(v1)
print(v2)

*v1, v2=[1,2,3,4,5]
print(v1)
print(v2)

*v1, v2, v3=[1,2,3,4,5]
print(v1)
print(v2)
print(v3)

v1, *v2, v3=[1,2,3,4,5]
print(v1)
print(v2)
print(v3)

v1, v2, *v3=[1,2,3,4,5]
print(v1)
print(v2)
print(v3)

#v1, v2=[1,2,3,4,5]        #에러
#v1, *v2, *v3=[1,2,3,4,5]  #에러