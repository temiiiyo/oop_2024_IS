"""Модуль с классом Order."""
import datetime
from typing import List
from order_item import OrderItem
from order_status import OrderStatus


class Order:
    """Представляет заказ."""

    def __init__(self, id: int, customer_id: int, order_date: datetime.datetime, distance_to_warehouse: int):
        """Инициализация заказа."""
        self._id = id
        self._customer_id = customer_id
        self._items = []
        self._order_date = order_date
        self._distance_to_warehouse = distance_to_warehouse
        self._status = OrderStatus.PENDING

    def get_id(self) -> int:
        """Возвращает id заказа."""
        return self._id

    def get_customer_id(self) -> int:
        """Возвращает id клиента."""
        return self._customer_id

    def get_order_date(self) -> datetime.datetime:
        """Возвращает дату заказа."""
        return self._order_date

    def get_distance_to_warehouse(self) -> int:
        """Возвращает расстояние до склада."""
        return self._distance_to_warehouse

    def get_status(self) -> OrderStatus:
        """Возвращает статус заказа."""
        return self._status

    def set_status(self, status: OrderStatus):
        """Устанавливает статус заказа."""
        self._status = status

    def add_item(self, item: OrderItem):
        """Добавляет позицию в заказ."""
        self._items.append(item)

    def get_items(self) -> List[OrderItem]:
        """Возвращает позиции заказа."""
        return self._items

    def __eq__(self, other: object) -> bool:
        """Сравнивает заказы по id."""
        if not isinstance(other, Order):
            return False
        return self._id == other._id

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"ID: {self._id}, Customer ID: {self._customer_id}, Date: {self._order_date}, Distance: {self._distance_to_warehouse}, Status: {self._status}"

    @classmethod
    def create_from_dict(cls, data: dict) -> 'Order':
        """Создает объект Order из словаря.

         Args:
            data (dict): Словарь с данными {id, customer_id, order_date, distance_to_warehouse}
         Returns:
             Order: Созданный заказ
        """
        if not all(key in data for key in ["id", "customer_id", "order_date", "distance_to_warehouse"]):
            raise ValueError("Invalid keys in dictionary for Order creation")
        return cls(id=data["id"], customer_id=data["customer_id"], order_date=data["order_date"],
                   distance_to_warehouse=data["distance_to_warehouse"])


def load_orders_from_file(filename):
    """Загружает заказы из файла."""
    orders = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, customerId, orderDate, distanceToWarehouse = line.strip().split(',')
                order = Order(int(id), int(customerId), datetime.datetime.strptime(orderDate, '%Y-%m-%d %H:%M:%S'),
                              int(distanceToWarehouse))
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return orders


if __name__ == "__main__":
    orders = load_orders_from_file('orders.txt')