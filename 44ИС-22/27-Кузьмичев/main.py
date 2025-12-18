from practice_manager import PracticeManager
from student import Student

def main():
    manager = PracticeManager()

    while True:
        print("\n1. Добавить студента")
        print("2. Сгенерировать отчет")
        print("3. Сохранить отчет в файл")
        print("4. Загрузить студентов из файла")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя студента: ")
            group = input("Введите группу: ")
            specialty = input("Введите специальность: ")
            student = Student(name, group, specialty)
            manager.add_student(student)
            print(f"Студент {name} добавлен.")

        elif choice == '2':
            report = manager.generate_report()
            if report:
                print(report)

        elif choice == '3':
            filename = input("Введите имя файла для сохранения отчета в ткст: ")
            manager.save_report_to_file(filename)

        elif choice == '4':
            filename = input("Введите имя файла для загрузки студентов в ткст: ")
            manager.load_students_from_file(filename)
            print("Студенты загружены из файла.")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()