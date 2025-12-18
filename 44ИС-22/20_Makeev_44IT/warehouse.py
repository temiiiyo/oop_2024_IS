# warehouse.py
"""Модуль с классом Warehouse, представляющим склад."""
from typing import List
from product import Product


class Warehouse:
    """
    Представляет склад.

    Атрибуты:
        _products (list[Product]): Список товаров на складе.
    """

    def __init__(self):
        """Инициализация склада."""
        self._products = []

    def add_product(self, product: Product):
        """Добавляет товар на склад.

         Args:
            product (Product): Товар для добавления.
        """
        self._products.append(product)

    def get_product(self, product_id: int) -> Product | None:
        """Возвращает товар по id.

        Args:
            product_id (int): Идентификатор товара.

        Returns:
             Product | None: Товар, если найден, None в противном случае.
        """
        for product in self._products:
            if product.get_id() == product_id:
                return product
        return None

    def update_product_quantity(self, product_id: int, quantity: int):
        """Обновляет количество товара на складе.

        Args:
            product_id (int): Идентификатор товара.
            quantity (int): Новое количество товара.
        """
        product = self.get_product(product_id)
        if product:
            product.set_quantity(quantity)

    def get_products(self) -> List[Product]:
        """Возвращает список товаров на складе."""
        return self._products

    def check_stock(self, product_id: int, quantity: int) -> bool:
        """Проверяет наличие товара на складе.

        Args:
            product_id (int): Идентификатор товара.
            quantity (int): Необходимое количество товара.

        Returns:
            bool: True, если достаточно, False в противном случае.
        """
        product = self.get_product(product_id)
        if product and product.get_quantity() >= quantity:
            return True
        return False

    def reduce_product_quantity(self, product_id: int, quantity: int) -> bool:
        """Уменьшает количество товара на складе.

         Args:
            product_id (int): Идентификатор товара.
            quantity (int): Количество товара для уменьшения.

         Returns:
            bool: True, если удалось уменьшить, False в противном случае.
        """
        product = self.get_product(product_id)
        if product and product.get_quantity() >= quantity:
            product.set_quantity(product.get_quantity() - quantity)
            return True
        return False

    def __len__(self) -> int:
        """Возвращает количество товаров на складе."""
        return len(self._products)

    def __str__(self) -> str:
        """Возвращает строковое представление склада."""
        return f"Склад: {', '.join([str(product) for product in self._products])}"


if __name__ == "__main__":
    warehouse = Warehouse()
    print(f"Склад: {warehouse}")
    from product import Product

    product1 = Product(1, "Test Product 1", 10.0, 100)
    product2 = Product(2, "Test Product 2", 20.0, 200)
    warehouse.add_product(product1)
    warehouse.add_product(product2)
    print(f"Склад после добавления товаров: {warehouse}")
    print(f"Количество продуктов: {len(warehouse)}")

    print(f"Проверьте наличие на складе товара 1 (50 наименований): {warehouse.check_stock(1, 50)}")
    print(f"Сократите запас товара 1 (на 10 наименований): {warehouse.reduce_product_quantity(1, 10)}")
    print(f"Проверьте наличие на складе товара 1 (50 наименований): {warehouse.check_stock(1, 50)}")
    print(f"Склад после сокращения продукта 1: {warehouse}")