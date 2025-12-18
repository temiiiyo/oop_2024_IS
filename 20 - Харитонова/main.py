# Билет №20
# Классы:
# 1. Product – товар.
# 2. Order – заказ.
# 3. Customer – клиент.
# 4. Warehouse – склад.
# 5. Manager – менеджер.
# 6. Delivery – доставка.

"""Разработать программу для демонстрации онлайн-магазина. Программа должна выдавать в текстовый файл
список заказов в работе, то есть принятых, но еще не выполненных, от клиентов, находящихся в радиусе N км
от склада (N - параметр)."""

import json
from datetime import datetime


class Product:
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity


class Order:
    def __init__(self, order_id, customer, product, quantity, status='Принят'):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.status = status  # Статус заказа (Принят, Выполнен и т.д.)


class Customer:
    def __init__(self, customer_id, name, address, distance_from_warehouse):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.distance_from_warehouse = distance_from_warehouse  # Расстояние до склада


class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        self.inventory[product] = self.inventory.get(product, 0) + quantity

    def check_stock(self, product, quantity):
        return self.inventory.get(product, 0) >= quantity


class Manager:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.orders = []

    def create_order(self, order_id, customer, product, quantity, status='Принят'):
        if self.warehouse.check_stock(product, quantity):
            order = Order(order_id, customer, product, quantity, status)
            self.orders.append(order)
            print(f"Заказ {order_id} принят от клиента {customer.name}. Статус: {status}.")
            return order
        else:
            print(f"Недостаточно товара {product.name} на складе.")
            return None

    def get_orders_in_progress(self, max_distance):
        return [order for order in self.orders if
                order.customer.distance_from_warehouse <= max_distance and order.status == 'Принят']


class Delivery:
    def deliver_order(self, order):
        print(f"Доставка заказа {order.order_id} клиенту {order.customer.name}")


def save_orders_to_file(orders, filename="orders_in_progress.txt"):
    """
    Сохраняет список заказов в текстовый файл
    """
    with open(filename, 'w', encoding='utf-8') as file:
        # Заголовок отчета
        file.write("=" * 60 + "\n")
        file.write("ОТЧЕТ О ЗАКАЗАХ В РАБОТЕ\n")
        file.write(f"Дата генерации: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
        file.write("=" * 60 + "\n\n")

        if not orders:
            file.write("Нет заказов в работе в указанном радиусе.\n")
        else:
            file.write(f"Найдено заказов: {len(orders)}\n\n")

            for i, order in enumerate(orders, 1):
                file.write(f"ЗАКАЗ #{i}\n")
                file.write(f"  ID заказа: {order.order_id}\n")
                file.write(f"  Клиент: {order.customer.name}\n")
                file.write(f"  Адрес: {order.customer.address}\n")
                file.write(f"  Расстояние от склада: {order.customer.distance_from_warehouse} км\n")
                file.write(f"  Товар: {order.product.name}\n")
                file.write(f"  Количество: {order.quantity}\n")
                file.write(f"  Статус: {order.status}\n")
                file.write("-" * 40 + "\n")


if __name__ == "__main__":
    # Создаем склад и менеджера
    warehouse = Warehouse()
    manager = Manager(warehouse)

    # Добавляем продукты на склад
    product1 = Product(1, "Laptop", 10)
    product2 = Product(2, "Smartphone", 5)
    product3 = Product(3, "Tablet", 20)
    product4 = Product(4, "Headphones", 15)
    product5 = Product(5, "Monitor", 8)

    warehouse.add_product(product1, 10)
    warehouse.add_product(product2, 5)
    warehouse.add_product(product3, 20)
    warehouse.add_product(product4, 15)
    warehouse.add_product(product5, 8)

    # Создаем клиентов
    customer1 = Customer(1, "Amina", "Portovo 5", 5)
    customer2 = Customer(2, "Alena", "Mitishi 9", 15)
    customer3 = Customer(3, "Ivan", "Moscow 12", 10)
    customer4 = Customer(4, "Olga", "Krasnodar 1", 25)
    customer5 = Customer(5, "Dmitry", "Sochi 3", 7)

    # Создаем заказы с разными статусами
    manager.create_order(1, customer1, product1, 1, 'Принят')
    manager.create_order(2, customer2, product2, 1, 'Выполнен')
    manager.create_order(3, customer3, product3, 2, 'Отменен')
    manager.create_order(4, customer4, product4, 1, 'Принят')
    manager.create_order(5, customer5, product5, 1, 'Выполнен')

    # Запрашиваем радиус у пользователя
    max_distance = float(input("Введите радиус (в км), в пределах которого нужно получить заказы: "))

    # Получаем заказы в работе в радиусе N км от склада
    orders_in_progress = manager.get_orders_in_progress(max_distance=max_distance)

    # Выводим результат в консоль
    print(f"\nНайдено заказов в работе в радиусе {max_distance} км: {len(orders_in_progress)}")

    if orders_in_progress:
        print("\nСписок заказов в работе:")
        for order in orders_in_progress:
            print(f"  Заказ #{order.order_id}: {order.customer.name} - {order.product.name}")

    # Сохраняем в текстовый файл
    save_orders_to_file(orders_in_progress)
    print(f"\nОтчет сохранен в файл 'orders_in_progress.txt'")