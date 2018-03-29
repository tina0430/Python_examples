#카페 31번 글 - numpy - random 함수 연습

import numpy as np

print('임의의 값으로 채워진 2*2 배열 생성')
result = np.random.random((2,2))
print(result)

print('\n표준 편차가 1이고 평균값이 0인 정규 분포에서 표본을 추출한다')
result = np.random.randn(2,3)
print(result)

print('\n임의의 값으로 채워진 4*4 배열 생성')
result = np.random.randn(4,4)
print(result)

print('\n임의의 값으로 채워진 3행 3열 배열 생성')
result = np.random.uniform(size=(3,3))
print(result)

print('\n임의의 값으로 채워진 1행 2열 배열 생성')
x_shape = [1,2]
result = np.random.uniform(size=x_shape)
print(result)

print('\n임의의 값으로 채워진 3면 3행 2열 배열 생성')
x_shape = [3,2,2]
result = np.random.uniform(size=x_shape)
print(result)

print('\n0이상 5미만의 임의의 정수 1개를 추출')
result = np.random.randint(5)
print(result)

print('\n0이상 3미만의 임의의 정수 4개를 추출')
result = np.random.randint(3, size=4)
print(result)

print('\n0이상 5미만의 정수 10개를 추출')
result = np.random.randint(0, 5, size=10)
print(result)

print()
total = 0
for idx in range(0, 3):
    print(idx, end = ' ')
    total +=np.random.randint(3)
    
print('\n합 :', total)

# print(np.random.seed(12345))

print()
print('permutation()은 0~4까지의 숫자를 랜덤하게 섞어준다.')
length = 5
result = np.random.permutation(length)
print(result)

print()
print('np.random.narmal(평균, 표준편차, 요소개수)')
result = np.random.normal(0, 0.01, 10)