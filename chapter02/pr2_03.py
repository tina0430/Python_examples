#-1, 3, -5, 7, -9, 11 ~ 99까지의 합 출력

sign = num = 1
mySum = 0

while num < 100 :
    sign = -sign
    mySum += sign*num
    num += 2
print(mySum) 