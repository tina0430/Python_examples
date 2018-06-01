import numpy as np

product = np.array([300, 80])
sales = np.array([4, 3])

_result = np.multiply(product, sales)
print('_result :', _result)
result = np.sum(_result)

print('총금액 :', result)
