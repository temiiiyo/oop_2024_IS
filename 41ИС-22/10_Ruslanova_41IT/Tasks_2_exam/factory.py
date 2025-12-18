class Factory:
    """Класс для завода."""
    def __init__(self, name):
        self.name = name
        self.shops = []

    def add_shop(self, shop):
        self.shops.append(shop)

    def __str__(self):
        return f"Завод: {self.name}, количество цехов: {len(self.shops)}"