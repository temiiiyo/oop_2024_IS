from Employee import Employee

class SectionManager(Employee):
    def __init__(self, name):
        super().__init__(name, "Начальник участка")