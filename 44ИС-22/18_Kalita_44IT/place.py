class Place:
    """Класс для представления места назначения."""

    def __init__(self, name, coordinates):
        self.name = name  # Название места
        self.coordinates = coordinates  # Координаты места (широта, долгота)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    def __eq__(self, other):
        return (self.name == other.name and
                self.coordinates == other.coordinates)

    def __str__(self):
        return f"Место: {self.name}, Координаты: {self.coordinates}"

if __name__ == '__main__':
    place = Place("Москва", (55.7558, 37.6173))
    print(place)