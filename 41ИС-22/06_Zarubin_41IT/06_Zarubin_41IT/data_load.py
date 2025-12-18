from judge import Judge
from section import Section
from students import Student


def load_conference_data(filename):
    sections = []
    students = []
    judges = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        current_section = None

        for line in lines:
            line = line.strip()
            if line.startswith("Секция:"):
                section_title = line.split(":")[1].strip()
                current_section = Section(section_title)
                sections.append(current_section)
            elif line.startswith("Студент:"):
                student_data = line.split(":")[1].strip().split(",")
                student = Student(student_data[0].strip(), student_data[1].strip())
                students.append(student)
                if current_section:
                    student.apply(current_section)
            elif line.startswith("Судья:"):
                judge_name = line.split(":")[1].strip()
                judge = Judge(judge_name, current_section)
                judges.append(judge)
                if current_section:
                    current_section.add_judge(judge)

    return sections, students, judges