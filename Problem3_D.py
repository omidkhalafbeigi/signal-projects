import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import Problem3_C as P_3

signal_1 = [0, 1, 0, -1, 0, -1, 1, 1, 0, 0]
signal_2 = [0, 0, -1, 1, 0, 1, 0]

P_3.convolution(signal_1, signal_2)