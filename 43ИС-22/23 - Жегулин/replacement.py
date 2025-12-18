class Replacement:
    """
    Класс, представляющий замену продукта по гарантии.

    Атрибуты:
        id (int): Идентификатор замены.
        warranty_claim (WarrantyClaim): Гарантийная заявка, связанная с заменой.
        replacement_date (str): Дата замены.
        reason (str): Причина замены.
    """

    def __init__(self, id, warranty_claim, replacement_date, reason):
        """
        Инициализация замены.

        Аргументы:
            id (int): Идентификатор замены.
            warranty_claim (WarrantyClaim): Гарантийная заявка.
            replacement_date (str): Дата замены.
            reason (str): Причина замены.
        """
        self.id = id
        self.warranty_claim = warranty_claim
        self.replacement_date = replacement_date
        self.reason = reason

    def __str__(self):
        """
        Строковое представление замены.

        Возвращает:
            str: Строка с информацией о замене.
        """
        return (f"Замена(ID: {self.id}, Гарантийная заявка ID: {self.warranty_claim.id}, "
                f"Дата замены: {self.replacement_date}, Причина: {self.reason})")

    def perform_replacement(self):
        """
        Провести замену продукта.
        """
        print(f"Замена для Гарантийной заявки {self.warranty_claim.id} завершена.")

    def get_replacement_reason(self):
        """
        Получить причину замены.

        Возвращает:
            str: Причина замены.
        """
        return f"Причина замены: {self.reason}"
