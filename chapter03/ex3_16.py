#재귀함수 연습

print('1~5까지의 정수의 곱 구하기')

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)
    
factorial = facto(5)

print('5! =', factorial)