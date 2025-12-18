class Car:
    def __init__(self, license_plate: str, mark: str, model: str, year: int):
        """Госномер"""
        self._license_plate = license_plate
        self._mark = mark
        self._model = model
        self._year = year

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value: str):
        self._license_plate = value

    def __str__(self):
        """Возвращает информацию об авто"""
        return f"{self._mark} {self._model} ({self._year}) - {self._license_plate}"

    def __eq__(self, other):
        """Сравнивает номера авто"""
        return self._license_plate == other._license_plate

    def __len__(self):
        """Возвращает длину номера авто"""
        return len(self._license_plate)

    @staticmethod
    def read_cars(file_path: str):
        cars = []
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    license_plate, mark, model, year = line.strip().split()
                    year = int(year)
                    car = Car(license_plate, mark, model, year)
                    cars.append(car)
                except ValueError:
                    print(f"Пропущена строка с некорректным форматом: '{line.strip()}'")
        return cars

    @classmethod
    def from_string(cls, data: str):
        license_plate, mark, model, year = data.strip().split(',')
        year = int(year)
        return cls(license_plate, mark, model, year)

    def __add__(self, other):

        if isinstance(other, Car):
            return self._year + other._year
        return NotImplemented


if __name__ == "__main__":
    file_path = "cars.txt"
    try:
        cars = Car.read_cars(file_path)
        for car in cars:
            print(car)

        # Пример использования метода from_string
        new_car = Car.from_string("GHI456,Ford,Focus,2019")
        print(new_car)

        # Пример использования метода __add__
        total_years = cars[0] + cars[1]  # Складывает годы первого и второго автомобиля
        print(f"Суммарный год: {total_years}")

    except FileNotFoundError:
        print(f"Ошибка, файл '{file_path}' не найден.")


