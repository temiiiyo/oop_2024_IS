from worker import Worker

class ShopChief(Worker):
    def __init__(self, name, age, shop_name):
        super().__init__(name, age)
        self.shop_name = shop_name

    def manage(self):
        return f"{self.name} управляет цехом {self.shop_name}."

    def __str__(self):
        return f"Начальник цеха: {self.name}, возраст: {self.age}, цех: {self.shop_name}"