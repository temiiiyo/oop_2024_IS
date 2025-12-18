class Student:
    def __init__(self, name, group, specialty):
        """Инициализация студента с его именем, группой и специальностью."""
        self._name = name
        self._group = group
        self._specialty = specialty

    def __str__(self):
        """Возвращает строковое представление студента."""
        return f"Имя: {self._name}, Группа: {self._group}, Специальность: {self._specialty}"

    @property
    def name(self):
        """Геттер для имени студента."""
        return self._name

    @name.setter
    def name(self, value):
        """Сеттер для имени студента."""
        self._name = value

    @property
    def group(self):
        """Геттер для группы студента."""
        return self._group

    @group.setter
    def group(self, value):
        """Сеттер для группы студента."""
        self._group = value

    @property
    def specialty(self):
        """Геттер для специальности студента."""
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        """Сеттер для специальности студента."""
        self._specialty = value

    def __eq__(self, other):
        """Сравнение студентов по имени."""
        if isinstance(other, Student):
            return self.name == other.name
        return False

    def __len__(self):
        """Возвращает длину имени студента."""
        return len(self.name)

    def __add__(self, other):
        """Складывает имена двух студентов."""
        if isinstance(other, Student):
            return self.name + " & " + other.name
        return NotImplemented

    @classmethod
    def from_string(cls, student_str):
        """Создает экземпляр Student из строки формата 'Имя, Группа, Специальность'."""
        name, group, specialty = map(str.strip, student_str.split(","))
        return cls(name, group, specialty)


if __name__ == "__main__":
    student1 = Student("Иван", "101", "Программирование")
    student2 = Student("Мария", "102", "Дизайн")

    print(student1)
    print(student2)

    student3 = Student.from_string("Алексей, 103, Архитектура")
    print(student3)
