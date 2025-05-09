from utils.lineal import lineal
from math import log, exp

def logarithmic(x, y):
    a, b, *args = lineal([log(i) for i in x], y)

    S = 0
    f = []
    eps = []
    for i in range(len(x)):
        fi = a * log(x[i]) + b
        f.append(fi)
        S += (fi - y[i]) ** 2
        eps.append(fi - y[i])

    return a, b, S, f, eps