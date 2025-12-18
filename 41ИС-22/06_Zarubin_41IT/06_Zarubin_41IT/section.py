import random
class Section:
    def __init__(self, title):
        self.title = title
        self.students = []
        self.judges = []
        self.ratings = []

    def add_student(self, student):
        self.students.append(student)

    def add_judge(self, judge):
        self.judges.append(judge)

    def evaluate(self):
        for judge in self.judges:
            for student in self.students:
                score = self.get_score_from_judge(judge, student)
                rating = judge.evaluate_performance(student, score)
                self.ratings.append(rating)

    def get_score_from_judge(self, judge, student):
        return random.randint(1, 10)

    def get_student_list(self):
        return [student.name for student in self.students]