class Carriage:
    """Класс для представления вагона."""

    def __init__(self, number, carriage_type):
        self.number = number  # Номер вагона
        self.carriage_type = carriage_type  # Тип вагона

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def carriage_type(self):
        return self._carriage_type

    @carriage_type.setter
    def carriage_type(self, value):
        self._carriage_type = value

    def __eq__(self, other):
        return (self.number == other.number and
                self.carriage_type == other.carriage_type)

    def __str__(self):
        return f"Вагон {self.number}: {self.carriage_type}"

if __name__ == '__main__':
    carriage = Carriage(1, "Пассажирский")
    print(carriage)