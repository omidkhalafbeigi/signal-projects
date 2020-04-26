from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


# pay attention: signal1 and signal2 must be the array of values.

def convolution(signal1, signal2):
    plt_signal1 = plt.subplot(221)
    plt_signal2 = plt.subplot(222)
    plt_convolve = plt.subplot(223)
    plt_signal1.set_title('Signal 1')
    plt_signal2.set_title('Signal 2')
    plt_convolve.set_title('Convolution')
    convolve = signal.convolve(signal1, signal2)
    plt_signal1.plot(signal1)
    plt_signal2.plot(signal2)
    plt_convolve.plot(convolve, color='green')
    plt.show()


sin = np.sin(list(map(lambda t: (t * np.pi) / 180, np.arange(360))))
cos = np.cos(list(map(lambda t: (t * np.pi) / 180, np.arange(360))))

convolution(sin, cos)
