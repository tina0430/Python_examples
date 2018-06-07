#데코레이터(decorator) 연습

def outer(func):
    def inner(no1, no2):
        print("결과는 : {0}".format(func(no1, no2)))
    return inner

@outer
def func(n1, n2):
    return (n1+n2)

func(3, 4)
func(1, 5)
print(func)
