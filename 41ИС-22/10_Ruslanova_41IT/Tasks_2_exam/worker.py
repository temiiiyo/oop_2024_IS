class Worker:
    """Базовый класс для всех работников."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} выполняет работу."

    def __str__(self):
        return f"Работник: {self.name}, возраст: {self.age}"


class Turner(Worker):
    def work(self):
        return f"{self.name} точит детали на станке."


class Locksmith(Worker):
    def work(self):
        return f"{self.name} чинит оборудование."


class Miller(Worker):
    def work(self):
        return f"{self.name} фрезерует детали."