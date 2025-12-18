class Division:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def __len__(self):
        return len(self.employees)

    def __str__(self):
        return f"{self.name} (Количество сотрудников: {len(self)})"

    def compare_size(self, other):
        if len(self) > len(other):
            return f"{self.name} больше, чем {other.name}"
        elif len(self) < len(other):
            return f"{self.name} меньше, чем {other.name}"
        else:
            return f"{self.name} и {other.name} имеют одинаковое количество сотрудников"