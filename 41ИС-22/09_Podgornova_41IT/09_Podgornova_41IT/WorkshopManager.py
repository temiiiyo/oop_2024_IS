from Employee import Employee

class WorkshopManager(Employee):
    def __init__(self, name):
        super().__init__(name, "Начальник цеха")