# supply_order.py
"""Модуль с классом SupplyOrder, представляющим заказ поставщику."""
from typing import List
from supply_order_item import SupplyOrderItem


class SupplyOrder:
    """
    Представляет заказ поставщику.

    Атрибуты:
        _id (int): Уникальный идентификатор заказа поставщику.
        _supplier_id (int): Идентификатор поставщика.
        _items (list[SupplyOrderItem]): Список позиций заказа.
    """

    def __init__(self, id: int, supplier_id: int):
        """
        Инициализирует объект SupplyOrder.

        Args:
           id (int): Уникальный идентификатор заказа поставщику.
           supplier_id (int): Идентификатор поставщика.
        """
        self._id = id
        self._supplier_id = supplier_id
        self._items = []

    def get_id(self) -> int:
        """Возвращает идентификатор заказа поставщику."""
        return self._id

    def get_supplier_id(self) -> int:
        """Возвращает идентификатор поставщика."""
        return self._supplier_id

    def add_item(self, item: SupplyOrderItem):
        """Добавляет позицию в заказ.

        Args:
           item (SupplyOrderItem): Позиция в заказе.
        """
        self._items.append(item)

    def get_items(self) -> List[SupplyOrderItem]:
        """Возвращает позиции заказа поставщику."""
        return self._items

    def __eq__(self, other: object) -> bool:
        """Сравнивает два объекта SupplyOrder по их id.

         Args:
            other (object): Объект для сравнения.

         Returns:
             bool: True, если id совпадают, False в противном случае.
         """
        if not isinstance(other, SupplyOrder):
            return False
        return self._id == other._id

    def __len__(self) -> int:
        """Возвращает количество позиций в заказе поставщику."""
        return len(self._items)

    def __add__(self, other: object) -> object:
        """Объединяет два заказа поставщику, добавляя позиции из другого заказа.

        Args:
          other (object): Другой заказ поставщику для объединения.

        Returns:
          object: Новый заказ поставщику, содержащий позиции из обоих заказов.
        """
        if not isinstance(other, SupplyOrder):
            raise TypeError("Unsupported operand type for +: SupplyOrder and {}".format(type(other)))

        new_supply_order = SupplyOrder(
            id=max(self._id, other._id) + 1,
            supplier_id=self._supplier_id,
        )
        new_supply_order._items = self._items + other._items
        return new_supply_order

    def __str__(self) -> str:
        """Возвращает строковое представление заказа поставщику."""
        return f"ID: {self._id}, Supplier ID: {self._supplier_id}"


if __name__ == "__main__":
    supply_order1 = SupplyOrder(1, 1)
    print(supply_order1)
    supply_order2 = SupplyOrder(2, 1)
    print(f"supply_order1 == supply_order2: {supply_order1 == supply_order2}")
    supply_order3 = SupplyOrder(1, 1)
    print(f"supply_order1 == supply_order3: {supply_order1 == supply_order3}")
    from .supply_order_item import SupplyOrderItem

    supply_order1.add_item(SupplyOrderItem(1, 2))
    supply_order1.add_item(SupplyOrderItem(2, 1))
    print(f"Количество предметов: {len(supply_order1)}")

    supply_order2.add_item(SupplyOrderItem(3, 3))
    new_supply_order = supply_order1 + supply_order2
    print(f"Количество позиций нового заказа на поставку: {len(new_supply_order)}")
    print(f"Новый заказ на поставку: {new_supply_order}")