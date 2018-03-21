#1~1000사이의 소수와 그 개수 출력
 
count = 0

for num in range(1, 1001) :
    if (num == 1) : continue
    for subN in range(2, int(num**0.5)+1) :
        if (num%subN == 0) : break
    else :
        count += 1
        print(format(num, '3d')) 
    
print('1~1000 총 소수의 개수 :',count)