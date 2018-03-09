a=[1,2,3]
b=[10,a,20.5,True,'문자열']
print(a)
print(b)
print(id(a), id(b))

print()
friends=['오공','팔계','오정','삼장']
print('친구 구성원 목록 :',friends)
print('친구 구성원 수 :', len(friends))
print('세 번째 친한 친구는',friends[2])

friends.append('관우')
friends.remove('오정')
friends.insert(0, '장비')
friends.extend(['조조', '제갈량'])
friends.append(['조조', '제갈량'])
friends+='손권'
friends+=['손권']
print('시간이 흐른 후 친구 구성원 목록 :', friends)
print('저팔계 친구는 %d번 째'%(friends.index('팔계')+1))
print('손오공 친구가 있나? :', '오공' in friends)
print('사오정 친구가 있나? :', '오정' in friends)

print('\n슬라이싱---')
myList=[1,2,3,4,5]
print(myList[0:2])
myList=[1,2,3,['a','b','c'],4,5]
myList[0] = 100;
print(myList)
myList[3][0]='good'
print(myList)
print(myList[0], myList[3])
print(myList[3][:2])
print(myList[3][2])

print()
myList[4] = 6
print(myList)
myList.remove(6)    #6을 찾아서 삭제
print(myList)
del myList[4]       #index가 4인 항목 삭제
print(myList)
myList[3].remove('c')
del myList[3][0]
print(myList)

print()
myList=[1,2,3,4,5]
myList.sort()
print('sort 결과 :', myList)
myList.sort(reverse=True)
print('sort reverse속성 설정 결과 :', myList)

print()
myList=['123', '34', '234']
print(myList)
myList.sort()
print(myList)
myList.sort(key=int)
print(myList)

print()
myList=[3,1,2]
myList2=sorted(myList)
print(myList)
print(myList2)