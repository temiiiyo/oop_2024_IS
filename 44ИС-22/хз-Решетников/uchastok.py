# Класс для участков
class Section:
    def __init__(self, name: str):
        self._name = name
        self._employees = []  # Список рабочих

    @property
    def name(self):
        return self._name

    def add_laborer(self, laborer):
        self._employees.append(laborer)
        print(f"{laborer.name} добавлен в участок {self.name}.")

    def __str__(self):
        return f"Section(Name: {self.name}, Employees: {len(self._employees)})"


if __name__ == "__main__":
    section = Section("Участок 1")
    print(section)
