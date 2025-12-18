# delivery_truck.py
"""Модуль с классом DeliveryTruck."""
class DeliveryTruck:
    """Представляет грузовик доставки."""
    def __init__(self, id: int):
        """Инициализация грузовика."""
        self._id = id

    def get_id(self) -> int:
        """Возвращает id грузовика."""
        return self._id

    def __eq__(self, other: object) -> bool:
        """Сравнивает грузовики по id."""
        if not isinstance(other, DeliveryTruck):
             return False
        return self._id == other._id

    def __str__(self) -> str:
        """Возвращает строковое представление грузовика."""
        return f"Грузовик доставки: ID: {self._id}"

if __name__ == "__main__":
    truck = DeliveryTruck(1)
    print(truck)