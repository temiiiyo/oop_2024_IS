from department import Department
from organization import Organization
from employee import Employee
""" 
Основной класс для запуска работы программы
и меню    
"""



def main_menu():
    organization = None

    while True:
        print("\nМеню:")
        print("1. Создать организацию")
        print("2. Добавить отдел")
        print("3. Добавить работника")
        print("4. Удалить работника")
        print("5. Сравнить отделы")
        print("6. Сохранить данные в файл")
        print("7. Загрузить данные из файла")
        print("8. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            name = input("Введите имя организации: ")
            organization = Organization(name)
            print(f"Организация {organization.name} создана.")

        elif choice == "2":
            if organization:
                name = input("Введите имя отдела: ")
                department = Department(name)
                organization.add_department(department)
            else:
                print("Сначала создайте организацию.")

        elif choice == "3":
            if organization:
                department_name = input("Введите имя отдела для добавления работника: ")
                department = next((d for d in organization.departments if d.name == department_name), None)
                if department:
                    worker_name = input("Введите имя работника: ")
                    worker_position = input("Введите должность работника: ")
                    worker = Employee(worker_name, worker_position)
                    department.add_employee(worker)
                else:
                    print("Отдел не найден.")
            else:
                print("Сначала создайте организацию.")

        elif choice == "4":
            if organization:
                department_name = input("Введите имя отдела для удаления работника: ")
                department = next((d for d in organization.departments if d.name == department_name), None)
                if department:
                    worker_name = input("Введите имя работника для удаления: ")
                    worker = next((e for e in department.employees if e.name == worker_name), None)
                    if worker:
                        department.remove_employee(worker)
                    else:
                        print("Работник не найден.")
                else:
                    print("Отдел не найден.")
            else:
                print("Сначала создайте организацию.")

        elif choice == "5":
            if organization:
                section1_name = input("Введите имя первого отдела: ")
                section2_name = input("Введите имя второго отдела: ")
                section1 = next((d for d in organization.departments if d.name == section1_name), None)
                section2 = next((d for d in organization.departments if d.name == section2_name), None)
                if section1 and section2:
                    if section1 < section2:
                        print(f"Отдел {section1.name} имеет меньше работников, чем {section2.name}.")
                    else:
                        print(f"Отдел {section1.name} имеет больше или столько же работников, сколько {section2.name}.")
                else:
                    print("Один из отделов не найден.")
            else:
                print("Сначала создайте организацию.")

        elif choice == "6":
            if organization:
                organization.save_to_file()
                for department in organization.departments:
                    department.save_to_file()
                print("Данные сохранены.")
            else:
                print("Сначала создайте организацию.")

        elif choice == "7":
            name = input("Введите имя организации для загрузки: ")
            organization = Organization(name)
            organization.load_from_file()
            print("Данные загружены.")

        elif choice == "8":
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main_menu()
