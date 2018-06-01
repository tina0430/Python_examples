import numpy as np

su1 = 2
rep_cnt1 = 5
result = np.repeat(su1, rep_cnt1)
print(type(result))
print(result)

array1 = np.array([1, 2])
array2 = np.array([3, 4])
print(array1)
print(array2)

result = np.concatenate((array1, array2))
print(result)

su2 = 3
rep_cnt2 = 4
result = np.concatenate((np.repeat(su1, rep_cnt1), np.repeat(su2, rep_cnt2)))
print(result)

array3 = np.array([1,2,3,4,5,6])
result = np.reshape(array3, [2,3])
print(result)

result = np.reshape(array3, [3,2])
print(result)

array4 = np.array([[3,6,2],[4,1,5]])
print(array4)

result = np.transpose(array4)
print(result)