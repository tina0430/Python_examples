#stack, queue 구현

print('\nList로 stack(LIFO) 처리') #선입 후출
sbs=[10, 20, 30]
sbs.append(40)  #마지막 요소로 추가됨 (push)
print(sbs)
sbs.pop()   #sbs의 마지막 요소 제거
print(sbs)
sbs.pop()
print(sbs)

print('List로 queue(FIFO) 처리')   #선입선출
sbs=[10, 20, 30]
sbs.append(40)  #put(offer)
print(sbs)
sbs.pop(0)      #get(poll)
print(sbs)
sbs.pop(0)
print(sbs)