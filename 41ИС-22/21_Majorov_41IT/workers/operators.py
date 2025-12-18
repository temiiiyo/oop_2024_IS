from workers.worker import Worker
from datetime import date

class Operator(Worker):
    def __init__(self, name, password, mashine, salary=0, dateon=date.today()):
        super().__init__(name, password, salary, dateon)
        self.mashine = mashine

    def get_work_period(self):
        return date.today() - self.dateon