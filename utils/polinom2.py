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
    for i in range(len(x)):
        fi = a + b * x[i] + c * x[i] ** 2
        f.append(fi)
        S += (fi - y[i]) ** 2
        eps.append(fi - y[i])

    return a, b, c, (S / len(x)) ** 0.5, f, eps
