from teacher import Teacher
from group import Group
from subject import Subject
from student import Student
from exam import Exam
from report import generate_excel_report

def main():
    teacher_name = input("Введите имя преподавателя: ")
    subject_name = input("Введите название предмета: ")
    teacher = Teacher(teacher_name, subject_name)

    group_name = input("Введите название группы: ")
    group = Group(group_name)

    subject = Subject(subject_name, teacher)

    while True:
        action = input(
            "\nВыберите действие:\n"
            "1. Добавить студента\n"
            "2. Удалить студента\n"
            "3. Провести экзамен для всех студентов\n"
            "4. Сформировать ведомость в Excel\n"
            "5. Выход\n"
            "Ваш выбор: "
        )

        if action == "1":
            student_name = input("Введите имя студента для добавления: ")
            new_student = Student(student_name, group)
            group.add_student(new_student)
        elif action == "2":
            student_name = input("Введите имя студента для удаления: ")
            student_to_remove = next((s for s in group.students if s.name == student_name), None)
            if student_to_remove:
                group.remove_student(student_to_remove)
            else:
                print(f"Студент {student_name} не найден.")
        elif action == "3":
            if not group.students:
                print("В группе нет студентов.")
            else:
                for student in group.students:
                    exam = Exam(subject, student)
                    exam.conduct_exam()
        elif action == "4":
            generate_excel_report(subject)
        elif action == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()