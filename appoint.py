from combinations_and_permutations import permut


def S(P, c, v):
    n = len(c[0])
    s = 0
    for i in range(n):
        for j in range(n):
            s += c[i][j] * v[P[i]-1][P[j]-1]

    return s


def appoint(c, v, a):
    n = len(a[0])
    p = permut(n)

    found = []
    variant = []
    ind = []

    for i in range(len(p)):
        ok = 0
        for j in range(n):
            search = p[i]
            l = search[j]
            if a[j][l - 1] == 0:
                ok += 1
        if ok == n:
            found.append(p[i])

    for i in range(len(found)):
        variant.append(S(found[i], c, v))

    if not variant:
        return []

    varmin = min(variant)
    for i in range(len(variant)):
        if variant[i] == varmin:
            ind.append(i)

    ans = [found[ind[i]] for i in range(len(ind))]
    return ans


if __name__ == '__main__':
    """TESTS 1"""
    a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    c = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
    v = [[0, 5, 6], [5, 0, 3], [6, 3, 0]]
    """TESTS 2"""
    a_1 = [[0, 0], [0, 0]]
    c_1 = [[1, 1], [1, 1]]
    v_1 = [[1, 1], [1, 1]]
    """TEST 3"""
    a_2 = [[0]]
    c_2 = [[1]]
    v_2 = [[1]]
    """TEST 4"""
    a_3 = [[1]]
    c_3 = [[1]]
    v_3 = [[1]]

    answer = appoint(c, v, a)
    answer_1 = appoint(c_1, v_1, a_1)
    answer_2 = appoint(c_2, v_2, a_2)
    answer_3 = appoint(c_3, v_3, a_3)

    print("Ответ на тест 1: ", answer)
    print("Ответ на тест 2: ", answer_1)
    print("Ответ на тест 3: ", answer_2)
    print("Ответ на тест 4: ", answer_3)
