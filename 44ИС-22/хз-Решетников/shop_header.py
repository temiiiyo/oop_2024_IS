from worker import Worker

# Класс для начальников цехов.
class ShopHead(Worker):
    def __init__(self, name: str, age: int, shop: str):

        super().__init__(name, age, "Начальник цеха")
        self._shop = shop

    @property
    def shop(self):
        return self._shop

    def coordinate_sections(self):
        print(f"{self.name} координирует участки в цехе {self.shop}.")

    def __str__(self):
        return f"ShopHead(Name: {self.name}, Age: {self.age}, Shop: {self.shop})"


if __name__ == "__main__":
    shop_head = ShopHead("Александр", 50, "Цех 1")
    print(shop_head)
    shop_head.coordinate_sections()