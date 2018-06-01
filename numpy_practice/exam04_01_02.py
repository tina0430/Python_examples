import numpy as np

arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype)
print()

arr1 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print()

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2.dtype)
print()

float_arr = arr2.astype(np.float64)
print(float_arr.dtype)
print()

arr3 = np.array([1.1, 2.7, 3.6])
print(arr3)
print()

int_arr4 = arr3.astype(np.int32)
print(int_arr4.dtype)
print()

print(int_arr4)
print()

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)