class Repair:
    """
    Класс, представляющий ремонт по гарантии.

    Атрибуты:
        id (int): Идентификатор ремонта.
        warranty_claim (WarrantyClaim): Гарантийная заявка, связанная с ремонтом.
        repair_cost (float): Стоимость ремонта.
        repair_date (str): Дата проведения ремонта.
        description (str): Описание ремонта.
    """

    def __init__(self, id, warranty_claim, repair_cost, repair_date, description):
        """
        Инициализация ремонта.

        Аргументы:
            id (int): Идентификатор ремонта.
            warranty_claim (WarrantyClaim): Гарантийная заявка.
            repair_cost (float): Стоимость ремонта.
            repair_date (str): Дата проведения ремонта.
            description (str): Описание ремонта.
        """
        self.id = id
        self.warranty_claim = warranty_claim
        self.repair_cost = repair_cost
        self.repair_date = repair_date
        self.description = description

    def __str__(self):
        """
        Строковое представление ремонта.

        Возвращает:
            str: Строка с информацией о ремонте.
        """
        return (f"Ремонт(ID: {self.id}, Гарантийная заявка ID: {self.warranty_claim.id}, "
                f"Стоимость ремонта: {self.repair_cost}, Дата ремонта: {self.repair_date}, "
                f"Описание: {self.description})")

    def perform_repair(self):
        """
        Провести ремонт по гарантии.
        """
        print(f"Ремонт ID {self.id} для Гарантийной заявки {self.warranty_claim.id} завершен.")

    def calculate_total_cost(self, additional_cost):
        """
        Рассчитать общую стоимость ремонта с учетом дополнительных расходов.

        Аргументы:
            additional_cost (float): Дополнительные расходы.

        Возвращает:
            float: Общая стоимость ремонта.
        """
        total_cost = self.repair_cost + additional_cost
        print(f"Общая стоимость ремонта: {total_cost}")
        return total_cost
