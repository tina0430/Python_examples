#그래프 여러개 그리기 연습2

import matplotlib
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1,2,1)
plt.plot([1,2,3,4], [1,2,3,4])
plt.subplot(1,2,2)
plt.plot([5,6,7,8], [5,6,7,8])
plt.show()

