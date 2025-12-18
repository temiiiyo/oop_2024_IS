class OfficeAdministrator():
    def __init__(self, name):
        self.name = name

    def process_orders(self, orders):
        for order in orders:
            print(f"Администратор {self.name} обрабатывает заказ {order.order_id}.")

    def generate_report(self):
        print(f"Отчет сгенерирован администратором {self.name}.")