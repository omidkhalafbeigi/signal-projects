import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(-5, 5, 1001)

plt_triangle_1 = plt.subplot(221)
plt_triangle_2 = plt.subplot(222)
plt_convolve = plt.subplot(223)

plt_triangle_1.set_xlim([-6, 6])
plt_triangle_2.set_xlim([-6, 6])
plt_triangle_1.set_title('Triangle 1')
plt_triangle_2.set_title('Triangle 2')
plt_convolve.set_title('Convolution')

triangle_1 = signal.triang(1001)
triangle_2 = signal.triang(1001)

plt_triangle_1.plot(t, triangle_1)
plt_triangle_2.plot(t, triangle_2)
plt_convolve.plot(signal.convolve(triangle_1, triangle_2), color='green')

plt.show()
