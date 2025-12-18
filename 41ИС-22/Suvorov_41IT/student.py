class Student:
    def __init__(self, student_id, name, rating, mark):
        self.id = student_id
        self.name = name
        self.rating = rating
        self.mark = mark

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_mark(self):
        return self.mark

    def __str__(self):
        return f"ID: {self.id}, Имя: {self.name}, Рейтинг: {self.rating}, Марка: {self.mark}"