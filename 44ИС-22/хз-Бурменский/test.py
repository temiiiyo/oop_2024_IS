
from main import Matrix

def test_matrix_equality():
    # Проверяем равенство матриц
    matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
    matrix2 = Matrix(2, 2, [[1, 2], [3, 4]])
    matrix3 = Matrix(2, 2, [[5, 6], [7, 8]])
    assert matrix1 == matrix2
    assert matrix1 != matrix3
