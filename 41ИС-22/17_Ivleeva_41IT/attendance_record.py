from lesson import Lesson

class AttendanceRecord:
    def __init__(self, lesson, student, attended):
        self.lesson = lesson
        self.student = student
        self.attended = attended  # 1 - присутствовал, 0 - отсутствовал