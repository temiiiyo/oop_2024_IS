# supply_manager.py
"""Модуль с классом SupplyManager."""
from typing import List
from supplier import Supplier
from supply_order import SupplyOrder

class SupplyManager:
    """Управляет поставками."""
    def __init__(self):
        """Инициализация менеджера поставок."""
        self._suppliers = []

    def add_supplier(self, supplier: Supplier):
        """Добавляет поставщика."""
        self._suppliers.append(supplier)

    def create_order(self, supply_order: SupplyOrder):
        """Создает заказ поставщику."""
        print(f"Создан заказ на поставку с ID {supply_order.get_id()} для поставщика ID {supply_order.get_supplier_id()}")
        for item in supply_order.get_items():
            print(f"ProductID: {item.get_product_id()}, Количество: {item.get_quantity()}")

    def get_supplier(self, supplier_id: int) -> Supplier | None:
        """Возвращает поставщика по id."""
        for supplier in self._suppliers:
            if supplier.get_id() == supplier_id:
                return supplier
        return None

    def __str__(self) -> str:
        """Возвращает строковое представление менеджера поставок."""
        return f"Поставщики: {', '.join([str(supplier) for supplier in self._suppliers])}"

if __name__ == "__main__":
    supply_manager = SupplyManager()
    print(supply_manager)