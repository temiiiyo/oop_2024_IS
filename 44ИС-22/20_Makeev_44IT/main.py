"""Основной модуль для запуска."""
import datetime
import random
import sys
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

from product import Product
from order import Order
from order_item import OrderItem
from customer import Customer
from warehouse import Warehouse
from order_manager import OrderManager
from supply_manager import SupplyManager
from supplier import Supplier
from supply_order import SupplyOrder
from store_keeper import StoreKeeper
from delivery_queue import DeliveryQueue, DateDistanceSortStrategy, DistanceDateSortStrategy
from order_status import OrderStatus


def load_products_from_file(filename):
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, quantity = line.strip().split(',')
                products.append(Product(int(id), name, float(price), int(quantity)))
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return products

def load_customers_from_file(filename):
    customers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, name, address = line.strip().split(',')
                customers.append(Customer(int(id), name, address))
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return customers


def load_orders_from_file(filename, customers):
    orders = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                id, customerId, orderDate, distanceToWarehouse, product_ids_quantities = line.strip().split(',')
                order = Order(int(id), int(customerId), datetime.datetime.strptime(orderDate, '%Y-%m-%d %H:%M:%S'), int(distanceToWarehouse))

                pairs = product_ids_quantities.split(';')
                for pair in pairs:
                    product_id, quantity = pair.split(':')
                    order.add_item(OrderItem(int(product_id), int(quantity)))
                orders.append(order)
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
    return orders


def run_module_with_output(module_name, module_function, *args, **kwargs):
    """Запускает модуль, перенаправляя вывод в файл."""
    output_dir = "output"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    stdout_path = Path(output_dir) / f"{module_name}_stdout.txt"
    stderr_path = Path(output_dir) / f"{module_name}_stderr.txt"

    with open(stdout_path, "w", encoding="utf-8") as stdout_file, open(stderr_path, "w") as stderr_file:
        with redirect_stdout(stdout_file), redirect_stderr(stderr_file):
            module_function(*args, **kwargs)


if __name__ == "__main__":
    def main_logic():
        products = load_products_from_file('products.txt')
        customers = load_customers_from_file('customers.txt')
        orders = load_orders_from_file('orders.txt', customers)

        warehouse = Warehouse()
        for product in products:
            warehouse.add_product(product)

        order_manager = OrderManager(warehouse)
        for order in orders:
            order_manager.process_new_order(order)

        supply_manager = SupplyManager()
        supplier = Supplier(1, "Supplier 1")
        supply_manager.add_supplier(supplier)

        store_keeper = StoreKeeper(warehouse)

        delivery_queue = DeliveryQueue(DateDistanceSortStrategy())

        for supply_order in order_manager.get_supply_orders():
            supply_manager.create_order(supply_order)

        radius = 1000

        print("--- Orders in Progress ---")
        for order in order_manager.get_orders():
            if (order.get_status() != OrderStatus.DELIVERED and order.get_distance_to_warehouse() <= radius):
                delivery_queue.enqueue(order)
                print(f"Add to Queue: {order}, Queue: {delivery_queue}")
                # Отпуск товара со склада и смена статуса заказа
                for item in order.get_items():
                    if store_keeper.release_product(item.get_product_id(),item.get_quantity()):
                        order_manager.update_order_status(order.get_id(), OrderStatus.SHIPPED)
                    else:
                        print(f"Not enough product on warehouse: {item.get_product_id()}")

        print(f"Warehouse: {warehouse}")

        print("--- Process Orders ---")
        while not delivery_queue.is_empty():
            order = delivery_queue.dequeue()
            order_manager.update_order_status(order.get_id(), OrderStatus.DELIVERED)
            print(f"Delivered order: {order}")

        with open("orders_report.txt", "w") as f:
            for order in order_manager.get_orders():
                f.write(f"{order} \n")

        print("Report generate to orders_report.txt")

    run_module_with_output("main", main_logic)