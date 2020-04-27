from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

plt_rectangular = plt.subplot(221)
plt_triangular = plt.subplot(222)
plt_step = plt.subplot(223)
plt_slope = plt.subplot(224)

t = np.linspace(-5, 5, 1001)  # between -5 and +5 there's 1001 sentence

pulse_rectangular = signal.square(t, 0.5)  # 0.5 is Duty Cycle (default)
pulse_triangular = signal.triang(1001)
pulse_zeros = list(np.zeros(500))  # Creating array of zeros
pulse_ones = list(np.ones(501))  # Creating array of ones
pulse_step = pulse_zeros + pulse_ones  # Creating step pulse

linear_values = []
for value in range(501):
    linear_values.append(value / 100)
pulse_slope = pulse_zeros + linear_values  # Creating slope pulse

plt_rectangular.set_title('Rectangular')
plt_triangular.set_title('Triangular')
plt_step.set_title('Single Step')
plt_slope.set_title('Single Slope')

plt_triangular.set_xlim([-6, 6])
plt_rectangular.set_xlim([-6, 6])
plt_step.set_xlim([-6, 6])
plt_slope.set_xlim([-6, 6])

plt_step.plot(t, pulse_step, color='purple')  # Plot single step signal
plt_slope.plot(t, pulse_slope, color='blue')  # Plot single slope signal
plt_triangular.plot(t, pulse_triangular, color='green')  # Plot triangular signal
plt_rectangular.plot(t, pulse_rectangular, color='red')  # Plot rectangular signal

plt.show()


