import math
import numpy as np
import pylab
from matplotlib import mlab


def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)


def g(x, h):
    return sum(w * (x ** n) for n, w in enumerate(h))


def listA(dots):
    return np.array([[(w ** n) for n in np.arange(len(dots))] for w in dots])


def listB(dots):
    return np.array([f(x) for x in dots])


containerDot = [
    (1, 15), (1, 8, 15), (1, 4, 10, 15),
]

def test():
    min, max, dx = 0, 16, 0.01

    for d in containerDot:
        a = listA(d)
        b = listB(d)
        h = np.linalg.solve(a, b)
        h = list(h)
        xlist = mlab.frange(min, max, dx)
        ylist = [f(x) for x in xlist]
        yrlist = [g(x, h) for x in xlist]
        pylab.plot(xlist, yrlist)
        pylab.plot(xlist, ylist)
        pylab.show()

