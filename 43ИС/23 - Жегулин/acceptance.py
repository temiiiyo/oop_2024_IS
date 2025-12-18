class Acceptance:
    """
    Класс, представляющий принятие гарантийной заявки.

    Атрибуты:
        id (int): Идентификатор принятия.
        warranty_claim (WarrantyClaim): Гарантийная заявка, которая была принята.
        acceptance_date (str): Дата принятия заявки.
        status (str): Статус принятия (например, "Ожидает", "Принято", "Отказано").
    """

    def __init__(self, id, warranty_claim, acceptance_date, status):
        """
        Инициализация принятия гарантийной заявки.

        Аргументы:
            id (int): Идентификатор принятия.
            warranty_claim (WarrantyClaim): Гарантийная заявка.
            acceptance_date (str): Дата принятия.
            status (str): Статус принятия заявки.
        """
        self.id = id
        self.warranty_claim = warranty_claim
        self.acceptance_date = acceptance_date
        self.status = status

    def __str__(self):
        """
        Строковое представление принятия заявки.

        Возвращает:
            str: Строка с информацией о принятии.
        """
        return (f"Принятие(ID: {self.id}, Гарантийная заявка ID: {self.warranty_claim.id}, "
                f"Дата принятия: {self.acceptance_date}, Статус: {self.status})")

    def update_status(self, new_status):
        """
        Обновить статус принятия заявки.

        Аргументы:
            new_status (str): Новый статус принятия (например, "Ожидает", "Принято", "Отказано").
        """
        if new_status not in ["Ожидает", "Принято", "Отказано"]:
            raise ValueError("Статус должен быть одним из: Ожидает, Принято, Отказано.")
        self.status = new_status
        print(f"Статус принятия обновлен на: {self.status}")

    def get_acceptance_info(self):
        """
        Получить информацию о принятии заявки.

        Возвращает:
            str: Информация о принятии заявки.
        """
        return f"Принятие ID: {self.id}, Дата: {self.acceptance_date}, Статус: {self.status}"
