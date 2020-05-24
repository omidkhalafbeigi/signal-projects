from matplotlib import pyplot as plt
import numpy as np

#  Fourier-Transform of Pulse, is (sin(pi * x))/(pi * x)

frequencies = np.linspace(-100, 100, 5000)
Xw = list()
ft_value = 0

for w in frequencies:
    if w != 0:
        ft_value = ((np.sin(w / 2)) / (w / 2))
        Xw.append(ft_value)
    else:
        Xw.append(1)

plt.title('Fourier-Transform of Pulse function')
plt.xlabel('Frequency (w)')
plt.ylabel('Value of signal in different frequencies (X(w))')
plt.plot(list(frequencies), Xw)
plt.show()
