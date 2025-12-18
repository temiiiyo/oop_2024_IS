from student import Student


class PracticeManager:
    def __init__(self):
        """Инициализация менеджера практики с пустым списком студентов."""
        self.students = []

    def add_student(self, student):
        """Добавляет студента в список."""
        self.students.append(student)

    def load_students_from_file(self, filename):
        """Загружает студентов из текстового файла."""
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                name, group, specialty = line.strip().split(',')
                student = Student(name, group, specialty)
                self.add_student(student)

    def generate_report(self):
        """Генерирует отчет о студентах."""
        if not self.students:
            print("Нет студентов для отображения.")
            return

        report_lines = ["Отчет о студентах:"]
        for student in self.students:
            report_lines.append(str(student))

        return "\n".join(report_lines)

    def save_report_to_file(self, filename):
        """Сохраняет отчет о студентах в текстовый файл."""
        report = self.generate_report()
        if report:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(report)
            print(f"Отчет сохранен в файл: {filename}")


if __name__ == "__main__":
    # Пример использования PracticeManager
    manager = PracticeManager()
    manager.load_students_from_file("students.txt")
    print(manager.generate_report())