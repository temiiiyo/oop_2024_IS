class Subject:
    FILE_NAME = "subjects.txt"

    def __init__(self, name, teacher_name):
        self.name = name
        self.teacher_name = teacher_name

    def save_to_file(self):
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{self.name},{self.teacher_name}\n")


    def load_all(self):
        with open(Subject.FILE_NAME, "r") as file:
            return [line.strip().split(",") for line in file]

    def describe(self):
        print(f"Дисциплина: {self.name}, Преподаватель: {self.teacher_name}")