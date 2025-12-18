class Mesto:
    # Конструктор класса Mesto, инициализирует номер, тип и занятость места
    def __init__(self, number, type, occupied=False):
        self.number = number  # Номер места (например, 1, 2, 3 и т. д.)
        self.type = type  # Тип места (например, "нижняя полка", "верхняя полка")
        self.occupied = occupied  # Занято ли место (по умолчанию False, т.е. место свободно)

    # Метод для отображения информации о месте
    def __str__(self):
        # Возвращает строковое представление места с указанием его номера, типа и занятости
        return f"Место {self.number}: {self.type}, {'занято' if self.occupied else 'свободно'}"

    # Метод для сравнения двух мест
    def __eq__(self, other):
        # Сравнивает два места по типу и номеру
        return self.type == other.type and self.number == other.number
