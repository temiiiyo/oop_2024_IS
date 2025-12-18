from datetime import date

class Worker:
    def __init__(self, name, password, salary=0, dateon=date.today()):
        self.name = name
        self.password = password
        self.salary = salary
        self.dateon = dateon

    def get_up(self, percent=0.2):
        self.salary = percent * self.salary + self.salary

    def get_down(self, percent=0.2):
        self.salary = percent * self.salary - self.salary
    def __str__(self) -> str:
        return f"{self.name}, {self.password}"