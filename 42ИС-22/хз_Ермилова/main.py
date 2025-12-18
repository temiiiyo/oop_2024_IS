import os

class Teacher:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)

    def report(self):
        report_lines = [f"Отчет преподавателя: {self.name}\n"]
        for group in self.groups:
            report_lines.append(f"\nГруппа: {group.name}\n")
            for subject in group.subjects:
                report_lines.append(f"  Предмет: {subject.name}\n")
                for class_session in subject.classes:
                    info = f"    Занятие №{class_session.session_number}"
                    if class_session.date:
                        info += f", дата: {class_session.date}"
                    if class_session.time:
                        info += f", время: {class_session.time}"
                    if class_session.room:
                        info += f", аудитория: {class_session.room}"
                    report_lines.append(info + "\n")
        return "".join(report_lines)

class Group:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

class Subject:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_class(self, class_session):
        if class_session not in self.classes:
            self.classes.append(class_session)

class ClassSession:
    def __init__(self, session_number, date=None, time=None, room=None):
        self.session_number = session_number
        self.date = date
        self.time = time
        self.room = room

def validate_line(line):
    return isinstance(line, str) and len(line.strip()) > 0

def parse_input_line(line):
    line = line.strip()
    if not validate_line(line):
        return None, None
    if ':' in line:
        key, value = line.split(':', 1)
        return key.strip(), value.strip()
    elif ',' in line:
        parts = [part.strip() for part in line.split(',')]
        return parts
    else:
        return line

def read_input_files(filenames):
    teachers = []
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            continue
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if validate_line(line)]
        current_teacher = None
        current_group = None
        current_subject = None

        for line in lines:
            if 'Преподаватель' in line:
                key, value = parse_input_line(line)
                if value:
                    current_teacher = Teacher(value)
                    teachers.append(current_teacher)
            elif 'Группа' in line:
                key, value = parse_input_line(line)
                if value:
                    group = Group(value)
                    if current_teacher:
                        current_teacher.add_group(group)
                    current_group = group
            elif 'Предмет' in line:
                key, value = parse_input_line(line)
                if value:
                    subject = Subject(value)
                    if current_group:
                        current_group.add_subject(subject)
                    current_subject = subject
            elif 'Занятие' in line:
                # Ожидается формат: 'Занятие: №, дата, время, аудитория'
                key, value = parse_input_line(line)
                if isinstance(value, list) and len(value) >= 1:
                    session_number = value[0]
                    date = value[1] if len(value) > 1 else None
                    time = value[2] if len(value) > 2 else None
                    room = value[3] if len(value) > 3 else None
                    class_session = ClassSession(session_number, date, time, room)
                    if current_subject:
                        current_subject.add_class(class_session)
    return teachers

def generate_report_for_teachers(teachers):
    reports = []
    for teacher in teachers:
        reports.append(teacher.report())
    return "\n" + ("-" * 40 + "\n").join(reports)

def save_reports(reports, output_filenames):
    for report, filename in zip(reports, output_filenames):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Отчет сохранен: {filename}")

def main():
    input_files = ['input1.txt', 'input.txt']
    output_files = ['report.txt', 'report1.txt']
    teachers = read_input_files(input_files)
    reports = generate_report_for_teachers(teachers)
    save_reports([reports], output_files)

if __name__ == "__main__":
    main()