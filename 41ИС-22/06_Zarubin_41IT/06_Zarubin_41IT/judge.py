from rating import Rating

class Judge:
    def __init__(self, name, section):
        self.name = name
        self.section = section

    def evaluate_performance(self, student, score):
        rating = Rating(student, self, score)
        return rating