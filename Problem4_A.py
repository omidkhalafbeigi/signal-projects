import numpy as np
import functools


def recursion_eq(N, M):
    # Formula: Sigma[k = 0 -> N](ak * y(n - k)) = Sigma[m = 0 -> M](bm * x(n - m))

    print('Original Formula is: Sigma[k = 0 -> N](ak * y(n - k)) = Sigma[m = 0 -> M](bm * x(n - m))')
    N = int(N)
    M = int(M)
    y_Factors = list()
    x_Factors = list()
    x_Inputs_Sum = 0
    y_Primal_Values = list()
    y_Applied_Factors = list()
    y_Last_Result = 0
    y_Sum = 0
    n = 0  # "n" starts than 0 (time)
    print('New formula is: Sigma[k = 0 -> {}](ak * y(n - k)) = Sigma[m = 0 -> {}](bm * x(n - m))'.format(N, M))

    print('For start, I should calculate y(0), so enter inputs on below:')
    # y_Factors.append(int(input('Enter a0: ')))

    for k in range(0, M + 1):  # Get (x) factors - (bm)
        x_Factors.append(float(input('Enter b{}: '.format(k))))

    x_Inputs = np.zeros(M + 1, dtype=float)
    y_Primal_Values = np.zeros(N + 1, dtype=float)
    y_Applied_Factors = np.zeros(N + 1, dtype=float)

    for k in range(0, N + 1):  # Get (y) factors - (am)
        y_Factors.append(float(input('Enter a{}: '.format(k))))

    y_Primal_Values[0] = 0
    for k in range(1, N + 1):  # Get (y) primal values
        y_Primal_Values[k] = (float(input('Enter y({}): '.format(n - k))))

    y_Primal_Values = list(reversed(y_Primal_Values))
    y_Factors = list(reversed(y_Factors))

    while True:
        for k in range(0, M + 1):  # calculating equation right-side
            x_Inputs[k] = float(input('Enter x({}): '.format(n - k))) * x_Factors[k]  # bm * x[n - m] (Applying (x)
            # factors to x[n - m])
            x_Inputs_Sum += x_Inputs[k]  # Sum all of (x) inputs
        #     print(f'x Inputs Sum: {x_Inputs_Sum}')

        # for k in range(0, N):  # Applying (y) factors to equation
        #     y_Primal_Values[k] = y_Primal_Values[k] * y_Factors[k]
        # print(f'y Primal Values: {y_Primal_Values}')
        # print(f'Factors{y_Factors}')
        for k in range(0, N):  # Applying (y) factors to equation
            y_Applied_Factors[k] = y_Primal_Values[k] * y_Factors[k]

        # print(f'Applied: {y_Applied_Factors}')

        y_Last_Result = functools.reduce(lambda a, b: a + b, y_Applied_Factors)  # Sum all of (y) values
        y_Sum = y_Last_Result
        y_Last_Result = (x_Inputs_Sum + (-1 * y_Last_Result)) / y_Factors[len(y_Factors) - 1]  # Shift sum of (y)
        # to right-side of equation and divide to (y[n]) factor
        y_Primal_Values[len(y_Primal_Values) - 1] = y_Last_Result
        for k in range(0, N):  # Shift (array) 1 element to left
            if k < N:
                y_Primal_Values[k] = y_Primal_Values[k + 1]
        y_Primal_Values[len(y_Primal_Values) - 1] = 0
        # print(f'Shifted: {y_Primal_Values}')
        # print(f'x Sum: {x_Inputs_Sum}')
        # print(f'y Sum:  {y_Sum}')
        print('y({}): {}'.format(n, y_Last_Result))
        # for k in range(0, N):  # Recursion y_Primal_Values to normal values (by division)
        #     y_Primal_Values[k] = y_Primal_Values[k] / y_Factors[k]
        n += 1
        x_Inputs_Sum = 0
        print('------------')

# recursion_eq(1, 3)  # For example
