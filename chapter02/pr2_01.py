#1~100사이의 정수 중 3의 배수의 합을 출력

sum = 0
num = 3
while num <= 100 :
    sum+=num
    num+=3
print("1~100사이의 정수중 3의 배수의 합 :", sum)