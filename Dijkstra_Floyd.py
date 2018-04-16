from math import *

"""Граф представляется в виде матрицы"""


def minv(d, x):
    minimum = inf
    for v in range(len(d)):
        if x[v] == 0:
            if d[v] < minimum:
                minimum = d[v]
    return minimum


def dijkstra(w, s, t):
    n = len(w)

    d = [inf for _ in range(n)]  # Верхняя оценка длины пути
    h = [-1 for _ in range(n)]  # Вершина, предшествующая данной вершине
    x = [0 for _ in range(n)]  # Вершины имеют временные метки

    d[s] = 0  # Вес вершины старта равен 0
    h[s] = -1  # Вершине s ничего не предшествует
    x[s] = 1  # Вершина s имеет постоянные метки

    p = s  # Вершина, которая получила постоянные метки последней

    while p != t:
        v_new = 0
        for v in range(n):
            if w[p][v] != inf:  # Вершины исходящих из p дуг
                if d[v] > d[p] + w[p][v]:  # найден более короткий путь
                    d[v] = d[p] + w[p][v]
                    h[v] = p

        for v in range(n):  # Превращение временных меток в постоянные
            if x[v] == 0 and d[v] == minv(d, x):
                x[v] = 1
                v_new = v
                break

        # print(d, h, x)
        p = v_new

    v = t
    short_way = [v]  # Нахождение последовательности вершин кратчайшего пути
    while v != s:
        v = h[v]
        short_way.append(v)

    return d[t], short_way


def floyd(w, s, t):
    n = len(w)

    d = w.copy()
    h = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):  # формирование начального состояния h
        for j in range(n):
            if w[i][j] == inf or i == j:
                h[i][j] = -1
            else:
                h[i][j] = i

    k = 0  # номер итерации
    while True:
        for i in range(n):
            for j in range(n):
                if i != k and j != k:
                    if (d[i][k] + d[k][j]) < d[i][j]:
                        h[i][j] = h[k][j]
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        k = k + 1
        stop = 0
        cont = 0
        for i in range(n):
            if d[i][i] < 0:
                return None
            if d[i][i] >= 0 and k == n:
                stop += 1
            if d[i][i] >= 0 and k < n:
                cont += 1

        if stop == n:
            q = t  # Нахождение последовательности вершин кратчайшего пути
            short_way = [t]
            while q != s:
                q = h[s][q]
                short_way.append(q)
            return d, h, short_way
        if cont == n:
            continue


if __name__ == '__main__':
    W1 = [[0, 2, 1, 6, inf, 9, inf, inf],
          [inf, 0, inf, 3, 5, inf, inf, inf],
          [inf, inf, 0, inf, 1, 7, inf, inf],
          [inf, inf, inf, 0, 2, 2, inf, inf],
          [inf, inf, inf, inf, 0, inf, 3, inf],
          [inf, inf, inf, inf, inf, 0, 2, 2],
          [inf, inf, inf, inf, inf, inf, 0, 1],
          [inf, inf, inf, inf, inf, inf, inf, 0]]

    W2 = [[0, -2, 3, -3],
          [inf, 0, 2, inf],
          [inf, inf, 0, -3],
          [4, 5, 5, 0]]

    W3 = [[0, 10, 17, inf, 3],
          [inf, 0, 4, inf, inf],
          [inf, inf, 0, 9, inf],
          [5, 15, inf, 0, inf],
          [inf, inf, inf, 4, 0]]

    W3_ones = [[0, 1, 1, inf, 1],
               [inf, 0, 1, inf, inf],
               [inf, inf, 0, 1, inf],
               [1, 1, inf, 0, inf],
               [inf, inf, inf, 1, 0]]

    W4 = [[0, 5, 7, 10, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf],
          [inf, 0, 16, inf, inf, 8, 9, 14, inf, inf, inf, inf, inf, inf],
          [inf, inf, 0, inf, inf, 11, inf, inf, inf, inf, inf, inf, inf, inf],
          [inf, inf, inf, 0, 11, inf, inf, inf, inf, 26, 30, inf, inf, inf],
          [inf, inf, inf, inf, 0, inf, inf, inf, inf, 3, inf, inf, inf, inf],
          [inf, inf, inf, inf, inf, 0, inf, inf, inf, 13, inf, 17, inf, inf],
          [inf, inf, inf, inf, inf, inf, 0, inf, 30, inf, inf, inf, inf, inf],
          [inf, inf, inf, inf, inf, inf, inf, 0, 18, inf, inf, 21, inf, inf],
          [inf, inf, inf, inf, inf, inf, inf, inf, 0, inf, inf, inf, 8, inf],
          [inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 15, inf, inf, inf],
          [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 19, 12, inf],
          [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 14, inf],
          [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 7],
          [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0]]

    W4o = [[0, 1, 1, 1, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf],
           [inf, 0, 1, inf, inf, 1, 1, 1, inf, inf, inf, inf, inf, inf],
           [inf, inf, 0, inf, inf, 1, inf, inf, inf, inf, inf, inf, inf, inf],
           [inf, inf, inf, 0, 1, inf, inf, inf, inf, 1, 1, inf, inf, inf],
           [inf, inf, inf, inf, 0, inf, inf, inf, inf, 1, inf, inf, inf, inf],
           [inf, inf, inf, inf, inf, 0, inf, inf, inf, 1, inf, 1, inf, inf],
           [inf, inf, inf, inf, inf, inf, 0, inf, 1, inf, inf, inf, inf, inf],
           [inf, inf, inf, inf, inf, inf, inf, 0, 1, inf, inf, 1, inf, inf],
           [inf, inf, inf, inf, inf, inf, inf, inf, 0, inf, inf, inf, 1, inf],
           [inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 1, inf, inf, inf],
           [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 1, 1, inf],
           [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 1, inf],
           [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 1],
           [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0]]

    n = len(W3)
    d, h, way = floyd(W4, 0, 0)
    
    K = 20
    for i in range(n):
        m = 0
        for j in range(n):
            if d[j][i] < K:
                m += 1
        if m == n:
            print(i)
