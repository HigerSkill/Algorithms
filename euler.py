""" начальное время t0 (мин);
    начальная температура кофе T0 ◦C;
    комнатная температура Ts ◦C;
    коэффициент остывания r (1/мин);
    длительность t (мин);
    количество шагов по времени M.
"""
from math import *

import pprint

def analytic_f(t, r=-0.034, Ts=25.1, T0=75.6):
    return round(Ts - (Ts - T0) * exp(r * t), 4)


def f(t, T, Ts=25.1, r=-0.034):
    return r * (T - Ts)


def euler(f, t0, t, m, T0=75.6):
    h = (t - t0) / float(m)
    x = t0
    y = T0

    for i in range(m):
        y += h * f(x, y)
        x += h

    return round(y, 4)
