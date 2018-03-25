def make2(fn):
    return lambda : "안녕" + fn()

def make1(fn):
    return lambda : "반가워" + fn()

def hello():
    return "홍길동"

hi = make2(make1(hello))
print(hi())

@make2
@make1
def hello2():
    return "신기해"

hi2 = hello2()
print(hi2)
hi3 = hello2
print(hi3)