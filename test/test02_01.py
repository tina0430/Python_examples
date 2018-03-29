#다음과 같은 그래프를 그리세요.

import matplotlib.pyplot as plt
plt.subplots()
plt.subplot(3,1,3)
plt.plot([1,2,3,4],[1,2,3,4]) #데이터 삽입
plt.xlim(2,3)
plt.title("mytitle")
plt.show()