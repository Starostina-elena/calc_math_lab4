from utils.lineal import lineal
from math import log, exp

def exponential(x, y):
    A, b, *args = lineal(x, [log(i) for i in y])
    a = exp(A)

    S = 0
    f = []
    eps = []
    for i in range(len(x)):
        fi = a * exp(b * x[i])
        f.append(fi)
        S += (fi - y[i]) ** 2
        eps.append(fi - y[i])

    return a, b, S, f, eps