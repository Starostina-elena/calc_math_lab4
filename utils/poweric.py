from math import log, exp
from utils.lineal import lineal

def poweric(x, y):
    A, b, *args = lineal([log(i) for i in x], [log(i) for i in y])
    a = exp(A)

    S = 0
    f = []
    eps = []
    for i in range(len(x)):
        fi = a * (x[i] ** b)
        f.append(fi)
        S += (fi - y[i]) ** 2
        eps.append(fi - y[i])

    return a, b, S, f, eps