#재귀함수 연습

print('1~10까지의 정수의 합 구하기')

def tot(n):
    if n == 1:
        print('1 =', end = ' ')
        return 1
    else:
        print('%d +'%n, end = ' ')
        return n + tot(n-1)
    
total = tot(10)

print(total)