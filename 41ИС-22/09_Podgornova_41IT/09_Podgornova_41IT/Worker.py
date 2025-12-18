from Employee import Employee

class Worker(Employee):
    def __init__(self, name):
        super().__init__(name, "Рабочий")