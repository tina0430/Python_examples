import numpy as np

arr1 = np.array(range(10))
print(arr1)
print()

print(arr1[5])
print()

print(arr1[5:8])
print()

arr1[5:8] = 12
print(arr1[5:8])
print()

arr_slice = arr1[5:8]
arr_slice[1] = 100
print(arr1)
print()

arr2 = np.array(range(9))
arr2 = np.reshape(arr2, [3, 3])

print(arr2[2])
print()

print(arr2[0][2])
print()

print(arr2[0, 2])
print()