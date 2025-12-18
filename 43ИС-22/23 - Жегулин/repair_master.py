class RepairMaster:
    """
    Класс, представляющий мастера по ремонту.


 Атрибуты:
        id (int): Идентификатор мастера.
        name (str): Имя мастера.
        expertise (str): Экспертиза мастера (например, "Ремонт электроники").
        repair_cost (float): Стоимость ремонта, выполняемого мастером.
    """

    def __init__(self, id, name, expertise, repair_cost):
        """
        Инициализация нового мастера.

        Аргументы:
            id (int): Идентификатор мастера.
            name (str): Имя мастера.
            expertise (str): Экспертиза мастера.
            repair_cost (float): Стоимость ремонта, выполняемого мастером.
        """
        self.id = id
        self.name = name
        self.expertise = expertise
        self.repair_cost = repair_cost

    def __str__(self):
        """
        Строковое представление мастера.

        Возвращает:
            str: Строка с информацией о мастере.
        """
        return f"Мастер(ID: {self.id}, Имя: {self.name}, Экспертиза: {self.expertise})"

    def assign_repair(self, warranty_claim):
        """
        Назначить мастера на гарантийную заявку.

        Аргументы:
            warranty_claim (WarrantyClaim): Гарантийная заявка, на которую назначен мастер.
        """
        print(f"Мастер {self.name} назначен на гарантийную заявку {warranty_claim.id}.")

    def update_repair_cost(self, new_cost):
        """
        Обновить стоимость ремонта.

        Аргументы:
            new_cost (float): Новая стоимость ремонта.
        """
        self.repair_cost = new_cost
        print(f"Стоимость ремонта обновлена на: {self.repair_cost}")
