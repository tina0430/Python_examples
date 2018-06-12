#간단한 1차 방정식

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return 2*x+1

#1.0 부터 4.5까지 05씩 증가시키기
x = np.arange(1.0, 4.1, 0.5)
y = step_function(x)

print("x :", x)
print("y :", y)

#파란색 그래프를 위한 실험용 데이터
y_answer = [3.1, 4.1, 4.9, 6.1, 6.9, 8.2, 9.1]
plt.plot(x, y, marker='o', color='r')