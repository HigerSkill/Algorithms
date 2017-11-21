import math as m
from scipy.misc import derivative

def newton(f, x0, eps=0.1):
    iteration = 0
    x = x0
    x_last = x
    while True:
        x_last = x
        x = x_last - f(x_last) / derivative(f, x_last)

        iteration = iteration + 1

        if abs(x - x_last) < eps:
            break

    return x


def secant(f, x0, x1, eps=0.1):
    iteration = 0
    x_last = x0
    x = x1
    while True:
        xl1 = x

        x = x - (f(x) * (x - x_last)) / (f(x) - f(x_last))

        x_last = xl1
        iteration = iteration + 1

        if abs(x - x_last) < eps:
            break

    return x


def iterative(f, x0, eps=0.1):
    x = x0.copy()
    while True:
        x_last = x.copy()

        for i in range(len(f)):
            x[i] = f[i](x_last)

        stop = [x - y for x, y in zip(x, x_last)]
        stop = [abs(o) for o in stop]

        if max(stop) <= eps:
            break

    return x
