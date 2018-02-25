def comb(n, k):
    A = []
    B = [i+1 for i in range(k)]

    p = k
    while p >= 0:
        A.append(B.copy())
        p = p-1 if B[k-1] == n else k-1
        if p >= 0:
            for i in range(k-1, p-1, -1):
                B[i] = B[p] + i - p + 1

    return A


def permut(n):
    A = []
    B = [i+1 for i in range(n)]

    while True:
        A.append(B.copy())
        i = n-2

        while i != -1 and B[i] >= B[i+1]:
            i = i-1

        if i == -1:
            break

        k = n-1
        while B[i] >= B[k]:
            k = k-1

        B[i], B[k] = B[k], B[i]
        B[i+1:n] = reversed(B[i+1:n])

    return A
