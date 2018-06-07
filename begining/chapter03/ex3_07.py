#dict 자료형 자료 출력

def func(w, h, **other):
    print('몸무게 {} 키 {}'.format(w, h), end= ' ')
    print(other)
    
func(65,175,name='jihee', age=24)
func(w=75,h=185,name='jihee')

print('\n파라미터 전달 - 종합')
def funcTotal(a, b, *t, **d):
    print('a, b: ', a, b, end = ' | ')
    print('t :', t, end = ' | ')
    print('d :', d)
    
funcTotal(1, 2)
funcTotal(1, 2, 3, 4, 5)
funcTotal(1, 2, 3, 4, 5, m =6, n =7)

print('\n튜플, 사전 인수로 함수 호출')
def func2(a, b, c):
    print(a, b, c)

func2(1, 2, 3)
tup = (10, 20)
dic = {'c':30}
lis = [11, 22]
se = {12, 23}
func2(*lis, **dic)
func2(*se, **dic)

dic = {'c':'수'}
func2(*tup, **dic)
