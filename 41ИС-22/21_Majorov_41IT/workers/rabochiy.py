from workers.worker import Worker
from datetime import date


class Rabochiy(Worker):
    def get_work_period(self):
        return date.today() - self.dateon