class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Студент {student.name} добавлен в группу {self.group_name}")
        self.save_group_data()

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удалён из группы {self.group_name}")
            self.save_group_data()
        else:
            print(f"Студент {student.name} не найден в группе {self.group_name}")

    def save_group_data(self):
        with open(f"{self.group_name}_students.txt", "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(student.name + "\n")