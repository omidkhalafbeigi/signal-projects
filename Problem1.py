import matplotlib.pyplot as plt
import math
import numpy as np

T = 26  # Period
plt1 = plt.subplot(223)
plt2 = plt.subplot(222)
t = np.arange(0, T, 0.001)  # Axis (x)
n = np.arange(0, T, 1)
plt1.plot(t, np.cos(t * 0.25), color='red', label='W = 0.25')
plt1.plot(t, np.cos(t * (math.pi / 2)), color='purple', label='W = PI/2')
plt1.plot(t, np.cos(t * math.pi), color='green', label='W = PI')
plt2.stem(n, np.cos(n * 0.25), label='W = 0.25', use_line_collection=True, markerfmt='s')
plt2.stem(n, np.cos(n * (math.pi / 2)), use_line_collection=True, label='W = PI/2', markerfmt='+')
plt2.stem(n, np.cos(n * math.pi), label='W = PI', use_line_collection=True, markerfmt='x')
plt2.set_title('Discrete Time')
plt1.set_title('Continues Time')
plt1.legend()
plt2.legend()
plt.show()