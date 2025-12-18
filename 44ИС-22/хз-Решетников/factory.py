# Класс завода
class Factory:
    def __init__(self, name: str):
        self._name = name
        self._employees = []  # Список сотрудников
        self._shops = []      # Список цехов

    @property
    def name(self):
        return self._name

    def add_employee(self, employee):
        self._employees.append(employee)
        print(f"{employee.name} добавлен в завод {self.name}.")

    def add_shop(self, shop):
        self._shops.append(shop)
        print(f"Цех {shop.name} добавлен в завод {self.name}.")

    def __str__(self):
        return f"Factory(Name: {self.name}, Employees: {len(self._employees)}, Shops: {len(self._shops)})"


if __name__ == "__main__":
    factory = Factory("Завод №1")
    print(factory)