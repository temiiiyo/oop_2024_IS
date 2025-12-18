# класс для работников
"""инициализация класса"""
class Worker:
    total_workers = 0

    def __init__(self, name: str, age: int, position: str):
        self._name = name
        self._age = age
        self._position = position
        Worker.total_workers += 1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def position(self):
        return self._position


    def work(self):
        print(f"{self.name} работает на должности {self.position}.")

    def __str__(self):
        return f"Worker(Name: {self.name}, Age: {self.age}, Position: {self.position})"

    def __add__(self, other):
        if isinstance(other, int):
            return Worker(self.name, self.age + other, self.position)
        return NotImplemented

    def __eq__(self, other):
        return isinstance(other, Worker) and self.name == other.name

    def __len__(self):
        return len(self.name)

    @classmethod
    def get_total_workers(cls):
        return cls.total_workers

"""запуск работы программы"""
if __name__ == "__main__":
    worker = Worker("Иван", 30, "Рабочий")
    print(worker.__add__(5))
    worker.work()
    print(worker.get_total_workers())
