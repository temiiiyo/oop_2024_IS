from datetime import datetime
from typing import Dict, List

# ==================================================
#              СТРАТЕГИИ ДОСТАВКИ
# ==================================================

class DeliveryStrategy:
    """Базовый класс стратегии доставки"""

    def calculate_pr(self, order):
        raise NotImplementedError("Метод должен быть реализован в подклассах")


class DatePrStrategy(DeliveryStrategy):
    """Приоритет по дате заказа"""

    def calculate_pr(self, order):
        return order.order_date


class DistancePrStrategy(DeliveryStrategy):
    """Приоритет по расстоянию"""

    def calculate_pr(self, order):
        return order.distance


# ==================================================
#                    ТОВАР
# ==================================================

class Product:
    """Класс товара"""

    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count

    def __str__(self):
        return f"{self.name} (Количество: {self.count})"


# ==================================================
#                    ЗАКАЗ
# ==================================================

class Order:
    """Класс заказа"""

    def __init__(
        self,
        customer_name: str,
        product_name: str,
        count: int,
        distance: float,
        order_date: datetime
    ):
        self.customer_name = customer_name
        self.product_name = product_name
        self.count = count
        self.distance = distance
        self.order_date = order_date
        self.status = "На ожидании"

    def __str__(self):
        return (
            f"Заказ: {self.product_name} | Клиент: {self.customer_name} | "
            f"Кол-во: {self.count} | Расстояние: {self.distance} км | "
            f"Статус: {self.status}"
        )


# ==================================================
#                    СКЛАД
# ==================================================

class Sklad:
    """Класс склада"""

    def __init__(self):
        self.inventory: Dict[str, int] = {}

    def add_product(self, product: Product):
        """Добавление товара на склад"""
        self.inventory[product.name] = self.inventory.get(product.name, 0) + product.count

    def get_product(self, product_name: str, count: int) -> bool:
        """Получение товара со склада"""
        if self.inventory.get(product_name, 0) >= count:
            self.inventory[product_name] -= count
            return True
        return False

    def __str__(self):
        return "Инвентарь склада:\n" + "\n".join(
            f"{name}: {qty}" for name, qty in self.inventory.items()
        )


# ==================================================
#                    МЕНЕДЖЕР
# ==================================================

class Manager:
    """Менеджер заказов"""

    def __init__(self, sklad: Sklad):
        self.sklad = sklad
        self.orders: List[Order] = []
        self.delivery_strategy: DeliveryStrategy = DatePrStrategy()

    def set_delivery_strategy(self, strategy: DeliveryStrategy):
        """Установка стратегии приоритета доставки"""
        self.delivery_strategy = strategy

    def set_order(self, order: Order):
        """Обработка нового заказа"""
        if self.sklad.get_product(order.product_name, order.count):
            order.status = "Готов к доставке"
        else:
            order.status = "Ожидание пополнения"
        self.orders.append(order)

    def waiting(self, product: Product):
        """Пополнение склада и обработка ожидающих заказов"""
        self.sklad.add_product(product)

        for order in self.orders:
            if order.status == "Ожидание пополнения" and order.product_name == product.name:
                if self.sklad.get_product(order.product_name, order.count):
                    order.status = "Готов к доставке"

    def get_orders_radius(self, radius: float) -> List[Order]:
        """Получение заказов в заданном радиусе"""
        filtered_orders = [
            order for order in self.orders
            if order.status != "Доставлен" and order.distance <= radius
        ]
        return sorted(filtered_orders, key=self.delivery_strategy.calculate_pr)


# ==================================================
#                    ДОСТАВКА
# ==================================================

class Delivery:
    """Класс доставки"""

    def deliver_order(self, order: Order):
        if order.status == "Готов к доставке":
            order.status = "Доставлен"
            print(f"✔ Доставлен заказ: {order}")
        else:
            print(f"✖ Невозможно доставить заказ: {order}")


# ==================================================
#              ЗАГРУЗКА ДАННЫХ ИЗ ФАЙЛОВ
# ==================================================

def load_products(filename: str, sklad: Sklad):
    """Загрузка товаров на склад из файла"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, count = line.strip().split(",")
            sklad.add_product(Product(name, int(count)))


def load_orders(filename: str) -> List[Order]:
    """Загрузка заказов из файла"""
    orders = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            customer_name, product_name, count, distance, order_date = line.strip().split(",")
            orders.append(
                Order(
                    customer_name,
                    product_name,
                    int(count),
                    float(distance),
                    datetime.strptime(order_date, "%Y-%m-%d")
                )
            )
    return orders


# ==================================================
#                 ТОЧКА ВХОДА
# ==================================================

if __name__ == "__main__":

    sklad = Sklad()
    manager = Manager(sklad)
    delivery = Delivery()

    # --- Загрузка данных ---
    load_products("products.txt", sklad)
    orders = load_orders("orders.txt")

    for order in orders:
        manager.set_order(order)

    # --- Пополнение склада ---
    manager.waiting(Product("Планшет", 7))

    # --- Установка стратегии доставки ---
    manager.set_delivery_strategy(DistancePrStrategy())

    # --- Заказы в радиусе ---
    radius = 20
    priority_orders = manager.get_orders_radius(radius)

    with open("p_orders.txt", "w", encoding="utf-8") as file:
        file.write(f"Заказы в радиусе {radius} км:\n")
        for order in priority_orders:
            file.write(str(order) + "\n")

    # --- Выполнение доставки ---
    for order in manager.orders:
        delivery.deliver_order(order)
