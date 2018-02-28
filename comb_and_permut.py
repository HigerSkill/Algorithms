def comb(n, k):
    A = []
    B = [i+1 for i in range(k)]

    if n == k:
        return [B]
    elif n < k:
        return False

    p = k
    while p >= 0:
        A.append(B.copy())
        if B[k-1] == n:
            p = p - 1
        else:
            p = k - 1
        if p >= 0:
            for i in range(k-1, p-1, -1):
                B[i] = B[p] + i - p + 1

    return A


def permut(n):
    A = []
    B = [i+1 for i in range(n)]

    if n == 0:
        return [[0]]
    elif n < 0:
        return False

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

"""
Test
comb(3, 3)
>>> [[1, 2, 3]]
comb(1, 1)
>>> [[1]]
comb(5, 3)
>>> [[1, 2, 3], [1, 2, 4], [1, 2, 5], 
     [1, 3, 4], [1, 3, 5], [1, 4, 5], 
     [2, 3, 4], [2, 3, 5], [2, 4, 5], 
     [3, 4, 5]]
    
permut(0)
>>> [[0]]
permut(1)
>>> [[1]]
permut(3)
>>> [[1, 2, 3], [1, 3, 2], [2, 1, 3], 
     [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
