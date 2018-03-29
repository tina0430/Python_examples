#난수 그래프

import numpy as np
import matplotlib.pyplot as plt

random_x = np.random.random_integers(0, 100, 50)
print(random_x)
random_y = np.random.random_integers(0, 100, 50)
print(random_y)
plt.scatter(random_x, random_y)
plt.show()
