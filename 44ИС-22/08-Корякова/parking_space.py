class ParkingSpace:

    def __init__(self, space_number: int):
        """Гос номер"""
        self._space_number = space_number
        """Статус"""
        self._is_occupied = False
        self._car = None

    @property
    def is_occupied(self):
        return self._is_occupied

    @property
    def car(self):
        return self._car
    """Занимает место"""
    def occupy(self, car):
        if not self.is_occupied:
            self._car = car
            self._is_occupied = True
            return True
        return False
    """Освобождает место"""
    def vacate(self):
        if self.is_occupied:
            self._car = None
            self._is_occupied = False
    """Возвращает информацию о статусе места"""
    def __str__(self):
        return f"Место {self._space_number}: {'Занято' if self.is_occupied else 'Свободно'}"


if __name__ == "__main__":
    space = ParkingSpace(1)
    print(space)
