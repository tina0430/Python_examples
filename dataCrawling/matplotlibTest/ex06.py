#그래프에 문자 삽입

from matplotlib import pyplot as plt

plt.plot([1,2,3,4], [1,2,3,4])
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('matplotlib 활용')
plt.text(3.5, 3.0, 'Avg:2.5')   #문자를 삽입할 좌표와 삽입할 문자
plt.grid(True)
plt.show()