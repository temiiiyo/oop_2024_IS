from datetime import datetime, timedelta

class Product:
    def __init__(self, name, manufacturer, price, warranty_period_days):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.warranty_expiry = datetime.now() + timedelta(days=warranty_period_days)

    def is_under_warranty(self):
        return datetime.now() <= self.warranty_expiry