#спроектироват класс матрица с операциями сравнения матриц, сложение матриц умноженния матрицы на число.
#разработать pytest/unittest для тестирования класса.
#разработать программу для демонстрции раоты с матрицей целых чисел.
#Исходные данные получить с испоьзование генератора случайных чисел.
import random

class Matrix:
    def __init__(self, rows, cols, values=None):
        """
        Инициализация матрицы.
        rows - количество строк.
        cols - количество столбцов.
        values - значения матрицы. Если None, генерируется случайная матрица.
        """
        self.rows = rows
        self.cols = cols
        if values:
            if len(values) != rows or any(len(row) != cols for row in values):
                raise ValueError("Неверные размеры матрицы.")
            self.data = values
        else:
            self.data = [[random.randint(0, 10) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        """Преобразует матрицу в строку для удобного вывода."""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        """
        Проверка на равенство двух матриц.
        other - другая матрица.
        True - если матрицы одинаковы, иначе False.
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))

    def __add__(self, other):
        """
        Сложение двух матриц.
        other - другая матрица.
        return- новая матрица, являющаяся результатом сложения.
        raises ValueError - если матрицы имеют разные размеры.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        return Matrix(self.rows, self.cols, [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __mul__(self, scalar):
        """
        Умножение матрицы на скаляр.
        scalar - число, на которое умножается матрица.
        return - новая матрица, являющаяся результатом умножения.
        """
        return Matrix(self.rows, self.cols, [
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    @staticmethod
    def create_random_matrix(rows, cols, min_val=0, max_val=10):
        data = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
        return Matrix(rows, cols, data)

    @staticmethod
    def add_matrices(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        return Matrix(matrix1.rows, matrix1.cols, [
            [matrix1.data[i][j] + matrix2.data[i][j] for j in range(matrix1.cols)]
            for i in range(matrix1.rows)
        ])

if __name__ == "__main__":
    matrix1 = Matrix.create_random_matrix(3, 3)
    matrix2 = Matrix.create_random_matrix(3, 3)

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nMatrix 1 + Matrix 2:")
    print(Matrix.add_matrices(matrix1, matrix2))

    print("\nMatrix 1 * 3:")
    print(matrix1 * 3)

