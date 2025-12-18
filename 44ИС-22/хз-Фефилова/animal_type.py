class AnimalType:
    """Класс для представления типа животного."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Геттер для имени типа."""
        return self._name

    @name.setter
    def name(self, value):
        """Сеттер для имени типа."""
        self._name = value

    def __str__(self):
        return f"Тип: {self.name}"

    def __eq__(self, other):
        return isinstance(other, AnimalType) and self.name == other.name

    def __len__(self):
        return len(self.name)

if __name__ == "__main__":
    at = AnimalType("Млекопитающие")
    print(at)