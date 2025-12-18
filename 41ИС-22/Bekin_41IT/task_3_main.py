import random


def gen_mtx(rows, cols, min_val=1, max_val=10):
    mtx = [[random.randint(min_val, max_val) for i in range(cols)] for j in range(rows)]
    return mtx


def sum_el_rows(mtx):
    row_sums = [sum(row) for row in mtx]
    return row_sums


def save_file(mtx, row_sums, filename="matrix_task_3.txt"):

    with open(filename, "w") as file:
        file.write("Matrix:\n")
        for row in mtx:
            file.write(" ".join(map(str, row)) + "\n")
        file.write("\nSumma el in evry rows:\n")
        file.write(" ".join(map(str, row_sums)) + "\n")


rows, cols = 5, 5
min_val, max_val = 1, 10

mtx = gen_mtx(rows, cols, min_val, max_val)

print("Сгенерированная матрица:")
for row in mtx:
    print(" ".join(map(str, row)))


row_sums = sum_el_rows(mtx)
print("\nСумма элементов в каждой строке:")
print(" ".join(map(str, row_sums)))

save_file(mtx, row_sums)
print("\nРезультаты сохранены в файл 'matrix_task_3.txt'.")