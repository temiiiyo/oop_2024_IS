class DepartmentHead:
    """
    Класс для представления начальника отдела.

    Атрибуты:
        id (int): Уникальный идентификатор начальника отдела.
        name (str): Имя начальника.
        decision (str, optional): Решение начальника отдела по заявке.
    """

    def __init__(self, id, name, decision=None):
        """
        Инициализация начальника отдела.

        Аргументы:
            id (int): Уникальный идентификатор начальника отдела.
            name (str): Имя начальника.
            decision (str, optional): Решение начальника отдела по заявке (например, "Возврат", "Замена", "Ремонт").
        """
        self.id = id
        self.name = name
        self.decision = decision

    def __str__(self):
        """
        Строковое представление начальника отдела.

        Возвращает:
            str: Строка с информацией о начальнике отдела.
        """
        return f"Начальник отдела(ID: {self.id}, Имя: {self.name}, Решение: {self.decision})"

    def update_decision(self, new_decision):
        """
        Обновить решение начальника отдела по заявке.

        Аргументы:
            new_decision (str): Новое решение (например, "Возврат", "Замена", "Ремонт").
        """
        if new_decision not in ["Возврат", "Замена", "Ремонт"]:
            raise ValueError("Решение должно быть одним из: Возврат, Замена, Ремонт.")
        self.decision = new_decision
        print(f"Решение обновлено на: {self.decision}")

    def get_department_head_info(self):
        """
        Получить информацию о начальнике отдела.

        Возвращает:
            str: Информация о начальнике отдела.
        """
        return f"Начальник отдела ID: {self.id}, Имя: {self.name}, Решение: {self.decision}"
