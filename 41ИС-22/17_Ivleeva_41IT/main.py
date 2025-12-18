from teacher import Teacher
from group import Group
from subject import Subject
from lesson import Lesson
from attendance_record import AttendanceRecord


def save_to_file(records):
    with open("file.txt", "w", encoding="utf-8") as file:
        for record in records:
            file.write(f"{record.lesson.subject.name}, {record.lesson.date}, {record.student}, {record.attended}\n")


def main():
    teacher = Teacher("Leonid", "OOOP")
    group = Group("Group A")
    subject = Subject("OOOP")

    lesson = Lesson(subject, "2025-12-18", "1 час")

    records = []
    records.append(AttendanceRecord(lesson, "Student 1", 1))

    save_to_file(records)

    print("Данные о посещаемости сохранены в файл 'file.txt'.")
    print(f"Преподаватель: {teacher.name}, Предмет: {teacher.subject}")
    print(
        f"Группа: {group.group_name}, Дата урока: {lesson.date}, Студент: {records[0].student}, Присутствовал: {'Да' if records[0].attended else 'Нет'}")


if __name__ == "__main__":
    main()