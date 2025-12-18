class Dispatcher():
    def __init__(self, name):
        self.name = name

    def assign_delivery(self, order):
        print(f"Экспедитор {self.name} назначил доставку для заказа {order.order_id}.")