import numpy as np
import math as m

f = open('matrix')
n = int(f.read(1))  # Размерность
matrix_txt = np.loadtxt('matrix', skiprows=1)  # Расширенная матрица

B = [0 for i in range(n)]  # Вектор-столбец B
for i in range(0, n):
    B[i] = matrix_txt[i, n]

A = matrix_txt  # Матрица A
A = np.delete(A, n, 1)

x = [0 for i in range(n)]  # Вектор-стоблец неизвестных

def rotate(matrix):
    """Метод вращений"""

    for i in range(0, n):  # Приведение матрицы к треугольному виду
        for j in range(i + 1, n):
            a = matrix[i, i]
            b = matrix[j, i]
            c = a / m.sqrt(a * a + b * b)
            s = b / m.sqrt(a * a + b * b)
            for k in range(i, n + 1):
                t = matrix[i, k]
                matrix[i, k] = (c * matrix[i, k]) + (s * matrix[j, k])
                matrix[j, k] = (-s * t) + (c * matrix[j, k])

    for i in range(n - 1, -1, -1):  # Обратный ход
        summ = 0
        for j in range(i + 1, n):
            summ += matrix[i, j] * x[j]
        summ = matrix[i, n] - summ
        if matrix[i, i] == 0:
            return False
        x[i] = summ / matrix[i, i]

    # Вектор невязки
    discrep = np.dot(A, x)
    discrep = discrep - B

    print("Method of rotation:")
    print("Vector discrep: ", discrep)
    print("Vector x: ", x, "\n")


def householder(a):
    """Метод отражений"""

    (rows, cols) = np.shape(a)
    q = np.identity(rows)  # Ортогональная матрица
    r = np.copy(a)  # Верхнетреугольная матрица

    for i in range(rows - 1):
        b = r[i:, i]  # Вектор-столбец матрицы А

        """Установим первый элемент вектора e
           в  norm(x) со знаком -A[i,i](по главной диагонали).
           Т.е. далее, чтобы применить формулу b-ac 
           мы запишем b+c.
        """
        c = np.zeros_like(b)
        c[0] = m.copysign(np.linalg.norm(b), -a[i, i])
        u = b + c
        v = u / np.linalg.norm(u)  # Делим u на норму u

        """Теперь мы используем формулу E-2*Omega"""
        Q_om = np.identity(rows)  # Еденичная матрица
        Q_om[i:, i:] -= 2.0 * np.outer(v, v)

        r = np.dot(Q_om, r)
        q = np.dot(q, Q_om.T)

    """Если известно разложение A = QR, 
       то решение сводится к 
       решению системы  Rx = Q.T * b
    """
    p = np.dot(q.T, B)
    hx = np.dot(np.linalg.inv(r), p)

    # Вектор невязки
    discrep = np.dot(a, x)
    discrep = discrep - B

    print("Method of Householder:")
    print("Vector discrep: ", discrep)
    print("Vector x: ", hx)
