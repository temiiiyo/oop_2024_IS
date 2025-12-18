import pandas as pd


class Student:
    def __init__(self, first_name, last_name, group, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.specialty = specialty
        self.grade = None
        self.report_submitted = False

    def complete_assignment(self, assignment):
        print(f"{self.first_name} {self.last_name} completed the assignment: {assignment}")

    def submit_report(self):
        self.report_submitted = True
        print(f"{self.first_name} {self.last_name} submitted the report.")

class Curator:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def prepare_student_list(self, students):
        print(f"Curator {self.first_name} {self.last_name} prepared the student list.")
        return [student for student in students]

class PracticeLeader:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def assign_task(self, student, task):
        student.complete_assignment(task)

    def evaluate_student(self, student, grade):
        student.grade = grade
        print(f"{student.first_name} {student.last_name} received a grade: {grade}")

class DepartmentHead:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sign_documents(self, document):
        print(f"Department Head {self.first_name} {self.last_name} signed the document: {document}")

class PracticeDepartmentHead:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def send_letters(self, organizations):
        for org in organizations:
            print(f"Sent letter to {org}")

class Organization:
    def __init__(self, name):
        self.name = name
        self.confirmed_students = 0

    def send_confirmation(self, number_of_students):
        self.confirmed_students = number_of_students
        print(f"{self.name} confirmed {number_of_students} students.")


def main():
    students = [
        Student("Ivan", "Ivanov", "101", "Computer Science"),
        Student("Petr", "Petrov", "102", "Mathematics"),
        Student("Anna", "Sidorova", "101", "Physics")
    ]

    organizations = [
        Organization("Tech Corp"),
        Organization("Math Solutions"),
        Organization("Physics Institute")
    ]

    curator = Curator("Maria", "Smirnova")
    practice_leader = PracticeLeader("Dmitry", "Kuznetsov")

    student_list = curator.prepare_student_list(students)

    for student in students:
        practice_leader.assign_task(student, "Complete project report")
        practice_leader.evaluate_student(student, 5)

    organizations[0].send_confirmation(2)
    organizations[1].send_confirmation(1)

    data = {
        "First Name": [student.first_name for student in students],
        "Last Name": [student.last_name for student in students],
        "Group": [student.group for student in students],
        "Specialty": [student.specialty for student in students],
        "Grade": [student.grade for student in students]
    }

    df = pd.DataFrame(data)
    df.to_excel("students_report.xlsx", index=False)
    print("Данные о студентах успешно сохранены в файл 'students_report.xlsx'.")


if __name__ == "__main__":
    main()
