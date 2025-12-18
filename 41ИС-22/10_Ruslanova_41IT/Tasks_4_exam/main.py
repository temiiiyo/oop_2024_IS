class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"


class ProductCatalog:
    def __init__(self):
        self.products = [
            Product("Смартфон", 20000),
            Product("Ноутбук", 50000),
            Product("Наушники", 3000),
        ]

    def list_products(self):
        print("Список доступных товаров:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")

    def get_product(self, index):
        if 0 <= index < len(self.products):
            return self.products[index]
        else:
            print("Неверный индекс товара")
            return None


#Класс фасада
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} добавлен в корзину")

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} удален из корзины")
                return
        print(f"{product_name} нет в корзине")

    def list_items(self):
        if not self.items:
            print("Корзина пуста")
        else:
            print("Текущие товары в корзине:")
            for item in self.items:
                print(f"- {item}")

    def calculate_total(self):
        return sum(item.price for item in self.items)


class PaymentSystem:
    def process_payment(self, amount):
        print(f"Оплата на сумму {amount} успешно выполнена")


class NotificationSystem:
    def send_notification(self, message):
        print(f"Уведомление: {message}")



class ECommerceFacade:
    def __init__(self):
        self.catalog = ProductCatalog()
        self.cart = ShoppingCart()
        self.payment = PaymentSystem()
        self.notifications = NotificationSystem()

    def browse_products(self):
        self.catalog.list_products()

    def add_to_cart(self, product_index):
        product = self.catalog.get_product(product_index - 1)
        if product:
            self.cart.add_item(product)

    def remove_from_cart(self, product_name):
        self.cart.remove_item(product_name)

    def view_cart(self):
        self.cart.list_items()

    def checkout(self):
        total_amount = self.cart.calculate_total()
        if total_amount > 0:
            self.payment.process_payment(total_amount)
            self.notifications.send_notification("Ваш заказ успешно оформлен!")
            print("Заказ успешно оформлен!")
        else:
            print("Корзина пуста. Заказ не может быть оформлен.")


if __name__ == "__main__":
    store = ECommerceFacade()

    while True:
        print("\nДобро пожаловать!")
        print("1. Просмотреть товары")
        print("2. Добавить товар в корзину")
        print("3. Удалить товар из корзины")
        print("4. Просмотреть корзину")
        print("5. Оформить заказ")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            store.browse_products()
        elif choice == "2":
            product_index = int(input("Введите номер товара для добавления: "))
            store.add_to_cart(product_index)
        elif choice == "3":
            product_name = input("Введите название товара для удаления: ")
            store.remove_from_cart(product_name)
        elif choice == "4":
            store.view_cart()
        elif choice == "5":
            store.checkout()
        elif choice == "6":
            break


