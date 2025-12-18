# order_item.py
"""Модуль с классом OrderItem."""
class OrderItem:
    """Представляет позицию в заказе."""
    def __init__(self, product_id: int, quantity: int):
        """Инициализация позиции в заказе."""
        self._product_id = product_id
        self._quantity = quantity

    def get_product_id(self) -> int:
        """Возвращает id товара."""
        return self._product_id

    def get_quantity(self) -> int:
        """Возвращает количество товара."""
        return self._quantity

    def __eq__(self, other: object) -> bool:
        """Сравнивает позиции заказа по id товара и количеству."""
        if not isinstance(other, OrderItem):
            return False
        return self._product_id == other._product_id and self._quantity == other._quantity

    def __str__(self) -> str:
        """Возвращает строковое представление позиции заказа."""
        return f"ProductID: {self._product_id}, Quantity: {self._quantity}"

if __name__ == "__main__":
    item = OrderItem(1, 2)
    print(item)