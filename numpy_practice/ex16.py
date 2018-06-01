import numpy as np

arrX = np.array([[1,2], [3,4]])
arrY = np.array([[5,6], [7,8]])

v = np.array([9,10])
w = np.array([11,12])

#벡터의 내적
print(v.dot(w))
print()

print(np.dot(v, w))
print()

print(v.dot(np.array([1,2])))
print(v.dot(np.array([3,4])))
print(arrX.dot(v))
print()

print(v.dot(arrX))
print()

print(arrX.dot(arrY))
print() 

print(np.dot(arrX, arrY))
print()

print(np.dot(arrY, arrX))
print()