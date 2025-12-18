from department import Department

class Organization:
    def __init__(self, name: str):
        self.name = name
        self.departments = []

    def add_department(self, department: Department):
        self.departments.append(department)
        print(f"Отдел {department.name} добавлен в организацию {self.name}.")

    def __str__(self):
        return f"Организация: {self.name}, Количество отделов: {len(self.departments)}"

    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as file:
            for department in self.departments:
                file.write(f"{department.name}\n")

    def load_from_file(self):
        try:
            with open(f"{self.name}.txt", "r") as file:
                for line in file:
                    department_name = line.strip()
                    department = Department(department_name)
                    self.add_department(department)
                    department.load_from_file()
        except FileNotFoundError:
            print(f"Файл для организации {self.name} не найден.")

if __name__ == "__main__":
    pass