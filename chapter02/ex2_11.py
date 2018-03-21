mydict=dict(k1=1, k2='abc', k3=3.4)
print(mydict)
print()
coffee = {'espresso':'에스프레소', 'latte':'라떼'}
print(coffee)
print('coffee 사전에 등록된 자료 개수:',len(coffee))
print(coffee['espresso'])   #키로 검색

print(coffee.keys())
print(coffee.values())
print(coffee.items())

print()
print(list(coffee.keys()))
print(list(coffee.values()))
print(list(coffee.items()))

print()
print('latte' in coffee)    #있으면 True 없으면 False
print('cola' in coffee)

print()
coffee['lungo']='룽고'
print(coffee)
del coffee['lungo']
print(coffee)

coffee.clear()
print(coffee)

print(None is False)
print(None is 0)
print(None is '')
print(None is ' ')

print((1.1 + 2.2) == 3.3)
print(1.1+2.2)
print(3.3)

print(1 and 3)
print(0 and 4)
print(4 and 2)
print('e' and 0)
print(1 or 3)
print(3 | 1)
print(0 | 1)

a = 12345789130
b = 12345789129+1
print(id(a), id(b))
print(a is b)

print((10/1) == 10)
print((10/1) is 10)
