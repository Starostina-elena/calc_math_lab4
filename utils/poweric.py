from math import log, exp
from utils.lineal import lineal

def poweric(x, y):
    b, A, *args = lineal([log(i) for i in x], [log(i) for i in y])
    a = exp(A)

    S = 0
    f = []
    eps = []
    f_middle = 0
    for i in range(len(x)):
        fi = a * (x[i] ** b)
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

    return a, b, R2, S, f, eps