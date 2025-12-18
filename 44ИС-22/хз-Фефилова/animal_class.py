from animal_type import AnimalType

class AnimalClass(AnimalType):
    """Класс для представления класса животного, наследуется от AnimalType."""

    total_animal = 0
    def __init__(self, class_name, animal_type):
        super().__init__(animal_type)
        self._class_name = class_name

    total_animal += 1

    @property
    def class_name(self):
        """Геттер для имени класса."""
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        """Сеттер для имени класса."""
        self._class_name = value

    def __str__(self):
        return f"{super().__str__()}, Класс: {self.class_name}"

    @classmethod
    def pop(cls):
        return cls.total_animal

if __name__ == "__main__":
    ac = AnimalClass("Хордовые", "Млекопитающие")
    print(ac)
    print(ac.pop())


