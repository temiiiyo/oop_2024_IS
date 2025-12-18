import json
from datetime import datetime

# Класс Подразделение
class Department:
    def __init__(self, name, employees_count):
        self.name = name
        self.employees_count = employees_count

    def __add__(self, other):
        if isinstance(other, int):
            return Department(self.name, self.employees_count + other)
        raise ValueError("Можно добавлять только количество сотрудников (int).")

    def __sub__(self, other):
        if isinstance(other, int):
            new_count = max(0, self.employees_count - other)
            return Department(self.name, new_count)
        raise ValueError("Можно вычитать только количество сотрудников (int).")

    def __eq__(self, other):
        if isinstance(other, Department):
            return self.employees_count == other.employees_count
        return False

    def __lt__(self, other):
        if isinstance(other, Department):
            return self.employees_count < other.employees_count
        return False

    def __str__(self):
        return f"Подразделение {self.name} с {self.employees_count} сотрудниками."


class DataManager:
    @staticmethod
    def save_to_json(file, data):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def log_action(action):
        log_entry = f"{datetime.now()} - {action}\n"
        with open("log.txt", 'a', encoding='utf-8') as log_file:
            log_file.write(log_entry)


def main():
    departments_file = "departments.json"
    departments = []

    raw_data = DataManager.load_from_json(departments_file)
    for item in raw_data:
        departments.append(Department(item['name'], item['employees_count']))

    while True:
        print("\nМеню:")
        print("1. Показать все подразделения")
        print("2. Добавить подразделение")
        print("3. Изменить количество сотрудников")
        print("4. Сравнить подразделения")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСписок подразделений:")
            for dep in departments:
                print(dep)

        elif choice == "2":
            name = input("Введите название подразделения: ")
            count = int(input("Введите количество сотрудников: "))
            departments.append(Department(name, count))
            DataManager.log_action(f"Добавлено подразделение: {name} с {count} сотрудниками.")

        elif choice == "3":
            name = input("Введите название подразделения: ")
            found = next((dep for dep in departments if dep.name == name), None)
            if found:
                action = input("Добавить сотрудников (+) или Убрать (-): ")
                count = int(input("Введите количество: "))
                if action == "+":
                    departments[departments.index(found)] += count
                    DataManager.log_action(f"Добавлено {count} сотрудников в {name}.")
                elif action == "-":
                    departments[departments.index(found)] -= count
                    DataManager.log_action(f"Убрано {count} сотрудников из {name}.")
                else:
                    print("Неверное действие.")
            else:
                print("Подразделение не найдено.")

        elif choice == "4":
            name1 = input("Введите название первого подразделения: ")
            name2 = input("Введите название второго подразделения: ")
            dep1 = next((dep for dep in departments if dep.name == name1), None)
            dep2 = next((dep for dep in departments if dep.name == name2), None)
            if dep1 and dep2:
                if dep1 == dep2:
                    print("Подразделения равны по количеству сотрудников.")
                elif dep1 < dep2:
                    print(f"{dep1.name} имеет меньше сотрудников, чем {dep2.name}.")
                else:
                    print(f"{dep1.name} имеет больше сотрудников, чем {dep2.name}.")
                DataManager.log_action(f"Сравнение {name1} и {name2}.")
            else:
                print("Одно или оба подразделения не найдены.")

        elif choice == "5":
            # Сохранение данных
            data_to_save = [{'name': dep.name, 'employees_count': dep.employees_count} for dep in departments]
            DataManager.save_to_json(departments_file, data_to_save)
            print("Данные сохранены. Выход.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()