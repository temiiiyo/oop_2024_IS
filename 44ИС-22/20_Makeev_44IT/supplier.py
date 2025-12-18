# supplier.py
"""Модуль с классом Supplier."""
class Supplier:
    """Представляет поставщика."""
    def __init__(self, id: int, name: str):
        """Инициализация поставщика."""
        self._id = id
        self._name = name

    def get_id(self) -> int:
        """Возвращает id поставщика."""
        return self._id

    def get_name(self) -> str:
        """Возвращает имя поставщика."""
        return self._name

    def __eq__(self, other: object) -> bool:
        """Сравнивает поставщиков по id."""
        if not isinstance(other, Supplier):
            return False
        return self._id == other._id

    def __str__(self) -> str:
        """Возвращает строковое представление поставщика."""
        return f"ID: {self._id}, Name: {self._name}"

if __name__ == "__main__":
    supplier = Supplier(1, "Diksi")
    print(supplier)