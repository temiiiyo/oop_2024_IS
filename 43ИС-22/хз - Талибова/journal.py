import openpyxl
from openpyxl.styles import Font
from subject import Subject
from lesson import Lesson


class Journal:
    def __init__(self):
        pass

    def export_to_excel(self, teacher_name, file_name):
        # Загружаем все уроки
        lessons = Lesson.load_all()

        # Фильтруем уроки по преподавателю
        filtered_lessons = [lesson for lesson in lessons if lesson[1] in self.get_subjects_by_teacher(teacher_name)]

        if not filtered_lessons:
            raise ValueError("Нет данных для отчета!")


        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = f"Отчет - {teacher_name}"


        worksheet.append(["Дата", "Дисциплина", "Группа", "Посещаемость"])

        # Делаем заголовки жирными
        for cell in worksheet["1:1"]:
            cell.font = Font(bold=True)

        # Заполнение данных уроками
        for lesson in filtered_lessons:
            worksheet.append(lesson)

        # Сохраняем файл
        workbook.save(file_name)

    def get_subjects_by_teacher(self, teacher_name):
        subjects = Subject.load_all()
        return [subject[0] for subject in subjects if subject[1] == teacher_name]