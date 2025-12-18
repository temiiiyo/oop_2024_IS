from article import Article
from data_load import load_conference_data


class Conference:
    def __init__(self):
        self.sections = []
        self.students = []
        self.judges = []

    def add_section(self, section):
        self.sections.append(section)

    def add_student(self, student):
        self.students.append(student)

    def add_judge(self, judge):
        self.judges.append(judge)

    def generate_report(self):
        report = "Распределение выступающих по отделениям:\n"
        for section in self.sections:
            report += f"Секция: {section.title}\n"
            for student in section.students:
                report += f" - {student.name}\n"
                for article in student.articles:
                    report += f"   - Поданная статья: {article.title}\n"
        return report

    def save_report_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.generate_report())


if __name__ == "__main__":
    conference = Conference()
    sections, students, judges = load_conference_data("fail.txt")

    for section in sections:
        conference.add_section(section)
    for student in students:
        conference.add_student(student)
    for judge in judges:
        conference.add_judge(judge)

    article1 = Article("Исследование в области ИТ", "Содержание статьи 1.")
    article2 = Article("Разработка нового приложения", "Содержание статьи 2.")
    article4 = Article("Разработка нового приложения", "Содержание статьи 2.")
    students[0].submit_article(article1)
    students[1].submit_article(article2)
    students[3].submit_article(article4)
    for section in conference.sections:
        section.evaluate()
    report = conference.generate_report()
    print(report)
    conference.save_report_to_file("report.txt")