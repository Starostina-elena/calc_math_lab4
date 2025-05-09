def lineal(x, y):
    SX = sum(x)
    SY = sum(y)
    SXX = sum([i ** 2 for i in x])
    SXY = sum([x[i] * y[i] for i in range(len(x))])

    a = (SXY * len(x) - SX * SY) / (SXX * len(x) - SX ** 2)
    b = (SXX * SY - SXY * SX) / (SXX * len(x) - SX ** 2)

    S = 0
    f = []
    eps = []
    for i in range(len(x)):
        f.append(a * x[i] + b)
        S += (y[i] - (a * x[i] + b)) ** 2
        eps.append(y[i] - (a * x[i] + b))

    return a, b, (S / len(x)) ** 0.5, f, eps
