# lesson.py
class Lesson:
    FILE_NAME = "lessons.txt"

    def __init__(self, date=None, subject_name=None, group_name=None, attendance=None):
        self.date = date
        self.subject_name = subject_name
        self.group_name = group_name
        self.attendance = attendance

    def save_to_file(self):
        with open(self.FILE_NAME, "a", encoding='utf-8') as file:
            file.write(f"{self.date},{self.subject_name},{self.group_name},{self.attendance}\n")

    def load_all(self):
        lessons = []
        with open(self.FILE_NAME, "r", encoding='utf-8') as file:
            for line in file:
                date, subject_name, group_name, attendance = line.strip().split(",")
                lessons.append(Lesson(date, subject_name, group_name, int(attendance)))  # Создаем объекты Lesson
        return lessons

    def describe(self):
        print(f"Занятие: {self.date}, Дисциплина: {self.subject_name}, Группа: {self.group_name}, Посещаемость: {self.attendance}")