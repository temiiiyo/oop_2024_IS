class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def get_info(self):
        print(f"Дисциплина: {self.name}, преподаватель: {self.teacher.name}")