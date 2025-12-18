from worker import Worker
# Класс для начальников участков


class SectionHead(Worker):
    def __init__(self, name: str, age: int, section: str):
        super().__init__(name, age, "Начальник участка")
        self._section = section

    @property
    def section(self):
        return self._section

    def manage_workers(self):
        print(f"{self.name} управляет рабочими на участке {self.section}.")

    def __str__(self):
        return f"Начальник участка(Name: {self.name}, Age: {self.age}, Section: {self.section})"


if __name__ == "__main__":
    section_head = SectionHead("Сергей", 45, "Участок 1")
    print(section_head)
    section_head.manage_workers()
