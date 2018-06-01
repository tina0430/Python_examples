import numpy as np

arr = np.array(range(12))
arr = np.reshape(arr, [3, 4])

print(arr[:, 1], arr[:, 1].shape)
print(arr[:, [1,2]], arr[:, [1,2]].shape)
print(arr[:, 1:2], arr[:, 1:2].shape)