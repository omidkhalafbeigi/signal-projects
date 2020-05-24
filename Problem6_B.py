import numpy as np
from scipy import integrate

X = lambda w: (((np.sin(w / 2)) / (w / 2)) ** 2) / (2 * np.pi)
energy = integrate.quad(X, -np.pi, np.round(np.pi, 13))

print(f'Energy of signal in [-PI]: {energy[0]}\nEnergy of signal in [+PI]: {energy[1]}\n'
      f'Energy in period [-PI, +PI]: {energy[1] - energy[0]}')
