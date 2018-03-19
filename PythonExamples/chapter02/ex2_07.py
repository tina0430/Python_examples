#객체의 복사

name1 = ['tom', 'james', 'charles']

name2 = name1 #주소 복사 : 같은 객체 참조
print(name1, id(name1))
print(name2, id(name2))

name1[0] = 'tina'
print('name1[0]를 tina로 바꿈')
print('name1 :', name1)
print('name2 :', name2)

import copy

print('====Deepcopty====')
name3 = copy.deepcopy(name1)
name1[0] = 'eliot'
print('name1 :', name1, id(name1))
print('name2 :', name2, id(name2))
print('name3 :', name3, id(name3))