# delivery_queue.py
"""Модуль с классом DeliveryQueue и стратегиями сортировки."""
from typing import List
import datetime
from order import Order


class SortStrategy:
    """Интерфейс для стратегий сортировки."""

    def sort(self, orders: List[Order]):
        """Сортирует список заказов."""
        raise NotImplementedError


class DateDistanceSortStrategy(SortStrategy):
    """Стратегия сортировки по дате и расстоянию."""

    def sort(self, orders: List[Order]):
        """Сортирует заказы по дате и расстоянию."""
        orders.sort(key=lambda order: (order.get_order_date(), order.get_distance_to_warehouse()))


class DistanceDateSortStrategy(SortStrategy):
    """Стратегия сортировки по расстоянию и дате."""

    def sort(self, orders: List[Order]):
        """Сортирует заказы по расстоянию и дате."""
        orders.sort(key=lambda order: (order.get_distance_to_warehouse(), order.get_order_date()))


class DeliveryQueue:
    """Представляет очередь доставки."""

    def __init__(self, sort_strategy: SortStrategy):
        """Инициализирует очередь доставки с заданной стратегией сортировки."""
        self._queue = []
        self._sort_strategy = sort_strategy

    def enqueue(self, order: Order):
        """Добавляет заказ в очередь."""
        self._queue.append(order)
        self._sort_strategy.sort(self._queue)

    def dequeue(self) -> Order | None:
        """Извлекает заказ из очереди."""
        if not self.is_empty():
            return self._queue.pop(0)
        return None

    def peek(self) -> Order | None:
        """Возвращает следующий заказ в очереди без удаления."""
        if not self.is_empty():
            return self._queue[0]
        return None

    def get_queue(self) -> List[Order]:
        """Возвращает очередь."""
        return self._queue

    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь."""
        return len(self._queue) == 0

    def __str__(self) -> str:
        """Возвращает строковое представление очереди доставки."""
        return f"Queue: {', '.join([str(order) for order in self._queue])}"


def load_orders_from_file(filename):
    """Загружает заказы из файла."""
    orders = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, customerId, orderDate, distanceToWarehouse = line.strip().split(',')
                order = Order(int(id), int(customerId), datetime.datetime.strptime(orderDate, '%Y-%m-%d %H:%M:%S'), int(distanceToWarehouse))
                orders.append(order)
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return orders


if __name__ == "__main__":
    strategy = DateDistanceSortStrategy()
    delivery_queue = DeliveryQueue(strategy)

    orders = load_orders_from_file('orders.txt')
    for order in orders:
        delivery_queue.enqueue(order)

    strategy_dist_date = DistanceDateSortStrategy()
    delivery_queue_dist = DeliveryQueue(strategy_dist_date)
    for order in orders:
        delivery_queue_dist.enqueue(order)