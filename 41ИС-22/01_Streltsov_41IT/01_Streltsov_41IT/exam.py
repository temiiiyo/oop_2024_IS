class Exam:
    def __init__(self, subject, student, grade=None):
        self.subject = subject
        self.student = student
        self.grade = grade

    def conduct_exam(self):
        while True:
            try:
                self.grade = int(input(f"Введите оценку для студента {self.student.name} по предмету {self.subject.name}: "))
                break
            except ValueError:
                print("Пожалуйста, введите целое число для оценки.")
        print(f"Экзамен завершён. {self.student.name} получил {self.grade}")
        self.save_exam_data()

    def save_exam_data(self):
        with open(f"{self.subject.name}_exam_results.txt", "a", encoding="utf-8") as file:
            file.write(f"{self.student.name}: {self.grade}\n")