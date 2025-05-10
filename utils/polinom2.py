import numpy as np


def polinom2(x, y):
    SX = sum(x)
    SXX = sum([i ** 2 for i in x])
    SXXX = sum([i ** 3 for i in x])
    SXXXX = sum([i ** 4 for i in x])
    SY = sum(y)
    SXY = sum([x[i] * y[i] for i in range(len(x))])
    SXXY = sum([x[i] ** 2 * y[i] for i in range(len(x))])
    matrix = [
        [len(x), SX, SXX],
        [SX, SXX, SXXX],
        [SXX, SXXX, SXXXX],
    ]
    right_matrix = [SY, SXY, SXXY]
    a, b, c = np.linalg.solve(matrix, right_matrix)

    S = 0
    f = []
    eps = []
    f_middle = 0
    for i in range(len(x)):
        fi = a + b * x[i] + c * x[i] ** 2
        f_middle += fi
        f.append(fi)
        S += (fi - y[i]) ** 2
        eps.append(fi - y[i])

    f_middle /= len(x)
    sum1 = 0
    sum2 = 0
    for i in range(len(x)):
        sum1 += (y[i] - f[i]) ** 2
        sum2 += (y[i] - f_middle) ** 2
    R2 = 1 - sum1 / sum2

    return a, b, c, R2, (S / len(x)) ** 0.5, f, eps
