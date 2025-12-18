class Rating:
    def __init__(self, student, judge, score):
        self.student = student
        self.judge = judge
        self.score = score

    def __str__(self):
        return f"{self.judge.name} оценил {self.student.name} на {self.score}"