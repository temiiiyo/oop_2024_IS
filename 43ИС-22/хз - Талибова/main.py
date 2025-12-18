# main.py
from teacher import Teacher
from group import Group
from subject import Subject
from lesson import Lesson
from journal import Journal

def main():
    teacher_name = input("Введите имя преподавателя: ")
    group_name = input("Введите название группы: ")
    subject_name = input("Введите название дисциплины: ")

    # Сохраняем данные преподавателя, группы и дисциплины
    teacher = Teacher(teacher_name)
    teacher.save_to_file()

    group = Group(group_name)
    group.save_to_file()

    subject = Subject(subject_name, teacher_name)
    subject.save_to_file()

    # Создаем или загружаем урок с данными из файла
    lesson = create_lesson(subject_name, group_name)
    lesson.save_to_file()  # Сохраняем урок в файл

    print("Данные сохранены!")

    # Запрос на экспорт отчета
    export = input("Хотите экспортировать отчет в Excel? (да/нет): ").strip().lower()

    if export == 'да':
        teacher_name_for_report = input("Введите имя преподавателя для отчета: ")
        excel_file = f"Отчет_{teacher_name_for_report.replace(' ', '_')}.xlsx"
        journal = Journal()
        try:
            journal.export_to_excel(teacher_name_for_report, excel_file)
            print(f"Отчет экспортирован в файл: {excel_file}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
    else:
        print("Отчет не был экспортирован.")


def create_lesson(subject_name, group_name):
    """
    Создает урок из данных в файле или возвращает новый урок, если не найден.
    """
    lesson = Lesson()  # Создаем экземпляр Lesson для работы с уроками
    lessons = lesson.load_all()  # Получаем все уроки из файла

    # Ищем урок, который соответствует дисциплине и группе
    for l in lessons:
        if l.subject_name == subject_name and l.group_name == group_name:
            return l  # Если нашли, возвращаем этот урок

    # Если урок не найден, создаем новый с дефолтными значениями
    print(f"Не найден урок для дисциплины {subject_name} в группе {group_name}, создаем новый урок.")
    return Lesson("2024-12-24", subject_name, group_name, 15)  # Создаем новый урок с дефолтными значениями


if __name__ == "__main__":
    main()