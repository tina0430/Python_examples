#일급 함수

def func1(a, b):
    return a+b

func2 = func1   #주소 치환(얕은 복사)

print(func1(3, 4))
print(func2(3, 4))

print()
def func3(func):    #함수를 인자로 받음 (일급객체이기 떄문에 가능)
    def func4():
        print('나는 내부 함수얌')
    func4()
    return func

mbc = func3(func1)
print(mbc(3, 4))