from animal_class import AnimalClass

class AnimalOrder(AnimalClass):
    """Класс для представления отряда животного, наследуется от AnimalClass."""

    def __init__(self, order_name, class_name, animal_type):
        super().__init__(class_name, animal_type)
        self._order_name = order_name

    @property
    def order_name(self):
        """Геттер для имени отряда."""
        return self._order_name

    @order_name.setter
    def order_name(self, value):
        """Сеттер для имени отряда."""
        self._order_name = value

    def __str__(self):
        return f"{super().__str__()}, Отряд: {self.order_name}"

if __name__ == "__main__":
    ao = AnimalOrder("Хищные", "Хордовые", "Млекопитающие")
    print(ao)