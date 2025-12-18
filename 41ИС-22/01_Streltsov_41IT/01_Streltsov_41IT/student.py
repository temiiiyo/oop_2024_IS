class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def take_exam(self):
        print(f"Студент {self.name} сдаёт экзамен")