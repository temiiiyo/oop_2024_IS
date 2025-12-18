class WarrantyClaim:
    """
    Класс, представляющий гарантийную заявку.

    Атрибуты:
        id (int): Идентификатор заявки.
        customer (Customer): Клиент, подавший заявку.
        product (Product): Продукт, на который подана гарантия.
        date (str): Дата подачи заявки.
        reason (str): Причина подачи заявки.
        status (str): Статус заявки (например, "Ожидает", "Принято", "Отказано").
        decision (str, optional): Принятое решение по заявке (например, "Возврат", "Замена", "Ремонт").
    """

    def __init__(self, id, customer, product, date, reason, status, decision=None):
        """
        Инициализация новой гарантийной заявки.

        Аргументы:
            id   (int): Идентификатор заявки.
            customer (Customer): Клиент, подавший заявку.
            product (Product): Продукт, на который подана гарантия.
            date (str): Дата подачи заявки.
            reason (str): Причина подачи заявки.
            status (str): Статус заявки.
            decision (str, optional): Принятое решение по заявке.
        """
        self.id = id
        self.customer = customer
        self.product = product
        self.date = date
        self.reason = reason
        self.status = status
        self.decision = decision

    def __str__(self):
        """
        Строковое представление гарантийной заявки.

        Возвращает:
            str: Строка с информацией о заявке.
        """
        return (f"Гарантийная заявка(ID: {self.id}, Клиент: {self.customer.name}, "
                f"Продукт: {self.product.name}, Дата: {self.date}, Причина: {self.reason}, "
                f"Статус: {self.status}, Решение: {self.decision})")

    def update_status(self, new_status):
        """
        Обновить статус заявки.

        Аргументы:
            new_status (str): Новый статус заявки (например, "Ожидает", "Принято", "Отказано").
        """
        if new_status not in ["Ожидает", "Принято", "Отказано"]:
            raise ValueError("Статус должен быть одним из: Ожидает, Принято, Отказано.")
        self.status = new_status
        print(f"Статус обновлен на: {self.status}")

    def update_decision(self, new_decision):
        """
        Обновить решение по заявке.

        Аргументы:
            new_decision (str): Новое решение (например, "Возврат", "Замена", "Ремонт").
        """
        if new_decision not in ["Возврат", "Замена", "Ремонт"]:
            raise ValueError("Решение должно быть одним из: Возврат, Замена, Ремонт.")
        self.decision = new_decision
        print(f"Решение обновлено на: {self.decision}")
