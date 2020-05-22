import cmath
from matplotlib import pyplot as plt
import numpy as np

phases = list()
magnitudes = list()
phases_k = list()

for k in range(-30, 30):
    if k != 0:
        numerator = (6 *
                     ((cmath.cos((2 / 3) * cmath.pi * k)) - (cmath.cos((1 / 3) * cmath.pi * k)) + (
                         cmath.cos((4 / 3) * cmath.pi * k))
                      - (cmath.cos((5 / 3) * cmath.pi * k))))  # Real Number
        denominator = complex(0, (cmath.pi * k))  # Complex Number

        phrase = numerator / denominator  # (Real/Complex) Number
        phases.append(np.degrees(cmath.phase(phrase)))  # Calculating phase of complex number
        magnitudes.append(np.abs(phrase))  # Calculating magnitude of complex number
        phases_k.append(k)

plt_phase = plt.subplot(221)
plt_magnitude = plt.subplot(222)

plt_phase.set_xlabel('k')
plt_magnitude.set_xlabel('k')
plt_phase.set_ylabel('phase of a(k)')
plt_magnitude.set_ylabel('magnitude of a(k)')
plt_phase.set_title('Phases (30 Samples in Degree)')
plt_magnitude.set_title('Magnitude (30 Samples in Degree)')
plt_phase.stem(phases_k, phases, use_line_collection=True)
plt_magnitude.stem(phases_k, magnitudes, use_line_collection=True)

plt.show()
