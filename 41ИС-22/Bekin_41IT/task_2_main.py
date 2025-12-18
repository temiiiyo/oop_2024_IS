import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape

    def random(rows, cols, min_val=1, max_val=10):
        data = np.random.randint(min_val, max_val + 1, size=(rows, cols))
        return Matrix(data)

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return Matrix(self.data == other.data)

    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        return Matrix(self.data - other.data)

    def __mul__(self, n):
        return Matrix(self.data * n)


mtx1 = Matrix.random(3, 3)
mtx2 = Matrix.random(3, 3)

print("Матрица 1:")
print(mtx1)

print("Матрица 2:")
print(mtx2)

if mtx1 == mtx2:
    print("1. Матрицы ранвы")
else:
    print("1. Матрицы не равны")


summa = mtx1 + mtx2
print(f"2. Сумма:\n {summa}")

sb = mtx1 - mtx2
print(f"3. Доп. функция разность:\n {sb}")

n = int(input())

mtx = mtx1 * n
print(f"5. Произведение на {n} первой матрицы:\n {mtx}")