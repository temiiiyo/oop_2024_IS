from product_man import ProductManager
from operation_log import OperationLog


def main():
    """Основная функция программы."""
    product_manager = ProductManager()
    product_manager.load_p_file("products.txt")

    log = OperationLog()
    log.load_file("operations.txt")

    log.generate_report()

    all_o = log.get_all_o()
    print("Все операции:")
    for op in all_o:
        product = product_manager.get_product(op[0])
        print(f"{product.display_info()}, Тип операции: {op[1]}")

    most_f_op = log.get_most_o()
    if most_f_op:
        print(f"Самая частая операция: {most_f_op[0]}, Количество: {most_f_op[1]}")


if __name__ == "__main__":
    main()
