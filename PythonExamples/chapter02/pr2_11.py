#1~100사이의 3의 배수이면서 5의 배수인 수의 합 출력
sum = 0

for i in range(1,101) :
    if not (i%3 or i%5) :
        sum += i
        print(i, end=' ')
print('\n결과 : ', sum)