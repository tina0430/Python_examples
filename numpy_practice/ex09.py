import numpy as np

arr1 = np.array(range(10))
print(arr1)
print("10까지 걍 배열 만들기", "#"*35)

print(arr1[5])
print("이제부터 슬라이싱", "#"*38)

print(arr1[5:8])
print("#"*50)

arr1[5:8] = 12
print(arr1[5:8])
print("#"*50)

arr_slice = arr1[5:8]
arr_slice[1] = 100
print(arr1)
print("슬라이싱 끝", "#"*43)

arr2 = np.array(range(9))
arr2 = np.reshape(arr2, [3, 3])

print(arr2[2])
print("#"*50)

print(arr2[0][2])
print("#"*50)

print(arr2[0, 2])
print("3차원 시작", "#"*43)

arr3d = np.array([[[1,2,3,100], [4,5,6,100]], [[7,8,9,100], [10,11,12,100]], 
                  [[13,14,15,100], [16,17,18,100]]])
print(arr3d)
print(arr3d.shape)
print("#"*50)

print(arr3d[0])
print("#"*50)

print(arr3d[:2, :1, :3])
print("100으로 바꾸기", "#"*39)

old_values = arr3d[0].copy()

arr3d[0] = 100
print(arr3d)
print("#"*50)

arr3d[0] = old_values
print(arr3d)
print("#"*50)