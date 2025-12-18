# store_keeper.py
"""Модуль с классом StoreKeeper и командами."""
from warehouse import Warehouse


class WarehouseCommand:
    """Интерфейс для команд склада."""

    def execute(self):
        """Выполняет команду."""
        raise NotImplementedError


class ReceiveProductCommand(WarehouseCommand):
    """Команда приема товара."""

    def __init__(self, store_keeper, product_id, quantity):
        """Инициализирует команду приема товара."""
        self._store_keeper = store_keeper
        self._product_id = product_id
        self._quantity = quantity

    def execute(self):
        """Выполняет команду приема товара."""
        self._store_keeper.receive_product(self._product_id, self._quantity)


class ReleaseProductCommand(WarehouseCommand):
    """Команда отпуска товара."""

    def __init__(self, store_keeper, product_id, quantity):
        """Инициализирует команду отпуска товара."""
        self._store_keeper = store_keeper
        self._product_id = product_id
        self._quantity = quantity

    def execute(self):
        """Выполняет команду отпуска товара."""
        return self._store_keeper.release_product(self._product_id, self._quantity)


class StoreKeeper:
    """
    Представляет кладовщика.

    Атрибуты:
         _warehouse (Warehouse): Склад.
    """

    def __init__(self, warehouse: Warehouse):
        """
         Инициализация кладовщика.
         Args:
            warehouse (Warehouse): Склад.
        """
        self._warehouse = warehouse

    def receive_product(self, product_id: int, quantity: int):
        """Принимает товар на склад.

        Args:
            product_id (int): Идентификатор товара.
            quantity (int): Количество товара для приема.
        """
        product = self._warehouse.get_product(product_id)
        if product:
            self._warehouse.update_product_quantity(product_id, product.get_quantity() + quantity)
        else:
            print(f"Product ID:{product_id} not found")

    def release_product(self, product_id: int, quantity: int) -> bool:
        """Отпускает товар со склада.
         Args:
            product_id (int): Идентификатор товара.
            quantity (int): Количество товара для отпуска.
         Returns:
            bool: True, если удалось отпустить, False в противном случае.
        """
        return self._warehouse.reduce_product_quantity(product_id, quantity)

    def __str__(self) -> str:
        """Возвращает строковое представление кладовщика."""
        return f"кладовщик: Склад: {self._warehouse}"


if __name__ == "__main__":
    from warehouse import Warehouse

    warehouse = Warehouse()
    store_keeper = StoreKeeper(warehouse)
    print(store_keeper)