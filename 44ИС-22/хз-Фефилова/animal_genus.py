from animal_family import AnimalFamily

class AnimalGenus(AnimalFamily):
    """Класс для представления рода животного, наследуется от AnimalFamily."""

    def __init__(self, genus_name, family_name, order_name, class_name, animal_type):
        super().__init__(family_name, order_name, class_name, animal_type)
        self._genus_name = genus_name

    @property
    def genus_name(self):
        """Геттер для имени рода."""
        return self._genus_name

    @genus_name.setter
    def genus_name(self, value):
        """Сеттер для имени рода."""
        self._genus_name = value

    def __str__(self):
        return f"{super().__str__()}, Род: {self.genus_name}"

if __name__ == "__main__":
    ag = AnimalGenus("Panthera", "Кошачьи", "Хищные", "Хордовые", "Млекопитающие")
    print(ag)