class Customer():
    def __init__(self, name, contact_details):
        self.name = name
        self.contact_details = contact_details

    @classmethod
    def place_order(cls, order):
        print(f"{cls.name} разместил заказ {order.order_id}.")