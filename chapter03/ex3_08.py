#클로저(clouser) 연습

#클로저 미사용
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
    
print('함수 내의   count 값은')
out()
out()

print()
#클로저 사용
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

print('함수 내의 count 값은')
add1= outer()
print(add1())
print(add1())
print(add1())

print()
add2 = outer()
print(add2())
print(add2())

print('주소 확인')
print(id(add1), id(add2))