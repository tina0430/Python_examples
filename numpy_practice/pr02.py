import numpy as np

arr = np.arange(1, 17)
arr = np.reshape(arr, [4, 4])
print(arr, end='\n\n')

arr2 = arr[0::2, 1:4]
arr3 = arr[1::2, 0:3]

print(arr2, end='\n\n')
print(arr3, end='\n\n')

arr3 = arr3.T
print(np.matmul(arr2, arr3))