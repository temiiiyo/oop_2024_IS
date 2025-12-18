class RailCar:
    MIN_CAR_TYPE = "грузовой"
    MAX_CAR_TYPE = "пассажирский"
    ALLOWED_CAR_TYPES = [MIN_CAR_TYPE, MAX_CAR_TYPE]

    def __init__(self, car_type):
        """Инициализация вагона."""
        if not self.validate(car_type):
            raise ValueError(f"Неверный тип вагона: {car_type}. Разрешенные типы: {', '.join(self.ALLOWED_CAR_TYPES)}")
        self._car_type = car_type

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, car_type):
        if not self.validate(car_type):
            raise ValueError(f"Неверный тип вагона: {car_type}. Разрешенные типы: {', '.join(self.ALLOWED_CAR_TYPES)}")
        self._car_type = car_type

    @classmethod
    def validate(cls, car_type):
        """Метод для проверки корректности типа вагона."""
        return car_type in cls.ALLOWED_CAR_TYPES

    @staticmethod
    def get_allowed_car_types():
        return RailCar.ALLOWED_CAR_TYPES

    def __eq__(self, other):
        if isinstance(other, RailCar):
            return self.car_type == other.car_type
        return False

    def __str__(self):
        return f"Вагон({self.car_type})"

    def __repr__(self):
        return f"Вагон({self.car_type})"