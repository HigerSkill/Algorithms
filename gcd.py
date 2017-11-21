def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcdBinary(a, b):
    deg = 0

    if a == 0 or b == 0:
        return a | b

    while (a | b) & 1 == 0:
        deg += 1
        a >>= 1
        b >>= 1

    while a and b:
        if b & 1:
            while (a & 1) == 0:
                a >>= 1
        else:
            while (b & 1) == 0:
                b >>= 1
        if a >= b:
            a = (a - b) >> 1
        else:
            b = (b - a) >> 1

    return (a | b) << deg
