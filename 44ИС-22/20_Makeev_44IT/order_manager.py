# order_manager.py
"""Модуль с классом OrderManager, управляющим заказами."""
import random
from typing import List
from warehouse import Warehouse
from order import Order
from supply_order import SupplyOrder
from order_item import OrderItem
from supply_order_item import SupplyOrderItem
from order_status import OrderStatus

class OrderStatusChangeObserver:
    """Интерфейс для наблюдателей за статусом заказа."""
    def update(self, order: Order):
        """Уведомляет наблюдателя об изменении статуса заказа."""
        raise NotImplementedError

class OrderManager(OrderStatusChangeObserver):
    """
    Управляет заказами.

    Атрибуты:
        _warehouse (Warehouse): Склад.
        _orders (list[Order]): Список заказов.
        _supply_orders (list[SupplyOrder]): Список заказов поставщикам.
        _observers (list[OrderStatusChangeObserver]): Список наблюдателей.
    """
    def __init__(self, warehouse: Warehouse):
        """
        Инициализирует объект OrderManager.

        Args:
            warehouse (Warehouse): Склад.
        """
        self._warehouse = warehouse
        self._orders = []
        self._supply_orders = []
        self._observers = []

    def add_observer(self, observer: OrderStatusChangeObserver):
        """Добавляет наблюдателя."""
        self._observers.append(observer)

    def remove_observer(self, observer: OrderStatusChangeObserver):
        """Удаляет наблюдателя."""
        self._observers.remove(observer)

    def notify_observers(self, order: Order):
        """Уведомляет всех наблюдателей об изменении статуса."""
        for observer in self._observers:
             observer.update(order)

    def process_new_order(self, order: Order):
        """Обрабатывает новый заказ."""
        for item in order.get_items():
            if not self._warehouse.check_stock(item.get_product_id(), item.get_quantity()):
                supply_order = self.create_supply_order(order.get_items())
                self.add_supply_order(supply_order)
        self._orders.append(order)

    def create_supply_order(self, items: List[OrderItem]) -> SupplyOrder:
        """Создает заказ поставщику."""
        supply_order_id = random.randint(1000, 9999)
        supply_order = SupplyOrder(supply_order_id, 1)
        for item in items:
            if not self._warehouse.check_stock(item.get_product_id(),item.get_quantity()):
                supply_order.add_item(SupplyOrderItem(item.get_product_id(), item.get_quantity()))
        return supply_order

    def add_supply_order(self, supply_order: SupplyOrder):
        """Добавляет заказ поставщику."""
        self._supply_orders.append(supply_order)

    def get_order_by_id(self, order_id: int) -> Order | None:
        """Возвращает заказ по id."""
        for order in self._orders:
            if order.get_id() == order_id:
              return order
        return None

    def get_orders(self) -> List[Order]:
        """Возвращает список заказов."""
        return self._orders

    def get_supply_orders(self) -> List[SupplyOrder]:
        """Возвращает список заказов поставщикам."""
        return self._supply_orders

    def update_order_status(self, order_id: int, status: OrderStatus):
        """Обновляет статус заказа."""
        order = self.get_order_by_id(order_id)
        if order:
             order.set_status(status)
             self.notify_observers(order)

    def update(self, order: Order):
       """Обрабатывает уведомления об изменении статуса заказа."""
       print(f"Статус заказа изменен на order ID: {order.get_id()} to {order.get_status()}")

    def __str__(self) -> str:
        """Возвращает строковое представление менеджера заказов."""
        return f"Заказы: {', '.join([str(order) for order in self._orders])}, Заказы на поставку: {', '.join([str(order) for order in self._supply_orders])}"

if __name__ == "__main__":
    from warehouse import Warehouse
    warehouse = Warehouse()
    order_manager = OrderManager(warehouse)
    print(order_manager)