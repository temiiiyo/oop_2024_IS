from animal_genus import AnimalGenus

class AnimalSpecies(AnimalGenus):
    """Класс для представления вида животного, наследуется от AnimalGenus."""

    def __init__(self, species_name, genus_name, family_name, order_name, class_name, animal_type):
        super().__init__(genus_name, family_name, order_name, class_name, animal_type)
        self._species_name = species_name

    @property
    def species_name(self):
        """Геттер для имени вида."""
        return self._species_name

    @species_name.setter
    def species_name(self, value):
        """Сеттер для имени вида."""
        self._species_name = value

    def __str__(self):
        return f"{super().__str__()}, Вид: {self.species_name}"

if __name__ == "__main__":
    aspec = AnimalSpecies("Лев", "Panthera", "Кошачьи", "Хищные", "Хордовые", "Млекопитающие")
    print(aspec)