#산의 봎이와 온도 상관관계 분석

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

height=[100,200,300,400,500,600,700,800,900]
temperature=[18.0,17.5,17.0,16.5,15,14.5,13,12,11]
plt.scatter(height, temperature)
plt.xlabel('산의 높이(m)')
plt.ylabel('온도(*C)')
plt.show() 