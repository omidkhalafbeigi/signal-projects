import Problem3_A as P_3
from scipy import signal

pulse_triangular = signal.triang(1001)
P_3.convolution(pulse_triangular, pulse_triangular)
