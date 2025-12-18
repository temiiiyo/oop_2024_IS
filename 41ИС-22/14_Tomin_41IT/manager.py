class WarrantyManager:
    def __init__(self, name):
        self.name = name

    def make_decision(self, product, analysis):
        if analysis["status"] == "faulty":
            return f"Продукт {product.name}: Решение - заменить."
        elif analysis["status"] == "repairable":
            repair_cost = product.price * 0.2  # примерная стоимость ремонта
            return f"Продукт {product.name}: Решение - отремонтировать. Стоимость ремонта: {repair_cost}."
        else:
            return f"Продукт {product.name}: Решение - вернуть клиенту."