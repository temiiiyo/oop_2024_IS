from employee import Employee

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Работник {employee.name} добавлен в отдел {self.name}.")

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)
        print(f"Работник {employee.name} удален из отдела {self.name}.")

    def get_employee_count(self):
        return len(self.employees)

    def __lt__(self, other):
        return self.get_employee_count() < other.get_employee_count()

    def __str__(self):
        return f"Отдел: {self.name}, Количество работников: {self.get_employee_count()}"

    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as file:
            for employee in self.employees:
                file.write(f"{employee}\n")

    def load_from_file(self):
        try:
            with open(f"{self.name}.txt", "r") as file:
                for line in file:
                    name, position = line.strip().split(", ")
                    self.add_employee(Employee(name, position))
        except FileNotFoundError:
            print(f"Файл для отдела {self.name} не найден.")

if __name__ == "__main__":
    pass