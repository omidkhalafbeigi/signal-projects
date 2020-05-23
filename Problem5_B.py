import matplotlib.pyplot as plt
import cmath
import numpy as np

k = 1
t_period = np.linspace(-6, 6, 1000)
phrase = list()
x = np.linspace(0, 0, 1000, dtype=complex)
plot_k_5 = plt.subplot(221)
plot_k_10 = plt.subplot(222)
plot_k_20 = plt.subplot(223)


for k in range(1, 6):
    numerator = (6 *
                 ((cmath.cos((2 / 3) * cmath.pi * k)) - (cmath.cos((1 / 3) * cmath.pi * k)) + (
                     cmath.cos((4 / 3) * cmath.pi * k))
                  - (cmath.cos((5 / 3) * cmath.pi * k))))  # Real Number

    denominator = complex(0, (cmath.pi * k))  # Complex Number
    ak = numerator / denominator  # (Real/Complex) Number

    for t in t_period:
        phrase.append((ak * cmath.exp(complex(0, (k / 3) * cmath.pi * t))))  # Calculating fourier series

    x += np.array(phrase, dtype=complex)
    phrase.clear()

x_real = list(map(lambda im: np.abs(im), x))

plot_k_5.set_title('k = 5')
plot_k_5.set_xlabel('t')
plot_k_5.set_ylabel('x(t)')
plot_k_5.plot(t_period, x_real)

for k in range(1, 11):
    numerator = (6 *
                 ((cmath.cos((2 / 3) * cmath.pi * k)) - (cmath.cos((1 / 3) * cmath.pi * k)) + (
                     cmath.cos((4 / 3) * cmath.pi * k))
                  - (cmath.cos((5 / 3) * cmath.pi * k))))  # Real Number

    denominator = complex(0, (cmath.pi * k))  # Complex Number
    ak = numerator / denominator  # (Real/Complex) Number

    for t in t_period:
        phrase.append((ak * cmath.exp(complex(0, (k / 3) * cmath.pi * t))))  # Calculating fourier series

    x += np.array(phrase, dtype=complex)
    phrase.clear()

x_real = list(map(lambda im: np.abs(im), x))

plot_k_10.set_title('k = 10')
plot_k_10.set_xlabel('t')
plot_k_10.set_ylabel('x(t)')
plot_k_10.plot(t_period, x_real, 'red')

for k in range(1, 21):
    numerator = (6 *
                 ((cmath.cos((2 / 3) * cmath.pi * k)) - (cmath.cos((1 / 3) * cmath.pi * k)) + (
                     cmath.cos((4 / 3) * cmath.pi * k))
                  - (cmath.cos((5 / 3) * cmath.pi * k))))  # Real Number

    denominator = complex(0, (cmath.pi * k))  # Complex Number
    ak = numerator / denominator  # (Real/Complex) Number

    for t in t_period:
        phrase.append((ak * cmath.exp(complex(0, (k / 3) * cmath.pi * t))))  # Calculating fourier series

    x += np.array(phrase, dtype=complex)
    phrase.clear()

x_real = list(map(lambda im: np.abs(im), x))

plot_k_20.set_title('k = 20')
plot_k_20.set_xlabel('t')
plot_k_20.set_ylabel('x(t)')
plot_k_20.plot(t_period, x_real, 'green')

plt.show()
