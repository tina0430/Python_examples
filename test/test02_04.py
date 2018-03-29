# numpy의 random 계열 함수를 사용하여 1부터 5사이의 
# 정수 3개를 복원 추출하고, 이것의 총합을 구하는 프로그램을 작성하세요.
import numpy as np

num_list = np.random.randint(1, 5 , size=3)
total = 0

for i in num_list:
    print(i, end=' ')
    total += i

print()
print(total)