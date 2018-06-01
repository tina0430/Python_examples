import numpy as np

a = np.array([3, 4])
b = np.array([2, 5])
c = np.array([5, -1, 4, 2])
c = np.reshape(c, [2, 2])
d = np.array([-1, 2])

print(a)
print(b)
print(c)
print(d)

print(np.matmul(a, b))
print(np.matmul(c, d))
