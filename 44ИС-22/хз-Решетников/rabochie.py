from worker import Worker
# Класс для рабочих


class Laborer(Worker):
    def __init__(self, name: str, age: int, position: str, grade: int):
        super().__init__(name, age, position)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    def perform_task(self):
        print(f"{self.name} (разряд {self.grade}) выполняет задачу.")

    def __str__(self):
        return f"Laborer(Name: {self.name}, Age: {self.age}, Position: {self.position}, Grade: {self.grade})"


if __name__ == "__main__":
    laborer = Laborer("Петр", 28, "Рабочий", 5)
    print(laborer)
    laborer.perform_task()
