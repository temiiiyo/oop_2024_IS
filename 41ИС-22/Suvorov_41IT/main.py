'''
Суворов Дангиил Сергеевич
Билет №2
'''
from student import Student
file_path = 'students.txt'
class Exam():
    def read_f(self, file_path):
        students = []
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:
                    student_id = int(data[0].strip())
                    name = data[1].strip()
                    rating = float(data[2].strip())
                    mark = float(data[3].strip())
                    student = Student(student_id, name, rating, mark)
                    students.append(student)
        return students


    def sort_s(self, students):
        for i in range(len(students)):
            for j in range(0, len(students)-i-1):
                if students[j].rating < students[j+1].rating:
                    students[j], students[j+1] = students[j+1], students[j]

    def print_all(self):
        students = Exam().read_f(file_path)
        Exam().sort_s(students)
        for student in students:
            print(student)

Exam().print_all()