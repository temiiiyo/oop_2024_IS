class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []
        self.student_count = 0

    def add_student(self, student_name):
        self.students.append(student_name)
        self.student_count += 1