import math as m
import numpy as np


def create_matrix_txt(form):
    """
    :param form: 
    extended or normal 
    :return:  
    extended matrix or a and column vector b
    """
    file = open('matrix')
    n = int(file.read(1))  # Dimension
    matrix_txt = np.loadtxt('matrix', skiprows=1)  # Extended matrix

    b = np.zeros(n, )  # Column vector b
    for i in range(0, n):
        b[i] = matrix_txt[i, n]

    a = matrix_txt  # matrix a
    a = np.delete(a, n, 1)

    if form == 'extended':
        return matrix_txt
    elif form == 'normal':
        return a, b


def hilbert(n):
    """
    :param n: 
    Dimension matrix
    :return: 
    Hilbert matrix (n x n)
    """
    hilb = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            hilb[i, j] = 1. / ((i + 1) + (j + 1) - 1)
    return hilb


def create_vector_b(matrix):
    """
    :param matrix: 
    source matrix 
    :return: 
    random column vector b
    """
    n, = np.shape(matrix)
    rand_b = np.zeros(shape=(n,))
    x = np.random.randint(1, size=(n,))
    for j in range(0, n):
        for i in range(0, n):
            rand_b[j] += matrix[i, j] * x[i]
    return rand_b


def condition(a):
    """
    :param a: 
    source matrix
    :return: 
    condition matrix a
    """
    a_inv = np.linalg.inv(a)
    a_norm = np.linalg.norm(a)
    a_inv_norm = np.linalg.norm(a_inv)

    cond = a_norm * a_inv_norm

    return cond


def rotate(matrix):
    """
    Method of rotation matrix and resolve linear system of equation
    :param matrix: 
    extended matrix
    :return: 
    vector of unknowns x
    """
    n, = np.shape(matrix)
    x = np.zeros(n, )  # Column vector of unknown

    """
    Reduction of the matrix to
    a triangular form
    """
    for i in range(0, n):
        for j in range(i + 1, n):
            a = matrix[i, i]
            b = matrix[j, i]
            c = a / m.sqrt(a * a + b * b)
            s = b / m.sqrt(a * a + b * b)
            for k in range(i, n + 1):
                t = matrix[i, k]
                matrix[i, k] = (c * matrix[i, k]) + (s * matrix[j, k])
                matrix[j, k] = (-s * t) + (c * matrix[j, k])

    """
    Back stroke from the Gauss method
    """
    for i in range(n - 1, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += matrix[i, j] * x[j]
        summ = matrix[i, n] - summ
        if matrix[i, i] == 0:
            return False
        x[i] = summ / matrix[i, i]

    i = 0
    while i < len(x):
        x[i] = int((x[i] * 10000) + 0.5) / 10000
        i += 1

    """
    Vector of discrepancy (Ax - B)
    """
    a, b = create_matrix_txt(form='normal')
    discrep = np.dot(a, x)
    discrep = discrep - b

    print("Method of rotation:\n")
    print("Vector discrepancy: ", discrep)
    print("Vector x: ", x, "\n")

    return x


def householder(a, b):
    """
    Householder method and resolve linear system of equation 
    :param a: 
    source matrix
    :param b:
    column vector b
    :return: 
    vector of unknowns x
    """
    rows, = np.shape(a)
    q = np.identity(rows)  # Orthogonal matrix
    r = np.copy(a)  # Upper triangular matrix

    for i in range(rows - 1):
        b = r[i:, i]  # Column vector

        """The first element of the vector e
           is norm(x) signed -A[i,i](on the main diagonal).
           Now we apply formula b-ac 
        """
        c = np.zeros_like(b)
        c[0] = m.copysign(np.linalg.norm(b), -a[i, i])
        u = b + c
        v = u / np.linalg.norm(u)

        """Now we apply E-2*Omega"""
        Q_om = np.identity(rows)  # Identity matrix
        Q_om[i:, i:] -= 2.0 * np.outer(v, v)

        r = np.dot(Q_om, r)
        q = np.dot(q, Q_om.T)

    """If we know the decomposition A = QR, 
       then the solution reduces to
       solving the system Rx = Q.T * b
    """
    p = np.dot(q.T, b)
    x = np.dot(np.linalg.inv(r), p)

    i = 0
    while i < len(x):
        x[i] = int((x[i] * 10000) + 0.5) / 10000
        i += 1

    # Вектор невязки
    discrep = np.dot(a, x)
    discrep = discrep - b

    print("Method of Householder:")
    print("Vector discrep: ", discrep)
    print("Vector x: ", x)

    return x
