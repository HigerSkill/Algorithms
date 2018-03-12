from combinations_and_permutations import permut


def S(P, c, v):
    n = len(c[0])
    k = P[1]
    s = 0
    for i in range(n):
        for j in range(n):
            s += c[i][j] * v[k[i]-1][k[j]-1]

    return s


def appoint(c, v, a):
    n = len(a[0])
    perm = permut(n)

    found = []
    variant = []

    p = []
    for i in range(len(perm)): # Находим все возможные перестановки
        p.append([[j for j in range(1, n + 1)], perm[i]])

    for i in range(len(perm)): # Ищем допустмые решения
        ok = 0
        for j in range(n):
            search = p[i]
            l = search[1][j]
            if a[j][l - 1] == 0:
                ok += 1
        if ok == n:
            found.append(p[i])

    for i in range(len(found)): # Вычисляем суммы затрат перевозки
        variant.append(S(found[i], c, v))

    ind = variant.index(min(variant)) # Находим оптимальное решение

    return found[ind]


if __name__ == '__main__':
    a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    c = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
    v = [[0, 5, 6], [5, 0, 3], [6, 3, 0]]
    answer = appoint(c, v, a)
    print(answer)
