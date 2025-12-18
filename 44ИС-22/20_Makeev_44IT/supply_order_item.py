# supply_order_item.py
"""Модуль с классом SupplyOrderItem."""
class SupplyOrderItem:
    """Представляет позицию в заказе поставщику."""
    def __init__(self, product_id: int, quantity: int):
        """Инициализация позиции в заказе поставщику."""
        self._product_id = product_id
        self._quantity = quantity

    def get_product_id(self) -> int:
        """Возвращает id товара."""
        return self._product_id

    def get_quantity(self) -> int:
        """Возвращает количество товара."""
        return self._quantity

    def __eq__(self, other: object) -> bool:
        """Сравнивает позиции заказа поставщику по id товара и количеству."""
        if not isinstance(other, SupplyOrderItem):
            return False
        return self._product_id == other._product_id and self._quantity == other._quantity

    def __str__(self) -> str:
        """Возвращает строковое представление позиции заказа поставщику."""
        return f"ProductID: {self._product_id}, Количество: {self._quantity}"

if __name__ == "__main__":
    item = SupplyOrderItem(1, 2)
    print(item)