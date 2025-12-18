class OperationLog:
    """Класс для ведения журнала операций."""

    def __init__(self):
        """Инициализация журнала операций."""
        self.operations = []

    def log_operation(self, product_id, o_type):
        """Логирует операцию в журнал.

        Args:
            product_id (int): Идентификатор товара.
            o_type (str): Тип операции.
        """
        self.operations.append((product_id, o_type))

    def generate_report(self):
        """Генерирует отчет о всех операциях и сохраняет его в файл."""
        operation_count = {}
        for _, operation in self.operations:
            if operation in operation_count:
                operation_count[operation] += 1
            else:
                operation_count[operation] = 1

        with open("operation_report.txt", "w", encoding='utf-8') as file:
            for operation, count in operation_count.items():
                file.write(f"Операция: {operation}, Количество: {count}\n")

        if operation_count:
            most_operation = max(operation_count.items(), key=lambda x: x[1])
            with open("most_operation.txt", "w", encoding='utf-8') as most_file:
                most_file.write(
                    f"Самая частая операция: {most_operation[0]}, Количество: {most_operation[1]}\n")

    def get_all_o(self):
        """Возвращает все зарегистрированные операции.

        Returns:
            list: Список операций.
        """
        return self.operations

    def get_most_o(self):
        """Возвращает самую частую операцию.

        Returns:
            tuple: Кортеж с самой частой операцией и ее количеством или None, если операций нет.
        """
        if not self.operations:
            return None

        operation_count = {}
        for _, operation in self.operations:
            if operation in operation_count:
                operation_count[operation] += 1
            else:
                operation_count[operation] = 1

        return max(operation_count.items(), key=lambda x: x[1])

    def load_file(self, filename):
        """Загружает операции из файла и добавляет их в журнал.

        Args:
            filename (str): Имя файла для загрузки операций.
        """
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                product_id, o_type = line.strip().split(',')
                self.log_operation(int(product_id), o_type)
