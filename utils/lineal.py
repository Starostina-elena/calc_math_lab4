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
    x_middle = sum(x) / len(x)
    y_middle = sum(y) / len(y)
    sum1, sum2, sum3 = 0, 0, 0
    f_middle = 0
    for i in range(len(x)):
        fi = a * x[i] + b
        f_middle += fi
        f.append(fi)
        S += (y[i] - fi) ** 2
        eps.append(y[i] - fi)
        sum1 += (x[i] - x_middle) * (fi - y_middle)
        sum2 += (x[i] - x_middle) ** 2
        sum3 += (fi - y_middle) ** 2

    r = sum1 / ((sum2 * sum3) ** 0.5)

    f_middle /= len(x)
    sum1 = 0
    sum2 = 0
    for i in range(len(x)):
        sum1 += (y[i] - f[i]) ** 2
        sum2 += (y[i] - f_middle) ** 2
    R2 = 1 - sum1 / sum2

    return a, b, r, R2, (S / len(x)) ** 0.5, f, eps
