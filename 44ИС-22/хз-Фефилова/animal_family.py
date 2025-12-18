from animal_order import AnimalOrder

class AnimalFamily(AnimalOrder):
    """Класс для представления семейства животного, наследуется от AnimalOrder."""

    def __init__(self, family_name, order_name, class_name, animal_type):
        super().__init__(order_name, class_name, animal_type)
        self._family_name = family_name

    @property
    def family_name(self):
        """Геттер для имени семейства."""
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        """Сеттер для имени семейства."""
        self._family_name = value

    def __str__(self):
        return f"{super().__str__()}, Семейство: {self.family_name}"

if __name__ == "__main__":
    af = AnimalFamily("Кошачьи", "Хищные", "Хордовые", "Млекопитающие")
    print(af)