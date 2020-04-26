import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


def convolution(signal1, signal2):
    sum_period = 0
    primary_signal1 = signal1
    primary_signal2 = signal2
    plt_signal1 = plt.subplot(221)
    plt_signal2 = plt.subplot(222)
    plt_convolve = plt.subplot(223)
    plt_convolve_orig = plt.subplot(224)
    plt_signal1.set_title('Signal 1')
    plt_signal2.set_title('Signal 2')
    plt_convolve.set_title('Convolution (Handmade)')
    plt_convolve_orig.set_title('Convolution (Original)')
    plt_signal1.stem(primary_signal1, use_line_collection=True, basefmt='black')
    plt_signal2.stem(primary_signal2, use_line_collection=True, basefmt='black')
    plt_convolve_orig.stem(signal.convolve(primary_signal1, primary_signal2), use_line_collection=True, basefmt='black')
    result = []
    biggest_signal = 0
    smallest_signal = 0
    if len(signal1) < len(signal2):
        for i in range(0, len(signal2) - len(signal1)):
            signal1.append(0)
        biggest_signal = signal2
        smallest_signal = signal1
    elif len(signal2) < len(signal1):
        for i in range(0, len(signal1) - len(signal2)):
            signal2.append(0)
        biggest_signal = signal1
        smallest_signal = signal2
    else:
        biggest_signal = signal1
        smallest_signal = signal2
    for i in range(0, len(signal1) - 1):
        for j in range(0, i + 1):
            sum_period += (signal1[abs(i - j)] * signal2[j])
        result.append(sum_period)
        sum_period = 0
        # -------------

    sum_period = 0

    smallest_signal = list(reversed(smallest_signal))

    for i in range(0, len(smallest_signal)):
        counter_small_length = len(smallest_signal) - 1
        counter_big_length = len(biggest_signal) - 1
        while counter_small_length >= 0:
            sum_period += (smallest_signal[counter_small_length] * biggest_signal[counter_big_length])
            counter_small_length -= 1
            counter_big_length -= 1
        del (smallest_signal[len(smallest_signal) - 1])
        result.append(sum_period)
        print(sum_period)
        sum_period = 0

    plt_convolve.stem(result, use_line_collection=True, linefmt='black', basefmt='black')
    plt.show()


#  Example: Signals must be the list type


# signal_1 = [0, 0, 1, 0, 0, 1, 0, -1]
# signal_2 = [1, 1, -1, 0, 0, 1, 0, 1]

# convolution(signal_1, signal_2)
