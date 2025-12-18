from workers.worker import Worker
from datetime import date

class Boss(Worker):
    def __init__(self, name, password, otdel, salary=0, dateon=date.today()):
        super().__init__(name, password, salary, dateon)
        self.otdel = otdel

    def transfer(self, new_otdel):
        self.otdel = new_otdel

    def get_up(self):
        self.salary *= 5